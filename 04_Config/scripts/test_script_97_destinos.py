#!/usr/bin/env python3
"""Tests de los destinos de Telegram de script_97 (unittest, sin red: requests.post simulado).

Uso: python 04_Config/scripts/test_script_97_destinos.py
"""
import importlib.util
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"


class FakeResponse:
    def __init__(self, status):
        self.status_code, self.text = status, "{}"


class DestinosTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="dest_")
        os.environ["SHOT_ROOT"] = self.tmp
        spec = importlib.util.spec_from_file_location("s97_dest", SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.m.TELEGRAM_BOT_TOKEN = "token-de-prueba"
        self.m.TELEGRAM_CHAT_ID = "111"
        self.m.TELEGRAM_PUBLIC_CHAT_ID = None
        self.posted, self.status = [], {}
        patcher = mock.patch.object(self.m.requests, "post", self.fake_post)   # se restaura solo
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("SHOT_ROOT", None)

    def fake_post(self, url, json=None, timeout=None):
        self.posted.append(json["chat_id"])
        return FakeResponse(self.status.get(json["chat_id"], 200))

    def test_sin_grupo_solo_chat_personal(self):
        self.assertEqual(self.m.telegram_destinations(), [("personal", "111")])
        self.assertTrue(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, ["111"])

    def test_con_grupo_envia_a_ambos(self):
        self.m.TELEGRAM_PUBLIC_CHAT_ID = "-100222"
        self.assertTrue(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, ["111", "-100222"])

    def test_grupo_vacio_o_igual_al_personal_no_duplica(self):
        for public in ("", "   ", "111"):
            self.m.TELEGRAM_PUBLIC_CHAT_ID = public
            self.assertEqual(self.m.telegram_destinations(), [("personal", "111")])

    def test_basta_un_destino_para_marcar_enviado(self):
        self.m.TELEGRAM_PUBLIC_CHAT_ID = "-100222"
        self.status = {"111": 400}
        self.assertTrue(self.m.send_telegram("hola"))           # el grupo lo recibió
        self.status = {"111": 400, "-100222": 403}
        self.assertFalse(self.m.send_telegram("hola"))          # ninguno lo recibió

    def test_solo_grupo_sin_chat_personal(self):
        self.m.TELEGRAM_CHAT_ID = None
        self.m.TELEGRAM_PUBLIC_CHAT_ID = "-100222"
        self.assertTrue(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, ["-100222"])

    def test_sin_token_no_envia(self):
        self.m.TELEGRAM_BOT_TOKEN = None
        self.m.TELEGRAM_PUBLIC_CHAT_ID = "-100222"
        self.assertFalse(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, [])

    def test_ops_chat_nunca_es_destino(self):
        os.environ["TELEGRAM_OPS_CHAT_ID"] = "999"
        try:
            self.m.TELEGRAM_PUBLIC_CHAT_ID = "-100222"
            self.assertNotIn("999", [c for _, c in self.m.telegram_destinations()])
        finally:
            os.environ.pop("TELEGRAM_OPS_CHAT_ID")


if __name__ == "__main__":
    unittest.main(verbosity=2)
