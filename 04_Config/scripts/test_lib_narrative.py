#!/usr/bin/env python3
"""Tests de lib_narrative (unittest, sin red: todo con FixtureFetcher o datos sintéticos).

Uso: python 04_Config/scripts/test_lib_narrative.py
"""
import json
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lib_narrative as ln  # noqa: E402

SOL, BASE = "solana", "base"
ATLAS = "ATLASXmbPQxBUYbxPsV97usA3fPQYEqzQBUHgiFCUsXx"
PRIME_BASE = "0xfa980ced6895ac314e7de34ef1bfae90a5add21b"
DAY_MS = 86_400_000
NOW_MS = 1_790_000_000_000

REGISTRY = {"narratives": {"gta6": {
    "keywords": ["GTA 6", "GTA VI", "Grand Theft Auto VI"],
    "name_keywords": ["gta6", "gtavi"],
    "link_weight_overrides": {"thematic": 0.0, "evidence": "piloto"},
    "tokens": [{"chain": SOL, "address": ATLAS, "symbol": "ATLAS", "link_type": "thematic"},
               {"chain": BASE, "address": PRIME_BASE, "symbol": "PRIME", "link_type": "thematic"}]}}}


def pair(chain, address, symbol, liq, age_days=None, vol=0.0, pc=0.0, buys=0, sells=0, name=""):
    p = {"chainId": chain, "dexId": "dex", "pairAddress": f"pair-{chain}-{symbol}",
         "baseToken": {"address": address, "symbol": symbol, "name": name or symbol},
         "liquidity": {"usd": liq}, "volume": {"h24": vol}, "priceChange": {"h24": pc},
         "txns": {"h24": {"buys": buys, "sells": sells}}, "priceUsd": "1.0"}
    if age_days is not None:
        p["pairCreatedAt"] = NOW_MS - age_days * DAY_MS
    return p


def flat_series(n, value=100.0, start=date(2026, 1, 1), spikes=None, source="wikipedia_pageviews"):
    spikes = spikes or {}
    return {"topic": "t", "source": source, "status": "ok",
            "points": [{"date": (start + timedelta(days=i)).isoformat(), "value": spikes.get(i, value + (i % 3))}
                       for i in range(n)]}


class TestFetchers(unittest.TestCase):
    def test_request_key_is_order_independent(self):
        self.assertEqual(ln.request_key("u", {"b": 2, "a": 1}), ln.request_key("u", {"a": 1, "b": 2}))

    def test_fixture_fetcher_missing_key_is_error_not_exception(self):
        f = ln.FixtureFetcher({ln.request_key("u", {"q": 1}): {"ok": True}})
        self.assertEqual(f("u", {"q": 1})["data"], {"ok": True})
        self.assertEqual(f("u", {"q": 2})["status"], "error")


class TestCapaA(unittest.TestCase):
    def test_event_phase_boundaries(self):
        ev, today = date(2026, 11, 19), date(2026, 11, 19)
        self.assertEqual(ln.event_phase(ev, today - timedelta(days=15))[0], "lejano")
        self.assertEqual(ln.event_phase(ev, today - timedelta(days=14))[0], "anticipacion")
        self.assertEqual(ln.event_phase(ev, today)[0], "evento")
        self.assertEqual(ln.event_phase(ev, today + timedelta(days=7))[0], "post")
        self.assertEqual(ln.event_phase(ev, today + timedelta(days=8))[0], "pasado")

    def test_calendar_merges_duplicate_dates_and_manual_events(self):
        today = date(2026, 9, 30)
        rows = [
            {"item": {"value": "http://www.wikidata.org/entity/Q23648408"}, "itemLabel": {"value": "Grand Theft Auto VI"},
             "date": {"value": "2026-11-19T00:00:00Z"}, "links": {"value": "66"}},
            {"item": {"value": "http://www.wikidata.org/entity/Q23648408"}, "itemLabel": {"value": "Grand Theft Auto VI"},
             "date": {"value": "2026-11-12T00:00:00Z"}, "links": {"value": "66"}},
            {"item": {"value": "http://www.wikidata.org/entity/Q1"}, "itemLabel": {"value": "Q1"},
             "date": {"value": "2026-10-15T00:00:00Z"}, "links": {"value": "20"}},
        ]
        key = ln.request_key(ln.WIKIDATA_SPARQL, {"query": ln._wikidata_query("Q7889", today, today + timedelta(days=90), 15),
                                                  "format": "json"})
        cal = ln.fetch_eventos_calendario(today, 90, ln.FixtureFetcher({key: {"results": {"bindings": rows}}}),
                                          manual_events=[{"id": "fomc-2026-10", "title": "FOMC", "date": "2026-10-28",
                                                          "category": "macro"}])
        gta = next(e for e in cal["events"] if e.get("wikidata_item") == "Q23648408")
        self.assertEqual(gta["date"], "2026-11-12")
        self.assertEqual(gta["date_quality"], "multiple")
        self.assertEqual(next(e for e in cal["events"] if e.get("wikidata_item") == "Q1")["label_quality"], "sin_etiqueta_en")
        self.assertIn("fomc-2026-10", [e["id"] for e in cal["events"]])
        self.assertEqual([e["date"] for e in cal["events"]], sorted(e["date"] for e in cal["events"]))

    def test_calendar_source_failure_is_reported(self):
        cal = ln.fetch_eventos_calendario(date(2026, 9, 30), 30, ln.FixtureFetcher({}))
        self.assertEqual(cal["events"], [])
        self.assertEqual(cal["sources"][0]["status"], "error")


class TestCapaB(unittest.TestCase):
    def test_wikipedia_and_gdelt_parsing(self):
        start, end = date(2023, 12, 4), date(2023, 12, 5)
        wurl = ln.WIKIPEDIA_PAGEVIEWS.format(project="en.wikipedia", article="Grand_Theft_Auto_VI",
                                             start="20231204", end="20231205")
        gkey = ln.request_key(ln.GDELT_DOC, {"query": '"x"', "mode": "timelinevol", "format": "json",
                                             "startdatetime": "20231204000000", "enddatetime": "20231205235959"})
        f = ln.FixtureFetcher({
            wurl: {"items": [{"timestamp": "2023120400", "views": 21711}, {"timestamp": "2023120500", "views": 341519}]},
            gkey: {"timeline": [{"data": [{"date": "20231204T000000Z", "value": 0.1}]}]}})
        w = ln.fetch_attention_series("gta6", "wikipedia_pageviews", start, end, f, article="Grand_Theft_Auto_VI")
        self.assertEqual(w["points"][1], {"date": "2023-12-05", "value": 341519.0})
        g = ln.fetch_attention_series("x", "gdelt_timelinevol", start, end, f, query='"x"')
        self.assertEqual(g["points"], [{"date": "2023-12-04", "value": 0.1}])
        with self.assertRaises(ValueError):
            ln.fetch_attention_series("x", "twitter", start, end, f)

    def test_spike_detected(self):
        det = ln.detect_narrative_emerging(flat_series(40, spikes={35: 5000.0}))
        self.assertEqual([s["date"] for s in det["spikes"]], [(date(2026, 1, 1) + timedelta(days=35)).isoformat()])

    def test_no_lookahead_result_invariant_to_future_data(self):
        # Lo detectado hasta el día t no puede cambiar al agregar datos posteriores a t.
        # Ventana corta (4 días) para que datos futuros SÍ movieran la mediana si se colaran.
        def series(n):
            vals = [100.0] * 10 + [600.0] + [1000.0] * 5
            return {"topic": "t", "source": "x", "points": [
                {"date": (date(2026, 1, 1) + timedelta(days=i)).isoformat(), "value": vals[i]} for i in range(n)]}
        kw = {"baseline_days": 4, "min_baseline": 0.0}
        past = ln.detect_narrative_emerging(series(11), **kw)
        full = ln.detect_narrative_emerging(series(16), **kw)
        day10 = (date(2026, 1, 1) + timedelta(days=10)).isoformat()
        self.assertEqual([s["date"] for s in past["spikes"]], [day10])
        self.assertEqual(past["spikes"], [s for s in full["spikes"] if s["date"] <= day10])

    def test_last_day_spike_is_emerging_now(self):
        det = ln.detect_narrative_emerging(flat_series(35, spikes={34: 900.0}))
        self.assertTrue(det["emerging_now"])

    def test_small_baseline_is_ignored(self):
        det = ln.detect_narrative_emerging(flat_series(40, value=3.0, spikes={35: 300.0}))
        self.assertEqual(det["spikes"], [])   # mediana < 50 vistas: ruido

    def test_flat_series_with_zero_mad(self):
        s = {"topic": "t", "source": "gdelt_timelinevol", "points":
             [{"date": (date(2026, 1, 1) + timedelta(days=i)).isoformat(), "value": 1.0 if i < 30 else 9.0} for i in range(31)]}
        self.assertEqual(len(ln.detect_narrative_emerging(s)["spikes"]), 1)


class TestCapaC(unittest.TestCase):
    def test_keyword_matcher_word_boundaries(self):
        m = ln.KeywordMatcher(REGISTRY)
        hits = m.extract("Rockstar confirma GTA VI; el trailer de gta 6 rompe récords. GTA 60 no cuenta.")
        self.assertEqual([h["keyword"] for h in hits], ["GTA VI", "GTA 6"])

    def test_mapping_two_chains_and_copycats(self):
        pairs = [
            pair(SOL, "GTA6copy111111111111111111111111111111111", "GTA6", 3000, age_days=2),
            pair(BASE, "0x" + "ab" * 20, "GTAVI", 50000, age_days=90),
            pair(BASE, PRIME_BASE.upper().replace("0X", "0x"), "PRIME", 1e6, age_days=900),   # ya curado (EVM case)
            pair(SOL, "Unrelated1111111111111111111111111111111", "DOGE", 1e6, age_days=900),
        ]
        links = ln.map_narrative_to_tokens("gta6", REGISTRY, pairs, now_ms=NOW_MS)
        self.assertEqual([(l["chain"], l["link_type"]) for l in links],
                         [(BASE, "thematic"), (SOL, "thematic"), (BASE, "name_match"), (SOL, "name_match")])
        sol_copy = next(l for l in links if l["chain"] == SOL and l["link_type"] == "name_match")
        self.assertEqual(sol_copy["risk_flags"], ["copycat_suspect", "new_token", "low_liquidity"])
        base_copy = next(l for l in links if l["chain"] == BASE and l["link_type"] == "name_match")
        self.assertEqual(base_copy["risk_flags"], ["copycat_suspect"])

    def test_unknown_narrative_raises(self):
        with self.assertRaises(KeyError):
            ln.map_narrative_to_tokens("nada", REGISTRY)


class TestCapaD(unittest.TestCase):
    def test_lupa_uses_only_pairs_of_the_requested_chain(self):
        data = {"pairs": [pair(BASE, PRIME_BASE, "PRIME", 20_000, age_days=800, vol=40_000, pc=5, buys=300, sells=100),
                          pair("ethereum", PRIME_BASE, "PRIME", 5_000_000, age_days=900)]}
        f = ln.FixtureFetcher({ln.DEXSCREENER_TOKENS.format(address=PRIME_BASE): data})
        res = ln.verify_quantitative({"chain": BASE, "address": PRIME_BASE}, f, now_ms=NOW_MS)
        self.assertEqual(res["metrics"]["liquidity_usd"], 20_000)
        self.assertEqual(res["evidence"]["verdict"], "flujo_confirmado")
        self.assertAlmostEqual(res["evidence"]["llr_raw"], 0.75)

    def test_lupa_chain_without_pairs(self):
        f = ln.FixtureFetcher({ln.DEXSCREENER_TOKENS.format(address=ATLAS): {"pairs": [pair(BASE, ATLAS, "X", 1)]}})
        res = ln.verify_quantitative({"chain": SOL, "address": ATLAS}, f, now_ms=NOW_MS)
        self.assertEqual(res["status"], "sin_par_en_chain")
        self.assertEqual(res["evidence"]["verdict"], "sin_datos")

    def test_lupa_new_illiquid_token_is_risk(self):
        m = ln.pair_metrics([pair(SOL, "x", "GTA6", 3000, age_days=1, vol=100)], SOL, now_ms=NOW_MS)
        ev = ln.lupa_evidence(m)
        self.assertEqual(ev["verdict"], "riesgo")
        self.assertLess(ev["llr_raw"], -1.0)


class TestCapaE(unittest.TestCase):
    EMERGING = {"latest": {"ratio": 10.0}}

    def test_thematic_anticipation_heuristic_vs_calibrated(self):
        link = {"link_type": "thematic"}
        heur = ln.narrative_evidence(link, self.EMERGING, {"phase": "anticipacion"})
        self.assertAlmostEqual(heur["llr_raw"], 0.5)                      # 0.5 x fuerza 1.0
        cal = ln.narrative_evidence(link, self.EMERGING, {"phase": "anticipacion"},
                                    weights=ln.link_weights_for(REGISTRY["narratives"]["gta6"]))
        self.assertEqual(cal["llr_raw"], 0.0)

    def test_post_event_is_negative_and_copycat_penalized(self):
        self.assertLess(ln.narrative_evidence({"link_type": "direct"}, self.EMERGING, {"phase": "post"})["llr_raw"], 0)
        cc = ln.narrative_evidence({"link_type": "name_match", "risk_flags": ["copycat_suspect", "new_token"]},
                                   self.EMERGING, {"phase": "anticipacion"})
        self.assertEqual(cc["llr_raw"], ln.COPYCAT_LLR)

    def test_override_ignores_unknown_keys(self):
        w = ln.link_weights_for({"link_weight_overrides": {"thematic": 0.1, "evidence": "x", "bogus": 5}})
        self.assertEqual(w, {"direct": 1.0, "thematic": 0.1, "name_match": 0.0})


class TestCiencia(unittest.TestCase):
    def prices(self, n=60, daily=0.0, jump_day=None, jump=0.0):
        out, v = {}, 100.0
        for i in range(n):
            d = (date(2026, 1, 1) + timedelta(days=i)).isoformat()
            v *= 1 + daily + (jump if jump_day is not None and i == jump_day else 0.0)
            out[d] = v
        return out

    def test_event_study_abnormal_and_vertical(self):
        basket = {"A": self.prices(jump_day=11, jump=0.30), "B": self.prices()}
        rows = ln.event_study([date(2026, 1, 11)], basket, self.prices(), 0, 1)
        self.assertAlmostEqual(rows[0]["abnormal_return"], 0.15, places=6)
        self.assertTrue(rows[0]["vertical"])

    def test_bootstrap_deterministic_and_brackets_mean(self):
        vals = [0.01 * i for i in range(-10, 21)]
        ci = ln.bootstrap_ci(vals)
        self.assertEqual(ci, ln.bootstrap_ci(vals))
        self.assertLess(ci[0], sum(vals) / len(vals))
        self.assertGreater(ci[1], sum(vals) / len(vals))
        self.assertIsNone(ln.bootstrap_ci([]))

    def test_placebo_excludes_radius(self):
        days = [date(2026, 1, 1) + timedelta(days=i) for i in range(30)]
        pl = ln.placebo_days(days, [date(2026, 1, 15)], exclusion_radius=7)
        self.assertTrue(all(abs((d - date(2026, 1, 15)).days) > 7 for d in pl))
        self.assertEqual(len(pl), 30 - 15)

    def test_walk_forward_purge_and_disjoint(self):
        days = [date(2024, 1, 1) + timedelta(days=i) for i in range(0, 900, 3)]
        splits = ln.walk_forward_splits(days, train_days=365, test_days=180, purge_days=2)
        self.assertGreater(len(splits), 0)
        for train, test in splits:
            self.assertFalse(set(train) & set(test))
            self.assertGreater((min(test) - max(train)).days, 2)

    def test_merge_close_events(self):
        ds = [date(2026, 1, 1), date(2026, 1, 3), date(2026, 1, 20)]
        self.assertEqual(ln.merge_close_events(ds, 7), [date(2026, 1, 1), date(2026, 1, 20)])

    def test_evaluate_hypothesis_acceptance_rules(self):
        win = [{"abnormal_return": 0.05, "vertical": False}] * 18 + [{"abnormal_return": -0.01, "vertical": False}] * 4
        placebo = [{"abnormal_return": 0.01 if i % 2 else -0.01, "vertical": False} for i in range(200)]
        self.assertTrue(ln.evaluate_hypothesis(win, placebo)["accepted"])
        few = ln.evaluate_hypothesis(win[:10], placebo)
        self.assertFalse(few["accepted"])
        self.assertIn("n=10 < 20", few["rejection_reasons"])


class TestAgnosticoEIntegracion(unittest.TestCase):
    def test_no_hardcoded_chain_in_library(self):
        text = (HERE / "lib_narrative.py").read_text(encoding="utf-8").lower()
        for token in ("solana", "ethereum", "base58", "pump.fun", "jupiter", '"base"'):
            self.assertNotIn(token, text, f"lib_narrative menciona {token!r}")

    def test_demo_dry_run_three_chains(self):
        import demo_gta6
        with tempfile.TemporaryDirectory() as tmp:
            demo_gta6.OUT_FILE = Path(tmp) / "demo.json"
            self.assertEqual(demo_gta6.main([]), 0)
            out = json.loads(demo_gta6.OUT_FILE.read_text(encoding="utf-8"))
        self.assertTrue(out["mode"].startswith("dry-run"))
        self.assertEqual(len(out["scenarios"]), 2)
        for s in out["scenarios"]:
            self.assertEqual({t["chain"] for t in s["tokens"]}, {"ethereum", "base", "solana"})
            for t in s["tokens"]:
                lo, hi = t["calibrado"]["ci_90"]
                self.assertLessEqual(lo, t["calibrado"]["probability"])
                self.assertLessEqual(t["calibrado"]["probability"], hi)
        self.assertTrue(out["scenarios"][1]["attention"]["wikipedia"]["emerging_now"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
