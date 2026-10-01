#!/usr/bin/env python3
"""Emisión multi-chain en script_97 (Fase 7). unittest, sin red: Telegram y CoinGecko simulados.

Uso: python 04_Config/scripts/test_script_97_multichain.py
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

SCRIPT = Path(__file__).resolve().parent / "script_97_emit_alerts.py"
GRUPO = "-100222"
NOW = datetime.now(timezone.utc)
SOL_MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
EVM = "0x1111111111111111111111111111111111111111"


def solana_candidate():
    return {"source": "pumpportal", "token": {"mint": SOL_MINT, "symbol": "TEST_CAT", "name": "Test Cat"},
            "dexscreener": {"priceUsd": 0.0123, "liquidityUsd": 141632.8, "volume24hUsd": 201003.7,
                            "marketCapUsd": 9844684.6, "priceChange24h": 120.0, "dexId": "pumpswap",
                            "pairAddress": "B6ELT7HZ2p4AWEWnXbM7B6DtuVJET8insnTxLaWUVh9k",
                            "pairCreatedAt": int((NOW - timedelta(minutes=120)).timestamp() * 1000)},
            "score": 72, "reasons": ["MCap > $1M"], "detected_at": NOW.isoformat(timespec="seconds"),
            "scoring_version": "7.2.1"}


def gov_scan(generated=None):
    item = {"id": "govtoken", "symbol": "GOV", "name": "Gov Token", "price_usd": 1.5, "mcap_usd": 40e6, "fdv_usd": 40e6,
            "volume_24h_usd": 5e6, "change_1h": 1.0, "change_24h": 8.0, "change_7d": 30.0, "source": "governance"}
    return {"generated_at": (generated or NOW).isoformat(timespec="seconds"), "groups": {"c": {"items": [item]}},
            "onchain": {}, "accelerating": [], "errors": [], "calls": 1}


class Resp:
    def __init__(self, status=200, data=None, text="{}"):
        self.status_code, self._data, self.text = status, data, text

    def json(self):
        return self._data


def result(key, group, score=70, **kw):
    base = {"key": key, "group": group, "group_rule": "test", "scoring_version": f"mc-{group}-0.1", "score": score,
            "confidence": 0.8, "reasons": ["r1"], "components": [], "event": "evento", "threshold": 56,
            "emittable": True, "status_reason": "emitible", "extra": {}, "symbol": key.split(":")[-1][:6].upper(),
            "name": "Activo", "chain": None, "cg_id": None, "address": None, "price_usd": 2.0, "mcap_usd": 1e8,
            "volume_24h_usd": 1e7, "liquidity_usd": None, "change_24h": 5.0, "change_7d": 9.0,
            "pool_address": None, "pool_created_at": None, "category": None}
    base.update(kw)
    return base


class MultichainEmision(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="s97mc_")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = Path(self.tmp) / "02_Analisis"
        for d in ("shadow_v4", "alerts", "multichain"):
            (self.root / d).mkdir(parents=True)
        self.acc = self.root / "shadow_v4" / "_accumulated.json"
        self.acc.write_text("{}", encoding="utf-8")
        self.alerts_file = self.root / "alerts" / "_all_alerts.json"
        self.alerts_file.write_text("[]", encoding="utf-8")
        self.mc = self.root / "multichain"
        self.env = {"SHOT_ROOT": self.tmp, "TELEGRAM_BOT_TOKEN": "t", "TELEGRAM_PUBLIC_CHAT_ID": GRUPO,
                    "DOSSIER_LIVE": "false", "SHADOW_MODE": "false", "PAUSE_EMISSIONS": "false",
                    "MULTICHAIN_EMISSIONS": "true"}
        self.posts, self.gets = [], []
        self.tickers = Resp(200, {"tickers": [{"base": "GOV", "target": "USDT", "market": {"identifier": "binance"}},
                                              {"base": "GOV", "target": "USD", "market": {"identifier": "gdax"}}]})

    def write_gov_inputs(self, generated=None):
        (self.mc / "scan_latest.json").write_text(json.dumps(gov_scan(generated)), encoding="utf-8")
        (self.mc / "_categories.json").write_text(json.dumps({"categories": {"governance": {
            "market_cap_change_24h_pct": 1.0, "sample": {"median_change_7d": 0.0}}}}), encoding="utf-8")
        (self.mc / "_protocols.json").write_text(json.dumps({"protocols": {"govtoken": {"tvl": 160e6, "change_7d": 20.0}}}),
                                                 encoding="utf-8")

    def fake_post(self, url, json=None, data=None, files=None, timeout=None):
        call = {"method": url.rsplit("/", 1)[-1], "json": json, "data": data}
        if files:
            name, handle, _ = files["document"]
            call["file"] = (name, handle.read().decode("utf-8"))
        self.posts.append(call)
        return Resp(200)

    def fake_get(self, url, timeout=None, headers=None):
        self.gets.append(url)
        return self.tickers

    def load(self, **env):
        self._env = mock.patch.dict(os.environ, {**self.env, **env})
        self._env.start()
        self.addCleanup(self._env.stop)
        spec = importlib.util.spec_from_file_location("s97_mc_test", SCRIPT)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        for p in (mock.patch.object(m.requests, "post", self.fake_post), mock.patch.object(m.requests, "get", self.fake_get),
                  mock.patch.object(m.time, "sleep", lambda s: None)):
            p.start()
            self.addCleanup(p.stop)
        return m

    def alerts(self):
        return json.loads(self.alerts_file.read_text(encoding="utf-8"))

    # --- extremo a extremo con la librería real ---------------------------------------------------------------

    def test_gobernanza_se_emite_por_cex_con_dossier_y_registro(self):
        self.write_gov_inputs()
        m = self.load()
        self.assertEqual(m.main([]), 0)
        rec = [a for a in self.alerts() if a.get("multichain")]
        self.assertEqual(len(rec), 1)
        r = rec[0]
        self.assertEqual((r["mint"], r["group"], r["status"], r["telegram_sent"]),
                         ("cg:govtoken", "c", "active_tracking_cex", True))
        self.assertEqual(self.gets, [m.CG_TICKERS_URL.format(id="govtoken")])
        doc = self.posts[0]
        self.assertEqual(doc["method"], "sendDocument")
        caption = doc["data"]["caption"]
        self.assertIn("🛒 *CÓMO ADQUIRIRLO*", caption)
        self.assertIn("https://www.binance.com/en/trade/GOV_USDT", caption)
        self.assertNotIn("ref", caption.lower().replace("referido", ""))
        name, body = doc["file"]
        self.assertLess(body.index("🛒 CÓMO ADQUIRIR ESTE ACTIVO"), body.index("📊 Identificación"))
        self.assertIn("Valuación mcap/TVL", body)
        scores = json.loads((self.mc / "_scores.json").read_text(encoding="utf-8"))
        self.assertEqual(scores["coverage_by_group"]["c"]["emittable"], 1)
        self.assertTrue((Path(self.tmp) / r["dossier"]).exists())

    def test_sin_exchange_confirmado_no_se_emite(self):
        self.write_gov_inputs()
        self.tickers = Resp(404)
        m = self.load()
        m.main([])
        self.assertEqual(self.alerts(), [])
        self.assertEqual(self.posts, [])

    def test_scan_viejo_no_se_usa(self):
        self.write_gov_inputs(NOW - timedelta(hours=3))
        m = self.load()
        m.main([])
        self.assertEqual(self.alerts(), [])
        self.assertFalse((self.mc / "_scores.json").exists())

    def test_desactivable_y_sombra(self):
        self.write_gov_inputs()
        m = self.load(MULTICHAIN_EMISSIONS="false")
        m.main([])
        self.assertEqual(self.alerts(), [])
        self.write_gov_inputs()
        m = self.load(SHADOW_MODE="true")
        m.main([])
        r = self.alerts()[0]
        self.assertEqual((r["status"], r["telegram_sent"]), ("shadow", False))
        self.assertEqual(self.posts, [])
        self.assertTrue((Path(self.tmp) / r["dossier"]).exists())

    def test_la_ruta_solana_no_cambia(self):
        self.acc.write_text(json.dumps({SOL_MINT: solana_candidate()}), encoding="utf-8")
        self.write_gov_inputs()
        m = self.load()
        m.main([])
        sol, mc = self.alerts()
        self.assertEqual(sol["mint"], SOL_MINT)                                  # Solana primero, igual que antes
        self.assertNotIn("multichain", sol)
        self.assertEqual(sol["status"], "active_tracking")
        self.assertEqual(mc["mint"], "cg:govtoken")

    # --- selección y rutas de compra (resultados simulados) ---------------------------------------------------

    def test_seleccion_ventana_tope_por_grupo_y_por_ciclo(self):
        m = self.load()
        ts = lambda h: (NOW - timedelta(hours=h)).strftime("%Y-%m-%d_%H%M%S")   # noqa: E731
        hist = [{"mint": "0xa1", "asset_key": "cg:a1", "multichain": True, "group": "e", "timestamp": ts(10)},
                {"mint": "cg:a2", "multichain": True, "group": "e", "timestamp": ts(5)},
                {"mint": "cg:a3", "multichain": True, "group": "e", "timestamp": ts(1)},
                {"mint": "cg:old", "multichain": True, "group": "f", "timestamp": ts(49)},
                {"mint": SOL_MINT, "timestamp": ts(1)}]
        res = [result("cg:a1", "e", 99), result("cg:e9", "e", 95), result("cg:old", "f", 90),
               result("cg:f2", "f", 80), result("cg:f3", "f", 70), result("cg:x", "c", 60, emittable=False)]
        sel, skipped = m.select_multichain(res, hist, NOW)
        self.assertEqual([r["key"] for r in sel], ["cg:old", "cg:f2"])           # >48 h vuelve a ser elegible
        self.assertEqual(skipped, {"cooldown": 1, "group_cap": 1})              # a1 en ventana; e9: tope de e (3/24 h)

    def test_blue_chip_ruta_cex_fija_sin_red(self):
        m = self.load()
        self.tickers = None
        links = m.cex_links_for(result("cg:bitcoin", "h", cg_id="bitcoin", symbol="BTC"), m.load_dossier_builder())
        self.assertEqual([n for n, _ in links], ["Binance", "Coinbase", "Kraken"])
        self.assertIn("BTC_USDT", links[0][1])
        self.assertEqual(self.gets, [])
        lines = m.cex_acquisition_lines(result("cg:ethereum", "h", cg_id="ethereum", symbol="ETH", chain="ethereum"), links)
        self.assertEqual(len(lines), 9)                                           # ruta + 8 pasos
        self.assertIn("MetaMask", lines[-1])                                      # custodia propia en la red nativa
        msg = m.format_multichain_message(result("cg:bitcoin", "h", cg_id="bitcoin", symbol="BTC",
                                                 extra={"barrier_pct": 5.6}), links, "01/10/2026 17:00 UTC")
        order = ["🪪 *ACTIVO*", "🛒 *CÓMO ADQUIRIRLO*", "🕒 *DETECCIÓN*", "🎯 *PROBABILIDADES*", "📊 *DATOS",
                 "🔎 *POR QUÉ", "🔗 *FUENTES VERIFICABLES*", "⏱️ *SEGUIMIENTO*"]
        self.assertEqual([msg.index(s) for s in order], sorted(msg.index(s) for s in order))
        self.assertIn("±5.60%", msg)

    def test_onchain_usa_la_guia_de_la_chain_y_monad_no_emite(self):
        m = self.load()
        (self.mc / "scan_latest.json").write_text(json.dumps(gov_scan()), encoding="utf-8")
        arb = result(f"arbitrum:{EVM}", "a", 61, chain="arbitrum", address=EVM, symbol="PEPE", liquidity_usd=5e5,
                     pool_address=f"arbitrum_{EVM}", pool_created_at=(NOW - timedelta(days=2)).isoformat())
        mon = result(f"monad:{EVM}", "a", 90, chain="monad", address=EVM, symbol="MONMEME")
        with mock.patch.object(m, "multichain_results", lambda now, scorer=None: [mon, arb]):
            n = m.emit_multichain(self.alerts(), "2026-10-01_170000", False, None, NOW)
        self.assertEqual(n, 1)
        rec = self.alerts()[0]
        self.assertEqual((rec["mint"], rec["asset_key"], rec["status"], rec["chain"]),
                         (EVM, f"arbitrum:{EVM}", "active_tracking", "arbitrum"))      # script_98 consulta el contrato
        caption = self.posts[0]["data"]["caption"]
        self.assertIn("— Arbitrum", caption)
        self.assertIn("Uniswap (https://app.uniswap.org)", caption)
        self.assertIn(f"https://arbiscan.io/token/{EVM}", caption)


    def test_un_salteado_cede_el_cupo_y_el_tope_por_ciclo_se_respeta(self):
        m = self.load()
        (self.mc / "scan_latest.json").write_text(json.dumps(gov_scan()), encoding="utf-8")
        mon = result(f"monad:{EVM}", "a", 95, chain="monad", address=EVM)          # sin guía: se saltea
        evms = [result(f"base:0x{i:040x}", g, 90 - i, chain="base", address=f"0x{i:040x}", liquidity_usd=1e6)
                for i, g in ((1, "a"), (2, "a"), (3, "c"))]
        with mock.patch.object(m, "multichain_results", lambda now, scorer=None: [mon] + evms):
            n = m.emit_multichain([], "2026-10-01_170000", False, None, NOW)
        self.assertEqual(n, m.MULTICHAIN_MAX_PER_CYCLE)
        self.assertEqual([a["asset_key"] for a in self.alerts()], [evms[0]["key"], evms[1]["key"]])

    def test_grupo_d_con_perps_de_hyperliquid_se_emite(self):
        item = {"id": "hyperliquid", "symbol": "HYPE", "name": "Hyperliquid", "price_usd": 40.0, "mcap_usd": 1.3e10,
                "fdv_usd": 1.3e10, "volume_24h_usd": 5e8, "change_24h": 12.0, "change_7d": 30.0,
                "source": "decentralized-perpetuals"}
        scan = dict(gov_scan(), groups={"d": {"items": [item]}})
        (self.mc / "scan_latest.json").write_text(json.dumps(scan), encoding="utf-8")
        t0, t1 = (NOW - timedelta(hours=24)).isoformat(), NOW.isoformat()
        (self.mc / "_perps.json").write_text(json.dumps({"perps": {"HYPE": {
            "funding_1h": -0.00002, "mark_px": 40.2, "oracle_px": 40.0}}, "oi_history": {"HYPE": [[t0, 100.0], [t1, 160.0]]}}),
            encoding="utf-8")
        self.tickers = Resp(200, {"tickers": [{"base": "HYPE", "target": "USDT", "market": {"identifier": "binance"}}]})
        m = self.load()
        m.main([])
        rec = [a for a in self.alerts() if a.get("multichain")]
        self.assertEqual([(r["asset_key"], r["group"], r["status"]) for r in rec],
                         [("cg:hyperliquid", "d", "active_tracking_cex")])
        self.assertIn("HYPE_USDT", self.posts[0]["data"]["caption"])
        scores = json.loads((self.mc / "_scores.json").read_text(encoding="utf-8"))
        self.assertEqual(scores["coverage_by_group"]["d"]["emittable"], 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
