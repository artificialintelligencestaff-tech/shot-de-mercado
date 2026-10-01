#!/usr/bin/env python3
"""Guías de compra multi-chain (Fase 6) — script_97 + script_113 (unittest, sin red).

- Cada chain con guía completa tiene >= 1 wallet y >= 1 DEX con URL, explorador y fondeo: emite.
- Una chain sin guía, o con la guía a medias (Monad sin DEX), NO emite (acquisition_ready=False) y el dossier lo
  dice (regla núcleo, doc 24).
- El bloque 🛒 se arma con 1 o 2 wallets y con o sin DEX alternativos.

Uso: python 04_Config/scripts/test_script_97_guias.py
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
EVM = "0x4200000000000000000000000000000000000042"
READY = ("solana", "ethereum", "base", "arbitrum", "optimism", "blast")


def load(name, file, root):
    os.environ["SHOT_ROOT"] = root
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def token(chain, mint=EVM, liquidity=120_000.0):
    created = int(datetime(2026, 10, 1, 9, 0, tzinfo=timezone.utc).timestamp() * 1000)
    tok = {"token": {"symbol": "TST", "name": "Test Token", "mint": mint}, "score": 70,
           "detected_at": "2026-10-01T12:00:00+00:00",
           "dexscreener": {"priceUsd": 0.01, "liquidityUsd": liquidity, "dexId": "uniswap",
                           "pairAddress": "0x" + "ab" * 20, "pairCreatedAt": created}}
    if chain:
        tok["chain"] = chain
    return tok


class GuiasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="guias_")
        cls.m = load("s97_guias", "script_97_emit_alerts.py", cls.tmp)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_cada_chain_lista_tiene_wallet_dex_explorador_y_fondeo(self):
        for chain in READY:
            g = self.m.guide_for(chain)
            self.assertIsNotNone(g, chain)
            self.assertGreaterEqual(len(g["wallets"]), 1, chain)
            self.assertGreaterEqual(len(g["dexes"]), 1, chain)
            for name, url in g["wallets"] + g["dexes"]:
                self.assertTrue(name and url.startswith("https://"), (chain, name, url))
            self.assertTrue(g["fund"] and g["native"] and g["address_word"], chain)
            self.assertIn(chain, self.m.EXPLORERS, chain)
            self.assertIn(chain, self.m.CHAIN_LABELS, chain)
            self.assertTrue(self.m.acquisition_ready(token(chain)), chain)

    def test_guias_de_la_directiva(self):
        names = lambda chain, key: [n for n, _ in self.m.ACQUISITION_GUIDES[chain][key]]   # noqa: E731
        self.assertEqual(names("arbitrum", "wallets"), ["MetaMask", "Rabby"])
        self.assertEqual(names("arbitrum", "dexes"), ["Uniswap", "1inch"])
        self.assertEqual(names("optimism", "dexes"), ["Uniswap"])
        self.assertEqual(names("blast", "dexes"), ["Thruster", "Blasterswap"])
        self.assertEqual(self.m.ACQUISITION_GUIDES["monad"]["native"], "MON")
        self.assertEqual(self.m.EXPLORERS["arbitrum"][1].format(addr=EVM), f"https://arbiscan.io/token/{EVM}")
        self.assertEqual(self.m.EXPLORERS["optimism"][1].format(addr=EVM),
                         f"https://optimistic.etherscan.io/token/{EVM}")

    def test_chain_sin_guia_o_con_guia_incompleta_no_emite(self):
        for chain in ("monad", "tron", "bsc"):
            self.assertIsNone(self.m.guide_for(chain), chain)
            self.assertFalse(self.m.acquisition_ready(token(chain)), chain)
        self.assertIsNone(self.m.guide_for(None))
        self.assertFalse(self.m.acquisition_ready(token("arbitrum", mint="")))          # sin contrato
        # Una guía con URL vacía cuenta como incompleta.
        saved = self.m.ACQUISITION_GUIDES["optimism"]
        try:
            self.m.ACQUISITION_GUIDES["optimism"] = dict(saved, dexes=[("Uniswap", "")])
            self.assertIsNone(self.m.guide_for("optimism"))
        finally:
            self.m.ACQUISITION_GUIDES["optimism"] = saved

    def test_bloque_de_compra_con_una_wallet_y_sin_alternativas(self):
        msg, _ = self.m.format_alert_message(token("blast"), (), None)
        self.assertIn("🛒 *CÓMO ADQUIRIRLO* — Blast", msg)
        self.assertIn("1. Wallet: MetaMask (https://metamask.io)\n", msg)
        self.assertIn("3. Conectar la wallet a Thruster (https://thruster.finance) (liquidez principal en uniswap)"
                      " · alternativas: Blasterswap (https://blasterswap.com)", msg)
        self.assertIn(f"https://blastscan.io/token/{EVM}", msg)
        msg, _ = self.m.format_alert_message(token("optimism"), (), None)
        self.assertIn("3. Conectar la wallet a Uniswap (https://app.uniswap.org) (liquidez principal en uniswap)\n", msg)
        self.assertNotIn("alternativas:", msg)
        self.assertIn("1. Wallet: MetaMask (https://metamask.io) o Rabby (https://rabby.io)", msg)
        self.assertIn("ETH o USDC en la red Optimism (OP Mainnet)", msg)

    def test_monad_dice_sin_guia_en_el_bloque(self):
        msg, _ = self.m.format_alert_message(token("monad"), (), None)
        self.assertIn("• Sin guía de compra verificada para esta chain", msg)

    def test_dossier_usa_la_misma_regla(self):
        s113 = load("s113_guias", "script_113_dossier_builder.py", self.tmp)
        src = (SCRIPTS / "script_113_dossier_builder.py").read_text(encoding="utf-8")
        self.assertIn("s97.guide_for(chain)", src)
        self.assertNotIn("s97.ACQUISITION_GUIDES.get(chain)", src)
        self.assertTrue(hasattr(s113, "build_dossier"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
