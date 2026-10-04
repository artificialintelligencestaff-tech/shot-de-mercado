#!/usr/bin/env python3
"""Tests de D-082 T1: token_nacido desde producción (script_116 early watch y script_114 multichain scanner) para el
calendario de preventa. unittest, sin red.

Uso: python 04_Config/scripts/test_d082_token_nacido.py
"""
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_events as events  # noqa: E402
import script_114_multichain_scanner as s114  # noqa: E402
import script_116_early_watch as s116  # noqa: E402

T0 = 1791000000
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
MINT2 = "7cnqaJLZaSD1s2PchXuYjauGSk6c8Nuj9Zcd1V5aMdKU"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="d082_"))
        self.addCleanup(shutil.rmtree, self.root, True)


class TokenNacido(Base):
    def test_early_watch_emite_solo_jovenes_de_30_min_con_liquidez(self):
        results = [{"mint": MINT, "scorer": "young", "age_min": 12.0},
                   {"mint": "So1viejo111111111111111111111111111111111111", "scorer": "young", "age_min": 45.0},
                   {"mint": "So1sinliq11111111111111111111111111111111111", "scorer": "young", "age_min": 5.0},
                   {"mint": MINT2, "scorer": "v7.2.1+early", "age_min": 8.0}]
        watch = {MINT: {"token": {"symbol": "KIT", "name": "Kitty Coin"}}}
        dexs = {MINT: {"priceUsd": 0.031, "liquidityUsd": 12000.0, "pairAddress": "PoolX"},
                "So1viejo111111111111111111111111111111111111": {"liquidityUsd": 9000.0},
                "So1sinliq11111111111111111111111111111111111": {"liquidityUsd": 0.0},
                MINT2: {"liquidityUsd": 50000.0}}
        seen = set()
        self.assertEqual(s116.emit_births(results, watch, dexs, self.root, T0, "b", seen), 1)
        (ev,) = events.read_events(types="token_nacido", now=T0 + 60, root=self.root)
        self.assertEqual((ev["subject"], ev["writer"], ev["data"]["symbol"], ev["data"]["chain"], ev["data"]["price_usd"]),
                         (MINT, "early_watch_b", "KIT", "solana", 0.031))
        self.assertEqual(s116.emit_births(results, watch, dexs, self.root, T0 + 120, "b", seen), 0)   # mismo loop
        self.assertEqual(s116.emit_births(results, watch, dexs, self.root, T0 + 180, "a", set()), 0)  # otra instancia: dedup
        with mock.patch.object(s116.ev, "write_events", side_effect=OSError("disco lleno")):
            self.assertEqual(s116.emit_births(results, watch, dexs, self.root, T0, "a", set()), 0)  # nunca lanza

    def test_scanner_emite_pools_nuevos_de_menos_de_24_h(self):
        now = datetime.fromtimestamp(T0, timezone.utc)
        iso = lambda h: (now - timedelta(hours=h)).isoformat().replace("+00:00", "Z")  # noqa: E731
        report = {"onchain": {
            "solana": {"items": [{"id": "P1", "symbol": "NEWT", "name": "NEWT / SOL", "chain": "solana",
                                  "token_address": MINT2, "price_usd": 0.65, "pool_created_at": iso(2)},
                                 {"id": "P2", "symbol": "OLD", "chain": "solana", "token_address": MINT,
                                  "price_usd": 1.0, "pool_created_at": iso(72)}]},
            "base": {"items": [{"id": "P3", "symbol": "SIN", "chain": "base", "token_address": None,
                                "pool_created_at": iso(1)}, {"id": "P4", "pool_created_at": "no es fecha"}]}}}
        self.assertEqual(s114.emit_births(report, now=T0, root=self.root), 1)
        (ev,) = events.read_events(types="token_nacido", now=T0 + 60, root=self.root)
        self.assertEqual((ev["subject"], ev["writer"], ev["data"]["symbol"], ev["data"]["chain"], ev["data"]["price_usd"]),
                         (MINT2, "multichain_scanner", "NEWT", "solana", 0.65))
        self.assertEqual(s114.emit_births(report, now=T0 + 600, root=self.root), 0)                 # dedup


if __name__ == "__main__":
    unittest.main(verbosity=2)
