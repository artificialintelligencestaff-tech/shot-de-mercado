#!/usr/bin/env python3
"""Tests de script_98: el trust loop solo procesa alertas en active_tracking (unittest, sin red).

Uso: python 04_Config/scripts/test_script_98_shadow.py
"""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "script_98_trust_scheduler.py"


def alert(mint, status, hours_ago=2.0, initial=1.0):
    ts = (datetime.utcnow() - timedelta(hours=hours_ago)).strftime("%Y-%m-%d_%H%M%S")
    return {"timestamp": ts, "mint": mint, "symbol": mint.upper(), "score": 70, "confidence": 60,
            "initial_price": initial, "status": status, "trust_updates": []}


class TestTrustLoopShadow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="s98_")
        os.environ["SHOT_ROOT"] = self.tmp
        spec = importlib.util.spec_from_file_location("script_98_under_test", SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.alerts_file = Path(self.tmp) / "02_Analisis" / "alerts" / "_all_alerts.json"
        self.alerts_file.parent.mkdir(parents=True, exist_ok=True)
        self.sent, self.priced = [], []
        self.m.send_telegram = lambda msg: self.sent.append(msg) or True
        self.m.get_current_price = lambda mint: self.priced.append(mint) or 1.5   # +50% -> ACIERTO, notifica

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("SHOT_ROOT", None)

    def test_shadow_se_ignora_y_no_notifica(self):
        self.alerts_file.write_text(json.dumps([alert("activo", "active_tracking"), alert("sombra", "shadow")]),
                                    encoding="utf-8")
        self.m.main()
        data = {a["mint"]: a for a in json.loads(self.alerts_file.read_text(encoding="utf-8"))}
        self.assertEqual(len(data["activo"]["trust_updates"]), 1)
        self.assertEqual(data["sombra"]["trust_updates"], [])
        self.assertEqual(self.priced, ["activo"])          # ni siquiera consulta precio de la sombra
        self.assertEqual(len(self.sent), 1)
        self.assertIn("ACTIVO", self.sent[0])

    def test_otros_estados_tampoco_se_procesan(self):
        self.alerts_file.write_text(json.dumps([alert("cerrada", "DESCARTAR_NOPAR")]), encoding="utf-8")
        self.m.main()
        self.assertEqual(self.priced, [])
        self.assertEqual(self.sent, [])

    def test_alerta_sin_status_se_trata_como_activa(self):
        legacy = alert("legado", "active_tracking")
        del legacy["status"]
        self.alerts_file.write_text(json.dumps([legacy]), encoding="utf-8")
        self.m.main()
        self.assertEqual(self.priced, ["legado"])


    def test_cex_se_sigue_con_precio_de_exchange(self):
        self.m.get_cex_price = lambda sym: (self.priced.append(f"cex:{sym}") or 1.2, "binance")
        btc = alert("cg:bitcoin", "active_tracking_cex")
        btc["symbol"] = "BTC"
        self.alerts_file.write_text(json.dumps([btc, alert("activo", "active_tracking")]), encoding="utf-8")
        self.m.main()
        data = {a["mint"]: a for a in json.loads(self.alerts_file.read_text(encoding="utf-8"))}
        self.assertEqual(self.priced, ["cex:BTC", "activo"])                  # DexScreener solo para la on-chain
        self.assertEqual(len(data["cg:bitcoin"]["trust_updates"]), 1)

    def test_get_cex_price_orden_y_parseo(self):
        calls = []

        class R:
            def __init__(self, code, data):
                self.status_code, self._d = code, data

            def json(self):
                return self._d
        answers = {"binance": R(451, {}), "coinbase": R(404, {}),
                   "kraken": R(200, {"error": [], "result": {"XXBTZUSD": {"c": ["77000.1", "1"]}}})}
        fake = lambda url, timeout=None: calls.append(url) or answers[                     # noqa: E731
            "binance" if "binance" in url else "coinbase" if "coinbase" in url else "kraken"]
        with mock.patch.object(self.m.requests, "get", fake):
            self.assertEqual(self.m.get_cex_price("btc"), (77000.1, "kraken"))
            self.assertIn("pair=XBTUSD", calls[-1])
            self.assertEqual(self.m.get_cex_price("BAD$"), (None, None))

if __name__ == "__main__":
    unittest.main(verbosity=2)
