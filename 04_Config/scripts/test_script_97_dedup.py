#!/usr/bin/env python3
"""Tests de deduplicación y robustez de script_97_emit_alerts (unittest, sin red).

Uso: python 04_Config/scripts/test_script_97_dedup.py
Cada test trabaja sobre un directorio temporal: nunca toca los JSON canónicos del repo.
"""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"

PARASITE_A = "8ed8xX8TVRDdeyyUwq7Kyo8VwxMWZ6c5J6ertxaBpump"   # los dos PARASITE reales
PARASITE_B = "3kmygWKZBkCYrgZHKfiuB9UFKTcDLTFFsKo3BWpmpump"
OTHER = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
EVM = "0x532f27101965dd16442E59d40670FaF5eBB142E4"


def token(symbol, price=0.01, score=80):
    return {"token": {"symbol": symbol}, "score": score, "dexscreener": {"priceUsd": price}}


def alert(mint, symbol, status="active_tracking", **extra):
    return {"timestamp": "2026-09-29_165149", "mint": mint, "symbol": symbol, "score": 65,
            "confidence": 58, "initial_price": 0.005, "status": status, "trust_updates": [], **extra}


class Script97TestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="s97_")
        os.environ["SHOT_ROOT"] = self.tmp
        spec = importlib.util.spec_from_file_location("script_97_under_test", SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        alerts_dir = Path(self.tmp) / "02_Analisis" / "alerts"
        self.alerts_file = alerts_dir / "_all_alerts.json"
        self.cycle_log = alerts_dir / "_cycle_log.json"
        self.precision = alerts_dir / "_precision_log.json"
        self.accumulated = Path(self.tmp) / "02_Analisis" / "shadow_v4" / "_accumulated.json"
        self.accumulated.parent.mkdir(parents=True, exist_ok=True)
        self.sent = []
        self.m.send_telegram = lambda msg: self.sent.append(msg) or True
        self.m.time.sleep = lambda s: None

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("SHOT_ROOT", None)

    def write(self, path, data):
        path.write_text(data if isinstance(data, str) else json.dumps(data), encoding="utf-8")

    def read(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def dedup_events(self):
        return self.read(self.cycle_log).get("dedup_events", []) if self.cycle_log.exists() else []


class TestDedup(Script97TestCase):
    def test_mint_ya_alertado_no_se_duplica_activo_ni_cerrado(self):
        self.write(self.alerts_file, [alert(PARASITE_A, "PARASITE"),
                                      alert(OTHER, "Fartcoin", status="DESCARTAR_NOPAR",
                                            final_verdict="FALSO POSITIVO")])
        self.write(self.accumulated, {PARASITE_A: token("PARASITE"), OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 0)
        self.assertEqual(self.sent, [])
        self.assertEqual(len(self.read(self.alerts_file)), 2)

    def test_mismo_symbol_distinto_mint_se_registra_y_se_marca(self):
        self.write(self.alerts_file, [alert(PARASITE_A, "PARASITE")])
        self.write(self.accumulated, {PARASITE_B: token("PARASITE", price=0.0029)})
        self.assertEqual(self.m.main(), 0)
        alerts = self.read(self.alerts_file)
        self.assertEqual([a["mint"] for a in alerts], [PARASITE_A, PARASITE_B])
        self.assertEqual(alerts[1]["symbol_collision"], [PARASITE_A])
        self.assertIn("OTRO token con el símbolo PARASITE", self.sent[0])
        events = self.dedup_events()
        self.assertEqual(events[0]["type"], "symbol_collision")
        self.assertEqual(events[0]["other_mints"], [PARASITE_A])

    def test_symbol_sin_colision_no_agrega_campo_ni_advertencia(self):
        self.write(self.alerts_file, [alert(OTHER, "Fartcoin")])
        self.write(self.accumulated, {PARASITE_A: token("PARASITE")})
        self.m.main()
        self.assertNotIn("symbol_collision", self.read(self.alerts_file)[1])
        self.assertNotIn("OTRO token", self.sent[0])

    def test_variantes_de_espacios_y_mayusculas_evm(self):
        self.write(self.alerts_file, [alert(PARASITE_A, "PARASITE"), alert(EVM.lower(), "BRETT")])
        self.write(self.accumulated, {f" {PARASITE_A} ": token("PARASITE"), EVM.upper().replace("0X", "0x"): token("BRETT")})
        self.m.main()
        self.assertEqual(self.sent, [])

    def test_base58_distingue_mayusculas(self):
        self.assertNotEqual(self.m.normalize_mint(PARASITE_A), self.m.normalize_mint(PARASITE_A.lower()))
        self.assertEqual(self.m.normalize_mint(EVM), self.m.normalize_mint(EVM.lower()))

    def test_dos_corridas_son_idempotentes(self):
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {PARASITE_A: token("PARASITE")})
        self.m.main()
        self.m.main()
        self.assertEqual(len(self.sent), 1)
        self.assertEqual(len(self.read(self.alerts_file)), 1)


class TestRobustez(Script97TestCase):
    def test_json_corrupto_no_emite_ni_sobrescribe(self):
        corrupt = '[{"mint": "' + PARASITE_A + '", "symbol": "PARASITE"'   # truncado
        self.write(self.alerts_file, corrupt)
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 1)
        self.assertEqual(self.alerts_file.read_text(encoding="utf-8"), corrupt)
        self.assertEqual(self.sent, [])
        self.assertEqual(self.dedup_events()[0]["type"], "corrupt_alerts_file")

    def test_json_que_no_es_lista_no_emite_ni_sobrescribe(self):
        self.write(self.alerts_file, {"alerts": []})
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 1)
        self.assertEqual(self.read(self.alerts_file), {"alerts": []})
        self.assertEqual(self.sent, [])

    def test_archivo_inexistente_es_primera_corrida(self):
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 0)
        self.assertEqual(len(self.read(self.alerts_file)), 1)

    def test_sin_precio_no_se_envia_ni_se_registra(self):
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: {"token": {"symbol": "X"}, "score": 90, "dexscreener": None}})
        self.m.main()
        self.m.main()
        self.assertEqual(self.sent, [])   # antes: se enviaba en CADA corrida sin registrarse
        self.assertEqual(self.read(self.alerts_file), [])

    def test_telegram_fallido_igual_queda_registrado_y_no_se_reenvia(self):
        self.m.send_telegram = lambda msg: self.sent.append(msg) or False
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.m.main()
        self.m.main()
        self.assertEqual(len(self.sent), 1)
        self.assertIs(self.read(self.alerts_file)[0]["telegram_sent"], False)

    def test_precision_log_curado_no_tumba_el_step(self):
        # Reproduce el crash de producción (run 36651496249): 9 alertas + 1 = 10 con log en formato dict
        curated = {"created_at": "2026-09-28T19:22:51Z", "precision_metrics": {"n": 2}, "alerts": []}
        self.write(self.precision, curated)
        self.write(self.alerts_file, [alert(f"mint{i:040d}", f"S{i}") for i in range(9)])
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 0)
        self.assertEqual(len(self.read(self.alerts_file)), 10)
        self.assertEqual(self.read(self.precision), curated)

    def test_duplicados_preexistentes_se_reportan_una_vez_y_no_se_borran(self):
        self.write(self.alerts_file, [alert(PARASITE_A, "PARASITE"), alert(PARASITE_A, "PARASITE")])
        self.write(self.accumulated, {})
        self.m.main()
        self.m.main()
        self.assertEqual(len(self.read(self.alerts_file)), 2)
        events = [e for e in self.dedup_events() if e["type"] == "existing_duplicates"]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["mints"], {PARASITE_A: 2})

    def test_cycle_log_existente_conserva_sus_ciclos(self):
        self.write(self.cycle_log, {"created_at": "x", "cycles": [{"id": "18.6"}]})
        self.write(self.alerts_file, [alert(PARASITE_A, "PARASITE")])
        self.write(self.accumulated, {PARASITE_B: token("PARASITE")})
        self.m.main()
        log = self.read(self.cycle_log)
        self.assertEqual(log["cycles"], [{"id": "18.6"}])
        self.assertEqual(len(log["dedup_events"]), 1)

    def test_escritura_atomica_no_deja_temporales(self):
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.m.main()
        self.assertEqual(sorted(p.name for p in self.alerts_file.parent.glob("*.tmp")), [])


class TestModos(Script97TestCase):
    def setUp(self):
        super().setUp()
        self._env = {k: os.environ.pop(k) for k in ("SHADOW_MODE", "PAUSE_EMISSIONS") if k in os.environ}

    def tearDown(self):
        for k in ("SHADOW_MODE", "PAUSE_EMISSIONS"):
            os.environ.pop(k, None)
        os.environ.update(self._env)
        super().tearDown()

    def test_shadow_registra_sin_telegram(self):
        os.environ["SHADOW_MODE"] = "true"
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: token("Fartcoin"), PARASITE_A: token("PARASITE")})
        self.assertEqual(self.m.main(), 0)
        self.assertEqual(self.sent, [])
        alerts = self.read(self.alerts_file)
        self.assertEqual({a["status"] for a in alerts}, {"shadow"})
        self.assertEqual({a["telegram_sent"] for a in alerts}, {False})

    def test_shadow_false_envia_normal(self):
        os.environ["SHADOW_MODE"] = "false"
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.m.main()
        self.assertEqual(len(self.sent), 1)
        self.assertEqual(self.read(self.alerts_file)[0]["status"], "active_tracking")

    def test_pause_no_procesa_nada_aunque_haya_shadow(self):
        os.environ["PAUSE_EMISSIONS"] = "true"
        os.environ["SHADOW_MODE"] = "true"
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.assertEqual(self.m.main(), 0)
        self.assertEqual(self.sent, [])
        self.assertFalse(self.alerts_file.exists())

    def test_reactivacion_shadow_queda_historico_y_nuevas_van_a_activo(self):
        os.environ["SHADOW_MODE"] = "true"
        self.write(self.alerts_file, [])
        self.write(self.accumulated, {OTHER: token("Fartcoin")})
        self.m.main()
        os.environ["SHADOW_MODE"] = "false"
        self.write(self.accumulated, {OTHER: token("Fartcoin"), PARASITE_A: token("PARASITE")})
        self.m.main()
        alerts = self.read(self.alerts_file)
        self.assertEqual([(a["mint"], a["status"]) for a in alerts],
                         [(OTHER, "shadow"), (PARASITE_A, "active_tracking")])
        self.assertEqual(len(self.sent), 1)   # solo el nuevo; el mint en sombra no se re-emite

    def test_valores_de_flag(self):
        for v, expected in (("TRUE", True), ("1", True), ("yes", True), ("false", False), ("", False), ("0", False)):
            os.environ["SHADOW_MODE"] = v
            self.assertIs(self.m.env_flag("SHADOW_MODE"), expected, v)


if __name__ == "__main__":
    unittest.main(verbosity=2)
