#!/usr/bin/env python3
"""Tests de bot_influencer_tracker (D-087): parsing, dedup, falla de una cuenta, rate limit, frescura, eventos,
configuración y corrida completa. unittest, sin red (HTTP simulado).

Uso: python 04_Config/scripts/test_bot_influencer_tracker.py
"""
import json
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_influencer_tracker as bit  # noqa: E402
import lib_events as events  # noqa: E402
import lib_sources_store as store  # noqa: E402

T0 = 1791000000
H, D = 3600, 86400
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
MINT2 = "7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr"
WALLET = "BKJ45do3q1VhmfccH51oEQkWbqCfWrtwFxTmYnC8vzz5"
FX = "https://api.fxtwitter.com/2/profile/{}/statuses"
SY = "https://syndication.twitter.com/srv/timeline-profile/screen-name/{}"


def cfg(cuentas, **kw):
    doc = {"pause_s": 0, "mecanismos": ["fxembed"], "cashtags_mayores": ["BTC", "ETH"], **kw,
           "cuentas": [{"cuenta": c, "categoria": cat, "prioridad": p} for c, cat, p in cuentas]}
    return bit.validate_config(doc)


def fx_post(pid, ts, text="", author=None, repost=False, likes=10):
    return {"id": str(pid), "created_timestamp": ts, "text": text, "author": {"screen_name": author or "x"},
            "reposted_by": {"screen_name": "x"} if repost else None, "likes": likes, "reposts": 2, "replies": 1,
            "views": 100}


def fx_body(cuenta, posts):
    for p in posts:
        if (p.get("author") or {}).get("screen_name") == "x" and not p.get("reposted_by"):
            p["author"]["screen_name"] = cuenta
    return json.dumps({"code": 200, "results": posts})


def tw_date(ts):
    return time.strftime("%a %b %d %H:%M:%S +0000 %Y", time.gmtime(ts))


def sy_body(cuenta, tweets):
    """tweets: [(id, ts, texto, urls {t.co: expandida}, autor_original|None)]."""
    entries = []
    for pid, ts, text, urls, rt in tweets:
        tw = {"id_str": str(pid), "created_at": tw_date(ts), "full_text": text, "user": {"screen_name": cuenta},
              "entities": {"urls": [{"url": k, "expanded_url": v} for k, v in (urls or {}).items()]},
              "favorite_count": 5, "retweet_count": 1, "reply_count": 0}
        if rt:
            tw["retweeted_status"] = {**tw, "user": {"screen_name": rt}}
        entries.append({"type": "tweet", "content": {"tweet": tw}})
    data = {"props": {"pageProps": {"timeline": {"entries": entries}}}}
    return f'<html><script id="__NEXT_DATA__" type="application/json">{json.dumps(data)}</script></html>'


class Http:
    """fetch simulado: {url: (estado, cuerpo, cabeceras)} o callable(url); cuenta las llamadas por URL."""

    def __init__(self, routes):
        self.routes, self.calls = routes, []

    def __call__(self, url):
        self.calls.append(url)
        r = self.routes(url) if callable(self.routes) else self.routes.get(url, (404, None, {}))
        status, body, headers = r
        return status, (body if status == 200 else None), headers

    def count(self, prefix):
        return sum(1 for u in self.calls if u.startswith(prefix))


class TestParsing(unittest.TestCase):
    def test_1_fxembed_syndication_y_extraccion(self):
        posts = bit.parse_fxembed(fx_body("lookonchain", [
            fx_post(1, T0 - 60, f"Whale bought $WIF https://pump.fun/coin/{MINT} via https://arkm.com/explorer/address/{WALLET}"),
            fx_post(2, T0 - 120, "rt de otro", author="otro", repost=True),
            {"id": "no-numérico", "text": "x"}]), "lookonchain")
        self.assertEqual([p["id"] for p in posts], ["1", "2"])
        self.assertEqual((posts[0]["ts"], posts[0]["likes"], posts[0]["repost"]), (T0 - 60, 10, False))
        self.assertTrue(posts[1]["repost"])
        urls, tok = bit.post_fields(posts[0]["text"])
        self.assertEqual(tok, [MINT])                                    # la wallet del explorador no es token
        self.assertIn(f"https://arkm.com/explorer/address/{WALLET}", urls)
        # syndication: repost (retweeted_status), t.co expandido, "CA:" y sufijo de launchpad
        sy = bit.parse_syndication(sy_body("solana", [
            (10, T0 - 30, "nuevo listado https://t.co/abc", {"https://t.co/abc": f"https://dexscreener.com/solana/{MINT2}"}, None),
            (11, T0 - 90, f"CA: {MINT2} y {MINT}", None, "fundador")]), "solana")
        self.assertEqual([(p["id"], p["repost"], p["author"]) for p in sy], [("10", False, "solana"), ("11", True, "fundador")])
        self.assertEqual(sy[0]["ts"], T0 - 30)
        self.assertIn(f"https://dexscreener.com/solana/{MINT2}", sy[0]["text"])
        self.assertEqual(bit.post_fields(sy[0]["text"])[1], [MINT2])
        self.assertEqual(sorted(bit.post_fields(sy[1]["text"])[1]), sorted([MINT2, MINT]))
        self.assertEqual(bit.post_fields("media https://t.co/zzz")[0], [])     # t.co sin expandir: fuera
        self.assertEqual(bit.parse_syndication(sy_body("vacia", []), "vacia"), [])
        for bad in ("<html>sin datos</html>", '<script id="__NEXT_DATA__" type="application/json">{"props": {}}</script>'):
            with self.assertRaises(ValueError):
                bit.parse_syndication(bad, "x")
        with self.assertRaises(ValueError):
            bit.parse_fxembed("<html>bloqueo</html>", "x")
        with self.assertRaises(ValueError):
            bit.parse_fxembed('{"code": 200}', "x")


class TestRun(unittest.TestCase):
    def test_2_dedup_por_id_y_ventana(self):
        c = cfg([("a", "cex", 1), ("b", "narrativa", 3)])
        http = Http({FX.format("a"): (200, fx_body("a", [fx_post(1, T0 - 600, "$WIF"), fx_post(2, T0 - 900),
                                                          fx_post(3, T0 - 3 * D, "fijado viejo")]), {}),
                     FX.format("b"): (200, fx_body("b", [fx_post(1, T0 - 600, "$WIF", author="a", repost=True)]), {})})
        recs, _, st = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None)
        self.assertEqual(sorted(r["id"] for r in recs), ["1", "2"])        # el repost de b es el mismo id; el viejo no
        self.assertEqual((st["sources"]["a"]["fresh"], st["sources"]["a"]["new"]), (2, 2))
        self.assertEqual((st["sources"]["b"]["fresh"], st["sources"]["b"]["new"]), (1, 0))
        r = next(x for x in recs if x["id"] == "1")
        self.assertEqual((r["v"], r["kind"], r["src"], r["c"], r["url"]), ("src-1", "tweet", "a", ["WIF"], "https://x.com/i/status/1"))
        self.assertNotIn("text", r)                                        # src-1: el texto no se guarda
        self.assertIsNone(r["title"])
        self.assertEqual((r["m"]["prio"], r["m"]["mec"], r["m"]["likes"]), (1, "fxembed", 10))
        recs2, _, st2 = bit.run(c, st, fetch=http, now=T0 + 1800, sleep=lambda s: None)
        self.assertEqual(recs2, [])                                        # segunda corrida: nada nuevo
        _, _, st3 = bit.run(c, st2, fetch=http, now=T0 + 73 * H, sleep=lambda s: None)
        self.assertEqual(st3["seen"], {})                                  # ids fuera de dedup_hours se olvidan…
        self.assertEqual(st3["items_last_run"], 0)                         # …y lo viejo tampoco vuelve (max_age_h)

    def test_3_falla_de_una_cuenta_no_corta_y_auto_off(self):
        c = cfg([("caida", "cex", 1), ("sana", "cex", 1), ("renombrada", "solana", 2)],
                mecanismos=["fxembed", "syndication"])
        routes = {FX.format("caida"): (500, None, {}), SY.format("caida"): ("error ConnectTimeout", None, {}),
                  FX.format("sana"): (200, fx_body("sana", [fx_post(5, T0 - 60)]), {}),
                  FX.format("renombrada"): (404, None, {}), SY.format("renombrada"): (200, sy_body("renombrada", []), {})}
        http = Http(routes)
        st = {}
        for i in range(3):
            recs, _, st = bit.run(c, st, fetch=http, now=T0 + i * 1800, sleep=lambda s: None)
            if i == 0:
                self.assertEqual([r["id"] for r in recs], ["5"])           # la caída no corta a la sana
        caida, ren = st["sources"]["caida"], st["sources"]["renombrada"]
        self.assertEqual((caida["status"], caida["fails"]), (500, 3))
        self.assertEqual(caida["errores"], {"fxembed": 500, "syndication": "error ConnectTimeout"})
        self.assertEqual(caida["auto_off_until"], T0 + 3600 + 6 * H)       # 3 fallas: apagada 6 h
        self.assertEqual((ren["status"], ren["fails"]), (404, 3))          # 404 + timeline vacío = handle muerto
        self.assertEqual(st["sources"]["sana"]["fails"], 0)
        before = http.count(FX.format("caida"))
        _, _, st = bit.run(c, st, fetch=http, now=T0 + 2 * H, sleep=lambda s: None)
        self.assertEqual(http.count(FX.format("caida")), before)           # apagada: no se consulta
        _, _, st = bit.run(c, st, fetch=http, now=T0 + 8 * H, sleep=lambda s: None)
        self.assertEqual(http.count(FX.format("caida")), before + 1)       # vence el auto_off: reintenta
        n = http.count(FX.format("sana"))
        bit.run(c, st, fetch=http, now=T0 + 9 * H, sleep=lambda s: None, auto_off={"sana": {"until": T0 + 10 * H}})
        self.assertEqual(http.count(FX.format("sana")), n)                 # auto_off de bot_self_repair respetado

    def test_4_rate_limit_429_y_cupo(self):
        c = cfg([("a", "cex", 1), ("b", "cex", 2), ("c", "narrativa", 3)], mecanismos=["fxembed", "syndication"],
                syndication_max_por_corrida=2)
        fresh = lambda name, pid: (200, sy_body(name, [(pid, T0 - 60, "hola", None, None)]), {"x-rate-limit-remaining": "20"})
        routes = {FX.format(n): (429, None, {"x-rate-limit-reset": str(T0 + 600)}) for n in "abc"}
        routes.update({SY.format("a"): fresh("a", 1), SY.format("b"): fresh("b", 2), SY.format("c"): fresh("c", 3)})
        http = Http(routes)
        recs, _, st = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None)
        self.assertEqual(http.count("https://api.fxtwitter.com"), 1)       # un 429 y no se insiste en la corrida
        self.assertEqual(st["rate_limit"], {"fxembed": T0 + 600})
        self.assertEqual(sorted(r["id"] for r in recs), ["1", "2"])        # a y b por syndication (cupo 2)
        self.assertEqual((st["sources"]["a"]["mec"], st["sources"]["b"]["mec"]), ("syndication", "syndication"))
        self.assertNotIn("c", st["sources"])                               # c: sin cupo ni fxembed → la próxima, sin falla
        # antes del reset no se llama a fxembed; un remaining <= 1 corta syndication sin esperar el 429
        routes[SY.format("a")] = (200, sy_body("a", [(1, T0 - 60, "hola", None, None)]), {"x-rate-limit-remaining": "1",
                                                                                           "x-rate-limit-reset": str(T0 + 900)})
        http2 = Http(routes)
        _, _, st2 = bit.run(c, st, fetch=http2, now=T0 + 300, sleep=lambda s: None)
        self.assertEqual(http2.count("https://api.fxtwitter.com"), 0)      # fxembed sigue limitado hasta su reset
        self.assertEqual(http2.calls, [SY.format("a")])                    # remaining 1: se frena sin esperar el 429
        self.assertEqual(st2["rate_limit"], {"fxembed": T0 + 600, "syndication": T0 + 900})
        self.assertEqual((st2["sources"]["a"]["status"], st2["sources"]["a"]["checked_at"]), (200, T0 + 300))
        self.assertEqual((st2["sources"]["b"]["checked_at"], st2["sources"]["b"]["fails"]), (T0, 0))   # b sin tocar
        # pasado el reset de ambos, fxembed vuelve a ser el primero
        routes.update({FX.format(n): (200, fx_body(n, []), {}) for n in "abc"})
        http3 = Http(routes)
        _, _, st3 = bit.run(c, st2, fetch=http3, now=T0 + 1000, sleep=lambda s: None)
        self.assertNotIn("fxembed", st3["rate_limit"])                     # límites vencidos se descartan
        self.assertTrue(http3.calls[0].startswith("https://api.fxtwitter.com"))

    def test_5_frescura_y_mecanismo_de_respaldo(self):
        c = cfg([("vieja", "narrativa", 3), ("congelada", "narrativa", 3), ("vacia", "depin", 3)],
                mecanismos=["fxembed", "syndication"])
        routes = {FX.format("vieja"): (200, fx_body("vieja", [fx_post(1, T0 - 40 * D)]), {}),
                  SY.format("vieja"): (200, sy_body("vieja", [(2, T0 - 120, "hoy", None, None)]), {}),
                  FX.format("congelada"): (200, fx_body("congelada", [fx_post(3, T0 - 20 * D)]), {}),
                  SY.format("congelada"): (200, sy_body("congelada", [(4, T0 - 330 * D, "viejo", None, None)]), {}),
                  FX.format("vacia"): (200, fx_body("vacia", []), {}), SY.format("vacia"): (200, sy_body("vacia", []), {})}
        http = Http(routes)
        recs, _, st = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None)
        s = st["sources"]
        self.assertEqual((s["vieja"]["mec"], s["vieja"]["estado"], [r["id"] for r in recs]), ("syndication", "vivo", ["2"]))
        self.assertEqual((s["congelada"]["mec"], s["congelada"]["estado"]), ("fxembed", "lento"))   # la más fresca de las dos
        self.assertEqual(s["congelada"]["next_check"], T0 + 6 * H)
        self.assertEqual((s["vacia"]["status"], s["vacia"]["estado"], s["vacia"]["next_check"]), (200, "vacio", T0 + D))
        n = len(http.calls)
        bit.run(c, st, fetch=http, now=T0 + H, sleep=lambda s: None)
        self.assertEqual(len(http.calls) - n, 2)                           # solo la viva (fx viejo → syndication)
        self.assertEqual(bit.estado_de([{"ts": T0 - 31 * D}], T0, 7), "congelado")


class TestEventos(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="xinf_ev_"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_6_eventos_tweet_mencion_keyword(self):
        c = cfg([("ballenas", "analista_onchain", 1), ("analista", "investigador", 2), ("sector", "depin", 3)])
        http = Http({FX.format("ballenas"): (200, fx_body("ballenas", [
                        fx_post(1, T0 - 600, f"$WIF launch CA: {MINT}"), fx_post(9, T0 - 5 * H, "$OLD")]), {}),
                     FX.format("analista"): (200, fx_body("analista", [fx_post(2, T0 - 300, "$wif airdrop launch")]), {}),
                     FX.format("sector"): (200, fx_body("sector", [fx_post(3, T0 - 60, "$BTC launch")]), {})})
        recs, evs, _ = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None, keywords=("launch", "airdrop"))
        self.assertEqual(len(recs), 4)                                     # el de hace 5 h se registra…
        by = {(e[0], e[1]): e for e in evs}
        self.assertNotIn(("tweet_influencer", "9"), by)                    # …pero no emite (event_max_age_h = 2)
        self.assertNotIn(("mencion_token", "$OLD"), by)
        self.assertEqual([by[("tweet_influencer", p)][2] for p in "123"], [2, 1, 0])
        self.assertEqual(by[("tweet_influencer", "1")][3]["tok"], [MINT])
        wif = by[("mencion_token", "$WIF")]
        self.assertEqual((wif[2], wif[3]["n_cuentas"], wif[3]["cuentas"], wif[3]["tipo"]), (2, 2, ["ballenas", "analista"], "cashtag"))
        self.assertEqual(by[("mencion_token", "$BTC")][2], 0)              # mayores: severidad 0
        self.assertEqual((by[("mencion_token", MINT)][2], by[("mencion_token", MINT)][3]["tipo"]), (2, "contrato"))
        launch = by[("keyword_narrativa", "launch")]
        self.assertEqual((launch[2], launch[3]["n_cuentas"]), (1, 3))
        self.assertEqual(by[("keyword_narrativa", "airdrop")][2], 0)
        written = events.write_events(evs, writer=bit.WRITER, now=T0, root=self.tmp)
        self.assertEqual(len(written), len(evs))
        self.assertTrue(all(e["writer"] == "x_influencers" for e in written))
        self.assertEqual(events.write_events(evs, writer=bit.WRITER, now=T0 + 60, root=self.tmp), [])   # mismo id
        got = events.read_events(types=["mencion_token"], now=T0 + 60, root=self.tmp)
        self.assertEqual(sorted(e["subject"] for e in got), sorted(["$WIF", "$BTC", MINT]))


class TestConfigYMain(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="xinf_main_"))
        self._root, self._http = store.ROOT, bit.http_get

    def tearDown(self):
        store.ROOT, bit.http_get = self._root, self._http
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_7_configuracion(self):
        real = bit.load_config(bit.config_path(SCRIPTS.parents[1]))
        on = [x for x in real["cuentas"] if x.get("enabled", True) is not False]
        self.assertEqual(len(on), 50)
        self.assertEqual(len({x["cuenta"].lower() for x in real["cuentas"]}), len(real["cuentas"]))
        self.assertTrue({"toly", "pumpfun", "mert", "lookonchain", "binance", "HyperliquidX"} <= {x["cuenta"] for x in on})
        self.assertFalse({"aeyakovenko", "pumpdotfun", "0xMert_", "spotonchain"} & {x["cuenta"] for x in real["cuentas"]})
        self.assertEqual(real["mecanismos"], ["fxembed", "syndication"])
        self.assertTrue(all(x["prioridad"] in (1, 2, 3) and x["categoria"] in bit.CATEGORIAS for x in real["cuentas"]))
        ok = {"cuenta": "a", "categoria": "cex", "prioridad": 1}
        for bad in ({}, {"cuentas": [ok, {**ok, "cuenta": "A"}]}, {"cuentas": [{**ok, "categoria": "otra"}]},
                    {"cuentas": [{**ok, "prioridad": 4}]}, {"cuentas": [{**ok, "cuenta": "con espacio"}]},
                    {"cuentas": [ok], "mecanismos": ["nitter"]}, {"cuentas": [ok], "mecanismos": []}):
            with self.assertRaises(ValueError, msg=bad):
                bit.validate_config(bad)

    def test_8_main_escribe_diario_estado_eventos_y_auditoria(self):
        now = time.time()
        (self.tmp / "04_Config").mkdir()
        (self.tmp / "04_Config" / "influencers.yaml").write_text(
            "pause_s: 0\nmecanismos: [fxembed]\ncuentas:\n"
            "  - {cuenta: lookonchain, categoria: analista_onchain, prioridad: 1}\n"
            "  - {cuenta: apagada, categoria: cex, prioridad: 2, enabled: false}\n", encoding="utf-8")
        secret_text = "Whale texto completo que no debe quedar en disco $WIF"
        http = Http({FX.format("lookonchain"): (200, fx_body("lookonchain", [fx_post(7, int(now) - 60, secret_text)]), {})})
        store.ROOT, bit.http_get = self.tmp, http
        self.assertEqual(bit.main(["--dry-run"]), 0)
        self.assertFalse((self.tmp / "02_Analisis").exists())              # dry-run: no escribe nada
        self.assertEqual(bit.main([]), 0)
        self.assertEqual(http.calls, [FX.format("lookonchain"), FX.format("lookonchain")])   # la apagada no se consulta
        folder = self.tmp / "02_Analisis" / "sources" / "x_influencers"
        diaries = sorted(folder.glob("20*.jsonl"))
        self.assertEqual(len(diaries), 1)
        raw = diaries[0].read_text(encoding="utf-8")
        self.assertNotIn("texto completo", raw)
        rec = json.loads(raw.splitlines()[0])
        self.assertEqual((rec["id"], rec["c"], rec["src"]), ("7", ["WIF"], "lookonchain"))
        st = json.loads((folder / "_state.json").read_text(encoding="utf-8"))
        self.assertEqual((st["sources"]["lookonchain"]["status"], st["items_last_run"], st["events_last_run"]), (200, 1, 2))
        self.assertIn("7", st["seen"])
        self.assertTrue((folder / "_audit.jsonl").exists() and (folder / "_metrics.json").exists())
        evs = sorted((self.tmp / "02_Analisis" / "events" / "x_influencers").glob("*.jsonl"))
        self.assertEqual(len(evs), 1)
        self.assertEqual(sorted(json.loads(x)["type"] for x in evs[0].read_text(encoding="utf-8").splitlines()),
                         ["mencion_token", "tweet_influencer"])
        self.assertEqual(bit.main([]), 0)                                  # segunda corrida: dedup, nada nuevo
        self.assertEqual(len(diaries[0].read_text(encoding="utf-8").splitlines()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
