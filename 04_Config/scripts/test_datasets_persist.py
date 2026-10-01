#!/usr/bin/env python3
"""Tests de la Fase 9: MemeChain, Binance histórico, dataset propio y auto-persistencia. unittest, sin red.

Uso: python 04_Config/scripts/test_datasets_persist.py
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import dataset_builder as D  # noqa: E402
import lib_persist as P  # noqa: E402
import lib_scoring_multichain as L  # noqa: E402

CORE = ("token_address,chain,token_name,symbol,deploy_date,website_url,X_url,telegram_url\n"
        "0xAAA,ethereum,Doge Max,DMAX,2024-05-01,https://d.x,https://x.com/d,https://t.me/d\n"
        "0xBBB,ethereum,Kitty Inu,KINU,2024-06-01,,https://x.com/k,\n"
        "So111,solana,AI Agent,AIA,2024-07-01,https://a.x,,https://t.me/a\n"
        "So222,solana,Random,RND,2024-07-02,,,\n"
        "0xCCC,base,Pepe Base,PB,2024-08-01,,,\n")
FIN = ("token_address,chain,price_usd,market_cap\n"
       "0xaaa,ethereum,0.01,5000000\n"       # dirección en minúsculas: se une igual
       "So111,solana,0.2,150000\n"
       "So222,solana,,\n")


class MemeChainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="mc_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        os.environ["SHOT_ROOT"] = str(self.tmp)
        src = self.tmp / "src"
        src.mkdir()
        (src / "core.csv").write_text(CORE, encoding="utf-8")
        (src / "financial.csv").write_text(FIN, encoding="utf-8")
        self.index = D.build_memechain(offline_dir=src, out_dir=self.tmp / "out")

    def test_indice_por_chain_y_narrativa(self):
        idx = self.index
        self.assertEqual(idx["n_tokens"], 5)
        self.assertEqual(idx["columns_detected"]["price"], "price_usd")
        self.assertEqual(idx["all"]["inactive"], 3)                              # sin precio ni mcap: BBB, So222, CCC
        self.assertEqual(idx["by_chain"]["ethereum"]["inactive_rate"], 0.5)
        self.assertEqual(idx["by_chain"]["base"]["inactive_rate"], 1.0)
        self.assertEqual(idx["by_chain"]["ethereum"]["web_rate"], 0.5)
        self.assertEqual(set(idx["by_narrative"]), {"canino", "ia", "otra", "rana_pepe"})   # Kitty Inu -> canino (inu)
        self.assertEqual(idx["by_chain"]["solana"]["mcap_buckets"]["$100K–$1M"], 1)
        self.assertIsNone(idx["by_chain"]["solana"]["one_day"])                  # sin columna de última actividad
        self.assertEqual(idx["license"], "CC-BY-4.0")
        ops = P.read_jsonl(self.tmp / "02_Analisis" / "operations" / "dataset_memechain.jsonl")
        self.assertEqual(ops[-1]["counts"]["tokens"], 5)

    def test_one_day_con_columna_de_actividad(self):
        rows = [{"_chain": "solana", "deploy_date": "2024-07-01T00:00:00", "last_trade_date": "2024-07-01T10:00:00"},
                {"_chain": "solana", "deploy_date": "2024-07-01T00:00:00", "last_trade_date": "2024-07-05T00:00:00"}]
        s = D.summarize(rows)
        self.assertEqual(s["by_chain"]["solana"]["one_day"], {"n_with_dates": 2, "rate": 0.5})

    def test_prior_y_umbral_para_memecoins(self):
        p = L.memechain_prior(self.index, "base", "Pepe Base", "PB")
        self.assertEqual((p["chain"], p["narrative"], p["inactive_rate_chain"]), ("base", "rana_pepe", 1.0))
        self.assertEqual(L.memechain_threshold(p), 63)                          # 56 + 10·(1,0/0,6 − 1) = 62,7
        q = L.memechain_prior(self.index, "ethereum", "x", "x")
        self.assertEqual(L.memechain_threshold(q), round(56 + 10 * (0.5 / 0.6 - 1)))
        self.assertEqual(L.memechain_threshold(L.memechain_prior(self.index, "arbitrum")), 56)   # fuera del dataset
        self.assertIsNone(L.memechain_prior(None, "base"))

    def test_evaluate_usa_el_umbral_de_memechain(self):
        a = {"source": "onchain", "pair_age_days": 1, "address": "0x1", "chain": "base", "name": "Pepe", "symbol": "P"}
        r = L.evaluate(a, memecoin_scorer=lambda t, d: (60, []), memechain=self.index)
        self.assertEqual(r["threshold"], L.memechain_threshold(L.memechain_prior(self.index, "base", "Pepe", "P")))
        self.assertFalse(r["emittable"])                                         # 60 < umbral de Base
        self.assertIn("memechain", r["extra"])


class BinanceTest(unittest.TestCase):
    def test_velas_paginadas_csv_e_indice(self):
        tmp = Path(tempfile.mkdtemp(prefix="bn_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        os.environ["SHOT_ROOT"] = str(tmp)
        day = 86_400_000
        import math
        import random
        rnd = random.Random(1)

        def make(start, n):
            out, p = [], 100.0
            for i in range(n):
                p *= math.exp(rnd.gauss(0, 0.03))
                t = start + i * day
                out.append([t, str(p), str(p * 1.01), str(p * 0.99), str(p), "1", t + day - 1])
            return out
        full = make(1500000000000, 1500)

        class S:
            calls = []

            def get(self, url, params=None, **kw):
                self.calls.append(params)
                start = params["startTime"]
                batch = [k for k in full if k[0] >= start][:1000]

                class R:
                    def raise_for_status(self):
                        pass

                    def json(self):
                        return batch
                return R()
        s = S()
        idx = D.build_binance(session=s, raw_dir=tmp / "raw", out_dir=tmp / "out", sleep=lambda x: None,
                              now_ms=full[-1][6] + 1)
        self.assertEqual(idx["assets"]["BTC"]["rows"], 1500)
        self.assertEqual(len([c for c in s.calls if c["symbol"] == "BTCUSDT"]), 2)   # paginado de a 1000
        self.assertIsNotNone(idx["assets"]["ETH"]["garch11_last_1500"])
        self.assertTrue((tmp / "raw" / "SOLUSDT_1d.csv").read_text().startswith("open_time_ms"))


class PersistTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ps_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        os.environ["SHOT_ROOT"] = str(self.tmp)

    def test_log_operation_y_jsonl(self):
        f = self.tmp / "02_Analisis" / "x.json"
        f.parent.mkdir(parents=True)
        f.write_text("{}")
        P.log_operation("prueba", "test", [f, self.tmp / "no_existe.json"], n=3)
        P.log_operation("prueba", "test", [], n=4)
        rows = P.read_jsonl(self.tmp / "02_Analisis" / "operations" / "prueba.jsonl")
        self.assertEqual([r["counts"]["n"] for r in rows], [3, 4])                # append, no sobrescribe
        self.assertEqual(rows[0]["outputs"][0]["path"], "02_Analisis/x.json")
        self.assertIsNotNone(rows[0]["outputs"][0]["sha256_16"])
        self.assertIsNone(rows[0]["outputs"][1]["sha256_16"])

    def test_dataset_propio_alerta_resultado_y_backfill(self):
        alerts = self.tmp / "02_Analisis" / "alerts" / "_all_alerts.json"
        alerts.parent.mkdir(parents=True)
        (alerts.parent / "alert_M1_2026-10-01_084036.json").write_text(json.dumps(
            {"reasons": ["MCap > $1M"], "scoring_version": "7.2.1"}))
        alerts.write_text(json.dumps([{"timestamp": "2026-10-01_084036", "mint": "M1", "symbol": "arc", "score": 72,
                                       "initial_price": 0.07, "status": "active_tracking"},
                                      {"timestamp": "2026-10-01_090000", "mint": "0xabc", "asset_key": "base:0xabc",
                                       "symbol": "PB", "score": 61, "group": "a", "chain": "base", "multichain": True}]))
        self.assertEqual(D.backfill_historical(alerts), 2)
        self.assertEqual(D.backfill_historical(alerts), 0)                       # no duplica
        P.record_outcome({"mint": "M1", "timestamp": "2026-10-01_084036", "initial_price": 0.07,
                          "trust_updates": [{"stage": "t+1h", "price": 0.071}]}, 0.091)
        rows = P.read_jsonl(P.historical_path())
        self.assertEqual([r["type"] for r in rows], ["alert", "alert", "outcome"])
        self.assertEqual(rows[1]["key"], "base:0xabc")
        self.assertEqual((rows[0]["reasons"], rows[0]["scoring_version"]), (["MCap > $1M"], "7.2.1"))   # del alert_*.json
        self.assertEqual(rows[2]["change_pct"], round((0.091 / 0.07 - 1) * 100, 4))
        self.assertTrue(rows[2]["secondary_hit"])                                # +30% >= +20%


class TrustOutcomeTest(unittest.TestCase):
    def test_script_98_registra_el_resultado_a_48h_una_vez(self):
        tmp = Path(tempfile.mkdtemp(prefix="s98o_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        os.environ["SHOT_ROOT"] = str(tmp)
        spec = importlib.util.spec_from_file_location("s98_out", SCRIPTS / "script_98_trust_scheduler.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        m.send_telegram = lambda msg: True
        m.get_current_price = lambda mint: 1.3
        f = tmp / "02_Analisis" / "alerts" / "_all_alerts.json"
        f.parent.mkdir(parents=True)
        ts = (datetime.utcnow() - timedelta(hours=49)).strftime("%Y-%m-%d_%H%M%S")
        f.write_text(json.dumps([{"timestamp": ts, "mint": "M1", "symbol": "X", "score": 70, "confidence": 60,
                                  "initial_price": 1.0, "status": "active_tracking", "trust_updates": []}]))
        m.main()
        m.main()
        out = [r for r in P.read_jsonl(tmp / "02_Analisis" / "datasets" / "historical_alerts.jsonl") if r["type"] == "outcome"]
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["change_pct"], 30.0)
        self.assertTrue(json.loads(f.read_text())[0]["outcome_48h_logged"])
        ops = P.read_jsonl(tmp / "02_Analisis" / "operations" / "trust_cycle.jsonl")
        self.assertEqual(len(ops), 2)
        late = (datetime.utcnow() - timedelta(hours=60)).strftime("%Y-%m-%d_%H%M%S")
        f.write_text(json.dumps([{"timestamp": late, "mint": "M2", "symbol": "Y", "score": 70, "confidence": 60,
                                  "initial_price": 1.0, "status": "active_tracking", "trust_updates": []}]))
        m.main()
        out = [r for r in P.read_jsonl(tmp / "02_Analisis" / "datasets" / "historical_alerts.jsonl") if r["type"] == "outcome"]
        self.assertEqual(len(out), 1)                                            # 60 h: fuera de la ventana, no se registra


if __name__ == "__main__":
    unittest.main(verbosity=2)
