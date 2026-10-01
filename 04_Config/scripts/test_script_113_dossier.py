#!/usr/bin/env python3
"""Tests del dossier por activo (script_113, doc 24). unittest, sin red.

Uso: python 04_Config/scripts/test_script_113_dossier.py
"""
import contextlib
import importlib.util
import io
import json
import os
import random
import re
import shutil
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parents[1]
spec = importlib.util.spec_from_file_location("s113_test", SCRIPTS / "script_113_dossier_builder.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

NOW = datetime(2026, 10, 1, 3, 0, tzinfo=timezone.utc)
HEADINGS = ["## 🛒 1.", "## 📊 2.", "## 🧬 3.", "## 🔬 4.", "## 🎯 5.", "## ⏱️ 6.", "## 📚 7."]
# Frases de juicio, disuasión o consejo: el dossier informa, no advierte (Dirección, 30/09).
MORAL = ["cuidado", "advertencia", "atención:", "peligro", "precaución", "estafa", "scam", "rug pull", "rugpull",
         "no inviertas", "no compres", "evitá", "evite ", "desaconsej", "alto riesgo", "riesgoso", "te recomendamos",
         "recomendamos", "no recomendable", "invertí solo", "solo lo que puedas perder", "ojo con"]
FAKE_TRACE = {"path": "02_Analisis/alerts/alert_X_2026-10-01_000000.json", "blob": "0" * 40, "commit": None,
              "commit_date": None}
NO_RECOMPUTE = {"version": "7.2.1", "score": None, "reasons": [], "error": "omitido en el test"}


def bare_data(record, **extra):
    data = {"record": record, "alert": None, "signals": None, "record_trace": FAKE_TRACE, "detection_trace": None,
            "population": None, "calibration": None, "shadow": {}, "recomputed": NO_RECOMPUTE}
    data.update(extra)
    return data


def bare_record(mint="TestMint1111111111111111111111111111111pump", chain=None, dx=None, **extra):
    record = {"token": {"mint": mint, "symbol": "TST", "name": "Test"}, "score": 0,
              "reasons": ["MCap bajo", "Volumen bajo", "Liquidez baja"], "detected_at": "2026-10-01T00:00:00+00:00",
              "scoring_version": "7.2.1", "dexscreener": dx}
    if chain:
        record["chain"] = chain
    record.update(extra)
    return record


class DossierVSOF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = m.dry_run_dossier()
        cls.md = m.render_markdown(cls.d)

    def test_presentacion_y_siete_secciones_en_orden(self):
        for key, _, _ in m.SECTIONS:
            self.assertIn(key, self.d)
        positions = [self.md.index(h) for h in HEADINGS]
        self.assertEqual(positions, sorted(positions))
        self.assertLess(self.md.index("🎴"), positions[0])
        self.assertEqual(len(m.SECTIONS), 7)

    def test_adquisicion_primero_y_completa(self):
        a = self.d["acquisition"]
        self.assertTrue(self.d["emitible"], self.d["missing"])
        self.assertEqual(self.d["missing"], [])
        self.assertEqual(len(a["steps"]), 8)
        self.assertEqual([w for w, _ in a["wallets"]], ["Phantom", "Solflare"])
        self.assertEqual([x for x, _ in a["dexes"]], ["Jupiter", "Raydium", "Orca"])
        self.assertEqual(a["verification"]["explorer"][1], f"https://solscan.io/token/{m.VSOF_MINT}")
        self.assertEqual(a["verification"]["dexscreener"],
                         "https://dexscreener.com/solana/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx")
        block = self.md[self.md.index(HEADINGS[0]):self.md.index(HEADINGS[1])]
        for i in range(1, 9):
            self.assertRegex(block, rf"(?m)^{i}\. \S")
        self.assertIn(f"`{m.VSOF_MINT}`", block)
        # Lo primero que se ve después de la portada es la compra
        self.assertNotIn("Fundamento", self.md[:self.md.index(HEADINGS[0])])

    def test_estudio_de_liquidez_vsof(self):
        det, cur = self.d["acquisition"]["liquidity_study"]
        self.assertEqual(det["liquidity"], 1195183.55)
        self.assertEqual(det["slippage"], "1%")
        self.assertEqual([m.fmt_impact(det["impacts"][str(u)]) for u in m.IMPACT_SIZES], ["0,017%", "0,167%", "1,673%"])
        self.assertEqual(m.fmt_usd(det["size_for"]["0.01"]), "$5.976")
        self.assertTrue(cur["moment"].startswith("consulta"))
        self.assertIn("| al detectar · 29/09/2026 17:08 UTC | pumpswap `5pav7s4…RGdx` | $1.195.184 | 1% | 0,017% | "
                      "0,167% | 1,673% | $5.976 | $17.928 |", self.md)

    def test_desglose_reproduce_el_score_registrado(self):
        b = self.d["foundation"]["breakdown"]
        self.assertTrue(b["reproducible"])
        self.assertEqual(b["total"], 95)
        self.assertEqual([r["points"] for r in b["rows"]], [30.0, 25, 15, 15, 10])
        self.assertIn("| **Total** | recortado a 0–100 |  | **95** |", self.md)

    def test_recalculo_con_el_scorer_vigente(self):
        rc = self.d["foundation"]["recomputed"]
        if rc.get("score") is None:
            self.skipTest(f"scorer no importable: {rc.get('error')}")
        self.assertEqual(rc["version"], m.current_scorer_version())
        if rc["version"] == "7.2.1":                       # doc 24 §4.5: 95 con el scorer de entonces, 45 con v7.2.1
            self.assertEqual(rc["score"], 45)
            self.assertIn("SOBRECOMPRA EXTREMA (>50,000%)", rc["reasons"])

    def test_wilson_reproduce_el_doc_21(self):
        self.assertEqual(m.cal.wilson(16, 21), [0.585, 0.879])
        self.assertIn("| Después de tocar +20%, llegar a ≤ −99% (≤ 48 h) | 16/21 | 76,2% | 58,5%–87,9% |", self.md)

    def test_formato_markdown(self):
        self.assertTrue(self.md.startswith("# VSOF (VSOF) — dossier\n"))
        for bad in (r"None", r"nan", r"\{\{", r"\}\}", r"\{'", r"(?<!\w)\[\]"):   # "markets[].lp" es una ruta de campo, no una lista vacía
            found = re.search(bad, self.md)
            self.assertIsNone(found, f"{bad}: {self.md[max(0, found.start() - 40):found.end() + 40] if found else ''}")
        lines = self.md.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("|---"):
                header = lines[i - 1]
                self.assertTrue(header.startswith("| "), header)
                self.assertEqual(line.count("---"), header.count(" | ") + 1, header)
        self.assertEqual(self.md.count("```"), 2)

    def test_sin_advertencias_morales(self):
        low = self.md.lower()
        for phrase in MORAL:
            self.assertNotIn(phrase, low)
        self.assertIn("No es asesoría financiera.", self.md)

    def test_metrica_dual_del_activo(self):
        dual = self.d["validity"]["dual"]
        self.assertEqual((dual["primary"], dual["secondary"]), ("hit", "pending"))
        self.assertIn("primaria se cumplió · secundaria pendiente", self.md)

    def test_trazabilidad(self):
        s = self.d["sources"]
        self.assertEqual(s["record"]["blob"], "21b15740ba0ac8503e86df35d82c8c8e93d66cc1")
        self.assertEqual(s["detection"]["commit"], "be8e7d3")
        self.assertIn("mock.patch('time.time',return_value=1790701698)", s["commands"]["score"])
        self.assertRegex(self.d["meta"]["input_sha256"], r"^[0-9a-f]{64}$")

    def test_dry_run_no_usa_la_red(self):
        def no_network(*a, **k):
            raise AssertionError("el dry-run hizo una llamada de red")
        out = io.StringIO()
        with mock.patch("requests.Session.request", no_network), mock.patch("requests.get", no_network), \
                contextlib.redirect_stdout(out):
            self.assertEqual(m.main(["--dry-run"]), 0)
        self.assertTrue(out.getvalue().startswith("# VSOF (VSOF) — dossier"))


class ReglaNucleo(unittest.TestCase):
    def test_chain_sin_guia_de_compra_no_se_emite(self):
        d = m.build_dossier("0x" + "a" * 40, "monad", bare_data(bare_record("0x" + "a" * 40, chain="monad")), now=NOW)
        self.assertFalse(d["emitible"])
        self.assertTrue(any("guía de compra" in x for x in d["missing"]))
        tmp = Path(tempfile.mkdtemp(prefix="dossier_"))
        try:
            self.assertIsNone(m.save_dossier(d, tmp / "x.md"))
            self.assertEqual(list(tmp.iterdir()), [])
        finally:
            shutil.rmtree(tmp)

    def test_sin_mint_no_se_emite(self):
        d = m.build_dossier("", "solana", bare_data(bare_record("")), now=NOW)
        self.assertFalse(d["emitible"])
        self.assertIn("mint / contrato", d["missing"])

    def test_sin_registro_trazable_no_se_emite(self):
        d = m.build_dossier("Mint1", "solana", bare_data(bare_record("Mint1"), record_trace=None), now=NOW)
        self.assertIn("registro de la detección con blob", d["missing"])
        self.assertIn("comando de recálculo del score", d["missing"])

    def test_main_no_guarda_lo_que_no_se_emite(self):
        data = bare_data(bare_record("0x" + "b" * 40, chain="monad"))
        with mock.patch.object(m, "load_alert_data", return_value=data), \
                mock.patch.object(m, "save_dossier") as save, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(["--mint", "0x" + "b" * 40, "--offline"]), 3)
        save.assert_not_called()


class DatosDesconocidos(unittest.TestCase):
    def test_registro_minimo_muestra_nd_y_no_inventa(self):
        d = m.build_dossier("Mint2", "solana", bare_data(bare_record("Mint2")), now=NOW)
        self.assertTrue(d["emitible"], d["missing"])
        row = d["acquisition"]["liquidity_study"][0]
        self.assertIsNone(row["liquidity"])
        self.assertEqual(row["slippage"], "5–10%")
        md = m.render_markdown(d)
        self.assertIn("| n/d | 5–10% | n/d | n/d | n/d | n/d | n/d |", md)
        self.assertNotIn("$0 ", md)
        self.assertIn("| Holders / top-10 | n/d / n/d |", md)
        self.assertIn("Métrica dual de este activo:** n/d", md)
        self.assertIn("sin descripción publicada", md)
        for phrase in MORAL:
            self.assertNotIn(phrase, md.lower())

    def test_desglose_no_reproducible_no_se_publica(self):
        record = bare_record("Mint3", reasons=["Motivo nuevo que el desglose no conoce"], score=40)
        d = m.build_dossier("Mint3", "solana", bare_data(record), now=NOW)
        self.assertFalse(d["foundation"]["breakdown"]["reproducible"])
        md = m.render_markdown(d)
        self.assertIn("Desglose no reproducible", md)
        self.assertNotIn("| **Total** |", md)


class GuiaEVM(unittest.TestCase):
    def test_base_usa_wallets_dex_y_explorador_de_base(self):
        addr = "0x" + "c" * 40
        dx = {"priceUsd": 0.01, "liquidityUsd": 300000.0, "marketCapUsd": 5e6, "volume24hUsd": 2e5,
              "dexId": "aerodrome", "pairAddress": "0x" + "d" * 40, "chainId": "base"}
        live = {"queried_at": "2026-10-01T02:50:00+00:00", "calls": [], "dexscreener": None, "rugcheck": None,
                "goplus": {"mintable": False, "honeypot": False, "open_source": True, "owner": None,
                           "buy_tax": 0.0, "sell_tax": 0.01, "holders": 1500}, "history": None, "dual": None}
        d = m.build_dossier(addr, "base", bare_data(bare_record(addr, chain="base", dx=dx)), live=live, now=NOW)
        a = d["acquisition"]
        self.assertTrue(d["emitible"], d["missing"])
        self.assertEqual([w for w, _ in a["wallets"]], ["MetaMask", "Coinbase Wallet"])
        self.assertEqual(a["dexes"][0][0], "Aerodrome")
        self.assertEqual(a["address_word"], "contrato")
        self.assertEqual(a["verification"]["explorer"], ["BaseScan", f"https://basescan.org/token/{addr}"])
        self.assertEqual(a["slippage"], "3%")
        self.assertIn("impuesto de compra / venta: 0,0% / 1,0%", a["steps"][5])


class Parsers(unittest.TestCase):
    def test_dexscreener_elige_el_par_de_mayor_liquidez_de_la_chain(self):
        data = {"pairs": [{"chainId": "solana", "pairAddress": "A", "liquidity": {"usd": 10}, "priceUsd": "1"},
                          {"chainId": "solana", "pairAddress": "B", "liquidity": {"usd": 500}, "priceUsd": "2",
                           "info": {"websites": [{"url": "https://x.example"}], "socials": [{"type": "twitter", "url": "https://t.example"}]}},
                          {"chainId": "base", "pairAddress": "C", "liquidity": {"usd": 9999}}]}
        p = m.parse_dexscreener(data, "solana")
        self.assertEqual((p["pair"], p["price"], p["n_pairs"]), ("B", 2.0, 2))
        self.assertEqual(p["websites"], ["https://x.example"])
        self.assertIsNone(m.parse_dexscreener({"pairs": []}, "solana"))
        self.assertIsNone(m.parse_dexscreener(None, "solana"))

    def test_rugcheck_top10_authorities_y_lp(self):
        data = {"mint": "M", "creator": "C", "mintAuthority": None, "freezeAuthority": "F", "totalHolders": 100,
                "topHolders": [{"pct": 5.0, "insider": True}] + [{"pct": 1.0}] * 11,
                "markets": [{"marketType": "pump_fun_amm", "lp": {"lpLockedPct": 100}}],
                "risks": [{"name": "High holder correlation", "level": "warn"}], "fileMeta": {"description": " Hola "}}
        r = m.parse_rugcheck(data)
        self.assertEqual(r["top10_pct"], 14.0)
        self.assertEqual(r["insiders_top10"], 1)
        self.assertEqual(r["lp_locked"], [("pump_fun_amm", 100.0)])
        self.assertEqual(r["labels"], ["High holder correlation"])
        self.assertEqual(r["description"], "Hola")
        self.assertIsNone(m.parse_rugcheck({"error": "not found"}))

    def test_goplus_solana_y_evm(self):
        sol = {"result": {"M": {"mintable": {"status": "0"}, "freezable": {"status": "1"}}}}
        self.assertEqual(m.parse_goplus(sol, "M", "solana"), {"mintable": False, "freezable": True, "metadata_mutable": None})
        evm = {"result": {"0xabc": {"is_mintable": "0", "is_honeypot": "0", "buy_tax": "0.05", "sell_tax": ""}}}
        g = m.parse_goplus(evm, "0xABC", "base")
        self.assertEqual((g["mintable"], g["honeypot"], g["buy_tax"], g["sell_tax"]), (False, False, 0.05, None))

    def test_ohlcv_ordena_y_toma_extremos(self):
        data = {"data": {"attributes": {"ohlcv_list": [[300, 3, 9, 2, 4, 1], [100, 1, 2, 0.5, 1.5, 1], [200, 2, 3, 1, 2, 1]]}}}
        h = m.parse_ohlcv(data)
        self.assertEqual((h["first_ts"], h["first_open"], h["max"], h["max_ts"], h["min"], h["min_ts"], h["last_close"]),
                         (100, 1, 9, 300, 0.5, 100, 4))

    def test_holders_efectivos(self):
        self.assertAlmostEqual(m._effective_holders([1.0] * 10), 10.0)
        self.assertLess(m._effective_holders([91.0] + [1.0] * 9), 1.3)
        self.assertIsNone(m._effective_holders([]))

    def test_parse_ts(self):
        self.assertEqual(m.parse_ts("2026-09-29_171330"), datetime(2026, 9, 29, 17, 13, 30, tzinfo=timezone.utc))
        self.assertEqual(m.parse_ts("2026-09-29T17:06:54.985219044Z").microsecond, 985219)
        self.assertIsNone(m.parse_ts("no es fecha"))


class DesgloseContraScorer(unittest.TestCase):
    """El desglose por motivos tiene que sumar exactamente lo que devuelve script_82.score_token."""

    @classmethod
    def setUpClass(cls):
        cls.work = tempfile.mkdtemp(prefix="s82_")
        try:
            cls.s82 = m.cal.load_script_82(cls.work)
        except Exception as e:     # dependencia del scorer ausente: se saltea, no falla
            cls.s82, cls.error = None, e

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.work, ignore_errors=True)

    def test_desglose_coincide_con_score_token(self):
        if self.s82 is None:
            self.skipTest(f"scorer no importable: {self.error}")
        rng = random.Random(20261001)
        t = 1790700000.0
        prev = os.getcwd()
        os.chdir(self.work)          # sin _accumulated.json: bp_delta = 0
        try:
            for _ in range(400):
                age = rng.choice([None, 3, 30, 59, 61, 90, 300, 2000])
                vh1 = rng.choice([0, 1000, 20000])
                b5, s5 = rng.choice([0, 3, 12]), rng.choice([0, 2, 20])
                dx = {"marketCapUsd": rng.choice([0, 40e3, 60e3, 2e5, 5e6]), "volume24hUsd": rng.choice([0, 6e4, 2e5, 2e6]),
                      "liquidityUsd": rng.choice([0, 1e4, 3e4, 6e4, 2e5]),
                      "priceChange24h": rng.choice([-40, 0, 25, 60, 600, 6000, 60000]),
                      "volume_m5": rng.choice([0, 400, 800, 5000]) if vh1 else 0, "volume_h1": vh1,
                      "txns_m5_buys": b5, "txns_m5_sells": s5, "txns_h1_buys": b5 * rng.choice([1, 3]),
                      "txns_h1_sells": s5 * rng.choice([1, 3]),
                      "priceChange_m5": rng.choice([-2, 0, 3]), "priceChange_h1": rng.choice([-10, -3, 4])}
                if age is not None:
                    dx["pairCreatedAt"] = (t - age * 60) * 1000
                tok = {"score": rng.choice([0, 30, 57, 65, 85, 100])}
                with mock.patch("time.time", return_value=t):
                    score, reasons = self.s82.score_token(tok, dx)
                b = m.score_breakdown({"token": tok, "dexscreener": dx, "score": score, "reasons": reasons})
                self.assertTrue(b["reproducible"], (score, b["total"], reasons, b["unknown_reasons"]))
        finally:
            os.chdir(prev)

    def test_sobrecompra_con_texto_dinamico(self):
        rp = m.reason_points
        self.assertEqual(rp("SOBRECOMPRA ALTA (>5,000%) + liq/mcap=2.1% <3%")[2], -15)
        self.assertEqual(rp("SOBRECOMPRA ALTA (>5,000%) + liq/mcap=0.4% <1%")[2], -50)
        self.assertEqual(rp("SOBRECOMPRA MEDIA (>500%) + liq/mcap=0.4% <1%")[2], -30)
        self.assertEqual(rp("SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.3% >=3% (sin penalización)")[2], 0)
        self.assertIsNone(rp("algo que no existe"))


class Salida(unittest.TestCase):
    def test_save_dossier_escribe_md_y_json(self):
        d = m.dry_run_dossier()
        tmp = Path(tempfile.mkdtemp(prefix="dossier_"))
        try:
            path = m.save_dossier(d, tmp / "solana" / f"{m.VSOF_MINT}.md")
            self.assertEqual(path.read_text(encoding="utf-8"), m.render_markdown(d))
            data = json.loads(path.with_suffix(".json").read_text(encoding="utf-8"))
            self.assertEqual(data["meta"]["input_sha256"], d["meta"]["input_sha256"])
            self.assertEqual(data["inputs"]["record"]["score"], 95)
            self.assertEqual(sorted(p.name for p in path.parent.iterdir()), [f"{m.VSOF_MINT}.json", f"{m.VSOF_MINT}.md"])
        finally:
            shutil.rmtree(tmp)

    def test_ruta_por_defecto_chain_y_mint(self):
        d = m.dry_run_dossier()
        self.assertEqual(m.default_path(d), m.DOSSIERS_DIR / "solana" / f"{m.VSOF_MINT}.md")

    def test_huella_cambia_con_los_datos(self):
        a = m.build_dossier("Mint4", "solana", bare_data(bare_record("Mint4")), now=NOW)
        b = m.build_dossier("Mint4", "solana", bare_data(bare_record("Mint4", score=1)), now=NOW)
        self.assertNotEqual(a["meta"]["input_sha256"], b["meta"]["input_sha256"])

    def test_pdf_pendiente(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(m.generate_pdf(m.dry_run_dossier()))


CG_BONK = {"id": "bonk", "symbol": "bonk", "categories": ["Meme", "Solana Meme", "Dog-Themed"],
           "tickers": [{"market": {"identifier": "binance"}, "base": "BONK", "target": "USDT",
                        "trade_url": "https://www.binance.com/en/trade/BONK_USDT?ref=37754157"},
                       {"market": {"identifier": "binance"}, "base": "BONK", "target": "TRY"},
                       {"market": {"identifier": "gdax"}, "base": "BONK", "target": "USD"},
                       {"market": {"identifier": "kraken"}, "base": "BONK", "target": "USD"},
                       {"market": {"identifier": "mexc"}, "base": "BONK", "target": "USDT"}]}


class ExchangeYCategoria(unittest.TestCase):
    """Fase 4 T2: ruta por exchange centralizado confirmada por contrato, y categoría / narrativa."""

    def live(self, cg=None, binance=None, coinbase=None, cex=True):
        return {"queried_at": "2026-10-01T04:30:00+00:00", "coingecko": cg,
                "cex": {"symbol": "BONK", "binance": binance, "coinbase": coinbase,
                        "at": "2026-10-01T04:30:00+00:00"} if cex else None}

    def test_ficha_de_coingecko(self):
        cg = m.parse_coingecko_contract(CG_BONK)
        self.assertEqual((cg["id"], cg["symbol"], cg["listed"]), ("bonk", "BONK", True))
        self.assertEqual(cg["cex"], {"Binance": [["BONK", "USDT"]], "Coinbase": [["BONK", "USD"]],
                                     "Kraken": [["BONK", "USD"]]})            # sin TRY ni exchanges fuera de la lista
        self.assertIsNone(m.parse_coingecko_contract({"error": "coin not found"}))

    def test_confirmado_por_contrato_con_enlaces_limpios(self):
        text, links = m.cex_route("BONK", self.live(m.parse_coingecko_contract(CG_BONK), True, True))
        self.assertEqual(links, [("Binance", "https://www.binance.com/en/trade/BONK_USDT"),
                                 ("Coinbase", "https://www.coinbase.com/advanced-trade/spot/BONK-USD"),
                                 ("Kraken", "https://pro.kraken.com/app/trade/BONK-USD")])
        self.assertNotIn("ref=", text)                                     # nunca el código de referido de CoinGecko
        self.assertIn("confirmado por contrato", text)

    def test_homonimo_no_se_enlaza(self):
        cg = {"listed": True, "id": "otro", "symbol": "BONK", "categories": [], "cex": {}}
        text, links = m.cex_route("BONK", self.live(cg, binance=True, coinbase=False))
        self.assertEqual(links, [])
        self.assertIn("Binance tiene un par BONKUSDT, pero CoinGecko no lo vincula a este contrato", text)
        self.assertNotIn("binance.com", text)

    def test_no_cotiza(self):
        text, links = m.cex_route("VSOF", self.live({"listed": False}, False, False))
        self.assertEqual(links, [])
        self.assertIn("no cotiza en Binance ni en Coinbase", text)
        self.assertIn("CoinGecko sin ficha para este contrato", text)

    def test_consulta_fallida_o_ausente_es_nd(self):
        self.assertIn("n/d (consulta fallida)", m.cex_route("X", self.live(None, None, None))[0])
        self.assertIn("n/d (sin consulta", m.cex_route("X", {"queried_at": None})[0])

    def test_blue_chip(self):
        text, links = m.cex_route("SOL", None)
        self.assertEqual([n for n, _ in links], ["Binance", "Coinbase", "Kraken"])
        self.assertIn("https://www.binance.com/en/trade/SOL_USDT", text)

    def test_binance_y_coinbase(self):
        self.assertTrue(m.parse_binance_symbol({"symbols": [{"symbol": "BONKUSDT", "status": "TRADING"}]}, "BONKUSDT"))
        self.assertFalse(m.parse_binance_symbol({"symbols": [{"symbol": "BONKUSDT", "status": "BREAK"}]}, "BONKUSDT"))
        self.assertTrue(m.parse_coinbase_product({"status": "online", "trading_disabled": False}))
        self.assertFalse(m.parse_coinbase_product({"status": "delisted"}))

    def test_categorias_scanner_y_narrativa(self):
        scan = {"generated_at": "2026-10-01T04:00:00+00:00",
                "groups": {"f": {"items": [{"id": "bonk", "source": "layer-1"}]}},
                "onchain": {"solana": {"items": [{"token_address": "MintA"}]}}}
        index = m.scanner_index(scan)
        self.assertEqual(m.scanner_match(index, "minta")["group"], "a")      # por contrato, sin distinguir mayúsculas
        self.assertEqual(m.scanner_match(index, "otro", "bonk")["category"], "layer-1")
        self.assertIsNone(m.scanner_match(index, "otro", "nada"))
        registry = {"narratives": {"gta6": {"title": "GTA VI", "tokens": [{"address": "MINTA", "link_type": "thematic"}]}}}
        narratives = m.registry_matches(registry, "minta")
        text = m.categories_text({"coingecko": m.parse_coingecko_contract(CG_BONK)}, m.scanner_match(index, "MintA"), narratives)
        self.assertEqual(text, "CoinGecko: Meme, Solana Meme, Dog-Themed · scanner multi-chain: grupo a "
                               "(memecoins micro-cap, trending_pools de solana) · narrativa: GTA VI (vínculo thematic, registro curado)")
        self.assertIn("n/d (CoinGecko sin ficha", m.categories_text({"coingecko": {"listed": False}}, None, []))

    def test_fetch_live_distingue_no_listado_de_falla(self):
        class R:
            def __init__(self, status, data=None):
                self.status_code, self.ok, self._data = status, status == 200, data

            def json(self):
                return self._data

        class S:
            def get(self, url, timeout=None, headers=None):
                if "coingecko" in url:
                    return R(404)
                if "binance" in url:
                    return R(400)
                if "coinbase" in url:
                    return R(503)
                return R(500)
        live = m.fetch_live("MintX", "solana", {"token": {"symbol": "TEST"}}, session=S(), pause_s=0)
        self.assertEqual(live["coingecko"], {"listed": False})
        self.assertEqual((live["cex"]["binance"], live["cex"]["coinbase"]), (False, None))   # 400 = no existe; 503 = n/d

    def test_dry_run_vsof_no_cotiza(self):
        d = m.dry_run_dossier()
        self.assertIn("no cotiza en Binance ni en Coinbase (consulta 01/10/2026 04:30 UTC", d["acquisition"]["cex_route"])
        self.assertTrue(d["nature"]["categories"].startswith("n/d (CoinGecko sin ficha"))


class BlobGit(unittest.TestCase):
    def test_blob_coincide_con_git_ls_tree(self):
        rel = "02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json"
        path = REPO / rel
        if not path.exists() or shutil.which("git") is None:
            self.skipTest("sin el archivo o sin git")
        out = subprocess.run(["git", "ls-tree", "HEAD", "--", rel], cwd=str(REPO), capture_output=True, text=True)
        match = re.search(r"blob ([0-9a-f]{40})", out.stdout)
        if not match:
            self.skipTest("archivo sin commitear")
        self.assertEqual(m.git_blob(path), match.group(1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
