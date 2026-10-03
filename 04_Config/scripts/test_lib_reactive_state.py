#!/usr/bin/env python3
"""Tests del estado reactivo por polling (patrón #3): lib_reactive_state. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_reactive_state.py
"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_reactive_state as rsl  # noqa: E402

T0 = 1791000000
STATE = "02_Analisis/sources/rss/_state.json"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="reactive_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.got = []

    def put(self, rel, obj):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj), encoding="utf-8")
        return p

    def rs(self, now=T0, **kw):
        return rsl.ReactiveState(self.root, now=now, **kw)

    def cb(self, ev):
        self.got.append((ev["change"], ev["path"]))


class Reactivo(Base):
    def test_linea_de_base_cambio_y_persistencia(self):
        self.put(STATE, {"last_run": T0, "feeds": {"a": {"status": 200}}})
        rs = self.rs()
        rs.subscribe(STATE, self.cb, name="rss")
        self.assertEqual(rs.poll(), [])                                  # primera vez: línea de base, sin disparar
        self.put(STATE, {"last_run": T0 + 1200, "feeds": {"a": {"status": 404}}})
        ev = rs.poll()
        self.assertEqual([(e["change"], e["path"]) for e in ev], [("modified", STATE)])
        self.assertTrue(ev[0]["prev_sha"] and ev[0]["sha"] != ev[0]["prev_sha"])
        self.assertEqual(ev[0]["data"]["feeds"]["a"]["status"], 404)
        self.assertEqual(rs.poll(), [])                                  # sin cambios: nada
        p, before = self.root / STATE, (self.root / STATE).stat()
        self.put(STATE, {"last_run": T0 + 2400, "feeds": {"a": {"status": 503}}})    # mismo tamaño...
        os.utime(p, ns=(before.st_atime_ns, before.st_mtime_ns))                     # ...y mismo mtime (mismo tic)
        self.assertEqual([e["change"] for e in rs.poll()], ["modified"])  # huella "racy": se re-hashea igual
        saved = json.loads(rsl.state_path(self.root).read_text(encoding="utf-8"))
        self.assertIn(STATE, saved["subscriptions"]["rss"]["files"])
        again = self.rs(now=T0 + 60)                                     # otra corrida: carga la huella y no re-dispara
        again.subscribe(STATE, self.cb, name="rss")
        self.assertEqual(again.poll(), [])

    def test_glob_multi_instancia_creado_y_borrado(self):
        self.put("02_Analisis/sources/telegram/_state_a.json", {"last_run": T0})
        rs = self.rs()
        rs.subscribe("02_Analisis/sources/*/_state*.json", self.cb, name="estados")
        rs.poll()
        self.put("02_Analisis/sources/telegram/_state_b.json", {"last_run": T0})
        (self.root / "02_Analisis/sources/telegram/_state_a.json").unlink()
        rs.poll()
        self.assertEqual(self.got, [("created", "02_Analisis/sources/telegram/_state_b.json"),
                                    ("deleted", "02_Analisis/sources/telegram/_state_a.json")])
        fresh = rsl.ReactiveState(self.root, consumer="orchestrator", now=T0)
        fresh.subscribe("02_Analisis/sources/*/_state*.json", self.cb, name="todo", fire_initial=True)
        self.assertEqual([e["change"] for e in fresh.poll()], ["created"])
        self.assertTrue((self.root / "02_Analisis/sources/_reactive_state_orchestrator.json").exists())
        with self.assertRaises(ValueError):
            rsl.state_path(self.root, "../x")

    def test_keys_solo_dispara_si_cambia_lo_que_importa(self):
        self.put(STATE, {"last_run": T0, "feeds": {"a": {"status": 200, "checked_at": T0}}})
        rs = self.rs()
        rs.subscribe(STATE, self.cb, name="estado_fuentes", keys=["feeds.a.status"])
        rs.poll()
        self.put(STATE, {"last_run": T0 + 1200, "feeds": {"a": {"status": 200, "checked_at": T0 + 1200}}})
        self.assertEqual(rs.poll(), [])                                  # solo cambió el reloj
        self.put(STATE, {"last_run": T0 + 2400, "feeds": {"a": {"status": 503, "checked_at": T0 + 2400}}})
        self.assertEqual([e["change"] for e in rs.poll()], ["modified"])
        (self.root / STATE).write_text('{"last_run": 1, "feeds": {"a"', encoding="utf-8")   # push a medias
        self.assertEqual(rs.poll(), [])
        self.assertEqual(self.got, [("modified", STATE)])

    def test_callback_roto_repite_y_no_frena_a_los_demas(self):
        p = self.put(STATE, {"v": 1})
        calls = {"n": 0}

        def roto(ev):
            calls["n"] += 1
            if calls["n"] == 1:
                raise RuntimeError("consumidor caído")
        rs = self.rs()
        rs.subscribe(STATE, roto, name="roto")
        rs.subscribe(STATE, self.cb, name="sano")
        rs.poll()
        self.put(STATE, {"v": 2})
        first = rs.poll()
        self.assertEqual(sorted((e["subscriber"], "error" in e) for e in first), [("roto", True), ("sano", False)])
        second = rs.poll()                                               # al menos una vez: se repite solo el roto
        self.assertEqual([(e["subscriber"], e["change"], "error" in e) for e in second], [("roto", "modified", False)])
        self.assertEqual(rs.poll(), [])
        st = p.stat()
        os.utime(p, ns=(st.st_atime_ns, st.st_mtime_ns + 5_000_000_000))  # mtime nuevo, mismo contenido (checkout)
        self.assertEqual(rs.poll(), [])
        self.assertEqual(self.got, [("modified", STATE)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
