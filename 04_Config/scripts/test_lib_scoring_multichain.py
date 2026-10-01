#!/usr/bin/env python3
"""Tests de lib_scoring_multichain (doc 27, Fase 7). unittest, sin red, con datos mock por tipo.

Uso: python 04_Config/scripts/test_lib_scoring_multichain.py
"""
import math
import random
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_scoring_multichain as L  # noqa: E402

NOW = datetime(2026, 10, 1, 17, 0, tzinfo=timezone.utc)
NOW_MS = int(NOW.timestamp() * 1000)
DAY = 86_400_000


def klines(closes, end_ms=NOW_MS - 3_600_000, spread=0.01):
    """Velas diarias cerradas que terminan antes de `end_ms`."""
    n = len(closes)
    rows = []
    for i, c in enumerate(closes):
        close_t = end_ms - (n - 1 - i) * DAY
        rows.append([close_t - DAY + 1, c, c * (1 + spread), c * (1 - spread), c, 1000.0, close_t])
    return rows


def garch_series(n, a=0.10, b=0.85, sigma=0.02, seed=7):
    rnd = random.Random(seed)
    w = sigma ** 2 * (1 - a - b)
    s2, out = sigma ** 2, []
    for _ in range(n):
        x = rnd.gauss(0, 1) * math.sqrt(s2)
        out.append(x)
        s2 = w + a * x * x + b * s2
    return out


def prices_from(returns, p0=100.0):
    out = [p0]
    for r in returns:
        out.append(out[-1] * math.exp(r))
    return out


class CommonTest(unittest.TestCase):
    def test_combine_cobertura_y_formula(self):
        comps = [L.comp("a", 0.5, 30, "x", "s"), L.comp("b", None, 20, None, "s"), L.comp("c", -2, 50, "y", "s")]
        r = L.combine(comps)
        self.assertEqual(r["confidence"], 0.8)
        self.assertAlmostEqual(r["D"], (30 * 0.5 + 50 * -1) / 80)            # s se recorta a ±1
        self.assertEqual(r["score"], round(50 + 50 * r["D"]))
        self.assertIn("b: n/d", r["reasons"])
        self.assertEqual(L.combine(comps, multiplier=1.5, adjust=-10)["score"],
                         round(L.clip(50 + 50 * r["D"] * 1.5 - 10, 0, 100)))
        self.assertIsNone(L.combine([L.comp("z", None, 100, None, "s")])["score"])

    def test_percentil(self):
        self.assertIsNone(L._pct_rank(1, [1, 2]))
        self.assertEqual(L._pct_rank(3, [1, 2, 3]), 1.0)
        self.assertEqual(L._pct_rank(1, [1, 2, 3]), 0.0)


class VolatilityTest(unittest.TestCase):
    def test_garch_recupera_parametros_y_pronostica(self):
        r = garch_series(1500)
        g = L.garch11(r)
        self.assertAlmostEqual(g["alpha"] + g["beta"], 0.95, delta=0.05)
        self.assertGreater(g["sigma_next"], 0)
        self.assertAlmostEqual(g["sigma_long"], 0.02, delta=0.004)
        self.assertIsNone(L.garch11(r[:99]))
        # El pronóstico sigue la recursión con los parámetros elegidos
        s2 = g["sigma_long"] ** 2
        for x in r:
            s2_last, s2 = s2, g["omega"] + g["alpha"] * x * x + g["beta"] * s2
        self.assertAlmostEqual(g["sigma_next"], math.sqrt(s2), places=12)
        self.assertAlmostEqual(g["sigma_last"], math.sqrt(s2_last), places=12)

    def test_atr_bollinger_y_velas_cerradas(self):
        rows = klines([100.0] * 20, spread=0.01)
        self.assertAlmostEqual(L.atr(rows), 2.0)                               # high − low = 2 todos los días
        mid, lo, hi, w = L.bollinger([100.0] * 19 + [120.0])
        self.assertAlmostEqual(mid, 101.0)
        self.assertGreater(hi, 101.0)
        open_day = rows + [[NOW_MS - 1000, 1, 1, 1, 1, 1, NOW_MS + 3_600_000]]
        self.assertEqual(len(L.closed_klines(open_day, NOW_MS)), 20)           # la vela del día en curso no cuenta


class BlueChipTest(unittest.TestCase):
    def asset(self, ch24=3.0, funding=None, fng=50.0, closes=None):
        closes = closes or prices_from(garch_series(399, seed=3), 60000)
        return {"cg_id": "bitcoin", "symbol": "BTC", "price_usd": closes[-1], "change_24h": ch24,
                "universe_a": {"klines_1d": klines(closes), "fear_greed": {"value": fng},
                               "perp": {"funding_1h": funding} if funding is not None else None}}

    def test_componentes_y_barreras(self):
        comps, m, adj, notes, extra = L.components_blue_chip(self.asset(funding=0.00005, fng=15), NOW_MS)
        by = {c["name"].split(" (")[0].split(" [")[0]: c for c in comps}
        self.assertEqual(len(comps), 5)
        self.assertGreater(by["Retorno 24 h / σ GARCH"]["s"], 0)
        self.assertEqual(by["Funding"]["s"], -1)                               # 0,005%/h = 43,8% anual >= 30%
        self.assertEqual(by["Fear & Greed"]["s"], 1)                           # 15 <= 20
        self.assertIn("garch", extra)
        self.assertAlmostEqual(extra["barrier_pct"], 2 * extra["garch"]["sigma_next"] * math.sqrt(2) * 100, places=2)
        self.assertEqual(m, 1.0)
        score, reasons, conf = L.score_blue_chip(self.asset(funding=0.00005, fng=15), NOW_MS)
        self.assertEqual(conf, 1.0)
        self.assertTrue(0 <= score <= 100)

    def test_sin_velas_queda_sin_cobertura(self):
        a = self.asset()
        a["universe_a"] = {"klines_1d": None, "fear_greed": {"value": 85}}
        score, reasons, conf = L.score_blue_chip(a, NOW_MS)
        self.assertEqual(conf, 0.15)                                           # solo Fear & Greed
        self.assertEqual(score, 0)                                             # 85 >= 80 -> −1 -> 50 − 50

    def test_tendencia_y_squeeze(self):
        hist = prices_from(garch_series(379, seed=5), 100.0)                   # historia con volatilidad
        closes = hist + [hist[-1] * (1 + 0.0001 * (i % 2)) for i in range(20)]  # últimas 20 casi planas: squeeze
        a = self.asset(closes=closes)
        a["price_usd"] = closes[-1] * 1.10                                     # rompe arriba
        comps, *_ = L.components_blue_chip(a, NOW_MS)
        by = {c["name"]: c for c in comps}
        self.assertEqual(by["Bollinger(20,2) con squeeze"]["s"], 1)
        self.assertEqual(by["Tendencia (MA20 ± ATR14)"]["s"], 1)


class GroupsTest(unittest.TestCase):
    def test_l1_l2_con_ranking_entre_chains(self):
        peers = [{"derived": {"dex_volume_tvl_24h": v, "fees_tvl_annualized_pct": f}}
                 for v, f in ((0.1, 5.0), (0.2, 10.0), (0.4, 20.0))]
        a = {"symbol": "MON", "change_7d": 30.0, "card": {"tvl": {"log_growth_7d": 0.05, "accel_7d": -0.05},
                                                          "derived": {"dex_volume_tvl_24h": 0.4,
                                                                      "fees_tvl_annualized_pct": 5.0}}}
        comps, *_ = L.components_l1_l2(a, peers, eth_change_7d=10.0)
        self.assertEqual([c["s"] for c in comps], [0.5, -1.0, 1.0, -1.0, 1.0])
        score, _, conf = L.score_l1_l2(a, peers, 10.0)
        self.assertEqual((score, conf), (round(50 + 50 * (12.5 - 15 + 20 - 15 + 25) / 100), 1.0))

    def test_gobernanza(self):
        a = {"symbol": "GOV", "mcap_usd": 40e6, "fdv_usd": 120e6, "change_7d": 12.0, "category_median_7d": 2.0,
             "protocol": {"tvl": 80e6, "change_7d": 15.0}}
        comps, *_ = L.components_governance(a)
        s = [c["s"] for c in comps]
        self.assertAlmostEqual(s[0], 1.0)                                      # ln 1,15 / 0,10 > 1
        self.assertAlmostEqual(s[1], 0.5, places=3)                            # mcap/TVL = 0,5
        self.assertIsNone(s[2])                                                # Snapshot sin colectar
        self.assertAlmostEqual(s[3], -1.0)                                     # FDV/mcap = 3
        self.assertAlmostEqual(s[4], 0.5)
        self.assertEqual(L.score_governance(a)[2], 0.8)
        self.assertEqual(L.score_governance(dict(a, protocol=None))[2], 0.35)  # sin TVL: no llega a 0,6

    def test_depin_y_rwa(self):
        a = {"symbol": "DPN", "volume_24h_usd": 30e6, "mcap_usd": 100e6, "fdv_usd": 150e6, "change_7d": 4.0,
             "category_median_7d": 6.0, "category_median_turnover": 0.1, "category_vs_market_24h": 2.1}
        comps, *_ = L.components_depin(a)
        self.assertAlmostEqual(comps[0]["s"], 1.0)                             # 0,3 vs 0,1 = 3x -> ln3/ln3
        self.assertAlmostEqual(comps[2]["s"], round(-math.log(1.5) / math.log(3), 4))
        self.assertEqual(L.score_depin(a)[2], 0.8)
        stable = {"symbol": "TBILL", "change_24h": 0.01, "change_7d": 0.1}
        self.assertEqual(L.score_rwa(stable)[0], None)
        rwa = {"symbol": "RWA", "change_24h": 2.0, "change_7d": 3.0, "protocol": {"change_7d": 15.0},
               "category_vs_market_24h": 0.0, "category_median_7d": -2.0}
        score, _, conf = L.score_rwa(rwa)
        self.assertEqual(conf, 0.85)
        self.assertGreater(score, 56)

    def test_sintetico_preventa_y_establecido(self):
        self.assertEqual(L.score_synthetic({"change_24h": 8.0})[2], 0.3)
        self.assertEqual(L.score_presale({})[2], 0.0)
        pre = {"days_to_listing": 6, "narrative": {"intensity": 4.2, "signal": True}}
        score, _, conf = L.score_presale(pre)
        self.assertEqual(conf, 0.5)
        self.assertEqual(score, round(50 + 50 * (25 + 25 * math.log(4.2) / math.log(10)) / 50))
        arc = {"volume_24h_usd": 6955.45, "liquidity_usd": 10333551.81, "pair_age_days": 621.7}
        score, reasons, conf = L.score_established(arc)                        # doc 27 §4.10, caso arc
        self.assertEqual((score, conf), (0, 0.2))
        self.assertIn("Descuento por edad: −10 (par > 1 año)", reasons)

    def test_memecoin_reusa_v721_con_el_mapeo_de_geckoterminal(self):
        seen = {}

        def fake_scorer(tok, dx):
            seen.update(tok=tok, dx=dx)
            return 61, ["MCap > $1M"]
        a = {"address": "0xabc", "symbol": "PEPE", "price_usd": 0.01, "liquidity_usd": 5e5, "volume_24h_usd": 2e6,
             "fdv_usd": 3e6, "change_24h": 40.0, "change_1h": 3.0, "pool_created_at": "2026-09-30T17:00:00Z",
             "pool_address": "0xpool"}
        score, reasons, conf = L.score_memecoin(a, fake_scorer)
        self.assertEqual((score, reasons, conf), (61, ["MCap > $1M"], 0.75))  # sin m5/h1: 6 de 8 campos
        self.assertEqual(seen["dx"]["marketCapUsd"], 3e6)                      # sin mcap usa FDV
        self.assertEqual(seen["dx"]["pairCreatedAt"], int(datetime(2026, 9, 30, 17, tzinfo=timezone.utc).timestamp() * 1000))
        self.assertEqual(seen["tok"]["mint"], "0xabc")

    def test_memecoin_con_el_script_82_real(self):
        try:
            scorer = L.load_memecoin_scorer()
        except ModuleNotFoundError as e:                                       # p. ej. websockets ausente
            self.skipTest(str(e))
        a = {"address": "0xabc", "symbol": "PEPE", "price_usd": 0.01, "liquidity_usd": 5e5, "volume_24h_usd": 2e6,
             "mcap_usd": 3e6, "change_24h": 40.0, "pool_created_at": "2020-01-01T00:00:00Z"}
        score, reasons, conf = L.score_memecoin(a, scorer)
        self.assertIn("Par >24h, no nativo pump.fun", reasons)                 # mismas reglas que Solana

    def test_los_nueve_tipos_devuelven_score_reasons_confidence(self):
        fns = [L.score_blue_chip, L.score_l1_l2, L.score_governance, L.score_depin, L.score_rwa, L.score_synthetic,
               L.score_presale, L.score_established]
        for fn in fns:
            out = fn({})
            self.assertEqual(len(out), 3, fn.__name__)
            self.assertIsInstance(out[1], list)
        self.assertEqual(len(L.score_memecoin({}, lambda t, d: (0, []))), 3)


class ClassifyTest(unittest.TestCase):
    def test_orden_de_reglas(self):
        cases = [({"cg_id": "bitcoin", "categories": ["layer-1"]}, "h"),
                 ({"prelaunch": True, "categories": ["depin"]}, "b"),
                 ({"categories": ["depin", "decentralized-perpetuals"]}, "d"),
                 ({"categories": ["real-world-assets-rwa", "governance"]}, "g"),
                 ({"categories": ["depin", "layer-1"]}, "e"),
                 ({"categories": ["layer-2", "governance"]}, "f"),
                 ({"card": {"tvl": {}}, "categories": []}, "f"),
                 ({"categories": ["governance"]}, "c"),
                 ({"source": "onchain", "pair_age_days": 2}, "a"),
                 ({"source": "onchain", "pair_age_days": 200}, "i"),
                 ({"source": "onchain", "pair_age_days": 30}, "a")]
        for asset, group in cases:
            self.assertEqual(L.classify(asset)[0], group, asset)

    def test_build_assets_y_evaluate(self):
        scan = {"groups": {
            "h": {"items": [{"id": "ethereum", "symbol": "ETH", "change_7d": 1.0, "change_24h": 0.5, "price_usd": 4000,
                             "source": "bitcoin,ethereum,solana"}]},
            "f": {"items": [{"id": "arbitrum", "symbol": "ARB", "source": "layer-2", "change_7d": 5.0},
                            {"id": "cardano", "symbol": "ADA", "source": "layer-1", "change_7d": 2.0}]},
            "c": {"items": [{"id": "arbitrum", "symbol": "ARB", "source": "governance"}]}},
            "onchain": {"solana": {"items": [{"token_address": "So1", "symbol": "X"}]},
                        "eth": {"items": [{"token_address": "0xABC", "symbol": "OLD",
                                           "pool_created_at": "2025-01-01T00:00:00Z", "volume_24h_usd": 1.0,
                                           "reserve_usd": 1e6}]}}}
        cards = {"arbitrum": {"native_token": {"id": "arbitrum", "symbol": "ARB"},
                              "tvl": {"log_growth_7d": 0.02, "accel_7d": 0.0}, "derived": {}}}
        assets = {a["key"]: a for a in L.build_assets(scan, cards, {"categories": {}}, None, NOW)}
        self.assertEqual(set(assets), {"cg:ethereum", "cg:arbitrum", "cg:cardano", "ethereum:0xabc"})  # sin Solana
        self.assertEqual(assets["cg:arbitrum"]["categories"], ["layer-2", "governance"])
        self.assertIs(assets["cg:arbitrum"]["card"], cards["arbitrum"])
        res = {r["key"]: r for r in L.evaluate_all(scan, cards, {"categories": {}}, None,
                                                   memecoin_scorer=lambda t, d: (90, []), now=NOW)}
        self.assertEqual(res["ethereum:0xabc"]["group"], "i")
        self.assertFalse(res["ethereum:0xabc"]["emittable"])                  # i: solo registro
        self.assertIn("Dirección", res["ethereum:0xabc"]["status_reason"])
        self.assertEqual(res["cg:cardano"]["status_reason"], "cobertura 0.25 < 0.6")
        self.assertEqual(res["cg:arbitrum"]["scoring_version"], "mc-f-0.1")
        cov = L.coverage_by_group(res.values())
        self.assertEqual(cov["f"]["assets"], 2)

    def test_umbral_y_registro(self):
        a = {"categories": ["governance"], "mcap_usd": 40e6, "fdv_usd": 40e6, "change_7d": 30.0,
             "category_median_7d": 0.0, "protocol": {"tvl": 160e6, "change_7d": 20.0}}
        r = L.evaluate(a, now=NOW)
        self.assertTrue(r["emittable"])
        self.assertGreaterEqual(r["score"], L.EMIT_THRESHOLD["c"])
        r = L.evaluate(dict(a, change_7d=-30.0, protocol={"tvl": 10e6, "change_7d": -20.0}), now=NOW)
        self.assertFalse(r["emittable"])
        self.assertTrue(r["status_reason"].startswith("score"))
        r = L.evaluate({"categories": ["decentralized-perpetuals"], "change_24h": 90.0}, now=NOW)
        self.assertEqual((r["group"], r["emittable"]), ("d", False))

    def test_memecoin_nunca_usa_modelos_de_volatilidad(self):
        orig = L.garch11
        L.garch11 = lambda *a, **k: (_ for _ in ()).throw(AssertionError("GARCH en memecoin"))
        try:
            r = L.evaluate({"source": "onchain", "pair_age_days": 1, "address": "0x1"},
                           memecoin_scorer=lambda t, d: (70, ["x"]), now=NOW)
            self.assertEqual(r["group"], "a")
        finally:
            L.garch11 = orig


class DossierTest(unittest.TestCase):
    def test_compra_primero_y_tabla_de_componentes(self):
        a = {"categories": ["governance"], "symbol": "GOV", "name": "Gov Token", "mcap_usd": 40e6, "fdv_usd": 40e6,
             "change_7d": 30.0, "category_median_7d": 0.0, "protocol": {"tvl": 160e6, "change_7d": 20.0},
             "price_usd": 1.5, "cg_id": "gov"}
        r = L.evaluate(a, now=NOW)
        md = L.render_dossier(r, ["1. Abrir cuenta en Binance", "2. ..."], "01/10/2026 17:00 UTC", ["CoinGecko"])
        self.assertLess(md.index("🛒 CÓMO ADQUIRIR ESTE ACTIVO"), md.index("📊 Identificación"))
        self.assertIn("| Evento de gobernanza (Snapshot) | n/d | n/d | 20 |", md)
        self.assertIn(f"**Total: {r['score']}**", md)
        self.assertIn("$40,000,000", md)


if __name__ == "__main__":
    unittest.main(verbosity=2)
