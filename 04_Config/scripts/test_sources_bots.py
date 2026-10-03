#!/usr/bin/env python3
"""lib_sources_store + bot_rss_news (doc 34). unittest, sin red, fixtures sintéticos.

Uso: python 04_Config/scripts/test_sources_bots.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bot_rss_news as bot  # noqa: E402
import lib_info_signals as inf  # noqa: E402
import lib_sources_store as store  # noqa: E402

NOW = 1_790_900_000
MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
EVM = "0x" + "AB" * 20

RSS = f"""<?xml version="1.0"?><rss version="2.0"><channel><title>X</title>
<item><title>New memecoin $WIF2 launches on pump.fun</title><link>https://n.example/a</link>
<guid>https://n.example/a</guid><pubDate>Sat, 03 Oct 2026 00:00:00 +0000</pubDate>
<description>&lt;p&gt;CA {MINT}&lt;/p&gt;</description><author>ana</author></item>
<item><title>New memecoin $WIF2 launches on pump.fun</title><link>https://n.example/a</link>
<pubDate>Sat, 03 Oct 2026 00:00:00 +0000</pubDate></item>
<item><title>RWA tokenization grows</title><link>https://n.example/b</link>
<pubDate>Sat, 03 Oct 2026 01:00:00 +0000</pubDate><description>{EVM}</description></item>
</channel></rss>"""

ATOM = """<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Solana DePIN update</title>
<link href="https://a.example/1"/><id>tag:1</id><updated>2026-10-03T02:00:00Z</updated>
<summary>nothing</summary><author><name>bob</name></author></entry></feed>"""

CONFIG = {"dedup_hours": 72, "feeds": [{"name": "rss1", "url": "u1"}, {"name": "atom1", "url": "u2"},
                                        {"name": "down", "url": "u3"}, {"name": "html", "url": "u4"},
                                        {"name": "off", "url": "u5", "enabled": False}]}
PAGES = {"u1": (200, RSS), "u2": (200, ATOM), "u3": ("error ConnectTimeout", None), "u4": (200, "<html>blocked")}


def fetch(url):
    return PAGES[url]


class Tmp(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="sources_"))
        self.addCleanup(shutil.rmtree, self.root, True)


class Store(Tmp):
    def test_make_record_esquema_sin_cuerpo(self):
        r = store.make_record("rss", "s", "news", f"cuerpo largo {MINT} y {EVM}", title="T $Wif memecoin " * 30,
                              ts=NOW, seen=NOW, author="Ana")
        self.assertEqual(r["v"], "src-1")
        self.assertEqual(r["a"], sorted([MINT, EVM.lower()]))
        self.assertEqual((r["c"], r["k"]), (["WIF"], ["memecoin"]))
        self.assertLessEqual(len(r["title"]), store.TITLE_MAX)                 # cortado y sin espacio final
        self.assertEqual(r["title"], r["title"].strip())
        self.assertNotIn("cuerpo", json.dumps(r))
        self.assertEqual((len(r["h"]), len(r["au"])), (16, 12))
        self.assertIsNone(store.make_record("telegram", "c", "message", "hola", title="hola")["title"])
        with self.assertRaises(ValueError):
            store.make_record("x", "s", "otro", "t")

    def rec(self, bot, src, text, ts, **kw):
        return store.make_record(bot, src, "news", text, ts=ts, seen=ts, title=text, **kw)

    def test_merge_dedup_global_ventana_e_indice(self):
        a = self.rec("rss", "s1", f"hola {MINT}", NOW - 60)
        dup = dict(a, bot="web")                                  # misma (src, ts, h) desde otro diario
        viejo = self.rec("rss", "s1", "viejo $ABC", NOW - 49 * 3600)
        b = self.rec("forums", "4chan", "$ABC memecoin", NOW - 30)
        store.append_records("rss", [a, viejo], NOW, root=self.root)
        store.append_records("rss", [viejo], NOW - 49 * 3600, root=self.root)
        store.append_records("web", [dup], NOW, root=self.root)
        store.append_records("forums", [b], NOW, root=self.root)
        tg = store.append_records("telegram", [self.rec("telegram", "c", "otro", NOW - 10)], NOW, "a", root=self.root)
        self.assertTrue(tg.name.endswith("_a.jsonl"))
        with tg.open("a") as f:
            f.write('{"cortada": ')                                # línea rota: se ignora
        self.assertEqual(store.merge(NOW, root=self.root), 3)
        base = store.sources_dir(self.root)
        merged = store.read_jsonl(base / "_merged.jsonl")
        self.assertEqual([r["ts"] for r in merged], [NOW - 10, NOW - 30, NOW - 60])
        idx = json.loads((base / "_index.json").read_text())
        self.assertEqual((idx["a"][MINT], idx["c"]["ABC"], idx["k"]["memecoin"]), ([2], [1], [1]))

    def test_query_y_load(self):
        store.append_records("rss", [self.rec("rss", "s", f"x {MINT}", NOW - 100),
                                     self.rec("rss", "s", "$ABC RWA tokenization", NOW - 50),
                                     self.rec("rss", "s", f"{EVM} abc", NOW - 10)], NOW, root=self.root)
        q = lambda k, **kw: store.query(k, now=NOW, root=self.root, **kw)   # noqa: E731  (sin _merged: reconstruye)
        self.assertEqual(len(q(MINT)), 1)
        self.assertEqual(len(q(EVM.upper().replace("0X", "0x"))), 1)
        self.assertEqual([r["ts"] for r in q("$abc")], [NOW - 50])
        self.assertEqual([r["ts"] for r in q("abc")], [NOW - 10, NOW - 50])   # cashtag o título
        self.assertEqual(len(q("RWA")), 1)
        self.assertEqual(len(q("abc", since=NOW - 20)), 1)
        self.assertEqual(len(q("abc", limit=1)), 1)
        self.assertEqual(q(""), [])
        store.merge(NOW, root=self.root)
        store.append_records("rss", [self.rec("rss", "s", "$ABC nuevo", NOW - 5)], NOW, root=self.root)
        self.assertEqual(len(store.query("$ABC", now=NOW + 60, root=self.root)), 1)          # _merged fresco
        self.assertEqual(len(store.query("$ABC", now=NOW + 20 * 60, root=self.root)), 2)     # viejo: reconstruye

    def test_compatible_con_mentions(self):
        recs = [self.rec("rss", "s", f"x {MINT}", NOW - 100), self.rec("rss", "s", "$PEPE", NOW - 50)]
        items = store.to_items_store(recs)
        self.assertEqual(items[0]["f"], "rss:s")
        self.assertIsNotNone(inf.mentions(MINT, "PEPE", items, NOW))

    def test_keywords_yaml(self):
        self.assertEqual(store.load_keywords(self.root), list(store.DEFAULT_KEYWORDS))
        real = store.load_keywords(HERE.parents[1])
        self.assertIn("depin", real)
        self.assertIn("pump.fun", real)


class Rss(Tmp):
    def test_run_dedup_salud_y_fuente_caida(self):
        sleeps = []
        recs, st = bot.run(CONFIG, {}, fetch, NOW, sleeps.append)
        self.assertEqual(sorted(r["title"] for r in recs),
                         ["New memecoin $WIF2 launches on pump.fun", "RWA tokenization grows", "Solana DePIN update"])
        first = next(r for r in recs if r["title"].startswith("New"))
        self.assertEqual((first["a"], first["c"], first["url"]), ([MINT], ["WIF2"], "https://n.example/a"))
        self.assertIn("pump.fun", first["k"])
        atom = next(r for r in recs if r["src"] == "atom1")
        self.assertEqual((atom["url"], atom["ts"]), ("https://a.example/1", 1790992800))
        f = st["feeds"]
        self.assertEqual((f["rss1"]["items"], f["rss1"]["new"], f["rss1"]["last_ok"]), (3, 2, NOW))
        self.assertEqual((f["down"]["fails"], f["down"]["status"]), (1, "error ConnectTimeout"))
        self.assertIn("parse_error", f["html"])
        self.assertNotIn("off", f)
        self.assertEqual(len(sleeps), 3)
        again, st2 = bot.run(CONFIG, st, fetch, NOW + 1200, lambda s: None)
        self.assertEqual(again, [])                                       # ya vistos
        self.assertEqual(st2["feeds"]["down"]["fails"], 2)
        late, _ = bot.run(CONFIG, st2, fetch, NOW + 73 * 3600, lambda s: None)
        self.assertEqual(len(late), 3)                                    # vencieron las 72 h

    def test_config_real_y_validacion(self):
        cfg = bot.load_config(bot.config_path(HERE.parents[1]))
        self.assertEqual(len(cfg["feeds"]), 12)
        bad = self.root / "bad.yaml"
        for text in ("feeds: 3", "feeds:\n  - {name: a}", "feeds:\n  - {name: a, url: x}\n  - {name: a, url: y}"):
            bad.write_text(text)
            with self.assertRaises(ValueError):
                bot.load_config(bad)

    def test_main_escribe_diario_y_estado(self):
        cfg = self.root / "rss.yaml"
        cfg.write_text("feeds:\n  - {name: rss1, url: u1}\n")
        from unittest import mock
        with mock.patch.object(store, "ROOT", self.root), mock.patch.object(bot, "http_fetch", fetch):
            self.assertEqual(bot.main(["--config", str(cfg), "--dry-run"]), 0)
            self.assertFalse((self.root / "02_Analisis").exists())
            self.assertEqual(bot.main(["--config", str(cfg)]), 0)
        d = self.root / "02_Analisis" / "sources" / "rss"
        self.assertEqual(len(store.read_jsonl(next(d.glob("20*.jsonl")))), 2)
        self.assertEqual(json.loads((d / "_state.json").read_text())["items_last_run"], 2)


class Workflow(unittest.TestCase):
    def test_sources_rss_yml(self):
        import yaml
        wf = yaml.safe_load((HERE.parents[1] / ".github" / "workflows" / "sources_rss.yml").read_text())
        self.assertEqual(wf[True]["schedule"][0]["cron"], "3,23,43 * * * *")      # 'on' -> True en YAML 1.1
        steps = " ".join(str(s.get("run", "")) for s in wf["jobs"]["collect"]["steps"])
        self.assertIn("bot_rss_news.py", steps)
        self.assertIn("git add -- 02_Analisis/sources/rss", steps)
        self.assertNotIn("--force", steps)


if __name__ == "__main__":
    unittest.main(verbosity=2)
