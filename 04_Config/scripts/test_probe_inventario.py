#!/usr/bin/env python3
"""Tests de probe_inventario (doc 28). unittest, sin red.

Uso: python 04_Config/scripts/test_probe_inventario.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import requests

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import probe_inventario as p  # noqa: E402

INVENTORY = json.loads((SCRIPTS.parent / "inventario.json").read_text(encoding="utf-8"))


class Resp:
    def __init__(self, status, body=b"{}", headers=None):
        self.status_code, self.content, self.headers = status, body, headers or {"content-type": "application/json"}


class Session:
    def __init__(self, routes):
        self.routes, self.calls = routes, []

    def _answer(self, url):
        for k, v in self.routes.items():
            if k in url:
                if isinstance(v, Exception):
                    raise v
                return v
        return Resp(200)

    def get(self, url, **kw):
        self.calls.append(("GET", url, None))
        return self._answer(url)

    def post(self, url, json=None, **kw):
        self.calls.append(("POST", url, json))
        return self._answer(url)


class InventarioTest(unittest.TestCase):
    def test_inventario_cumple_las_metas_de_la_fase_8(self):
        entries = INVENTORY["entries"]
        self.assertGreaterEqual(len(entries), 50)
        self.assertGreaterEqual(sum(1 for e in entries if e["probe"]), 30)
        self.assertEqual(sorted({g for e in entries for g in e["groups"]}), list("abcdefghi"))
        self.assertEqual(len({e["id"] for e in entries}), len(entries))          # ids únicos
        for e in entries:
            self.assertIn(e["priority"], ("P0", "P1", "P2", "P3"), e["id"])
            self.assertTrue(e["verified"].startswith(("[V]", "[P]")), e["id"])
            if e["probe"]:
                self.assertTrue(e["probe"].startswith(("https://", "http://")), e["id"])
        datasets = [e for e in entries if e["category"] == "datasets"]
        self.assertGreaterEqual(len(datasets), 2)

    def test_clasificacion(self):
        self.assertEqual(p.classify(200, '{"price": 1}'), "ok")
        self.assertEqual(p.classify(200, "Invalid API key"), "auth")
        self.assertEqual(p.classify(402, "Upgrade to the paid API plan"), "auth")
        self.assertEqual(p.classify(401, ""), "auth")
        self.assertEqual(p.classify(451, ""), "blocked")
        self.assertEqual(p.classify(429, ""), "rate_limited")
        self.assertEqual(p.classify(500, ""), "error")
        self.assertEqual(p.classify(200, "x" * 1000 + " api key"), "ok")       # una página larga que menciona keys

    def test_corrida_con_post_errores_y_resumen(self):
        inv = {"version": "t", "entries": [
            {"id": "a", "name": "A", "category": "precios", "probe": "https://a.test/x", "groups": ["h"]},
            {"id": "b", "name": "B", "category": "defi", "probe": "https://b.test/x", "groups": ["c"]},
            {"id": "c", "name": "C", "category": "gobernanza", "probe": "https://c.test/gql", "method": "POST",
             "body": {"query": "{x}"}, "groups": ["c"]},
            {"id": "d", "name": "D", "category": "mcp", "probe": None, "groups": []},
            {"id": "e", "name": "E", "category": "precios", "probe": "https://e.test/x", "groups": ["d"]}]}
        s = Session({"b.test": Resp(402, b"Upgrade to the paid API plan"), "e.test": requests.ConnectionError("x")})
        waits = []
        rep = p.run(session=s, sleep=waits.append, inventory=inv)
        self.assertEqual(rep["summary"]["probed"], 4)                            # d no tiene endpoint
        self.assertEqual(rep["summary"]["by_result"], {"ok": 2, "auth": 1, "error": 1})
        self.assertEqual(rep["summary"]["groups_with_ok_source"], ["c", "h"])
        self.assertIn(("POST", "https://c.test/gql", {"query": "{x}"}), s.calls)
        self.assertEqual(waits, [p.PAUSE_S] * 3)
        self.assertIn("body_head", next(r for r in rep["results"] if r["id"] == "b"))
        tmp = tempfile.mkdtemp()
        try:
            out = Path(tmp) / "probe.json"
            p.save(rep, out)
            p.save(rep, out)
            self.assertEqual(len(json.loads(out.read_text(encoding="utf-8"))["history"]), 2)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_user_agent_ascii(self):
        p.HEADERS["User-Agent"].encode("ascii")


if __name__ == "__main__":
    unittest.main(verbosity=2)
