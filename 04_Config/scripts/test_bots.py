#!/usr/bin/env python3
"""Tests de los bots gemelos (unittest, sin red: API de GitHub y Telegram simulados).

Uso: python 04_Config/scripts/test_bots.py
Todo corre sobre un SHOT_ROOT temporal: nunca toca los JSON del repo.
"""
import json
import os
import shutil
import sys
import tempfile
import time
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

TMP = tempfile.mkdtemp(prefix="bots_")
os.environ["SHOT_ROOT"] = TMP
for k in ("TELEGRAM_OPS_CHAT_ID", "TELEGRAM_BOT_TOKEN", "GITHUB_TOKEN"):
    os.environ.pop(k, None)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_ops  # noqa: E402
import bot_health_check as health  # noqa: E402
import bot_autorepair as repair  # noqa: E402
import bot_daily_summary as daily  # noqa: E402
import monitor_shadow as mon  # noqa: E402

NOW = datetime(2026, 9, 30, 12, 0, tzinfo=timezone.utc)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def run(rid, concl, minutes_ago, attempt=1):
    return {"id": rid, "status": "completed", "conclusion": concl, "created_at": iso(NOW - timedelta(minutes=minutes_ago)),
            "run_attempt": attempt, "head_sha": "abc1234", "event": "schedule"}


class Base(unittest.TestCase):
    def setUp(self):
        for child in Path(TMP).iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
        self.sent = []

    def notify(self, text, dry_run=False):
        self.sent.append(text)
        return "sent"


class TestLibOps(Base):
    def test_telegram_solo_chat_de_operaciones(self):
        os.environ["TELEGRAM_CHAT_ID"] = "chat-publico"
        os.environ["TELEGRAM_BOT_TOKEN"] = "x"
        try:
            self.assertEqual(lib_ops.send_ops_telegram("hola"), "skipped_no_ops_chat")
        finally:
            os.environ.pop("TELEGRAM_CHAT_ID")
            os.environ.pop("TELEGRAM_BOT_TOKEN")
        self.assertEqual(lib_ops.send_ops_telegram("hola", dry_run=True), "dry_run")

    def test_append_capped(self):
        p = Path(TMP) / "log.json"
        for i in range(7):
            data = lib_ops.append_capped(p, {"i": i}, cap=5)
        self.assertEqual([e["i"] for e in data["entries"]], [2, 3, 4, 5, 6])


class TestHealth(Base):
    def api(self, path, method="GET", payload=None):
        return {"workflows": [{"path": ".github/workflows/pipeline_t0.yml", "state": "active"},
                              {"path": ".github/workflows/trust_update.yml", "state": "active"},
                              {"path": ".github/workflows/viejo.yml", "state": "disabled_manually"}]}

    def write_data(self, det_minutes_ago, alert_hours_ago):
        det = Path(TMP) / "01_Datos_Crudos" / "final_detection"
        det.mkdir(parents=True)
        (det / f"detection_{(NOW - timedelta(minutes=det_minutes_ago)):%Y-%m-%d_%H%M%S}.json").write_text("{}")
        al = Path(TMP) / "02_Analisis" / "alerts"
        al.mkdir(parents=True)
        (al / "_all_alerts.json").write_text(json.dumps(
            [{"timestamp": f"{(NOW - timedelta(hours=alert_hours_ago)):%Y-%m-%d_%H%M%S}", "mint": "m"}]))

    def test_fallas_consecutivas_y_pipeline_parado(self):
        self.write_data(10, 1)
        runs = {"pipeline_t0.yml": [run(3, "failure", 20), run(2, "failure", 40), run(1, "success", 200)],
                "trust_update.yml": [run(9, "success", 20)]}
        e = health.run(api=self.api, runs_fn=lambda wf: runs[wf], now=NOW, notify=self.notify)
        self.assertEqual(e["problem_keys"], ["consecutive_failures:pipeline_t0.yml", "pipeline_stale:pipeline_t0.yml"])
        self.assertNotIn("viejo.yml", e["workflows"])
        self.assertEqual(len(self.sent), 1)

    def test_avisa_solo_si_cambia(self):
        self.write_data(10, 1)
        runs = {"pipeline_t0.yml": [run(3, "failure", 20), run(2, "failure", 40), run(1, "success", 60)],
                "trust_update.yml": [run(9, "success", 20)]}
        health.run(api=self.api, runs_fn=lambda wf: runs[wf], now=NOW, notify=self.notify)
        health.run(api=self.api, runs_fn=lambda wf: runs[wf], now=NOW, notify=self.notify)
        self.assertEqual(len(self.sent), 1)
        runs["pipeline_t0.yml"].insert(0, run(4, "success", 5))
        e = health.run(api=self.api, runs_fn=lambda wf: runs[wf], now=NOW, notify=self.notify)
        self.assertEqual(e["problem_keys"], [])
        self.assertIn("resueltos", self.sent[-1])

    def test_sin_detecciones_y_sin_alertas(self):
        self.write_data(7 * 60, 30)
        runs = {"pipeline_t0.yml": [run(1, "success", 5)], "trust_update.yml": [run(9, "success", 5)]}
        e = health.run(api=self.api, runs_fn=lambda wf: runs[wf], now=NOW, notify=self.notify)
        self.assertEqual(sorted(p["type"] for p in e["problems"]), ["no_alerts_24h", "no_detections_6h"])


class TestAutorepair(Base):
    def setUp(self):
        super().setUp()
        self.calls, self.issues = [], []

    def api(self, path, method="GET", payload=None):
        self.calls.append((method, path))
        if path.endswith("/issues?state=open&per_page=100"):
            return self.issues
        if method == "POST" and path.endswith("/issues"):
            self.issues.append({"number": 7, "title": payload["title"]})
            return {"number": 7}
        return {}

    def test_relanza_una_vez_la_falla_transitoria(self):
        runs = {"pipeline_t0.yml": [run(5, "failure", 10)], "trust_update.yml": [], "prelaunch.yml": []}
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Commit state changes", notify=self.notify)
        self.assertEqual([a["type"] for a in e["actions"]], ["rerun"])
        self.assertIn(("POST", f"repos/{lib_ops.REPO}/actions/runs/5/rerun-failed-jobs"), self.calls)
        runs["pipeline_t0.yml"] = [run(5, "failure", 10, attempt=2)]
        self.calls.clear()
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Commit state changes", notify=self.notify)
        self.assertEqual(e["actions"], [])

    def test_no_relanza_fallas_de_codigo(self):
        runs = {"pipeline_t0.yml": [run(5, "failure", 10)], "trust_update.yml": [], "prelaunch.yml": []}
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Emit alerts", notify=self.notify)
        self.assertEqual(e["actions"], [])

    def test_escala_patron_una_sola_vez(self):
        runs = {"pipeline_t0.yml": [run(i, "failure", 20 * i, attempt=2) for i in range(1, 4)] + [run(9, "success", 100)],
                "trust_update.yml": [], "prelaunch.yml": []}
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Emit alerts", notify=self.notify)
        self.assertEqual([a["type"] for a in e["actions"]], ["escalate"])
        self.assertEqual(len(self.issues), 1)
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Emit alerts", notify=self.notify)
        self.assertEqual(e["actions"], [])                       # mismos runs: no repite
        runs["pipeline_t0.yml"].insert(0, run(20, "failure", 1, attempt=2))
        e = repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Emit alerts", notify=self.notify)
        self.assertEqual(e["actions"][0].get("issue"), 7)        # run nuevo: comenta el issue abierto
        self.assertTrue(any(p.endswith("/issues/7/comments") for _, p in self.calls))

    def test_dry_run_no_escribe(self):
        runs = {"pipeline_t0.yml": [run(5, "failure", 10)], "trust_update.yml": [], "prelaunch.yml": []}
        repair.run(api=self.api, runs_fn=lambda wf: runs[wf], step_fn=lambda rid: "Commit state changes",
                   dry_run=True, notify=lambda t, dry_run=False: "dry_run")
        self.assertFalse(any(m == "POST" for m, _ in self.calls))
        self.assertFalse(repair.LOG_FILE.exists())


class TestDaily(Base):
    def test_resumen_y_una_entrada_por_dia(self):
        al = Path(TMP) / "02_Analisis" / "alerts"
        al.mkdir(parents=True)
        (al / "_all_alerts.json").write_text(json.dumps([
            {"timestamp": f"{(NOW - timedelta(hours=2)):%Y-%m-%d_%H%M%S}", "status": "shadow", "telegram_sent": False},
            {"timestamp": f"{(NOW - timedelta(hours=40)):%Y-%m-%d_%H%M%S}", "status": "active_tracking"}]))
        s = daily.run(now=NOW, notify=self.notify)
        self.assertEqual(s["alerts_24h"], {"total": 1, "by_status": {"shadow": 1}, "telegram_sent": 0})
        daily.run(now=NOW, notify=self.notify)
        self.assertEqual(len(lib_ops.read_json(daily.OUT)["days"]), 1)
        self.assertIn("Resumen diario", self.sent[0])


class TestMonitorBot(Base):
    def test_incremental_y_tope_de_llamadas(self):
        class Src:
            calls = 0
            def get(self, pool, t0):
                Src.calls += 1
                return "ok", []
            def save(self):
                pass
        t0 = time.time() - 3 * 86400
        rows = [{"mint": f"m{i}", "alert_ts": "2026-09-27_000000", "pool": "p", "price": 1.0, "t0": t0,
                 "version": "7.2.1", "age_min_at_detection": 90, "staleness_min": 1, "telegram_sent": False}
                for i in range(3)]
        prev = [dict(rows[0], status="ok", primary="miss", secondary="miss")]
        out = mon.measure([dict(r) for r in rows], Src(), previous=prev, max_calls=1)
        self.assertTrue(out[0]["reused"])
        self.assertEqual(Src.calls, 1)
        self.assertEqual(out[2]["status"], "pendiente_de_medicion")

    def test_cycle_log_y_veredicto_unico(self):
        log = Path(TMP) / "cycle.json"
        s = mon.summarize([{"primary": "hit" if i < 8 else "miss", "secondary": "pending", "status": "ok",
                            "age_min_at_detection": 90, "staleness_min": 1, "alert_ts": "2026-09-30_050000",
                            "telegram_sent": False} for i in range(20)])
        report = {"by_version": {"7.2.1": s}}
        self.assertEqual(mon.record_cycle(report, log, notify=self.notify), "sent")
        self.assertEqual(mon.record_cycle(report, log, notify=self.notify), "not_needed")
        data = json.loads(log.read_text(encoding="utf-8"))
        self.assertEqual(len(data["shadow_monitor"]), 1)
        self.assertTrue(data["verdicts"]["shadow_verdict:7.2.1"]["passed"])
        self.assertIn("CUMPLE", self.sent[0])

    def test_record_only_reintento_no_reenvia(self):
        (Path(TMP) / "02_Analisis" / "alerts").mkdir(parents=True)
        s = mon.summarize([{"primary": "hit", "secondary": "pending", "status": "ok", "age_min_at_detection": 90,
                            "staleness_min": 1, "alert_ts": "2026-09-30_050000", "telegram_sent": False}
                           for _ in range(20)])
        out = Path(TMP) / "shadow_monitor.json"
        out.write_text(json.dumps({"by_version": {"7.2.1": s}, "rows": []}), encoding="utf-8")
        self.assertEqual(mon.main(["--record-only", "--cycle-log", "--notified-previous", "--out", str(out)]), 0)
        log = json.loads((mon.ALERTS_DIR / "_cycle_log.json").read_text(encoding="utf-8"))
        self.assertEqual(log["verdicts"]["shadow_verdict:7.2.1"]["notified"], "sent_previous_attempt")
        self.assertEqual(log["shadow_monitor"][0]["version"], "7.2.1")


def tearDownModule():
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
