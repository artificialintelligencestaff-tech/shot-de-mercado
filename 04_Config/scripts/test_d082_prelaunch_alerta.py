#!/usr/bin/env python3
"""Test de D-082 T2: script_97 suma la línea de PRE-LANZAMIENTO cuando el calendario de preventa siguió al token
antes de nacer, y degrada al mensaje normal si el calendario no existe o está roto. unittest, sin red ni Telegram.

Uso: python 04_Config/scripts/test_d082_prelaunch_alerta.py
"""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"
MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
NOW = datetime(2026, 10, 3, 4, 0, tzinfo=timezone.utc)


def candidate():
    return {"source": "pumpportal", "token": {"mint": MINT, "symbol": "KIT", "name": "Kitty Coin"},
            "dexscreener": {"priceUsd": 0.03, "liquidityUsd": 141632.8, "volume24hUsd": 201003.7,
                            "marketCapUsd": 9844684.6, "dexId": "pumpswap", "pairAddress": "PoolX",
                            "pairCreatedAt": int((NOW - timedelta(minutes=45)).timestamp() * 1000)},
            "score": 72, "reasons": ["MCap > $1M"], "detected_at": NOW.isoformat(timespec="seconds"),
            "scoring_version": "7.2.1"}


class AlertaPrelaunch(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="s97pre_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        with mock.patch.dict(os.environ, {"SHOT_ROOT": str(self.tmp)}):
            spec = importlib.util.spec_from_file_location("s97_prelaunch_test", SCRIPT)
            self.m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.m)

    def calendar(self, asset):
        p = self.tmp / "02_Analisis" / "prelaunch" / "_calendar.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"assets": {asset["key"]: asset}}) if isinstance(asset, dict) else asset,
                     encoding="utf-8")

    def test_linea_prelanzamiento_y_degradacion(self):
        normal, _ = self.m.format_alert_message(candidate())               # sin calendario: mensaje de siempre
        self.assertNotIn("PRE-LANZAMIENTO", normal)
        asset = {"key": "sym:KIT", "symbol": "KIT", "state": "seguimiento", "prelaunch_known": True,
                 "contract": MINT, "sources": {"hyperliquid": {}, "bybit": {}},
                 "born": {"contract": MINT, "match": "contrato", "alertable": True, "precio_preventa": 0.02,
                          "precio_apertura": 0.03, "delta_preventa_apertura_pct": 50.0}}
        self.calendar(asset)
        msg, _ = self.m.format_alert_message(candidate())
        self.assertIn("🆕 *PRE-LANZAMIENTO*: precio preventa $0.02, delta vs apertura +50.0%", msg)
        self.assertEqual(msg.replace("🆕 *PRE-LANZAMIENTO*: precio preventa $0.02, delta vs apertura +50.0%\n", ""),
                         normal)                                           # solo agrega la línea
        asset["born"].update(alertable=False, match="simbolo", precio_preventa=None, delta_preventa_apertura_pct=None)
        asset.pop("precio_preventa", None)
        self.calendar(asset)
        self.assertIn("🆕 *PRE-LANZAMIENTO* (candidato por símbolo): seguido desde el anuncio (bybit, hyperliquid)",
                      self.m.format_alert_message(candidate())[0])
        other = dict(asset, contract="So1otro11111111111111111111111111111111111", born={"contract": "So1otro11111111111111111111111111111111111"})
        self.calendar(other)
        self.assertEqual(self.m.format_alert_message(candidate())[0], normal)   # otro contrato: nada (nunca por símbolo)
        self.calendar("{roto")
        self.assertEqual(self.m.format_alert_message(candidate())[0], normal)   # calendario corrupto: degrada


if __name__ == "__main__":
    unittest.main(verbosity=2)
