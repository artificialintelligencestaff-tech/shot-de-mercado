#!/usr/bin/env python3
"""Tests de la memoria episódica (patrón #12): lib_episodic_memory y su cableado en bot_self_repair y
lib_scientific_method. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_episodic_memory.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_self_repair as sr  # noqa: E402
import lib_episodic_memory as em  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

T0 = 1791000000
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
EVM = "0xAbC0000000000000000000000000000000000dEf"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="episodes_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.src = self.root / "02_Analisis" / "sources"


class Memoria(Base):
    def test_escribe_consulta_y_no_duplica(self):
        e = em.write_episode("alerta_emitida", MINT, {"score": 72}, "emitida", ["Solana", "young"], T0, self.root)
        self.assertEqual((e["tipo"], e["entidad"], e["tags"], e["timestamp"]),
                         ("alerta_emitida", MINT, ["solana", "young"], "2026-10-03T04:00:00+00:00"))
        self.assertIsNone(em.write_episode("alerta_emitida", MINT, {"score": 72}, "emitida", ["solana"], T0,
                                           self.root))                  # mismo hecho: no se duplica
        em.write_episode("feed_caido", "rss/messari", {"evidence": "404 x3"}, "auto_off", ["rss"], T0 + 60, self.root)
        em.write_episode("alerta_emitida", EVM, {"score": 55}, "emitida", ["base"], T0 + 120, self.root)
        self.assertEqual(len(em.query_episodes(root=self.root)), 3)
        self.assertEqual([x["entidad"] for x in em.query_episodes({"tipo": "alerta_emitida"}, self.root)],
                         [MINT, EVM.lower()])                           # entidad canónica (EVM en minúsculas)
        self.assertEqual(len(em.query_episodes({"entidad": EVM.upper().replace("0X", "0x")}, self.root)), 1)
        self.assertEqual(len(em.query_episodes({"tags": ["SOLANA"]}, self.root)), 1)
        self.assertEqual(len(em.query_episodes({"desde": T0 + 60, "hasta": "2026-10-03T04:01:00Z"}, self.root)), 1)
        self.assertEqual(len(em.query_episodes(lambda x: x["contexto"].get("score", 0) > 60, self.root)), 1)
        with self.assertRaises(ValueError):
            em.write_episode("rumor", MINT, root=self.root)
        with self.assertRaises(ValueError):
            em.write_episode("feed_caido", "  ", root=self.root)

    def test_fragmentos_por_escritor_y_lectura_unificada(self):
        em.write_episode("bot_reparado", "rss", resultado="rerun", now=T0 + 10, root=self.root, writer="self_repair")
        em.write_episode("hipotesis_evaluada", "H-0", resultado="pendiente", now=T0, root=self.root, writer="method")
        em.write_episode("alerta_emitida", MINT, resultado="emitida", now=T0 + 20, root=self.root)
        self.assertEqual(sorted(p.name for p in self.src.glob("_episodes*.jsonl")),
                         ["_episodes.jsonl", "_episodes_method.jsonl", "_episodes_self_repair.jsonl"])
        eps = em.query_episodes(root=self.root)
        self.assertEqual([x["tipo"] for x in eps], ["hipotesis_evaluada", "bot_reparado", "alerta_emitida"])
        self.assertEqual([x["writer"] for x in em.query_episodes({"writer": "method"}, self.root)], ["method"])
        self.assertEqual([x["tipo"] for x in em.query_episodes(root=self.root, limit=1)], ["alerta_emitida"])
        with self.assertRaises(ValueError):
            em.episodes_path(self.root, "../fuera")
        (self.src / "_episodes.jsonl").open("a", encoding="utf-8").write('{"tipo": "alerta_emi')   # push a medias
        self.assertEqual(len(em.query_episodes(root=self.root)), 3)


class Cableado(Base):
    def test_self_repair_registra_caida_y_arreglo_solo_en_transiciones(self):
        (self.src / "rss").mkdir(parents=True)
        (self.root / "_servicios_open_source").mkdir()
        (self.root / "_servicios_open_source" / "_INSTALADOS.md").write_text("# I\n", encoding="utf-8")
        state = self.src / "rss" / "_state.json"
        state.write_text(json.dumps({"last_run": T0, "feeds": {"muerta": {"status": 404, "fails": 3}}}),
                         encoding="utf-8")
        (self.src / "_health.json").write_text(json.dumps({"bots": {"rss": {
            "status": "ok", "last_run": T0, "last_output": 5, "sources_ok": 1, "sources_total": 2}}}), encoding="utf-8")
        bots = {"rss": {"workflow": "sources_rss.yml", "every_min": 20, "stale_min": 60, "enabled": True}}
        gh = type("GH", (), {"enabled": False, "workflows": lambda s: [], "runs": lambda s, w: None})()
        sr.Repair(self.root, bots, gh, now=T0).run()
        sr.Repair(self.root, bots, gh, now=T0 + 1800).run()             # sigue apagada: no es episodio nuevo
        caidas = em.query_episodes({"tipo": "feed_caido"}, self.root)
        self.assertEqual([(x["entidad"], x["resultado"], x["writer"]) for x in caidas],
                         [("rss/muerta", "auto_off", "self_repair")])
        state.write_text(json.dumps({"last_run": T0, "feeds": {"muerta": {"status": 200, "fails": 0}}}),
                         encoding="utf-8")
        sr.Repair(self.root, bots, gh, now=T0 + 3600).run()             # se recuperó: auto_on
        self.assertEqual([x["resultado"] for x in em.query_episodes({"tipo": "bot_reparado"}, self.root)],
                         ["auto_on"])
        self.assertTrue((self.src / "_episodes_self_repair.jsonl").exists())

    def test_hipotesis_evaluada_y_alerta(self):
        sm.migrate_h0(root=self.root, now=T0)
        rows = [{"h0_group": "info_ge20", "primary": "hit"}] * 18 + [{"h0_group": "info_ge20", "primary": "miss"}] * 7 \
            + [{"h0_group": "info_lt20", "primary": "hit"}] * 5 + [{"h0_group": "info_lt20", "primary": "miss"}] * 15
        sm.evaluate_hypothesis("H-0", rows, root=self.root, now=T0 + 60, persist=False)
        self.assertEqual(em.query_episodes(root=self.root), [])          # sin persistir no hay episodio
        sm.evaluate_hypothesis("H-0", rows, root=self.root, now=T0 + 60)
        (ep,) = em.query_episodes({"tipo": "hipotesis_evaluada", "entidad": "H-0"}, self.root)
        self.assertEqual((ep["resultado"], ep["tags"], ep["contexto"]["n"], ep["contexto"]["test"]),
                         ("H-0 rechazada", ["a", "rechazada"], 45, "fisher_one_sided"))
        self.assertEqual(ep["contexto"]["data_hash"], sm.sha(rows))
        alert = {"mint": MINT, "symbol": "PEPE", "chain": "solana", "scorer": "young", "score": 64,
                 "timestamp": "2026-10-03_040000"}
        a = em.alert_episode(alert)
        self.assertEqual((a["tipo"], a["entidad"], a["ts"], a["resultado"], a["contexto"]["score"]),
                         ("alerta_emitida", MINT, T0, "emitida", 64))


if __name__ == "__main__":
    unittest.main(verbosity=2)
