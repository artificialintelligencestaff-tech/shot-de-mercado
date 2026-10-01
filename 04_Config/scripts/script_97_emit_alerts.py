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


def acquisition_ready(token, mint=None):
    """Regla núcleo: se emite solo si hay guía de compra para la chain y un mint/contrato para pegar."""
    mint = mint or (token.get("token") or {}).get("mint") or token.get("mint")
    return bool(mint) and detection_facts(token)["chain"] in ACQUISITION_GUIDES


def acquisition_block(mint, facts, snap):
    """Bloque 🛒: wallet, fondeo, DEX, mint, slippage + impacto estimado, verificación, swap y confirmación."""
    chain_text = CHAIN_LABELS.get(facts["chain"], facts["chain"])
    guide = ACQUISITION_GUIDES.get(facts["chain"])
    if not guide:
        return f"🛒 *CÓMO ADQUIRIRLO* — {chain_text}\n• Sin guía de compra verificada para esta chain\n"
    (w1, wu1), (w2, wu2) = guide["wallets"][:2]
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
    alternatives = ", ".join(f"{name} ({url})" for name, url in alts)
    return (f"🛒 *CÓMO ADQUIRIRLO* — {chain_text}\n"
            f"1. Wallet: {w1} ({wu1}) o {w2} ({wu2})\n"
            f"2. Fondear con {guide['fund']} (comprados en {FUNDING_EXCHANGES}); dejar {guide['native']} para comisiones\n"
            f"3. Conectar la wallet a {d1} ({du1}){pool} · alternativas: {alternatives}\n"
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

    # Filter score >= EMIT_MIN_SCORE and not already alerted (dedup por mint normalizado, activas y cerradas)
    candidates, stats = select_candidates(accumulated, all_alerts)
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