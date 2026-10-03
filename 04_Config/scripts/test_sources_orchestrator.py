#!/usr/bin/env python3
"""bot_orchestrator (5) + integración de lib_sources_store.query con script_116 y script_97 (3). Sin red.

Uso: python 04_Config/scripts/test_sources_orchestrator.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bot_orchestrator as orch  # noqa: E402
import lib_info_signals as inf  # noqa: E402
import lib_sources_store as store  # noqa: E402

NOW = 1_790_900_000
MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"


def rec(text, ts, bot="rss", src="s"):
    return store.make_record(bot, src, "news", text, ts=ts, seen=ts, title=text)


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="orch_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        (self.root / "04_Config" / "sources").mkdir(parents=True)
        shutil.copy(HERE.parents[1] / "04_Config" / "sources" / "_bots.yaml", self.root / "04_Config" / "sources")
        self.base = store.sources_dir(self.root)

    def state(self, bot, last_run, items=1, feeds=None):
        d = self.base / bot
        d.mkdir(parents=True, exist_ok=True)
        (d / "_state.json").write_text(json.dumps({"last_run": last_run, "items_last_run": items,
                                                   "feeds": feeds or {"f1": {"status": 200}}}))


class Orchestrator(Base):
    def test_merge_index_y_health(self):
        store.append_records("rss", [rec(f"x {MINT}", NOW - 60), rec("$ABC", NOW - 30)], NOW, root=self.root)
        self.state("rss", NOW - 120, 2)
        doc = orch.run(self.root, NOW)
        self.assertEqual(doc["merged_items"], 2)
        self.assertEqual(len(store.read_jsonl(self.base / "_merged.jsonl")), 2)
        self.assertEqual(json.loads((self.base / "_index.json").read_text())["a"][MINT], [1])
        h = json.loads((self.base / "_health.json").read_text())
        self.assertEqual((h["bots"]["rss"]["status"], h["bots"]["rss"]["last_output"]), ("ok", 2))
        self.assertEqual(h["bots"]["telegram"]["status"], "diseño")

    def test_estados_atrasado_sin_datos_y_errores(self):
        self.assertEqual(orch.run(self.root, NOW)["bots"]["rss"]["status"], "sin_datos")
        self.state("rss", NOW - 61 * 60, 0, {"a": {"status": 200}, "b": {"status": 403},
                                             "c": {"status": 200, "parse_error": "ParseError: x"}})
        h = orch.run(self.root, NOW)["bots"]["rss"]
        self.assertEqual((h["status"], h["sources_ok"], h["sources_total"]), ("atrasado", 1, 3))
        self.assertEqual(h["errors"], ["b: 403", "c: 200 (ParseError: x)"])

    def test_vacio_y_caido_cuentan_corridas_nuevas(self):
        for i in range(3):                                   # 3 corridas nuevas sin ítems
            self.state("rss", NOW + i * 1200, 0)
            st = orch.run(self.root, NOW + i * 1200 + 60)["bots"]["rss"]
        self.assertEqual((st["status"], st["empty_runs"]), ("vacío", 3))
        st = orch.run(self.root, NOW + 2 * 1200 + 120)["bots"]["rss"]     # misma corrida: no suma
        self.assertEqual(st["empty_runs"], 3)
        for i in range(3, 6):
            self.state("rss", NOW + i * 1200, 0, {"f1": {"status": "error X"}})
            st = orch.run(self.root, NOW + i * 1200 + 60)["bots"]["rss"]
        self.assertEqual(st["status"], "caído")

    def test_poda_7_dias_y_dry_run(self):
        store.append_records("rss", [rec("viejo", NOW - 8 * 86400)], NOW - 8 * 86400, root=self.root)
        store.append_records("rss", [rec("nuevo", NOW - 60)], NOW, root=self.root)
        orch.run(self.root, NOW, write=False)
        self.assertFalse((self.base / "_health.json").exists())
        self.assertEqual(len(list((self.base / "rss").glob("*.jsonl"))), 2)
        doc = orch.run(self.root, NOW)
        self.assertEqual(len(doc["pruned"]), 1)
        self.assertEqual(len(list((self.base / "rss").glob("*.jsonl"))), 1)

    def test_bloque_auto_de_instalados_idempotente(self):
        inst = self.root / "_servicios_open_source" / "_INSTALADOS.md"
        inst.parent.mkdir()
        inst.write_text("# Servicios\n\nTexto de YIN.\n")
        self.state("rss", NOW - 60)
        self.assertTrue(orch.run(self.root, NOW)["installed_updated"])
        text = inst.read_text()
        self.assertIn("Texto de YIN.", text)
        self.assertIn("| `rss` | ok |", text)
        self.assertFalse(orch.run(self.root, NOW + 60)["installed_updated"])      # sin cambio de estado
        self.state("rss", NOW - 2 * 3600)
        self.assertTrue(orch.run(self.root, NOW)["installed_updated"])
        self.assertEqual(inst.read_text().count(orch.AUTO_START), 1)
        self.assertIn("| `rss` | atrasado |", inst.read_text())


class Integracion(Base):
    def test_script_116_suma_menciones_del_almacen(self):
        import script_116_early_watch as s116
        store.append_records("rss", [rec(f"CA {MINT}", NOW - 120), rec("$EARLY moon", NOW - 60)], NOW, root=self.root)
        ctx = {"items": None, "sources": store.safe_load(NOW, self.root)}
        items = s116.young_mention_items(MINT, "EARLY", ctx)
        self.assertEqual(len(items), 2)
        m = inf.mentions(MINT, "EARLY", items, NOW)
        self.assertGreater(m["s"], 0)
        base = [{"ts": NOW - 10, "a": [MINT], "c": [], "f": "reddit_rss"}]
        self.assertEqual(len(s116.young_mention_items(MINT, "EARLY", dict(ctx, items=base))), 3)

    def test_sin_almacen_no_hay_dependencia_dura(self):
        import script_116_early_watch as s116
        self.assertEqual(store.safe_load(NOW, self.root), [])
        with mock.patch.object(store, "load", side_effect=OSError("roto")):
            self.assertEqual(store.safe_load(NOW, self.root), [])
        self.assertIsNone(s116.young_mention_items(MINT, "X", {"items": None, "sources": []}))
        self.assertEqual(s116.young_mention_items(MINT, "X", {"items": [], "sources": []}), [])
        import script_97_emit_alerts as s97
        self.assertEqual(s97.source_mentions(MINT, "X", NOW, rows=[]),
                         {"sources_mentions_1h": 0, "sources_mentions_24h": 0, "sources_feeds": []})

    def test_script_97_menciones_informativas_para_60_min_o_mas(self):
        import script_97_emit_alerts as s97
        store.append_records("rss", [rec(f"{MINT}", NOW - 600), rec("$GOV news", NOW - 7200, src="b")], NOW,
                             root=self.root)
        rows = store.safe_load(NOW, self.root)
        got = s97.source_mentions(MINT, "GOV", NOW, rows=rows)
        self.assertEqual(got, {"sources_mentions_1h": 1, "sources_mentions_24h": 2,
                               "sources_feeds": ["rss:b", "rss:s"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
