#!/usr/bin/env python3
"""Autonomía por módulo (D-105, doc 38 §6): cada script crítico corre con SHOT_ROOT en una carpeta temporal vacía o
con datos mínimos, sin depender de las carpetas de otros módulos; mover una carpeta se resuelve en lib_paths sin
tocar el script; y ningún módulo migrado tiene rutas literales. unittest, sin red.

Uso: python 04_Config/scripts/test_modulos_autonomos.py
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import audit_gate  # noqa: E402
import lib_alerts  # noqa: E402
import lib_early_watch as ew  # noqa: E402
import lib_paths as P  # noqa: E402
import lib_sources_domain as domain  # noqa: E402

ROOT = SCRIPTS.parents[1]
NOW = 1_791_000_000
MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"


def load(name, root):
    """Carga el script con SHOT_ROOT = root (sus constantes de módulo se calculan al importar)."""
    with mock.patch.dict(os.environ, {"SHOT_ROOT": str(root), "TELEGRAM_BOT_TOKEN": "", "TELEGRAM_PUBLIC_CHAT_ID": ""}):
        spec = importlib.util.spec_from_file_location(f"{name}_autonomo", SCRIPTS / f"{name}.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return mod


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="autonomo_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.env = mock.patch.dict(os.environ, {"SHOT_ROOT": str(self.root)})
        self.env.start()
        self.addCleanup(self.env.stop)


class Interfaz(Base):
    def test_clave_desconocida_y_campo_faltante_fallan_explicito(self):
        with self.assertRaises(KeyError):
            P.path("no.existe")
        with self.assertRaises(KeyError):
            P.path("alerts.detail", mint="X")                       # falta ts
        self.assertEqual(P.path("alerts.all"), self.root / P.rel("alerts.all"))   # raíz leída en cada llamada
        self.assertEqual(P.path_str("early.watch", inst="b"), str(self.root / P.rel("early.watch", inst="b")))

    def test_register_idempotente_y_conflicto(self):
        with mock.patch.dict(P.PATHS):
            P.register("mod.x", "otra/carpeta/x.json")
            P.register("mod.x", "otra/carpeta/x.json")              # misma ruta: idempotente
            with self.assertRaises(ValueError):
                P.register("mod.x", "otra/carpeta/y.json")
        self.assertNotIn("mod.x", P.PATHS)

    def test_validate_repo_real_y_carpeta_vacia(self):
        self.assertEqual(P.validate(ROOT), [])                      # el repo cumple su propia tabla
        probs = P.validate(self.root)                               # vacío: solo faltan las no "pending"
        self.assertTrue(probs)
        self.assertTrue(all("no existe" in p for p in probs))
        self.assertFalse(any(k.startswith(("early.gate", "alerts.detail")) for k in (p.split(":")[0] for p in probs)))


class ScriptsAisladosSinOtrasCarpetas(Base):
    """Cada script crítico arranca con SHOT_ROOT vacío: ninguna carpeta ajena presente."""

    def test_script_97_y_98_importan_y_98_corre_sin_alertas(self):
        s97 = load("script_97_emit_alerts", self.root)
        self.assertEqual(s97.load_alerts(s97.ALL_ALERTS_FILE), [])
        self.assertEqual(s97.load_early_signals(), None)            # sin early/: sin bono, sin error
        s98 = load("script_98_trust_scheduler", self.root)
        self.assertIsNone(s98.main())                               # sin _all_alerts.json: sale limpio

    def test_script_116_sin_alertas_ni_claims(self):
        s116 = load("script_116_early_watch", self.root)
        self.assertEqual(s116.alerted_mints(self.root), set())
        self.assertEqual(s116.early_records(self.root), [])
        self.assertEqual(s116.resolve_min_age(self.root), s116.EARLY_MIN_AGE_MIN_DEFAULT)

    def test_early_review_y_orquestador_y_calendario_con_raiz_vacia(self):
        er = load("early_review", self.root)
        rep = er.run(self.root, source=None, now=NOW, dry_run=True)
        self.assertEqual(rep["gate"]["decision"], "sin_medir")
        (self.root / "04_Config" / "sources").mkdir(parents=True)
        shutil.copy(ROOT / "04_Config" / "sources" / "_bots.yaml", self.root / "04_Config" / "sources")
        orch = load("bot_orchestrator", self.root)
        doc = orch.run(self.root, NOW)                              # sin ningún diario de bots
        self.assertEqual(doc["merged_items"], 0)
        self.assertTrue(P.path("sources.orchestrator_state", self.root).exists())
        pc = load("bot_prelaunch_calendar", self.root)
        cal = pc.Calendar(self.root, {}, NOW, emit=False)           # sin calendario previo
        self.assertEqual(cal.assets, {})

    def test_un_modulo_roto_no_arrastra_a_otro(self):
        a = P.path("alerts.all", self.root)
        a.parent.mkdir(parents=True)
        a.write_text("{roto")                                       # el historial de alertas está corrupto
        s116 = load("script_116_early_watch", self.root)
        self.assertEqual(s116.alerted_mints(self.root), set())      # el early watch sigue (lectura no estricta)
        er = load("early_review", self.root)
        self.assertEqual(er.run(self.root, source=None, now=NOW, dry_run=True)["rows"], [])
        with self.assertRaises(lib_alerts.CorruptAlertsError):      # el emisor NO pisa un historial ilegible
            lib_alerts.read_alerts(a)


class MoverCarpetas(Base):
    """Mover una carpeta = cambiar UNA entrada de lib_paths; los scripts no se tocan."""

    def test_mover_alertas(self):
        moved = {"alerts.dir": ("datos_v2/alertas", "dir", False),
                 "alerts.all": ("datos_v2/alertas/_all_alerts.json", "file", False),
                 "alerts.detail": ("datos_v2/alertas/alert_{mint}_{ts}.json", "file", True)}
        with mock.patch.dict(P.PATHS, moved):
            lib_alerts.write_alerts([{"mint": MINT, "timestamp": "2026-10-05_000000"}], lib_alerts.all_path(self.root))
            lib_alerts.write_detail(MINT, "2026-10-05_000000", {"x": 1}, root=self.root)
            s116 = load("script_116_early_watch", self.root)
            self.assertEqual(s116.alerted_mints(self.root), {MINT})
            self.assertTrue((self.root / "datos_v2" / "alertas" / f"alert_{MINT}_2026-10-05_000000.json").exists())
            self.assertFalse(P.path("analisis.dir", self.root).exists())    # nada se escribió en la ruta vieja

    def test_mover_early_watch(self):
        moved = {"early.dir": ("datos_v2/early", "dir", False),
                 "early.watch": ("datos_v2/early/_watch_{inst}.json", "file", True),
                 "early.alerts_dir": ("datos_v2/early/reclamos", "dir", True),
                 "early.claim": ("datos_v2/early/reclamos/{mint}.json", "file", True),
                 "early.alerts_legacy": ("datos_v2/early/_early_alerts.json", "file", True)}
        with mock.patch.dict(P.PATHS, moved):
            ew.write_watch("a", {"instance": "a", "listener_intervals": [[NOW - 60, NOW]]}, self.root)
            claim = P.path("early.claim", self.root, mint=MINT)
            claim.parent.mkdir(parents=True)
            claim.write_text(json.dumps({"mint": MINT, "timestamp": "2026-10-05_000000"}))
            er = load("early_review", self.root)
            self.assertEqual(er.load_intervals(self.root), {"a": [[NOW - 60, NOW]]})
            self.assertEqual([r["mint"] for r in er.early_records(self.root)], [MINT])
            s116 = load("script_116_early_watch", self.root)
            self.assertEqual(s116.instance_paths("a")["watch"], "datos_v2/early/_watch_a.json")   # git add sigue

    def test_mover_fuentes(self):
        moved = {"sources.dir": ("datos_v2/fuentes", "dir", False),
                 "sources.bot": ("datos_v2/fuentes/{bot}", "dir", True)}
        with mock.patch.dict(P.PATHS, moved):
            import lib_sources_store as store
            rec = store.make_record("rss", "s", "news", f"CA {MINT}", ts=NOW - 60, seen=NOW - 60, title="t")
            domain.write_sources("rss", [rec], when=NOW, root=self.root)
            self.assertEqual(len(domain.read_sources("rss", root=self.root)), 1)
            self.assertTrue((self.root / "datos_v2" / "fuentes" / "rss").is_dir())
            self.assertEqual(store.merge(NOW, root=self.root), 1)


class SinRutasLiterales(unittest.TestCase):
    def test_modulos_migrados_sin_rutas_literales(self):
        hits = audit_gate.check_rutas(lambda p: (ROOT / p).read_text(encoding="utf-8"))
        self.assertEqual(hits, [], hits[:5])

    def test_la_compuerta_detecta_literales_y_respeta_excepciones(self):
        src = 'X = "' + audit_gate.DATA_ROOT + '/alerts"\n# "' + audit_gate.DATA_ROOT + '/ok" en comentario\n'
        src += 'def f():\n    """doc con ' + audit_gate.DATA_ROOT + '/x"""\n    return 1\n'
        self.assertEqual([n for n, _ in audit_gate.literal_paths(src)], [1])
        changed = {"04_Config/scripts/script_nuevo.py": [(1, "")], "04_Config/scripts/test_algo.py": [(1, "")],
                   "04_Config/scripts/lib_paths.py": [(1, "")]}
        hits = audit_gate.check_rutas(lambda p: src if p in changed else "", changed)
        self.assertEqual([(h["rule"], h["path"]) for h in hits],
                         [("ruta_literal_nueva", "04_Config/scripts/script_nuevo.py")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
