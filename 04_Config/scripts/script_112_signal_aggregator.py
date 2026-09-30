#!/usr/bin/env python3
"""
script_112_signal_aggregator.py
Agregador multimodal de señales por activo, identificado por (chain, mint).

Capítulo II — Paso A: primera fuente real, Jupiter Tokens V2 (específica de Solana).
Las demás fuentes del template siguen como placeholders hasta que se integren.

Salida: 02_Analisis/signals/{chain}/{mint}.json  (schema 1.1, "chain" es campo raíz)
NO modifica _all_alerts.json ni _accumulated.json.

Uso:
    python 04_Config/scripts/script_112_signal_aggregator.py --chain <chain> --mint <MINT> [--mint ...]
    python 04_Config/scripts/script_112_signal_aggregator.py --from-alerts --legacy-chain <chain>
    agregar --dry-run para no consultar ninguna API (solo placeholders)

Los registros de _all_alerts.json anteriores al schema multi-chain no tienen campo "chain";
--legacy-chain indica a qué chain pertenecen. Sin ese flag, esos registros se ignoran.
"""
import argparse
import copy
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
SIGNALS_DIR = ROOT / "02_Analisis" / "signals"
ALERTS_FILE = ROOT / "02_Analisis" / "alerts" / "_all_alerts.json"

SCHEMA_VERSION = "1.1"
USER_AGENT = (
    "shot-de-mercado-signal-aggregator/1.1 "
    "(+https://github.com/artificialintelligencestaff-tech/shot-de-mercado)"
)
# chain: slug en minúsculas (solana, ethereum, base, ...). mint: base58 o 0x-hex.
# Ambos terminan en una ruta de archivo, por eso se validan estrictamente.
CHAIN_RE = re.compile(r"[a-z0-9][a-z0-9-]{1,31}")
MINT_RE = re.compile(r"(0x)?[A-Za-z0-9]{20,80}")

# Registro de fuentes que alimentan la fusión.
#   chains: lista de chains soportadas, o "*" si la fuente es multi-chain.
#   status: "implemented" (consulta real) | "pending" (cuenta en sources_total, sin datos todavía).
SOURCE_REGISTRY: Dict[str, Dict[str, Any]] = {
    "jupiter":       {"chains": ["solana"], "status": "implemented", "scope": "chain_specific"},
    "geckoterminal": {"chains": "*",        "status": "pending",     "scope": "multi_chain"},
    "dexpaprika":    {"chains": "*",        "status": "pending",     "scope": "multi_chain"},
    "goplus":        {"chains": "*",        "status": "pending",     "scope": "multi_chain"},
    "dexscreener":   {"chains": "*",        "status": "pending",     "scope": "multi_chain"},
}

# Estructura de señales multimodal (schema 1.1)
SIGNAL_TEMPLATE = {
    "chain": "",
    "mint": "",
    "symbol": "",
    "collected_at": "",
    "signals": {
        "onchain": {
            "holder_distribution": None,      # top holders %, concentration
            "creator_wallet": None,           # deployer address, history
            "token_program": None,            # freeze/mint authority status
            "bonding_curve": None,            # launchpad / graduation state
            "recent_transactions": None,      # last N txs volume/buyers
            "solscan_enrichment": None,       # holder count, tx count
            "helius_enrichment": None,        # DAS API metadata
        },
        "market": {
            "jupiter": None,                  # Jupiter Tokens V2 (raw + estado de la consulta)
            "dexscreener": None,              # price, liq, vol, mcap, pc24h
            "coingecko": None,                # global rank, market data
            "pumpfun": None,                  # bonding curve progress
            "three_ws_token": None,           # token details from three.ws
            "liquidity_usd": None,
            "market_cap_usd": None,
            "price_change_24h": None,
            "volume_24h_usd": None,
            "price_usd": None,
        },
        "social": {
            "reddit_mentions": None,          # subreddit, sentiment, count
            "stocktwits_sentiment": None,     # bullish/bearish ratio
            "cryptopanic_news": None,         # recent news items
            "kol_signals": None,              # KOL accumulation from three.ws
            "twitter_mentions": None,         # X mentions (si disponible)
            "lunarcrush_galaxy_score": None,  # social dominance score
        },
        "news": {
            "coindesk_rss": None,             # recent headlines
            "decrypt_rss": None,
            "the_block_rss": None,
            "cointelegraph_rss": None,
            "sentiment_score": None,          # aggregated news sentiment
        },
        "kol": {
            "three_ws_kol_accumulating": None, # KOLs accumulating this token
            "three_ws_kol_exit": None,        # KOLs exiting
            "pumpfun_claims": None,           # creator fee claims
            "deployer_reputation": None,      # deployer track record
        },
        "macro": {
            "defillama_tvl": None,            # chain TVL trend
            "defillama_dex_vol": None,        # chain DEX volume
            "alt_fear_greed": None,           # Fear & Greed index
            "stablecoin_supply": None,        # Global stablecoin supply
            "native_price_usd": None,         # precio del activo nativo de la chain (SOL, ETH, ...)
        }
    },
    "evidence": {},                           # por fuente: LLR heurístico + componentes
    "metadata": {
        "schema_version": SCHEMA_VERSION,
        "collection_mode": "dry_run",
        "sources_registry": [],               # fuentes de fusión aplicables a la chain
        "sources_attempted": [],
        "sources_succeeded": [],
        "sources_failed": [],                 # [{source, status, detail}]
        "sources_pending": [],                # aplicables pero sin integrar todavía
        "sources_skipped": [],                # [{source, reason}] no aplican a la chain
        "field_provenance": {},               # "market.price_usd" -> fuente
    }
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sources_for_chain(chain: str) -> List[str]:
    """Fuentes del registro aplicables a una chain (multi-chain + específicas de esa chain)."""
    return [name for name, meta in SOURCE_REGISTRY.items()
            if meta["chains"] == "*" or chain in meta["chains"]]


# ---------------------------------------------------------------------------
# Placeholders de fuentes todavía no integradas
# ---------------------------------------------------------------------------

def collect_onchain_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta Solscan, Helius, PumpPortal on-chain."""
    return {
        "holder_distribution": {"status": "placeholder", "source": "solscan"},
        "creator_wallet": {"status": "placeholder", "source": "helius"},
        "token_program": {"status": "placeholder", "source": "pumpfun"},
        "bonding_curve": {"status": "placeholder", "source": "pumpfun"},
        "recent_transactions": {"status": "placeholder", "source": "helius"},
        "solscan_enrichment": {"status": "placeholder", "source": "solscan"},
        "helius_enrichment": {"status": "placeholder", "source": "helius"},
    }

def collect_market_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta DexScreener, CoinGecko, Pump.fun, three.ws."""
    return {
        "jupiter": {"status": "placeholder", "source": "jupiter"},
        "dexscreener": {"status": "placeholder", "source": "dexscreener"},
        "coingecko": {"status": "placeholder", "source": "coingecko"},
        "pumpfun": {"status": "placeholder", "source": "pumpfun"},
        "three_ws_token": {"status": "placeholder", "source": "three_ws"},
        "liquidity_usd": None,
        "market_cap_usd": None,
        "price_change_24h": None,
        "volume_24h_usd": None,
        "price_usd": None,
    }

def collect_social_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta Reddit, StockTwits, CryptoPanic, KOL signals."""
    return {
        "reddit_mentions": {"status": "placeholder", "source": "reddit"},
        "stocktwits_sentiment": {"status": "placeholder", "source": "stocktwits"},
        "cryptopanic_news": {"status": "placeholder", "source": "cryptopanic"},
        "kol_signals": {"status": "placeholder", "source": "three_ws"},
        "twitter_mentions": {"status": "placeholder", "source": "twitter"},
        "lunarcrush_galaxy_score": {"status": "placeholder", "source": "lunarcrush"},
    }

def collect_news_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta RSS feeds."""
    return {
        "coindesk_rss": {"status": "placeholder", "source": "coindesk_rss"},
        "decrypt_rss": {"status": "placeholder", "source": "decrypt_rss"},
        "the_block_rss": {"status": "placeholder", "source": "the_block_rss"},
        "cointelegraph_rss": {"status": "placeholder", "source": "cointelegraph_rss"},
        "sentiment_score": None,
    }

def collect_kol_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta three.ws KOL signals, pumpfun-claims."""
    return {
        "three_ws_kol_accumulating": {"status": "placeholder", "source": "three_ws"},
        "three_ws_kol_exit": {"status": "placeholder", "source": "three_ws"},
        "pumpfun_claims": {"status": "placeholder", "source": "pumpfun_claims"},
        "deployer_reputation": {"status": "placeholder", "source": "helius"},
    }

def collect_macro_signals(mint: str) -> Dict[str, Any]:
    """Placeholder: consulta DefiLlama, Alternative.me, CoinGecko global."""
    return {
        "defillama_tvl": {"status": "placeholder", "source": "defillama"},
        "defillama_dex_vol": {"status": "placeholder", "source": "defillama"},
        "alt_fear_greed": {"status": "placeholder", "source": "alternative_me"},
        "stablecoin_supply": {"status": "placeholder", "source": "defillama"},
        "native_price_usd": None,
    }


# ---------------------------------------------------------------------------
# Fuente 1: Jupiter Tokens V2 (específica de Solana, sin API key)
# Campos verificados contra la API real el 2026-09-29/30:
#   dev, holderCount, organicScore, organicScoreLabel, isVerified, tokenProgram,
#   launchpad, graduatedPool, graduatedAt, usdPrice, mcap, liquidity,
#   audit.{mintAuthorityDisabled, freezeAuthorityDisabled, topHoldersPercentage,
#          devBalancePercentage, devMints, devMigrations}, stats5m/1h/6h/24h
# ---------------------------------------------------------------------------

JUPITER_SEARCH_URL = "https://api.jup.ag/tokens/v2/search"
JUPITER_MIN_INTERVAL_S = 2.0   # 0.5 RPS sin API key
JUPITER_MAX_RETRIES = 2
_last_jupiter_call = 0.0


def _jupiter_throttle() -> None:
    global _last_jupiter_call
    wait = JUPITER_MIN_INTERVAL_S - (time.monotonic() - _last_jupiter_call)
    if wait > 0:
        time.sleep(wait)
    _last_jupiter_call = time.monotonic()


def fetch_jupiter(mint: str) -> Dict[str, Any]:
    """Consulta /tokens/v2/search. Nunca lanza: devuelve status ok | not_found | error."""
    result = {"source": "jupiter", "endpoint": JUPITER_SEARCH_URL, "fetched_at": None,
              "http_status": None, "status": "error", "detail": "", "raw": None}
    for attempt in range(JUPITER_MAX_RETRIES + 1):
        _jupiter_throttle()
        result["fetched_at"] = now_iso()
        try:
            r = requests.get(JUPITER_SEARCH_URL, params={"query": mint}, timeout=20,
                             headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        except requests.RequestException as e:
            result["detail"] = f"error de red: {e}"
            continue
        result["http_status"] = r.status_code
        if r.status_code == 429 and attempt < JUPITER_MAX_RETRIES:
            retry_after = r.headers.get("Retry-After", "")
            time.sleep(min(float(retry_after) if retry_after.isdigit() else 5.0 * (attempt + 1), 30.0))
            continue
        if r.status_code != 200:
            result["detail"] = f"HTTP {r.status_code}: {r.text[:160]}"
            return result
        try:
            items = r.json()
        except ValueError:
            result["detail"] = "respuesta no es JSON"
            return result
        if not isinstance(items, list):
            result["detail"] = f"se esperaba una lista, llegó {type(items).__name__}"
            return result
        # /search es difuso: solo se acepta el resultado cuyo id coincide exactamente con el mint
        match = next((it for it in items if isinstance(it, dict) and it.get("id") == mint), None)
        if match is None:
            result["status"] = "not_found"
            result["detail"] = f"/search devolvió {len(items)} resultados, ninguno con id == mint"
            return result
        result.update(status="ok", detail="match exacto por id", raw=match)
        return result
    return result


def _num(x: Any) -> Optional[float]:
    return float(x) if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def map_jupiter(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Traduce el item de Jupiter a los campos del template. Devuelve (onchain, market)."""
    audit = raw.get("audit") or {}
    stats24 = raw.get("stats24h") or {}
    buy24, sell24 = _num(stats24.get("buyVolume")), _num(stats24.get("sellVolume"))
    vol24 = None if buy24 is None and sell24 is None else (buy24 or 0.0) + (sell24 or 0.0)
    onchain = {
        "holder_distribution": {
            "source": "jupiter",
            "holder_count": raw.get("holderCount"),
            "top_holders_pct": audit.get("topHoldersPercentage"),
            "holder_change_24h_pct": stats24.get("holderChange"),
        },
        "creator_wallet": {
            "source": "jupiter",
            "address": raw.get("dev"),
            "dev_mints": audit.get("devMints"),
            "dev_migrations": audit.get("devMigrations"),
            "dev_balance_pct": audit.get("devBalancePercentage"),
        },
        "token_program": {
            "source": "jupiter",
            "program": raw.get("tokenProgram"),
            "mint_authority_disabled": audit.get("mintAuthorityDisabled"),
            "freeze_authority_disabled": audit.get("freezeAuthorityDisabled"),
        },
        "bonding_curve": {
            "source": "jupiter",
            "launchpad": raw.get("launchpad"),
            "graduated_pool": raw.get("graduatedPool"),
            "graduated_at": raw.get("graduatedAt"),
        },
    }
    market = {
        "price_usd": raw.get("usdPrice"),
        "market_cap_usd": raw.get("mcap"),
        "liquidity_usd": raw.get("liquidity"),
        "price_change_24h": stats24.get("priceChange"),
        "volume_24h_usd": vol24,
    }
    return onchain, market


def jupiter_evidence(raw: Dict[str, Any]) -> Dict[str, Any]:
    """LLR (log-odds, nats) a favor de 'aceleración vertical sin rug'.

    Reglas HEURÍSTICAS NO CALIBRADAS: con n<20 alertas cerradas no hay datos para estimar
    razones de verosimilitud. Cada componente declara su regla para que YANG la audite.
    El recorte ±c se aplica en lib_fusion, no acá.
    """
    audit = raw.get("audit") or {}
    comps: List[Dict[str, Any]] = []

    def add(feature: str, value: Any, llr: float, rule: str) -> None:
        comps.append({"feature": feature, "value": value, "llr": round(llr, 4), "rule": rule})

    for key, what in (("mintAuthorityDisabled", "mint"), ("freezeAuthorityDisabled", "freeze")):
        v = audit.get(key)
        if v is False:
            add(f"audit.{key}", v, -1.0, f"{what} authority activa: riesgo de emisión/congelamiento")
        else:
            add(f"audit.{key}", v, 0.0, "revocada (esperado)" if v is True else "sin dato")

    organic = _num(raw.get("organicScore"))
    if organic is None:
        add("organicScore", None, 0.0, "sin dato")
    else:
        add("organicScore", organic, (organic - 50.0) / 50.0 * 0.75,
            "lineal: (score-50)/50 * 0.75 -> [-0.75, +0.75]")

    holders = _num(raw.get("holderCount"))
    if holders is None:
        add("holderCount", None, 0.0, "sin dato")
    elif holders < 100:
        add("holderCount", holders, -0.5, "<100 holders: base demasiado fina")
    elif holders >= 1000:
        add("holderCount", holders, 0.25, ">=1000 holders")
    else:
        add("holderCount", holders, 0.0, "100-999 holders: neutro")

    top = _num(audit.get("topHoldersPercentage"))
    if top is None:
        add("audit.topHoldersPercentage", None, 0.0, "sin dato")
    elif top > 50:
        add("audit.topHoldersPercentage", top, -0.75, ">50% en top holders")
    elif top > 30:
        add("audit.topHoldersPercentage", top, -0.25, ">30% en top holders")
    else:
        add("audit.topHoldersPercentage", top, 0.0, "<=30%: neutro")

    dev_bal = _num(audit.get("devBalancePercentage"))
    if dev_bal is None:
        add("audit.devBalancePercentage", None, 0.0, "sin dato")
    elif dev_bal > 10:
        add("audit.devBalancePercentage", dev_bal, -0.5, "dev retiene >10%")
    elif dev_bal > 5:
        add("audit.devBalancePercentage", dev_bal, -0.25, "dev retiene >5%")
    else:
        add("audit.devBalancePercentage", dev_bal, 0.0, "<=5%: neutro")

    liq_chg = _num((raw.get("stats24h") or {}).get("liquidityChange"))
    if liq_chg is not None and liq_chg <= -90:
        add("stats24h.liquidityChange", liq_chg, -1.5, "liquidez drenada >=90% en 24h: patrón de rug")
    else:
        add("stats24h.liquidityChange", liq_chg, 0.0, "sin drenaje de liquidez" if liq_chg is not None else "sin dato")

    s1h = raw.get("stats1h") or {}
    buy1h, sell1h = _num(s1h.get("buyVolume")) or 0.0, _num(s1h.get("sellVolume")) or 0.0
    if buy1h + sell1h > 0:
        share = buy1h / (buy1h + sell1h)
        if share > 0.6:
            add("stats1h.buyShare", round(share, 4), 0.25, "compras >60% del volumen 1h")
        elif share < 0.4:
            add("stats1h.buyShare", round(share, 4), -0.25, "compras <40% del volumen 1h")
        else:
            add("stats1h.buyShare", round(share, 4), 0.0, "40-60%: neutro")
    else:
        add("stats1h.buyShare", None, 0.0, "sin volumen 1h")

    add("isVerified", raw.get("isVerified"), 0.25 if raw.get("isVerified") is True else 0.0,
        "verificado por Jupiter" if raw.get("isVerified") is True else "no verificado: no se penaliza")

    # Informativos: dirección ambigua (Fartcoin, token maduro, tiene dev con 495 mints)
    add("audit.devMints", audit.get("devMints"), 0.0, "informativo, sin dirección clara")
    add("audit.devMigrations", audit.get("devMigrations"), 0.0, "informativo, sin dirección clara")

    return {
        "source": "jupiter",
        "label": "HEURISTICA_NO_CALIBRADA",
        "llr_raw": round(sum(c["llr"] for c in comps), 4),
        "components": comps,
    }


# ---------------------------------------------------------------------------
# Ensamblado
# ---------------------------------------------------------------------------

def new_signal(chain: str, mint: str, symbol: str) -> Dict[str, Any]:
    """Estructura vacía (template + placeholders) para un activo."""
    signal = copy.deepcopy(SIGNAL_TEMPLATE)
    signal.update(chain=chain, mint=mint, symbol=symbol.strip(), collected_at=now_iso())
    signal["signals"] = {
        "onchain": collect_onchain_signals(mint),
        "market": collect_market_signals(mint),
        "social": collect_social_signals(mint),
        "news": collect_news_signals(mint),
        "kol": collect_kol_signals(mint),
        "macro": collect_macro_signals(mint),
    }
    return signal


def collect_signals(chain: str, mint: str, symbol: str = "", dry_run: bool = False) -> Dict[str, Any]:
    """Función principal: recolecta las señales disponibles para (chain, mint)."""
    signal = new_signal(chain, mint, symbol)
    meta = signal["metadata"]
    applicable = sources_for_chain(chain)
    meta["sources_registry"] = applicable
    for name, info in SOURCE_REGISTRY.items():
        if name not in applicable:
            meta["sources_skipped"].append({"source": name, "reason": f"no aplica a chain '{chain}'"})
        elif info["status"] != "implemented":
            meta["sources_pending"].append(name)

    if dry_run or "jupiter" not in applicable:
        return signal

    meta["collection_mode"] = "live"
    meta["sources_attempted"].append("jupiter")
    jup = fetch_jupiter(mint)
    signal["signals"]["market"]["jupiter"] = jup
    if jup["status"] != "ok":
        meta["sources_failed"].append({"source": "jupiter", "status": jup["status"], "detail": jup["detail"]})
        return signal

    meta["sources_succeeded"].append("jupiter")
    raw = jup["raw"]
    onchain, market = map_jupiter(raw)
    signal["signals"]["onchain"].update(onchain)
    signal["signals"]["market"].update(market)
    for field in onchain:
        meta["field_provenance"][f"onchain.{field}"] = "jupiter"
    for field in market:
        meta["field_provenance"][f"market.{field}"] = "jupiter"
    signal["evidence"]["jupiter"] = jupiter_evidence(raw)
    if not signal["symbol"]:
        signal["symbol"] = (raw.get("symbol") or "").strip()
    return signal


def save_signals(signals: Dict[str, Any]) -> Path:
    """Guarda señales en 02_Analisis/signals/{chain}/{mint}.json."""
    out_dir = SIGNALS_DIR / signals["chain"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{signals['mint']}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(signals, f, indent=2, ensure_ascii=False)
    return out_file


def load_alerts() -> List[Dict[str, Any]]:
    if not ALERTS_FILE.exists():
        print(f"[WARN] No existe {ALERTS_FILE}")
        return []
    with open(ALERTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def alert_targets(alerts: List[Dict[str, Any]], legacy_chain: Optional[str]) -> List[Tuple[str, str, str]]:
    """(chain, mint, symbol) de las alertas en seguimiento activo."""
    targets, skipped = [], 0
    for alert in alerts:
        if alert.get("status") != "active_tracking":
            continue
        chain = alert.get("chain") or legacy_chain
        if not chain:
            skipped += 1
            continue
        targets.append((chain, alert["mint"], alert.get("symbol", "")))
    if skipped:
        print(f"[WARN] {skipped} alertas activas sin campo 'chain' ignoradas (usar --legacy-chain)")
    return targets


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Agregador multimodal de señales por (chain, mint).")
    p.add_argument("--chain", help="chain de los --mint (slug: solana, ethereum, base, ...)")
    p.add_argument("--mint", action="append", default=[], help="dirección del token (repetible)")
    p.add_argument("--from-alerts", action="store_true",
                   help="procesar las alertas en active_tracking de _all_alerts.json")
    p.add_argument("--legacy-chain",
                   help="chain asumida para registros de _all_alerts.json sin campo 'chain'")
    p.add_argument("--dry-run", action="store_true", help="no consultar APIs; solo placeholders")
    args = p.parse_args(argv)
    if args.mint and not args.chain:
        p.error("--mint requiere --chain")
    if not args.mint and not args.from_alerts:
        p.error("indicar --chain y --mint, o --from-alerts")
    for chain in filter(None, (args.chain, args.legacy_chain)):
        if not CHAIN_RE.fullmatch(chain):
            p.error(f"chain inválida: {chain!r} (slug en minúsculas)")
    for mint in args.mint:
        if not MINT_RE.fullmatch(mint):
            p.error(f"mint inválido: {mint!r}")
    return args


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    targets = [(args.chain, mint, "") for mint in args.mint]
    if args.from_alerts:
        targets += alert_targets(load_alerts(), args.legacy_chain)
    print(f"[INFO] {len(targets)} activos a procesar")

    for chain, mint, symbol in targets:
        if not (CHAIN_RE.fullmatch(chain) and MINT_RE.fullmatch(mint)):
            print(f"[WARN] par inválido ignorado: {chain!r} / {mint!r}")
            continue
        signals = collect_signals(chain, mint, symbol, dry_run=args.dry_run)
        out_file = save_signals(signals)
        meta = signals["metadata"]
        status = "ok: " + ",".join(meta["sources_succeeded"]) if meta["sources_succeeded"] else "sin fuentes"
        print(f"[OK] {chain}/{signals['symbol'] or '?'} ({mint[:12]}...) -> {out_file} [{status}]")
        for fail in meta["sources_failed"]:
            print(f"     [FALLA] {fail['source']}: {fail['status']} — {fail['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
