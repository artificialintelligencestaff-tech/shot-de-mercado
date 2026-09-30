#!/usr/bin/env python3
"""Tests de monitor_shadow (unittest, sin red: fuente de velas simulada).

Uso: python 04_Config/scripts/test_monitor_shadow.py
"""
import importlib.util
import json
import os
import shutil
import tempfile
import time
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent


class FakeSource:
    def __init__(self, candles_by_pool):
        self.candles = candles_by_pool

    def get(self, pool, t0):
        return ("ok", self.candles.get(pool, [])) if pool in self.candles else ("http_429", [])

    def save(self):
        pass


class MonitorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="mon_")
        os.environ["SHOT_ROOT"] = self.tmp
        spec = importlib.util.spec_from_file_location("monitor_under_test", HERE / "monitor_shadow.py")
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.alerts_dir = Path(self.tmp) / "02_Analisis" / "alerts"
        self.alerts_dir.mkdir(parents=True)
        self.now = datetime.now(timezone.utc)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("SHOT_ROOT", None)

    def add(self, mint, version, det_min_ago, age_min, pool, status="shadow", sent=False):
        ts = self.now.strftime("%Y-%m-%d_%H%M%S")
        det = self.now - timedelta(minutes=det_min_ago)
        alert = {"timestamp": ts, "mint": mint, "symbol": mint[:4], "score": 70, "initial_price": 1.0,
                 "status": status, "telegram_sent": sent, "trust_updates": []}
        snap = {"score": 70, "dexscreener": {"pairAddress": pool, "priceUsd": 1.0,
                                             "pairCreatedAt": int((det.timestamp() - age_min * 60) * 1000)}}
        if version:
            snap.update(scoring_version=version, detected_at=det.isoformat(timespec="seconds"))
        (self.alerts_dir / f"alert_{mint}_{ts}.json").write_text(json.dumps(snap), encoding="utf-8")
        return alert

    def write_alerts(self, alerts):
        (self.alerts_dir / "_all_alerts.json").write_text(json.dumps(alerts), encoding="utf-8")

    def test_collect_filtra_shadow_version_edad_y_frescura(self):
        self.write_alerts([self.add("A" * 40, "7.2.1", 5, 3, "p1"), self.add("B" * 40, "7.2.1", 10, 120, "p2"),
                           self.add("C" * 40, None, 0, 10, "p3"),
                           self.add("D" * 40, "7.2.1", 5, 3, "p4", status="active_tracking")])
        rows = self.m.collect("7.2.1")
        self.assertEqual([r["mint"][0] for r in rows], ["A", "B"])
        self.assertAlmostEqual(rows[0]["age_min_at_detection"], 3, delta=0.2)
        self.assertAlmostEqual(rows[0]["staleness_min"], 5, delta=0.2)
        self.assertEqual({r["version"] for r in self.m.collect()}, {"7.2.1", "7.2-preR1"})

    def test_medicion_y_resumen(self):
        self.write_alerts([self.add("A" * 40, "7.2.1", 5, 3, "hit"), self.add("B" * 40, "7.2.1", 5, 120, "miss"),
                           self.add("C" * 40, "7.2.1", 5, 120, "sin_api")])
        t = time.time()
        src = FakeSource({"hit": [[t - 100, 1.0, 1.3, 0.95, 1.2, 1.0]], "miss": [[t - 100, 1.0, 1.05, 0.5, 0.6, 1.0]]})
        rows = self.m.measure(self.m.collect("7.2.1"), src)
        s = self.m.summarize(rows)
        self.assertEqual((s["primary"]["k_hit"], s["primary"]["n_resolved"]), (1, 2))
        self.assertEqual(s["secondary"]["pending"], 2)                  # 48 h no cumplidas
        self.assertEqual(s["status_counts"]["http_429"], 1)
        self.assertEqual(s["young_lt_60m"], {"k": 1, "n_known_age": 3, "share": round(1 / 3, 4)})
        self.assertEqual(s["verdict_partial"], {"exposure_young": False})   # n < 20: sin veredicto de precisión
        self.assertIn("DÍA 1", self.m.block("7.2.1", s))

    def test_veredicto_con_n_suficiente(self):
        rows = [{"primary": "hit" if i < 9 else "miss", "secondary": "pending", "status": "ok",
                 "age_min_at_detection": 120, "staleness_min": 5, "alert_ts": "2026-09-30_050000",
                 "telegram_sent": False} for i in range(20)]
        s = self.m.summarize(rows)
        self.assertTrue(s["verdict_partial"]["primary"])                 # 45% con IC90 inferior > 15%
        self.assertTrue(s["verdict_partial"]["exposure_young"])
        self.assertNotIn("secondary", s["verdict_partial"])              # secundaria sin n resuelto


if __name__ == "__main__":
    unittest.main(verbosity=2)
