#!/usr/bin/env python3
"""
pilot_event_study_gaming.py — Piloto de la hipótesis H1 del Capítulo VII (datos reales, solo lectura).

H1 [H]: "En los días con pico de atención (Wikipedia) sobre videojuegos masivos, la canasta de
tokens gaming supera a BTC en las 48 h siguientes a la detección."

Datos:
  - Atención: Wikipedia Pageviews diarios (sin key) de ARTICLES, 2022-01-01 -> ayer.
  - Precios:  Binance data-api (sin key), velas 1d de BASKET y del benchmark BTCUSDT.
Método:
  - Picos: lib_narrative.detect_narrative_emerging con los parámetros por defecto (fijados ANTES
    de mirar resultados: no hay ajuste, así que el test es fuera de muestra por construcción).
  - Eventos a <= 7 días entre sí se fusionan (comparten ventana de retorno).
  - Ventanas: concurrente [-1,+1] (asociación) · operable [+1,+3] (el dato de pageviews del día t
    se publica ~t+1: entrada al cierre de t+1, 48 h) · anticipación [-8,-1].
  - Placebo: todos los días a más de 7 días de cualquier evento.
  - Aceptación (Dirección): n >= 20, P(retorno anormal > 0) > 55% y cota inferior del IC 90%
    del hit rate por encima del placebo.
  - Tasa base sectorial: frecuencia de +20% en 48 h por token en todos los días (prior de la fusión).
Salida: 02_Analisis/narrative/pilot_event_study_gaming.json

Uso: python 04_Config/scripts/pilot_event_study_gaming.py [--start 2022-01-01]
"""
import argparse
import json
import os
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_narrative as ln  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
OUT_FILE = ROOT / "02_Analisis" / "narrative" / "pilot_event_study_gaming.json"

# Selección a priori: juegos/anuncios masivos 2022-2026 (títulos exactos de en.wikipedia).
ARTICLES = [
    "Grand_Theft_Auto_VI", "Elden_Ring", "Hogwarts_Legacy", "The_Legend_of_Zelda:_Tears_of_the_Kingdom",
    "Baldur's_Gate_3", "Starfield_(video_game)", "Black_Myth:_Wukong", "Call_of_Duty:_Black_Ops_6",
    "Monster_Hunter_Wilds", "Nintendo_Switch_2", "Palworld", "Helldivers_2", "Marvel's_Spider-Man_2",
    "Final_Fantasy_VII_Rebirth", "Diablo_IV", "Hollow_Knight:_Silksong", "Ghost_of_Yōtei",
    "Death_Stranding_2:_On_the_Beach", "Battlefield_6", "Borderlands_4",
]
BASKET = ["IMXUSDT", "AXSUSDT", "SANDUSDT", "MANAUSDT", "GALAUSDT"]
BENCHMARK = "BTCUSDT"
BINANCE_KLINES = "https://data-api.binance.vision/api/v3/klines"
MERGE_GAP_DAYS = 7
WINDOWS = {"concurrente": (-1, 1), "operable_48h": (1, 3), "anticipacion": (-8, -1)}


def fetch_daily_closes(symbol, start, end, fetcher):
    closes, cursor = {}, int(datetime(start.year, start.month, start.day, tzinfo=timezone.utc).timestamp() * 1000)
    end_ms = int(datetime(end.year, end.month, end.day, tzinfo=timezone.utc).timestamp() * 1000)
    status = "ok"
    while cursor <= end_ms:
        res = fetcher(BINANCE_KLINES, {"symbol": symbol, "interval": "1d", "startTime": cursor, "limit": 1000})
        if res["status"] != "ok" or not res["data"]:
            status = res["status"] if res["status"] != "ok" else status
            break
        for k in res["data"]:
            closes[datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc).date().isoformat()] = float(k[4])
        cursor = res["data"][-1][0] + 86_400_000
        if len(res["data"]) < 1000:
            break
    return closes, status


def vertical_base_rate(prices, horizon=2):
    """Por token: fracción de días con retorno >= +20% en `horizon` días (todos los días)."""
    out = {}
    for sym, p in prices.items():
        days = sorted(p)
        hits = n = 0
        for d in days:
            r = ln.forward_return(p, date.fromisoformat(d), 0, horizon)
            if r is not None:
                n += 1
                hits += r >= ln.VERTICAL_MOVE
        out[sym] = {"hits": hits, "n": n, "rate": round(hits / n, 5) if n else None}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--start", default="2022-01-01")
    args = ap.parse_args(argv)
    start = date.fromisoformat(args.start)
    end = datetime.now(timezone.utc).date() - timedelta(days=1)
    fetcher = ln.HttpFetcher()

    # 1) Atención y picos
    detections, all_spikes, sources = [], [], []
    for art in ARTICLES:
        series = ln.fetch_attention_series(art, "wikipedia_pageviews", start, end, fetcher, article=art)
        det = ln.detect_narrative_emerging(series)
        sources.append({"article": art, "status": series["status"], "n_points": det["n_points"],
                        "n_spikes": len(det["spikes"])})
        for s in det["spikes"]:
            all_spikes.append({"date": s["date"], "article": art, "ratio": s["ratio"], "value": s["value"]})
        print(f"[{series['status']:<5}] {art}: {det['n_points']} días, {len(det['spikes'])} picos", flush=True)
    event_days = ln.merge_close_events((date.fromisoformat(s["date"]) for s in all_spikes), MERGE_GAP_DAYS)

    # 2) Precios
    prices, price_status = {}, {}
    for sym in BASKET + [BENCHMARK]:
        closes, st = fetch_daily_closes(sym, start - timedelta(days=10), end, fetcher)
        prices[sym], price_status[sym] = closes, {"status": st, "n_days": len(closes)}
        print(f"[{st:<5}] {sym}: {len(closes)} velas diarias", flush=True)
    bench = prices.pop(BENCHMARK)
    basket = {k: v for k, v in prices.items() if v}

    # 3) Estudio de eventos vs placebo
    all_days = [date.fromisoformat(d) for d in sorted(bench) if date.fromisoformat(d) >= start]
    placebo = ln.placebo_days(all_days, event_days, MERGE_GAP_DAYS)
    results = {}
    for name, (a, b) in WINDOWS.items():
        ev_rows = ln.event_study(event_days, basket, bench, a, b)
        pl_rows = ln.event_study(placebo, basket, bench, a, b)
        results[name] = {"window": [a, b], **ln.evaluate_hypothesis(ev_rows, pl_rows)}
        if name == "operable_48h":
            results[name]["events"] = ev_rows
    # Estabilidad temporal (no hay parámetros ajustados: se reporta el hit rate por bloque anual con purga 2d)
    op = {r["date"]: r for r in results["operable_48h"]["events"]}
    stability = []
    for _, test in ln.walk_forward_splits(event_days, train_days=365, test_days=365, purge_days=2):
        rows = [op[d.isoformat()] for d in test if d.isoformat() in op]
        if rows:
            stability.append({"from": test[0].isoformat(), "to": test[-1].isoformat(), "n": len(rows),
                              "hit_rate": round(statistics.fmean(1.0 if r["abnormal_return"] > 0 else 0.0 for r in rows), 4)})

    base = vertical_base_rate(basket)
    k = sum(v["hits"] for v in base.values())
    n = sum(v["n"] for v in base.values())
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hypothesis": "H1: pico de atención (Wikipedia) sobre videojuegos masivos -> canasta gaming supera a BTC en 48 h",
        "period": [start.isoformat(), end.isoformat()],
        "params": {"spike_ratio": ln.SPIKE_RATIO, "spike_robust_z": ln.SPIKE_ROBUST_Z,
                   "baseline_days": ln.SPIKE_BASELINE_DAYS, "merge_gap_days": MERGE_GAP_DAYS,
                   "vertical_move": ln.VERTICAL_MOVE, "label": ln.LABEL},
        "basket": BASKET, "benchmark": BENCHMARK,
        "attention_sources": sources, "price_sources": price_status,
        "spikes_raw": sorted(all_spikes, key=lambda s: s["date"]),
        "event_days": [d.isoformat() for d in event_days],
        "results": results, "stability_by_year": stability,
        "sector_base_rate_vertical_48h": {"per_token": base, "hits": k, "n": n,
                                          "beta_prior": [1 + k, 1 + n - k],
                                          "note": "[V] frecuencia histórica de +20% en 48h por token-día; prior sectorial [I] para tokens sin historia propia"},
    }
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] {OUT_FILE}")
    for name, r in results.items():
        print(f"  {name:<13} n={r['n_events']:<3} hit={r['hit_rate']} IC90={r['hit_rate_ci90']} "
              f"placebo={r['placebo_hit_rate']} AR={r['mean_abnormal']} IC90={r['mean_abnormal_ci90']} "
              f"vertical={r['vertical_rate']} (placebo {r['placebo_vertical_rate']}) aceptada={r['accepted']}")
    print(f"  tasa base +20%/48h (sector): {k}/{n} = {k / n:.4f}" if n else "  sin tasa base")
    return 0


if __name__ == "__main__":
    sys.exit(main())
