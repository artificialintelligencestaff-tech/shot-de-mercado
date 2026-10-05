#!/usr/bin/env python3
import importlib.util
import json
import re
import sys
import time
import requests
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

from pathlib import Path as _Path
PROJECT_ROOT = _Path(os.getenv("SHOT_ROOT", str(_Path(__file__).resolve().parents[2])))
load_dotenv(PROJECT_ROOT / "04_Config" / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# Destino ÚNICO de las alertas de mercado: el grupo (TELEGRAM_PUBLIC_CHAT_ID). El chat personal
# (TELEGRAM_CHAT_ID) está deprecado (Dirección, 30/09): este script ya no lo lee, así que no recibe nada
# aunque el secret exista. Los avisos de sistema van por TELEGRAM_OPS_CHAT_ID (bots, lib_ops).
# El bot es solo emisor: no lee updates ni comandos de nadie.
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
             "too_young_or_unknown_age": [], "group_i_registered": 0}
    for mint, token in accumulated.items():
        if token.get("score", 0) < min_score:
            continue
        if token.get("group") == "i":          # Fase 8: establecido sin grupo (par > 180 días): registro, no emisión
            stats["group_i_registered"] += 1
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
    """Destino de las alertas de mercado: solo el grupo (TELEGRAM_PUBLIC_CHAT_ID). Sin grupo = ningún destino
    (send_telegram imprime el mensaje en consola y no envía)."""
    chat_id = (TELEGRAM_PUBLIC_CHAT_ID or "").strip()
    return [("grupo", chat_id)] if chat_id else []


TELEGRAM_PAUSE_S = 0.5   # pausa entre destinos si alguna vez hay más de uno (rate limit de Telegram)


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
            print(f"[INFO] Mensaje enviado a Telegram ({label}).")
            return True
        print(f"[ERROR] Telegram API error ({label}): {r.status_code} - {r.text}")
        return False
    except Exception as e:
        print(f"[ERROR] Telegram exception ({label}): {e}")
        return False


def send_to_destinations(text):
    """Envía `text` a cada destino, con una pausa entre envíos. Devuelve [(destino, ok)]; [] sin credenciales."""
    dests = telegram_destinations()
    if not TELEGRAM_BOT_TOKEN or not dests:
        return []
    results = []
    for i, (label, chat_id) in enumerate(dests):
        if i:
            time.sleep(TELEGRAM_PAUSE_S)
        results.append((label, send_telegram_to(label, chat_id, text)))
    return results


def send_telegram(text):
    """Envía la alerta a todos los destinos. True si al menos uno la recibió: así el mint queda registrado
    como enviado y no se reintenta en cada ciclo (la falla de un destino queda en el log del workflow)."""
    results = send_to_destinations(text)
    if not results:
        print("[WARN] Sin TELEGRAM_PUBLIC_CHAT_ID o sin token: no se envía; mensaje por consola.")
        print(text)
        return False
    return any(ok for _, ok in results)


TELEGRAM_CAPTION_LIMIT = 1024   # límite de Telegram para el caption de un documento
CAPTION_SUFFIX = "\n📎 Alerta completa y estudio de adquisición en el adjunto."
ACQUISITION_MARK = "CÓMO ADQUIRIRLO"


def _markdown_balanced(text):
    """True si los '*', '_' y '`' sin escapar están cerrados (Markdown legacy de Telegram)."""
    unescaped = re.sub(r"\\.", "", text)
    return all(unescaped.count(ch) % 2 == 0 for ch in "*_`")


def _cut_lines(text, budget):
    """Corte en el último salto de línea que entra en `budget` y deja el Markdown balanceado."""
    lines = text[:budget].split("\n")[:-1]   # descarta la línea cortada a la mitad
    while lines and not _markdown_balanced("\n".join(lines)):
        lines.pop()
    return "\n".join(lines).rstrip()


def document_caption(text, limit=TELEGRAM_CAPTION_LIMIT):
    """Caption del dossier: la alerta entera si entra en `limit`. Si no, se arma por bloques (separados por línea
    en blanco): encabezado + bloque 🛒 COMPLETO siempre (regla núcleo) + el resto, en el orden del mensaje,
    mientras entren enteros; al final, la referencia al adjunto. Nunca supera `limit` ni corta una entidad
    Markdown (Telegram rechazaría el envío). Si ni el 🛒 entra, se corta por líneas."""
    if len(text) <= limit:
        return text
    budget = limit - len(CAPTION_SUFFIX)
    head, *blocks = [b for b in text.split("\n\n") if b.strip()]
    order = sorted(range(len(blocks)), key=lambda i: ACQUISITION_MARK not in blocks[i])   # el 🛒 primero
    chosen, size = set(), len(head)
    for i in order:
        if size + 2 + len(blocks[i]) <= budget and _markdown_balanced(blocks[i]):
            chosen.add(i)
            size += 2 + len(blocks[i])
    if not any(ACQUISITION_MARK in blocks[i] for i in chosen):
        return _cut_lines(text, budget) + CAPTION_SUFFIX
    return "\n\n".join([head.rstrip()] + [blocks[i].rstrip() for i in sorted(chosen)]) + CAPTION_SUFFIX


def send_telegram_document(file_path, caption, chat_id, filename=None):
    """sendDocument: adjunta el dossier (Markdown) con un caption de ≤ 1024 caracteres. True si Telegram lo aceptó."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
    data = {"chat_id": chat_id, "caption": document_caption(caption), "parse_mode": "Markdown"}
    try:
        with open(file_path, "rb") as f:
            r = requests.post(url, data=data, timeout=30,
                              files={"document": (filename or os.path.basename(file_path), f, "text/markdown")})
        if r.status_code == 200:
            print(f"[INFO] Dossier enviado a Telegram ({chat_id}).")
            return True
        print(f"[ERROR] Telegram sendDocument error ({chat_id}): {r.status_code} - {r.text}")
        return False
    except Exception as e:
        print(f"[ERROR] Telegram sendDocument exception ({chat_id}): {e}")
        return False


def send_alert(msg, dossier_path=None, filename=None):
    """Alerta con el dossier adjunto (caption = la alerta). Si no hay dossier o el documento no llega a ningún
    destino, se envía el mensaje normal: el adjunto nunca hace perder la alerta.
    Devuelve (alerta enviada, dossier enviado)."""
    dests = telegram_destinations()
    if dossier_path and TELEGRAM_BOT_TOKEN and dests:
        results = []
        for i, (_, chat_id) in enumerate(dests):
            if i:
                time.sleep(TELEGRAM_PAUSE_S)
            results.append(send_telegram_document(dossier_path, msg, chat_id, filename))
        if any(results):
            return True, True
        print("[WARN] Falló sendDocument: se envía solo el mensaje.")
    return send_telegram(msg), False


def load_dossier_builder():
    """script_113 (dossier por activo, doc 24) se carga al emitir y no al importar este módulo: script_113 importa
    script_97 para reutilizar las guías de compra (importarlo arriba sería circular) y toma sus rutas del
    SHOT_ROOT vigente. Si no se puede cargar, las alertas salen igual, sin documento."""
    try:
        path = _Path(__file__).resolve().parent / "script_113_dossier_builder.py"
        spec = importlib.util.spec_from_file_location("script_113_dossier_builder", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:   # el adjunto es opcional: ningún error del builder frena la emisión
        print(f"[WARN] script_113 no disponible; las alertas salen sin dossier: {e}")
        return None


def generate_dossier(builder, mint):
    """Arma y guarda el dossier del mint recién alertado, con el registro y el historial ya persistidos.
    Consultas gratuitas en vivo salvo DOSSIER_LIVE=false. Devuelve (ruta, nombre del adjunto) o (None, None):
    un dossier incompleto (regla núcleo del doc 24) o un error no frenan la alerta."""
    if builder is None:
        return None, None
    try:
        alert_data = builder.load_alert_data(mint)
        if alert_data is None:
            print(f"[WARN] Dossier de {mint[:10]}...: sin registro de la alerta.")
            return None, None
        record = alert_data["record"]
        chain = detection_facts(record)["chain"]
        live = builder.fetch_live(mint, chain, record) if os.getenv("DOSSIER_LIVE", "true").strip().lower() in TRUTHY else None
        dossier = builder.build_dossier(mint, chain, alert_data, live=live, mode="live" if live else "offline")
        if not dossier["emitible"]:
            print(f"[WARN] Dossier de {mint[:10]}... incompleto ({'; '.join(dossier['missing'])}): no se adjunta.")
            return None, None
        path = builder.save_dossier(dossier)
        symbol = re.sub(r"[^A-Za-z0-9]+", "", str(dossier["asset"]["symbol"] or ""))[:20] or "token"
        print(f"[INFO] Dossier guardado: {path}")
        return path, f"dossier_{symbol}_{mint[:8]}.md"
    except Exception as e:   # ídem: la alerta sale aunque el dossier falle
        print(f"[WARN] No se pudo generar el dossier de {mint[:10]}...: {e}")
        return None, None


def test_send():
    """--test-send: UN mensaje marcado como prueba al grupo (único destino). No es una alerta: no lee
    candidatos ni toca archivos. 0 si el grupo lo recibió, 1 si no (o si no hay grupo/token)."""
    labels = [label for label, _ in telegram_destinations()]
    text = ("🧪 *PRUEBA DE ENVÍO — Shot de Mercado*\n"
            "Mensaje de prueba de destinos. No es una alerta de mercado.\n"
            f"• Destinos configurados: {', '.join(labels) or 'ninguno'}\n"
            f"• {datetime.now(timezone.utc):%d/%m/%Y %H:%M UTC}")
    results = send_to_destinations(text)
    if not results:
        print("[TEST-SEND] Sin token o sin TELEGRAM_PUBLIC_CHAT_ID: no se envió nada.")
        return 1
    for label, ok in results:
        print(f"[TEST-SEND] {label}: {'OK' if ok else 'FALLO'}")
    return 0 if all(ok for _, ok in results) else 1

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
CHAIN_LABELS = {"solana": "Solana", "base": "Base", "ethereum": "Ethereum", "arbitrum": "Arbitrum",
                "optimism": "Optimism", "blast": "Blast", "monad": "Monad"}
# Exploradores por cadena (nombre, URL). Cadena sin explorador conocido = sin link (no se inventa).
EXPLORERS = {"solana": ("Solscan", "https://solscan.io/token/{addr}"),
             "base": ("BaseScan", "https://basescan.org/token/{addr}"),
             "ethereum": ("Etherscan", "https://etherscan.io/token/{addr}"),
             "arbitrum": ("Arbiscan", "https://arbiscan.io/token/{addr}"),
             "optimism": ("Optimistic Etherscan", "https://optimistic.etherscan.io/token/{addr}"),
             "blast": ("BlastScan", "https://blastscan.io/token/{addr}"),
             "monad": ("MonadScan", "https://monadscan.com/token/{addr}")}
DEXSCREENER_CHAINS = {"solana", "base", "ethereum", "arbitrum", "optimism", "blast"}
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
            "pair": dx.get("pairAddress"), "dex": dx.get("dexId"), "created": created_dt, "detected": detected_dt,
            "age_min": age}


# Guía de compra por chain (Dirección, 01/10): la adquisición es el núcleo del producto y va primero en la
# alerta. Chain sin guía o candidato sin mint = no se emite (acquisition_ready). Enlaces a los sitios oficiales;
# los enlaces de swap con el par precargado quedan pendientes de verificación manual (doc 24 §1.5).
ACQUISITION_GUIDES = {
    "solana": {"wallets": [("Phantom", "https://phantom.app"), ("Solflare", "https://solflare.com")],
               "dexes": [("Jupiter", "https://jup.ag"), ("Raydium", "https://raydium.io"), ("Orca", "https://www.orca.so")],
               "fund": "SOL o USDC", "native": "SOL", "address_word": "mint"},
    "ethereum": {"wallets": [("MetaMask", "https://metamask.io"), ("Rabby", "https://rabby.io")],
                 "dexes": [("Uniswap", "https://app.uniswap.org"), ("1inch", "https://app.1inch.io")],
                 "fund": "ETH o USDC/USDT", "native": "ETH", "address_word": "contrato"},
    "base": {"wallets": [("MetaMask", "https://metamask.io"), ("Coinbase Wallet", "https://www.coinbase.com/wallet")],
             "dexes": [("Aerodrome", "https://aerodrome.finance"), ("Uniswap", "https://app.uniswap.org")],
             "fund": "ETH o USDC en la red Base", "native": "ETH", "address_word": "contrato"},
    # Fase 6 (Dirección, 01/10): L2 y L1 nuevas. Dominios oficiales [I: no verificados por HTTP desde la sesión].
    "arbitrum": {"wallets": [("MetaMask", "https://metamask.io"), ("Rabby", "https://rabby.io")],
                 "dexes": [("Uniswap", "https://app.uniswap.org"), ("1inch", "https://app.1inch.io")],
                 "fund": "ETH o USDC en la red Arbitrum", "native": "ETH", "address_word": "contrato"},
    "optimism": {"wallets": [("MetaMask", "https://metamask.io"), ("Rabby", "https://rabby.io")],
                 "dexes": [("Uniswap", "https://app.uniswap.org")],
                 "fund": "ETH o USDC en la red Optimism (OP Mainnet)", "native": "ETH", "address_word": "contrato"},
    "blast": {"wallets": [("MetaMask", "https://metamask.io")],
              "dexes": [("Thruster", "https://thruster.finance"), ("Blasterswap", "https://blasterswap.com")],
              "fund": "ETH en la red Blast", "native": "ETH", "address_word": "contrato"},
    # Monad: sin DEX definido todavía (Dirección) -> guía incompleta -> no se emite hasta agregarlo.
    "monad": {"wallets": [("MetaMask", "https://metamask.io")], "dexes": [],
              "fund": "MON", "native": "MON", "address_word": "contrato"},
}
FUNDING_EXCHANGES = "Binance, Coinbase o Kraken"
# Slippage por liquidez del par [H, doc 24 §1.2]: < $50K 10% · < $250K 5% · < $1M 3% · resto 1%.
SLIPPAGE_TIERS = ((50_000, "10%"), (250_000, "5%"), (1_000_000, "3%"))


def suggested_slippage(liquidity):
    if not liquidity:
        return "5–10%"          # liquidez desconocida (p. ej., bonding curve de pump.fun: DexScreener informa 0)
    return next((slip for limit, slip in SLIPPAGE_TIERS if liquidity < limit), "1%")


def price_impact(usd, liquidity):
    """Impacto estimado de comprar `usd` en un pool de producto constante con liquidez total `liquidity` (la mitad
    del lado cotizado), sin comisiones: prima del precio promedio sobre el spot ≈ 2·usd/liquidity [H]."""
    return 2 * usd / liquidity if liquidity else None


def guide_for(chain):
    """Guía de compra COMPLETA de la chain (>= 1 wallet y >= 1 DEX, todos con URL), o None.

    Única fuente de verdad para la alerta (script_97) y el dossier (script_113): una chain con la guía a medias
    (p. ej., Monad sin DEX) cuenta como sin guía.
    """
    guide = ACQUISITION_GUIDES.get(str(chain or "").lower())
    if not guide:
        return None
    for key in ("wallets", "dexes"):
        entries = guide.get(key) or []
        if not entries or not all(name and url for name, url in entries):
            return None
    return guide


def acquisition_ready(token, mint=None):
    """Regla núcleo: se emite solo si hay guía de compra completa para la chain y un mint/contrato para pegar."""
    mint = mint or (token.get("token") or {}).get("mint") or token.get("mint")
    return bool(mint) and guide_for(detection_facts(token)["chain"]) is not None


def acquisition_block(mint, facts, snap):
    """Bloque 🛒: wallet, fondeo, DEX, mint, slippage + impacto estimado, verificación, swap y confirmación."""
    chain_text = CHAIN_LABELS.get(facts["chain"], facts["chain"])
    guide = guide_for(facts["chain"])
    if not guide:
        return f"🛒 *CÓMO ADQUIRIRLO* — {chain_text}\n• Sin guía de compra verificada para esta chain\n"
    wallets = " o ".join(f"{name} ({url})" for name, url in guide["wallets"][:2])
    (d1, du1), *alts = guide["dexes"]
    liq = snap["liquidity"]

    def impact(usd):
        x = price_impact(usd, liq)
        return "n/d" if x is None else ("<0.01%" if x < 0.0001 else f"{x * 100:.2f}%")

    explorer = EXPLORERS.get(facts["chain"])
    explorer_url = explorer[1].format(addr=mint) if explorer and mint else "n/d"
    pair_url = (f"https://dexscreener.com/{facts['chain']}/{facts['pair'] or mint}"
                if facts["chain"] in DEXSCREENER_CHAINS and (facts["pair"] or mint) else "n/d")
    pool = f" (liquidez principal en {md(facts['dex'])})" if facts.get("dex") else ""
    alternatives = f" · alternativas: {', '.join(f'{name} ({url})' for name, url in alts)}" if alts else ""
    return (f"🛒 *CÓMO ADQUIRIRLO* — {chain_text}\n"
            f"1. Wallet: {wallets}\n"
            f"2. Fondear con {guide['fund']} (comprados en {FUNDING_EXCHANGES}); dejar {guide['native']} para comisiones\n"
            f"3. Conectar la wallet a {d1} ({du1}){pool}{alternatives}\n"
            f"4. Pegar el {guide['address_word']} (coincidencia exacta): {f'`{mint}`' if mint else 'n/d'}\n"
            f"5. Slippage sugerido: {suggested_slippage(liq)} (liquidez {f'${liq:,.0f}' if liq else 'n/d'}) · "
            f"impacto estimado: $100 → {impact(100)} · $1,000 → {impact(1000)}\n"
            f"6. Verificar: contrato {explorer_url} · par {pair_url}\n"
            f"7. Ejecutar el swap\n"
            f"8. Confirmar la transacción en {explorer[0] if explorer else 'el explorador'}\n")


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


def prelaunch_line(mint, root=None):
    """D-082: '🆕 PRE-LANZAMIENTO …' si el calendario de preventa siguió este token (por contrato) antes de nacer.
    Sin calendario, sin coincidencia o ante cualquier error: '' y la alerta sale igual que siempre."""
    try:
        here = str(_Path(__file__).resolve().parent)
        if here not in sys.path:
            sys.path.insert(0, here)
        import lib_sources_store   # noqa: E402
        asset = lib_sources_store.prelaunch_lookup(mint, PROJECT_ROOT if root is None else root)
    except Exception:
        return ""
    if not asset:
        return ""
    born = asset.get("born") or {}
    # D-101 (doc 38 fix B): "preventa" solo si es precio de mercado real (perp); el de la ronda se muestra como venta
    real = born.get("precio_preventa") if "precio_preventa" in born else (
        asset.get("precio_preventa") if asset.get("precio_preventa_fuente") in ("hyperliquid", "aevo") else None)
    venta = born.get("precio_venta") or (asset.get("precio_venta") or {}).get("usd")
    delta, delta_v = born.get("delta_preventa_apertura_pct"), born.get("delta_venta_apertura_pct")
    if real is not None and delta is not None:
        text = f"precio preventa ${real:.8g}, delta vs apertura {delta:+.1f}%"
    elif real is not None:
        text = f"precio preventa ${real:.8g}"
    elif venta is not None:
        text = f"precio de venta (ICO) ${venta:.8g}" + (f", delta vs apertura {delta_v:+.1f}%" if delta_v is not None else "")
    else:
        text = "seguido desde el anuncio (" + ", ".join(sorted(asset.get("sources") or {})) + ")"
    tag = "" if born.get("alertable") else " (candidato por símbolo)"
    return f"🆕 *PRE-LANZAMIENTO*{tag}: {md(text)}\n"


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
{acquisition_block(mint, facts, snap)}
🕒 *DETECCIÓN*
• Detectado: {when(facts['detected'])}
• Edad del par al detectar: {age_text}
• Par creado: {when(facts['created'])}
• Ventana operativa: < {SIGNAL_WINDOW_H} h desde la detección
{prelaunch_line(mint)}
{probabilities}
📊 *DATOS (DexScreener, al detectar)*
• Precio: {show(snap['price'], '${:.8g}')}
• MCap: {show(snap['mcap_usd'], '${:,.0f}')}
• Liquidez: {show(snap['liquidity'], '${:,.0f}')}
• Volumen 24h: {show(snap['volume_24h'], '${:,.0f}')}
{sol_line}{collision_line}
🔎 *POR QUÉ LO DETECTAMOS* (score {score})
{reasons_block}
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

# ---------------------------------------------------------------------------
# Emisión multi-chain (Fase 7, doc 27). La ruta de memecoins Solana de arriba NO cambia: esto corre después,
# con su propio tope por ciclo, y lee las salidas de script_114 (02_Analisis/multichain/).
# ---------------------------------------------------------------------------
MULTICHAIN_DIR = PROJECT_ROOT / "02_Analisis" / "multichain"
MULTICHAIN_SCORES_FILE = MULTICHAIN_DIR / "_scores.json"
DOSSIERS_MULTICHAIN_DIR = PROJECT_ROOT / "02_Analisis" / "dossiers" / "multichain"
MULTICHAIN_MAX_AGE_MIN = 120          # el scanner corre cada 1 h: un scan de más de 2 h no se usa
MULTICHAIN_MAX_PER_CYCLE = 2          # aparte de las 3 de Solana
MULTICHAIN_MAX_PER_GROUP_24H = 3      # ningún grupo acapara la emisión
MULTICHAIN_COOLDOWN_H = SIGNAL_WINDOW_H   # el mismo activo se puede volver a alertar pasada la ventana de 48 h
CEX_BLUE_CHIPS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL"}
CEX_HOME = {"Binance": "https://www.binance.com", "Coinbase": "https://www.coinbase.com", "Kraken": "https://www.kraken.com"}
CG_TICKERS_URL = "https://api.coingecko.com/api/v3/coins/{id}/tickers?exchange_ids=binance,gdax,kraken"
GROUP_LABELS = {"a": "memecoin multi-chain", "b": "preventa", "c": "gobernanza DeFi", "d": "sintéticos",
                "e": "DePIN", "f": "L1/L2", "g": "RWA", "h": "blue chip", "i": "establecido sin grupo"}


def _persist():
    """lib_persist (Fase 9): dataset propio y bitácora de operaciones."""
    here = str(_Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import lib_persist   # noqa: E402
    return lib_persist


def tradability_flags(token=None, cex_links=None):
    """D-023-R3 T4: flag informativo de cada alerta (no bloquea): tradable, liquidity_usd, buy_route,
    initial_liquidity_usd. On-chain: lib_info_signals.tradability sobre el par. CEX: exchanges confirmados."""
    if cex_links is not None:
        names = [n for n, _ in cex_links]
        return {"tradable": bool(names), "liquidity_usd": None, "buy_route": "CEX: " + ", ".join(names),
                "initial_liquidity_usd": None}
    here = str(_Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import lib_info_signals   # noqa: E402
    dx = (token or {}).get("dexscreener") or (token or {}).get("dx") or {}
    liq = dx.get("liquidityUsd")
    return lib_info_signals.tradability(dx, [(0, liq)] if liq is not None else None)


_SOURCES_ROWS = None


def source_mentions(mint, symbol, now=None, rows=None):
    """Doc 34 / D-035: menciones del almacén de bots (lib_sources_store.query por mint y $symbol) para tokens
    >= 60 min. Informativo: no suma puntos hasta que se implemente el bono de v7.2.2. Sin almacén: ceros."""
    global _SOURCES_ROWS
    here = str(_Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import lib_sources_store   # noqa: E402
    now = now if now is not None else time.time()
    if rows is None:
        if _SOURCES_ROWS is None:
            _SOURCES_ROWS = lib_sources_store.safe_load(now, PROJECT_ROOT)
        rows = _SOURCES_ROWS
    items = lib_sources_store.mention_items(mint, symbol, rows) if rows else []
    return {"sources_mentions_1h": sum(1 for i in items if now - 3600 <= i["ts"] <= now),
            "sources_mentions_24h": sum(1 for i in items if now - 86400 <= i["ts"] <= now),
            "sources_feeds": sorted({i["f"] for i in items})}


def _load_lib_scoring():
    """lib_scoring_multichain, cargada recién al emitir multi-chain (vive al lado de este script)."""
    here = str(_Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import lib_scoring_multichain   # noqa: E402
    return lib_scoring_multichain


def _read_json_file(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def load_multichain_inputs(now=None, max_age_min=MULTICHAIN_MAX_AGE_MIN):
    """(scan, cards, categories, protocols) del último scan, o None si falta o tiene más de `max_age_min`."""
    now = now or datetime.now(timezone.utc)
    scan = _read_json_file(MULTICHAIN_DIR / "scan_latest.json")
    if not isinstance(scan, dict):
        return None
    try:
        at = datetime.fromisoformat(str(scan.get("generated_at")).replace("Z", "+00:00"))
    except ValueError:
        return None
    if (now - at).total_seconds() / 60 > max_age_min:
        return None
    cards = {}
    for path in MULTICHAIN_DIR.glob("*.json"):
        if not path.name.startswith(("_", "scan_")):
            card = _read_json_file(path)
            if isinstance(card, dict):
                cards[path.stem] = card
    return scan, cards, _read_json_file(MULTICHAIN_DIR / "_categories.json"), _read_json_file(MULTICHAIN_DIR / "_protocols.json")


EARLY_DIR = PROJECT_ROOT / "02_Analisis" / "early"
EARLY_ALERTS_FILE = EARLY_DIR / "_early_alerts.json"     # v0.1 (una sola instancia); se sigue leyendo
EARLY_CLAIMS_DIR = EARLY_DIR / "alerts"                 # Fase 10b: un archivo por mint (reclamo entre instancias)
EARLY_SIGNALS_MAX_AGE_MIN = 20       # script_116 los reescribe cada 2 min mientras corre
EARLY_WORKFLOWS = ("early_watch.yml", "early_watch_b.yml")


def load_early_signals(now=None, max_age_min=EARLY_SIGNALS_MAX_AGE_MIN):
    """Fase 10: {key: bono anticipatorio} de script_116 (order book / funding / F&G), o None si no hay nada fresco.
    Fase 10b: un archivo por instancia (_signals_<inst>.json, y el _signals.json de la v0.1); por activo gana
    el archivo más reciente."""
    now = now or datetime.now(timezone.utc)
    fresh = []
    for path in EARLY_DIR.glob("_signals*.json"):
        data = _read_json_file(path)
        if not isinstance(data, dict):
            continue
        try:
            at = datetime.fromisoformat(str(data.get("generated_at")).replace("Z", "+00:00"))
        except ValueError:
            continue
        if (now - at).total_seconds() / 60 <= max_age_min:
            fresh.append((at, data.get("signals") or {}))
    merged = {}
    for _, signals in sorted(fresh, key=lambda x: x[0]):
        merged.update(signals)
    return merged or None


def load_multichain_extras():
    """Fase 8: Snapshot (c), perps de Hyperliquid (d), pre-mercado de Aevo y TGEs de script_99 (b).
    Fase 10: bono anticipatorio de script_116 (early)."""
    return {"early": load_early_signals(),
            "memechain": _read_json_file(PROJECT_ROOT / "02_Analisis" / "datasets" / "memechain_index.json"),
            "governance": _read_json_file(MULTICHAIN_DIR / "_governance.json"),
            "perps": _read_json_file(MULTICHAIN_DIR / "_perps.json"),
            "premarket": _read_json_file(MULTICHAIN_DIR / "_premarket.json"),
            "prelaunch": _read_json_file(PROJECT_ROOT / "02_Analisis" / "pre_launch" / "_prelaunch_accumulated.json")}


def multichain_results(now=None, memecoin_scorer=None):
    """Puntúa todos los activos del último scan (lib_scoring_multichain) y deja el registro en _scores.json."""
    now = now or datetime.now(timezone.utc)
    inputs = load_multichain_inputs(now)
    if inputs is None:
        return None
    lib = _load_lib_scoring()
    results = lib.evaluate_all(*inputs, memecoin_scorer=memecoin_scorer, now=now, **load_multichain_extras())
    write_json_atomic(str(MULTICHAIN_SCORES_FILE), {
        "generated_at": now.isoformat(timespec="seconds"), "scan_generated_at": inputs[0].get("generated_at"),
        "lib_version": lib.VERSION, "min_coverage": lib.MIN_COVERAGE, "thresholds": lib.EMIT_THRESHOLD,
        "register_only": lib.REGISTER_ONLY, "coverage_by_group": lib.coverage_by_group(results),
        "results": [{k: r.get(k) for k in ("key", "group", "symbol", "chain", "score", "confidence", "emittable",
                                           "status_reason", "scoring_version")} for r in results]})
    return results


def _alert_time(alert):
    try:
        return datetime.strptime(str(alert.get("timestamp")), "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def select_multichain(results, all_alerts, now=None, per_cycle=MULTICHAIN_MAX_PER_CYCLE,
                      per_group_24h=MULTICHAIN_MAX_PER_GROUP_24H, cooldown_h=MULTICHAIN_COOLDOWN_H):
    """Emitibles por score, sin repetir un activo dentro de su ventana y con tope por grupo en 24 h."""
    now = now or datetime.now(timezone.utc)
    recent_keys, group_count = set(), {}
    for a in all_alerts:
        t = _alert_time(a) if isinstance(a, dict) and a.get("multichain") else None
        if t is None:
            continue
        if now - t < timedelta(hours=cooldown_h):
            recent_keys.add(a.get("asset_key") or a.get("mint"))
        if now - t < timedelta(hours=24):
            group_count[a.get("group")] = group_count.get(a.get("group"), 0) + 1
    out, skipped = [], {"cooldown": 0, "group_cap": 0}
    for r in results or []:
        if not r.get("emittable"):
            continue
        if r["key"] in recent_keys:
            skipped["cooldown"] += 1
            continue
        if group_count.get(r["group"], 0) >= per_group_24h:
            skipped["group_cap"] += 1
            continue
        out.append(r)
        group_count[r["group"]] = group_count.get(r["group"], 0) + 1
        if len(out) >= per_cycle:
            break
    return out, skipped


def cex_links_for(result, builder, fetch=None):
    """Exchanges centralizados confirmados para el activo: blue chips directos; el resto, pares que CoinGecko
    lista para ESE id (tickers de Binance, Coinbase y Kraken). Enlaces armados sin parámetros (sin referidos)."""
    if builder is None:
        return []
    cg_id, sym = result.get("cg_id"), (result.get("symbol") or "").upper()
    if cg_id in CEX_BLUE_CHIPS:
        return [(name, builder.CEX_LINKS[name].format(base=sym, quote="USDT" if name == "Binance" else "USD"))
                for name in ("Binance", "Coinbase", "Kraken")]
    fetch = fetch or (lambda url: requests.get(url, timeout=15, headers={"Accept": "application/json"}))
    try:
        r = fetch(CG_TICKERS_URL.format(id=cg_id))
        data = r.json() if r.status_code == 200 else None
    except (requests.RequestException, ValueError):
        data = None
    parsed = builder.parse_coingecko_contract({"id": cg_id, "symbol": sym, "tickers": (data or {}).get("tickers")}) \
        if isinstance(data, dict) else None
    confirmed = (parsed or {}).get("cex") or {}
    return [(name, builder.CEX_LINKS[name].format(base=pair[0], quote=pair[1]))
            for name in ("Binance", "Coinbase", "Kraken") for pair in confirmed.get(name, [])[:1]]


def multichain_token(result, detected_at):
    """Activo on-chain (pool de GeckoTerminal) con la forma de un candidato de script_82: reusa el mensaje y la guía."""
    created = result.get("pool_created_at")
    try:
        created_ms = int(datetime.fromisoformat(str(created).replace("Z", "+00:00")).timestamp() * 1000)
    except ValueError:
        created_ms = None
    return {"source": "multichain", "chain": result["chain"],
            "token": {"mint": result["address"], "symbol": result.get("symbol"), "name": result.get("name")},
            "dexscreener": {"priceUsd": result.get("price_usd"), "liquidityUsd": result.get("liquidity_usd"),
                            "volume24hUsd": result.get("volume_24h_usd"), "marketCapUsd": result.get("mcap_usd"),
                            "priceChange24h": result.get("change_24h"), "pairCreatedAt": created_ms,
                            "pairAddress": str(result.get("pool_address") or "").split("_", 1)[-1] or None},
            "score": result["score"], "reasons": result.get("reasons") or [], "detected_at": detected_at,
            "scoring_version": result["scoring_version"], "group": result["group"]}


def cex_acquisition_lines(result, links):
    """Pasos de compra por exchange centralizado (más la ruta on-chain de la red nativa en ETH y SOL)."""
    sym = md(result.get("symbol") or "?")
    cg = f"https://www.coingecko.com/en/coins/{result['cg_id']}" if result.get("cg_id") else "n/d"
    exchanges = " · ".join(f"{n} ({u})" for n, u in links)
    lines = [f"Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): {exchanges}",
             "1. Abrir cuenta en " + " o ".join(f"{n} ({CEX_HOME[n]})" for n, _ in links),
             "2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)",
             f"3. Abrir el par: {links[0][1]}",
             f"4. Verificar que el activo es {md(result.get('name') or sym)} ({sym}): {cg}",
             "5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)",
             "6. Ejecutar la compra",
             "7. Confirmar la operación en el historial de órdenes"]
    guide = guide_for(result.get("chain")) if result.get("cg_id") in CEX_BLUE_CHIPS else None
    if guide:
        w = " o ".join(f"{n} ({u})" for n, u in guide["wallets"][:2])
        d = " · ".join(f"{n} ({u})" for n, u in guide["dexes"][:2])
        lines.append(f"8. Opcional, custodia propia: retirar a una wallet de {CHAIN_LABELS.get(result['chain'])}: {w}. "
                     f"Ruta on-chain alternativa: fondear la wallet y comprar en {d}")
    else:
        lines.append("8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo")
    return lines


def format_multichain_message(result, links, detected_at):
    """Alerta de un activo sin contrato único (blue chips y tokens de CoinGecko): mismo orden de bloques, 🛒 primero."""
    sym = md(result.get("symbol") or "?")
    group = result["group"]
    comps = [c for c in result.get("components") or [] if c.get("s") is not None]
    comps.sort(key=lambda c: -abs(c["w"] * c["s"]))
    reasons = "".join(f"• {md(c['name'])}: {md(c['value'])} (s {c['s']:+.2f}, w {c['w']})\n" for c in comps[:4]) or "• n/d\n"
    extra = result.get("extra") or {}
    barrier = (f"• Barreras de la métrica (±2σ₄₈ del GARCH): ±{extra['barrier_pct']:.2f}%\n"
               if extra.get("barrier_pct") is not None else "")

    def usd(x, fmt=",.0f"):
        return "n/d" if x is None else "$" + format(x, fmt)

    def pct(x):
        return "n/d" if x is None else f"{x:+.2f}%"
    steps = "\n".join(cex_acquisition_lines(result, links))
    return (f"🚨 *SHOT DE MERCADO* — {sym} ({GROUP_LABELS.get(group, group)})\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🪪 *ACTIVO*\n• Nombre: {md(result.get('name') or 'n/d')} ({sym})\n"
            f"• Grupo: {group} — {GROUP_LABELS.get(group, group)} ({md(result.get('group_rule') or '')})\n"
            f"• Chain: {CHAIN_LABELS.get(result.get('chain'), result.get('chain') or 'multi-chain')}\n"
            f"• CoinGecko: {result.get('cg_id') or 'n/d'}\n\n"
            f"🛒 *CÓMO ADQUIRIRLO*\n{steps}\n\n"
            f"🕒 *DETECCIÓN*\n• Detectado: {detected_at}\n• Ventana operativa: < {SIGNAL_WINDOW_H} h desde la detección\n\n"
            f"🎯 *PROBABILIDADES*: en validación para el grupo {group} (scoring {result['scoring_version']})\n"
            f"• Evento medido: {result.get('event')}\n{barrier}\n"
            f"📊 *DATOS (CoinGecko, al detectar)*\n• Precio: {usd(result.get('price_usd'), ',.8g')}\n"
            f"• MCap: {usd(result.get('mcap_usd'))}\n• Volumen 24h: {usd(result.get('volume_24h_usd'))}\n"
            f"• Cambio 24h / 7d: {pct(result.get('change_24h'))} / {pct(result.get('change_7d'))}\n\n"
            f"🔎 *POR QUÉ LO DETECTAMOS* (score {result['score']}, cobertura {result['confidence']:.2f})\n{reasons}\n"
            f"🔗 *FUENTES VERIFICABLES*\n• CoinGecko: https://www.coingecko.com/en/coins/{result.get('cg_id')}\n"
            f"• Datos del scan: 02_Analisis/multichain/ (script_114)\n\n"
            f"⏱️ *SEGUIMIENTO*\n• Ventana de {SIGNAL_WINDOW_H} h; el activo se puede volver a alertar al cerrarla\n")


def _plain(text):
    return re.sub(r"[*`]", "", re.sub(r"\\([_*`\[])", r"\1", text))


def emit_multichain(all_alerts, timestamp, shadow, calibration, now=None, memecoin_scorer=None, cex_fetch=None):
    """Bloque multi-chain del ciclo. Mismo orden seguro que Solana: precio → registro persistido → dossier → envío."""
    if os.getenv("MULTICHAIN_EMISSIONS", "true").strip().lower() not in TRUTHY:
        print("[INFO] MULTICHAIN_EMISSIONS desactivado: no se emite multi-chain.")
        return 0
    now = now or datetime.now(timezone.utc)
    try:
        results = multichain_results(now, memecoin_scorer)
    except Exception as e:      # el bloque multi-chain nunca tumba la ruta Solana ni el commit del ciclo
        print(f"[WARN] Scoring multi-chain falló: {type(e).__name__}: {e}")
        return 0
    if results is None:
        print(f"[INFO] Multi-chain: sin scan de los últimos {MULTICHAIN_MAX_AGE_MIN} min en {MULTICHAIN_DIR}.")
        return 0
    # Se eligen hasta el doble del tope: si uno no tiene ruta de compra confirmada, el cupo pasa al siguiente.
    selected, skipped = select_multichain(results, all_alerts, now, per_cycle=2 * MULTICHAIN_MAX_PER_CYCLE)
    emittable = sum(1 for r in results if r.get("emittable"))
    print(f"[INFO] Multi-chain: {len(results)} activos puntuados · emitibles {emittable} · seleccionados "
          f"{len(selected)} (en ventana: {skipped['cooldown']}, tope por grupo: {skipped['group_cap']})")
    builder = load_dossier_builder() if selected else None
    detected_at = now.strftime("%d/%m/%Y %H:%M UTC")
    emitted = 0
    for r in selected:
        if emitted >= MULTICHAIN_MAX_PER_CYCLE:
            break
        onchain = bool(r.get("address"))
        if onchain:
            token = multichain_token(r, now.isoformat(timespec="seconds"))
            if not acquisition_ready(token, r["address"]):
                print(f"[SKIP] {r['symbol']} ({r['chain']}): sin guía de compra completa para la chain")
                continue
            msg, _ = format_alert_message(token, (), calibration if r["group"] == "a" else None)
            snap, facts = market_snapshot(token), detection_facts(token)
            acq = _plain(acquisition_block(r["address"], facts, snap)).splitlines()[1:]
        else:
            links = cex_links_for(r, builder, cex_fetch)
            if not links:
                print(f"[SKIP] {r['symbol']} ({r['key']}): sin exchange confirmado por CoinGecko (regla núcleo)")
                continue
            msg = format_multichain_message(r, links, detected_at)
            acq = [_plain(x) for x in cex_acquisition_lines(r, links)]
        flags = tradability_flags(token if onchain else None, None if onchain else links)
        price = r.get("price_usd")
        if not price or price <= 0:
            print(f"[SKIP] {r['symbol']} sin precio. No se emite.")
            continue
        # mint = contrato on-chain (script_98 consulta DexScreener con él); los activos CEX usan la clave cg:<id>
        record = {"timestamp": timestamp, "mint": r["address"] if onchain else r["key"], "asset_key": r["key"],
                  "symbol": r.get("symbol"), "score": r["score"],
                  "confidence": int(round(100 * (r.get("confidence") or 0))), "initial_price": price,
                  "status": ("shadow" if shadow else "active_tracking" if onchain else "active_tracking_cex"),
                  "multichain": True, "group": r["group"], "scoring_version": r["scoring_version"],
                  "chain": r.get("chain"), "coingecko_id": r.get("cg_id"), "trust_updates": []}
        record.update(flags)
        record.update(source_mentions(r["address"] if onchain else r["key"], r.get("symbol")))  # D-035, informativo
        safe = re.sub(r"[^A-Za-z0-9]+", "_", r["key"])
        with open(os.path.join(ALERTS_DIR, f"alert_{safe}_{timestamp}.json"), "w", encoding="utf-8") as f:
            json.dump(r, f, indent=2, ensure_ascii=False)
        all_alerts.append(record)
        write_json_atomic(ALL_ALERTS_FILE, all_alerts)            # persistido ANTES de enviar
        lib = _load_lib_scoring()
        dossier_path = DOSSIERS_MULTICHAIN_DIR / r["group"] / f"{safe}.md"
        dossier_path.parent.mkdir(parents=True, exist_ok=True)
        dossier_path.write_text(lib.render_dossier(r, acq, detected_at, [f"CoinGecko / GeckoTerminal / DefiLlama vía script_114"]),
                                encoding="utf-8")
        record["dossier"] = dossier_path.relative_to(PROJECT_ROOT).as_posix()
        name = f"dossier_{re.sub(r'[^A-Za-z0-9]+', '', str(r.get('symbol') or 'activo'))[:20]}_{safe[-8:]}.md"
        if shadow:
            record["telegram_sent"] = False
        else:
            record["telegram_sent"], record["dossier_sent"] = send_alert(msg, str(dossier_path), name)
        write_json_atomic(ALL_ALERTS_FILE, all_alerts)
        _persist().record_alert(record, r.get("components"), r.get("reasons"), source="script_97:multichain")
        print(f"[INFO] Multi-chain emitida: {r['symbol']} grupo {r['group']} score {r['score']} ({r['key']})")
        emitted += 1
        time.sleep(1)
    return emitted


# ---------------------------------------------------------------------------
# Fase 10: vigilancia temprana (script_116). Mientras early_watch corre, la ruta Solana es suya (poll de 2 min);
# acá solo se adoptan sus alertas en _all_alerts.json (para script_98 y el dataset) y se les adjunta el dossier.
# ---------------------------------------------------------------------------

def early_watch_active(get=None, repo=None, token=None):
    """True si hay una corrida en curso de early_watch.yml o early_watch_b.yml (API de Actions con GITHUB_TOKEN).
    Sin token, sin repo o con error: False (pipeline_t0 sigue emitiendo como siempre). EARLY_HANDOFF=false lo
    desactiva."""
    if (os.getenv("EARLY_HANDOFF") or "true").strip().lower() not in TRUTHY:
        return False
    repo = repo or os.getenv("GITHUB_REPOSITORY")
    token = token or os.getenv("GITHUB_TOKEN")
    if not repo or not token:
        return False
    get = get or requests.get
    for wf in EARLY_WORKFLOWS:
        url = f"https://api.github.com/repos/{repo}/actions/workflows/{wf}/runs?status=in_progress&per_page=1"
        try:
            r = get(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
                    timeout=15)
            if r.status_code == 200 and (r.json() or {}).get("total_count", 0) > 0:
                return True
        except Exception:
            continue
    return False


def _local_early_records():
    data = _read_json_file(EARLY_ALERTS_FILE, [])
    out = [r for r in data if isinstance(r, dict)] if isinstance(data, list) else []
    if EARLY_CLAIMS_DIR.is_dir():
        for path in sorted(EARLY_CLAIMS_DIR.glob("*.json")):
            rec = _read_json_file(path)
            if isinstance(rec, dict):
                out.append(rec)
    return out


def load_early_alerts(fresh=False, run=None):
    """Registros de script_116: early/alerts/<mint>.json (Fase 10b) + _early_alerts.json (v0.1).
    fresh=True: además los de origin/main recién traídos (git fetch), para no re-emitir algo que early_watch
    pusheó después del checkout de esta corrida; si git falla, solo lo local."""
    out = _local_early_records()
    if not fresh:
        return out
    import subprocess
    run = run or subprocess.run
    root = str(PROJECT_ROOT)
    have = {normalize_mint(r.get("mint")) for r in out}
    try:
        if run(["git", "fetch", "-q", "origin", "main"], cwd=root, capture_output=True, timeout=60).returncode != 0:
            return out
        for rel in (EARLY_ALERTS_FILE.relative_to(PROJECT_ROOT).as_posix(),):
            r = run(["git", "show", f"FETCH_HEAD:{rel}"], cwd=root, capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                data = json.loads(r.stdout)
                for rec in data if isinstance(data, list) else []:
                    if isinstance(rec, dict) and normalize_mint(rec.get("mint")) not in have:
                        out.append(rec)
                        have.add(normalize_mint(rec.get("mint")))
        claims = EARLY_CLAIMS_DIR.relative_to(PROJECT_ROOT).as_posix()
        r = run(["git", "ls-tree", "--name-only", "FETCH_HEAD", f"{claims}/"], cwd=root, capture_output=True,
                text=True, timeout=30)
        for rel in (r.stdout.split() if r.returncode == 0 else []):
            mint = rel.rsplit("/", 1)[-1][:-5] if rel.endswith(".json") else ""
            if not mint or normalize_mint(mint) in have:
                continue
            shown = run(["git", "show", f"FETCH_HEAD:{rel}"], cwd=root, capture_output=True, text=True, timeout=30)
            if shown.returncode == 0:
                rec = json.loads(shown.stdout)
                if isinstance(rec, dict):
                    out.append(rec)
                    have.add(normalize_mint(mint))
    except Exception:
        pass
    return out


def adopt_early_alerts(all_alerts, early_alerts, shadow=False, builder_loader=None):
    """Agrega a all_alerts (en memoria y en disco) las alertas de script_116 que todavía no figuran, con su
    status original (script_98 las sigue), y les adjunta el dossier (doc 24) si se enviaron. Devuelve las adoptadas."""
    have = {normalize_mint(a.get("mint")) for a in all_alerts if isinstance(a, dict)}
    adopted = []
    for rec in early_alerts:
        if not isinstance(rec, dict) or normalize_mint(rec.get("mint")) in have or not rec.get("mint"):
            continue
        record = dict(rec, early=True, adopted_at=datetime.utcnow().strftime("%Y-%m-%d_%H%M%S"))
        all_alerts.append(record)
        have.add(normalize_mint(rec["mint"]))
        adopted.append(record)
    if not adopted:
        return []
    write_json_atomic(ALL_ALERTS_FILE, all_alerts)
    builder = (builder_loader or load_dossier_builder)()
    for record in adopted:
        path, name = generate_dossier(builder, record["mint"])
        if path:
            record["dossier"] = _Path(os.path.relpath(path, PROJECT_ROOT)).as_posix()
            if record.get("telegram_sent") and not shadow:
                caption = (f"📎 Dossier de la alerta temprana *{md(str(record.get('symbol')))}* "
                           f"({record.get('timestamp')} UTC): {ACQUISITION_MARK} y estudio completo en el adjunto.")
                record["dossier_sent"] = send_alert(caption, path, name)[1]
        try:
            _persist().record_alert(dict(record, chain="solana", group="a"), source="script_116:early")
        except Exception as e:
            print(f"[WARN] dataset: {e}")
    write_json_atomic(ALL_ALERTS_FILE, all_alerts)
    print(f"[INFO] Alertas tempranas adoptadas: {[r.get('symbol') for r in adopted]}")
    return adopted


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if "--test-send" in argv:
        print("[YIN] Script 97 --test-send: prueba de destinos de Telegram (no emite alertas).")
        return test_send()
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

    # Fase 10: alertas de early_watch -> historial (dedup y seguimiento) antes de elegir candidatos
    delegated = early_watch_active()
    adopt_early_alerts(all_alerts, load_early_alerts(fresh=not delegated), shadow)

    # Filter score >= EMIT_MIN_SCORE and not already alerted (dedup por mint normalizado, activas y cerradas)
    candidates, stats = select_candidates(accumulated, all_alerts)
    if delegated:
        print(f"[INFO] early_watch en curso: la ruta Solana la emite script_116 (poll de 2 min). "
              f"Candidatos que habría tomado este ciclo: {len(candidates)}.")
        candidates = []
    if stats["intra_cycle_duplicates"]:
        dups = sorted(stats["intra_cycle_duplicates"])
        print(f"[WARN] Candidatos repetidos en el mismo ciclo (variantes del mismo mint): {dups}")
        log_cycle_event({"key": f"intra_cycle_duplicates:{timestamp}", "type": "intra_cycle_duplicates",
                         "timestamp": timestamp, "mints": dups})

    # Regla núcleo: sin guía de compra para la chain (o sin mint) no se emite
    no_guide = [(m, detection_facts(t)["chain"]) for m, t in candidates if not acquisition_ready(t, m)]
    candidates = [(m, t) for m, t in candidates if acquisition_ready(t, m)]
    for m, chain in no_guide[:5]:
        print(f"[SKIP] {m[:10]}... sin guía de compra para la chain '{chain}' o sin mint")

    # Max 3 alerts per cycle
    to_emit = candidates[:3]
    print(f"[INFO] Candidatos con score >= {EMIT_MIN_SCORE} pendientes de emitir: {len(candidates)} "
          f"(ya alertados y omitidos: {stats['already_alerted']}; "
          f"sin scoring en los últimos {CANDIDATE_MAX_AGE_MIN} min: {stats['stale_or_undated']}; "
          f"edad < {EMIT_MIN_AGE_MIN} min o desconocida: {len(stats['too_young_or_unknown_age'])}; "
          f"grupo i registrados: {stats['group_i_registered']})")
    for skip in stats["too_young_or_unknown_age"][:5]:
        print(f"[SKIP] {skip['mint'][:10]}... {skip['reason']} (edad: {skip['age_min']})")
    print(f"[INFO] Emitiendo {len(to_emit)} alertas en este ciclo.")

    builder = load_dossier_builder() if to_emit else None   # dossier por alerta (doc 24), adjunto al enviar
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
        alert_record.update(tradability_flags(token))      # D-023-R3: flag informativo
        alert_record.update(source_mentions(mint, symbol))  # D-035: menciones de bots, informativo (v7.2.2)
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

        # Dossier del activo: se arma con el registro ya persistido; en sombra se guarda sin enviarse
        dossier_path, dossier_name = generate_dossier(builder, mint)
        if dossier_path:
            alert_record["dossier"] = _Path(os.path.relpath(dossier_path, PROJECT_ROOT)).as_posix()
        if shadow:
            if dossier_path:
                print(f"[INFO] Sombra: dossier en {dossier_path}, no se envía.")
            alert_record["telegram_sent"] = False
        else:
            alert_record["telegram_sent"], alert_record["dossier_sent"] = send_alert(msg, dossier_path, dossier_name)
        write_json_atomic(ALL_ALERTS_FILE, all_alerts)
        _persist().record_alert(dict(alert_record, scoring_version=token.get("scoring_version"), chain="solana",
                                     group=token.get("group") or "a"), reasons=token.get("reasons"),
                                source="script_97:solana")
        emitted_count += 1
        time.sleep(1) # rate limit telegram

    # Multi-chain (Fase 7): después de la ruta Solana, con su propio tope y su propio registro.
    emitted_count += emit_multichain(all_alerts, timestamp, shadow, calibration)

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

    _persist().log_operation("emission_cycle", "script_97",
                             [ALL_ALERTS_FILE] + ([MULTICHAIN_SCORES_FILE] if MULTICHAIN_SCORES_FILE.exists() else []),
                             emitted=emitted_count, total_alerts=len(all_alerts), shadow=bool(shadow))
    print(f"\n[YIN] Emisión de alertas finalizada. Emitidas: {emitted_count}")
    print(f"Total histórico de alertas: {len(all_alerts)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())