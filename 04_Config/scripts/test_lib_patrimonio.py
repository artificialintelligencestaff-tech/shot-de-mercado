#!/usr/bin/env python3
"""Tests de lib_patrimonio (D-087): el inventario real es consistente con el disco y check() detecta lo que falta.

Uso: python 04_Config/scripts/test_lib_patrimonio.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_patrimonio as pat  # noqa: E402

REPO = SCRIPTS.parents[1]


class TestPatrimonio(unittest.TestCase):
    def test_1_inventario_real_consistente(self):
        self.assertEqual(pat.check(REPO), [])                              # cubre todo 02_Analisis/ y el esquema
        doc = pat.load(REPO)
        rutas = {e["ruta"] for e in doc["entradas"]}
        for sub in pat.CATEGORIAS:                                         # el árbol de D-087 existe
            self.assertIn(f"02_Analisis/patrimonio/{sub}/", rutas)
            self.assertTrue((REPO / "02_Analisis" / "patrimonio" / sub / "README.md").is_file())
        self.assertTrue({"02_Analisis/sources/", "02_Analisis/prelaunch/", "02_Analisis/events/",
                         "02_Analisis/alerts/"} <= rutas)
        res = pat.resumen(REPO, doc)
        self.assertEqual(sum(r["entradas"] for r in res.values()), len(doc["entradas"]))

    def test_2_check_detecta_problemas(self):
        tmp = Path(tempfile.mkdtemp(prefix="patrimonio_"))
        try:
            (tmp / "02_Analisis" / "viva").mkdir(parents=True)
            (tmp / "02_Analisis" / "nueva_sin_anotar").mkdir()
            (tmp / "02_Analisis" / "viva" / "x.json").write_text("{}", encoding="utf-8")
            (tmp / "02_Analisis" / "_viejo.json.bak2").write_text("{}", encoding="utf-8")    # backups: se ignoran
            base = {"categorias": {c: "-" for c in pat.CATEGORIAS}}
            ok = {"ruta": "02_Analisis/viva/", "categoria": "cuantitativo", "estado": "vivo", "dueno": "w",
                  "formato": "json", "que": "q"}
            doc = {**base, "entradas": [ok, {**ok, "ruta": "02_Analisis/futura/", "estado": "futuro"},
                                        {**ok, "ruta": "02_Analisis/nueva_sin_anotar/"}]}
            self.assertEqual(pat.check(tmp, doc), [])
            res = pat.resumen(tmp, doc)
            self.assertEqual((res["cuantitativo"]["entradas"], res["cuantitativo"]["archivos"]), (3, 1))
            bad = {**base, "entradas": [ok, {**ok, "ruta": "02_Analisis/legado_borrado/", "estado": "legado"},
                                        {**ok, "ruta": "02_Analisis/viva", "categoria": "otra"},
                                        {**ok, "ruta": "fuera/de/analisis", "estado": "futuro"},
                                        {"ruta": "02_Analisis/incompleta/"}]}
            problems = pat.check(tmp, bad)
            joined = "\n".join(problems)
            self.assertIn("legado_borrado/: estado legado pero la ruta no existe", joined)
            self.assertIn("ruta repetida", joined)
            self.assertIn("categoría desconocida", joined)
            self.assertIn("dentro de 02_Analisis/", joined)
            self.assertIn("incompleta/: faltan", joined)
            self.assertIn("02_Analisis/nueva_sin_anotar: no figura en el inventario", joined)
            self.assertNotIn("bak2", joined)
            self.assertIn("categorias debe ser", "\n".join(pat.check(tmp, {**bad, "categorias": {"x": 1}})))
            (tmp / "02_Analisis" / "patrimonio").mkdir()
            (tmp / "02_Analisis" / "patrimonio" / "_inventario.json").write_text("{roto", encoding="utf-8")
            self.assertTrue(pat.check(tmp)[0].startswith("inventario ilegible"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
