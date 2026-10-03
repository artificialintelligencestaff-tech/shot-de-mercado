#!/usr/bin/env python3
"""Tests de los eventos entre bots (Ola 3): lib_events. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_events.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_events as ev  # noqa: E402

T0 = 1791000000                      # 2026-10-03T04:00:00Z (múltiplo de 3600 y de 14400)
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="events_"))
        self.addCleanup(shutil.rmtree, self.root, True)

    def w(self, type="pump_naciente", subject=MINT, severity=2, writer="early_watch_a", now=T0 + 120, **kw):
        return ev.write_event(type, subject, severity, kw.pop("data", {"score": 61}), writer=writer, now=now,
                              root=self.root, **kw)

    def lines(self, writer, day="2026-10-03"):
        p = self.root / "02_Analisis/events" / writer / f"{day}.jsonl"
        return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []


class Escritura(Base):
    def test_esquema_id_bucket_y_archivo_por_escritor(self):
        e = self.w()
        self.assertEqual(sorted(e), ["bucket", "data", "id", "parent", "severity", "subject", "ts", "ttl_s", "type",
                                     "v", "writer"])
        self.assertEqual((e["v"], e["bucket"], e["ttl_s"], e["writer"]), (1, T0, 3600, "early_watch_a"))
        self.assertEqual(e["id"], ev.event_id("pump_naciente", MINT, T0))
        self.assertEqual(self.lines("early_watch_a"), [e])
        self.assertEqual(ev.TYPES["feed_caido"]["ttl_s"], 7200)
        self.assertEqual(ev.TYPES["narrativa_emergente"]["ttl_s"], 14400)
        hijo = self.w("alerta_emitida", parent=e["id"], writer="script_97")
        self.assertEqual(hijo["parent"], e["id"])
        for bad in (dict(type="rumor"), dict(severity=4), dict(severity=True), dict(subject="  "),
                    dict(writer="Early-A"), dict(parent="xyz"), dict(data={"blob": "x" * 5000})):
            with self.assertRaises(ValueError, msg=bad):
                self.w(**bad)

    def test_idempotencia_mismo_hecho_misma_ventana(self):
        first = self.w(now=T0 + 120)
        self.assertIsNone(self.w(now=T0 + 3000))                         # misma hora: mismo id, no se reescribe
        later = self.w(now=T0 + 3700)                                    # ventana siguiente: hecho nuevo
        self.assertNotEqual(later["id"], first["id"])
        self.assertEqual(len(self.lines("early_watch_a")), 2)

    def test_dedup_entre_escritores(self):
        a = self.w(writer="early_watch_a")
        self.assertIsNone(self.w(writer="early_watch_b", now=T0 + 900))  # b ve que a ya lo escribió
        # carrera real: los dos escribieron antes de ver el commit del otro
        raced = dict(a, writer="early_watch_b", ts=T0 + 130)
        p = self.root / "02_Analisis/events/early_watch_b/2026-10-03.jsonl"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps(raced) + "\n", encoding="utf-8")
        got = ev.read_events(now=T0 + 600, root=self.root)
        self.assertEqual([(x["id"], x["writer"]) for x in got], [(a["id"], "early_watch_a")])


class Lectura(Base):
    def test_ttl_por_tipo(self):
        self.w("pump_naciente", now=T0)
        self.w("narrativa_emergente", "memecoin", 1, writer="orchestrator", now=T0)
        self.w("feed_caido", "rss/coindesk", 1, writer="self_repair", now=T0)
        types = lambda now, **kw: [x["type"] for x in ev.read_events(now=now, root=self.root, **kw)]  # noqa: E731
        self.assertEqual(sorted(types(T0 + 3600)), ["feed_caido", "narrativa_emergente", "pump_naciente"])
        self.assertEqual(sorted(types(T0 + 3601)), ["feed_caido", "narrativa_emergente"])
        self.assertEqual(types(T0 + 7201), ["narrativa_emergente"])
        self.assertEqual(types(T0 + 14401), [])
        self.assertEqual(len(types(T0 + 14401, include_expired=True)), 3)

    def test_filtros_since_tipos_y_severidad(self):
        self.w("pump_naciente", severity=3, now=T0)
        self.w("mencion_acelerada", "$WIF", 1, writer="orchestrator", now=T0 + 600)
        self.w("fuente_saturada", "telegram/pumpfun", 0, writer="telegram_a", now=T0 + 1200)
        read = lambda **kw: [x["type"] for x in ev.read_events(now=T0 + 1300, root=self.root, **kw)]  # noqa: E731
        self.assertEqual(read(since_ts=T0 + 600), ["mencion_acelerada", "fuente_saturada"])
        self.assertEqual(read(types=["pump_naciente", "fuente_saturada"]), ["pump_naciente", "fuente_saturada"])
        self.assertEqual(read(max_severity=1), ["mencion_acelerada", "fuente_saturada"])
        self.assertEqual(read(min_severity=3), ["pump_naciente"])
        self.assertEqual(ev.read_events(types="mencion_acelerada", now=T0 + 1300, root=self.root)[0]["subject"],
                         "$WIF")


class Consumo(Base):
    def test_cursor_propio_entrega_solo_lo_nuevo(self):
        got = []
        self.w(now=T0)
        out = ev.consume("dossier", got.append, now=T0 + 60, root=self.root)
        self.assertEqual([x["type"] for x in out["delivered"]], ["pump_naciente"])
        self.assertTrue((self.root / "02_Analisis/events/_cursors/dossier.json").exists())
        self.assertEqual(ev.consume("dossier", got.append, now=T0 + 120, root=self.root)["delivered"], [])
        self.w("graduacion", now=T0 + 200)
        self.assertEqual([x["type"] for x in ev.consume("dossier", got.append, now=T0 + 300, root=self.root)
                          ["delivered"]], ["graduacion"])
        self.assertEqual(len(got), 2)
        otro = ev.consume("sampler", lambda e: None, types="graduacion", now=T0 + 300, root=self.root)
        self.assertEqual([x["type"] for x in otro["delivered"]], ["graduacion"])    # cursores independientes

    def test_evento_viejo_que_llega_tarde_por_merge_igual_se_entrega(self):
        self.w(now=T0 + 600)
        ev.consume("dossier", lambda e: None, now=T0 + 700, root=self.root)
        # otro escritor pushea después un evento con ts ANTERIOR al último consumido (cursor por líneas, no por ts)
        late = ev.make_event("feed_caido", "rss/decrypt", 1, writer="self_repair", now=T0 + 100)
        p = self.root / "02_Analisis/events/self_repair/2026-10-03.jsonl"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps(late) + "\n" + '{"v": 1, "id": "abc', encoding="utf-8")       # + línea a medias
        out = ev.consume("dossier", lambda e: None, now=T0 + 800, root=self.root)
        self.assertEqual([x["subject"] for x in out["delivered"]], ["rss/decrypt"])
        cur = json.loads((self.root / "02_Analisis/events/_cursors/dossier.json").read_text(encoding="utf-8"))
        self.assertEqual(cur["files"]["self_repair/2026-10-03.jsonl"], 1)          # la línea a medias se relee

    def test_callback_que_falla_reintenta_sin_perder_ni_duplicar(self):
        self.w(now=T0)
        self.w(subject="So11111111111111111111111111111111111111112", now=T0 + 60)
        self.w("feed_caido", "rss/x", 1, writer="self_repair", now=T0 + 30)
        calls = []

        def flaky(e):
            calls.append(e["subject"])
            if e["subject"] == MINT and calls.count(MINT) == 1:
                raise RuntimeError("caído")
        first = ev.consume("c1", flaky, now=T0 + 100, root=self.root)
        self.assertEqual(len(first["errors"]), 1)
        self.assertEqual([x["subject"] for x in first["delivered"]], ["rss/x"])     # el otro escritor siguió
        second = ev.consume("c1", flaky, now=T0 + 200, root=self.root)
        self.assertEqual([x["subject"] for x in second["delivered"]],
                         [MINT, "So11111111111111111111111111111111111111112"])     # orden del escritor
        self.assertEqual(ev.consume("c1", flaky, now=T0 + 300, root=self.root)["delivered"], [])
        self.assertEqual(calls.count("rss/x"), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
