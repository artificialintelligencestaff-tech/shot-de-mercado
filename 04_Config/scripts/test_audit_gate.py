#!/usr/bin/env python3
"""Tests de las compuertas deterministas de auditoría (Ola 3): audit_gate. unittest, sin red ni git real.

Uso: python 04_Config/scripts/test_audit_gate.py
"""
import hashlib
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import audit_gate as ag  # noqa: E402

F = "--" + "force"                       # armado por partes, como en audit_gate
TOKEN = "123456789:" + "A" * 35
CHAT = "TELEGRAM_" + "CHAT_ID"


def diff(path, added, new=False, start=1):
    head = f"diff --git a/{path} b/{path}\n" + ("--- /dev/null\n" if new else f"--- a/{path}\n") + f"+++ b/{path}\n"
    return head + f"@@ -0,0 +{start},{len(added)} @@\n" + "".join(f"+{x}\n" for x in added)


class Prohibidos(unittest.TestCase):
    def test_detecta_lo_prohibido_en_lineas_agregadas(self):
        d = (diff(".github/workflows/x.yml", ["      - run: git push " + F + " origin main", "      - run: git reset --hard HEAD~1"])
             + diff("04_Config/scripts/bot_x.py", ['subprocess.run(["git", "push", "' + F + '"])',
                                                    'subprocess.run(["git", "reset", "--hard"])',
                                                    f'chat = os.environ["{CHAT}"]'])
             + diff("El cerebro de dios/notas.md", [f"el token es {TOKEN}"])
             + diff("deploy/.env", ["X=1"], new=True))
        hits = {(h["rule"], h["path"]) for h in ag.scan(d)}
        self.assertEqual(hits, {("force_push", ".github/workflows/x.yml"), ("reset_hard", ".github/workflows/x.yml"),
                                ("force_push", "04_Config/scripts/bot_x.py"), ("reset_hard", "04_Config/scripts/bot_x.py"),
                                ("telegram_chat_id", "04_Config/scripts/bot_x.py"),
                                ("telegram_bot_token", "El cerebro de dios/notas.md"),
                                ("env_file", "deploy/.env")})

    def test_no_denuncia_reglas_comentarios_tests_ni_datos(self):
        d = (diff("El cerebro de dios/22.md", ["- Nunca " + F + " ni reset --hard; " + CHAT + " deprecado"])
             + diff("04_Config/scripts/bot_y.py", ["# nunca " + F + " ni reset --hard",
                                                   '    """git_commit: pull --rebase y push con reintentos, nunca ' + F + '."""',
                                                   'ops = os.environ.get("TELEGRAM_OPS_CHAT_ID")'])
             + diff("04_Config/scripts/test_telegram_hardening.py", [f'self.assertNotIn("{CHAT}", text)'])
             + diff(".github/workflows/z.yml", ["# sin " + F + " de ningún tipo"])
             + diff("02_Analisis/sources/x/2026-10-03.jsonl", [f'{{"t": "{TOKEN}"}}']))
        self.assertEqual(ag.scan(d), [])

    def test_parser_de_diff_numera_lineas_y_ve_archivos_nuevos(self):
        d = ("diff --git a/a.py b/a.py\n--- a/a.py\n+++ b/a.py\n@@ -10,2 +10,3 @@\n ctx\n-viejo\n+nuevo1\n+nuevo2\n"
             "diff --git a/b.py b/b.py\n--- /dev/null\n+++ b/b.py\n@@ -0,0 +1 @@\n+hola\n"
             "diff --git a/c.py b/c.py\n--- a/c.py\n+++ /dev/null\n@@ -1 +0,0 @@\n-borrado\n")
        lines, new = ag.added_lines(d)
        self.assertEqual(lines, {"a.py": [(11, "nuevo1"), (12, "nuevo2")], "b.py": [(1, "hola")]})
        self.assertEqual(new, {"b.py"})


class Doc35YProduccion(unittest.TestCase):
    def test_doc35_contra_blobs_y_actualizacion(self):
        blobs = {"a.py": b"print(1)\n", "b.yml": b"on: push\n"}
        ok_a, ok_b = (hashlib.sha256(blobs[k]).hexdigest() for k in ("a.py", "b.yml"))
        z0, z1, z2 = "0" * 64, "1" * 64, "2" * 64
        text = (f"| `a.py` | uno | producción | `{ok_a}` |\n"
                f"| `b.yml` | dos | producción | `{z0}` |\n"
                f"| `c.py` | tres | rama | `{z1}` |\n"
                f"| `viejo.py` | cuatro | borrado | `{z2}` |\n")
        bad = ag.check_doc35(text, blobs.get)
        self.assertEqual([(b["path"], b["problem"]) for b in bad], [("b.yml", "hash distinto"),
                                                                   ("c.py", "no existe en el commit")])
        fixed = ag.update_doc35(text, blobs.get)
        self.assertEqual([b["path"] for b in ag.check_doc35(fixed, blobs.get)], ["c.py"])
        self.assertIn(ok_b, fixed)

    def test_produccion_por_doc35_y_por_workflows(self):
        files = {".github/workflows/w.yml": "run: python 04_Config/scripts/bot_a.py",
                 "04_Config/scripts/bot_a.py": "import json\nimport lib_b\n",
                 "04_Config/scripts/lib_b.py": "from lib_c import x\n",
                 "04_Config/scripts/lib_c.py": "import os\n",
                 "04_Config/scripts/suelto.py": "import lib_b\n"}
        closure = ag.workflow_closure(files.get, lambda: [".github/workflows/w.yml"])
        self.assertEqual(closure, {"04_Config/scripts/bot_a.py", "04_Config/scripts/lib_b.py",
                                   "04_Config/scripts/lib_c.py"})
        doc = f"| `04_Config/scripts/script_97.py` | emisor | producción | `{'3' * 64}` |\n"
        t = ag.touched(["04_Config/scripts/lib_c.py", "04_Config/scripts/script_97.py", "04_Config/scripts/suelto.py",
                        ".github/workflows/w.yml", "02_Analisis/sources/x/_state.json"], doc, closure)
        self.assertEqual(t["production"], ["04_Config/scripts/lib_c.py", "04_Config/scripts/script_97.py"])
        self.assertEqual((t["workflows"], t["data"]), ([".github/workflows/w.yml"], ["02_Analisis/sources/x/_state.json"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
