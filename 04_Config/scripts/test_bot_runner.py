#!/usr/bin/env python3
"""Tests del ejecutor genérico de recetas (Ola 3): bot_runner. unittest, sin red (HTTP simulado).

Uso: python 04_Config/scripts/test_bot_runner.py
"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_runner as br  # noqa: E402
import lib_events as events  # noqa: E402

try:
    import bs4  # noqa: F401
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
# html_list y telegram_preview necesitan beautifulsoup4. Sin él, esos tests se saltan con el motivo a la vista.
# audit_gate corre con REQUIRE_TEST_DEPS=1: ahí faltar bs4 es una FALLA, nunca un salto silencioso (D-075).
requires_bs4 = unittest.skipUnless(HAS_BS4 or os.environ.get("REQUIRE_TEST_DEPS"),
                                   "beautifulsoup4 no instalado: pip install --require-hashes -r requirements-dev.txt")

T0 = 1791000000
MINT_A = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
MINT_B = "7cnqaJLZaSD1s2PchXuYjauGSk6c8Nuj9Zcd1V5aMdKU"
POOLS = {"results": [
    {"id": "PoolAAAA", "dex_id": "pumpfun", "dex_name": "Pump.fun", "created_at": "2026-10-03T03:58:00Z",
     "volume_usd_24h": 1234.5, "tokens": [{"id": MINT_A, "symbol": "PEPE"}, {"id": "So11111111111111111111111111111111111111112", "symbol": "SOL"}]},
    {"id": "PoolBBBB", "dex_id": "raydium", "dex_name": "Raydium", "created_at": "2026-10-03T03:59:00Z",
     "volume_usd_24h": 99.0, "tokens": [{"id": MINT_B, "symbol": "CAT"}]}]}
DEXP = {"name": "dexp_test", "kind": "json_api", "cadencia_min": 30, "grupo": "a",
        "url_base": "https://api.dexpaprika.com/networks/solana/pools/search?limit=50",
        "extractores": [{"items": "$.results[*]"}, {"id": "$.id"}, {"title": "$.dex_name"}, {"ts": "$.created_at"},
                        {"text": ["$.tokens[*].id", "$.tokens[*].symbol"]}, {"meta.volume_usd_24h": "$.volume_usd_24h"},
                        {"meta.dex": "$.dex_id"}]}
BTC_HTML = """<html><body><table>
<tr><td><span id="msg_1"><a href="https://bitcointalk.org/index.php?topic=1.0">Reglas del foro</a></span></td></tr>
<tr><td><span id="msg_2"><a href="index.php?topic=5550001.0">[ANN] Kitty Coin $KITTY — fair launch</a></span></td></tr>
<tr><td><span id="msg_3"><a href="index.php?topic=5550002.0">[ANN][PRESALE] Solar DePIN network</a></span></td></tr>
</table></body></html>"""
RSS = """<?xml version="1.0"?><rss><channel>
<item><title>Solana memecoin season returns</title><link>https://news.example/a</link><guid>a1</guid>
<pubDate>Sat, 03 Oct 2026 03:30:00 +0000</pubDate><description>pump.fun volumes</description></item>
</channel></rss>"""
TG = """<div class="tgme_widget_message" data-post="pumpfun/101"><div class="tgme_widget_message_text">New: $DOGE2
<a href="https://pump.fun/coin/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump">ver</a></div>
<span class="tgme_widget_message_views">1.2K</span><time datetime="2026-10-03T03:50:00+00:00"></time></div>"""


class FakeHTTP:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def __call__(self, url, headers=None):
        self.calls.append(url)
        for prefix, resp in self.responses.items():
            if url.startswith(prefix):
                return resp
        return 404, None, url


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="runner_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        (self.root / br.RECIPES_REL).mkdir(parents=True)

    def recipe(self, r, enabled=True):
        import yaml
        (self.root / br.RECIPES_REL / f"{r['name']}.yaml").write_text(yaml.safe_dump(r, allow_unicode=True),
                                                                        encoding="utf-8")
        st_path = self.root / br.RECIPES_REL / br.STATE_NAME
        st = json.loads(st_path.read_text(encoding="utf-8")) if st_path.exists() else {"recipes": {}}
        st["recipes"][r["name"]] = {"enabled": enabled}
        st_path.write_text(json.dumps(st), encoding="utf-8")
        return br.validate_recipe(r)

    def diary(self, name):
        p = self.root / "02_Analisis/sources" / name / "2026-10-03.jsonl"
        return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []


class Runner(Base):
    def test_plan_cadencia_y_habilitacion(self):
        self.recipe(DEXP)
        self.recipe(dict(DEXP, name="apagada"), enabled=False)
        self.recipe(dict(DEXP, name="lenta", cadencia_min=60))
        self.assertEqual(br.plan(self.root, now=T0), ["dexp_test", "lenta"])           # nunca corrieron
        for name, ago in (("dexp_test", 25 * 60), ("lenta", 25 * 60)):
            d = self.root / "02_Analisis/sources" / name
            d.mkdir(parents=True)
            (d / "_state.json").write_text(json.dumps({"last_run": T0 - ago}), encoding="utf-8")
        self.assertEqual(br.plan(self.root, now=T0), [])
        self.assertEqual(br.plan(self.root, now=T0 + 4 * 60), ["dexp_test"])           # 29 min: tolerancia de 2
        with self.assertRaises(ValueError):
            br.validate_recipe(dict(DEXP, name="rss"))                                 # carpeta de otro bot
        with self.assertRaises(ValueError):
            br.validate_recipe(dict(DEXP, url_base="http://inseguro.example/x", cadencia_min=5))

    def test_json_api_escribe_src1_y_deduplica(self):
        r = self.recipe(DEXP)
        http = FakeHTTP({"https://api.dexpaprika.com": (200, json.dumps(POOLS), DEXP["url_base"])})
        out = br.run_recipe(r, now=T0, fetch=http, root=self.root)
        recs = self.diary("dexp_test")
        self.assertEqual([x["id"] for x in recs], ["PoolAAAA", "PoolBBBB"])
        self.assertEqual((recs[0]["v"], recs[0]["kind"], recs[0]["bot"], recs[0]["title"]),
                         ("src-1", "token", "dexp_test", "Pump.fun"))
        self.assertIn(MINT_A, recs[0]["a"])
        self.assertEqual(recs[0]["m"], {"volume_usd_24h": 1234.5, "dex": "pumpfun", "grupo": "a"})
        self.assertEqual(recs[0]["ts"], 1790999880)
        self.assertNotIn("text", recs[0])                                              # src-1: sin cuerpo
        self.assertEqual((out["state"]["new"], out["state"]["fails"]), (2, 0))
        again = br.run_recipe(r, now=T0 + 1800, fetch=http, root=self.root)
        self.assertEqual(again["state"]["new"], 0)
        self.assertEqual(len(self.diary("dexp_test")), 2)
        st = json.loads((self.root / "02_Analisis/sources/dexp_test/_state.json").read_text(encoding="utf-8"))
        self.assertEqual((st["last_run"], st["items"], st["status"]), (T0 + 1800, 2, 200))
        self.assertTrue((self.root / "02_Analisis/sources/dexp_test/_audit.jsonl").exists())
        self.assertEqual(br.jsonpath(POOLS, "$.results[1].tokens[0]['symbol']"), ["CAT"])

    @requires_bs4
    def test_html_list_con_selectores_css(self):
        r = self.recipe({"name": "btc_ann", "kind": "html_list", "cadencia_min": 60, "grupo": "f",
                         "url_base": "https://bitcointalk.org/index.php?board=159.0", "src_kind": "post",
                         "extractores": {"items": "span[id^=msg_] > a", "id": "@href", "url": "@href", "title": "."}})
        http = FakeHTTP({"https://bitcointalk.org": (200, BTC_HTML, "https://bitcointalk.org/index.php?board=159.0")})
        br.run_recipe(r, now=T0, fetch=http, root=self.root)
        recs = self.diary("btc_ann")
        self.assertEqual(len(recs), 3)
        self.assertEqual(recs[1]["url"], "https://bitcointalk.org/index.php?topic=5550001.0")   # relativa → absoluta
        self.assertEqual(recs[1]["c"], ["KITTY"])
        self.assertIn("presale", recs[2]["k"])

    def test_rss_sin_dependencias(self):
        rss = self.recipe({"name": "rss_extra", "kind": "rss", "cadencia_min": 20, "grupo": "a",
                           "url_base": "https://news.example/feed.xml"})
        br.run_recipe(rss, now=T0, fetch=FakeHTTP({"https://news.example": (200, RSS, rss["url_base"])}),
                      root=self.root)
        (n,) = self.diary("rss_extra")
        self.assertEqual((n["kind"], n["url"], n["ts"]), ("news", "https://news.example/a", 1790998200))
        self.assertTrue({"solana", "memecoin", "pump.fun"} <= set(n["k"]))

    def test_dependencia_faltante_no_se_disfraza_de_receta_vacia(self):
        """D-075: sin bs4, collect() antes devolvía 0 ítems con status parse_error; ahora el ImportError sube."""
        from unittest import mock
        r = br.validate_recipe({"name": "btc_ann", "kind": "html_list", "cadencia_min": 60,
                                "url_base": "https://bitcointalk.org/index.php?board=159.0",
                                "extractores": {"items": "span > a", "id": "@href"}})
        http = FakeHTTP({"https://bitcointalk.org": (200, BTC_HTML, r["url_base"])})
        with mock.patch.dict(sys.modules, {"bs4": None}):
            with self.assertRaises(ImportError):
                br.collect(r, now=T0, fetch=http, root=self.root)
        self.assertFalse((self.root / "02_Analisis/sources/btc_ann/_state.json").exists())    # no deja estado falso

    @requires_bs4
    def test_telegram_preview(self):
        tg = self.recipe({"name": "tg_pump", "kind": "telegram_preview", "cadencia_min": 30, "grupo": "a",
                          "url_base": "https://t.me/s/pumpfun"})
        br.run_recipe(tg, now=T0, fetch=FakeHTTP({"https://t.me/s/pumpfun": (200, TG, tg["url_base"])}),
                      root=self.root)
        (m,) = self.diary("tg_pump")
        self.assertEqual((m["kind"], m["id"], m["url"], m["m"]["views"]),
                         ("message", "pumpfun/101", "https://t.me/pumpfun/101", 1200))
        self.assertIn(MINT_A, m["a"])
        self.assertIsNone(m["title"])                                                   # mensajes: sin título

    def test_errores_429_y_secreto_faltante(self):
        r = self.recipe(DEXP)
        br.run_recipe(r, now=T0, fetch=FakeHTTP({"https://api.dexpaprika.com": (500, None, "x")}), root=self.root)
        out = br.run_recipe(r, now=T0 + 1800, fetch=FakeHTTP({"https://api": (429, None, "x")}), root=self.root)
        self.assertEqual((out["state"]["fails"], out["state"]["status"], out["state"]["new"]), (2, 429, 0))
        (sat,) = events.read_events(types="fuente_saturada", now=T0 + 1801, root=self.root)
        self.assertEqual((sat["subject"], sat["writer"]), ("recipe/dexp_test", "runner_dexp_test"))
        hel = self.recipe({"name": "helius_test", "kind": "json_api", "cadencia_min": 30, "secreto": "HELIUS_TEST_KEY",
                           "url_base": "https://api.helius.xyz/v0/x?api-key={secreto}",
                           "extractores": {"items": "$[*]", "id": "$.signature"}})
        os.environ.pop("HELIUS_TEST_KEY", None)
        http = FakeHTTP({})
        st = br.run_recipe(hel, now=T0, fetch=http, root=self.root)["state"]
        self.assertEqual((st["status"], http.calls), ("sin_secreto", []))               # sin secret no hay request
        self.assertNotIn("api-key", json.dumps(st))                                     # el secreto nunca se guarda

    def test_sujetos_desde_eventos_y_jsonpath_sobre_dict(self):
        gp = self.recipe({"name": "goplus_test", "kind": "json_api", "cadencia_min": 60, "grupo": "a",
                          "url_base": "https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses={subjects}",
                          "sujetos": {"tipo": "pump_naciente", "max": 10, "prueba": [MINT_A]},
                          "extractores": {"items": "$.result.*", "id": "$._key", "title": "$.metadata.name",
                                          "text": "$._key", "meta.mintable": "$.mintable.status",
                                          "meta.freezable": "$.freezable.status"}})
        idle = br.run_recipe(gp, now=T0, fetch=FakeHTTP({}), root=self.root)["state"]
        self.assertEqual((idle["status"], idle["fails"]), ("sin_sujetos", 0))          # sin sujetos no es falla
        events.write_event("pump_naciente", MINT_A, 2, writer="early_watch_a", now=T0 + 60, root=self.root)
        events.write_event("pump_naciente", MINT_B, 2, writer="early_watch_b", now=T0 + 90, root=self.root)
        body = {"code": 1, "result": {MINT_A: {"mintable": {"status": "0"}, "freezable": {"status": "1"},
                                               "metadata": {"name": "Pepe"}},
                                      MINT_B: {"mintable": {"status": "1"}, "freezable": {"status": "0"},
                                               "metadata": {"name": "Cat"}}}}
        http = FakeHTTP({"https://api.gopluslabs.io": (200, json.dumps(body), "x")})
        br.run_recipe(gp, now=T0 + 120, fetch=http, root=self.root)
        self.assertEqual(http.calls, [gp["url_base"].replace("{subjects}", f"{MINT_B},{MINT_A}")])
        recs = {x["id"]: x for x in self.diary("goplus_test")}
        self.assertEqual(recs[MINT_A]["m"]["freezable"], "1")
        self.assertEqual(recs[MINT_B]["a"], [MINT_B])
        items, info = br.collect(gp, now=T0, fetch=http, root=self.root, sample_subjects=True)
        self.assertEqual(info["status"], 200)                                           # validación con `prueba`


if __name__ == "__main__":
    unittest.main(verbosity=2)
