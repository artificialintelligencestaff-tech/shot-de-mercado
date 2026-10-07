#!/usr/bin/env python3
"""
lib_ohlcv.py — lib centralizada de velas OHLCV (GeckoTerminal).

Uso:
    from lib_ohlcv import get_candles
    candles = get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

Rate limit: 30 req/min (2s entre requests).
Cache local: 02_Analisis/tmp/ohlcv_cache/<sha16>.json con TTL 1h.
"""
import hashlib
import json
import os
import time
from pathlib import Path
from typing import Optional

import requests

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "02_Analisis" / "tmp" / "ohlcv_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

GECKO_BASE = "https://api.geckoterminal.com/api/v2"

# Mapeo de chain a ID de GeckoTerminal
CHAIN_MAP = {
    "solana": "solana",
    "eth": "eth",
    "ethereum": "eth",
    "base": "base",
    "arbitrum": "arbitrum",
    "optimism": "optimism",
    "blast": "blast",
    "bsc": "bsc",
    "bnb": "bsc",
    "polygon": "polygon",
    "avax": "avalanche",
    "avalanche": "avalanche",
}

# Rate limiting
_last_request_ts = 0.0
_MIN_INTERVAL = 2.0  # 30 req/min = 2s entre requests


def _rate_limit():
    global _last_request_ts
    now = time.time()
    elapsed = now - _last_request_ts
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    _last_request_ts = time.time()


def _cache_key(chain: str, pool_or_token: str, timeframe: str, aggregate: int, limit: int, before_ts: Optional[int]) -> str:
    s = f"{chain}|{pool_or_token}|{timeframe}|{aggregate}|{limit}|{before_ts or ''}"
    return hashlib.sha1(s.encode()).hexdigest()[:16]


def _load_cache(key: str) -> Optional[list]:
    cache_file = CACHE_DIR / f"{key}.json"
    if not cache_file.exists():
        return None
    try:
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        cached_ts = data.get("cached_at", 0)
        if time.time() - cached_ts > 3600:  # TTL 1h
            return None
        return data.get("candles", [])
    except Exception:
        return None


def _save_cache(key: str, candles: list):
    cache_file = CACHE_DIR / f"{key}.json"
    try:
        data = {"cached_at": time.time(), "candles": candles}
        cache_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass


def _normalize_chain(chain: str) -> str:
    return CHAIN_MAP.get(chain.lower(), chain.lower())


def _is_pool_address(s: str) -> bool:
    # Pool addresses are typically longer and have specific format
    # For GeckoTerminal, pool addresses on Solana are base58 ~44 chars
    # On EVM they're 0x... 42 chars
    return len(s) >= 40 and (s.startswith("0x") or (all(c in "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz" for c in s)))


def _fetch_pool_ohlcv(network: str, pool: str, timeframe: str, aggregate: int, limit: int, before_ts: Optional[int]) -> list:
    """Fetch OHLCV for a specific pool."""
    url = f"{GECKO_BASE}/networks/{network}/pools/{pool}/ohlcv/{timeframe}"
    params = {"aggregate": aggregate, "limit": limit}
    if before_ts:
        params["before_timestamp"] = before_ts

    _rate_limit()
    try:
        r = requests.get(url, params=params, timeout=30)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}") from e

    if r.status_code == 404:
        return []
    if r.status_code == 429:
        # Rate limited - wait and retry once
        time.sleep(5)
        _rate_limit()
        r = requests.get(url, params=params, timeout=30)
        if r.status_code == 429:
            raise RuntimeError("Rate limited (429) after retry")
    if 500 <= r.status_code < 600:
        # Server error - retry with backoff
        for attempt in range(3):
            time.sleep(2 ** attempt)
            _rate_limit()
            r = requests.get(url, params=params, timeout=30)
            if r.status_code < 500:
                break
        if 500 <= r.status_code < 600:
            raise RuntimeError(f"Server error {r.status_code} after retries")
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")

    try:
        data = r.json()
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON response: {r.text[:200]}")

    ohlcv = data.get("data", {}).get("attributes", {}).get("ohlcv_list", [])
    # GeckoTerminal returns: [timestamp, open, high, low, close, volume]
    candles = []
    for item in ohlcv:
        if len(item) >= 6:
            candles.append({
                "ts": int(item[0]),
                "o": float(item[1]),
                "h": float(item[2]),
                "l": float(item[3]),
                "c": float(item[4]),
                "v": float(item[5]),
            })
    return candles


def _fetch_token_ohlcv(network: str, token: str, timeframe: str, aggregate: int, limit: int, before_ts: Optional[int]) -> list:
    """Fetch OHLCV for a token (uses first pool found)."""
    # First, find pools for this token
    url = f"{GECKO_BASE}/networks/{network}/tokens/{token}/pools"
    params = {"page": 1}

    _rate_limit()
    try:
        r = requests.get(url, params=params, timeout=30)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}") from e

    if r.status_code != 200:
        return []

    try:
        data = r.json()
    except json.JSONDecodeError:
        return []

    pools = data.get("data", [])
    if not pools:
        return []

    # Use the pool with highest volume/reserve
    best_pool = max(pools, key=lambda p: float(p.get("attributes", {}).get("reserve_in_usd", 0) or 0))
    pool_address = best_pool.get("attributes", {}).get("address")
    if not pool_address:
        return []

    return _fetch_pool_ohlcv(network, pool_address, timeframe, aggregate, limit, before_ts)


def get_candles(
    chain: str,
    pool_or_token: str,
    timeframe: str = "minute",
    aggregate: int = 1,
    limit: int = 100,
    before_ts: Optional[int] = None,
) -> list[dict]:
    """
    Devuelve velas OHLCV de GeckoTerminal.

    Args:
        chain: "solana" | "eth" | "base" | "arbitrum" | "optimism" | "blast" | "bsc" | "polygon" | "avalanche" | ...
        pool_or_token: dirección del pool o del token.
        timeframe: "minute" | "hour" | "day"
        aggregate: agregación (1, 5, 15, etc.)
        limit: máximo de velas a devolver (máx 1000 en API)
        before_ts: timestamp epoch para paginación histórica

    Returns:
        Lista de dicts: [{"ts": epoch, "o": float, "h": float, "l": float, "c": float, "v": float}, ...]
        Orden ascendente por timestamp.
    """
    if limit > 1000:
        limit = 1000

    network = _normalize_chain(chain)
    key = _cache_key(chain, pool_or_token, timeframe, aggregate, limit, before_ts)

    # Check cache
    cached = _load_cache(key)
    if cached is not None:
        return cached

    # Determine if pool_or_token is a pool address or token address
    if _is_pool_address(pool_or_token):
        candles = _fetch_pool_ohlcv(network, pool_or_token, timeframe, aggregate, limit, before_ts)
    else:
        candles = _fetch_token_ohlcv(network, pool_or_token, timeframe, aggregate, limit, before_ts)

    # Save to cache
    _save_cache(key, candles)

    return candles


if __name__ == "__main__":
    # Test rápido
    import sys
    if len(sys.argv) >= 3:
        chain = sys.argv[1]
        addr = sys.argv[2]
        tf = sys.argv[3] if len(sys.argv) > 3 else "minute"
        print(f"Fetching {tf} candles for {chain}:{addr}...")
        c = get_candles(chain, addr, tf)
        print(f"Got {len(c)} candles")
        if c:
            print(f"First: {c[0]}")
            print(f"Last: {c[-1]}")
    else:
        print("Uso: python lib_ohlcv.py <chain> <pool_or_token> [timeframe]")