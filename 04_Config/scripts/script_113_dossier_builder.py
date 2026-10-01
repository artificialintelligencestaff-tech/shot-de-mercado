#!/usr/bin/env python3
"""
script_113_dossier_builder.py — Dossier por activo (diseño: doc 24 v1.1), con la adquisición primero.

El dossier informa con datos y método: cómo se adquiere el activo paso a paso, qué es, por qué lo detectó el
sistema, con qué datos y cálculos, por cuánto tiempo aplica la señal y cómo auditar cada número. No juzga,
no recomienda: el lector decide.

Orden fijo: presentación → 🛒 1 cómo adquirir → 📊 2 identificación → 🧬 3 naturaleza → 🔬 4 método →
🎯 5 fundamento → ⏱️ 6 vigencia → 📚 7 fuentes.
Regla núcleo (Dirección, 01/10): si falta un campo obligatorio de la adquisición, el dossier no se emite.
Lo desconocido se escribe "n/d" con la fuente que lo resolvería; nunca se rellena con valores por defecto.

Fuentes (gratuitas, sin key):
  repo     02_Analisis/alerts/_all_alerts.json + alert_<mint>_<ts>.json (registro exacto al alertar)
           02_Analisis/shadow_v4/_accumulated.json (fallback y población del scorer)
           02_Analisis/signals/[<chain>/]<mint>.json (señales on-chain de Jupiter, si existen)
           02_Analisis/diagnostics/{emission_calibration,shadow_monitor}.json
           01_Datos_Crudos/final_detection/detection_*.json (archivo de la corrida que lo detectó)
  en vivo  DexScreener (par y mercado) · RugCheck (Solana: authorities, holders, LP) · GoPlus (Solana y EVM) ·
           GeckoTerminal (velas de 1 h para la historia y de 15 min para la métrica dual del activo)

Reutiliza script_97 (guías de compra, slippage, impacto, exploradores) y calibrate_threshold_v72 (métrica dual,
Wilson, velas, carga del scorer): el dossier, la alerta y la calibración usan las mismas definiciones.

Uso (desde la raíz del repo):
  python 04_Config/scripts/script_113_dossier_builder.py --dry-run              # VSOF con datos fijos, sin red
  python 04_Config/scripts/script_113_dossier_builder.py --mint <MINT>          # repo + consultas -> guarda
  opciones: --chain solana · --offline (solo repo) · --stdout (imprime, no guarda) · --out RUTA · --pdf
Salida: 02_Analisis/dossiers/<chain>/<mint>.md + <mint>.json (el dict completo, con sus datos de entrada).
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import requests

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import calibrate_threshold_v72 as cal  # noqa: E402  métrica dual, Wilson, velas de 15 min, carga del scorer


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s97 = _load("s97_dossier", "script_97_emit_alerts.py")   # guías de compra por chain, slippage, impacto

ROOT = s97.PROJECT_ROOT
ALERTS_DIR = Path(s97.ALERTS_DIR)
ACCUMULATED_FILE = Path(s97.ACCUMULATED_FILE)
SIGNALS_DIR = ROOT / "02_Analisis" / "signals"
SHADOW_MONITOR_FILE = ROOT / "02_Analisis" / "diagnostics" / "shadow_monitor.json"
DETECTION_DIR = ROOT / "01_Datos_Crudos" / "final_detection"
DOSSIERS_DIR = ROOT / "02_Analisis" / "dossiers"
SCORER_FILE = SCRIPTS / "script_82_final_detection.py"

DOSSIER_VERSION = "1.0"
SECTIONS = (("acquisition", "🛒", "Cómo adquirir"),
            ("identification", "📊", "Identificación del activo"),
            ("nature", "🧬", "Naturaleza del activo"),
            ("method", "🔬", "Método científico aplicado"),
            ("foundation", "🎯", "Fundamento de la detección"),
            ("validity", "⏱️", "Vigencia estimada"),
            ("sources", "📚", "Fuentes verificables"))
WINDOW_H = s97.SIGNAL_WINDOW_H
IMPACT_SIZES = (100, 1_000, 10_000)
IMPACT_TARGETS = (0.01, 0.03)          # tamaño de orden cuya prima de ejecución es 1% y 3%
DETECTION_LOOKBACK_MIN = 60            # el archivo de la corrida que detectó está en la hora previa a la alerta
BLUE_CHIPS = {"BTC", "ETH", "SOL"}
BASELINE_PRIMARY = 0.105               # baseline de la primaria (doc 22 §1.1), si shadow_monitor no lo trae

# Grupos del doc 23 (a–h) y el tipo de activo que corresponde a cada uno.
GROUPS = {"a": ("memecoins micro-cap", "Memecoin"), "b": ("preventa / pre-market", "Token en preventa"),
          "c": ("DeFi de gobernanza nueva", "Token de gobernanza DeFi"),
          "d": ("sintéticos y derivados algorítmicos", "Activo sintético"), "e": ("DePIN", "Token DePIN"),
          "f": ("L1/L2 emergentes", "Token de L1/L2"), "g": ("RWA", "Token RWA"), "h": ("blue chips", "Blue chip")}

# Histórico legado (v7.1, score ≥ 56), k/n de los docs 19 §4.2 y 21 [V]. El IC90 se calcula con Wilson.
HISTORICAL_SOURCE = "legado v7.1, score ≥ 56 (docs 19 §4.2 y 21)"
HISTORICAL = {"primary": (21, 35), "secondary": (3, 35),
              "post_hit": (round(s97.HISTORICAL_RUG_AFTER_HIT["rate"] * s97.HISTORICAL_RUG_AFTER_HIT["n"]),
                           s97.HISTORICAL_RUG_AFTER_HIT["n"])}
# Duración de eventos similares: aciertos primarios del legado v7.1, n = 38 de 75 tokens con velas (doc 24 §6) [V].
HISTORICAL_DURATION = {"n": 38, "of": 75, "median_max": 1.13, "median_min_after": -0.996, "median_last_48h": -0.995}

DEXSCREENER_TOKENS = "https://api.dexscreener.com/latest/dex/tokens/{addr}"
RUGCHECK_REPORT = "https://api.rugcheck.xyz/v1/tokens/{addr}/report"
GOPLUS_SOLANA = "https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses={addr}"
GOPLUS_EVM = "https://api.gopluslabs.io/api/v1/token_security/{chain_id}?contract_addresses={addr}"
GOPLUS_CHAIN_IDS = {"ethereum": "1", "base": "8453"}
GECKO_NETWORKS = {"solana": "solana", "ethereum": "eth", "base": "base"}
GECKO_OHLCV_HOUR = "https://api.geckoterminal.com/api/v2/networks/{net}/pools/{pool}/ohlcv/hour?limit=1000"
# Categoría y ruta por exchange centralizado (Fase 4 T2). CoinGecko identifica el activo POR CONTRATO; Binance y
# Coinbase solo confirman que el par existe por SÍMBOLO, que puede ser de otro token homónimo: se enlaza un
# exchange solo si CoinGecko confirma ese contrato en ese exchange (o si es un blue chip nativo).
COINGECKO_CONTRACT = "https://api.coingecko.com/api/v3/coins/{platform}/contract/{addr}"
COINGECKO_PLATFORMS = {"solana": "solana", "ethereum": "ethereum", "base": "base"}
BINANCE_EXCHANGE_INFO = "https://data-api.binance.vision/api/v3/exchangeInfo?symbol={symbol}"
COINBASE_PRODUCT = "https://api.exchange.coinbase.com/products/{product}"
CG_EXCHANGES = {"binance": "Binance", "gdax": "Coinbase", "kraken": "Kraken"}   # identificador de CoinGecko -> exchange
CEX_QUOTES = ("USDT", "USD", "USDC")
# Enlaces armados acá y sin parámetros: los trade_url de CoinGecko para Binance traen un código de referido.
CEX_LINKS = {"Binance": "https://www.binance.com/en/trade/{base}_{quote}",
             "Coinbase": "https://www.coinbase.com/advanced-trade/spot/{base}-{quote}",
             "Kraken": "https://pro.kraken.com/app/trade/{base}-{quote}"}
SCANNER_FILE = ROOT / "02_Analisis" / "multichain" / "scan_latest.json"
NARRATIVE_REGISTRY = ROOT / "04_Config" / "narrative_registry.json"
HTTP_TIMEOUT_S = 15
HTTP_PAUSE_S = 1.0
HTTP_HEADERS = {"User-Agent": "shot-de-mercado-dossier/1.0", "Accept": "application/json"}


# ---------------------------------------------------------------------------
# Formato (castellano: miles con punto, decimales con coma)
# ---------------------------------------------------------------------------

def _es(text):
    return text.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def fmt_usd(x, decimals=0):
    return "n/d" if x is None else "$" + _es(f"{x:,.{decimals}f}")


def fmt_price(x):
    """Precio con 4 cifras significativas, sin notación científica."""
    if x is None:
        return "n/d"
    if x <= 0:
        return "$0"
    decimals = max(2, 3 - math.floor(math.log10(x)))
    return "$" + _es(f"{x:,.{decimals}f}")


def fmt_int(x):
    return "n/d" if x is None else _es(f"{x:,.0f}")


def fmt_pct(ratio, decimals=1, signed=False):
    """Fracción -> porcentaje (0,0167 -> 1,7%)."""
    if ratio is None:
        return "n/d"
    return _es(f"{ratio * 100:{'+' if signed else ''},.{decimals}f}") + "%"


def fmt_pp(value, decimals=1, signed=True):
    """Valor que ya está en puntos porcentuales (priceChange de DexScreener)."""
    if value is None:
        return "n/d"
    return _es(f"{value:{'+' if signed else ''},.{decimals}f}") + "%"


def fmt_impact(x):
    if x is None:
        return "n/d"
    return "<0,001%" if x < 0.00001 else fmt_pct(x, 3)


def fmt_num(x, decimals=2):
    return "n/d" if x is None else _es(f"{x:,.{decimals}f}")


def fmt_points(p):
    return f"{round(p):+d}" if abs(p - round(p)) < 1e-9 else _es(f"{p:+.1f}")


def fmt_age(minutes):
    if minutes is None:
        return "n/d"
    if minutes < 120:
        return _es(f"{minutes:.1f}") + " min"
    if minutes < 2880:
        return _es(f"{minutes / 60:.1f}") + " h"
    return _es(f"{minutes / 1440:.1f}") + " días"


def short(addr):
    return f"{addr[:7]}…{addr[-4:]}" if addr and len(addr) > 14 else (addr or "n/d")


def when(dt):
    return dt.strftime("%d/%m/%Y %H:%M UTC") if dt else "n/d"


def iso(dt):
    return dt.isoformat(timespec="seconds") if dt else None


def _num(value):
    return s97._num(value)


def parse_ts(value):
    """ISO 8601 (con o sin 'Z', hasta nanosegundos) o 'YYYY-mm-dd_HHMMSS' (convención de alerts) -> datetime UTC."""
    if not value or not isinstance(value, str):
        return None
    text = re.sub(r"(\.\d{6})\d+", r"\1", value.strip()).replace("Z", "+00:00")
    try:
        dt = datetime.strptime(text, "%Y-%m-%d_%H%M%S") if "_" in text else datetime.fromisoformat(text)
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def from_ms(ms):
    value = _num(ms)
    return datetime.fromtimestamp(value / 1000, timezone.utc) if value and value > 0 else None


# ---------------------------------------------------------------------------
# Desglose del score a partir de los motivos registrados (sin reloj ni estado: reproducible)
# ---------------------------------------------------------------------------

# Motivo que registra script_82.score_token -> (componente, condición, puntos), Anexo C del doc 24 [V, del código].
# El aporte del feed (score WS × 0,3) se suma siempre, aunque no deje motivo (WS < 60).
REASON_RULES = (
    ("MCap > $1M", "MCap", "≥ $1M", 25), ("MCap > $100K", "MCap", "≥ $100K", 15),
    ("MCap > $50K", "MCap", "≥ $50K", 10), ("MCap bajo", "MCap", "< $50K", 0),
    ("Volumen masivo", "Volumen 24 h", "≥ $1M", 20), ("Volumen alto", "Volumen 24 h", "≥ $100K", 15),
    ("Volumen decente", "Volumen 24 h", "≥ $50K", 10), ("Volumen bajo", "Volumen 24 h", "< $50K", 0),
    ("Liquidez alta", "Liquidez", "≥ $100K", 15), ("Liquidez decente", "Liquidez", "≥ $50K", 10),
    ("Liquidez mínima", "Liquidez", "≥ $20K", 5), ("Liquidez baja", "Liquidez", "< $20K", 0),
    ("Pump 24h", "Cambio 24 h", "≥ +50%", 10), ("Subida 24h", "Cambio 24 h", "≥ +20%", 5),
    ("Dump 24h", "Cambio 24 h", "≤ −30%", -5),
    ("Buy pressure cayendo", "Buy pressure dinámica", "Δ vs la corrida anterior ≤ −0,10", -15),
    ("Buy pressure subiendo", "Buy pressure dinámica", "Δ vs la corrida anterior ≥ +0,10 (par maduro)", 15),
    ("Volumen acelerado", "Volumen m5/h1", "> 0,5 (par maduro)", 25),
    ("Volumen en aceleración", "Volumen m5/h1", "> 0,25 (par maduro)", 15),
    ("Trades acelerados", "Trades m5/h1", "> 0,5 (par maduro)", 20),
    ("Trades en aceleración", "Trades m5/h1", "> 0,25 (par maduro)", 10),
    ("Buy pressure >60%", "Buy pressure m5", "> 60% (par maduro)", 25),
    ("Buy pressure >55%", "Buy pressure m5", "> 55% (par maduro)", 15),
    ("Momentum corto+medio positivo", "Momentum", "m5 > 0 y h1 > 0 (par maduro)", 20),
    ("Momentum corto positivo", "Momentum", "m5 > 0 y h1 > −5% (par maduro)", 10),
    ("Edge temprano (<4h)", "Edge temprano", "edad < 4 h (par maduro)", 8),
    ("Volumen activo m5", "Volumen m5", "> $1K (par maduro)", 10),
    ("Volumen moderado m5", "Volumen m5", "> $500 (par maduro)", 5),
    ("Detección tardía", "Detección tardía", "sin volumen m5 y edad > 4 h", -30),
    ("Par >24h", "Par viejo", "edad > 24 h", -50),
    ("Venta dominante", "Venta dominante", "buy pressure < 40% con volumen m5", -20),
    ("Venta agresiva", "Venta dominante", "buy pressure < 30% con volumen m5", -35),
    ("SOBRECOMPRA EXTREMA", "Sobrecompra", "cambio 24 h > 50.000%", -50),
    ("KILL SWITCH", "Kill switch", "edad < 5 min y cambio 24 h > 10.000%", -50),
    ("v7.2.1: bonos temporales omitidos", "Gate de edad v7.2.1", "edad < 60 min o desconocida: sin bonos temporales", 0),
)
OVERBOUGHT = {"ALTA": ("cambio 24 h > 5.000%", -50, -15), "MEDIA": ("cambio 24 h > 500%", -30, -10)}


def reason_points(reason):
    """(componente, condición, puntos) de un motivo; ("feed",) si es parte del aporte del feed; None si es desconocido."""
    text = str(reason).strip()
    if text.startswith("WS score"):
        return ("feed",)
    for tier, (base, below_1, below_3) in OVERBOUGHT.items():
        if text.startswith(f"SOBRECOMPRA {tier}"):
            if "sin penalización" in text:
                return ("Sobrecompra", f"{base} con liq/mcap ≥ 3%", 0)
            if text.endswith("<1%"):
                return ("Sobrecompra", f"{base} con liq/mcap < 1%", below_1)
            if text.endswith("<3%"):
                return ("Sobrecompra", f"{base} con liq/mcap < 3%", below_3)
            return None
    for prefix, component, condition, points in REASON_RULES:
        if text.startswith(prefix):
            return (component, condition, points)
    return None


def _dx(record):
    return record.get("dexscreener") or record.get("dx") or {}


def observed_values(record, age_min):
    """Valor observado por componente, desde el registro de la detección."""
    dx, tok = _dx(record), record.get("token") or {}
    mcap = _num(dx.get("marketCapUsd")) or _num(tok.get("marketCapUsd"))
    vol = _num(dx.get("volume24hUsd")) or _num(tok.get("volumeUsd"))
    liq, change = _num(dx.get("liquidityUsd")), _num(dx.get("priceChange24h"))
    vm5, vh1 = _num(dx.get("volume_m5")), _num(dx.get("volume_h1"))
    b5, s5 = _num(dx.get("txns_m5_buys")), _num(dx.get("txns_m5_sells"))
    b1, s1 = _num(dx.get("txns_h1_buys")), _num(dx.get("txns_h1_sells"))
    t5 = (b5 or 0) + (s5 or 0) if b5 is not None or s5 is not None else None
    t1 = (b1 or 0) + (s1 or 0) if b1 is not None or s1 is not None else None
    bp = b5 / t5 if t5 else None
    ratio = liq / mcap if liq is not None and mcap else None
    age = fmt_age(age_min)
    return {
        "Score del feed": f"WS {fmt_int(_num(tok.get('score')) or 0)} × 0,3",
        "MCap": fmt_usd(mcap), "Volumen 24 h": fmt_usd(vol), "Liquidez": fmt_usd(liq),
        "Cambio 24 h": fmt_pp(change, 0),
        "Buy pressure dinámica": "n/d (el Δ contra la corrida anterior no se guarda)",
        "Volumen m5/h1": fmt_num(vm5 / vh1) if vm5 is not None and vh1 else "n/d",
        "Trades m5/h1": fmt_num(t5 / t1) if t5 is not None and t1 else "n/d",
        "Buy pressure m5": fmt_pct(bp, 0), "Venta dominante": fmt_pct(bp, 0),
        "Momentum": f"m5 {fmt_pp(_num(dx.get('priceChange_m5')))} · h1 {fmt_pp(_num(dx.get('priceChange_h1')))}",
        "Edge temprano": f"edad {age}", "Par viejo": f"edad {age}", "Gate de edad v7.2.1": f"edad {age}",
        "Volumen m5": fmt_usd(vm5), "Detección tardía": f"vol m5 {fmt_usd(vm5)} · edad {age}",
        "Sobrecompra": f"{fmt_pp(change, 0)} · liq/mcap {fmt_pct(ratio, 1)}",
        "Kill switch": f"edad {age} · cambio 24 h {fmt_pp(change, 0)}",
    }


def score_breakdown(record, age_min=None):
    """Desglose del score registrado. 'reproducible' = la suma recortada a 0–100 coincide con el score guardado."""
    tok = record.get("token") or {}
    ws = _num(tok.get("score")) or 0
    observed = observed_values(record, age_min)
    rows = [{"component": "Score del feed", "condition": "score WS × 0,3", "reason": None,
             "observed": observed["Score del feed"], "points": ws * 0.3}]
    unknown = []
    for reason in record.get("reasons") or []:
        rule = reason_points(reason)
        if rule is None:
            unknown.append(reason)
        elif rule[0] != "feed":
            component, condition, points = rule
            rows.append({"component": component, "condition": condition, "reason": reason,
                         "observed": observed.get(component, "n/d"), "points": points})
    raw = sum(r["points"] for r in rows)
    total = min(100, max(0, int(raw)))
    registered = record.get("score")
    reproducible = (not unknown and isinstance(registered, (int, float)) and not isinstance(registered, bool)
                    and total == registered)
    return {"rows": rows, "sum": raw, "total": total, "registered": registered,
            "reproducible": reproducible, "unknown_reasons": unknown}


def current_scorer_version():
    """SCORING_VERSION del script_82 del árbol (sin importarlo)."""
    try:
        match = re.search(r'^SCORING_VERSION\s*=\s*"([^"]+)"', SCORER_FILE.read_text(encoding="utf-8"), re.M)
    except OSError:
        return None
    return match.group(1) if match else None


def recompute_current(record, t_score):
    """Score del registro con el scorer vigente: reloj fijado al momento de la detección y sin _accumulated.json
    (bp_delta = 0), igual que calibrate_threshold_v72. Si el scorer no se puede importar -> error, se informa n/d."""
    try:
        with tempfile.TemporaryDirectory() as work:
            s82 = cal.load_script_82(work)
            prev = os.getcwd()
            os.chdir(work)
            try:
                with mock.patch("time.time", return_value=t_score):
                    score, reasons = s82.score_token(record.get("token") or {}, _dx(record) or None)
            finally:
                os.chdir(prev)
        return {"version": getattr(s82, "SCORING_VERSION", None), "score": score, "reasons": reasons,
                "clock": iso(datetime.fromtimestamp(t_score, timezone.utc))}
    except Exception as e:   # dependencia faltante o registro incompatible: el dossier lo informa, no se cae
        return {"version": None, "score": None, "reasons": [], "error": f"{type(e).__name__}: {e}"}


# ---------------------------------------------------------------------------
# Estudio de adquisición
# ---------------------------------------------------------------------------

def size_for_impact(target, liquidity):
    """Monto Δ cuya prima de ejecución es `target` en el modelo de producto constante: 2Δ/L = target -> Δ = target·L/2."""
    return target * liquidity / 2 if liquidity else None


def liquidity_row(moment, dex, pair, liquidity):
    return {"moment": moment, "dex": dex, "pair": pair, "liquidity": liquidity,
            "slippage": s97.suggested_slippage(liquidity),
            "impacts": {str(usd): s97.price_impact(usd, liquidity) for usd in IMPACT_SIZES},
            "size_for": {str(t): size_for_impact(t, liquidity) for t in IMPACT_TARGETS}}


# ---------------------------------------------------------------------------
# Datos en vivo: parsers (puros, testeables) y consulta
# ---------------------------------------------------------------------------

def parse_dexscreener(data, chain):
    """Par principal (mayor liquidez) de la chain, igual criterio que script_82."""
    pairs = [p for p in (data or {}).get("pairs") or [] if str(p.get("chainId", "")).lower() == chain]
    if not pairs:
        return None
    p = max(pairs, key=lambda x: _num((x.get("liquidity") or {}).get("usd")) or 0)
    info = p.get("info") or {}
    return {"price": _num(p.get("priceUsd")), "liquidity": _num((p.get("liquidity") or {}).get("usd")),
            "mcap": _num(p.get("marketCap")), "fdv": _num(p.get("fdv")), "pair": p.get("pairAddress"),
            "dex": p.get("dexId"), "pair_created_ms": _num(p.get("pairCreatedAt")),
            "price_change": p.get("priceChange") or {}, "volume": p.get("volume") or {}, "txns": p.get("txns") or {},
            "websites": [w.get("url") for w in info.get("websites") or [] if w.get("url")],
            "socials": [(s.get("type"), s.get("url")) for s in info.get("socials") or [] if s.get("url")],
            "n_pairs": len(pairs)}


def parse_rugcheck(data):
    if not isinstance(data, dict) or not data.get("mint"):
        return None
    top = [_num(h.get("pct")) for h in data.get("topHolders") or [] if _num(h.get("pct")) is not None][:10]
    file_meta, token_meta = data.get("fileMeta") or {}, data.get("tokenMeta") or {}
    return {"creator": data.get("creator"), "mint_authority": data.get("mintAuthority"),
            "freeze_authority": data.get("freezeAuthority"), "holders": _num(data.get("totalHolders")),
            "top10": top, "top10_pct": sum(top) if top else None,
            "insiders_top10": sum(1 for h in (data.get("topHolders") or [])[:10] if h.get("insider")),
            "lp_locked": [(m.get("marketType"), _num((m.get("lp") or {}).get("lpLockedPct")))
                          for m in data.get("markets") or []],
            "labels": [r.get("name") for r in data.get("risks") or [] if r.get("name")],
            "description": (file_meta.get("description") or "").strip(),
            "metadata_uri": token_meta.get("uri"), "metadata_mutable": token_meta.get("mutable"),
            "total_liquidity": _num(data.get("totalMarketLiquidity")), "detected_at": data.get("detectedAt")}


def _flag(value):
    return None if value in (None, "") else str(value) == "1"


def parse_goplus(data, address, chain):
    result = (data or {}).get("result") or {}
    res = result.get(address) or result.get(str(address).lower())
    if not isinstance(res, dict):
        return None
    if chain == "solana":
        return {"mintable": _flag((res.get("mintable") or {}).get("status")),
                "freezable": _flag((res.get("freezable") or {}).get("status")),
                "metadata_mutable": _flag((res.get("metadata_mutable") or {}).get("status"))}
    return {"mintable": _flag(res.get("is_mintable")), "honeypot": _flag(res.get("is_honeypot")),
            "open_source": _flag(res.get("is_open_source")), "owner": res.get("owner_address") or None,
            "buy_tax": _num(res.get("buy_tax")), "sell_tax": _num(res.get("sell_tax")),
            "holders": _num(res.get("holder_count"))}


def parse_ohlcv(data, interval="1 h"):
    rows = (((data or {}).get("data") or {}).get("attributes") or {}).get("ohlcv_list") or []
    rows = sorted(r for r in rows if isinstance(r, list) and len(r) >= 5)
    if not rows:
        return None
    hi, lo = max(rows, key=lambda r: r[2]), min(rows, key=lambda r: r[3])
    return {"interval": interval, "n": len(rows), "first_ts": rows[0][0], "first_open": rows[0][1],
            "max": hi[2], "max_ts": hi[0], "min": lo[3], "min_ts": lo[0], "last_close": rows[-1][4],
            "last_ts": rows[-1][0]}


def parse_coingecko_contract(data):
    """Ficha de CoinGecko por contrato: id, símbolo, categorías y pares en Binance / Coinbase / Kraken."""
    if not isinstance(data, dict) or not data.get("id"):
        return None
    cex = {}
    for t in data.get("tickers") or []:
        exchange = CG_EXCHANGES.get(((t.get("market") or {}).get("identifier") or "").lower())
        base, quote = str(t.get("base") or "").upper(), str(t.get("target") or "").upper()
        if (exchange and quote in CEX_QUOTES and re.fullmatch(r"[A-Z0-9]{1,15}", base)
                and [base, quote] not in cex.get(exchange, [])):
            cex.setdefault(exchange, []).append([base, quote])
    return {"listed": True, "id": data["id"], "symbol": str(data.get("symbol") or "").upper(),
            "categories": [c for c in data.get("categories") or [] if c], "cex": cex}


def parse_binance_symbol(data, symbol):
    symbols = (data or {}).get("symbols") or []
    return any(s.get("symbol") == symbol and s.get("status") == "TRADING" for s in symbols)


def parse_coinbase_product(data):
    return bool(data) and data.get("status") == "online" and not data.get("trading_disabled")


def cex_route(symbol, live):
    """Ruta por exchange centralizado: listados confirmados por contrato, con enlace limpio. Devuelve (texto, enlaces)."""
    cg, cex = (live or {}).get("coingecko"), (live or {}).get("cex")
    sym = (symbol or "").upper()
    if sym in BLUE_CHIPS:
        links = [(name, CEX_LINKS[name].format(base=sym, quote="USDT" if name == "Binance" else "USD"))
                 for name in ("Binance", "Coinbase", "Kraken")]
        return "Cotiza en exchanges centralizados (blue chip): " + " · ".join(f"{n} ({u})" for n, u in links), links
    if cg is None and cex is None:
        return "Ruta por exchange centralizado: n/d (sin consulta a CoinGecko, Binance ni Coinbase).", []
    when_txt = when(parse_ts((cex or {}).get("at") or (live or {}).get("queried_at")))
    confirmed = (cg or {}).get("cex") or {}
    links = [(name, CEX_LINKS[name].format(base=pair[0], quote=pair[1]))
             for name in ("Binance", "Coinbase", "Kraken") for pair in confirmed.get(name, [])[:1]]
    notes = []
    for name, key, pair in (("Binance", "binance", f"{(cex or {}).get('symbol', sym)}USDT"),
                            ("Coinbase", "coinbase", f"{(cex or {}).get('symbol', sym)}-USD")):
        if (cex or {}).get(key) and name not in confirmed:
            notes.append(f"{name} tiene un par {pair}, pero CoinGecko no lo vincula a este contrato (puede ser otro "
                         "token con el mismo símbolo): no se enlaza")
    if links:
        text = ("Cotiza en exchanges centralizados (par confirmado por contrato en CoinGecko, consulta "
                f"{when_txt}): " + " · ".join(f"{n} ({u})" for n, u in links))
    elif (cg or {}).get("listed") is False or (cex and cex.get("binance") is not None):
        source = ("CoinGecko sin ficha para este contrato" if (cg or {}).get("listed") is False else
                  "CoinGecko sin pares de este contrato en esos exchanges" if cg else "CoinGecko n/d")
        text = f"Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta {when_txt}; {source})."
    else:
        text = "Ruta por exchange centralizado: n/d (consulta fallida)."
    return text + "".join(f" {n}." for n in notes), links


def asset_dual_metric(pool, t0, p0, now=None):
    """Métrica dual del activo con velas de 15 min (mismas definiciones y orden intra-vela que la calibración)."""
    status, candles = cal.CandleSource().get(pool, t0)
    if status != "ok":
        return {"status": status}
    out = cal.evaluate_outcome(candles, p0, t0, now or time.time())
    up = p0 * (1 + cal.EVENT_UP)
    first_up = next((c[0] for c in candles if c[2] >= up), None)
    out.update({"status": "ok" if candles else "sin_velas", "hours_to_up": (first_up - t0) / 3600 if first_up else None,
                "candle_min": cal.CANDLE_S // 60})
    return out


def fetch_live(mint, chain, record=None, t0=None, p0=None, session=None, pause_s=HTTP_PAUSE_S):
    """Consultas gratuitas, sin key. Cada llamada queda registrada con URL, estado y momento."""
    session = session or requests.Session()
    calls = []

    def get(source, url):
        at = datetime.now(timezone.utc)
        try:
            r = session.get(url, timeout=HTTP_TIMEOUT_S, headers=HTTP_HEADERS)
            status, data = r.status_code, (r.json() if r.ok else None)
        except (requests.RequestException, ValueError) as e:
            status, data = f"error {type(e).__name__}", None
        calls.append({"source": source, "url": url, "status": status, "at": iso(at)})
        if pause_s:
            time.sleep(pause_s)
        return data

    live = {"queried_at": iso(datetime.now(timezone.utc)), "calls": calls, "rugcheck": None, "goplus": None,
            "history": None, "dual": None}
    live["dexscreener"] = parse_dexscreener(get("DexScreener", DEXSCREENER_TOKENS.format(addr=mint)), chain)
    if chain == "solana":
        live["rugcheck"] = parse_rugcheck(get("RugCheck", RUGCHECK_REPORT.format(addr=mint)))
        live["goplus"] = parse_goplus(get("GoPlus", GOPLUS_SOLANA.format(addr=mint)), mint, chain)
    elif chain in GOPLUS_CHAIN_IDS:
        url = GOPLUS_EVM.format(chain_id=GOPLUS_CHAIN_IDS[chain], addr=mint)
        live["goplus"] = parse_goplus(get("GoPlus", url), mint, chain)
    pool = (live["dexscreener"] or {}).get("pair") or _dx(record or {}).get("pairAddress")
    if pool and chain in GECKO_NETWORKS:
        url = GECKO_OHLCV_HOUR.format(net=GECKO_NETWORKS[chain], pool=pool)
        live["history"] = parse_ohlcv(get("GeckoTerminal (velas 1 h)", url))
    platform = COINGECKO_PLATFORMS.get(chain)
    if platform:
        data = get("CoinGecko (ficha por contrato)", COINGECKO_CONTRACT.format(platform=platform, addr=mint))
        live["coingecko"] = (parse_coingecko_contract(data) if data else
                             {"listed": False} if calls[-1]["status"] == 404 else None)
    symbol = ((live.get("coingecko") or {}).get("symbol") or ((record or {}).get("token") or {}).get("symbol")
              or (record or {}).get("symbol") or "").upper()
    if re.fullmatch(r"[A-Z0-9]{1,15}", symbol):
        b = get("Binance (data-api)", BINANCE_EXCHANGE_INFO.format(symbol=f"{symbol}USDT"))
        binance = parse_binance_symbol(b, f"{symbol}USDT") if b else (False if calls[-1]["status"] == 400 else None)
        c = get("Coinbase (API pública)", COINBASE_PRODUCT.format(product=f"{symbol}-USD"))
        coinbase = parse_coinbase_product(c) if c else (False if calls[-1]["status"] == 404 else None)
        live["cex"] = {"symbol": symbol, "binance": binance, "coinbase": coinbase, "at": iso(datetime.now(timezone.utc))}
    pool_at_detection = _dx(record or {}).get("pairAddress")
    if chain == "solana" and pool_at_detection and t0 and p0:
        at = datetime.now(timezone.utc)
        live["dual"] = asset_dual_metric(pool_at_detection, t0, p0)
        calls.append({"source": "GeckoTerminal (velas 15 min, métrica dual)",
                      "url": cal.GT_OHLCV.format(pool=pool_at_detection), "status": live["dual"].get("status"),
                      "at": iso(at)})
    return live


# ---------------------------------------------------------------------------
# Datos del repo
# ---------------------------------------------------------------------------

def _read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return None


def git_blob(path):
    """Blob de git del archivo. `git hash-object` aplica los filtros del repo (p. ej., autocrlf en Windows), así que
    coincide con `git ls-tree`; sin git, se calcula sobre los bytes del disco."""
    try:
        out = subprocess.run(["git", "hash-object", "--", Path(path).name], cwd=str(Path(path).resolve().parent),
                             capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", out.stdout.strip()):
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    data = Path(path).read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def git_trace(path):
    """Ruta relativa + blob + último commit que tocó el archivo (None si no está commiteado)."""
    if not path or not Path(path).exists():
        return None
    path = Path(path)
    try:
        rel = path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        rel = path.as_posix()
    commit = commit_date = None
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%h|%cI", "--", rel], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and "|" in out.stdout:
            commit, commit_date = out.stdout.strip().split("|", 1)
    except (OSError, subprocess.SubprocessError):
        pass
    return {"path": rel, "blob": git_blob(path), "commit": commit, "commit_date": commit_date}


def find_detection_file(mint, t_ref):
    """Archivo de la corrida de script_82 que contiene el mint, en la hora previa a la alerta."""
    if not t_ref or not DETECTION_DIR.exists():
        return None
    candidates = []
    for f in DETECTION_DIR.glob("detection_*.json"):
        ts = parse_ts(f.stem.replace("detection_", ""))
        if ts and t_ref - timedelta(minutes=DETECTION_LOOKBACK_MIN) <= ts <= t_ref:
            candidates.append((ts, f))
    for _, f in sorted(candidates, reverse=True):
        data = _read_json(f) or {}
        if mint in (data.get("enriched") or {}):
            return f
    return None


def population_histogram(accumulated, version):
    """Distribución de scores del scorer `version` en el acumulado: {score: cantidad}."""
    hist = {}
    for rec in (accumulated or {}).values():
        score = rec.get("score") if isinstance(rec, dict) else None
        if rec.get("scoring_version") == version and isinstance(score, int):
            hist[str(score)] = hist.get(str(score), 0) + 1
    return {"version": version, "n": sum(hist.values()), "hist": hist,
            "source": "02_Analisis/shadow_v4/_accumulated.json"}


def load_alert_data(mint, chain=None):
    """Registro exacto de la alerta (o del acumulado), entrada del historial, señales, trazas y contexto."""
    alerts = s97.load_alerts(str(ALERTS_DIR / "_all_alerts.json"))
    entries = [a for a in alerts if a.get("mint") == mint]
    alert = entries[-1] if entries else None
    record, record_path = None, None
    if alert:
        path = ALERTS_DIR / f"alert_{mint}_{alert['timestamp']}.json"
        record = _read_json(path)
        record_path = path if record else None
    accumulated = _read_json(ACCUMULATED_FILE) or {}
    if record is None and isinstance(accumulated.get(mint), dict):
        record, record_path = accumulated[mint], ACCUMULATED_FILE
    if record is None:
        return None
    chain = (chain or s97.detection_facts(record)["chain"]).lower()
    signals = _read_json(SIGNALS_DIR / chain / f"{mint}.json") or _read_json(SIGNALS_DIR / f"{mint}.json")
    t_ref = parse_ts(alert["timestamp"]) if alert else parse_ts(record.get("detected_at"))
    detection = find_detection_file(mint, t_ref)
    shadow = (_read_json(SHADOW_MONITOR_FILE) or {}).get("by_version") or {}
    version = current_scorer_version()
    return {"record": record, "record_trace": git_trace(record_path), "alert": alert, "signals": signals,
            "detection_trace": git_trace(detection) if detection else None,
            "population": population_histogram(accumulated, version), "calibration": s97.load_emission_calibration(),
            "shadow": shadow, "scanner": scanner_index(_read_json(SCANNER_FILE)),
            "narratives": registry_matches(_read_json(NARRATIVE_REGISTRY), mint)}


def scanner_index(scan):
    """Índice del último escaneo de script_114: id de CoinGecko -> (grupo, categoría) y contrato -> grupo a."""
    if not isinstance(scan, dict):
        return None
    by_id, by_address = {}, {}
    for group, data in (scan.get("groups") or {}).items():
        for item in (data or {}).get("items") or []:
            if item.get("id"):
                by_id.setdefault(item["id"], {"group": group, "category": item.get("source")})
    for net, data in (scan.get("onchain") or {}).items():
        for item in (data or {}).get("items") or []:
            if item.get("token_address"):
                by_address.setdefault(str(item["token_address"]).lower(),
                                      {"group": "a", "category": f"trending_pools de {net}"})
    return {"scanned_at": scan.get("generated_at"), "by_id": by_id, "by_address": by_address}


def scanner_match(index, address, coingecko_id=None):
    """Grupo del scanner en el que aparece el activo (por contrato o por id de CoinGecko). None si no aparece."""
    if not index:
        return None
    hit = index["by_address"].get(str(address or "").lower()) or (index["by_id"].get(coingecko_id) if coingecko_id else None)
    if not hit:
        return None
    return {**hit, "label": GROUPS.get(hit["group"], (hit["group"],))[0], "scanned_at": index.get("scanned_at")}


def registry_matches(registry, address):
    """Narrativas del registro curado (04_Config/narrative_registry.json) que vinculan este contrato."""
    out = []
    for key, n in ((registry or {}).get("narratives") or {}).items():
        for t in n.get("tokens") or []:
            if str(t.get("address") or "").lower() == str(address).lower():
                out.append({"narrative": key, "title": n.get("title"), "link_type": t.get("link_type")})
    return out


def categories_text(live, scanner, narratives):
    """Categoría y narrativa: CoinGecko (por contrato) + grupo del scanner + registro curado. Sin dato: n/d."""
    parts = []
    cg = (live or {}).get("coingecko")
    if cg and cg.get("categories"):
        cats = cg["categories"][:8]
        parts.append("CoinGecko: " + ", ".join(cats) + (f" (+{len(cg['categories']) - 8})" if len(cg["categories"]) > 8 else ""))
    if scanner:
        parts.append(f"scanner multi-chain: grupo {scanner['group']} ({scanner['label']}"
                     + (f", {scanner['category']}" if scanner.get("category") else "") + ")")
    for n in narratives or []:
        parts.append(f"narrativa: {n['title']} (vínculo {n['link_type']}, registro curado)")
    if parts:
        return " · ".join(parts)
    if (cg or {}).get("listed") is False:
        return "n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)"
    return "n/d (sin categoría de CoinGecko consultada; sin narrativa en el registro curado)"


# ---------------------------------------------------------------------------
# Construcción del dossier
# ---------------------------------------------------------------------------

def _detected_dt(record, detection_trace, alert):
    dt = parse_ts(record.get("detected_at"))
    if dt is None and detection_trace:
        dt = parse_ts(Path(detection_trace["path"]).stem.replace("detection_", ""))
    if dt is None and alert:
        dt = parse_ts(alert.get("timestamp"))
    return dt


def _launchpad(record, mint, signals):
    tok, dx = record.get("token") or {}, _dx(record)
    curve = (((signals or {}).get("signals") or {}).get("onchain") or {}).get("bonding_curve") or {}
    if curve.get("launchpad"):
        return curve["launchpad"], curve.get("graduated_at")
    if (tok.get("pool") == "pump" or str(tok.get("url", "")).startswith("https://pump.fun")
            or str(dx.get("dexId", "")).startswith("pump") or str(mint).endswith("pump")):
        return "pump.fun", curve.get("graduated_at")
    return None, None


def _probabilities(calibration, shadow, version):
    def item(k, n):
        return {"k": k, "n": n, "rate": k / n if n else None, "ci90": cal.wilson(k, n)}

    hist = {key: item(*kn) for key, kn in HISTORICAL.items()}
    if calibration:
        return {"status": "validada", "scoring_version": calibration.get("scoring_version"),
                "threshold": calibration.get("threshold"),
                "primary": calibration["primary"], "secondary": calibration["secondary"],
                "post_hit": calibration["rug_after_primary_hit"], "historical": hist}
    partial = (shadow or {}).get(version) or {}
    return {"status": "en validación", "scoring_version": version, "criteria_min_n": 20,
            "shadow_primary": partial.get("primary"), "shadow_secondary": partial.get("secondary"),
            "historical": hist}


def _percentile(hist, score):
    n = sum(hist.values())
    if not n or score is None:
        return None
    below = sum(c for s, c in hist.items() if int(s) < score)
    equal = hist.get(str(score), 0)
    return (below + 0.5 * equal) / n


def build_dossier(mint, chain, alert_data, live=None, now=None, mode="live"):
    """Dict con la presentación y las 7 secciones del doc 24, más 'missing' y 'emitible' (regla núcleo)."""
    now = now or datetime.now(timezone.utc)
    record = alert_data.get("record") or {}
    alert = alert_data.get("alert") or {}
    signals = alert_data.get("signals")
    rtrace, dtrace = alert_data.get("record_trace"), alert_data.get("detection_trace")
    live = live or {}
    lds, lrc, lgp = live.get("dexscreener"), live.get("rugcheck"), live.get("goplus")
    chain = (chain or s97.detection_facts(record)["chain"]).lower()
    record = {**record, "chain": chain}
    facts = s97.detection_facts(record)
    snap = s97.market_snapshot(record)
    dx, tok = _dx(record), record.get("token") or {}
    symbol = tok.get("symbol") or alert.get("symbol") or record.get("symbol")
    name = facts["name"] or ((lrc or {}).get("name")) or symbol
    chain_label = s97.CHAIN_LABELS.get(chain, chain)
    queried = parse_ts(live.get("queried_at"))
    q_label = f"consulta {when(queried)}" if queried else "sin consulta en vivo"
    detected = _detected_dt(record, dtrace, alert)
    alerted = parse_ts(alert.get("timestamp")) if alert else None
    t_window = alerted or detected
    expires = t_window + timedelta(hours=WINDOW_H) if t_window else None
    created = facts["created"] or from_ms((lds or {}).get("pair_created_ms"))
    age_det = (detected - created).total_seconds() / 60 if detected and created and detected >= created else None
    age_alert = (alerted - created).total_seconds() / 60 if alerted and created and alerted >= created else None
    age_now = (now - created).total_seconds() / 60 if created else None
    version_reg = record.get("scoring_version") or "7.2-preR1"
    version_cur = current_scorer_version()
    entry = _num(alert.get("initial_price")) or snap["price"]
    onchain = ((signals or {}).get("signals") or {}).get("onchain") or {}

    # --- 🛒 1. Cómo adquirir -------------------------------------------------------------------
    guide = s97.ACQUISITION_GUIDES.get(chain)
    explorer = s97.EXPLORERS.get(chain)
    pair_det = facts["pair"]
    pair_now = (lds or {}).get("pair") or pair_det
    explorer_url = explorer[1].format(addr=mint) if explorer and mint else None
    dexscreener_url = (f"https://dexscreener.com/{chain}/{pair_now or mint}"
                       if chain in s97.DEXSCREENER_CHAINS and (pair_now or mint) else None)
    launchpad, graduated_at = _launchpad(record, mint, signals)
    launchpad_url = f"https://pump.fun/coin/{mint}" if launchpad == "pump.fun" and mint else None
    study = [liquidity_row(f"al detectar · {when(detected)}", facts["dex"], pair_det, snap["liquidity"])]
    if lds:
        study.append(liquidity_row(q_label, lds.get("dex"), lds.get("pair"), lds.get("liquidity")))
    ref = study[-1]
    rc_auth = gp_auth = None
    if lrc:
        rc_auth = (lrc["mint_authority"] is None, lrc["freeze_authority"] is None)
    if lgp and chain == "solana":
        gp_auth = (lgp.get("mintable") is False, lgp.get("freezable") is False)
    auth_text = _authority_text(rc_auth, gp_auth, onchain)
    holders, top10 = _holders(lrc, onchain)
    verify_facts = (f"mint authority / freeze authority: {auth_text} · holders {fmt_int(holders)} · "
                    f"top-10 {fmt_pct(top10 / 100 if top10 is not None else None, 2)} ({q_label})")
    if lgp and chain != "solana":
        verify_facts = (f"impuesto de compra / venta: {fmt_pct(lgp.get('buy_tax'), 1)} / "
                        f"{fmt_pct(lgp.get('sell_tax'), 1)} · honeypot: {_yes_no(lgp.get('honeypot'))} · "
                        f"contrato verificado: {_yes_no(lgp.get('open_source'))} (GoPlus, {q_label})")
    acquisition = {"chain": chain, "chain_label": chain_label, "guide_available": bool(guide), "mint": mint}
    if guide:
        (w1, wu1), *wrest = guide["wallets"]
        (d1, du1), *dalts = guide["dexes"]
        main_dex = (lds or {}).get("dex") or facts["dex"]
        cex, cex_links = cex_route(symbol, live)
        address_word = guide["address_word"]
        steps = [
            f"Instalar la wallet: {w1} ({wu1})" + "".join(f" o {n} ({u})" for n, u in wrest),
            f"Fondearla con {guide['fund']}, comprados en {s97.FUNDING_EXCHANGES} y enviados a la dirección de la "
            f"wallet. Dejar un resto de {guide['native']} para las comisiones de red",
            f"Conectar la wallet a {d1} ({du1})" + (f"; la liquidez principal está en {main_dex}" if main_dex else ""),
            f"Pegar el {address_word} y verificar que coincide carácter por carácter: `{mint}`",
            f"Configurar el slippage: {ref['slippage']} (liquidez {fmt_usd(ref['liquidity'])}, {ref['moment']})",
            f"Verificar el contrato en {explorer[0] if explorer else 'el explorador'} ({explorer_url or 'n/d'}) y el par "
            f"en DexScreener ({dexscreener_url or 'n/d'}); {verify_facts}",
            "Ejecutar el swap",
            f"Confirmar la transacción en {explorer[0] if explorer else 'el explorador'}. Si el token no aparece en "
            f"la wallet, agregarlo pegando el {address_word}",
        ]
        acquisition.update({
            "wallets": guide["wallets"], "dexes": guide["dexes"], "fund": guide["fund"], "native": guide["native"],
            "address_word": address_word, "funding_exchanges": s97.FUNDING_EXCHANGES, "cex_route": cex,
            "cex_links": cex_links,
            "main_dex": main_dex, "liquidity_study": study, "slippage": ref["slippage"], "steps": steps,
            "verification": {"explorer": [explorer[0], explorer_url] if explorer and explorer_url else None,
                             "dexscreener": dexscreener_url, "launchpad": launchpad_url, "facts": verify_facts},
            "swap_links": "[P] enlaces de swap con el par precargado: pendientes de verificación manual de "
                          "Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar",
        })

    # --- 📊 2. Identificación ------------------------------------------------------------------
    deployer, deployer_src = _deployer(tok, lrc, onchain)
    lp_text = ("; ".join(f"{m or 'mercado'} {fmt_pp(p, 0, signed=False)}" for m, p in lrc["lp_locked"])
               if lrc and lrc["lp_locked"] else "n/d")
    eff = _effective_holders((lrc or {}).get("top10"))
    links = [("DexScreener", dexscreener_url), (explorer[0] if explorer else "Explorador", explorer_url),
             ("pump.fun", launchpad_url)]
    links += [("web", u) for u in (lds or {}).get("websites", [])]
    links += [(t or "red social", u) for t, u in (lds or {}).get("socials", [])]
    link_text = " · ".join(f"{label}: {url}" for label, url in links if url) or "n/d"
    if lds is not None and not lds.get("websites") and not lds.get("socials"):
        link_text += " · web / Telegram / X: no publicados en DexScreener"
    identification = {
        "name": name, "symbol": symbol, "mint": mint, "chain": chain, "dex": facts["dex"], "pair": pair_det,
        "deployer": deployer, "pair_created": iso(created), "age_detection_min": age_det, "age_alert_min": age_alert,
        "age_now_min": age_now, "authority": auth_text, "holders": holders, "top10_pct": top10,
        "effective_holders_top10": eff, "lp_locked": lp_text, "rugcheck_labels": (lrc or {}).get("labels"),
        "rows": [
            ("Nombre / symbol", f"{name or 'n/d'} / {symbol or 'n/d'}", f"registro de la detección ({record.get('source') or 'n/d'})"),
            ("Mint / contrato", f"`{mint}`" if mint else "n/d", "registro de la detección"),
            ("Chain / DEX / par", f"{chain_label} / {facts['dex'] or 'n/d'} / `{pair_det or 'n/d'}`",
             "DexScreener, al detectar" + (f" ({lds['n_pairs']} par(es) en la {q_label})" if lds else "")),
            ("Deployer", f"`{deployer}`" if deployer else "n/d", deployer_src),
            ("Par creado", when(created), "DexScreener `pairCreatedAt`"),
            ("Edad del par al detectar / al alertar / ahora", f"{fmt_age(age_det)} / {fmt_age(age_alert)} / {fmt_age(age_now)}",
             "cálculo con `pairCreatedAt`"),
            ("Mint / freeze authority", auth_text, _authority_sources(rc_auth, gp_auth, onchain, q_label)),
            ("Holders / top-10", f"{fmt_int(holders)} / {fmt_pct(top10 / 100 if top10 is not None else None, 2)}",
             _holders_source(lrc, onchain, q_label)),
            ("Holders efectivos del top-10", fmt_num(eff, 1) if eff else "n/d",
             "(Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo"),
            ("Liquidez bloqueada", lp_text, f"RugCheck `markets[].lp.lpLockedPct`, {q_label}" if lrc else "RugCheck [P]"),
            ("Etiquetas de RugCheck", ", ".join(f"«{x}»" for x in lrc["labels"]) if lrc and lrc["labels"] else
             ("ninguna" if lrc else "n/d"), f"RugCheck `risks[].name` (texto de la fuente), {q_label}" if lrc else "RugCheck [P]"),
            ("Links", link_text, q_label if lds else "registro de la detección"),
        ],
    }

    # --- 🧬 3. Naturaleza -----------------------------------------------------------------------
    group = record.get("group") or ("h" if (symbol or "").upper() in BLUE_CHIPS else ("a" if launchpad else None))
    asset_type = "Memecoin" if launchpad else (GROUPS[group][1] if group in GROUPS else "n/d")
    origin = (f"lanzada en {launchpad}" + (f", migrada a {facts['dex']}" if facts["dex"] else "")
              if launchpad else "n/d")
    description = (lrc or {}).get("description")
    history = [f"Par creado el {when(created)} (DexScreener `pairCreatedAt`)." if created else
               "Fecha de creación del par: n/d (el registro no guarda `pairCreatedAt` y no hubo consulta)."]
    if graduated_at:
        history.append(f"Migración desde la bonding curve: {when(parse_ts(graduated_at))} (Jupiter, señales on-chain).")
    if detected:
        history.append(f"Detectado el {when(detected)}, con el par a {fmt_age(age_det)} de creado: precio "
                       f"{fmt_price(snap['price'])}, mcap {fmt_usd(snap['mcap_usd'])}, liquidez {fmt_usd(snap['liquidity'])}.")
    h = live.get("history")
    if h:
        first = datetime.fromtimestamp(h["first_ts"], timezone.utc)
        history.append(
            f"Velas de {h['interval']} de GeckoTerminal ({h['n']}, desde {when(first)}): apertura {fmt_price(h['first_open'])}"
            f" · máximo {fmt_price(h['max'])} ({when(datetime.fromtimestamp(h['max_ts'], timezone.utc))})"
            f" · mínimo {fmt_price(h['min'])} ({when(datetime.fromtimestamp(h['min_ts'], timezone.utc))})"
            f" · último cierre {fmt_price(h['last_close'])}.")
    if lds:
        history.append(f"En la {q_label}: precio {fmt_price(lds.get('price'))}, liquidez {fmt_usd(lds.get('liquidity'))}, "
                       f"FDV {fmt_usd(lds.get('fdv'))}.")
    nature = {"type": asset_type, "group": group, "group_label": GROUPS[group][0] if group in GROUPS else None,
              "origin": origin,
              "categories": categories_text(live, scanner_match(alert_data.get("scanner"), mint,
                                                                (live.get("coingecko") or {}).get("id")),
                                            alert_data.get("narratives")),
              "description": description or None,
              "description_source": f"RugCheck `fileMeta.description` (metadata del token), {q_label}" if lrc else None,
              "history": history}

    # --- 🔬 4. Método ---------------------------------------------------------------------------
    inputs = [("Precio", fmt_price(snap["price"])), ("Liquidez", fmt_usd(snap["liquidity"])),
              ("MCap", fmt_usd(snap["mcap_usd"])), ("Volumen 24 h", fmt_usd(snap["volume_24h"])),
              ("Cambio 24 h", fmt_pp(_num(dx.get("priceChange24h")), 0)),
              ("Cambio m5 / h1", f"{fmt_pp(_num(dx.get('priceChange_m5')))} / {fmt_pp(_num(dx.get('priceChange_h1')))}"),
              ("Volumen m5 / h1", f"{fmt_usd(_num(dx.get('volume_m5')))} / {fmt_usd(_num(dx.get('volume_h1')))}"),
              ("Trades m5 (compras / ventas)", f"{fmt_int(_num(dx.get('txns_m5_buys')))} / {fmt_int(_num(dx.get('txns_m5_sells')))}"),
              ("Edad del par", fmt_age(age_det)),
              ("Score del feed (WS)", fmt_int(_num(tok.get("score"))) if tok.get("score") is not None else "n/d (feed sin score)")]
    probs = _probabilities(alert_data.get("calibration"), alert_data.get("shadow"), version_cur)
    method = {"scorer_version_registered": version_reg, "scorer_version_current": version_cur,
              "inputs": inputs, "inputs_source": f"DexScreener vía script_82, al detectar: {when(detected)}",
              "probabilities": probs}

    # --- 🎯 5. Fundamento -----------------------------------------------------------------------
    breakdown = score_breakdown(record, age_det)
    t_score = detected.timestamp() if detected else (t_window.timestamp() if t_window else now.timestamp())
    recomputed = alert_data.get("recomputed") or recompute_current(record, t_score)
    pop = alert_data.get("population") or {}
    hist = pop.get("hist") or {}
    score_cur = record.get("score") if version_reg == version_cur else recomputed.get("score")
    threshold = s97.EMIT_MIN_SCORE
    k_ge = sum(c for s, c in hist.items() if int(s) >= threshold)
    shadow_cur = (alert_data.get("shadow") or {}).get(version_cur) or {}
    baseline = ((shadow_cur.get("criteria") or {}).get("baseline_primary")) or BASELINE_PRIMARY
    foundation = {"breakdown": breakdown, "recomputed": recomputed, "threshold": threshold,
                  "population": {"version": pop.get("version"), "n": pop.get("n"), "k_ge_threshold": k_ge,
                                 "share_ge_threshold": k_ge / pop["n"] if pop.get("n") else None,
                                 "score_current_version": score_cur, "percentile": _percentile(hist, score_cur),
                                 "source": pop.get("source")},
                  "baseline_primary": baseline, "top_reasons": [r for r in record.get("reasons") or []
                                                                if not str(r).startswith("v7.2.1:")][:3]}

    # --- ⏱️ 6. Vigencia -------------------------------------------------------------------------
    remaining_h = (expires - now).total_seconds() / 3600 if expires else None
    if remaining_h is None:
        window_status = "n/d"
    elif remaining_h > 0:
        window_status = f"vigente: quedan {fmt_num(remaining_h, 1)} h"
    else:
        window_status = f"vencida hace {fmt_num(-remaining_h, 1)} h"
    vm5, vh1 = _num(dx.get("volume_m5")), _num(dx.get("volume_h1"))
    tracking = [{"stage": u.get("stage"), "at": iso(parse_ts(u.get("timestamp"))), "price": _num(u.get("price")),
                 "change_pct": _num(u.get("price_change_pct")), "label": u.get("stage_verdict")}
                for u in alert.get("trust_updates") or []]
    current_change = (lds["price"] / entry - 1) if lds and lds.get("price") and entry else None
    validity = {"window_from": iso(t_window), "expires": iso(expires), "window_status": window_status,
                "acceleration": {"m5": _num(dx.get("priceChange_m5")), "h1": _num(dx.get("priceChange_h1")),
                                 "h24": _num(dx.get("priceChange24h")),
                                 "vol_ratio": vm5 / vh1 if vm5 is not None and vh1 else None,
                                 "age_min": age_det},
                "entry_price": entry, "tracking": tracking,
                "current": {"price": (lds or {}).get("price"), "change": current_change, "label": q_label},
                "dual": live.get("dual"), "historical": HISTORICAL_DURATION}

    # --- 📚 7. Fuentes --------------------------------------------------------------------------
    rel = (rtrace or {}).get("path")
    clock = recomputed.get("clock") or iso(datetime.fromtimestamp(t_score, timezone.utc))
    audit_cmd = (
        "python -c \"import json,importlib.util as u;from unittest import mock;"
        "s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');"
        "m=u.module_from_spec(s);s.loader.exec_module(m);"
        f"d=json.load(open('{rel}',encoding='utf-8'));d=d.get('{mint}',d);"
        f"p=mock.patch('time.time',return_value={t_score:.0f});p.start();"
        "print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))\""
    ) if rel else None
    consistency = []
    if lds and lrc and lds.get("liquidity") and lrc.get("total_liquidity"):
        a, b = lds["liquidity"], lrc["total_liquidity"]
        consistency.append(("Liquidez DexScreener vs RugCheck", f"{fmt_usd(a)} vs {fmt_usd(b)}",
                            fmt_pct(abs(a - b) / max(a, b), 2)))
    if lds and lds.get("price") and h and h.get("last_close"):
        a, b = lds["price"], h["last_close"]
        consistency.append(("Precio DexScreener vs último cierre 1 h de GeckoTerminal", f"{fmt_price(a)} vs {fmt_price(b)}",
                            fmt_pct(abs(a - b) / max(a, b), 2)))
    detection_url = f"https://api.dexscreener.com/latest/dex/tokens/{mint}"
    sources = {"record": rtrace, "detection": dtrace,
               "alert": {"timestamp": alert.get("timestamp"), "status": alert.get("status")} if alert else None,
               "calls": [{"source": "DexScreener (vía script_82)", "url": detection_url, "status": None,
                          "at": iso(detected)}] + list(live.get("calls") or []),
               "consistency": consistency,
               "commands": {"score": audit_cmd, "score_clock": clock,
                            "dossier": f"python 04_Config/scripts/script_113_dossier_builder.py --mint {mint} --chain {chain} --stdout",
                            "dual": "python 04_Config/scripts/monitor_shadow.py"}}

    # --- 🎴 Presentación ------------------------------------------------------------------------
    detected_by = ", ".join(foundation["top_reasons"]) or "n/d"
    presentation = [
        f"🎴 {asset_type} en {chain_label}" + (f" ({origin})" if launchpad else "") +
        f" · precio {fmt_price(snap['price'])} · liquidez {fmt_usd(snap['liquidity'])} · mcap {fmt_usd(snap['mcap_usd'])} (al detectar)",
        f"Detectado el {when(detected)} por: {detected_by} (score {record.get('score', 'n/d')}, scorer {version_reg})",
        f"Cómo adquirirlo: {acquisition['wallets'][0][0]} → {acquisition['dexes'][0][0]} · slippage {acquisition['slippage']}"
        if guide else f"Cómo adquirirlo: sin guía de compra verificada para {chain_label}",
        f"Ventana de la señal: hasta el {when(expires)} (< {WINDOW_H} h) · {window_status}",
        "Material educativo y documentación del método. No es asesoría financiera.",
    ]

    dossier = {
        "meta": {"dossier_version": DOSSIER_VERSION, "built_at": iso(now), "mode": mode,
                 "queried_at": live.get("queried_at")},
        "asset": {"mint": mint, "symbol": symbol, "name": name, "chain": chain, "chain_label": chain_label},
        "presentation": presentation, "acquisition": acquisition, "identification": identification,
        "nature": nature, "method": method, "foundation": foundation, "validity": validity, "sources": sources,
        "inputs": {"record": record, "alert": alert or None, "live": live or None},
    }
    dossier["meta"]["input_sha256"] = hashlib.sha256(
        json.dumps(dossier["inputs"], sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")).hexdigest()
    dossier["missing"] = check_required(dossier)
    dossier["emitible"] = not dossier["missing"]
    return dossier


def _yes_no(flag):
    return "n/d" if flag is None else ("sí" if flag else "no")


def _authority_text(rc_auth, gp_auth, onchain):
    pairs = [x for x in (rc_auth, gp_auth) if x is not None]
    tp = onchain.get("token_program") or {}
    if not pairs and "mint_authority_disabled" in tp:
        pairs = [(bool(tp.get("mint_authority_disabled")), bool(tp.get("freeze_authority_disabled")))]
    if not pairs:
        return "n/d"
    mint_rev = {p[0] for p in pairs}
    freeze_rev = {p[1] for p in pairs}

    def word(values):
        return ("revocada" if values == {True} else "activa") if len(values) == 1 else "las fuentes difieren"

    return f"{word(mint_rev)} / {word(freeze_rev)}"


def _authority_sources(rc_auth, gp_auth, onchain, q_label):
    used = [n for n, x in (("RugCheck", rc_auth), ("GoPlus", gp_auth)) if x is not None]
    if used:
        return f"{' y '.join(used)}, {q_label}"
    if "mint_authority_disabled" in (onchain.get("token_program") or {}):
        return "Jupiter (señales on-chain del repo)"
    return "GoPlus / RugCheck [P: sin consulta]"


def _holders(lrc, onchain):
    if lrc and lrc.get("holders") is not None:
        return lrc["holders"], lrc.get("top10_pct")
    dist = onchain.get("holder_distribution") or {}
    return _num(dist.get("holder_count")), _num(dist.get("top_holders_pct"))


def _holders_source(lrc, onchain, q_label):
    if lrc and lrc.get("holders") is not None:
        return f"RugCheck `totalHolders` y suma de `topHolders[:10].pct`, {q_label}"
    if onchain.get("holder_distribution"):
        return "Jupiter (señales on-chain del repo)"
    return "RugCheck [P: sin consulta]"


def _deployer(tok, lrc, onchain):
    if tok.get("traderPublicKey"):
        return tok["traderPublicKey"], "PumpPortal (evento create), al detectar"
    if lrc and lrc.get("creator"):
        return lrc["creator"], "RugCheck `creator`"
    wallet = (onchain.get("creator_wallet") or {}).get("address")
    if wallet:
        return wallet, "Jupiter `dev` (señales on-chain del repo)"
    return None, "n/d (fuente: RugCheck `creator`)"


def _effective_holders(top):
    """Número efectivo de holders del top-10 (inversa del índice de Herfindahl normalizado)."""
    top = [p for p in (top or []) if p and p > 0]
    if not top:
        return None
    return sum(top) ** 2 / sum(p * p for p in top)


def check_required(d):
    """Checklist del doc 24 (Anexo A): campos obligatorios. Si falta alguno, el dossier no se emite."""
    a, missing = d["acquisition"], []
    if not d["asset"]["mint"]:
        missing.append("mint / contrato")
    if not a["guide_available"]:
        missing.append(f"guía de compra para la chain '{a['chain']}'")
    else:
        if not a.get("wallets") or not all(url for _, url in a["wallets"]):
            missing.append("wallet con enlace oficial")
        if not a.get("dexes") or not all(url for _, url in a["dexes"]):
            missing.append("DEX con enlace oficial")
        if not a.get("fund"):
            missing.append("activo para fondear")
        if len(a.get("steps") or []) != 8:
            missing.append("los 8 pasos")
        if not a.get("slippage"):
            missing.append("slippage sugerido")
        verification = a.get("verification") or {}
        if not verification.get("explorer"):
            missing.append("enlace al explorador")
        if not verification.get("dexscreener"):
            missing.append("enlace a DexScreener")
    if not d["asset"]["symbol"] or not d["asset"]["chain"]:
        missing.append("nombre / symbol / chain")
    if not d["method"]["scorer_version_registered"]:
        missing.append("versión del scorer")
    record = (d["sources"] or {}).get("record") or {}
    if not record.get("path") or not record.get("blob"):
        missing.append("registro de la detección con blob")
    if not d["sources"]["commands"].get("score"):
        missing.append("comando de recálculo del score")
    return missing


# ---------------------------------------------------------------------------
# Render Markdown
# ---------------------------------------------------------------------------

def _table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |" for row in rows]
    return out


def _render_acquisition(d):
    a, sym = d["acquisition"], d["asset"]["symbol"] or "el activo"
    if not a["guide_available"]:
        return [f"Sin guía de compra verificada para {a['chain_label']}: el dossier no se emite (regla núcleo, doc 24)."]
    (w1, wu1), *wrest = a["wallets"]
    (d1, du1), *dalts = a["dexes"]
    route = (f"**Ruta en {a['chain_label']}:** {w1} ({wu1})" + "".join(f" o {n} ({u})" for n, u in wrest) +
             f" → fondear con {a['fund']} → {d1} ({du1})" +
             (" · alternativas: " + ", ".join(f"{n} ({u})" for n, u in dalts) if dalts else ""))
    out = [f"Estudio de cómo se adquiere {sym}, con los datos de su par.", "", route, ""]
    if a.get("main_dex"):
        out += [f"La liquidez principal está en **{a['main_dex']}**; un agregador como {d1} enruta la orden hacia ese pool.", ""]
    out += [a["cex_route"], "", "### 1.1 Estudio de liquidez del par", ""]
    rows = []
    for r in a["liquidity_study"]:
        rows.append([r["moment"], f"{r['dex'] or 'n/d'} `{short(r['pair'])}`", fmt_usd(r["liquidity"]), r["slippage"]]
                    + [fmt_impact(r["impacts"][str(u)]) for u in IMPACT_SIZES]
                    + [fmt_usd(r["size_for"][str(t)]) for t in IMPACT_TARGETS])
    out += _table(["Momento", "Pool principal", "Liquidez (L)", "Slippage sugerido", "Impacto $100", "Impacto $1.000",
                   "Impacto $10.000", "Orden con prima 1%", "Orden con prima 3%"], rows)
    out += ["", "Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del "
            "precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un "
            "agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo "
            "muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].", "", "### 1.2 Pasos", ""]
    out += [f"{i}. {step}" for i, step in enumerate(a["steps"], 1)]
    v = a["verification"]
    out += ["", "### 1.3 Verificación previa", ""]
    if v["explorer"]:
        out.append(f"- Contrato en {v['explorer'][0]}: {v['explorer'][1]}")
    out.append(f"- Par en DexScreener: {v['dexscreener'] or 'n/d'}")
    if v["launchpad"]:
        out.append(f"- Página del lanzamiento (pump.fun): {v['launchpad']}")
    out += [f"- Datos para comparar: {v['facts']}", f"- {a['swap_links']}"]
    return out


def _render_identification(d):
    return _table(["Campo", "Valor", "Fuente / momento"], d["identification"]["rows"])


def _render_nature(d):
    n = d["nature"]
    group = f" (grupo {n['group']}: {n['group_label']}, doc 23)" if n["group"] else ""
    out = [f"- **Tipo:** {n['type']}{group}" + (f" · origen: {n['origin']}" if n["origin"] != "n/d" else ""),
           f"- **Categoría / narrativa:** {n['categories']}"]
    if n["description"]:
        text = " ".join(n["description"].split())
        text = text if len(text) <= 400 else text[:399] + "…"
        out.append(f"- **Qué promete / qué representa** (cita textual): «{text}» — fuente: {n['description_source']}")
    else:
        out.append("- **Qué promete / qué representa:** sin descripción publicada" +
                   (f" ({n['description_source']})" if n["description_source"] else " (metadata sin consultar [P])"))
    out += ["- **Historia:**"] + [f"  - {line}" for line in n["history"]]
    return out


def _fmt_ci(ci):
    return f"{fmt_pct(ci[0])}–{fmt_pct(ci[1])}" if ci else "n/d"


def _render_method(d):
    m = d["method"]
    p = m["probabilities"]
    out = [f"**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer "
           f"**{m['scorer_version_registered']}**; vigente: **{m['scorer_version_current'] or 'n/d'}**. "
           "Tabla de componentes: Anexo C del doc 24.", "",
           f"**Datos de entrada** ({m['inputs_source']}):", ""]
    out += _table(["Dato", "Valor"], m["inputs"])
    out += ["", "**Probabilidades** (definiciones del doc 19; IC90 de Wilson):", ""]
    if p["status"] == "validada":
        rows = [["Primaria: tocar +20% antes de caer −30% (≤ 48 h)", fmt_pct(p["primary"]["rate"]), _fmt_ci(p["primary"]["ci90"]), p["primary"].get("n", "n/d")],
                ["Secundaria: cierre ≥ +20% a las 48 h", fmt_pct(p["secondary"]["rate"]), _fmt_ci(p["secondary"]["ci90"]), p["secondary"].get("n", "n/d")],
                ["Después de tocar +20%, llegar a ≤ −99% (≤ 48 h)", fmt_pct(p["post_hit"]["rate"]), _fmt_ci(p["post_hit"]["ci90"]), p["post_hit"].get("n", "n/d")]]
        out += [f"Calibración validada del scorer {p['scoring_version']}, score ≥ {p['threshold']}:", ""]
        out += _table(["Métrica", "Tasa", "IC90", "n"], rows)
    else:
        sp, ss = p.get("shadow_primary") or {}, p.get("shadow_secondary") or {}
        out.append(f"- Scorer {p['scoring_version'] or 'n/d'}: **en validación** (veredicto con n ≥ {p['criteria_min_n']} "
                   f"primarias resueltas). En sombra hasta ahora: primaria {sp.get('k_hit', 'n/d')}/{sp.get('n_resolved', 'n/d')}"
                   + (f" ({fmt_pct(sp['rate'])}, IC90 {_fmt_ci(sp.get('ci90'))})" if sp.get("rate") is not None else "")
                   + f" · secundaria {ss.get('k_hit', 'n/d')}/{ss.get('n_resolved', 'n/d')} resueltas"
                   + " (shadow_monitor.json).")
        out += ["", f"Histórico ({HISTORICAL_SOURCE}):", ""]
    hist = p["historical"]
    out += _table(["Métrica (histórico)", "k/n", "Tasa", "IC90"], [
        ["Primaria: tocar +20% antes de caer −30% (≤ 48 h)", f"{hist['primary']['k']}/{hist['primary']['n']}", fmt_pct(hist["primary"]["rate"]), _fmt_ci(hist["primary"]["ci90"])],
        ["Secundaria: cierre ≥ +20% a las 48 h", f"{hist['secondary']['k']}/{hist['secondary']['n']}", fmt_pct(hist["secondary"]["rate"]), _fmt_ci(hist["secondary"]["ci90"])],
        ["Después de tocar +20%, llegar a ≤ −99% (≤ 48 h)", f"{hist['post_hit']['k']}/{hist['post_hit']['n']}", fmt_pct(hist["post_hit"]["rate"]), _fmt_ci(hist["post_hit"]["ci90"])]])
    out += ["", "**IC90 de Wilson** (z = 1,645): p̂ = k/n · centro = (p̂ + z²/2n)/(1 + z²/n) · "
            "radio = z·√(p̂(1−p̂)/n + z²/4n²)/(1 + z²/n).",
            "**Métrica dual:** velas de 15 min de GeckoTerminal del mismo pool, orden intra-vela conservador "
            "open → low → high → close; si una vela toca −30% y +20%, cuenta primero la caída.",
            "**Estudio de liquidez:** prima de ejecución = 2Δ/L (sección 1.1)."]
    return out


def _render_foundation(d):
    f = d["foundation"]
    b = f["breakdown"]
    out = []
    if b["reproducible"]:
        rows = [[r["component"], r["condition"], r["observed"], fmt_points(r["points"])] for r in b["rows"]]
        rows.append(["**Total**", "recortado a 0–100", "", f"**{b['total']}**"])
        out += [f"Desglose reconstruido desde los motivos registrados; suma {b['total']} = score registrado "
                f"{b['registered']} [V].", ""]
        out += _table(["Componente", "Condición", "Valor observado", "Puntos"], rows)
    else:
        out.append(f"Desglose no reproducible desde los motivos registrados (suma {b['total']} vs score "
                   f"{b['registered']}; motivos sin regla: {', '.join(b['unknown_reasons']) or 'ninguno'}): no se publica.")
    rc = f["recomputed"]
    if rc.get("score") is not None:
        out += ["", f"**Recalculado con el scorer vigente {rc['version']}** sobre los mismos datos (reloj fijado en "
                f"{rc['clock']}, sin estado previo): **{rc['score']}** · motivos: {', '.join(rc['reasons']) or 'n/d'}."]
    else:
        out += ["", f"Recalculado con el scorer vigente: n/d ({rc.get('error', 'sin datos')})."]
    p = f["population"]
    if p.get("n"):
        out += ["", f"**Población** (scorer {p['version']}, {p['source']}): {fmt_int(p['k_ge_threshold'])} de "
                f"{fmt_int(p['n'])} tokens analizados ({fmt_pct(p['share_ge_threshold'], 2)}) quedan ≥ {f['threshold']}."
                + (f" Con score {p['score_current_version']}, este activo queda en el percentil "
                   f"{fmt_num(p['percentile'] * 100, 1)} de esa población." if p.get("percentile") is not None else "")]
    out.append(f"**Baseline de la primaria:** {fmt_pct(f['baseline_primary'])} (tasa de la población sin filtro, doc 22 §1.1).")
    return out


def _render_validity(d):
    v = d["validity"]
    acc = v["acceleration"]
    out = [f"- **Ventana operativa:** < {WINDOW_H} h desde {when(parse_ts(v['window_from']))}, hasta "
           f"{when(parse_ts(v['expires']))} · {v['window_status']}.",
           f"- **Aceleración al detectar:** cambio m5 {fmt_pp(acc['m5'])} · h1 {fmt_pp(acc['h1'])} · h24 "
           f"{fmt_pp(acc['h24'], 0)} · volumen m5/h1 {fmt_num(acc['vol_ratio'])} · edad del par {fmt_age(acc['age_min'])}.",
           f"- **Precio de entrada** (alerta): {fmt_price(v['entry_price'])}."]
    if v["tracking"]:
        out += ["- **Seguimiento registrado** (trust loop):", ""]
        out += _table(["Momento", "Fecha", "Precio", "Cambio vs entrada", "Etiqueta del registro"],
                      [[t["stage"], when(parse_ts(t["at"])), fmt_price(t["price"]), fmt_pp(t["change_pct"]), t["label"] or ""]
                       for t in v["tracking"]])
        out.append("")
    cur = v["current"]
    if cur["price"] is not None:
        out.append(f"- **{cur['label'][:1].upper() + cur['label'][1:]}:** {fmt_price(cur['price'])} "
                   f"({fmt_pct(cur['change'], 1, signed=True)} vs la entrada).")
    dual = v["dual"]
    if dual and dual.get("status") in ("ok", "sin_velas"):
        names = {"hit": "se cumplió", "miss": "no se cumplió", "pending": "pendiente"}
        out.append(f"- **Métrica dual de este activo** (velas de {dual.get('candle_min', 15)} min, {dual.get('n_candles')} velas): "
                   f"primaria {names.get(dual['primary'], dual['primary'])} · secundaria "
                   f"{names.get(dual['secondary'], dual['secondary'])} · máximo {fmt_pct(dual.get('max_ret'), 1, True)} · "
                   f"mínimo {fmt_pct(dual.get('min_ret'), 1, True)} · último {fmt_pct(dual.get('last_ret'), 1, True)}"
                   + (f" · tocó +20% a las {fmt_num(dual['hours_to_up'], 2)} h" if dual.get("hours_to_up") is not None else "")
                   + f" · velas ambiguas: {dual.get('ambiguous_candles', 0)}.")
    else:
        out.append(f"- **Métrica dual de este activo:** n/d ({(dual or {}).get('status', 'sin consulta de velas')}).")
    hd = v["historical"]
    out.append(f"- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = {hd['n']} de "
               f"{hd['of']} con velas, medianas): máximo {fmt_pct(hd['median_max'], 0, True)} · mínimo posterior "
               f"{fmt_pct(hd['median_min_after'], 1, True)} · último precio a 48 h {fmt_pct(hd['median_last_48h'], 1, True)}.")
    return out


def _render_sources(d):
    s, meta = d["sources"], d["meta"]
    out = []
    for label, t in (("Registro de la detección", s["record"]), ("Archivo de la corrida", s["detection"])):
        if t:
            out.append(f"- **{label}:** `{t['path']}` · blob `{t['blob']}` · commit "
                       + (f"`{t['commit']}` ({t['commit_date']})" if t.get("commit") else "pendiente (archivo sin commitear)"))
    if s["alert"]:
        out.append(f"- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `{s['alert']['timestamp']}`, "
                   f"status `{s['alert']['status']}`.")
    out += ["- **Consultas:**"]
    out += [f"  - {c['source']}: {c['url']} · {('HTTP ' + str(c['status'])) if isinstance(c['status'], int) else (c['status'] or 'registro')}"
            f" · {when(parse_ts(c['at']))}" for c in s["calls"]]
    if s["consistency"]:
        out += ["- **Consistencia entre fuentes** (diferencia relativa):"]
        out += [f"  - {name}: {values} → {diff}" for name, values, diff in s["consistency"]]
    cmd = s["commands"]
    out += ["- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):", "",
            "  ```bash", f"  {cmd['score']}", "  ```", "",
            f"- **Regenerar este dossier:** `{cmd['dossier']}`",
            f"- **Métrica dual de todas las alertas en sombra:** `{cmd['dual']}`",
            f"- **Dossier:** versión {meta['dossier_version']} · armado {when(parse_ts(meta['built_at']))} · modo "
            f"{meta['mode']} · huella de los datos de entrada (SHA-256 de `inputs` del .json): `{meta['input_sha256'][:16]}…`"]
    return out


RENDERERS = {"acquisition": _render_acquisition, "identification": _render_identification,
             "nature": _render_nature, "method": _render_method, "foundation": _render_foundation,
             "validity": _render_validity, "sources": _render_sources}


def render_markdown(dossier):
    a = dossier["asset"]
    out = [f"# {a['name'] or a['symbol']} ({a['symbol']}) — dossier", ""]
    out += [line + "  " for line in dossier["presentation"]]
    for i, (key, emoji, title) in enumerate(SECTIONS, 1):
        heading = f"{title} {a['symbol']}" if key == "acquisition" else title
        out += ["", "---", "", f"## {emoji} {i}. {heading}", ""]
        out += RENDERERS[key](dossier)
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Salida
# ---------------------------------------------------------------------------

def default_path(dossier):
    return DOSSIERS_DIR / dossier["asset"]["chain"] / f"{dossier['asset']['mint']}.md"


def save_dossier(dossier, path=None):
    """Guarda <mint>.md y <mint>.json (el dict completo). Dossier incompleto -> None, no escribe nada."""
    if not dossier.get("emitible"):
        return None
    path = Path(path) if path else default_path(dossier)
    path.parent.mkdir(parents=True, exist_ok=True)
    for target, text in ((path, render_markdown(dossier)),
                         (path.with_suffix(".json"), json.dumps(dossier, ensure_ascii=False, indent=1, default=str))):
        tmp = target.with_suffix(target.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, target)
    return path


def generate_pdf(dossier, path=None):
    """[P] PDF opcional. No hay librería liviana instalada (fpdf2 / reportlab) y no se agregan dependencias sin
    verificar su supply chain: devuelve None. El .md es el formato de entrega (doc 24)."""
    if importlib.util.find_spec("fpdf") is None:
        print("[P] PDF: sin librería liviana instalada (fpdf2); se entrega el .md.")
    else:
        print("[P] PDF: fpdf2 presente pero sin verificación de supply chain; se entrega el .md.")
    return None


# ---------------------------------------------------------------------------
# Dry-run: VSOF con datos fijos (registro del repo + consulta del 01/10), sin red
# ---------------------------------------------------------------------------

VSOF_MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
# Registro, alerta y trazas tal como están en el repo [V]; población y sombra del 01/10; consulta en vivo real del
# 01/10/2026 02:46 UTC (DexScreener, RugCheck, GoPlus, GeckoTerminal), ya normalizada por los parsers de arriba.
# El score recalculado con el scorer vigente se calcula al correr (código local, sin red).
VSOF_ALERT_DATA = {'record': {'source': 'trending',
            'windows': '1h',
            'token': {'mint': '6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump',
                      'symbol': 'VSOF',
                      'name': 'VSOF',
                      'marketCapUsd': 170671390.284296,
                      'volumeUsd': 595511.3658249074,
                      'change': None,
                      'score': 100,
                      'url': 'https://pump.fun/coin/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump',
                      'window': '1h'},
            'dexscreener': {'priceUsd': 0.1721,
                            'liquidityUsd': 1195183.55,
                            'volume24hUsd': 586622.08,
                            'marketCapUsd': 172160515.0,
                            'priceChange24h': 350628.0,
                            'dexId': 'pumpswap',
                            'pairAddress': '5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx'},
            'score': 95,
            'reasons': ['WS score muy alto', 'MCap > $1M', 'Volumen alto', 'Liquidez alta', 'Pump 24h']},
 'alert': {'timestamp': '2026-09-29_171330',
           'mint': '6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump',
           'symbol': 'VSOF',
           'score': 95,
           'confidence': 64,
           'initial_price': 0.1721,
           'status': 'active_tracking',
           'trust_updates': [{'stage': 't+1h',
                              'timestamp': '2026-09-29_181639',
                              'price': 0.1819,
                              'price_change_pct': 5.69,
                              'confidence_adjustment': 0,
                              'new_confidence': 64,
                              'stage_verdict': 'NEUTRAL'},
                             {'stage': 't+6h',
                              'timestamp': '2026-09-29_233403',
                              'price': 0.2303,
                              'price_change_pct': 33.82,
                              'confidence_adjustment': 15,
                              'new_confidence': 79,
                              'stage_verdict': 'ACIERTO'},
                             {'stage': 't+24h',
                              'timestamp': '2026-09-30_171456',
                              'price': 0.4448,
                              'price_change_pct': 158.45,
                              'confidence_adjustment': 15,
                              'new_confidence': 79,
                              'stage_verdict': 'ACIERTO'}],
           'final_verdict': 'NEUTRAL'},
 'signals': None,
 'record_trace': {'path': '02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json',
                  'blob': '21b15740ba0ac8503e86df35d82c8c8e93d66cc1',
                  'commit': 'be8e7d3',
                  'commit_date': '2026-09-29T17:13:31+00:00'},
 'detection_trace': {'path': '01_Datos_Crudos/final_detection/detection_2026-09-29_170818.json',
                     'blob': '3eae871029a40334fee5b69efe8e4adeeea15068',
                     'commit': 'be8e7d3',
                     'commit_date': '2026-09-29T17:13:31+00:00'},
 'population': {'version': '7.2.1',
                'n': 2802,
                'hist': {'19': 1,
                         '59': 1,
                         '46': 1,
                         '67': 1,
                         '0': 2393,
                         '35': 42,
                         '10': 196,
                         '5': 135,
                         '25': 6,
                         '15': 4,
                         '30': 12,
                         '44': 1,
                         '20': 5,
                         '60': 1,
                         '45': 2,
                         '7': 1},
                'source': '02_Analisis/shadow_v4/_accumulated.json'},
 'calibration': None,
 'shadow': {'7.2.1': {'primary': {'n_resolved': 2, 'k_hit': 1, 'pending': 0, 'rate': 0.5, 'ci90': [0.1209, 0.8791]},
                      'secondary': {'n_resolved': 0, 'k_hit': 0, 'pending': 2, 'rate': None, 'ci90': None},
                      'criteria': {'min_n': 20,
                                   'primary_rate': 0.3,
                                   'primary_ci_lo': 0.15,
                                   'secondary_rate': 0.05,
                                   'secondary_ci_lo': 0.02,
                                   'max_young_share': 0.2,
                                   'baseline_primary': 0.105}}}}
VSOF_LIVE = {'queried_at': '2026-10-01T02:46:33+00:00',
 'calls': [{'source': 'DexScreener',
            'url': 'https://api.dexscreener.com/latest/dex/tokens/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump',
            'status': 200,
            'at': '2026-10-01T02:46:33+00:00'},
           {'source': 'RugCheck',
            'url': 'https://api.rugcheck.xyz/v1/tokens/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump/report',
            'status': 200,
            'at': '2026-10-01T02:46:35+00:00'},
           {'source': 'GoPlus',
            'url': 'https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump',
            'status': 200,
            'at': '2026-10-01T02:46:38+00:00'},
           {'source': 'GeckoTerminal (velas 1 h)',
            'url': 'https://api.geckoterminal.com/api/v2/networks/solana/pools/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx/ohlcv/hour?limit=1000',
            'status': 200,
            'at': '2026-10-01T02:46:41+00:00'},
           {'source': 'GeckoTerminal (velas 15 min, métrica dual)',
            'url': 'https://api.geckoterminal.com/api/v2/networks/solana/pools/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx/ohlcv/minute',
            'status': 'ok',
            'at': '2026-10-01T02:46:42+00:00'}],
 'rugcheck': {'creator': 'BYBkmcyrsF2ZADiTJyGYuYvXhuGFitLiBnCAoiBDAm56',
              'mint_authority': None,
              'freeze_authority': None,
              'holders': 2817.0,
              'top10': [1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896,
                        1.0024779554616896],
              'top10_pct': 10.024779554616893,
              'insiders_top10': 0,
              'lp_locked': [['pump_fun_amm', 100.0]],
              'labels': ['High market cap per holder', 'High holder correlation'],
              'description': '',
              'metadata_uri': 'https://ipfs.io/ipfs/bafkreib5iqdw5erpyxglwrbls7oikezlturc3p6yzga62tlajxnsvqxm64',
              'metadata_mutable': False,
              'total_liquidity': 2168770.385295354,
              'detected_at': '2026-09-29T17:06:54.985219044Z'},
 'goplus': {'mintable': False, 'freezable': False, 'metadata_mutable': False},
 'history': {'interval': '1 h',
             'n': 34,
             'first_ts': 1790701200,
             'first_open': 4.914972145891968e-05,
             'max': 0.5638053867006757,
             'max_ts': 1790820000,
             'min': 4.914972145891968e-05,
             'min_ts': 1790701200,
             'last_close': 0.5634088785158624,
             'last_ts': 1790820000},
 'dual': {'primary': 'hit',
          'secondary': 'pending',
          'complete': False,
          'ambiguous_candles': 0,
          'n_candles': 135,
          'max_ret': 2.276,
          'min_ret': -0.0087,
          'last_ret': 2.2737,
          'status': 'ok',
          'hours_to_up': 3.861666666666667,
          'candle_min': 15},
 'dexscreener': {'price': 0.5639,
                 'liquidity': 2166716.2,
                 'mcap': 563954155.0,
                 'fdv': 563954155.0,
                 'pair': '5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx',
                 'dex': 'pumpswap',
                 'pair_created_ms': 1790701613000.0,
                 'price_change': {'m5': 0.19, 'h1': 2.73, 'h6': 17.88, 'h24': 115},
                 'volume': {'h24': 1011395.4, 'h6': 250995.26, 'h1': 41682.37, 'm5': 2801.94},
                 'txns': {'m5': {'buys': 279, 'sells': 4},
                          'h1': {'buys': 3857, 'sells': 61},
                          'h6': {'buys': 22696, 'sells': 364},
                          'h24': {'buys': 91551, 'sells': 1485}},
                 'websites': [],
                 'socials': [],
                 'n_pairs': 1}}
# CoinGecko, Binance y Coinbase de VSOF: consulta real del 01/10/2026 04:30 UTC (Fase 4 T2) [V].
VSOF_LIVE["coingecko"] = {"listed": False}
VSOF_LIVE["cex"] = {"symbol": "VSOF", "binance": False, "coinbase": False, "at": "2026-10-01T04:30:14+00:00"}
VSOF_LIVE["calls"] = VSOF_LIVE["calls"] + [
    {"source": "CoinGecko (ficha por contrato)", "url": COINGECKO_CONTRACT.format(platform="solana", addr=VSOF_MINT),
     "status": 404, "at": "2026-10-01T04:30:00+00:00"},
    {"source": "Binance (data-api)", "url": BINANCE_EXCHANGE_INFO.format(symbol="VSOFUSDT"), "status": 400,
     "at": "2026-10-01T04:30:14+00:00"},
    {"source": "Coinbase (API pública)", "url": COINBASE_PRODUCT.format(product="VSOF-USD"), "status": 404,
     "at": "2026-10-01T04:30:15+00:00"}]
VSOF_NOW = datetime(2026, 10, 1, 2, 46, 33, tzinfo=timezone.utc)


def dry_run_dossier():
    return build_dossier(VSOF_MINT, "solana", VSOF_ALERT_DATA, live=VSOF_LIVE, now=VSOF_NOW, mode="dry-run")


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description="Dossier por activo (doc 24), con la adquisición primero.")
    target = ap.add_mutually_exclusive_group(required=True)
    target.add_argument("--dry-run", action="store_true", help="VSOF con datos fijos, sin red")
    target.add_argument("--mint", help="mint / contrato del activo alertado")
    ap.add_argument("--chain", help="chain (default: la del registro)")
    ap.add_argument("--offline", action="store_true", help="solo datos del repo, sin consultas")
    ap.add_argument("--stdout", action="store_true", help="imprime el Markdown y no guarda (salvo --out)")
    ap.add_argument("--out", help="ruta del .md")
    ap.add_argument("--pdf", action="store_true", help="[P] PDF opcional")
    args = ap.parse_args(argv)

    if args.dry_run:
        dossier = dry_run_dossier()
    else:
        alert_data = load_alert_data(args.mint, args.chain)
        if alert_data is None:
            print(f"[ERROR] {args.mint}: sin registro en alerts ni en el acumulado.", file=sys.stderr)
            return 2
        record, alert = alert_data["record"], alert_data["alert"] or {}
        chain = (args.chain or s97.detection_facts(record)["chain"]).lower()
        t0 = _detected_dt(record, alert_data["detection_trace"], alert)
        live = None if args.offline else fetch_live(
            args.mint, chain, record, t0=t0.timestamp() if t0 else None,
            p0=_num(alert.get("initial_price")) or s97.market_snapshot(record)["price"])
        dossier = build_dossier(args.mint, chain, alert_data, live=live, mode="offline" if args.offline else "live")

    if not dossier["emitible"]:
        print("[NO SE EMITE] faltan campos obligatorios: " + "; ".join(dossier["missing"]), file=sys.stderr)
        return 3
    if args.stdout or (args.dry_run and not args.out):
        print(render_markdown(dossier), end="")
    if args.out or not (args.stdout or args.dry_run):
        print(f"[OK] dossier guardado: {save_dossier(dossier, args.out)}")
    if args.pdf:
        generate_pdf(dossier)
    return 0


if __name__ == "__main__":
    sys.exit(main())
