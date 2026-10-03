#!/usr/bin/env python3
"""Tests de lib_normalize (normalización semántica, patrón #19). unittest, sin red.

Uso: python 04_Config/scripts/test_lib_normalize.py
"""
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("lib_normalize_test", SCRIPTS / "lib_normalize.py")
norm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(norm)

MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
EVM = "0x532f27101965dd16442E59d40670FaF5eBB142E4"


class Casos(unittest.TestCase):
    def test_1_mint_solana(self):
        self.assertEqual(norm.address(f"  {MINT} "), MINT)                 # base58 exacto: no se cambia el caso
        self.assertIsNone(norm.address(MINT.replace("6", "0")))            # '0' no es base58
        self.assertIsNone(norm.address("abc"))

    def test_2_evm(self):
        self.assertEqual(norm.address(EVM), EVM.lower())
        self.assertIsNone(norm.address(EVM[:-1]))                          # 39 hex

    def test_3_cashtag(self):
        for v in ("$wif", "wif", "WIF", " $Wif "):
            self.assertEqual(norm.cashtag(v), "WIF")
        self.assertIsNone(norm.cashtag("$1INCH"))                          # tiene que empezar con letra
        self.assertIsNone(norm.cashtag("$" + "A" * 16))

    def test_4_keyword_y_sinonimos(self):
        self.assertEqual(norm.keyword("  Meme   Coin "), "memecoin")
        self.assertEqual(norm.keyword("PumpFun"), "pump.fun")
        self.assertEqual(norm.keyword("L2"), "layer 2")
        self.assertEqual(norm.keyword("Solana,"), "solana")
        groups = {"memecoin": "a", "layer 2": "f"}
        self.assertEqual(norm.keyword_group("meme coins", groups), "a")

    def test_5_timestamp(self):
        t = 1790823600                                                     # 01/10/2026 03:00 UTC
        for v in (t, float(t), t * 1000, str(t), "2026-10-01T03:00:00Z", "2026-10-01T03:00:00.000000123+00:00",
                  "Thu, 01 Oct 2026 03:00:00 +0000", "2026-10-01_030000"):
            self.assertEqual(norm.timestamp(v), t, v)
        self.assertIsNone(norm.timestamp(12))                              # 1970: no es una fecha de ítem
        self.assertIsNone(norm.timestamp("ayer"))
        self.assertIsNone(norm.timestamp(True))

    def test_6_url(self):
        self.assertEqual(norm.url("HTTPS://News.Example.COM/a/b/?utm_source=x&id=7&ref=37754157#frag"),
                         "https://news.example.com/a/b?id=7")
        self.assertEqual(norm.url("https://example.com/"), "https://example.com")
        self.assertIsNone(norm.url("javascript:alert(1)"))
        self.assertIsNone(norm.url("t.me/s/canal"))                        # sin esquema

    def test_7_hash(self):
        self.assertEqual(norm.hash_hex(" 3F2A9C1E0B7D4A55 "), "3f2a9c1e0b7d4a55")
        self.assertIsNone(norm.hash_hex("xyz"))
        self.assertIsNone(norm.hash_hex("abc"))                            # demasiado corto

    def test_8_nulos(self):
        for v in (None, "", "  ", "null", "None", "N/A", "nan", "undefined"):
            self.assertTrue(norm.is_null(v), v)
            self.assertIsNone(norm.address(v))
            self.assertIsNone(norm.cashtag(v))
            self.assertIsNone(norm.keyword(v))
            self.assertIsNone(norm.timestamp(v))
            self.assertIsNone(norm.url(v))
        self.assertFalse(norm.is_null(0))


class Registro(unittest.TestCase):
    def test_registro_src1_completo(self):
        raw = {"v": "src-1", "bot": " rss ", "src": "gnews", "kind": "news", "id": "x", "url": "https://A.com/x/?utm_medium=1",
               "ts": 1790823600000, "seen": "2026-10-01T03:05:00Z", "title": "  Hola   mundo ",
               "a": [EVM, EVM.lower(), MINT, "basura"], "c": ["wif", "$WIF", "bonk"], "k": ["Meme Coin", "memecoin", "l2"],
               "h": "ABCDEF0123456789", "au": None, "m": {"x": 1}}
        r = norm.record(raw)
        self.assertEqual(r["a"], sorted([EVM.lower(), MINT]))
        self.assertEqual(r["c"], ["BONK", "WIF"])
        self.assertEqual(r["k"], ["layer 2", "memecoin"])
        self.assertEqual((r["ts"], r["seen"]), (1790823600, 1790823900))
        self.assertEqual((r["url"], r["h"], r["bot"], r["title"]), ("https://a.com/x", "abcdef0123456789", "rss", "Hola mundo"))
        self.assertEqual(r["m"], {"x": 1})
        self.assertEqual(norm.record(r), r)                                # idempotente

    def test_almacen_usa_la_forma_canonica(self):
        import lib_sources_store as store
        root = Path(tempfile.mkdtemp(prefix="norm_"))
        self.addCleanup(shutil.rmtree, root, True)
        r = store.make_record("rss", "s", "news", "Nueva meme coin en PumpFun", ts=1790823600, seen=1790823600,
                              keywords=["meme coin", "pumpfun"])
        self.assertEqual(r["k"], ["memecoin", "pump.fun"])
        self.assertEqual(len(store.query("Meme Coin", records=[r])), 1)    # la consulta también se normaliza
        legacy = dict(r, ts=r["ts"] * 1000, c=["wif"], k=["meme coin"])     # diario viejo, sin normalizar
        path = store.day_path("rss", 1790823600, root=root)
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(legacy) + "\n", encoding="utf-8")
        (merged,) = store.collect(now=1790823600 + 60, root=root)
        self.assertEqual((merged["ts"], merged["c"], merged["k"]), (1790823600, ["WIF"], ["memecoin"]))
        self.assertEqual(norm.check_file(path), {"total": 1, "changed": 1, "broken": 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)
