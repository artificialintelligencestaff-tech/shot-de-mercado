#!/usr/bin/env python3
"""
test_lib_ohlcv.py — tests para lib_ohlcv.

Uso: python -m unittest 04_Config/scripts/test_lib_ohlcv.py -v
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_ohlcv  # noqa: E402


class LibOhlcv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.cache_dir = Path(cls.temp_dir.name) / "ohlcv_cache"
        cls.cache_dir.mkdir(parents=True)
        # Override cache dir
        lib_ohlcv.CACHE_DIR = cls.cache_dir

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def setUp(self):
        # Clear cache before each test
        for f in self.cache_dir.glob("*.json"):
            f.unlink()

    def test_parse_response(self):
        """Parseo correcto de respuesta OHLCV de GeckoTerminal."""
        mock_response = {
            "data": {
                "attributes": {
                    "ohlcv_list": [
                        [1700000000, 1.0, 1.1, 0.9, 1.05, 1000.0],
                        [1700000060, 1.05, 1.15, 1.0, 1.1, 2000.0],
                    ]
                }
            }
        }
        with patch("lib_ohlcv.requests.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            mock_resp.json.return_value = mock_response
            mock_get.return_value = mock_resp

            candles = lib_ohlcv.get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

        self.assertEqual(len(candles), 2)
        self.assertEqual(candles[0]["ts"], 1700000000)
        self.assertEqual(candles[0]["o"], 1.0)
        self.assertEqual(candles[0]["h"], 1.1)
        self.assertEqual(candles[0]["l"], 0.9)
        self.assertEqual(candles[0]["c"], 1.05)
        self.assertEqual(candles[0]["v"], 1000.0)

    def test_cache_hit(self):
        """Cache hit evita llamada HTTP."""
        # Pre-populate cache
        key = lib_ohlcv._cache_key("solana", "pool123", "minute", 1, 100, None)
        cached_candles = [{"ts": 1700000000, "o": 1.0, "h": 1.1, "l": 0.9, "c": 1.05, "v": 1000.0}]
        lib_ohlcv._save_cache(key, cached_candles)

        with patch("lib_ohlcv.requests.get") as mock_get:
            candles = lib_ohlcv.get_candles("solana", "pool123", "minute", 1, 100)

        self.assertEqual(len(candles), 1)
        self.assertEqual(candles[0]["ts"], 1700000000)
        mock_get.assert_not_called()

    def test_cache_miss(self):
        """Cache miss realiza llamada HTTP."""
        mock_response = {
            "data": {
                "attributes": {
                    "ohlcv_list": [[1700000000, 1.0, 1.1, 0.9, 1.05, 1000.0]]
                }
            }
        }
        with patch("lib_ohlcv.requests.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            mock_resp.json.return_value = mock_response
            mock_get.return_value = mock_resp

            # Use a valid pool address format
            candles = lib_ohlcv.get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

        self.assertEqual(len(candles), 1)
        mock_get.assert_called_once()

    def test_429_retry_success(self):
        """HTTP 429 reintenta y tiene éxito."""
        mock_response = {
            "data": {
                "attributes": {
                    "ohlcv_list": [[1700000000, 1.0, 1.1, 0.9, 1.05, 1000.0]]
                }
            }
        }
        call_count = {"n": 0}

        def side_effect(*args, **kwargs):
            call_count["n"] += 1
            mock_resp = MagicMock()
            if call_count["n"] == 1:
                mock_resp.status_code = 429
            else:
                mock_resp.status_code = 200
                mock_resp.json.return_value = mock_response
            return mock_resp

        with patch("lib_ohlcv.requests.get", side_effect=side_effect) as mock_get:
            with patch("lib_ohlcv.time.sleep"):  # Skip actual sleep
                candles = lib_ohlcv.get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

        self.assertEqual(len(candles), 1)
        self.assertEqual(call_count["n"], 2)

    def test_404_returns_empty(self):
        """HTTP 404 devuelve lista vacía sin romper."""
        with patch("lib_ohlcv.requests.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.status_code = 404
            mock_get.return_value = mock_resp

            candles = lib_ohlcv.get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

        self.assertEqual(candles, [])
        mock_get.assert_called_once()

    def test_500_retry_then_success(self):
        """HTTP 5xx reintenta con backoff y tiene éxito."""
        mock_response = {
            "data": {
                "attributes": {
                    "ohlcv_list": [[1700000000, 1.0, 1.1, 0.9, 1.05, 1000.0]]
                }
            }
        }
        call_count = {"n": 0}

        def side_effect(*args, **kwargs):
            call_count["n"] += 1
            mock_resp = MagicMock()
            if call_count["n"] <= 2:
                mock_resp.status_code = 500
            else:
                mock_resp.status_code = 200
                mock_resp.json.return_value = mock_response
            return mock_resp

        with patch("lib_ohlcv.requests.get", side_effect=side_effect) as mock_get:
            with patch("lib_ohlcv.time.sleep"):
                candles = lib_ohlcv.get_candles("solana", "5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx", "minute", 1, 100)

        self.assertEqual(len(candles), 1)
        self.assertEqual(call_count["n"], 3)

    def test_chain_normalization(self):
        """Normalización de nombres de chain."""
        self.assertEqual(lib_ohlcv._normalize_chain("ethereum"), "eth")
        self.assertEqual(lib_ohlcv._normalize_chain("bnb"), "bsc")
        self.assertEqual(lib_ohlcv._normalize_chain("avax"), "avalanche")
        self.assertEqual(lib_ohlcv._normalize_chain("solana"), "solana")
        self.assertEqual(lib_ohlcv._normalize_chain("base"), "base")


if __name__ == "__main__":
    unittest.main(verbosity=2)