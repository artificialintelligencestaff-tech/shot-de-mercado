#!/usr/bin/env python3
"""Destinos de Telegram de script_98 / script_99 y hardening del bot (unittest, sin red).

- Trust updates (script_98) y pre-launch (script_99) van SOLO al grupo (TELEGRAM_PUBLIC_CHAT_ID).
- Ningún workflow pasa el chat personal deprecado (TELEGRAM_CHAT_ID).
- Workflows de mercado -> TELEGRAM_PUBLIC_CHAT_ID; bots de sistema -> TELEGRAM_OPS_CHAT_ID.
- El bot es solo emisor: ningún script de producción lee updates (getUpdates / webhooks / handlers).

Uso: python 04_Config/scripts/test_telegram_hardening.py
"""
import importlib.util
import os
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
PERSONAL, GRUPO = "111", "-100222"
MARKET_WORKFLOWS = {"pipeline_t0.yml", "trust_update.yml", "prelaunch.yml", "telegram_test_send.yml"}
OPS_WORKFLOWS = {"monitor_shadow_bot.yml", "health_check_bot.yml", "autorepair_bot.yml", "daily_summary_bot.yml"}
READ_PATTERNS = re.compile(r"getUpdates|setWebhook|deleteWebhook|CommandHandler|MessageHandler|start_polling|"
                           r"run_polling|infinity_polling|telebot|aiogram|telegram\.ext", re.IGNORECASE)


def workflow_scripts():
    """Scripts .py que corre algún workflow (producción)."""
    found = set()
    for wf in WORKFLOWS.glob("*.yml"):
        found |= set(re.findall(r"04_Config/scripts/(\w+\.py)", wf.read_text(encoding="utf-8")))
    return found


class DestinoGrupoTest(unittest.TestCase):
    def load(self, name):
        tmp = tempfile.mkdtemp(prefix="hard_")
        self.addCleanup(shutil.rmtree, tmp, True)
        env = mock.patch.dict(os.environ, {"SHOT_ROOT": tmp, "TELEGRAM_CHAT_ID": PERSONAL,
                                           "TELEGRAM_BOT_TOKEN": "token-de-prueba", "TELEGRAM_PUBLIC_CHAT_ID": GRUPO})
        env.start()
        self.addCleanup(env.stop)
        spec = importlib.util.spec_from_file_location(f"{name}_hard", SCRIPTS / f"{name}.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        posted = []
        patcher = mock.patch.object(m.requests, "post",
                                    lambda url, json=None, timeout=None: posted.append(json["chat_id"]) or
                                    type("R", (), {"status_code": 200, "text": "{}"})())
        patcher.start()
        self.addCleanup(patcher.stop)
        return m, posted

    def check_only_group(self, name):
        m, posted = self.load(name)
        self.assertTrue(m.send_telegram("hola"))
        self.assertEqual(posted, [GRUPO])                       # nunca el chat personal
        self.assertFalse(hasattr(m, "TELEGRAM_CHAT_ID"))
        m.TELEGRAM_PUBLIC_CHAT_ID = None
        self.assertFalse(m.send_telegram("hola"))               # sin grupo: no envía y no falla
        self.assertEqual(posted, [GRUPO])

    def test_trust_updates_solo_al_grupo(self):
        self.check_only_group("script_98_trust_scheduler")

    def test_prelaunch_solo_al_grupo(self):
        self.check_only_group("script_99_prelaunch")


class WorkflowsTest(unittest.TestCase):
    def telegram_env(self, wf):
        d = yaml.safe_load((WORKFLOWS / wf).read_text(encoding="utf-8"))
        return {k for j in d["jobs"].values() for s in j["steps"] for k in (s.get("env") or {}) if k.startswith("TELEGRAM")}

    def test_ningun_workflow_pasa_el_chat_personal(self):
        for wf in WORKFLOWS.glob("*.yml"):
            self.assertNotIn("TELEGRAM_CHAT_ID", self.telegram_env(wf.name), wf.name)

    def test_mercado_al_grupo_y_sistema_a_ops(self):
        for wf in MARKET_WORKFLOWS:
            self.assertIn("TELEGRAM_PUBLIC_CHAT_ID", self.telegram_env(wf), wf)
            self.assertNotIn("TELEGRAM_OPS_CHAT_ID", self.telegram_env(wf), wf)
        for wf in OPS_WORKFLOWS:
            self.assertIn("TELEGRAM_OPS_CHAT_ID", self.telegram_env(wf), wf)
            self.assertNotIn("TELEGRAM_PUBLIC_CHAT_ID", self.telegram_env(wf), wf)


class SoloEmisorTest(unittest.TestCase):
    def test_produccion_no_lee_updates_ni_comandos(self):
        scripts = workflow_scripts() | {"lib_ops.py"}
        self.assertIn("script_97_emit_alerts.py", scripts)
        for name in sorted(scripts):
            text = (SCRIPTS / name).read_text(encoding="utf-8")
            self.assertIsNone(READ_PATTERNS.search(text), f"{name} lee updates/comandos de Telegram")
            for call in re.findall(r"api\.telegram\.org/bot\{[^}]+\}/(\w+)", text):
                self.assertEqual(call, "sendMessage", f"{name} llama a {call}")

    def test_ningun_script_de_produccion_lee_el_chat_personal(self):
        for name in sorted(workflow_scripts() | {"lib_ops.py"}):
            text = (SCRIPTS / name).read_text(encoding="utf-8")
            self.assertNotRegex(text, r"getenv\(\s*[\"']TELEGRAM_CHAT_ID[\"']|environ(\.get)?\(?\[?\s*[\"']TELEGRAM_CHAT_ID",
                                name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
