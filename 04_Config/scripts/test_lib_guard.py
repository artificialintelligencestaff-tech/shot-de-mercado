#!/usr/bin/env python3
"""
test_lib_guard.py — tests para lib_guard.

Uso: python -m unittest 04_Config/scripts/test_lib_guard.py -v
"""
import json
import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_guard  # noqa: E402


class LibGuard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear repo temporal para tests de gitlinks
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_root = Path(cls.temp_dir.name)
        # Inicializar git
        subprocess = __import__("subprocess")
        subprocess.run(["git", "init"], cwd=cls.temp_root, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=cls.temp_root, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=cls.temp_root, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def _write_file(self, rel_path: str, content: str):
        """Escribe un archivo en el repo temporal."""
        path = self.temp_root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return str(path.relative_to(self.temp_root))

    def test_gitlink_detectado(self):
        """Un gitlink (modo 160000) debe ser detectado."""
        # Crear un archivo normal y commitear
        self._write_file("normal.txt", "content")
        subprocess = __import__("subprocess")
        subprocess.run(["git", "add", "normal.txt"], cwd=self.temp_root, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=self.temp_root, capture_output=True)

        # Crear un gitlink (submódulo)
        subdir = self.temp_root / "submod"
        subdir.mkdir()
        subprocess.run(["git", "init"], cwd=subdir, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=subdir, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=subdir, capture_output=True)
        (subdir / "file.txt").write_text("sub")
        subprocess.run(["git", "add", "."], cwd=subdir, capture_output=True)
        subprocess.run(["git", "commit", "-m", "sub"], cwd=subdir, capture_output=True)

        # Agregar como submódulo al repo principal
        subprocess.run(["git", "submodule", "add", str(subdir), "submod"], cwd=self.temp_root, capture_output=True)
        subprocess.run(["git", "commit", "-m", "add submod"], cwd=self.temp_root, capture_output=True)

        # Verificar detección
        issues = lib_guard.check_gitlinks(cwd=str(self.temp_root))
        gitlink_issues = [i for i in issues if i["tipo"] == "gitlink"]
        self.assertEqual(len(gitlink_issues), 1)
        self.assertEqual(gitlink_issues[0]["ruta"], "submod")

    def test_sin_gitlinks_ok(self):
        """Sin gitlinks, check_gitlinks debe retornar lista vacía."""
        # Crear repo limpio en nuevo directorio
        temp_root2 = self.temp_root / "clean_repo"
        temp_root2.mkdir()
        subprocess = __import__("subprocess")
        subprocess.run(["git", "init"], cwd=temp_root2, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=temp_root2, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=temp_root2, capture_output=True)
        (temp_root2 / "file.txt").write_text("content")
        subprocess.run(["git", "add", "file.txt"], cwd=temp_root2, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=temp_root2, capture_output=True)

        issues = lib_guard.check_gitlinks(cwd=str(temp_root2))
        gitlink_issues = [i for i in issues if i["tipo"] == "gitlink"]
        self.assertEqual(len(gitlink_issues), 0)

    def test_ruta_literal_detectada(self):
        """Ruta literal '02_Analisis/' en .py debe ser detectada."""
        content = '''
def foo():
    path = "02_Analisis/alerts/algo.json"
    return path
'''
        f = self._write_file("test_script.py", content)
        issues = lib_guard.check_rutas_literales([f], cwd=str(self.temp_root))
        ruta_issues = [i for i in issues if i["tipo"] == "ruta_literal"]
        self.assertEqual(len(ruta_issues), 1)
        self.assertIn("02_Analisis/alerts/algo.json", ruta_issues[0]["detalle"])

    def test_ruta_literal_en_lib_paths_ok(self):
        """lib_paths.py está exento de la regla de rutas literales."""
        content = '''
PATHS = {
    "alerts.all": "02_Analisis/alerts/_all_alerts.json",
}
'''
        f = self._write_file("lib_paths.py", content)
        issues = lib_guard.check_rutas_literales([f], cwd=str(self.temp_root))
        ruta_issues = [i for i in issues if i["tipo"] == "ruta_literal"]
        self.assertEqual(len(ruta_issues), 0, "lib_paths.py debe ser exento")

    def test_secreto_hardcodeado_detectado(self):
        """Secreto hardcodeado debe ser detectado."""
        content = 'HELIUS_API_KEY = "abc123def456ghi789jkl"'
        f = self._write_file("config.py", content)
        issues = lib_guard.check_secretos_fuera_dominio([f], {}, cwd=str(self.temp_root))
        secret_issues = [i for i in issues if i["tipo"] == "secreto_hardcodeado"]
        self.assertEqual(len(secret_issues), 1)
        self.assertIn("HELIUS_API_KEY", secret_issues[0]["detalle"])

    def test_secreto_desde_entorno_ok(self):
        """Secreto leído desde os.environ NO debe ser detectado."""
        content = 'HELIUS_API_KEY = os.environ.get("HELIUS_API_KEY")'
        f = self._write_file("config.py", content)
        issues = lib_guard.check_secretos_fuera_dominio([f], {}, cwd=str(self.temp_root))
        secret_issues = [i for i in issues if i["tipo"] == "secreto_hardcodeado"]
        self.assertEqual(len(secret_issues), 0)

    def test_archivo_limpio_ok(self):
        """Archivo sin problemas pasa todos los checks."""
        content = '''
import os
from lib_paths import path

def main():
    p = path("alerts.all")
    print(p)
'''
        f = self._write_file("clean_script.py", content)
        issues = lib_guard.check([f], {}, cwd=str(self.temp_root))
        self.assertTrue(issues["ok"], f"Issues encontrados: {issues['issues']}")


if __name__ == "__main__":
    unittest.main(verbosity=2)