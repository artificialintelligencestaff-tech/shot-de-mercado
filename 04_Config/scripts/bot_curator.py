#!/usr/bin/env python3
"""
bot_curator.py — curador de dataset curado (patrimonio).

Funciones:
- bootstrap_from_alerts(): crea dataset desde _all_alerts.json
- resolve_outcomes(): resuelve outcomes pendientes usando lib_ohlcv
- ingest_mentions_from_events(): ingiere menciones desde events/
- compute_lift_by_source(): calcula lift por fuente
"""
import hashlib
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import lib_ohlcv  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ALERTS_FILE = ROOT / "02_Analisis" / "alerts" / "_all_alerts.json"
CURATED_FILE = ROOT / "02_Analisis" / "patrimonio" / "dataset_curado.jsonl"
EVENTS_DIR = ROOT / "02_Analisis" / "events"
LIFT_FILE = ROOT / "02_Analisis" / "diagnostics" / "lift_by_source.json"

# Chain mapping para lib_ohlcv
CHAIN_MAP = {
    "solana": "solana",
    "eth": "eth",
    "ethereum": "eth",
    "base": "base",
    "arbitrum": "arbitrum",
    "optimism": "optimism",
    "blast": "blast",
    "bsc": "bsc",
    "polygon": "polygon",
    "avalanche": "avalanche",
}


def _sha16(s: str) -> str:
    return hashlib.sha1(s.encode()).hexdigest()[:16]


def _load_curated() -> list[dict]:
    if not CURATED_FILE.exists():
        return []
    rows = []
    with open(CURATED_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def _save_curated(rows: list[dict]):
    CURATED_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CURATED_FILE, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def _row_id(mint: str, ts: str) -> str:
    return _sha16(f"{mint}|{ts}")


def _get_chain_for_alert(alert: dict) -> Optional[str]:
    """Determina la chain para una alerta."""
    if alert.get("multichain"):
        coingecko_id = alert.get("coingecko_id", "")
        if coingecko_id:
            # Mapeo simple
            if "ethereum" in coingecko_id or "eth" in coingecko_id:
                return "eth"
            if "base" in coingecko_id:
                return "base"
            if "arbitrum" in coingecko_id:
                return "arbitrum"
            if "optimism" in coingecko_id:
                return "optimism"
            if "blast" in coingecko_id:
                return "blast"
            if "bsc" in coingecko_id or "binance" in coingecko_id:
                return "bsc"
            if "polygon" in coingecko_id:
                return "polygon"
            if "avalanche" in coingecko_id:
                return "avalanche"
    return "solana"  # default


def bootstrap_from_alerts():
    """
    Lee _all_alerts.json completo.
    Para cada alerta con mint conocido:
    - Crea fila en dataset_curado.jsonl si no existe (id = sha16(mint + timestamp_alert)).
    - Registra mention con source_kind = "alert".
    - Deja outcome.status = "pending".
    """
    if not ALERTS_FILE.exists():
        print("No _all_alerts.json")
        return

    with open(ALERTS_FILE, encoding="utf-8") as f:
        alerts = json.load(f)

    existing = _load_curated()
    existing_ids = {row["id"] for row in existing}

    new_rows = []
    for alert in alerts:
        mint = alert.get("mint") or alert.get("asset_key")
        if not mint:
            continue
        ts = alert.get("timestamp")
        if not ts:
            continue

        row_id = _row_id(mint, ts)
        if row_id in existing_ids:
            continue

        chain = _get_chain_for_alert(alert)
        pool = alert.get("mint")  # usar mint como pool/token address

        row = {
            "id": row_id,
            "mint": mint,
            "symbol": alert.get("symbol"),
            "chain": chain,
            "pool": pool,
            "first_mention_ts": ts,
            "first_mention_score": alert.get("score"),
            "first_mention_group": alert.get("group"),
            "sources_related": [{
                "source_kind": "alert",
                "source_id": f"alert_{ts}",
                "ts": ts,
                "score": alert.get("score"),
            }],
            "outcome": {
                "status": "pending",
                "price_1h": None,
                "price_24h": None,
                "price_48h": None,
                "max_gain_pct": None,
                "max_drawdown_pct": None,
                "touched_20pct": False,
                "primaria": False,
                "secundaria": False,
                "rug": False,
                "resolved_at": None,
            },
        }
        new_rows.append(row)
        existing_ids.add(row_id)

    if new_rows:
        all_rows = existing + new_rows
        _save_curated(all_rows)
        print(f"Bootstrap: {len(new_rows)} filas nuevas añadidas (total: {len(all_rows)})")
    else:
        print(f"Bootstrap: 0 filas nuevas (total: {len(existing)})")


def resolve_outcomes(max_age_hours: int = 72):
    """
    Lee dataset_curado.jsonl.
    Para cada fila con outcome.status == "pending" y antigüedad > 2h:
    - Llama lib_ohlcv.get_candles(chain, pool).
    - Calcula precios a 1h, 24h, 48h desde ts de mención.
    - Calcula max_gain_pct, max_drawdown_pct.
    - Actualiza touched_20pct, primaria, secundaria, rug.
    - Si todos los plazos están resueltos, status = "resolved".
    """
    rows = _load_curated()
    if not rows:
        print("No hay filas en dataset_curado")
        return

    ahora = datetime.now(timezone.utc)
    resolved_count = 0

    for row in rows:
        outcome = row.get("outcome", {})
        if outcome.get("status") != "pending":
            continue

        ts_str = row.get("first_mention_ts")
        if not ts_str:
            continue

        try:
            mention_ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        except ValueError:
            continue

        age_h = (ahora - mention_ts).total_seconds() / 3600
        if age_h < 2:
            continue  # No resolver antes de 2h

        chain = row.get("chain", "solana")
        pool = row.get("pool") or row.get("mint")
        if not pool:
            continue

        # Obtener velas de 1 minuto desde la mención
        try:
            candles = lib_ohlcv.get_candles(
                chain, pool, "minute", 1, limit=min(1000, int(age_h * 60) + 10)
            )
        except Exception as e:
            print(f"Error fetching candles for {row['id']}: {e}")
            continue

        if not candles:
            # Si no hay velas y ya pasó max_age_hours, marcar como no resuelto
            if age_h >= max_age_hours:
                outcome["status"] = "no_data"
                outcome["resolved_at"] = ahora.isoformat()
                resolved_count += 1
            continue

        # Precio de referencia (close de la vela más cercana a la mención)
        ref_price = None
        for c in candles:
            if c["ts"] >= mention_ts.timestamp():
                ref_price = c["c"]
                break
        if ref_price is None:
            ref_price = candles[-1]["c"]

        # Calcular métricas
        close_prices = [c["c"] for c in candles]
        low_prices = [c["l"] for c in candles]
        high_prices = [c["h"] for c in candles]
        max_price = max(high_prices)
        min_price = min(low_prices)

        gain_pct = ((max_price - ref_price) / ref_price) * 100
        dd_pct = ((min_price - ref_price) / ref_price) * 100

        # Precios en horizontes específicos
        price_1h = price_24h = price_48h = None
        for c in candles:
            diff_h = (c["ts"] - mention_ts.timestamp()) / 3600
            if price_1h is None and diff_h >= 1:
                price_1h = c["c"]
            if price_24h is None and diff_h >= 24:
                price_24h = c["c"]
            if price_48h is None and diff_h >= 48:
                price_48h = c["c"]
                break

        touched_20 = gain_pct >= 20
        primaria = gain_pct >= 100  # 2x
        secundaria = gain_pct >= 50  # 1.5x
        rug = dd_pct <= -50  # -50% desde la mención

        outcome["price_1h"] = price_1h
        outcome["price_24h"] = price_24h
        outcome["price_48h"] = price_48h
        outcome["max_gain_pct"] = round(gain_pct, 2)
        outcome["max_drawdown_pct"] = round(dd_pct, 2)
        outcome["touched_20pct"] = touched_20
        outcome["primaria"] = primaria
        outcome["secundaria"] = secundaria
        outcome["rug"] = rug

        # Determinar si ya está resuelto (todos los horizontes cubiertos o max_age)
        if age_h >= 48 or (price_48h is not None) or age_h >= max_age_hours:
            outcome["status"] = "resolved"
            outcome["resolved_at"] = ahora.isoformat()
            resolved_count += 1

    _save_curated(rows)
    print(f"Resolve: {resolved_count} filas resueltas")


def _iter_events():
    """Itera todos los eventos en 02_Analisis/events/."""
    if not EVENTS_DIR.exists():
        return

    for writer_dir in EVENTS_DIR.iterdir():
        if not writer_dir.is_dir():
            continue
        for event_file in writer_dir.glob("*.jsonl"):
            with open(event_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        yield writer_dir.name, json.loads(line)
                    except json.JSONDecodeError:
                        pass


def ingest_mentions_from_events():
    """
    Lee 02_Analisis/events/tweet_influencer/*.jsonl y events/mencion_token/*.jsonl.
    Para cada evento:
    - Si el asset existe en dataset_curado, agrega source_id a sources_related.
    - Si no existe, crea fila con tipo según contexto (nacido/no_nacido).
    """
    rows = _load_curated()
    # Index por (mint, ts aproximado) para búsqueda rápida
    index = {}
    for row in rows:
        key = (row["mint"], row["first_mention_ts"][:13])  # hasta hora
        index.setdefault(key, []).append(row)

    added_sources = 0
    new_rows = []

    for writer, event in _iter_events():
        # Extraer mint/token del evento
        mint = event.get("mint") or event.get("token") or event.get("asset")
        ts = event.get("ts") or event.get("timestamp") or event.get("created_at")
        if not mint or not ts:
            continue

        # Buscar fila existente (match por mint y hora aproximada)
        ts_hour = ts[:13] if len(ts) >= 13 else ts
        key = (mint, ts_hour)
        candidates = index.get(key, [])

        source_kind = "influencer" if "influencer" in writer else "token_mention"
        source_id = f"{writer}_{ts}"

        if candidates:
            # Agregar a sources_related si no existe
            for row in candidates:
                sources = row.setdefault("sources_related", [])
                if not any(s["source_id"] == source_id for s in sources):
                    sources.append({
                        "source_kind": source_kind,
                        "source_id": source_id,
                        "ts": ts,
                        "raw": event,
                    })
                    added_sources += 1
        else:
            # Crear nueva fila
            chain = "solana"  # default, podría mejorarse
            row_id = _row_id(mint, ts)
            row = {
                "id": row_id,
                "mint": mint,
                "symbol": event.get("symbol") or event.get("ticker"),
                "chain": chain,
                "pool": mint,
                "first_mention_ts": ts,
                "first_mention_score": None,
                "first_mention_group": "event",
                "sources_related": [{
                    "source_kind": source_kind,
                    "source_id": source_id,
                    "ts": ts,
                    "raw": event,
                }],
                "outcome": {
                    "status": "pending",
                    "price_1h": None,
                    "price_24h": None,
                    "price_48h": None,
                    "max_gain_pct": None,
                    "max_drawdown_pct": None,
                    "touched_20pct": False,
                    "primaria": False,
                    "secundaria": False,
                    "rug": False,
                    "resolved_at": None,
                },
            }
            new_rows.append(row)

    if new_rows or added_sources > 0:
        all_rows = rows + new_rows
        _save_curated(all_rows)
        print(f"Ingest events: {len(new_rows)} filas nuevas, {added_sources} sources añadidos (total: {len(all_rows)})")
    else:
        print(f"Ingest events: 0 cambios")


def compute_lift_by_source():
    """
    Analiza dataset_curado.
    Agrupa por (source_kind, source_id).
    Calcula:
    - n_menciones
    - n_resueltas
    - tasa_primaria = touched_20pct / n_resueltas
    - IC90 Wilson
    Salida: 02_Analisis/diagnostics/lift_by_source.json.
    """
    import math

    rows = _load_curated()
    if not rows:
        print("No hay filas en dataset_curado")
        return

    from collections import defaultdict

    # Agrupar por source
    groups = defaultdict(lambda: {"total": 0, "resolved": 0, "touched_20": 0})

    for row in rows:
        outcome = row.get("outcome", {})
        for src in row.get("sources_related", []):
            key = (src.get("source_kind", "unknown"), src.get("source_id", "unknown"))
            groups[key]["total"] += 1
            if outcome.get("status") == "resolved":
                groups[key]["resolved"] += 1
                if outcome.get("touched_20pct"):
                    groups[key]["touched_20"] += 1

    # Calcular IC90 Wilson
    def wilson_ci(successes: int, trials: int, z: float = 1.645):
        if trials == 0:
            return (0.0, 0.0)
        p = successes / trials
        denom = 1 + z * z / trials
        centre = (p + z * z / (2 * trials)) / denom
        half = z * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials)) / denom
        return (max(0.0, centre - half), min(1.0, centre + half))

    results = {}
    for (kind, src_id), stats in groups.items():
        total = stats["total"]
        resolved = stats["resolved"]
        touched = stats["touched_20"]
        tasa = touched / resolved if resolved > 0 else 0.0
        ci_low, ci_high = wilson_ci(touched, resolved)
        results[f"{kind}:{src_id}"] = {
            "source_kind": kind,
            "source_id": src_id,
            "n_menciones": total,
            "n_resueltas": resolved,
            "tasa_primaria": round(tasa, 4),
            "ic90_low": round(ci_low, 4),
            "ic90_high": round(ci_high, 4),
        }

    LIFT_FILE.parent.mkdir(parents=True, exist_ok=True)
    LIFT_FILE.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Lift by source: {len(results)} fuentes analizadas → {LIFT_FILE}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python bot_curator.py {bootstrap|resolve|ingest|lift}")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "bootstrap":
        bootstrap_from_alerts()
    elif cmd == "resolve":
        max_age = int(sys.argv[2]) if len(sys.argv) > 2 else 72
        resolve_outcomes(max_age)
    elif cmd == "ingest":
        ingest_mentions_from_events()
    elif cmd == "lift":
        compute_lift_by_source()
    else:
        print(f"Comando desconocido: {cmd}")
        sys.exit(1)