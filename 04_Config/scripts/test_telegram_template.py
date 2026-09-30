#!/usr/bin/env python3
"""Tests del mensaje de Telegram con métrica dual (unittest, sin red).

Uso: python 04_Config/scripts/test_telegram_template.py
"""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"
CALIB = {"validated": True, "scoring_version": "7.2.1", "threshold": 56,
         "primary": {"rate": 0.60, "ci90": [0.4614, 0.7243], "n": 35},
         "secondary": {"rate": 0.0857, "ci90": [0.0348, 0.1961], "n": 35},
         "rug_after_primary_hit": {"rate": 0.762, "ci90": [0.585, 0.879], "n": 21}}
TOKEN = {"token": {"symbol": "PARASITE", "mint": "8ed8xX8TVRDdeyyUwq7Kyo8VwxMWZ6c5J6ertxaBpump", "solAmount": 1.5},
         "score": 72, "reasons": ["v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta)",
                                   "MCap > $1M", "Volumen alto", "Liquidez alta"],
         "dexscreener": {"priceUsd": 0.009848, "liquidityUsd": 141632.8, "volume24hUsd": 201003.7,
                         "marketCapUsd": 9844684.6}}

class TemplateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="tg_")
        os.environ["SHOT_ROOT"] = self.tmp
        spec = importlib.util.spec_from_file_location("s97_tpl", SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.calib_path = Path(self.tmp) / "02_Analisis" / "diagnostics" / "emission_calibration.json"
        self.calib_path.parent.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("SHOT_ROOT", None)

    def test_con_calibracion_validada_muestra_metrica_dual(self):
        msg, _ = self.m.format_alert_message(TOKEN, (), CALIB)
        self.assertIn("Tocar +20% antes de caer −30% (≤48 h): 60% (IC90: 46%–72%)", msg)
        self.assertIn("Cerrar ≥ +20% a las 48 h (mantener): 9% (IC90: 3%–20%)", msg)
        self.assertIn("Después de tocar +20%, llegar a ≤ −99% (≤48 h): 76% (IC90: 58%–88%, n=21)", msg)
        self.assertIn("scoring v7.2.1, score ≥ 56, n=35", msg)

    def test_sin_calibracion_no_inventa_cifras(self):
        msg, _ = self.m.format_alert_message(TOKEN, (), None)
        self.assertIn("en validación", msg)
        self.assertNotIn("IC90", msg)

    def test_datos_reales_y_nunca_valores_por_defecto(self):
        msg, _ = self.m.format_alert_message(TOKEN, (), None)
        self.assertIn("$0.009848", msg)
        self.assertIn("$141,633", msg)
        self.assertIn("Compra inicial del creador: 1.50 SOL", msg)
        bare = {"token": {"symbol": "X"}, "score": 60, "dexscreener": None}
        msg, _ = self.m.format_alert_message(bare, (), None)
        for fake in ("$0.001", "$25,000", "$50,000", "85.0 SOL", "top 1%", "Sin señales de riesgo", "ballena"):
            self.assertNotIn(fake, msg)
        self.assertEqual(msg.count("n/d"), 5)   # precio, mcap, liquidez, volumen + motivos

    def test_motivos_reales_sin_nota_interna(self):
        msg, _ = self.m.format_alert_message(TOKEN, (), None)
        self.assertIn("• MCap > $1M", msg)
        self.assertNotIn("v7.2.1: bonos temporales", msg)
        self.assertIn("(score 72)", msg)

    def test_colision_de_simbolo_como_dato(self):
        msg, _ = self.m.format_alert_message(TOKEN, ["otro_mint"], None)
        self.assertIn("• Símbolo compartido: ya se alertó OTRO token PARASITE con mint distinto", msg)
        # Va en el bloque de datos: después del mercado y antes de los motivos
        self.assertLess(msg.index("Volumen 24h"), msg.index("Símbolo compartido"))
        self.assertLess(msg.index("Símbolo compartido"), msg.index("POR QUÉ LO DETECTAMOS"))
        msg, _ = self.m.format_alert_message(TOKEN, (), None)
        self.assertNotIn("Símbolo compartido", msg)

    def test_carga_de_calibracion(self):
        self.assertIsNone(self.m.load_emission_calibration(str(self.calib_path)))            # no existe
        self.calib_path.write_text(json.dumps(dict(CALIB, validated=False)), encoding="utf-8")
        self.assertIsNone(self.m.load_emission_calibration(str(self.calib_path)))            # sin validar
        self.calib_path.write_text(json.dumps(dict(CALIB, primary={"rate": "x"})), encoding="utf-8")
        self.assertIsNone(self.m.load_emission_calibration(str(self.calib_path)))            # mal formada
        self.calib_path.write_text(json.dumps(CALIB), encoding="utf-8")
        self.assertEqual(self.m.load_emission_calibration(str(self.calib_path))["threshold"], 56)
        self.assertEqual(self.m.load_emission_calibration()["threshold"], 56)                # ruta por defecto

    def test_metrica_post_hit_siempre_sin_consejo(self):
        bare = {"token": {"symbol": "X"}, "score": 60, "dexscreener": None}
        for token, calib in ((TOKEN, CALIB), (TOKEN, None), (bare, None), (bare, CALIB)):
            msg, _ = self.m.format_alert_message(token, ["otro_mint"], calib)
            self.assertIn("≤ −99%", msg)
            for text in ("ADVERTENCIA", "altísimo riesgo", "Plan sugerido", "NO mantener", "Stop en −30%",
                         "No invertir más"):
                self.assertNotIn(text, msg)

    def test_sin_calibracion_usa_cifra_historica_rotulada(self):
        msg, _ = self.m.format_alert_message(TOKEN, (), None)
        self.assertIn("• Histórico (histórico v7.1, score ≥ 56, n=21): después de tocar +20%, "
                      "el 76% llegó a ≤ −99% dentro de las 48 h", msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)