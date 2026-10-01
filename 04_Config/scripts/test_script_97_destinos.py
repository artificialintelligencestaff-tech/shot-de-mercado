#!/usr/bin/env python3
"""Tests del destino de Telegram de script_97 (unittest, sin red: requests.post simulado).

Desde el 30/09 (Dirección) las alertas de mercado van SOLO al grupo (TELEGRAM_PUBLIC_CHAT_ID). El chat
personal (TELEGRAM_CHAT_ID) está deprecado: aunque el secret exista, no recibe nada.

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
PERSONAL, GRUPO = "111", "-100222"


class FakeResponse:
    def __init__(self, status):
        self.status_code, self.text = status, "{}"


class DestinosTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="dest_")
        # El chat personal EXISTE en el entorno: el script no debe usarlo nunca
        self.env = mock.patch.dict(os.environ, {"SHOT_ROOT": self.tmp, "TELEGRAM_CHAT_ID": PERSONAL,
                                                "TELEGRAM_BOT_TOKEN": "token-de-prueba",
                                                "TELEGRAM_PUBLIC_CHAT_ID": GRUPO})
        self.env.start()
        self.addCleanup(self.env.stop)
        spec = importlib.util.spec_from_file_location("s97_dest", SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.posted, self.status, self.slept = [], {}, []
        for target, attr, fake in ((self.m.requests, "post", self.fake_post), (self.m.time, "sleep", self.slept.append)):
            patcher = mock.patch.object(target, attr, fake)                    # se restaura solo
            patcher.start()
            self.addCleanup(patcher.stop)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def fake_post(self, url, json=None, timeout=None):
        self.posted.append(json["chat_id"])
        return FakeResponse(self.status.get(json["chat_id"], 200))

    def test_no_envia_al_chat_personal_aunque_este_definido(self):
        self.assertTrue(self.m.send_telegram("hola"))
        self.assertNotIn(PERSONAL, self.posted)
        self.assertFalse(hasattr(self.m, "TELEGRAM_CHAT_ID"))   # el script ya no lee el secret personal

    def test_envia_solo_al_grupo(self):
        self.assertEqual(self.m.telegram_destinations(), [("grupo", GRUPO)])
        self.assertTrue(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, [GRUPO])
        self.assertEqual(self.slept, [])                        # un solo destino: sin pausa

    def test_sin_grupo_no_envia_y_no_falla(self):
        for public in (None, "", "   "):
            self.m.TELEGRAM_PUBLIC_CHAT_ID = public
            self.assertEqual(self.m.telegram_destinations(), [])
            self.assertFalse(self.m.send_telegram("hola"))      # imprime por consola, no lanza
        self.assertEqual(self.posted, [])

    def test_sin_token_no_envia(self):
        self.m.TELEGRAM_BOT_TOKEN = None
        self.assertFalse(self.m.send_telegram("hola"))
        self.assertEqual(self.posted, [])

    def test_falla_del_grupo_se_informa(self):
        self.status = {GRUPO: 403}
        self.assertFalse(self.m.send_telegram("hola"))

    def test_test_send_solo_apunta_al_grupo(self):
        sent = []
        orig = self.m.send_telegram_to
        self.m.send_telegram_to = lambda label, cid, text: sent.append((label, text)) or orig(label, cid, text)
        self.assertEqual(self.m.main(["--test-send"]), 0)
        self.assertEqual(self.posted, [GRUPO])
        self.assertEqual([label for label, _ in sent], ["grupo"])
        self.assertIn("PRUEBA DE ENVÍO", sent[0][1])
        self.assertIn("No es una alerta", sent[0][1])
        self.assertIn("Destinos configurados: grupo", sent[0][1])
        self.assertFalse(os.path.exists(self.m.ALL_ALERTS_FILE))   # no toca alertas

    def test_test_send_falla_sin_grupo_o_si_el_grupo_falla(self):
        self.status = {GRUPO: 403}
        self.assertEqual(self.m.test_send(), 1)
        self.m.TELEGRAM_PUBLIC_CHAT_ID = None
        self.posted.clear()
        self.assertEqual(self.m.test_send(), 1)
        self.assertEqual(self.posted, [])

    def test_ops_chat_nunca_es_destino(self):
        with mock.patch.dict(os.environ, {"TELEGRAM_OPS_CHAT_ID": "999"}):
            self.assertNotIn("999", [c for _, c in self.m.telegram_destinations()])


if __name__ == "__main__":
    unittest.main(verbosity=2)
