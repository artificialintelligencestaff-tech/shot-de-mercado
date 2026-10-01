#!/usr/bin/env python3
"""latency_analysis (Fase 10, T1). unittest, sin red: velas y API de Actions simuladas.

Uso: python 04_Config/scripts/test_latency_analysis.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import latency_analysis as la  # noqa: E402

EMIT = datetime(2026, 10, 1, 17, 14, 1, tzinfo=timezone.utc).timestamp()
CREATED = EMIT - 41.8 * 60


class Resp:
    def __init__(self, data, status=200):
        self.status_code, self._data = status, data

    def json(self):
        return self._data


def candles_from(prices, t0, step=60):
    return [(t0 + i * step, p, p) for i, p in enumerate(prices)]


class Pump(unittest.TestCase):
    def test_primer_minuto_con_5pct_en_5min(self):
        prices = [1.0] * 10 + [1.01, 1.02, 1.03, 1.04, 1.06, 1.2]
        hit = la.pump_start(candles_from(prices, 0))
        self.assertEqual(hit[0], 14 * 60)            # 1.06 vs 1.0 de 5 min antes
        self.assertFalse(hit[2])

    def test_pump_desde_el_lanzamiento(self):
        c = [(0, 0.5, 0.9), (60, 0.9, 1.0)]          # la primera vela ya sube 80 % sobre su apertura
        hit = la.pump_start(c)
        self.assertEqual((hit[0], hit[2]), (0, True))

    def test_huecos_y_sin_pump(self):
        c = [(0, 1, 1.0), (600, 1, 1.03), (1200, 1, 1.04)]
        self.assertIsNone(la.pump_start(c))
        self.assertIsNone(la.pump_start([]))

    def test_gap_y_resumen(self):
        row = {"symbol": "X", "pair_created_at": la.iso(EMIT - 3600)}
        prices = [1.0] * 30 + [1.1] * 30                                  # pump en el minuto 30
        m = la.measured_row(row, candles_from(prices, EMIT - 3600), EMIT)
        self.assertEqual(m["gap_min"], 30.0)
        self.assertAlmostEqual(m["move_since_pump_start_at_emit"], 0.0)
        s = la.summarize_gaps([m, {"gap_min": 3.0}, {"gap_min": -2.0}, {"gap_min": None}])
        self.assertEqual((s["n_measured"], s["within_5min_pct"], s["anticipated_pct"]), (3, 33.3, 33.3))


class Estructura(unittest.TestCase):
    def test_fila_estructural_y_cota_del_gap(self):
        alert = {"timestamp": "2026-10-01_171401", "mint": "M1", "symbol": "1M X", "status": "active_tracking"}
        detail = {"detected_at": la.iso(EMIT - 37.1 * 60),
                  "dexscreener": {"pairCreatedAt": int(CREATED * 1000), "priceChange_m5": 7243.0,
                                  "priceChange_h1": 7243.0, "pairAddress": "POOL"}}
        r = la.structural_row(alert, detail)
        self.assertEqual((r["detect_to_emit_min"], r["pair_age_at_emit_min"]), (37.1, 41.8))
        self.assertEqual(r["gap_bounds_min"], [37.1, 41.8])
        self.assertEqual(la.summarize_structural([r])["already_moved_100pct_at_snapshot"], ["1M X"])

    def test_cron_drift_y_piso(self):
        runs = [{"run_started_at": "2026-10-01T19:06:50Z", "updated_at": "2026-10-01T19:12:51Z"},
                {"run_started_at": "2026-10-01T18:53:29Z", "updated_at": "2026-10-01T18:59:15Z"},
                {"event": "workflow_dispatch", "run_started_at": "2026-10-01T18:01:00Z"}]
        c = la.cron_drift(runs)
        self.assertEqual(c["n"], 2)
        self.assertAlmostEqual(c["start_delay_mean_min"], round((6 + 50 / 60 + 13 + 29 / 60) / 2, 1))
        self.assertEqual(la.structural_floor(c)["expected_first_emit_age_min"], 40.0)


class Corrida(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lat_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        a = self.tmp / "02_Analisis" / "alerts"
        a.mkdir(parents=True)
        alerts = [{"timestamp": "2026-10-01_171401", "mint": "M1", "symbol": "1M X", "status": "active_tracking"},
                  {"timestamp": "2026-10-01_185902", "mint": "cg:bitcoin", "symbol": "BTC",
                   "status": "active_tracking_cex", "multichain": True, "group": "h"},
                  {"timestamp": "2026-10-01_100000", "mint": "M0", "symbol": "NOPE", "status": "DESCARTAR_NOPAR"}]
        (a / "_all_alerts.json").write_text(json.dumps(alerts), encoding="utf-8")
        (a / "alert_M1_2026-10-01_171401.json").write_text(json.dumps(
            {"detected_at": la.iso(EMIT - 37.1 * 60),
             "dexscreener": {"pairCreatedAt": int(CREATED * 1000), "pairAddress": "POOL", "priceChange_h1": 50}}))
        self.urls = []

    def fake_get(self, url, headers=None, timeout=None):
        self.urls.append(url)
        if "geckoterminal" in url:
            rows = [[int(CREATED) + i * 60, 1.0, 1, 1, 1.0 if i < 3 else 2.0, 10] for i in range(60)]
            return Resp({"data": {"attributes": {"ohlcv_list": list(reversed(rows))}}})
        if "binance" in url:
            return Resp([])
        return Resp({"workflow_runs": []})

    def test_offline_y_medida(self):
        off = la.run(self.tmp, 20, None, [])
        self.assertEqual(len(off["alerts"]), 2)                 # la descartada no cuenta
        self.assertIsNone(off["summary"]["measured"])
        on = la.run(self.tmp, 20, self.fake_get, [], sleep=lambda s: None)
        row = on["alerts"][0]
        self.assertEqual(row["pump_start_at"], la.iso(CREATED + 3 * 60))
        self.assertEqual(row["gap_min"], round(41.8 - 3, 1))
        self.assertFalse(on["alerts"][1]["measured"])            # sin velas de Binance
        self.assertIn("pools/POOL/ohlcv/minute", self.urls[0])
        self.assertEqual(on["summary"]["measured"]["n_measured"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
