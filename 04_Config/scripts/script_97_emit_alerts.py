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
# Grupo de usuarios finales (opcional). Si está definido, cada alerta de mercado va también ahí.
# No confundir con TELEGRAM_OPS_CHAT_ID ("La mano de Dios"), que solo recibe avisos de los bots.
TELEGRAM_PUBLIC_CHAT_ID = os.getenv("TELEGRAM_PUBLIC_CHAT_ID")
ACCUMULATED_FILE = str(PROJECT_ROOT / "02_Analisis" / "shadow_v4" / "_accumulated.json")
ALERTS_DIR = str(PROJECT_ROOT / "02_Analisis" / "alerts")
os.makedirs(ALERTS_DIR, exist_ok=True)

PRECISION_LOG = os.path.join(ALERTS_DIR, "_precision_log.json")
ALL_ALERTS_FILE = os.path.join(ALERTS_DIR, "_all_alerts.json")
CYCLE_LOG = os.path.join(ALERTS_DIR, "_cycle_log.json")

EVM_ADDRESS = re.compile(r"0x[0-9a-fA-F]{40}")
TRUTHY = {"1", "true", "yes", "on"}
# v7.2.1 (19_CALIBRACION_V72.md): con el gate de edad la distribución es bimodal; 56 es el primer
# umbral que deja afuera el grupo de tokens jóvenes (heurístico, pendiente de validar con la métrica dual).
EMIT_MIN_SCORE = 56
# R1: antigüedad máxima del scoring de un candidato. Evita que el modo sombra/emisión recorra el
# atraso de _accumulated.json (269 candidatos v7.2 el 30/09) con precios de detección viejos.
CANDIDATE_MAX_AGE_MIN = 60
# Edad mínima del par para emitir (Dirección, 30/09): la exposición a tokens recién nacidos debe ser
# < 20%. Sin edad conocida (sin pairCreatedAt) no se emite.
EMIT_MIN_AGE_MIN = 30
# Métrica post +20% que se muestra SIEMPRE como dato, junto a primaria y secundaria (sin advertencia ni
# consejo: el proyecto informa, el usuario decide). Hasta que exista calibración validada del scorer que
# emite, se usa la cifra histórica medida (21_INSIGHT_84_RUG.md: legado v7.1, score >= 56, 16/21).
HISTORICAL_RUG_AFTER_HIT = {"rate": 0.762, "n": 21, "source": "histórico v7.1, score ≥ 56"}


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


def is_fresh(token, now, max_age_min):
    """R1: solo candidatos puntuados en los últimos `max_age_min` minutos (campo detected_at de script_82).
    Sin detected_at (atraso anterior a R1) = no fresco."""
    try:
        detected = datetime.fromisoformat(token["detected_at"]).timestamp()
    except (KeyError, TypeError, ValueError):
        return False
    return now - detected <= max_age_min * 60


def pair_age_min(token, now):
    """Edad del par en minutos a `now`, desde dexscreener.pairCreatedAt (ms). None si no se conoce."""
    dx = token.get("dexscreener") or token.get("dx") or {}
    created = dx.get("pairCreatedAt")
    if not isinstance(created, (int, float)) or isinstance(created, bool) or created <= 0:
        return None
    return (now - created / 1000) / 60


def select_candidates(accumulated, all_alerts, min_score=EMIT_MIN_SCORE, max_age_min=CANDIDATE_MAX_AGE_MIN,
                      now=None, min_age_min=EMIT_MIN_AGE_MIN):
    """Candidatos con score >= min_score, frescos, con edad >= min_age_min y cuyo mint no fue alertado nunca."""
    alerted = {normalize_mint(a.get("mint")) for a in all_alerts if isinstance(a, dict)} - {""}
    now = time.time() if now is None else now
    candidates, seen = [], set()
    stats = {"already_alerted": 0, "intra_cycle_duplicates": [], "stale_or_undated": 0,
             "too_young_or_unknown_age": []}
    for mint, token in accumulated.items():
        if token.get("score", 0) < min_score:
            continue
        if max_age_min is not None and not is_fresh(token, now, max_age_min):
            stats["stale_or_undated"] += 1
            continue
        if min_age_min is not None:
            age = pair_age_min(token, now)
            if age is None or age < min_age_min:
                stats["too_young_or_unknown_age"].append(
                    {"mint": mint, "age_min": round(age, 1) if age is not None else None,
                     "reason": f"age<{min_age_min}min" if age is not None else "edad desconocida"})
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

def telegram_destinations():
    """Destinos de las alertas de mercado: el chat personal (TELEGRAM_CHAT_ID) y, si está definido, el grupo
    de usuarios (TELEGRAM_PUBLIC_CHAT_ID). Sin grupo = comportamiento anterior. Un mismo chat_id no se repite."""
    dests = []
    for label, chat_id in (("personal", TELEGRAM_CHAT_ID), ("grupo", TELEGRAM_PUBLIC_CHAT_ID)):
        chat_id = (chat_id or "").strip()
        if chat_id and all(chat_id != c for _, c in dests):
            dests.append((label, chat_id))
    return dests


def send_telegram_to(label, chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
        if r.status_code == 200:
            print(f"[INFO] Alerta enviada a Telegram ({label}).")
            return True
        print(f"[ERROR] Telegram API error ({label}): {r.status_code} - {r.text}")
        return False
    except Exception as e:
        print(f"[ERROR] Telegram exception ({label}): {e}")
        return False


def send_telegram(text):
    """Envía la alerta a todos los destinos. True si al menos uno la recibió: así el mint queda registrado
    como enviado y no se reintenta en cada ciclo (la falla de un destino queda en el log del workflow)."""
    dests = telegram_destinations()
    if not TELEGRAM_BOT_TOKEN or not dests:
        print("[WARN] Telegram credentials missing, printing to console instead.")
        print(text)
        return False
    results = [send_telegram_to(label, chat_id, text) for label, chat_id in dests]
    return any(results)

def load_emission_calibration(path=None):
    """Probabilidades VALIDADAS (métrica dual) del scorer/umbral que emiten.

    Archivo 02_Analisis/diagnostics/emission_calibration.json con validated=true. Sin archivo, ilegible
    o sin validar -> None, y el mensaje dice "en validación": nunca se muestran cifras no validadas.
    """
    path = path or os.path.join(str(PROJECT_ROOT), "02_Analisis", "diagnostics", "emission_calibration.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("validated") is not True:
        return None
    try:
        for key in ("primary", "secondary", "rug_after_primary_hit"):
            float(data[key]["rate"])
            float(data[key]["ci90"][0]), float(data[key]["ci90"][1])
    except (KeyError, TypeError, ValueError, IndexError):
        return None
    return data


def _num(value):
    try:
        return float(value) if value is not None and not isinstance(value, bool) else None
    except (TypeError, ValueError):
        return None


def market_snapshot(token):
    """Datos reales del token al detectarlo: DexScreener (script_82) o el formato viejo 'dx'.
    Lo que falta queda en None: el mensaje muestra "n/d", nunca un valor por defecto."""
    dx = token.get("dexscreener") or token.get("dx") or {}
    tok = token.get("token") or {}
    return {"price": _num(dx.get("priceUsd")), "liquidity": _num(dx.get("liquidityUsd")),
            "volume_24h": _num(dx.get("volume24hUsd")), "mcap_usd": _num(dx.get("marketCapUsd")),
            "sol_amount": _num(tok.get("solAmount", token.get("solAmount")))}


# El pipeline de script_82 es Solana; un token de otra cadena trae "chain" (multi-chain, doc 23).
DEFAULT_CHAIN = "solana"
CHAIN_LABELS = {"solana": "Solana", "base": "Base", "ethereum": "Ethereum", "blast": "Blast", "monad": "Monad"}
# Exploradores por cadena (nombre, URL). Cadena sin explorador conocido = sin link (no se inventa).
EXPLORERS = {"solana": ("Solscan", "https://solscan.io/token/{addr}"),
             "base": ("BaseScan", "https://basescan.org/token/{addr}"),
             "ethereum": ("Etherscan", "https://etherscan.io/token/{addr}"),
             "blast": ("BlastScan", "https://blastscan.io/token/{addr}")}
DEXSCREENER_CHAINS = {"solana", "base", "ethereum", "blast"}
SIGNAL_WINDOW_H = 48   # horizonte de la métrica dual: la señal se evalúa dentro de las 48 h


def md(text):
    """Escapa '_', '*', '`' y '[' (Markdown de Telegram) en datos externos: un '_' en un nombre o en un
    motivo rompía el parseo y la API rechazaba el mensaje entero."""
    return re.sub(r"([_*`\[])", r"\\\1", str(text))


def detection_facts(token):
    """Identificación y tiempos de la detección. Lo desconocido queda en None ("n/d" en el mensaje)."""
    tok = token.get("token") or {}
    dx = token.get("dexscreener") or token.get("dx") or {}
    created = dx.get("pairCreatedAt")
    created_dt = (datetime.fromtimestamp(created / 1000, timezone.utc)
                  if isinstance(created, (int, float)) and not isinstance(created, bool) and created > 0 else None)
    try:
        detected_dt = datetime.fromisoformat(token["detected_at"])
        if detected_dt.tzinfo is None:
            detected_dt = detected_dt.replace(tzinfo=timezone.utc)
    except (KeyError, TypeError, ValueError):
        detected_dt = None
    age = ((detected_dt - created_dt).total_seconds() / 60
           if detected_dt and created_dt and detected_dt >= created_dt else None)
    return {"name": tok.get("name") or token.get("name"),
            "chain": str(token.get("chain") or dx.get("chainId") or DEFAULT_CHAIN).lower(),
            "creator": tok.get("traderPublicKey") or tok.get("creator"), "pool": tok.get("pool"),
            "pair": dx.get("pairAddress"), "created": created_dt, "detected": detected_dt, "age_min": age}


def source_links(mint, facts):
    """Fuentes externas verificables: explorador de la cadena, DexScreener y la página oficial del lanzamiento."""
    links, chain = [], facts["chain"]
    if mint and chain in EXPLORERS:
        label, url = EXPLORERS[chain]
        links.append((label, url.format(addr=mint)))
    if chain in DEXSCREENER_CHAINS and (facts["pair"] or mint):
        links.append(("DexScreener", f"https://dexscreener.com/{chain}/{facts['pair'] or mint}"))
    if facts["pool"] == "pump" and mint:
        links.append(("pump.fun (página del lanzamiento)", f"https://pump.fun/coin/{mint}"))
    return links


def format_alert_message(token, collisions=(), calibration=None):
    # Symbol is in token.token.symbol, fallback to top-level
    symbol = (token.get("token") or {}).get("symbol") or token.get("symbol") or "UNKNOWN"
    # Mint is in token.token.mint, fallback to top-level
    mint = (token.get("token") or {}).get("mint") or token.get("mint", "")
    score = token.get("score", 0)

    # Confianza heredada (solo se guarda en el registro para script_98; no se muestra: no está calibrada)
    confidence = min(65, 45 + int(score * 0.2))

    snap = market_snapshot(token)

    def show(value, fmt):
        return fmt.format(value) if value is not None else "n/d"

    def pct(x):
        return f"{x * 100:.0f}%"

    if calibration:
        p, s, r = calibration["primary"], calibration["secondary"], calibration["rug_after_primary_hit"]
        probabilities = (
            f"🎯 *PROBABILIDADES* (scoring v{calibration.get('scoring_version', '?')}, "
            f"score ≥ {calibration.get('threshold', '?')}, n={p.get('n', '?')})\n"
            f"• Tocar +20% antes de caer −30% (≤48 h): {pct(p['rate'])} (IC90: {pct(p['ci90'][0])}–{pct(p['ci90'][1])})\n"
            f"• Cerrar ≥ +20% a las 48 h (mantener): {pct(s['rate'])} (IC90: {pct(s['ci90'][0])}–{pct(s['ci90'][1])})\n"
            f"• Después de tocar +20%, llegar a ≤ −99% (≤48 h): {pct(r['rate'])} "
            f"(IC90: {pct(r['ci90'][0])}–{pct(r['ci90'][1])}, n={r.get('n', '?')})\n"
        )
    else:
        probabilities = "🎯 *PROBABILIDADES*: en validación (todavía no hay cifras calibradas para este scoring)\n"
        r = HISTORICAL_RUG_AFTER_HIT
        probabilities += f"• Histórico ({r['source']}, n={r['n']}): después de tocar +20%, el {pct(r['rate'])} llegó a ≤ −99% dentro de las 48 h\n"

    # Dato de identificación (no advertencia): otro token ya alertado comparte el símbolo
    collision_line = (
        f"• Símbolo compartido: ya se alertó OTRO token {md(symbol)} con mint distinto\n" if collisions else ""
    )
    reasons = [r for r in token.get("reasons", []) if not str(r).startswith("v7.2.1:")][:4]
    reasons_block = "".join(f"• {md(r)}\n" for r in reasons) or "• n/d\n"
    sol_line = f"• Compra inicial del creador: {snap['sol_amount']:.2f} SOL\n" if snap["sol_amount"] is not None else ""

    facts = detection_facts(token)

    def when(dt):
        return dt.strftime("%d/%m/%Y %H:%M UTC") if dt else "n/d"

    age = facts["age_min"]
    age_text = "n/d" if age is None else (f"{age:.0f} min" if age < 120 else f"{age / 60:.1f} h")
    name_text = f"{md(facts['name'])} ({md(symbol)})" if facts["name"] else "n/d"
    chain_text = CHAIN_LABELS.get(facts["chain"], facts["chain"])
    mint_text = f"`{mint}`" if mint else "n/d"
    creator_line = f"• Creador: `{facts['creator']}`\n" if facts["creator"] else ""
    links_block = "".join(f"• {label}: {url}\n" for label, url in source_links(mint, facts)) or "• n/d\n"

    msg = f"""🚨 *SHOT DE MERCADO* — {md(symbol)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🪪 *ACTIVO*
• Nombre: {name_text}
• Chain: {chain_text}
• Mint: {mint_text}
{creator_line}
🕒 *DETECCIÓN*
• Detectado: {when(facts['detected'])}
• Edad del par al detectar: {age_text}
• Par creado: {when(facts['created'])}
• Ventana operativa: < {SIGNAL_WINDOW_H} h desde la detección

{probabilities}
📊 *DATOS (DexScreener, al detectar)*
• Precio: {show(snap['price'], '${:.8g}')}
• MCap: {show(snap['mcap_usd'], '${:,.0f}')}
• Liquidez: {show(snap['liquidity'], '${:,.0f}')}
• Volumen 24h: {show(snap['volume_24h'], '${:,.0f}')}
{sol_line}{collision_line}
🔎 *POR QUÉ LO DETECTAMOS* (score {score})
{reasons_block}
🛒 *CÓMO ADQUIRIRLO (paso a paso)*
1. Instalar Phantom: https://phantom.app
2. Comprar SOL en Binance/Coinbase
3. Enviar SOL a tu wallet Phantom
4. Conectar a Jupiter: https://jup.ag
5. Pegar mint (verificá que coincida): `{mint}`
6. Slippage: 5-10%
7. Ejecutar swap

🔗 *FUENTES VERIFICABLES*
{links_block}
⏱️ *SEGUIMIENTO*
• t+1h, t+6h y t+24h: actualización del precio contra la entrada
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
    calibration = load_emission_calibration()
    if calibration is None:
        print("[INFO] Sin calibración validada: el mensaje muestra las probabilidades como 'en validación'.")

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

    # Filter score >= EMIT_MIN_SCORE and not already alerted (dedup por mint normalizado, activas y cerradas)
    candidates, stats = select_candidates(accumulated, all_alerts)
    if stats["intra_cycle_duplicates"]:
        dups = sorted(stats["intra_cycle_duplicates"])
        print(f"[WARN] Candidatos repetidos en el mismo ciclo (variantes del mismo mint): {dups}")
        log_cycle_event({"key": f"intra_cycle_duplicates:{timestamp}", "type": "intra_cycle_duplicates",
                         "timestamp": timestamp, "mints": dups})

    # Max 3 alerts per cycle
    to_emit = candidates[:3]
    print(f"[INFO] Candidatos con score >= {EMIT_MIN_SCORE} pendientes de emitir: {len(candidates)} "
          f"(ya alertados y omitidos: {stats['already_alerted']}; "
          f"sin scoring en los últimos {CANDIDATE_MAX_AGE_MIN} min: {stats['stale_or_undated']}; "
          f"edad < {EMIT_MIN_AGE_MIN} min o desconocida: {len(stats['too_young_or_unknown_age'])})")
    for skip in stats["too_young_or_unknown_age"][:5]:
        print(f"[SKIP] {skip['mint'][:10]}... {skip['reason']} (edad: {skip['age_min']})")
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
        msg, confidence = format_alert_message(token, collisions, calibration)
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