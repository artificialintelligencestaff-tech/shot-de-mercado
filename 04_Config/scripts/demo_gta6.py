#!/usr/bin/env python3
"""
demo_gta6.py — Flujo completo de la Capa Narrativa (Capítulo VII) sobre el lanzamiento de GTA VI.

Modos:
  (por defecto)        dry-run: respuestas REALES capturadas el 2026-09-30 (fixtures), sin red.
  --live               consulta las APIs reales (Wikidata, Wikipedia, GDELT, DexScreener).
  --capture-fixtures   --live + guarda las respuestas como fixtures (mantenimiento).

Escenarios:
  real_hoy                 todo con datos reales a la fecha de captura.
  simulado_anticipacion    fecha de análisis = lanzamiento − 7 días; la serie de atención se completa
                           con una rampa SIMULADA (rotulada) hasta 8x la mediana; lupa con métricas reales
                           del día de captura. Muestra el pipeline completo con un pico.

Flujo: A calendario -> B atención -> C mapeo -> D lupa (3 tokens, 3 chains) -> E fusión (lib_fusion)
Salida: consola + 02_Analisis/narrative/demo_gta6.json
"""
import argparse
import json
import os
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_fusion  # noqa: E402
import lib_narrative as ln  # noqa: E402
from script_112_signal_aggregator import sources_for_chain  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
REGISTRY_FILE = ROOT / "04_Config" / "narrative_registry.json"
FIXTURES_FILE = Path(__file__).resolve().parent / "fixtures" / "narrative_gta6.json"
PILOT_FILE = ROOT / "02_Analisis" / "narrative" / "pilot_event_study_gaming.json"
OUT_FILE = ROOT / "02_Analisis" / "narrative" / "demo_gta6.json"
NARRATIVE = "gta6"
LUPA_TOKENS = [("ethereum", "IMX"), ("base", "PRIME"), ("solana", "ATLAS")]   # 3 chains
ATTENTION_DAYS = 120
SIM_DAYS_BEFORE_EVENT = 7
SIM_PEAK_MULTIPLE = 8.0


class RecordingFetcher:
    def __init__(self, inner):
        self.inner, self.recorded = inner, {}

    def __call__(self, url, params=None):
        res = self.inner(url, params)
        if res["status"] == "ok":
            self.recorded[ln.request_key(url, params)] = res["data"]
        return res


def load_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def sector_prior():
    pilot = load_json(PILOT_FILE, {})
    prior = (pilot.get("sector_base_rate_vertical_48h") or {}).get("beta_prior")
    if prior:
        return tuple(prior), "[V] piloto: frecuencia histórica de +20%/48h en tokens gaming (Binance 2022-2026)"
    return (1.0, 1.0), "[P] sin piloto: prior Beta(1,1)"


def simulated_series(real, as_of):
    """Serie real + tramo SIMULADO hasta as_of − 1: nivel base y un shock en los últimos 3 días
    (3x, 5x, 8x), el patrón observado en el Trailer 1 de GTA VI (100 -> 341.519 vistas en 1 día)."""
    pts = [dict(p, simulated=False) for p in real["points"]]
    if not pts:
        return dict(real, points=pts)
    base = statistics.median(p["value"] for p in pts[-28:])
    last = date.fromisoformat(pts[-1]["date"])
    days = (as_of - last).days - 1
    shock = [3.0, 5.0, SIM_PEAK_MULTIPLE]
    for i in range(days):
        mult = shock[i - (days - len(shock))] if i >= days - len(shock) else 1.0
        pts.append({"date": (last + timedelta(days=i + 1)).isoformat(), "value": round(base * mult),
                    "simulated": True})
    return dict(real, points=pts, simulated_from=(last + timedelta(days=1)).isoformat())


def run_scenario(name, as_of, fetcher, registry, capture_day, prior, prior_note, simulate):
    spec = registry["narratives"][NARRATIVE]
    out = {"scenario": name, "as_of": as_of.isoformat(), "simulated": simulate}

    # A — calendario
    cal = ln.fetch_eventos_calendario(capture_day, 120, fetcher)
    ev = next((e for e in cal["events"] if e.get("wikidata_item") in spec["wikidata_items"]), None)
    if ev:
        ev = dict(ev)
        ev["phase"], ev["days_to_event"] = ln.event_phase(date.fromisoformat(ev["date"]), as_of)
    out["calendar"] = {"event": ev, "sources": cal["sources"], "n_events_in_horizon": len(cal["events"])}

    # B — atención (la serie real siempre termina el día anterior a la captura)
    real = ln.fetch_attention_series(NARRATIVE, "wikipedia_pageviews", capture_day - timedelta(days=ATTENTION_DAYS),
                                     capture_day - timedelta(days=1), fetcher, article=spec["wikipedia_articles"][0])
    series = simulated_series(real, as_of) if simulate else real
    emergence = ln.detect_narrative_emerging(series)
    gdelt = ln.fetch_attention_series(NARRATIVE, "gdelt_timelinevol", capture_day - timedelta(days=30),
                                      capture_day - timedelta(days=1), fetcher, query=spec["gdelt_query"])
    out["attention"] = {"wikipedia": {"status": real["status"], "latest": emergence["latest"],
                                      "n_spikes": len(emergence["spikes"]), "emerging_now": emergence["emerging_now"],
                                      "simulated_from": series.get("simulated_from")},
                        "gdelt": {"status": gdelt["status"], "detail": gdelt["detail"][:120], "n_points": len(gdelt["points"])}}

    # C — mapeo
    search = fetcher(ln.DEXSCREENER_SEARCH, {"q": "GTA6"})
    pairs = (search["data"] or {}).get("pairs", []) if search["status"] == "ok" else []
    links = ln.map_narrative_to_tokens(NARRATIVE, registry, pairs, now_ms=_ms(capture_day))
    name_matches = [l for l in links if l["link_type"] == "name_match"]
    out["mapping"] = {"thematic": [l for l in links if l["link_type"] != "name_match"],
                      "name_match_count": len(name_matches),
                      "name_match_flags": _flag_counts(name_matches),
                      "name_match_sample": name_matches[:5]}

    # D + E — lupa y fusión sobre 3 tokens en 3 chains
    calibrated = ln.link_weights_for(spec)
    rows = []
    for chain, symbol in LUPA_TOKENS:
        link = next(l for l in links if l["chain"] == chain and l["symbol"] == symbol)
        lupa = ln.verify_quantitative(link, fetcher, now_ms=_ms(capture_day))
        row = {"chain": chain, "symbol": symbol, "address": link["address"], "link_type": link["link_type"],
               "lupa": {"status": lupa["status"], "verdict": lupa["evidence"]["verdict"],
                        "llr": lupa["evidence"]["llr_raw"], "metrics": lupa["metrics"],
                        "components": lupa["evidence"]["components"]}}
        for mode, weights in (("heuristico", ln.LINK_WEIGHTS), ("calibrado", calibrated)):
            nev = ln.narrative_evidence(link, emergence, ev, weights=weights)
            sources = {s: None for s in sources_for_chain(chain)}
            sources["dexscreener"] = lupa["evidence"]["llr_raw"]          # la lupa usa DexScreener
            sources["narrative"] = nev["llr_raw"]
            fused = lib_fusion.fuse(chain, link["address"], sources, base_prior=prior)
            row[mode] = {"narrative_llr": nev["llr_raw"], "probability": fused["probability"],
                         "ci_90": fused["ci_90"], "sources_active": fused["sources_active"],
                         "sources_total": fused["sources_total"],
                         "max_individual_contribution": fused["max_individual_contribution"]}
        rows.append(row)
    out["tokens"] = rows
    out["prior"] = {"beta": list(prior), "mean": round(prior[0] / sum(prior), 5), "note": prior_note,
                    "event": "+20% en 48 h (aceleración vertical)"}
    return out


def _ms(day):
    return datetime(day.year, day.month, day.day, tzinfo=timezone.utc).timestamp() * 1000


def _flag_counts(links):
    counts = {}
    for l in links:
        for f in l["risk_flags"]:
            counts[f] = counts.get(f, 0) + 1
    return counts


def print_scenario(s):
    print(f"\n=== Escenario: {s['scenario']} (fecha de análisis {s['as_of']}){'  [SIMULADO]' if s['simulated'] else ''}")
    ev = s["calendar"]["event"]
    print(f"A  Calendario : {ev['title']} sale {ev['date']} ({ev['source']}) -> fase '{ev['phase']}', "
          f"faltan {ev['days_to_event']} días" if ev else "A  Calendario : evento no encontrado")
    w, g = s["attention"]["wikipedia"], s["attention"]["gdelt"]
    lt = w["latest"] or {}
    print(f"B  Atención   : Wikipedia {w['status']} · último {lt.get('date')} = {lt.get('value')} vistas, "
          f"ratio {lt.get('ratio')}x · picos {w['n_spikes']} · emergente hoy={w['emerging_now']}"
          + (f" · SIMULADO desde {w['simulated_from']}" if w.get("simulated_from") else ""))
    print(f"               GDELT {g['status']} ({g['n_points']} puntos) {g['detail'][:60]}")
    m = s["mapping"]
    print(f"C  Mapeo      : {len(m['thematic'])} vínculos temáticos curados · {m['name_match_count']} tokens por "
          f"coincidencia de nombre, flags {m['name_match_flags']}")
    print("D+E Lupa y fusión (evento = +20% en 48h; prior " + f"{s['prior']['mean']:.4f}):")
    for r in s["tokens"]:
        lm = r["lupa"]["metrics"] or {}
        print(f"   {r['chain']:<9}{r['symbol']:<6} lupa={r['lupa']['verdict']:<16} llr={r['lupa']['llr']} "
              f"liq=${lm.get('liquidity_usd', 0):,.0f} vol24=${lm.get('volume_24h_usd', 0):,.0f}")
        for mode in ("heuristico", "calibrado"):
            x = r[mode]
            print(f"      {mode:<11} narrativa llr={x['narrative_llr']:+.3f} -> P={x['probability']:.4f} "
                  f"IC90={x['ci_90']} fuentes {x['sources_active']}/{x['sources_total']}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Demo de la capa narrativa sobre GTA VI.")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--capture-fixtures", action="store_true")
    args = ap.parse_args(argv)
    registry = load_json(REGISTRY_FILE)
    if registry is None:
        print(f"[ERROR] no se pudo leer {REGISTRY_FILE}")
        return 2
    if args.live or args.capture_fixtures:
        fetcher = RecordingFetcher(ln.HttpFetcher()) if args.capture_fixtures else ln.HttpFetcher()
        capture_day = datetime.now(timezone.utc).date()
        mode = "live"
    else:
        fx = load_json(FIXTURES_FILE)
        if fx is None:
            print(f"[ERROR] faltan fixtures en {FIXTURES_FILE}: correr con --capture-fixtures")
            return 2
        fetcher = ln.FixtureFetcher(fx["responses"])
        capture_day = date.fromisoformat(fx["captured_for_day"])
        mode = f"dry-run (fixtures reales capturadas {fx['captured_at']})"
    prior, prior_note = sector_prior()
    print(f"[demo_gta6] modo: {mode}")

    scenarios = [run_scenario("real_hoy", capture_day, fetcher, registry, capture_day, prior, prior_note, False)]
    ev = scenarios[0]["calendar"]["event"]
    if ev:
        as_of = date.fromisoformat(ev["date"]) - timedelta(days=SIM_DAYS_BEFORE_EVENT)
        scenarios.append(run_scenario("simulado_anticipacion", as_of, fetcher, registry, capture_day,
                                      prior, prior_note, True))
    for s in scenarios:
        print_scenario(s)

    if args.capture_fixtures:
        FIXTURES_FILE.parent.mkdir(parents=True, exist_ok=True)
        FIXTURES_FILE.write_text(json.dumps({
            "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "captured_for_day": capture_day.isoformat(),
            "note": "Respuestas reales de APIs públicas sin key, usadas para dry-run reproducible.",
            "responses": fetcher.recorded}, ensure_ascii=False), encoding="utf-8")
        print(f"\n[OK] fixtures: {FIXTURES_FILE} ({len(fetcher.recorded)} respuestas)")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps({"mode": mode, "narrative": NARRATIVE, "scenarios": scenarios},
                                   indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] salida: {OUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
