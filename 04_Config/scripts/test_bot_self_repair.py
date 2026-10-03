#!/usr/bin/env python3
"""Tests de bot_self_repair (patrón #20, doc 34 §11). unittest, sin red: API de GitHub simulada.

Uso: python 04_Config/scripts/test_bot_self_repair.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_rss_news as rss  # noqa: E402
import bot_self_repair as sr  # noqa: E402

T0 = 1791000000
BOTS = {"rss": {"workflow": "sources_rss.yml", "every_min": 20, "stale_min": 60, "enabled": True},
        "telegram": {"workflow": "sources_telegram_a.yml", "enabled": False}}
INSTALADOS = "# Instalados\n\n<!-- AUTO:sources -->\nbloque del orquestador\n<!-- /AUTO:sources -->\n"


class FakeGH:
    def __init__(self, runs=None, enabled=True):
        self.enabled, self._runs = enabled, runs or {}
        self.reruns, self.dispatched = [], []

    def workflows(self):
        return sorted(self._runs)

    def runs(self, wf):
        return self._runs.get(wf)

    def rerun_failed(self, run_id):
        self.reruns.append(run_id)
        return True

    def dispatch(self, wf):
        self.dispatched.append(wf)
        return True


def run_list(*conclusions):
    return [{"id": 100 + i, "conclusion": c, "html_url": f"https://x/runs/{100 + i}"} for i, c in enumerate(conclusions)]


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="repair_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.src = self.root / "02_Analisis" / "sources"
        (self.src / "rss").mkdir(parents=True)
        (self.root / "_servicios_open_source").mkdir()
        self.inst = self.root / "_servicios_open_source" / "_INSTALADOS.md"
        self.inst.write_text(INSTALADOS, encoding="utf-8")

    def state(self, feeds, seen=None):
        (self.src / "rss" / "_state.json").write_text(
            json.dumps({"last_run": T0, "feeds": feeds, "seen": seen or {}}), encoding="utf-8")

    def health(self, **rss_row):
        row = {"status": "ok", "last_run": T0, "last_output": 5, "sources_ok": 2, "sources_total": 2, **rss_row}
        (self.src / "_health.json").write_text(json.dumps({"bots": {"rss": row}}), encoding="utf-8")

    def repair(self, now, gh=None):
        return sr.Repair(self.root, BOTS, gh or FakeGH(enabled=False), now=now).run()

    def repair_state(self):
        return json.loads((self.src / "_repair_state.json").read_text(encoding="utf-8"))


class FuenteCaida(Base):
    def test_3_fallas_apaga_6_h_y_el_bot_la_salta(self):
        self.state({"ok": {"status": 200, "fails": 0}, "muerta": {"status": 404, "fails": 3}})
        self.health()
        out = self.repair(T0)
        self.assertEqual([a["action"] for a in out["actions"]], ["auto_off"])
        off = self.repair_state()["auto_off"]["rss"]["muerta"]
        self.assertEqual(off["until"], T0 + sr.AUTO_OFF_S)
        fetched = []
        config = {"feeds": [{"name": "ok", "url": "u1"}, {"name": "muerta", "url": "u2"}]}
        _, st = rss.run(config, {"feeds": {"muerta": {"status": 404, "fails": 3}}}, now=T0 + 60, sleep=lambda s: None,
                        fetch=lambda u: fetched.append(u) or (200, "<rss><channel></channel></rss>"),
                        auto_off={"muerta": off})
        self.assertEqual(fetched, ["u1"])                                   # la caída no se consulta
        self.assertEqual(st["feeds"]["muerta"]["auto_off_until"], off["until"])
        _, st = rss.run(config, st, now=off["until"] + 1, sleep=lambda s: None,
                        fetch=lambda u: (200, "<rss><channel></channel></rss>"), auto_off={"muerta": off})
        self.assertEqual(st["feeds"]["muerta"]["fails"], 0)                 # al vencer reintenta (y se recuperó)

    def test_24_h_caida_escala_y_al_recuperarse_se_borra(self):
        self.health()
        self.state({"muerta": {"status": 404, "fails": 3}})
        self.repair(T0)
        self.state({"muerta": {"status": 404, "fails": 9}})
        self.health(last_run=T0 + sr.SOURCE_ESCALATE_S)                    # el bot sigue corriendo y trayendo ítems
        out = self.repair(T0 + sr.SOURCE_ESCALATE_S + 60)
        self.assertIn("source:rss:muerta", out["escalations"])
        text = self.inst.read_text(encoding="utf-8")
        self.assertIn("[P]", text)
        self.assertIn("muerta: 404 x9", text)
        self.assertIn("bloque del orquestador", text)                      # AUTO:sources intacto
        self.state({"muerta": {"status": 200, "fails": 0}})
        self.health(last_run=T0 + sr.SOURCE_ESCALATE_S + 3000)
        out = self.repair(T0 + sr.SOURCE_ESCALATE_S + 3600)
        self.assertEqual(out["escalations"], {})
        self.assertNotIn("rss", self.repair_state()["auto_off"])
        self.assertIn("Sin problemas abiertos", self.inst.read_text(encoding="utf-8"))
        self.assertIn("resolved", [a["action"] for a in out["actions"]])


class Workflows(Base):
    def test_rerun_una_vez_y_escala_sin_relanzar_produccion(self):
        self.health()
        gh = FakeGH({"sources_rss.yml": run_list("failure", "failure", "success"),
                     "pipeline_t0.yml": run_list("failure", "failure", "failure", "failure", "success")})
        out = self.repair(T0, gh)
        self.assertEqual(gh.reruns, [100])                                  # solo el workflow de un bot de fuentes
        self.assertIn("workflow:pipeline_t0.yml", out["escalations"])
        self.assertNotIn("workflow:sources_rss.yml", out["escalations"])   # 2 fallas: relanza, todavía no escala
        self.repair(T0 + 1800, gh)
        self.assertEqual(gh.reruns, [100])                                  # el mismo run no se relanza dos veces

    def test_atrasado_un_dispatch_y_despues_escala(self):
        self.health(status="atrasado", last_run=T0 - 7200)
        gh = FakeGH({})
        self.repair(T0, gh)
        self.assertEqual(gh.dispatched, ["sources_rss.yml"])
        out = self.repair(T0 + 3600, gh)
        self.assertEqual(gh.dispatched, ["sources_rss.yml"])                # no reintenta en loop
        self.assertIn("late:rss", out["escalations"])


class Salidas(Base):
    def test_vacio_mas_de_24_h_y_vacio_con_fuentes_ok_escalan(self):
        self.health(last_output=5)
        self.repair(T0)
        self.health(last_output=0, status="vacío", empty_runs=3, sources_ok=2, sources_total=2, last_run=T0 + 3000)
        out = self.repair(T0 + 3600)
        self.assertIn("parser:rss", out["escalations"])                    # vacío con fuentes OK: de inmediato
        self.assertNotIn("empty:rss", out["escalations"])
        out = self.repair(T0 + sr.EMPTY_ESCALATE_S + 60)
        self.assertIn("empty:rss", out["escalations"])

    def test_estado_corrupto_y_seen_inflado(self):
        self.health()
        (self.src / "rss" / "_state.json").write_text("{roto", encoding="utf-8")
        out = self.repair(T0)
        self.assertEqual([a["action"] for a in out["actions"]], ["reset_state"])
        self.assertFalse((self.src / "rss" / "_state.json").exists())
        self.assertTrue((self.src / "rss" / f"_state.json.corrupt-{T0}").exists())
        seen = {f"k{i}": T0 - (10 if i % 2 else 400_000) for i in range(sr.SEEN_MAX + 10)}
        self.state({"ok": {"status": 200, "fails": 0}}, seen)
        out = self.repair(T0 + 60)
        self.assertEqual([a["action"] for a in out["actions"]], ["trim_seen"])
        st = json.loads((self.src / "rss" / "_state.json").read_text(encoding="utf-8"))
        self.assertEqual(len(st["seen"]), (sr.SEEN_MAX + 10) // 2)          # quedan solo las de la ventana de 72 h

    def test_sin_token_detecta_pero_no_actua(self):
        self.health(status="atrasado", last_run=T0 - 7200)
        out = self.repair(T0, FakeGH({"sources_rss.yml": run_list("failure", "failure")}, enabled=False))
        self.assertEqual([a["action"] for a in out["actions"]], ["sin_token"])
        log = (self.src / "_repair_log.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(json.loads(log[0])["action"], "sin_token")


class RssConfig(unittest.TestCase):
    def test_feed_sacado_del_yaml_no_queda_en_la_salud(self):
        config = {"feeds": [{"name": "ok", "url": "u1"}]}
        _, st = rss.run(config, {"feeds": {"messari": {"status": 404, "fails": 2}}}, now=T0, sleep=lambda s: None,
                        fetch=lambda u: (200, "<rss><channel></channel></rss>"))
        self.assertEqual(sorted(st["feeds"]), ["ok"])
        feeds = rss.load_config(SCRIPTS.parents[0] / "sources" / "rss.yaml")["feeds"]
        self.assertNotIn("messari", [f["name"] for f in feeds])           # D-041: Messari eliminado (404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
