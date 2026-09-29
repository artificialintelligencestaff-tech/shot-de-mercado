#!/usr/bin/env python3
"""
script_112_signal_aggregator.py
Agregador multimodal de señales para tokens.
Modo dry-run: solo escribe estructura vacía con placeholders.
NO modifica _all_alerts.json ni _accumulated.json.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

SIGNALS_DIR = Path("02_Analisis/signals")
SIGNALS_DIR.mkdir(parents=True, exist_ok=True)

# Estructura de señales multimodal
SIGNAL_TEMPLATE = {
    "mint": "",
    "symbol": "",
    "collected_at": "",
    "signals": {
        "onchain": {
            "holder_distribution": None,      # top holders %, concentration
            "creator_wallet": None,           # deployer address, history
            "token_program": None,            # freeze/mint authority status
            "bonding_curve": None,            # pump.fun bonding curve state
            "recent_transactions": None,      # last N txs volume/buyers
            "solscan_enrichment": None,       # holder count, tx count
            "helius_enrichment": None,        # DAS API metadata
        },
        "market": {
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
            "defillama_tvl": None,            # Solana TVL trend
            "defillama_dex_vol": None,        # Solana DEX volume
            "alt_fear_greed": None,           # Fear & Greed index
            "stablecoin_supply": None,        # Global stablecoin supply
            "sol_price_usd": None,            # SOL price reference
        }
    },
    "metadata": {
        "schema_version": "1.0",
        "collection_mode": "dry_run",
        "sources_attempted": [],
        "sources_succeeded": [],
        "sources_failed": []
    }
}

def create_empty_signal_file(mint: str, symbol: str) -> Path:
    """Crea archivo de señal vacío con template."""
    signal_data = SIGNAL_TEMPLATE.copy()
    signal_data["mint"] = mint
    signal_data["symbol"] = symbol
    signal_data["collected_at"] = datetime.now(timezone.utc).isoformat()
    
    out_file = SIGNALS_DIR / f"{mint}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(signal_data, f, indent=2, ensure_ascii=False)
    return out_file

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
        "sol_price_usd": None,
    }

def collect_signals(mint: str, symbol: str = "") -> Dict[str, Any]:
    """
    Función principal: recolecta todas las señales para un mint.
    Modo dry-run: retorna estructura con placeholders.
    """
    signals = {
        "mint": mint,
        "symbol": symbol,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "signals": {
            "onchain": collect_onchain_signals(mint),
            "market": collect_market_signals(mint),
            "social": collect_social_signals(mint),
            "news": collect_news_signals(mint),
            "kol": collect_kol_signals(mint),
            "macro": collect_macro_signals(mint),
        },
        "metadata": {
            "schema_version": "1.0",
            "collection_mode": "dry_run",
            "sources_attempted": [
                "solscan", "helius", "pumpfun", "dexscreener", "coingecko",
                "three_ws", "reddit", "stocktwits", "cryptopanic",
                "coindesk_rss", "decrypt_rss", "the_block_rss", "cointelegraph_rss",
                "pumpfun_claims", "defillama", "alternative_me"
            ],
            "sources_succeeded": [],
            "sources_failed": []
        }
    }
    return signals

def save_signals(signals: Dict[str, Any]) -> Path:
    """Guarda señales en archivo JSON."""
    mint = signals["mint"]
    out_file = SIGNALS_DIR / f"{mint}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(signals, f, indent=2, ensure_ascii=False)
    return out_file

def main():
    """Modo dry-run: crear archivos vacíos para mints de alertas activas."""
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    # Leer alertas activas para saber qué mints procesar
    alerts_file = Path("02_Analisis/alerts/_all_alerts.json")
    if not alerts_file.exists():
        print(f"[WARN] No existe {alerts_file}")
        return
    
    with open(alerts_file, encoding="utf-8") as f:
        alerts = json.load(f)
    
    active_mints = [a for a in alerts if a.get("status") == "active_tracking"]
    print(f"[INFO] {len(active_mints)} alertas activas encontradas")
    
    for alert in active_mints:
        mint = alert["mint"]
        symbol = alert.get("symbol", "")
        signals = collect_signals(mint, symbol)
        out_file = save_signals(signals)
        print(f"[OK] {symbol} ({mint[:12]}...) -> {out_file}")

if __name__ == "__main__":
    main()