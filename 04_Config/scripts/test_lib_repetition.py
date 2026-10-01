#!/usr/bin/env python3
"""Tests de lib_repetition (doc 26 v0.1): parsers con fixtures y fórmula. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_repetition.py
"""
import importlib.util
import math
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("lib_repetition_test", Path(__file__).resolve().parent / "lib_repetition.py")
rep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rep)

CA = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
RSS = """<?xml version="1.0"?><rss version="2.0"><channel><title>t</title>
<item><title>VSOF sube</title><link>https://a.example/1</link><guid>g1</guid>
<pubDate>Thu, 01 Oct 2026 03:00:00 +0000</pubDate><description><![CDATA[<p>CA: 6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump</p>]]></description></item>
<item><title>Otra</title><guid>g2</guid><pubDate>Thu, 01 Oct 2026 02:00:00 GMT</pubDate></item>
</channel></rss>"""
ATOM = """<?xml version="1.0" encoding="UTF-8"?><feed xmlns="http://www.w3.org/2005/Atom">
<entry><author><name>/u/alguien</name></author><id>t3_abc</id><title>$VSOF to the moon</title>
<updated>2026-10-01T03:10:00+00:00</updated><content type="html">&lt;p&gt;hola&lt;/p&gt;</content></entry></feed>"""
TELEGRAM = """<html><body>
<div class="tgme_widget_message_wrap js-widget_message_wrap"><div class="tgme_widget_message js-widget_message" data-post="whale_alert_io/101">
<div class="tgme_widget_message_bubble"><div class="tgme_widget_message_text js-message_text" dir="auto">Nuevo par<br/>CA: 6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump <div class="inner">anidado</div> fin</div>
<div class="tgme_widget_message_footer"><a class="tgme_widget_message_date"><time datetime="2026-10-01T03:55:38+00:00" class="time">03:55</time></a></div></div></div></div>
<div class="tgme_widget_message_wrap"><div class="tgme_widget_message" data-post="whale_alert_io/102">
<div class="tgme_widget_message_text">sin fecha</div></div></div>
</body></html>"""
CHAN = [{"page": 1, "threads": [{"no": 7, "time": 1790800000, "last_modified": 1790800500, "sub": "$VSOF",
                                 "com": "CA: <wbr>" + CA + " &gt; vamos"}]}]
HN = {"hits": [{"objectID": "9", "created_at_i": 1790800000, "title": "Solana news", "author": "pg", "story_text": None}]}
CG = {"coins": [{"item": {"id": "vsof", "name": "VSOF", "symbol": "VSOF"}}]}
GDELT = {"timeline": [{"series": "Volume", "data": [{"date": "20261001T030000Z", "value": 12}]}]}


class Parsers(unittest.TestCase):
    def test_rss(self):
        items = rep.parse_feed(RSS, "CoinDesk")
        self.assertEqual([i["id"] for i in items], ["g1", "g2"])
        self.assertEqual(items[0]["ts"], 1790823600.0)                    # 01/10/2026 03:00 UTC
        self.assertIn(CA, items[0]["text"])
        self.assertNotIn("<p>", items[0]["text"])

    def test_atom_de_reddit(self):
        (item,) = rep.parse_feed(ATOM, "r/solana")
        self.assertEqual((item["id"], item["author"]), ("t3_abc", "/u/alguien"))
        self.assertEqual(item["ts"], 1790824200.0)
        self.assertIn("$VSOF", item["text"])

    def test_telegram_un_item_por_mensaje(self):
        items = rep.parse_telegram_preview(TELEGRAM, "t.me/s/whale_alert_io")
        self.assertEqual([i["id"] for i in items], ["whale_alert_io/101", "whale_alert_io/102"])
        self.assertEqual(items[0]["ts"], 1790826938.0)                 # 01/10/2026 03:55:38 UTC
        self.assertEqual(items[0]["text"], f"Nuevo par CA: {CA} anidado fin")
        self.assertIsNone(items[1]["ts"])
        self.assertEqual(items[0]["author"], "whale_alert_io")

    def test_4chan_hn_coingecko_gdelt(self):
        (t,) = rep.parse_4chan_catalog(CHAN, "/biz/")
        self.assertEqual((t["id"], t["ts"]), ("7", 1790800500))
        self.assertIn(CA, t["text"])
        self.assertIn("> vamos", t["text"])
        self.assertEqual(rep.parse_hn(HN, "hn")[0]["text"], "Solana news")
        self.assertEqual(rep.parse_coingecko_trending(CG, "cg")[0]["text"], "VSOF $VSOF")
        self.assertEqual(rep.parse_gdelt_timeline(GDELT, "gdelt")[0]["ts"], 1790823600.0)

    def test_respuesta_rota_lanza_para_que_la_sonda_la_registre(self):
        with self.assertRaises(Exception):
            rep.parse_feed("<html>bloqueado</html", "x")


class Menciones(unittest.TestCase):
    def test_pesos(self):
        self.assertEqual(rep.match_weight(f"CA: {CA}", CA, "VSOF"), 1.0)
        self.assertEqual(rep.match_weight("compré $vsof hoy", CA, "VSOF"), 0.5)
        self.assertEqual(rep.match_weight("compré $VSOFX hoy", CA, "VSOF"), 0.0)        # otro cashtag
        self.assertEqual(rep.match_weight("Weird Cat sube", CA, "WEIRD", "Weird Cat"), 0.25)
        self.assertEqual(rep.match_weight("Cat sube", CA, "CAT", "Cat"), 0.0)            # nombre de 1 palabra: no

    def test_dedup_por_fuente_y_texto(self):
        items = [{"source": "a", "ts": 1, "text": f"CA {CA} https://x.example/1", "author": "u1"},
                 {"source": "a", "ts": 2, "text": f"ca {CA}  https://y.example/2", "author": "u2"},   # reenvío
                 {"source": "b", "ts": 3, "text": f"CA {CA}", "author": "u3"},
                 {"source": "b", "ts": None, "text": f"CA {CA} otro", "author": "u4"}]           # sin fecha
        found = rep.mentions(items, CA)
        self.assertEqual([(m["source"], m["ts"]) for m in found], [("a", 1), ("b", 3)])


class Formula(unittest.TestCase):
    """Los números del doc 26 §3.3 [V, cálculo]."""

    def test_caso_a_directiva_y_v01(self):
        self.assertAlmostEqual(rep.intensity_v0(24, 3, 4, 1.5), 21.33, places=2)
        self.assertAlmostEqual(rep.intensity_v01(24, 3, 8, 4, 1.5), 27.78, places=2)
        self.assertAlmostEqual(rep.surprise(24, 3), 31.3, places=1)

    def test_caso_b_ruido(self):
        self.assertEqual(rep.intensity_v0(2, 0.5, 1, 1), 4.0)
        self.assertAlmostEqual(math.exp(-rep.surprise(2, 0.5)), 0.0902, places=4)
        self.assertLess(rep.surprise(2, 0.5), rep.SURPRISE_MIN)

    def test_caso_c_token_nuevo_sin_division_por_cero(self):
        self.assertIsNone(rep.intensity_v0(6, 0, 2, 0))
        self.assertAlmostEqual(rep.intensity_v01(6, 0, 0, 1, 0), 7.0 * 7.0 ** 0.5, places=6)
        self.assertAlmostEqual(math.exp(-rep.surprise(6, 0)), 2.738e-7, delta=1e-9)

    def test_fuentes_efectivas(self):
        self.assertAlmostEqual(rep.effective_sources({"a": 12, "b": 6, "c": 4, "d": 2}), 3.32, places=2)
        self.assertAlmostEqual(rep.effective_sources({"a": 21, "b": 1, "c": 1, "d": 1}), 1.67, places=2)
        self.assertEqual(rep.effective_sources({}), 0.0)

    def test_poisson_estable(self):
        for k, lam in ((0, 2.0), (1, 0.3), (5, 5.0), (12, 3.0)):
            direct = 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))
            self.assertAlmostEqual(math.exp(rep.poisson_log_sf(k, lam)), direct, places=10)
        self.assertTrue(math.isfinite(rep.surprise(400, 3)))                 # cola extrema sin overflow
        self.assertGreater(rep.surprise(400, 3), 1000)


class Snapshot(unittest.TestCase):
    NOW = 1790830000.0

    def mention(self, minutes_ago, source, author):
        return {"ts": self.NOW - minutes_ago * 60, "source": source, "weight": 1.0, "author": author}

    def test_pico_con_varias_fuentes(self):
        base = [self.mention(60 + 20 * i, "r/solana", f"b{i}") for i in range(72)]      # 3/h durante 24 h
        cur = [self.mention(i * 2 + 1, src, f"u{i}") for i, src in
               enumerate(["t.me/a"] * 12 + ["r/solana"] * 6 + ["/biz/"] * 4 + ["hn"] * 2)]
        s = rep.repetition_snapshot(base + cur, self.NOW)
        self.assertEqual(s["m_1h"], 24)
        self.assertAlmostEqual(s["m_24h_mean"], 3.0)
        self.assertAlmostEqual(s["seff_1h"], 3.32, places=2)
        self.assertTrue(s["signal"])
        self.assertEqual(s["tier"], "saturación")
        self.assertEqual(s["version"], "rep-0.1")

    def test_ruido_no_es_senal(self):
        s = rep.repetition_snapshot([self.mention(10, "a", "x"), self.mention(20, "b", "y")], self.NOW)
        self.assertFalse(s["signal"])
        self.assertEqual(s["tier"], "normal")

    def test_una_sola_cuenta_repitiendo_no_es_senal(self):
        cur = [self.mention(i + 1, src, "bot") for i, src in enumerate(["a", "b", "c"] * 4)]
        s = rep.repetition_snapshot(cur, self.NOW)
        self.assertLess(s["authors_ratio"], rep.AUTHORS_MIN)
        self.assertFalse(s["signal"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
