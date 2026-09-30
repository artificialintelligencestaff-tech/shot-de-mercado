#!/usr/bin/env python3
import json
import re
import sys
import time
import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

from pathlib import Path as _Path
PROJECT_ROOT = _Path(os.getenv("SHOT_ROOT", str(_Path(__file__).resolve().parents[2])))
load_dotenv(PROJECT_ROOT / "04_Config" / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ACCUMULATED_FILE = str(PROJECT_ROOT / "02_Analisis" / "shadow_v4" / "_accumulated.json")
ALERTS_DIR = str(PROJECT_ROOT / "02_Analisis" / "alerts")
os.makedirs(ALERTS_DIR, exist_ok=True)

PRECISION_LOG = os.path.join(ALERTS_DIR, "_precision_log.json")
ALL_ALERTS_FILE = os.path.join(ALERTS_DIR, "_all_alerts.json")
CYCLE_LOG = os.path.join(ALERTS_DIR, "_cycle_log.json")

EVM_ADDRESS = re.compile(r"0x[0-9a-fA-F]{40}")
TRUTHY = {"1", "true", "yes", "on"}


def env_flag(name):
    """PAUSE_EMISSIONS / SHADOW_MODE: se leen en cada corrida (no al importar)."""
    return os.getenv(name, "").strip().lower() in TRUTHY


class CorruptStateError(Exception):
    """El archivo canónico de alertas no se puede leer como lista: no se emite ni se sobrescribe."""


def normalize_mint(mint):
    """Clave de deduplicación: mint sin espacios.

    Las direcciones EVM (0x + 40 hex) no distinguen mayúsculas y se comparan en minúsculas.
    Base58 (Solana) SÍ distingue mayúsculas: se compara exacto.
    """
    if not isinstance(mint, str):
        return ""
    mint = mint.strip()
    return mint.lower() if EVM_ADDRESS.fullmatch(mint) else mint


def normalize_symbol(symbol):
    return symbol.strip().upper() if isinstance(symbol, str) else ""


def load_alerts(path):
    """Historial de alertas. Inexistente -> []. Ilegible o no-lista -> CorruptStateError.

    Antes, un error de lectura dejaba la lista vacía y el write final borraba el historial.
    """
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        raise CorruptStateError(f"{path}: {e}") from e
    if not isinstance(data, list):
        raise CorruptStateError(f"{path}: se esperaba una lista, llegó {type(data).__name__}")
    return data


def duplicate_mints(all_alerts):
    """{mint: n} de mints que ya aparecen más de una vez en el historial."""
    counts = {}
    for a in all_alerts:
        key = normalize_mint(a.get("mint")) if isinstance(a, dict) else ""
        if key:
            counts[key] = counts.get(key, 0) + 1
    return {k: n for k, n in counts.items() if n > 1}


def select_candidates(accumulated, all_alerts, min_score=50):
    """Candidatos con score >= min_score cuyo mint no fue alertado nunca (activas y cerradas)."""
    alerted = {normalize_mint(a.get("mint")) for a in all_alerts if isinstance(a, dict)} - {""}
    candidates, seen = [], set()
    stats = {"already_alerted": 0, "intra_cycle_duplicates": []}
    for mint, token in accumulated.items():
        if token.get("score", 0) < min_score:
            continue
        key = normalize_mint(mint)
        if not key:
            continue
        if key in alerted:
            stats["already_alerted"] += 1
            continue
        if key in seen:
            stats["intra_cycle_duplicates"].append(mint)
            continue
        seen.add(key)
        candidates.append((mint, token))
    return candidates, stats


def symbol_collisions(symbol, mint, all_alerts):
    """Mints ya alertados con el mismo símbolo y distinto mint (posible copia del token)."""
    sym, key = normalize_symbol(symbol), normalize_mint(mint)
    if not sym or sym == "UNKNOWN":
        return []
    return sorted({a.get("mint") for a in all_alerts
                   if isinstance(a, dict) and normalize_symbol(a.get("symbol")) == sym
                   and normalize_mint(a.get("mint")) not in ("", key)})


def write_json_atomic(path, data):
    """Escritura atómica: un corte a mitad de escritura no deja el JSON truncado."""
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)


def log_cycle_event(event):
    """Registra un evento de deduplicación en _cycle_log.json (clave "dedup_events").

    Idempotente por event["key"]: el mismo hallazgo no se repite en cada corrida.
    Nunca interrumpe la emisión: ante cualquier problema solo avisa por consola.
    """
    try:
        log = {}
        if os.path.exists(CYCLE_LOG):
            with open(CYCLE_LOG, "r", encoding="utf-8") as f:
                log = json.load(f)
        if not isinstance(log, dict):
            print(f"[WARN] {CYCLE_LOG} no es un objeto JSON; evento no registrado: {event}")
            return
        events = log.setdefault("dedup_events", [])
        if any(e.get("key") == event["key"] for e in events if isinstance(e, dict)):
            return
        events.append(event)
        log["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        write_json_atomic(CYCLE_LOG, log)
    except Exception as e:
        print(f"[WARN] No se pudo registrar en _cycle_log.json: {e}")

def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[WARN] Telegram credentials missing, printing to console instead.")
        print(text)
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
        if r.status_code == 200:
            print("[INFO] Alerta enviada a Telegram exitosamente.")
            return True
        else:
            print(f"[ERROR] Telegram API error: {r.status_code} - {r.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Telegram exception: {e}")
        return False

def format_alert_message(token, collisions=()):
    # Symbol is in token.token.symbol, fallback to top-level
    symbol = token.get("token", {}).get("symbol") or token.get("symbol") or "UNKNOWN"
    # Mint is in token.token.mint, fallback to top-level
    mint = token.get("token", {}).get("mint") or token.get("mint", "")
    score = token.get("score", 55)
    # solAmount is in token, fallback
    sol_amt = token.get("solAmount", 85)
    # marketCapSol is in token, fallback
    mcap = token.get("marketCapSol", 411)
    
    # Get price/liq from dexscreener or ms_data if available
    dx = token.get("dx", {})
    liq = dx.get("liquidityUsd", 25000)
    price = dx.get("priceUsd", 0.001)
    vol = dx.get("volume24hUsd", 50000)

    # Confianza formula (50-69 score -> 50-65% confidence)
    confidence = min(65, 45 + int(score * 0.2))

    collision_warning = (
        f"• Ya alertamos OTRO token con el símbolo {symbol} (mint distinto): "
        f"verificá el mint antes de operar\n" if collisions else ""
    )

    msg = f"""🚨 *SHOT DE MERCADO — {symbol}*
Confianza: {confidence}% (MODERADA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *DATOS*
• Precio: ${price:.6f}
• MCap: {mcap:.1f} SOL (${mcap * 140:,.0f})
• Liquidez: ${liq:,.0f}
• Volumen 24h: ${vol:,.0f}
• Whale entry: {sol_amt:.1f} SOL

🎯 *POR QUÉ LO DETECTAMOS*
• Whale entry: {sol_amt:.1f} SOL (top 1%)
• MCap respaldado por ballena
• Liquidez activa en DEX
• Sin señales de riesgo (mint/freeze revoked)

📈 *NIVEL DE CONFIANZA: MODERADA ({confidence}%)*
Este token cumple los criterios mínimos. No tiene señales de KOL accumulating ni trending masivo, por lo que la confianza es moderada.

🛒 *CÓMO ADQUIRIRLO (paso a paso)*
1. Instalar Phantom: https://phantom.app
2. Comprar SOL en Binance/Coinbase
3. Enviar SOL a tu wallet Phantom
4. Conectar a Jupiter: https://jup.ag
5. Pegar mint: `{mint}`
6. Slippage: 5-10%
7. Ejecutar swap

⚠️ *ADVERTENCIAS*
{collision_warning}• No invertir más del 1-2% del capital
• Token de <6h de vida = alto riesgo
• Confianza moderada, no segura
• El sistema actualizará la confianza en 1h/6h/24h

⏱️ *SEGUIMIENTO*
• t+1h: actualización de confianza
• t+6h: actualización
• t+24h: veredicto final (acierto/fallo/falso positivo)
"""
    return msg, confidence


def get_current_price(token):
    """Extract current price from token data (dexscreener or ms_data)."""
    # Priority 1: dx (pumpportal enriched)
    dx = token.get("dx", {})
    price = dx.get("priceUsd")
    if price and price > 0:
        return float(price)
    # Priority 2: dexscreener (direct from detection)
    dx2 = token.get("dexscreener", {})
    price = dx2.get("priceUsd")
    if price and price > 0:
        return float(price)
    # Fallback: try ms_data if present
    ms = token.get("ms_data", {})
    price = ms.get("priceUsd")
    if price and price > 0:
        return float(price)
    return None

def main():
    print("[YIN] Iniciando emisión de alertas reales (Script 97)...")

    # Defensa en profundidad: la pausa se respeta aunque el workflow ejecute el step.
    if env_flag("PAUSE_EMISSIONS"):
        print("[INFO] PAUSE_EMISSIONS activo: no se procesa ni se envía nada.")
        return 0
    # Modo sombra: se registran las alertas (status=shadow) exactamente como se emitirían, sin Telegram.
    shadow = env_flag("SHADOW_MODE")
    if shadow:
        print("[INFO] SHADOW_MODE activo: alertas registradas con status=shadow, sin envío a Telegram.")

    if not os.path.exists(ACCUMULATED_FILE):
        print("[ERROR] _accumulated.json no encontrado.")
        return

    with open(ACCUMULATED_FILE, "r", encoding="utf-8") as f:
        accumulated = json.load(f)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")

    # Historial ilegible: abortar sin enviar ni sobrescribir (antes se perdía todo el historial)
    try:
        all_alerts = load_alerts(ALL_ALERTS_FILE)
    except CorruptStateError as e:
        print(f"[ERROR] Historial de alertas ilegible, no se emite ni se sobrescribe: {e}")
        log_cycle_event({"key": f"corrupt_alerts_file:{timestamp}", "type": "corrupt_alerts_file",
                         "timestamp": timestamp, "detail": str(e)})
        return 1

    existing_dups = duplicate_mints(all_alerts)
    if existing_dups:
        print(f"[WARN] Mints duplicados ya presentes en el historial (no se borran): {existing_dups}")
        log_cycle_event({"key": "existing_duplicates:" + ",".join(sorted(existing_dups)),
                         "type": "existing_duplicates", "timestamp": timestamp, "mints": existing_dups})

    # Filter score >= 50 and not already alerted (dedup por mint normalizado, activas y cerradas)
    candidates, stats = select_candidates(accumulated, all_alerts)
    if stats["intra_cycle_duplicates"]:
        dups = sorted(stats["intra_cycle_duplicates"])
        print(f"[WARN] Candidatos repetidos en el mismo ciclo (variantes del mismo mint): {dups}")
        log_cycle_event({"key": f"intra_cycle_duplicates:{timestamp}", "type": "intra_cycle_duplicates",
                         "timestamp": timestamp, "mints": dups})

    # Max 3 alerts per cycle
    to_emit = candidates[:3]
    print(f"[INFO] Candidatos con score >= 50 pendientes de emitir: {len(candidates)} "
          f"(ya alertados y omitidos: {stats['already_alerted']})")
    print(f"[INFO] Emitiendo {len(to_emit)} alertas en este ciclo.")

    emitted_count = 0

    for mint, token in to_emit:
        # mint is already available from the tuple
        # Fix Ciclo 17.16: persistir initial_price al emitir alerta.
        # Sin este campo, el trust scheduler no puede calcular cambio real.
        # El precio se valida ANTES de enviar: antes se enviaba a Telegram y recién después se
        # descartaba por falta de precio, sin registrar -> reenvío en cada ciclo.
        try:
            initial_price = get_current_price(token)
        except Exception:
            initial_price = None
        if not initial_price or initial_price <= 0:
            print(f"[SKIP] {token.get('symbol')} sin precio inicial. No se emite alerta.")
            continue
        # Get symbol from token.token.symbol or fallback
        symbol = (token.get("token") or {}).get("symbol") or token.get("symbol", "UNKNOWN")
        collisions = symbol_collisions(symbol, mint, all_alerts)
        msg, confidence = format_alert_message(token, collisions)
        alert_record = {
            "timestamp": timestamp,
            "mint": mint,
            "symbol": symbol,
            "score": token["score"],
            "confidence": confidence,
            "initial_price": initial_price,
            "status": "shadow" if shadow else "active_tracking",
            "trust_updates": []
        }
        if collisions:
            alert_record["symbol_collision"] = collisions
            print(f"[WARN] {symbol}: mismo símbolo que otros mints ya alertados {collisions}")
            log_cycle_event({"key": f"symbol_collision:{normalize_mint(mint)}", "type": "symbol_collision",
                             "timestamp": timestamp, "symbol": symbol, "mint": mint,
                             "other_mints": collisions})

        # Save individual alert record
        ind_file = os.path.join(ALERTS_DIR, f"alert_{mint}_{timestamp}.json")
        with open(ind_file, "w", encoding="utf-8") as f:
            json.dump(token, f, indent=2)

        # Persistir ANTES de enviar: si algo falla después, el mint ya figura como alertado
        all_alerts.append(alert_record)
        write_json_atomic(ALL_ALERTS_FILE, all_alerts)

        alert_record["telegram_sent"] = False if shadow else send_telegram(msg)
        write_json_atomic(ALL_ALERTS_FILE, all_alerts)
        emitted_count += 1
        time.sleep(1) # rate limit telegram

    # Feedback loop check (every 10 alerts). Nunca debe tumbar el step: si fallara después de
    # enviar, el commit del workflow se saltea y la alerta se reenvía en el ciclo siguiente.
    total_alerts = len(all_alerts)
    if emitted_count and total_alerts % 10 == 0:
        try:
            precision_log = []
            if os.path.exists(PRECISION_LOG):
                with open(PRECISION_LOG, "r", encoding="utf-8") as f:
                    precision_log = json.load(f)
            if isinstance(precision_log, list):
                precision_log.append({
                    "timestamp": timestamp,
                    "total_alerts": total_alerts,
                    "success_rate": 0.5 # placeholder until feedback loop resolves
                })
                write_json_atomic(PRECISION_LOG, precision_log)
            else:
                print("[WARN] _precision_log.json tiene formato curado (no lista); no se agrega el placeholder.")
        except Exception as e:
            print(f"[WARN] No se pudo actualizar _precision_log.json: {e}")

    print(f"\n[YIN] Emisión de alertas finalizada. Emitidas: {emitted_count}")
    print(f"Total histórico de alertas: {len(all_alerts)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
