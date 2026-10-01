#!/usr/bin/env python3
"""Tests de probe_narrative_sources (sonda de fuentes del doc 26). unittest, sin red: sesión simulada.

Uso: python 04_Config/scripts/test_probe_narrative_sources.py
"""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import requests

SCRIPTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("probe_test", SCRIPTS / "probe_narrative_sources.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

ATOM = ('<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><entry><id>1</id><title>x</title>'
        '<updated>2026-10-01T03:10:00+00:00</updated></entry></feed>')
TG = ('<div class="tgme_widget_message" data-post="c/1"><div class="tgme_widget_message_text">hola</div>'
      '<time datetime="2026-10-01T03:55:38+00:00"></time></div>')


class FakeResponse:
    def __init__(self, status, body, url, headers=None):
        self.status_code, self.url, self.headers = status, url, headers or {}
        self.text = body if isinstance(body, str) else json.dumps(body)
        self.content = self.text.encode("utf-8")

    def json(self):
        return json.loads(self.text)


class FakeSession:
    """Respuesta por host: 200 con un payload válido, salvo los hosts marcados como caídos o rotos."""

    def __init__(self, down=(), broken=(), raises=()):
        self.down, self.broken, self.raises, self.calls = set(down), set(broken), set(raises), []

    def get(self, url, headers=None, timeout=None):
        self.calls.append((url, headers))
        host = url.split("/")[2]
        if host in self.raises:
            raise requests.ConnectionError("sin conexión")
        if host in self.down:
            return FakeResponse(403, "forbidden", url)
        if host in self.broken:
            return FakeResponse(200, "<html>no es lo esperado", url)
        payload = {"www.reddit.com": ATOM, "t.me": TG,
                   "a.4cdn.org": [{"threads": [{"no": 1, "time": 1790800000, "com": "hola"}]}],
                   "hn.algolia.com": {"hits": [{"objectID": "1", "created_at_i": 1790800000, "title": "t"}]},
                   "api.gdeltproject.org": {"timeline": [{"data": [{"date": "20261001T030000Z", "value": 3}]}]},
                   "api.coingecko.com": {"coins": [{"item": {"id": "x", "name": "X", "symbol": "X"}}]}}.get(host, ATOM)
        return FakeResponse(200, payload, url, {"x-ratelimit-remaining": "99"})


class ProbeTest(unittest.TestCase):
    def test_todo_ok_habilita_la_fase_0(self):
        r = probe.run_probe(session=FakeSession(), sleep=lambda s: None)
        s = r["summary"]
        self.assertEqual(s["mention_families_ok_count"], 6)
        self.assertEqual(s["mention_families_total"], 6)          # coingecko_trending no cuenta como menciones
        self.assertEqual(s["endpoints_ok"], s["endpoints_total"])
        self.assertTrue(s["phase0_enabled_by_probe"])
        e = r["families"]["reddit_rss"]["endpoints"][0]
        self.assertEqual((e["status"], e["items"], e["rate_limit"]), (200, 1, {"x-ratelimit-remaining": "99"}))

    def test_menos_de_tres_familias_no_habilita(self):
        down = {"www.reddit.com", "t.me", "a.4cdn.org", "hn.algolia.com"}
        r = probe.run_probe(session=FakeSession(down=down), sleep=lambda s: None)
        self.assertEqual(r["summary"]["mention_families_ok"], ["gdelt", "news_rss"])
        self.assertFalse(r["summary"]["phase0_enabled_by_probe"])

    def test_200_que_no_se_parsea_no_cuenta(self):
        r = probe.run_probe(session=FakeSession(broken={"a.4cdn.org"}), sleep=lambda s: None)
        e = r["families"]["4chan_biz"]["endpoints"][0]
        self.assertEqual((e["status"], e["ok"]), (200, False))
        self.assertIn("parse_error", e)

    def test_error_de_red_no_corta_la_sonda(self):
        r = probe.run_probe(session=FakeSession(raises={"t.me"}), sleep=lambda s: None)
        e = r["families"]["telegram_web"]["endpoints"][0]
        self.assertEqual((e["status"], e["ok"]), ("error ConnectionError", False))
        self.assertTrue(r["families"]["hn_algolia"]["ok"])

    def test_pausas_entre_requests(self):
        pauses = []
        probe.run_probe(session=FakeSession(), sleep=pauses.append)
        n = sum(len(v[1]) for v in probe.SOURCES.values())
        self.assertEqual(len(pauses), n - 1)
        self.assertGreaterEqual(min(pauses), 2)
        reddit = [p for (_, eps) in [probe.SOURCES["reddit_rss"]] for *_, p in eps]
        self.assertTrue(all(p >= 10 for p in reddit))
        self.assertTrue(all(p >= 5 for *_, p in probe.SOURCES["telegram_web"][1]))

    def test_user_agent_ascii(self):
        # Con un User-Agent no ASCII, 4chan y Decrypt respondían 403 [V, 01/10]
        probe.HEADERS["User-Agent"].encode("ascii")
        session = FakeSession()
        probe.run_probe(session=session, quick=True, sleep=lambda s: None)
        self.assertTrue(all(h == probe.HEADERS for _, h in session.calls))

    def test_quick_un_endpoint_por_familia(self):
        session = FakeSession()
        probe.run_probe(session=session, quick=True, sleep=lambda s: None)
        self.assertEqual(len(session.calls), len(probe.SOURCES))

    def test_save_conserva_historial_acotado(self):
        tmp = Path(tempfile.mkdtemp(prefix="probe_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        path = tmp / "d" / "narrative_sources_probe.json"
        for _ in range(probe.HISTORY_MAX + 3):
            probe.save(probe.run_probe(session=FakeSession(), quick=True, sleep=lambda s: None), path)
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(data["history"]), probe.HISTORY_MAX)
        self.assertIn("families", data)
        self.assertEqual(data["history"][-1]["runner"], data["runner"])
        self.assertFalse(path.with_suffix(".json.tmp").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
