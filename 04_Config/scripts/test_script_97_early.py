#!/usr/bin/env python3
"""script_97 + vigilancia temprana (Fase 10): hand-off de la ruta Solana a script_116, adopción de sus alertas en
_all_alerts.json (con dossier) y bono anticipatorio multi-chain. unittest, sin red.

Uso: python 04_Config/scripts/test_script_97_early.py
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

HERE = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc)
SOL_MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
EARLY_MINT = "AAAAbbbbCCCCddddEEEEffffGGGGhhhhIIIIjjjjpump"

import test_script_97_multichain as base  # noqa: E402  (fixtures compartidos)


class Resp(base.Resp):
    pass


def early_record(mint=EARLY_MINT, sent=True):
    return {"timestamp": (NOW - timedelta(minutes=3)).strftime("%Y-%m-%d_%H%M%S"), "mint": mint, "symbol": "EARLY",
            "score": 61, "score_base": 55, "early_bonus": 6, "confidence": 57, "initial_price": 0.001,
            "status": "active_tracking", "trust_updates": [], "early": True, "age_min_at_alert": 31.0,
            "telegram_sent": sent}


class Early(base.MultichainEmision):
    def write_early(self, records, with_detail=True):
        d = Path(self.tmp) / "02_Analisis" / "early"
        d.mkdir(parents=True, exist_ok=True)
        (d / "_early_alerts.json").write_text(json.dumps(records), encoding="utf-8")
        if with_detail:
            for r in records:
                tok = base.solana_candidate()
                tok["token"] = {"mint": r["mint"], "symbol": r["symbol"], "name": "Early"}
                (self.root / "alerts" / f"alert_{r['mint']}_{r['timestamp']}.json").write_text(json.dumps(tok))

    def test_early_watch_active(self):
        m = self.load()
        self.assertFalse(m.early_watch_active(repo="o/r", token=None))
        self.assertTrue(m.early_watch_active(lambda *a, **k: Resp(200, {"total_count": 1}), "o/r", "tok"))
        self.assertFalse(m.early_watch_active(lambda *a, **k: Resp(200, {"total_count": 0}), "o/r", "tok"))
        self.assertFalse(m.early_watch_active(lambda *a, **k: (_ for _ in ()).throw(OSError()), "o/r", "tok"))
        with mock.patch.dict(os.environ, {"EARLY_HANDOFF": "false"}):
            self.assertFalse(m.early_watch_active(lambda *a, **k: Resp(200, {"total_count": 1}), "o/r", "tok"))

    def test_con_early_watch_activo_la_ruta_solana_se_cede_y_se_adopta(self):
        self.acc.write_text(json.dumps({SOL_MINT: base.solana_candidate()}), encoding="utf-8")
        self.write_early([early_record()])
        m = self.load()
        with mock.patch.object(m, "early_watch_active", lambda: True):
            self.assertEqual(m.main([]), 0)
        alerts = self.alerts()
        self.assertEqual([a["mint"] for a in alerts], [EARLY_MINT])          # SOL_MINT no se emitió acá
        rec = alerts[0]
        self.assertTrue(rec["early"])
        self.assertIn("adopted_at", rec)
        self.assertTrue(rec.get("dossier"))
        doc = [p for p in self.posts if p["method"] == "sendDocument"]
        self.assertEqual(len(doc), 1)
        self.assertIn("CÓMO ADQUIRIRLO", doc[0]["data"]["caption"])
        hist = (Path(self.tmp) / "02_Analisis" / "datasets" / "historical_alerts.jsonl").read_text().splitlines()
        self.assertEqual(json.loads(hist[0])["mint"], EARLY_MINT)

    def test_sin_early_watch_emite_como_siempre_y_no_duplica(self):
        self.acc.write_text(json.dumps({SOL_MINT: base.solana_candidate()}), encoding="utf-8")
        self.write_early([early_record(SOL_MINT)], with_detail=False)          # early ya emitió ese mint
        m = self.load()
        with mock.patch.object(m, "early_watch_active", lambda: False):
            m.main([])
        alerts = self.alerts()
        self.assertEqual(len(alerts), 1)
        self.assertTrue(alerts[0]["early"])
        self.assertFalse([p for p in self.posts if p["method"] == "sendMessage"])
        # sin alertas tempranas: la ruta Solana de siempre
        self.alerts_file.write_text("[]", encoding="utf-8")
        self.write_early([])
        m.main([])
        self.assertEqual([a["mint"] for a in self.alerts()], [SOL_MINT])

    def test_adopcion_idempotente_y_sombra_sin_envio(self):
        self.write_early([early_record(sent=False)])
        m = self.load()
        all_alerts = []
        first = m.adopt_early_alerts(all_alerts, m.load_early_alerts(), shadow=True)
        again = m.adopt_early_alerts(all_alerts, m.load_early_alerts(), shadow=True)
        self.assertEqual((len(first), len(again), len(all_alerts)), (1, 0, 1))
        self.assertFalse(self.posts)

    def test_load_early_alerts_fresco_desde_origin(self):
        m = self.load()

        class R:
            def __init__(self, rc, out=""):
                self.returncode, self.stdout = rc, out

        calls = []

        def run(args, **kw):
            calls.append(args[1])
            return R(0, json.dumps([early_record()])) if args[1] == "show" else R(0)

        self.assertEqual(m.load_early_alerts(fresh=True, run=run)[0]["mint"], EARLY_MINT)
        self.assertEqual(calls, ["fetch", "show"])
        self.assertEqual(m.load_early_alerts(fresh=True, run=lambda *a, **k: R(1)), [])

    def test_bono_multichain_desde_signals(self):
        self.write_gov_inputs()
        m = self.load()
        sin = {r["key"]: r["score"] for r in m.multichain_results(NOW)}["cg:govtoken"]
        d = Path(self.tmp) / "02_Analisis" / "early"
        d.mkdir(parents=True, exist_ok=True)
        sig = {"generated_at": NOW.isoformat(timespec="seconds"),
               "signals": {"cg:govtoken": {"version": "early-0.1", "bonus": 3, "reasons": ["orderbook +0.6"]}}}
        (d / "_signals.json").write_text(json.dumps(sig))
        res = {r["key"]: r for r in m.multichain_results(NOW)}["cg:govtoken"]
        self.assertEqual(res["score"], min(100, sin + 3))
        self.assertTrue(any("Anticipación" in x for x in res["reasons"]))
        sig["generated_at"] = (NOW - timedelta(minutes=45)).isoformat(timespec="seconds")   # viejo: no cuenta
        (d / "_signals.json").write_text(json.dumps(sig))
        self.assertIsNone(m.load_early_signals())


def load_tests(loader, tests, pattern):
    """Solo los tests propios (Early hereda fixtures, no los tests de test_script_97_multichain)."""
    return unittest.TestSuite(Early(n) for n in sorted(vars(Early)) if n.startswith("test_"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
