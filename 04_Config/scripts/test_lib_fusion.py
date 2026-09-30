#!/usr/bin/env python3
"""Tests de lib_fusion (solo biblioteca estándar).

Uso: python 04_Config/scripts/test_lib_fusion.py
"""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_fusion as lf  # noqa: E402

# Activos reales de dos chains distintas
SOL_CHAIN, SOL_MINT = "solana", "8ed8xX8TVRDdeyyUwq7Kyo8VwxMWZ6c5J6ertxaBpump"   # PARASITE
BASE_CHAIN, BASE_MINT = "base", "0x532f27101965dd16442E59d40670FaF5eBB142E4"     # BRETT
FIVE = ["jupiter", "geckoterminal", "dexpaprika", "goplus", "dexscreener"]


class TestWeights(unittest.TestCase):
    def test_equal_priors_give_equal_weights(self):
        w = lf.source_weights(FIVE)
        for v in w.values():
            self.assertAlmostEqual(v, 0.2)

    def test_fixed_share_floor_and_cap(self):
        trust = {"jupiter": {"alpha": 200, "beta": 1}}
        trust.update({s: {"alpha": 1, "beta": 200} for s in FIVE[1:]})
        w = lf.source_weights(FIVE, trust)
        self.assertAlmostEqual(sum(w.values()), 1.0)
        floor = lf.FIXED_SHARE_GAMMA / len(FIVE)
        self.assertTrue(all(v >= floor - 1e-9 for v in w.values()), w)
        self.assertLessEqual(max(w.values()), lf.MAX_WEIGHT + 1e-9)
        self.assertAlmostEqual(w["jupiter"], lf.MAX_WEIGHT)

    def test_infeasible_cap_falls_back_to_uniform(self):
        w = lf.cap_weights([0.9, 0.1], max_weight=0.35)   # 1/N = 0.5 > 0.35
        self.assertEqual([round(v, 9) for v in w], [0.5, 0.5])

    def test_cap_preserves_order_and_sum(self):
        w = lf.cap_weights([0.7, 0.2, 0.05, 0.05], max_weight=0.4)
        self.assertAlmostEqual(sum(w), 1.0)
        self.assertAlmostEqual(w[0], 0.4)
        self.assertGreater(w[1], w[2])


class TestFuse(unittest.TestCase):
    def test_output_schema(self):
        out = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": -0.5, "geckoterminal": 0.8, "dexpaprika": None,
                                            "goplus": 0.3, "dexscreener": None, "madeonsol": 1.2})
        for key in ("probability", "ci_90", "sources_active", "sources_total",
                    "max_individual_contribution", "breakdown"):
            self.assertIn(key, out)
        self.assertEqual(out["sources_active"], 4)
        self.assertEqual(out["sources_total"], 6)
        self.assertAlmostEqual(sum(out["breakdown"].values()), 1.0, places=3)
        self.assertEqual(out["label"], "HEURISTICA_NO_CALIBRADA")

    def test_no_evidence_returns_base_rate(self):
        out = lf.fuse(SOL_CHAIN, SOL_MINT, {s: None for s in FIVE}, base_prior=(1, 3))
        self.assertAlmostEqual(out["probability"], 0.25, places=4)
        self.assertEqual(out["sources_active"], 0)
        self.assertEqual(out["max_individual_contribution"], 0.0)

    def test_clipping_bounds_a_single_source(self):
        big = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": 50.0, "goplus": None})
        at_clip = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": lf.LLR_CLIP, "goplus": None})
        self.assertEqual(big["probability"], at_clip["probability"])
        self.assertEqual(lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": math.inf})["contributions"]
                         ["jupiter"]["llr_clipped"], lf.LLR_CLIP)

    def test_monotonic_in_evidence(self):
        ps = [lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": v, "goplus": None})["probability"]
              for v in (-2.0, -0.5, 0.0, 0.5, 2.0)]
        self.assertEqual(ps, sorted(ps))
        self.assertLess(ps[0], ps[-1])

    def test_ci_deterministic_and_contains_point(self):
        src = {"jupiter": 1.0, "geckoterminal": -0.4, "goplus": None}
        a = lf.fuse(SOL_CHAIN, SOL_MINT, src, base_prior=(1, 3))
        b = lf.fuse(SOL_CHAIN, SOL_MINT, src, base_prior=(1, 3))
        self.assertEqual(a["ci_90"], b["ci_90"])
        lo, hi = a["ci_90"]
        self.assertLessEqual(lo, a["probability"])
        self.assertLessEqual(a["probability"], hi)

    def test_ci_narrows_with_more_history(self):
        src = {"jupiter": 1.0, "goplus": None}
        wide = lf.fuse(SOL_CHAIN, SOL_MINT, src, base_prior=(1, 3))
        narrow = lf.fuse(SOL_CHAIN, SOL_MINT, src, base_prior=(26, 76))
        self.assertLess(narrow["ci_90"][1] - narrow["ci_90"][0], wide["ci_90"][1] - wide["ci_90"][0])

    def test_max_individual_contribution(self):
        one = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": 1.0, "goplus": None})
        self.assertEqual(one["max_individual_contribution"], 1.0)
        two = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": 1.0, "goplus": -1.0})
        self.assertEqual(two["max_individual_contribution"], 0.5)

    def test_nan_and_non_numeric_are_inactive(self):
        out = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": float("nan"), "goplus": "0.5", "x": True})
        self.assertEqual(out["sources_active"], 0)

    def test_rejects_empty_identifiers(self):
        with self.assertRaises(ValueError):
            lf.fuse("", SOL_MINT, {"jupiter": 0.1})


class TestChainAgnostic(unittest.TestCase):
    def test_two_chains_same_math(self):
        src = {"geckoterminal": 0.6, "dexpaprika": -0.2, "goplus": None, "dexscreener": None}
        sol = lf.fuse(SOL_CHAIN, SOL_MINT, src)
        base = lf.fuse(BASE_CHAIN, BASE_MINT, src)
        self.assertEqual((sol["chain"], sol["mint"]), (SOL_CHAIN, SOL_MINT))
        self.assertEqual((base["chain"], base["mint"]), (BASE_CHAIN, BASE_MINT))
        self.assertEqual(base["asset"], f"{BASE_CHAIN}:{BASE_MINT}")
        self.assertEqual(sol["probability"], base["probability"])
        self.assertEqual(sol["ci_90"], base["ci_90"])

    def test_chain_specific_source_only_where_registered(self):
        sol = lf.fuse(SOL_CHAIN, SOL_MINT, {"jupiter": 0.5, "geckoterminal": None})
        base = lf.fuse(BASE_CHAIN, BASE_MINT, {"geckoterminal": None})
        self.assertIn("jupiter", sol["breakdown"])
        self.assertNotIn("jupiter", base["breakdown"])
        self.assertEqual(base["sources_total"], 1)

    def test_no_hardcoded_chain_in_library(self):
        text = Path(lf.__file__).read_text(encoding="utf-8").lower()
        for chain in ("solana", "ethereum", "base58", "pump.fun", "jupiter"):
            self.assertNotIn(chain, text, f"lib_fusion menciona '{chain}'")

    def test_rrf_across_chains(self):
        a, b = lf.asset_key(SOL_CHAIN, SOL_MINT), lf.asset_key(BASE_CHAIN, BASE_MINT)
        out = lf.rrf({"lista_1": [a, b], "lista_2": [b]})
        self.assertEqual(out[0]["item"], b)
        self.assertEqual(out[0]["ranks"], {"lista_1": 2, "lista_2": 1})


class TestTrustLoop(unittest.TestCase):
    def test_base_rate_posterior(self):
        self.assertEqual(lf.base_rate_posterior([False, False]), (1.0, 3.0))
        self.assertEqual(lf.base_rate_posterior([True, False, True]), (3.0, 2.0))

    def test_update_trust_directions(self):
        t0 = lf.default_trust(["a", "b", "c", "d"])
        t1 = lf.update_trust(t0, {"a": 0.8, "b": -0.8, "c": None, "d": 0.0}, outcome=True)
        self.assertEqual(t1["a"], {"alpha": 2.0, "beta": 1.0})   # dijo sube, subió
        self.assertEqual(t1["b"], {"alpha": 1.0, "beta": 2.0})   # dijo baja, subió
        self.assertEqual(t1["c"], {"alpha": 1.0, "beta": 1.0})   # sin evidencia
        self.assertEqual(t1["d"], {"alpha": 1.0, "beta": 1.0})   # neutro
        self.assertEqual(t0["a"], {"alpha": 1.0, "beta": 1.0})   # no muta la entrada
        t2 = lf.update_trust(t0, {"b": -0.8}, outcome=False)
        self.assertEqual(t2["b"], {"alpha": 2.0, "beta": 1.0})   # dijo baja, bajó

    def test_replay_rejects_lookahead(self):
        records = [
            {"id": "ok", "alert_ts": 1000.0, "snapshot_ts": 900.0, "llrs": {"a": 1.0}, "outcome": True},
            {"id": "post", "alert_ts": 1000.0, "snapshot_ts": 1100.0, "llrs": {"a": 1.0}, "outcome": True},
            {"id": "nosnap", "alert_ts": 1000.0, "snapshot_ts": None, "llrs": {}, "outcome": False},
        ]
        trust, stats = lf.replay_trust(["a"], records)
        self.assertEqual(stats["applied"], 1)
        self.assertEqual(trust["a"], {"alpha": 2.0, "beta": 1.0})
        self.assertEqual([r["id"] for r in stats["rejected"]], ["post", "nosnap"])

    def test_trust_moves_weights(self):
        trust = {"a": {"alpha": 6, "beta": 2}, "b": {"alpha": 2, "beta": 6}}
        w = lf.source_weights(["a", "b", "c", "d", "e"], trust)
        self.assertGreater(w["a"], w["c"])
        self.assertGreater(w["c"], w["b"])

    def test_cap_limits_differentiation_with_few_sources(self):
        # Con N=3, 1/N ≈ 0.333 está casi en el tope 0.35: la fuente confiable y la neutra empatan.
        trust = {"a": {"alpha": 20, "beta": 2}, "b": {"alpha": 2, "beta": 20}}
        w = lf.source_weights(["a", "b", "c"], trust)
        self.assertAlmostEqual(w["a"], lf.MAX_WEIGHT)
        self.assertAlmostEqual(w["c"], lf.MAX_WEIGHT)
        self.assertLess(w["b"], w["c"])


class TestRRF(unittest.TestCase):
    def test_known_scores(self):
        out = lf.rrf({"a": ["x", "y", "z"], "b": ["y", "z"], "c": ["y"]}, k=60)
        self.assertEqual([r["item"] for r in out], ["y", "z", "x"])
        self.assertAlmostEqual(out[0]["rrf_score"], round(1/62 + 1/61 + 1/61, 6))

    def test_duplicates_count_once(self):
        out = lf.rrf({"a": ["x", "x", "y"]})
        self.assertEqual(out[0], {"item": "x", "rrf_score": round(1/61, 6), "ranks": {"a": 1}})
        self.assertEqual(out[1]["ranks"], {"a": 3})

    def test_ties_are_deterministic(self):
        out = lf.rrf({"a": ["y", "x"], "b": ["x", "y"]})
        self.assertEqual(out[0]["rrf_score"], out[1]["rrf_score"])
        self.assertEqual([r["item"] for r in out], ["x", "y"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
