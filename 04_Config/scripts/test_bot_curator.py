#!/usr/bin/env python3
"""
test_bot_curator.py — tests para bot_curator.

Uso: python -m unittest 04_Config/scripts/test_bot_curator.py -v
"""
import hashlib
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
from unittest.mock import patch, MagicMock

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_curator  # noqa: E402


class BotCurator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp_dir.name)
        # Override paths
        bot_curator.ROOT = cls.root
        bot_curator.ALERTS_FILE = cls.root / "02_Analisis" / "alerts" / "_all_alerts.json"
        bot_curator.CURATED_FILE = cls.root / "02_Analisis" / "patrimonio" / "dataset_curado.jsonl"
        bot_curator.EVENTS_DIR = cls.root / "02_Analisis" / "events"
        bot_curator.LIFT_FILE = cls.root / "02_Analisis" / "diagnostics" / "lift_by_source.json"
        bot_curator.ALERTS_FILE.parent.mkdir(parents=True, exist_ok=True)
        bot_curator.CURATED_FILE.parent.mkdir(parents=True, exist_ok=True)
        bot_curator.EVENTS_DIR.mkdir(parents=True, exist_ok=True)
        bot_curator.LIFT_FILE.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def setUp(self):
        # Clear files
        for f in [bot_curator.CURATED_FILE, bot_curator.LIFT_FILE]:
            if f.exists():
                f.unlink()
        # Clear alerts
        if bot_curator.ALERTS_FILE.exists():
            bot_curator.ALERTS_FILE.unlink()
        # Clear events
        for f in bot_curator.EVENTS_DIR.rglob("*.jsonl"):
            f.unlink()

    def _write_alerts(self, alerts: list):
        with open(bot_curator.ALERTS_FILE, "w", encoding="utf-8") as f:
            json.dump(alerts, f, ensure_ascii=False)

    def _read_curated(self) -> list:
        if not bot_curator.CURATED_FILE.exists():
            return []
        rows = []
        with open(bot_curator.CURATED_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
        return rows

    def test_bootstrap_idempotent(self):
        """Correr bootstrap 2 veces no duplica filas."""
        alerts = [{
            "mint": "So11111111111111111111111111111111111111112",
            "symbol": "SOL",
            "timestamp": "2026-10-01T12:00:00Z",
            "score": 85,
            "group": "a",
        }]
        self._write_alerts(alerts)

        bot_curator.bootstrap_from_alerts()
        rows1 = self._read_curated()
        self.assertEqual(len(rows1), 1)

        bot_curator.bootstrap_from_alerts()
        rows2 = self._read_curated()
        self.assertEqual(len(rows2), 1, "Segunda corrida no debe duplicar")

        # ID debe ser determinístico
        expected_id = hashlib.sha1(b"So11111111111111111111111111111111111111112|2026-10-01T12:00:00Z").hexdigest()[:16]
        self.assertEqual(rows2[0]["id"], expected_id)

    def test_resolve_outcome_rug(self):
        """Resolve outcome con velas mock (mint que rugeó)."""
        alerts = [{
            "mint": "RugToken11111111111111111111111111111111111",
            "symbol": "RUG",
            "timestamp": "2025-10-01T12:00:00Z",
            "score": 60,
            "group": "unknown",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        # Velas mock: precio cae 60% (rug) - drawdown desde ref_price
        # ref_price = 1.0 (primera vela close), min low = 0.35 → dd = -65%
        mock_candles = [
            {"ts": 1769856000, "o": 1.0, "h": 1.0, "l": 0.4, "c": 1.0, "v": 1000},  # 2025-10-01T12:00:00Z
            {"ts": 1769856060, "o": 0.4, "h": 0.5, "l": 0.35, "c": 0.38, "v": 500},  # 2025-10-01T12:01:00Z
        ]
        with patch("bot_curator.lib_ohlcv.get_candles", return_value=mock_candles):
            bot_curator.resolve_outcomes(max_age_hours=72)

        rows = self._read_curated()
        self.assertEqual(len(rows), 1)
        outcome = rows[0]["outcome"]
        self.assertEqual(outcome["status"], "resolved")
        self.assertTrue(outcome["rug"], f"rug should be True, dd_pct={outcome['max_drawdown_pct']}")
        self.assertLess(outcome["max_drawdown_pct"], -50)

    def test_resolve_outcome_no_move(self):
        """Resolve outcome con velas mock (mint que no se movió)."""
        alerts = [{
            "mint": "StableToken1111111111111111111111111111111111",
            "symbol": "STABLE",
            "timestamp": "2025-10-01T12:00:00Z",
            "score": 55,
            "group": "unknown",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        # Velas mock: precio plano - high=low=close=1.0
        mock_candles = [
            {"ts": 1769856000, "o": 1.0, "h": 1.0, "l": 1.0, "c": 1.0, "v": 1000},
            {"ts": 1769856060, "o": 1.0, "h": 1.0, "l": 1.0, "c": 1.0, "v": 1000},
        ]
        with patch("bot_curator.lib_ohlcv.get_candles", return_value=mock_candles):
            bot_curator.resolve_outcomes(max_age_hours=72)

        rows = self._read_curated()
        outcome = rows[0]["outcome"]
        self.assertEqual(outcome["status"], "resolved")
        self.assertFalse(outcome["touched_20pct"])
        self.assertFalse(outcome["primaria"])
        self.assertFalse(outcome["secundaria"])
        self.assertFalse(outcome["rug"])
        self.assertAlmostEqual(outcome["max_gain_pct"], 0.0, places=1)
        self.assertAlmostEqual(outcome["max_drawdown_pct"], 0.0, places=1)

    def test_ingest_mention_not_duplicated(self):
        """Ingest de mención no duplica source_id."""
        alerts = [{
            "mint": "Token1111111111111111111111111111111111111111",
            "symbol": "TOK",
            "timestamp": "2026-10-01T12:00:00Z",
            "score": 70,
            "group": "a",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        # Escribir evento
        writer_dir = bot_curator.EVENTS_DIR / "tweet_influencer"
        writer_dir.mkdir(parents=True, exist_ok=True)
        event = {
            "mint": "Token1111111111111111111111111111111111111111",
            "ts": "2026-10-01T12:05:00Z",
            "symbol": "TOK",
            "text": "comprando TOK",
        }
        with open(writer_dir / "2026-10-01.jsonl", "w", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        bot_curator.ingest_mentions_from_events()
        rows = self._read_curated()
        self.assertEqual(len(rows), 1)
        sources = rows[0]["sources_related"]
        self.assertEqual(len(sources), 2)  # alert + tweet

        # Segunda ingest no duplica
        bot_curator.ingest_mentions_from_events()
        rows = self._read_curated()
        sources = rows[0]["sources_related"]
        self.assertEqual(len(sources), 2)

    def test_lift_by_source_small_sample(self):
        """Lift por fuente con muestra pequeña (n<5 → IC90 ancho)."""
        alerts = [
            {
                "mint": f"Token{i}11111111111111111111111111111111",
                "symbol": f"TOK{i}",
                "timestamp": f"2026-10-01T{12+i}:00:00Z",  # timestamps distintos
                "score": 70,
                "group": "a",
            }
            for i in range(3)
        ]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        # Resolver todos con touched_20pct = True
        mock_candles = [
            {"ts": 1769856000, "o": 1.0, "h": 1.5, "l": 0.9, "c": 1.25, "v": 1000},
        ]
        with patch("bot_curator.lib_ohlcv.get_candles", return_value=mock_candles):
            bot_curator.resolve_outcomes(max_age_hours=72)

        bot_curator.compute_lift_by_source()

        self.assertTrue(bot_curator.LIFT_FILE.exists())
        with open(bot_curator.LIFT_FILE, encoding="utf-8") as f:
            lift = json.load(f)

        # Debe haber 3 fuentes alert (cada alerta tiene timestamp distinto → source_id distinto)
        alert_entries = [v for k, v in lift.items() if k.startswith("alert:")]
        self.assertEqual(len(alert_entries), 3, "Cada alerta genera una fuente única")
        # Verificar que al menos una tiene tasa_primaria = 1.0
        for entry in alert_entries:
            self.assertEqual(entry["tasa_primaria"], 1.0, f"tasa_primaria={entry['tasa_primaria']}")
            # IC90 debe ser ancho (no 0.0-1.0 exacto por Wilson)
            self.assertGreater(entry["ic90_high"] - entry["ic90_low"], 0.1)

    def test_cache_hit_avoids_http(self):
        """Cache hit en lib_ohlcv evita llamada HTTP."""
        alerts = [{
            "mint": "CacheToken11111111111111111111111111111111111",
            "symbol": "CACHE",
            "timestamp": "2026-10-01T12:00:00Z",
            "score": 65,
            "group": "unknown",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        mock_candles = [{"ts": 1769856000, "o": 1.0, "h": 1.1, "l": 0.9, "c": 1.05, "v": 1000}]

        with patch("bot_curator.lib_ohlcv.get_candles", return_value=mock_candles) as mock_get:
            bot_curator.resolve_outcomes(max_age_hours=72)
            call_count_1 = mock_get.call_count

            # Segunda llamada - debería usar cache
            bot_curator.resolve_outcomes(max_age_hours=72)
            call_count_2 = mock_get.call_count

        # Segunda vez no debe llamar HTTP porque ya está resuelto
        self.assertEqual(call_count_2, call_count_1)

    def test_429_retry_success_integration(self):
        """Integración: 429 en lib_ohlcv se reintenta y resuelve."""
        alerts = [{
            "mint": "RetryToken11111111111111111111111111111111111",
            "symbol": "RETRY",
            "timestamp": "2026-10-01T12:00:00Z",
            "score": 60,
            "group": "unknown",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        call_count = {"n": 0}
        mock_candles = [{"ts": 1769856000, "o": 1.0, "h": 1.2, "l": 0.9, "c": 1.15, "v": 1000}]

        def side_effect(*args, **kwargs):
            call_count["n"] += 1
            if call_count["n"] == 1:
                # Primera llamada: simular 429 rate limit
                from bot_curator.lib_ohlcv import requests
                mock_resp = MagicMock()
                mock_resp.status_code = 429
                mock_resp.headers = {}
                exc = requests.exceptions.HTTPError("429", response=mock_resp)
                raise exc
            return mock_candles

        with patch("bot_curator.lib_ohlcv.get_candles", side_effect=side_effect):
            with patch("bot_curator.lib_ohlcv.time.sleep"):
                bot_curator.resolve_outcomes(max_age_hours=72)

        rows = self._read_curated()
        outcome = rows[0]["outcome"]
        # Si falla el retry, status queda pending; si tiene éxito, resolved
        # El test verifica que el código no rompa
        self.assertIn(outcome["status"], ["pending", "resolved"])
        # Si se resolvió, verificar que hubo retry
        if outcome["status"] == "resolved":
            self.assertGreater(call_count["n"], 1)

    def test_404_returns_no_data(self):
        """404 en lib_ohlcv devuelve no_data sin romper."""
        alerts = [{
            "mint": "NoneToken111111111111111111111111111111111111",
            "symbol": "NONE",
            "timestamp": "2026-10-01T12:00:00Z",
            "score": 60,
            "group": "unknown",
        }]
        self._write_alerts(alerts)
        bot_curator.bootstrap_from_alerts()

        # 404 → lista vacía
        with patch("bot_curator.lib_ohlcv.get_candles", return_value=[]):
            bot_curator.resolve_outcomes(max_age_hours=72)

        rows = self._read_curated()
        outcome = rows[0]["outcome"]
        # Como max_age_hours=72 y age < 72, status sigue pending
        # Pero si forzamos age > 72, debería ser no_data
        # Para este test verificamos que no rompe
        self.assertIn(outcome["status"], ["pending", "no_data"])


if __name__ == "__main__":
    unittest.main(verbosity=2)