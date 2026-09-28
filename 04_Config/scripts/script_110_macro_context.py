"""
script_110_macro_context.py
Consolida señales macro de DefiLlama.
Free, sin auth, sin key.
Output: 02_Analisis/macro/_macro_signals.json
"""
import json
import requests
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path("02_Analisis/macro")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "_macro_signals.json"

def get_tvl_series(chain="Solana"):
    r = requests.get(f"https://api.llama.fi/v2/historicalChainTvl/{chain}", timeout=15)
    r.raise_for_status()
    return r.json()

def compute_tvl_metrics(series):
    if len(series) < 2:
        return {}
    curr = series[-1]["tvl"]
    metrics = {
        "current": curr,
        "days_of_history": len(series),
    }
    for n, label in [(1, "change_1d"), (7, "change_7d"), (30, "change_30d"), (90, "change_90d")]:
        if len(series) > n:
            prev = series[-1-n]["tvl"]
            metrics[label + "_pct"] = round((curr - prev) / prev * 100, 2)
    vals = sorted([x["tvl"] for x in series])
    pct_rank = sum(1 for v in vals if v <= curr) / len(vals) * 100
    metrics["percentile_historic"] = round(pct_rank, 1)
    metrics["min_historic"] = vals[0]
    metrics["max_historic"] = vals[-1]
    metrics["ratio_to_ath"] = round(curr / vals[-1] * 100, 1)
    return metrics

def get_dex_volumes(chain="solana"):
    r = requests.get(
        f"https://api.llama.fi/overview/dexs/{chain}",
        params={"excludeTotalDataChart": "true", "excludeTotalDataChartBreakdown": "true"},
        timeout=15,
    )
    r.raise_for_status()
    d = r.json()
    return {
        "total_24h": d.get("total24h"),
        "total_7d": d.get("total7d"),
        "change_1d_pct": d.get("change_1d"),
    }

def get_stablecoins_total():
    r = requests.get("https://stablecoins.llama.fi/stablecoins", params={"includePrices": "false"}, timeout=15)
    r.raise_for_status()
    d = r.json()
    total = sum(a.get("circulating", {}).get("peggedUSD", 0) for a in d.get("peggedAssets", []))
    return {"total_usd_b": round(total / 1e9, 2)}

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result = {"generated_at": now, "source": "defillama", "cost": "free", "auth": "none"}

    try:
        tvl_series = get_tvl_series("Solana")
        result["solana_tvl"] = compute_tvl_metrics(tvl_series)
    except Exception as e:
        result["solana_tvl"] = {"error": str(e)}

    try:
        result["solana_dex_volumes"] = get_dex_volumes("solana")
    except Exception as e:
        result["solana_dex_volumes"] = {"error": str(e)}

    try:
        result["stablecoins_global"] = get_stablecoins_total()
    except Exception as e:
        result["stablecoins_global"] = {"error": str(e)}

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("WROTE:", OUT_FILE)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()