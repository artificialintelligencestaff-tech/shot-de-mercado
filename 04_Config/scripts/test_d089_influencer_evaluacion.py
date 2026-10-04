#!/usr/bin/env python3
"""Tests de D-089-R en bot_influencer_tracker: frescura, aporte, marcado `evaluar` (y `marginal` por mecanismo),
NO eliminación automática, y extracto + sha256 para casi-duplicados. unittest, sin red (HTTP simulado).

Uso: python 04_Config/scripts/test_d089_influencer_evaluacion.py
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
import lib_sources_store as store  # noqa: E402
from test_bot_influencer_tracker import FX, SY, MINT, MINT2, T0, D, H, Http, cfg, fx_body, fx_post, sy_body  # noqa: E402

VIG = {"symbols": {"HNT", "UDR", "NEWT", "BTC"}, "contracts": {MINT2}, "fuentes": {"test": 4}}


def rec(src, pid, ts, c=(), tok=(), a=()):
    return {"v": "src-1", "src": src, "id": str(pid), "ts": ts, "c": list(c), "a": list(a), "m": {"tok": list(tok)}}


class TestEvaluacion(unittest.TestCase):
    def test_1_frescura(self):
        self.assertEqual([bit.frescura_score(d) for d in (None, 0, 6.9, 7, 30, 30.1, 400)],
                         [0.2, 1.0, 1.0, 0.5, 0.5, 0.2, 0.2])
        c = cfg([("nueva", "cex", 1), ("lenta", "rwa", 3), ("dormida", "depin", 3)])
        routes = {FX.format("nueva"): (200, fx_body("nueva", [fx_post(1, T0 - 2 * H)]), {}),
                  FX.format("lenta"): (200, fx_body("lenta", [fx_post(2, T0 - 10 * D)]), {}),
                  FX.format("dormida"): (200, fx_body("dormida", [fx_post(3, T0 - 45 * D), fx_post(4, T0 - 900 * D)]), {})}
        recs, _, st = bit.run(c, {}, fetch=Http(routes), now=T0, sleep=lambda s: None, vig=VIG)
        s = st["sources"]
        self.assertEqual([(s[k]["dias_desde_ultimo_post"], s[k]["frescura_score"]) for k in ("nueva", "lenta", "dormida")],
                         [(0.1, 1.0), (10.0, 0.5), (45.0, 0.2)])
        self.assertEqual(s["dormida"]["posts_30d"], 0)                     # el de 45 d no entra en la ventana…
        self.assertEqual(s["dormida"]["ultimo_post_ts"], T0 - 45 * D)      # …pero sí cuenta como último post
        self.assertEqual(sorted(r["id"] for r in recs), ["1", "2"])
        routes[FX.format("lenta")] = (500, None, {})                       # si después falla, el dato no se pierde
        _, _, st2 = bit.run(c, st, fetch=Http(routes), now=T0 + 7 * H, sleep=lambda s: None, vig=VIG, history=recs)
        self.assertEqual((st2["sources"]["lenta"]["status"], st2["sources"]["lenta"]["ultimo_post_ts"]), (500, T0 - 10 * D))
        self.assertEqual(st2["sources"]["lenta"]["dias_desde_ultimo_post"], 10.3)

    def test_2_aporte_y_activos_vigentes(self):
        tmp = Path(tempfile.mkdtemp(prefix="xinf_vig_"))
        try:
            a = tmp / "02_Analisis"
            for sub in ("prelaunch", "alerts", "multichain", "early"):
                (a / sub).mkdir(parents=True)
            (a / "prelaunch" / "_calendar.json").write_text(json.dumps({"assets": {
                "sym:NEWT": {"symbol": "NEWT", "state": "anunciado"},
                "sym:OLD": {"symbol": "OLD", "state": "purgado"},
                "c:x": {"symbol": "BORN", "state": "seguimiento", "born": {"contract": MINT}}}}), encoding="utf-8")
            day = lambda ts: time.strftime("%Y-%m-%d_%H%M%S", time.gmtime(ts))
            (a / "alerts" / "_all_alerts.json").write_text(json.dumps([
                {"timestamp": day(T0 - 2 * D), "symbol": "UDR", "mint": MINT2},
                {"timestamp": day(T0 - 40 * D), "symbol": "VIEJO", "mint": "So1viejo1111111111111111111111111111111111"}]),
                encoding="utf-8")
            (a / "multichain" / "scan_latest.json").write_text(json.dumps({
                "groups": {"e": {"items": [{"symbol": "HNT"}]}},
                "onchain": {"solana": {"items": [{"symbol": "CARNAGE", "token_address": "AVKpeeWaCku3Mni5THbY4bkBn5dQrEXgmTzmAPEMwMDJ"}]}},
                "accelerating": [{"symbol": "CRAWL"}]}), encoding="utf-8")
            (a / "multichain" / "_perps.json").write_text(json.dumps({"perps": {"kPEPE": {}, "1000BONK": {}, "HYPE": {}}}),
                                                          encoding="utf-8")
            (a / "early" / "_watch_a.json").write_text(json.dumps({"top": [{"mint": MINT, "score": 24}]}), encoding="utf-8")
            vig = bit.vigentes(tmp, T0)
            self.assertTrue({"NEWT", "BORN", "UDR", "HNT", "CARNAGE", "CRAWL", "PEPE", "BONK", "HYPE"} <= vig["symbols"])
            self.assertFalse({"OLD", "VIEJO", "KPEPE"} & vig["symbols"])   # purgado, alerta vieja, prefijo de perp
            self.assertTrue({MINT, MINT2} <= vig["contracts"])
            self.assertEqual(sorted(vig["fuentes"]), ["alertas", "calendario", "early_watch", "multichain", "perps"])
            self.assertEqual(bit.vigentes(tmp / "no_existe", T0)["symbols"], set())    # sin archivos: vacío, sin error
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        majors = {"BTC", "ETH"}
        self.assertTrue(bit.tiene_aporte(rec("x", 1, T0, c=["NEWT"]), VIG, majors))
        self.assertFalse(bit.tiene_aporte(rec("x", 1, T0, c=["RANDOM"]), VIG, majors))
        self.assertFalse(bit.tiene_aporte(rec("x", 1, T0, c=["BTC"]), VIG, majors))       # vigente pero mayor
        self.assertTrue(bit.tiene_aporte(rec("x", 1, T0, tok=[MINT]), VIG, majors))        # contrato: siempre
        self.assertTrue(bit.tiene_aporte(rec("x", 1, T0, a=[MINT2]), VIG, majors))         # dirección vigente
        c = cfg([("anal", "analista_onchain", 1)])
        http = Http({FX.format("anal"): (200, fx_body("anal", [fx_post(1, T0 - H, "$HNT sube"), fx_post(2, T0 - 2 * H, "$RANDOM"),
                                                                fx_post(3, T0 - 3 * H, f"CA: {MINT}"), fx_post(4, T0 - 4 * H, "$BTC")]), {})})
        history = [rec("anal", 10, T0 - 20 * D, c=["UDR"]), rec("anal", 11, T0 - 35 * D, c=["NEWT"]),
                   rec("anal", 1, T0 - H, c=["HNT"])]                    # el 1 ya estaba en los diarios: cuenta una vez
        _, _, st = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None, vig=VIG, history=history)
        r = st["sources"]["anal"]
        self.assertEqual((r["posts_30d"], r["aporte_estimado"]), (5, 3))  # 1, 2, 3, 4, 10 · aporte: HNT, CA, UDR

    def test_3_marcado_evaluar_y_mecanismo_marginal(self):
        c = cfg([("vieja", "narrativa", 3), ("ruidosa", "noticias", 2), ("diez", "noticias", 2),
                 ("util", "noticias", 2), ("rota", "cex", 1), ("eco", "noticias", 2), ("sin_turno", "rwa", 3)],
                mecanismos=["fxembed", "syndication"])

        def many(name, first_id, n, txt):
            return fx_body(name, [fx_post(first_id + i, T0 - (i + 1) * H, txt) for i in range(n)])
        routes = {FX.format("vieja"): (200, fx_body("vieja", [fx_post(1, T0 - 40 * D)]), {}),
                  SY.format("vieja"): (200, sy_body("vieja", [(900 + i, T0 - (60 + i) * D, "viejo", None, None)
                                                              for i in range(49)]), {}),
                  FX.format("ruidosa"): (200, many("ruidosa", 100, 12, "$RANDOM y nada más"), {}),
                  FX.format("diez"): (200, many("diez", 200, 10, "$RANDOM"), {}),
                  FX.format("util"): (200, fx_body("util", [fx_post(700 + i, T0 - (i + 1) * H, "$RANDOM") for i in range(11)]
                                                  + [fx_post(777, T0 - 30 * H, "$HNT sube")]), {}),
                  FX.format("rota"): (404, None, {}), SY.format("rota"): (200, sy_body("rota", []), {}),
                  FX.format("eco"): (200, fx_body("eco", [fx_post(5, T0 - 10 * D)]), {}),
                  SY.format("eco"): (200, sy_body("eco", [(999, T0 - 2 * H, "único fresco", None, None)]), {})}
        http = Http(routes)
        _, _, st = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None, vig=VIG, max_accounts=6)
        s = st["sources"]
        self.assertEqual(http.count(FX.format("rota")), 2)                 # 404 de FxEmbed: un reintento
        self.assertEqual(st["evaluar"], ["rota", "ruidosa", "vieja"])
        self.assertEqual(s["vieja"]["evaluar_motivo"], ["sin_post_30d"])
        self.assertEqual(s["ruidosa"]["evaluar_motivo"], ["sin_aporte"])
        self.assertEqual(s["rota"]["evaluar_motivo"], ["sin_posts_visibles"])
        self.assertFalse(s["diez"]["evaluar"])                             # 10 posts sin aporte: no supera el umbral
        self.assertEqual((s["util"]["evaluar"], s["util"]["aporte_estimado"]), (False, 1))
        self.assertNotIn("sin_turno", s)                                  # nunca consultada: sin datos, sin juicio
        m = st["mecanismos"]
        self.assertFalse(m["fxembed"]["marginal"])
        self.assertEqual((m["syndication"]["posts_total"], m["syndication"]["posts_frescos_30d"]), (50, 1))
        self.assertEqual((m["syndication"]["ratio"], m["syndication"]["marginal"]), (0.02, True))
        md, log = bit.reporte_semanal(st, c)
        self.assertIn("Decide Yang", md)
        self.assertIn("| vieja | narrativa | 3 |", md)
        self.assertIn("| syndication | 1 / 50 | 0.020 | sí |", md)
        self.assertEqual([f["cuenta"] for f in log["evaluar"]], ["rota", "ruidosa", "vieja"])   # por prioridad

    def test_4_no_eliminacion_automatica(self):
        tmp = Path(tempfile.mkdtemp(prefix="xinf_noelim_"))
        root, http_get = store.ROOT, bit.http_get
        try:
            now = time.time()
            yaml_text = ("pause_s: 0\nmecanismos: [fxembed]\ncuentas:\n"
                         "  - {cuenta: dormida, categoria: depin, prioridad: 3}\n"
                         "  - {cuenta: activa, categoria: cex, prioridad: 1}\n")
            (tmp / "04_Config").mkdir()
            cfg_file = tmp / "04_Config" / "influencers.yaml"
            cfg_file.write_text(yaml_text, encoding="utf-8")
            http = Http({FX.format("dormida"): (200, fx_body("dormida", [fx_post(1, int(now) - 60 * D)]), {}),
                         FX.format("activa"): (200, fx_body("activa", [fx_post(2, int(now) - 60)]), {})})
            store.ROOT, bit.http_get = tmp, http
            self.assertEqual(bit.main([]), 0)
            self.assertEqual(cfg_file.read_text(encoding="utf-8"), yaml_text)   # la config no se toca
            st = json.loads((tmp / "02_Analisis" / "sources" / "x_influencers" / "_state.json").read_text(encoding="utf-8"))
            d = st["sources"]["dormida"]
            self.assertEqual((d["evaluar"], d["status"], d["fails"]), (True, 200, 0))
            self.assertNotIn("auto_off_until", d)                          # evaluar no apaga
            self.assertEqual(d["next_check"] - d["checked_at"], 24 * 3600)  # el turno normal de una congelada
            report = (tmp / "02_Analisis" / "sources" / "x_influencers" / "_evaluar_semanal.md").read_text(encoding="utf-8")
            self.assertIn("| dormida | depin | 3 |", report)
            loaded = bit.load_config(cfg_file)
            self.assertIn("dormida", [x["cuenta"] for x in loaded["cuentas"] if x.get("enabled", True)])
        finally:
            store.ROOT, bit.http_get = root, http_get
            shutil.rmtree(tmp, ignore_errors=True)
        # varias corridas con evaluar: true la siguen consultando en su turno
        c = cfg([("dormida", "depin", 3)])
        http = Http({FX.format("dormida"): (200, fx_body("dormida", [fx_post(1, T0 - 60 * D)]), {})})
        st = {}
        for i in range(4):
            _, _, st = bit.run(c, st, fetch=http, now=T0 + i * 25 * H, sleep=lambda s: None, vig=VIG)
            self.assertTrue(st["sources"]["dormida"]["evaluar"])
        self.assertEqual(http.count(FX.format("dormida")), 4)


class TestExtracto(unittest.TestCase):
    def test_5_hash_y_extracto_detectan_casi_duplicados(self):
        base = ("Thread largo de contexto de mercado " * 6 + "Whale bought 2M $WIF at 1.20 and moved it to Binance, "
                "watch the unlock next week " + "y más relleno de cierre " * 6)
        ext = bit.extracto(base, ("unlock",))
        self.assertLessEqual(len(ext), 200)
        self.assertIn("$WIF", ext)                                        # centrado en lo detectado, no al comienzo
        self.assertFalse(ext.startswith("Thread"))
        self.assertTrue(bit.extracto("x" * 500).startswith("xxx"))         # sin nada detectado: el comienzo
        self.assertEqual(bit.extracto("corto  $WIF\n ok"), "corto $WIF ok")
        sha = bit.sha256_texto(base)
        self.assertEqual(len(sha), 64)
        self.assertLessEqual(len(ext.encode("utf-8")) + len(sha), 300)     # ~250 bytes por post
        edit = base.replace("Whale bought", "Whale boughtt").replace("next week", "next week 🚨") + " https://t.co/zz"
        a = {"sha": sha, "ext": ext}
        b = {"sha": bit.sha256_texto(edit), "ext": bit.extracto(edit, ("unlock",))}
        self.assertNotEqual(a["sha"], b["sha"])
        self.assertTrue(bit.casi_duplicado(a, b))                          # mismo texto con typo, emoji y link
        other = "Hyperliquid lists a new perp for $NEWT with 5x leverage starting tomorrow at 10:00 UTC, details in thread"
        self.assertFalse(bit.casi_duplicado(a, {"sha": bit.sha256_texto(other), "ext": bit.extracto(other)}))
        self.assertTrue(bit.casi_duplicado({"sha": "x" * 64, "ext": "a"}, {"sha": "x" * 64, "ext": "b"}))  # mismo hash
        self.assertFalse(bit.casi_duplicado({"sha": "1", "ext": "gm"}, {"sha": "2", "ext": "gm"}))       # mínimo: solo hash
        # en la corrida: copia de otra cuenta → dup_de y su aviso; repetición de la misma cuenta → sin tweet_influencer
        c = cfg([("a", "analista_onchain", 1), ("b", "noticias", 2)])
        http = Http({FX.format("a"): (200, fx_body("a", [fx_post(1, T0 - 50 * 60, base), fx_post(3, T0 - 10 * 60, edit)]), {}),
                     FX.format("b"): (200, fx_body("b", [fx_post(2, T0 - 20 * 60, edit + " via @a")]), {})})
        recs, evs, _ = bit.run(c, {}, fetch=http, now=T0, sleep=lambda s: None, keywords=("unlock",))
        by = {r["id"]: r["m"] for r in recs}
        self.assertNotIn("dup_de", by["1"])
        self.assertEqual((by["3"]["dup_de"], by["3"]["dup_cuenta"]), ("1", "a"))
        self.assertEqual((by["2"]["dup_de"], by["2"]["dup_cuenta"]), ("1", "a"))
        tweets = sorted(e[1] for e in evs if e[0] == "tweet_influencer")
        self.assertEqual(tweets, ["1", "2"])                               # el 3 (misma cuenta) no avisa de nuevo
        self.assertTrue(all(len(m["sha"]) == 64 and len(m["ext"]) <= 200 for m in by.values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
