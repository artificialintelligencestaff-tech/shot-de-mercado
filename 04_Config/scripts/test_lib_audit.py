#!/usr/bin/env python3
"""Tests de la auditoría por bot (patrón #15): lib_audit, bot_rss_news y bot_orchestrator. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_audit.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_orchestrator as orch  # noqa: E402
import bot_rss_news as rss  # noqa: E402
import lib_audit as audit  # noqa: E402
import lib_sources_store as store  # noqa: E402

NOW = 1791000000
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="audit_"))
        self.addCleanup(shutil.rmtree, self.root, True)

    def lines(self, folder):
        return [json.loads(x) for x in (folder / "_audit.jsonl").read_text(encoding="utf-8").splitlines()]


class Rss(Base):
    def test_linea_por_corrida_y_metricas(self):
        state = {"last_run": NOW, "feeds": {
            "ok": {"status": 200, "items": 5, "new": 3, "checked_at": NOW},
            "caido": {"status": 404, "items": 0, "new": 0, "checked_at": NOW, "fails": 2},
            "apagado": {"status": 404, "items": 0, "checked_at": NOW - 3600, "auto_off_until": NOW + 100}}}
        folder = self.root / "rss"
        m = rss.write_audit(state, 3, 12.345, folder=folder)
        (line,) = self.lines(folder)
        self.assertEqual({k: line[k] for k in ("ts", "bot", "items_in", "items_new", "items_discarded", "errors",
                                               "sources", "duration_s", "status")},
                         {"ts": NOW, "bot": "rss", "items_in": 5, "items_new": 3, "items_discarded": 2, "errors": 1,
                          "sources": 2, "duration_s": 12.35, "status": "partial"})   # el apagado no se consultó
        self.assertTrue(line["timestamp"].startswith("2026-10-0"))
        self.assertEqual((m["runs"], m["dedup_rate"], m["error_rate"], m["sources_healthy"], m["sources_total"]),
                         (1, 0.4, 0.5, 1, 3))
        self.assertEqual(json.loads((folder / "_metrics.json").read_text(encoding="utf-8")), m)


class Orchestrator(Base):
    def test_auditoria_del_orquestador(self):
        (self.root / "04_Config" / "sources").mkdir(parents=True)
        (self.root / "04_Config" / "sources" / "_bots.yaml").write_text(
            "bots:\n  rss: {workflow: x.yml, stale_min: 60}\n  web: {workflow: w.yml, enabled: false}\n",
            encoding="utf-8")
        rec = store.make_record("rss", "s", "news", f"memecoin {MINT}", ts=NOW - 600, seen=NOW - 500)
        store.append_records("rss", [rec, rec], NOW - 500, root=self.root)       # duplicado: se descarta al fusionar
        base = store.sources_dir(self.root)
        (base / "rss" / "_state.json").write_text(json.dumps({"last_run": NOW - 300, "items_last_run": 2,
                                                              "feeds": {"s": {"status": 200}}}), encoding="utf-8")
        doc = orch.run(self.root, now=NOW)
        (line,) = self.lines(base / "orchestrator")
        self.assertEqual((line["bot"], line["items_in"], line["items_new"], line["items_discarded"]),
                         ("orchestrator", 2, 1, 1))
        self.assertEqual((line["errors"], line["sources"], line["status"]), (0, 1, "success"))   # web está en diseño
        self.assertEqual(doc["metrics"]["runs"], 1)
        self.assertEqual(store.collect(NOW, root=self.root)[0]["a"], [MINT])     # _audit.jsonl no entra al merge
        orch.prune(self.root, NOW + 30 * 86400)
        self.assertTrue((base / "orchestrator" / "_audit.jsonl").exists())        # ni lo poda el orquestador


class Agregados(Base):
    def test_metricas_rodantes_y_retencion(self):
        folder = self.root / "rss"
        old = audit.audit_line("rss", NOW - 100 * 86400, 10, 10, 0, 2, 1.0)        # fuera de la retención (90 d)
        mid = audit.audit_line("rss", NOW - 40 * 86400, 10, 10, 0, 2, 1.0)         # retenida, fuera de métricas (30 d)
        for line in (old, mid):
            audit.record_run(folder, line, 2, 2)
        audit.record_run(folder, audit.audit_line("rss", NOW - 3600, 10, 6, 1, 2, 3.0), 2, 2)   # partial
        m = audit.record_run(folder, audit.audit_line("rss", NOW, 0, 0, 2, 2, 5.0), 0, 2)
        lines = self.lines(folder)
        self.assertEqual([x["ts"] for x in lines], [NOW - 40 * 86400, NOW - 3600, NOW])
        self.assertEqual((m["runs"], m["items_total"], m["availability"], m["avg_duration_s"]), (2, 6, 0.5, 4.0))
        self.assertEqual((m["dedup_rate"], m["error_rate"]), (0.4, 0.75))
        self.assertEqual(audit.status_of(0, 0), "failure")


if __name__ == "__main__":
    unittest.main(verbosity=2)
