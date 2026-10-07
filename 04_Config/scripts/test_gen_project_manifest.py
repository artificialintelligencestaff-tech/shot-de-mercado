#!/usr/bin/env python3
"""
test_gen_project_manifest.py — tests para gen_project_manifest (D-101).

Uso: python 04_Config/scripts/test_gen_project_manifest.py
"""
import json
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import gen_project_manifest as gen  # noqa: E402

REAL_ROOT = SCRIPTS.parents[1]


def copy_repo_subset(src_root, dst_root, patterns):
    """Copia solo los archivos/directorios necesarios para que gen.build funcione."""
    dst_root = Path(dst_root)
    for pat in patterns:
        for src in Path(src_root).glob(pat):
            rel = src.relative_to(src_root)
            dst = dst_root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_file():
                shutil.copy2(src, dst)
            else:
                shutil.copytree(src, dst, dirs_exist_ok=True)


class Manifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear root temporal con solo lo necesario
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_root = Path(cls.temp_dir.name)

        # Patrones mínimos para que gen.build funcione
        patterns = [
                    ".github/workflows/*.yml",
                    "04_Config/scripts/*.py",
                    "04_Config/sources/_bots.yaml",
                    "04_Config/recipes/*.yaml",
                    "02_Analisis/patrimonio/_inventario.json",
                    "02_Analisis/patrimonio/_retention.yaml",
                    "02_Analisis/sources/**/_retention.yaml",
                    "El cerebro de dios/README.md",
                    "tools/probe_fuentes.py",
                ]
        copy_repo_subset(REAL_ROOT, cls.temp_root, patterns)

        # build usa timestamp fijo para determinismo
        cls.m = gen.build(cls.temp_root, now="2026-10-05T00:00:00Z")

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def test_sin_rutas_locales_y_scripts_de_workflows_existen(self):
            text = json.dumps(self.m)
            # Verificar que no hay rutas Windows reales (D:\ o C:\) — no falsos positivos por \uXXXX en JSON
            self.assertNotIn("D:\\", text)
            self.assertNotIn("C:\\", text)
            for w in self.m["workflows"]:
                for s in w["scripts"]:
                    self.assertTrue((self.temp_root / s).exists(), f"{w['file']}: {s}")

    def test_clasificacion_de_scripts(self):
        st = {k: v["estado"] for k, v in self.m["scripts"].items()}
        self.assertEqual(st["script_116_early_watch"], "workflow")
        self.assertEqual(st["lib_scoring_young"], "importado")    # lo importa script_116
        self.assertEqual(st["script_99_prelaunch"], "sin_uso")    # su workflow está desactivado (if: false)
        self.assertEqual(sum(self.m["scripts_resumen"].values()), len(self.m["scripts"]))

    def test_retencion_y_manifest_al_dia(self):
        rows = {d["ruta"]: d for d in self.m["datos"]}
        self.assertEqual(rows["02_Analisis/sources/x_influencers/"]["retencion_dias"], 35)

        # Escribir manifiesto EN LA CARPETA TEMPORAL (no en el repo real)
        manifest_path = self.temp_root / gen.MANIFEST_REL
        manifest_path.write_text(json.dumps(self.m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

        # Leer el manifiesto ESCRITO EN TEMP (no el repo real)
        cur = json.loads(manifest_path.read_text(encoding="utf-8"))
        strip = lambda d: {k: v for k, v in d.items() if k != "generated_at"}   # noqa: E731
        self.assertEqual(strip(cur), strip(self.m), "correr gen_project_manifest.py en temp")


if __name__ == "__main__":
    unittest.main(verbosity=2)
