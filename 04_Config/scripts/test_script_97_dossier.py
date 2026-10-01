#!/usr/bin/env python3
"""Tests de la integración del dossier (script_113) en la emisión (script_97). unittest, sin red.

Uso: python 04_Config/scripts/test_script_97_dossier.py
Cada test trabaja en un SHOT_ROOT temporal y con requests.post simulado: nunca toca el repo ni Telegram.
"""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"
GRUPO = "-100222"
MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
NOW = datetime.now(timezone.utc)


def candidate():
    """Candidato real en forma: score ≥ 56, puntuado ahora, par de 2 h, datos completos de DexScreener."""
    return {"source": "pumpportal",
            "token": {"mint": MINT, "symbol": "TEST_CAT", "name": "Test Cat",
                      "traderPublicKey": "K6Eh9fwKkrhVNq6SpRtJn7F4Myi3HUst5QP8x5BKHnR", "pool": "pump"},
            "dexscreener": {"priceUsd": 0.0123, "liquidityUsd": 141632.8, "volume24hUsd": 201003.7,
                            "marketCapUsd": 9844684.6, "priceChange24h": 120.0, "dexId": "pumpswap",
                            "pairAddress": "B6ELT7HZ2p4AWEWnXbM7B6DtuVJET8insnTxLaWUVh9k",
                            "volume_m5": 1500.0, "volume_h1": 9000.0, "txns_m5_buys": 30, "txns_m5_sells": 10,
                            "txns_h1_buys": 200, "txns_h1_sells": 150, "priceChange_m5": 1.0, "priceChange_h1": 4.0,
                            "pairCreatedAt": int((NOW - timedelta(minutes=120)).timestamp() * 1000)},
            "score": 72, "reasons": ["MCap > $1M", "Volumen alto", "Liquidez alta", "Pump 24h"],
            "detected_at": NOW.isoformat(timespec="seconds"), "scoring_version": "7.2.1"}


class Response:
    def __init__(self, status=200, text="{}"):
        self.status_code, self.text = status, text


class DossierEnEmision(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="s97doc_")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.env = {"SHOT_ROOT": self.tmp, "TELEGRAM_BOT_TOKEN": "token-de-prueba", "TELEGRAM_PUBLIC_CHAT_ID": GRUPO,
                    "DOSSIER_LIVE": "false", "SHADOW_MODE": "false", "PAUSE_EMISSIONS": "false"}
        root = Path(self.tmp) / "02_Analisis"
        (root / "shadow_v4").mkdir(parents=True)
        (root / "alerts").mkdir(parents=True)
        (root / "shadow_v4" / "_accumulated.json").write_text(json.dumps({MINT: candidate()}), encoding="utf-8")
        (root / "alerts" / "_all_alerts.json").write_text("[]", encoding="utf-8")
        self.alerts_file = root / "alerts" / "_all_alerts.json"
        self.posts = []
        self.status = {"sendDocument": 200, "sendMessage": 200}

    def fake_post(self, url, json=None, data=None, files=None, timeout=None):
        method = url.rsplit("/", 1)[-1]
        call = {"method": method, "json": json, "data": data}
        if files:
            name, handle, ctype = files["document"]
            call["file"] = (name, handle.read().decode("utf-8"), ctype)
        self.posts.append(call)
        return Response(self.status[method], "Bad Request" if self.status[method] != 200 else "{}")

    def run_main(self, **env):
        with mock.patch.dict(os.environ, {**self.env, **env}):
            spec = importlib.util.spec_from_file_location("s97_dossier_test", SCRIPT)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            with mock.patch.object(m.requests, "post", self.fake_post), mock.patch.object(m.time, "sleep", lambda s: None):
                self.assertEqual(m.main([]), 0)
        self.m = m
        return json.loads(self.alerts_file.read_text(encoding="utf-8"))

    def dossier_file(self):
        return Path(self.tmp) / "02_Analisis" / "dossiers" / "solana" / f"{MINT}.md"

    def test_sombra_genera_el_dossier_y_no_envia_nada(self):
        alerts = self.run_main(SHADOW_MODE="true")
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["status"], "shadow")
        self.assertIs(alerts[0]["telegram_sent"], False)
        self.assertEqual(alerts[0]["dossier"], f"02_Analisis/dossiers/solana/{MINT}.md")
        self.assertTrue(self.dossier_file().exists())
        self.assertTrue(self.dossier_file().with_suffix(".json").exists())
        self.assertEqual(self.posts, [])                                   # nada sale a Telegram
        text = self.dossier_file().read_text(encoding="utf-8")
        self.assertLess(text.index("## 🛒 1."), text.index("## 📊 2."))    # la compra va primero

    def test_fuera_de_sombra_envia_el_dossier_con_send_document(self):
        alerts = self.run_main()
        self.assertEqual([p["method"] for p in self.posts], ["sendDocument"])
        post = self.posts[0]
        self.assertEqual(post["data"]["chat_id"], GRUPO)
        self.assertEqual(post["data"]["parse_mode"], "Markdown")
        name, content, ctype = post["file"]
        self.assertEqual((name, ctype), ("dossier_TESTCAT_9BB6NFEc.md", "text/markdown"))
        self.assertTrue(content.startswith("# Test Cat (TEST_CAT) — dossier"))
        self.assertTrue(post["data"]["caption"].startswith("🚨 *SHOT DE MERCADO*"))
        self.assertEqual((alerts[0]["status"], alerts[0]["telegram_sent"], alerts[0]["dossier_sent"]),
                         ("active_tracking", True, True))

    def test_caption_se_trunca_a_1024_sin_romper_el_markdown(self):
        self.run_main()
        caption = self.posts[0]["data"]["caption"]
        msg, _ = self.m.format_alert_message(candidate())
        self.assertGreater(len(msg), 1024)                                 # la alerta real no entra entera
        self.assertLessEqual(len(caption), 1024)
        self.assertTrue(caption.endswith(self.m.CAPTION_SUFFIX))
        self.assertTrue(self.m._markdown_balanced(caption))
        blocks = caption[:-len(self.m.CAPTION_SUFFIX)].split("\n\n")
        self.assertTrue(blocks[0].startswith("🚨 *SHOT DE MERCADO*"))
        for block in blocks:                                               # bloques enteros, sin cortes
            self.assertIn(block, msg)
        self.assertIn("🛒 *CÓMO ADQUIRIRLO*", caption)                     # la compra, completa, siempre
        for step in range(1, 9):
            self.assertIn(f"\n{step}. ", caption)
        self.assertIn("8. Confirmar la transacción en Solscan", caption)

    def test_fallback_al_mensaje_si_falla_send_document(self):
        self.status["sendDocument"] = 400
        alerts = self.run_main()
        self.assertEqual([p["method"] for p in self.posts], ["sendDocument", "sendMessage"])
        msg, _ = self.m.format_alert_message(candidate())
        self.assertEqual(self.posts[1]["json"]["text"], msg)               # el mensaje completo, sin cortar
        self.assertEqual(self.posts[1]["json"]["chat_id"], GRUPO)
        self.assertEqual((alerts[0]["telegram_sent"], alerts[0]["dossier_sent"]), (True, False))

    def test_si_el_dossier_falla_la_alerta_sale_igual(self):
        with mock.patch.dict(os.environ, self.env):
            spec = importlib.util.spec_from_file_location("s97_dossier_fail", SCRIPT)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        broken = mock.Mock()
        broken.load_alert_data.side_effect = RuntimeError("falla simulada")
        with mock.patch.dict(os.environ, self.env), mock.patch.object(m, "load_dossier_builder", return_value=broken), \
                mock.patch.object(m.requests, "post", self.fake_post), mock.patch.object(m.time, "sleep", lambda s: None):
            self.assertEqual(m.main([]), 0)
        alerts = json.loads(self.alerts_file.read_text(encoding="utf-8"))
        self.assertEqual([p["method"] for p in self.posts], ["sendMessage"])
        self.assertEqual((alerts[0]["telegram_sent"], alerts[0]["dossier_sent"]), (True, False))
        self.assertNotIn("dossier", alerts[0])

    def test_sin_builder_la_alerta_sale_igual(self):
        with mock.patch.dict(os.environ, self.env):
            spec = importlib.util.spec_from_file_location("s97_dossier_none", SCRIPT)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        with mock.patch.dict(os.environ, self.env), mock.patch.object(m, "load_dossier_builder", return_value=None), \
                mock.patch.object(m.requests, "post", self.fake_post), mock.patch.object(m.time, "sleep", lambda s: None):
            self.assertEqual(m.main([]), 0)
        self.assertEqual([p["method"] for p in self.posts], ["sendMessage"])


class Caption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("s97_caption", SCRIPT)
        cls.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.m)

    def test_mensaje_corto_queda_igual(self):
        self.assertEqual(self.m.document_caption("🚨 *corto*\nlínea"), "🚨 *corto*\nlínea")

    def test_nunca_supera_el_limite(self):
        for n in (1025, 2000, 5000):
            text = "\n".join(f"• línea {i} con *negrita* y `codigo`" for i in range(n // 30 + 1))
            caption = self.m.document_caption(text)
            self.assertLessEqual(len(caption), 1024)
            self.assertTrue(self.m._markdown_balanced(caption))

    def test_no_deja_entidades_abiertas(self):
        # Una línea con un backtick sin cerrar (dato roto) no puede quedar al final del caption
        text = "🚨 *A*\n" + "x" * 900 + "\n`roto\n" + "y" * 400
        caption = self.m.document_caption(text)
        self.assertNotIn("`roto", caption)
        self.assertTrue(self.m._markdown_balanced(caption))

    def test_bloque_de_compra_completo_tambien_en_evm(self):
        c = candidate()
        c.update(chain="base")
        c["token"]["mint"] = "0x" + "a" * 40
        c["dexscreener"]["pairAddress"] = "0x" + "b" * 40
        msg, _ = self.m.format_alert_message(c)
        caption = self.m.document_caption(msg)
        self.assertLessEqual(len(caption), 1024)
        self.assertIn("🛒 *CÓMO ADQUIRIRLO* — Base", caption)
        self.assertIn("8. Confirmar la transacción en BaseScan", caption)

    def test_escapes_no_cuentan_como_entidades(self):
        self.assertTrue(self.m._markdown_balanced(r"PEPE\_CAT *ok*"))
        self.assertFalse(self.m._markdown_balanced("*abierta"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
