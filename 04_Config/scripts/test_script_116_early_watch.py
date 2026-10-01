#!/usr/bin/env python3
"""script_116_early_watch (Fase 10, T3–T6). unittest, sin red: DexScreener, RugCheck, Hyperliquid y Telegram
simulados; script_97 real (formato de alerta y guía de compra) sobre un SHOT_ROOT temporal.

Uso: python 04_Config/scripts/test_script_116_early_watch.py
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import script_116_early_watch as ew  # noqa: E402

NOW = time.time()
MINT_A = "AAAAbbbbCCCCddddEEEEffffGGGGhhhhIIIIjjjjpump"
MINT_B = "BBBBbbbbCCCCddddEEEEffffGGGGhhhhIIIIjjjjpump"
MINT_C = "CCCCbbbbCCCCddddEEEEffffGGGGhhhhIIIIjjjjpump"
MINT_OLD = "DDDDbbbbCCCCddddEEEEffffGGGGhhhhIIIIjjjjpump"


class Resp:
    def __init__(self, data, status=200):
        self.status_code, self._data, self.text = status, data, json.dumps(data)

    def json(self):
        return self._data


def pair(mint, age_min, liq=60000.0, vol_m5=6000.0, vol_h1=15000.0, buys=30, sells=8, m5=2.0, symbol="TST"):
    return {"baseToken": {"address": mint, "symbol": symbol}, "priceUsd": "0.0012", "liquidity": {"usd": liq},
            "volume": {"m5": vol_m5, "h1": vol_h1, "h6": vol_h1 * 3, "h24": vol_h1 * 6}, "marketCap": 900000,
            "priceChange": {"m5": m5, "h1": 10.0, "h24": 30.0}, "dexId": "pumpswap", "pairAddress": "P" + mint[:20],
            "txns": {"m5": {"buys": buys, "sells": sells}, "h1": {"buys": 100, "sells": 100}},
            "pairCreatedAt": int((NOW - age_min * 60) * 1000)}


class EarlyWatch(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="s116_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        a = self.tmp / "02_Analisis"
        for d in ("shadow_v4", "alerts", "multichain", "narrative", "early"):
            (a / d).mkdir(parents=True)
        (a / "alerts" / "_all_alerts.json").write_text("[]", encoding="utf-8")
        env = {"SHOT_ROOT": str(self.tmp), "TELEGRAM_BOT_TOKEN": "t", "TELEGRAM_PUBLIC_CHAT_ID": "-100222",
               "SHADOW_MODE": "false", "PAUSE_EMISSIONS": "false"}
        p = mock.patch.dict(os.environ, env)
        p.start()
        self.addCleanup(p.stop)
        spec = importlib.util.spec_from_file_location("s97_for_116", HERE / "script_97_emit_alerts.py")
        self.s97 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.s97)
        self.posts, self.pairs, self.gets = [], [], []
        for patch in (mock.patch.object(self.s97.requests, "post", self.fake_tg),
                      mock.patch.object(self.s97.time, "sleep", lambda s: None)):
            patch.start()
            self.addCleanup(patch.stop)
        self.scores = {}            # mint -> score base que devuelve el scorer simulado

    def fake_tg(self, url, json=None, data=None, files=None, timeout=None):
        self.posts.append({"method": url.rsplit("/", 1)[-1], "json": json})
        return Resp({"ok": True})

    def fake_get(self, url, timeout=None, headers=None):
        self.gets.append(url)
        if "dexscreener" in url:
            asked = url.rsplit("/", 1)[-1].split(",")
            return Resp([p for p in self.pairs if p["baseToken"]["address"] in asked])
        if "rugcheck" in url:
            return Resp({"totalHolders": 500, "topHolders": [{"pct": 5}] * 10})
        if "dydx" in url:
            return Resp({"bids": [{"price": "10", "size": "100"}], "asks": [{"price": "10.01", "size": "1"}]})
        return Resp({}, 404)

    def fake_post(self, url, json=None, timeout=None):
        if json == {"type": "metaAndAssetCtxs"}:
            return Resp([{"universe": [{"name": "LDO"}]}, [{"funding": "0.0000125", "openInterest": "1000"}]])
        if json.get("type") == "l2Book":
            return Resp({"levels": [[{"px": "1.00", "sz": "5000"}], [{"px": "1.001", "sz": "100"}]]})
        return Resp({}, 404)

    def scorer(self, token, dx):
        mint = token.get("mint")
        return self.scores.get(mint, 30), [f"base {mint[:4]}"]

    def ctx(self, **kw):
        c = {"root": self.tmp, "get": self.fake_get, "post": self.fake_post, "state": {}, "watch": {},
             "scorer": self.scorer, "s97": self.s97, "git": ew.Git(self.tmp, enabled=False), "shadow": False,
             "dry_run": False, "threshold": 56, "min_age_min": 30, "poll_seconds": 120, "listener": None,
             "sleep": lambda s: None, "multichain": False}
        c.update(kw)
        return c

    def accumulate(self, entries):
        (self.tmp / "02_Analisis" / "shadow_v4" / "_accumulated.json").write_text(json.dumps(entries))

    def acc_entry(self, mint, score=45, detected_min_ago=10):
        return {"source": "pumpportal", "token": {"mint": mint, "symbol": "TST", "name": "Test"},
                "score": score, "detected_at": ew.now_iso(NOW - detected_min_ago * 60), "scoring_version": "7.2.1"}

    def early_alerts(self):
        return json.loads((self.tmp / "02_Analisis" / "early" / "_early_alerts.json").read_text())

    # -----------------------------------------------------------------------------------------------------------

    def test_bono_lleva_al_umbral_y_emite_con_guia_de_compra(self):
        self.accumulate({MINT_A: self.acc_entry(MINT_A)})
        self.scores[MINT_A] = 52
        self.pairs = [pair(MINT_A, 35)]
        c = self.ctx()
        c["state"]["liquidity"] = {MINT_A: [[NOW - 600, 40000.0]]}      # +50 % de liquidez en 10 min
        snap = ew.poll_once(c, NOW)
        self.assertEqual([e["mint"] for e in snap["emitted"]], [MINT_A])
        rec = self.early_alerts()[0]
        self.assertEqual((rec["status"], rec["early"], rec["score_base"], rec["telegram_sent"]),
                         ("active_tracking", True, 52, True))
        self.assertGreaterEqual(rec["early_bonus"], 4)
        msg = self.posts[0]["json"]["text"]
        self.assertIn("CÓMO ADQUIRIRLO", msg)
        self.assertLess(msg.index("CÓMO ADQUIRIRLO"), len(msg))
        detail = json.loads((self.tmp / "02_Analisis" / "alerts" / f"alert_{MINT_A}_{rec['timestamp']}.json").read_text())
        self.assertEqual(detail["scoring_version"], "7.2.1+" + ew.es.VERSION)
        self.assertTrue(any("Anticipación" in r for r in detail["reasons"]))
        # segundo poll: no se repite
        snap2 = ew.poll_once(c, NOW + 120)
        self.assertEqual(snap2["emitted"], [])
        self.assertEqual(len(self.early_alerts()), 1)

    def test_edad_minima_configurable(self):
        self.accumulate({MINT_A: self.acc_entry(MINT_A)})
        self.scores[MINT_A] = 70
        self.pairs = [pair(MINT_A, 12)]
        snap = ew.poll_once(self.ctx(), NOW)
        self.assertEqual(snap["emitted"], [])
        self.assertIn("edad", snap["top"][0]["why"])
        snap = ew.poll_once(self.ctx(min_age_min=10), NOW)
        self.assertEqual(len(snap["emitted"]), 1)

    def test_paridad_con_script_97_score_de_deteccion(self):
        self.accumulate({MINT_B: self.acc_entry(MINT_B, score=60, detected_min_ago=20)})
        self.scores[MINT_B] = 40                                       # el re-score bajó
        self.pairs = [pair(MINT_B, 33, vol_m5=500, vol_h1=12000, buys=5, sells=5)]   # sin señales
        snap = ew.poll_once(self.ctx(), NOW)
        self.assertEqual(len(snap["emitted"]), 1)
        self.assertEqual(self.early_alerts()[0]["score_base"], 60)

    def test_grupo_i_ya_alertados_y_sin_par(self):
        self.accumulate({MINT_OLD: self.acc_entry(MINT_OLD), MINT_B: self.acc_entry(MINT_B),
                         MINT_C: self.acc_entry(MINT_C)})
        self.scores.update({MINT_OLD: 80, MINT_B: 80, MINT_C: 80})
        (self.tmp / "02_Analisis" / "alerts" / "_all_alerts.json").write_text(json.dumps([{"mint": MINT_B}]))
        self.pairs = [pair(MINT_OLD, 200 * 1440), pair(MINT_B, 60)]   # MINT_C sin par en DexScreener
        snap = ew.poll_once(self.ctx(), NOW)
        self.assertEqual(snap["emitted"], [])
        self.assertIn("grupo i", snap["top"][0]["why"])
        self.assertNotIn(MINT_B, ",".join(self.gets))

    def test_rugcheck_para_los_cercanos_y_bono_on_chain(self):
        self.accumulate({MINT_A: self.acc_entry(MINT_A)})
        self.scores[MINT_A] = 50
        self.pairs = [pair(MINT_A, 20)]
        c = self.ctx()
        ew.poll_once(c, NOW)
        ew.poll_once(c, NOW + 300)
        self.assertEqual(sum("rugcheck" in u for u in self.gets), 1)    # 2.º poll: el anterior lo dejó cerca
        c["state"]["holders"][MINT_A].insert(0, {"ts": NOW - 300, "holders": 200, "top10_pct": 50})
        r = ew.evaluate(MINT_A, c["watch"][MINT_A], ew.flatten_pair(self.pairs[0]), c["state"], NOW + 400,
                        self.scorer, self.tmp, 30, 56)
        self.assertIn("holder_accumulation", r["early"]["active"])

    def test_senal_social_de_script_115(self):
        (self.tmp / "02_Analisis" / "narrative" / f"{MINT_A}.json").write_text(json.dumps(
            {"snapshot": {"m_1h": 6, "m_prev_1h": 1, "surprise_nats": 8, "seff_1h": 3}, "coingecko_trending": None}))
        sig = ew.narrative_signal(self.tmp, MINT_A)
        self.assertEqual(sig["s"], 1.0)
        self.assertIsNone(ew.narrative_signal(self.tmp, MINT_B))

    def test_multichain_order_book_y_funding(self):
        mc = self.tmp / "02_Analisis" / "multichain"
        (mc / "_scores.json").write_text(json.dumps({"results": [
            {"key": "cg:lido-dao", "group": "c", "symbol": "LDO", "score": 62},
            {"key": "cg:curve", "group": "c", "symbol": "CRV", "score": 55},
            {"key": "cg:presale", "group": "b", "symbol": "PRE", "score": 90}]}))
        (mc / "_perps.json").write_text(json.dumps({"perps": {"LDO": {}}}))
        (mc / "bitcoin.json").write_text(json.dumps({"universe_a": {"fear_greed": {"value": 10}}}))
        self.accumulate({})
        ew.poll_once(self.ctx(multichain=True), NOW)
        sig = json.loads((self.tmp / "02_Analisis" / "early" / "_signals.json").read_text())["signals"]
        self.assertEqual(set(sig), {"cg:lido-dao", "cg:curve"})          # b (preventa) no
        self.assertEqual(sig["cg:lido-dao"]["book_source"], "hyperliquid")
        self.assertEqual(sig["cg:curve"]["book_source"], "dydx")           # sin perp en Hyperliquid
        self.assertIn("orderbook_imbalance", sig["cg:lido-dao"]["active"])
        self.assertIn("fear_greed_extreme", sig["cg:lido-dao"]["active"])
        self.assertGreaterEqual(sig["cg:lido-dao"]["bonus"], 3)

    def test_lanzamientos_en_vivo_y_poda(self):
        w = ew.merge_launches({}, [{"mint": MINT_A, "timestamp": ew.now_iso(NOW - 200 * 60)},
                                   {"mint": MINT_B, "timestamp": ew.now_iso(NOW - 5 * 60)}], NOW)
        kept = ew.prune_watch(w, {MINT_C}, NOW)
        self.assertEqual(set(kept), {MINT_B})
        listener = ew.LaunchListener(lambda toks: ([t for t in toks if t["solAmount"] >= 0.5], []))
        listener._buf = [{"mint": "x", "solAmount": 0.1}, {"mint": "y", "solAmount": 1.0}]
        self.assertEqual([t["mint"] for t in listener.drain()], ["y"])
        self.assertEqual(listener.drain(), [])

    def test_mejor_par_por_liquidez(self):
        best = ew.best_pairs([pair(MINT_A, 40, liq=1000), pair(MINT_A, 40, liq=9000), {"x": 1}])
        self.assertEqual(best[MINT_A]["liquidityUsd"], 9000)
        self.assertEqual(best[MINT_A]["txns_m5_buys"], 30)

    def test_git_solo_archivos_propios_con_reintento(self):
        calls = []

        class R:
            def __init__(self, rc):
                self.returncode = rc

        script = iter([0, 1, 0, 1, 0, 0, 0])      # add, diff(cambios), commit, pull falla, abort, pull, push

        def run(args, **kw):
            calls.append(args[1])
            return R(next(script))

        (self.tmp / "f.json").write_text("{}")
        g = ew.Git(self.tmp, run=run)
        with mock.patch.object(ew.time, "sleep", lambda s: None):
            self.assertTrue(g.commit_push(["f.json", "no_existe.json"], "m"))
        self.assertEqual(calls, ["add", "diff", "commit", "pull", "rebase", "pull", "push"])

    def test_scorer_aislado_igual_al_original_y_restaura_cwd(self):
        spec = importlib.util.spec_from_file_location("s82_for_116", HERE / "script_82_final_detection.py")
        s82 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(s82)
        tok = {"mint": MINT_A, "symbol": "TST", "solAmount": 1.0, "marketCapSol": 40.0}
        dx = ew.flatten_pair(pair(MINT_A, 90))
        cwd = os.getcwd()
        fast = ew.isolated_scorer(s82.score_token, str(self.tmp / "02_Analisis" / "early"))
        os.chdir(self.tmp / "02_Analisis")       # sin shadow_v4/_accumulated.json relativo
        try:
            direct = s82.score_token(tok, dx)
        finally:
            os.chdir(cwd)
        self.assertEqual(fast(tok, dx), direct)
        self.assertEqual(os.getcwd(), cwd)

    def test_bucle_respeta_la_duracion(self):
        t = [0.0]
        c = self.ctx()
        self.accumulate({})
        polls = ew.run_loop(c, loop_minutes=10, poll_seconds=120, clock=lambda: t[0],
                            sleep=lambda s: t.__setitem__(0, t[0] + s))
        self.assertEqual(polls, 6)                     # t = 0, 2, 4, 6, 8, 10 min


if __name__ == "__main__":
    unittest.main(verbosity=2)
