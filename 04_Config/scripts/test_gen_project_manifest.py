#!/usr/bin/env python3
"""gen_project_manifest (D-101): el manifiesto sale del repo real, sin rutas locales, y clasifica los scripts.

Uso: python 04_Config/scripts/test_gen_project_manifest.py
"""
import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import gen_project_manifest as gen  # noqa: E402

ROOT = SCRIPTS.parents[1]


class Manifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = gen.build(ROOT, now="2026-10-05T00:00:00Z")

    def test_sin_rutas_locales_y_scripts_de_workflows_existen(self):
        text = json.dumps(self.m)
        self.assertNotIn(":\\\\", text)                          # nada de D:\ ni C:\
        for w in self.m["workflows"]:
            for s in w["scripts"]:
                self.assertTrue((ROOT / s).exists(), f"{w['file']}: {s}")

    def test_clasificacion_de_scripts(self):
        st = {k: v["estado"] for k, v in self.m["scripts"].items()}
        self.assertEqual(st["script_116_early_watch"], "workflow")
        self.assertEqual(st["lib_scoring_young"], "importado")    # lo importa script_116
        self.assertEqual(st["script_99_prelaunch"], "sin_uso")    # su workflow está desactivado (if: false)
        self.assertEqual(sum(self.m["scripts_resumen"].values()), len(self.m["scripts"]))

    def test_retencion_y_manifest_al_dia(self):
        rows = {d["ruta"]: d for d in self.m["datos"]}
        self.assertEqual(rows["02_Analisis/sources/x_influencers/"]["retencion_dias"], 35)
        cur = json.loads((ROOT / gen.MANIFEST_REL).read_text(encoding="utf-8"))
        strip = lambda d: {k: v for k, v in d.items() if k != "generated_at"}   # noqa: E731
        self.assertEqual(strip(cur), strip(self.m), "correr gen_project_manifest.py")


if __name__ == "__main__":
    unittest.main(verbosity=2)
