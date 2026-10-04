#!/usr/bin/env python3
"""Tests del calendario de activos no nacidos (D-079): bot_prelaunch_calendar. unittest, sin red (HTTP simulado).

Uso: python 04_Config/scripts/test_bot_prelaunch_calendar.py
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
import bot_prelaunch_calendar as pc  # noqa: E402
import lib_episodic_memory as episodes  # noqa: E402
import lib_events as events  # noqa: E402

try:
    import bs4  # noqa: F401
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
requires_bs4 = unittest.skipUnless(HAS_BS4 or os.environ.get("REQUIRE_TEST_DEPS"),
                                   "beautifulsoup4 no instalado: pip install --require-hashes -r requirements-dev.txt")

T0 = 1791000000
H, D = 3600, 86400
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
CFG = {"min_sources_confirm": 2, "purge_born_hours": 72, "purge_unborn_days": 30, "purged_memory_days": 90,
       "liq_born_usd": 100000, "pause_s": 0, "excluir": ["BSV"],
       "sources": {k: {"enabled": True} for k in ("hyperliquid", "aevo", "polymarket", "bybit", "binance", "bitcointalk")}}
HL = [{"universe": [{"name": n} for n in ("BTC", "PURR", "NEWT", "FART", "BSV")] + [{"name": "OLD", "isDelisted": True}]},
      [{"markPx": p, "openInterest": "10", "dayNtlVlm": "5"} for p in ("60000", "0.2", "0.50", "0.17", "20", "1")]]
AEVO = [{"instrument_type": "PERPETUAL", "is_active": True, "market_type": "crypto", "underlying_asset": "NEWT",
         "mark_price": "0.52"},
        {"instrument_type": "PERPETUAL", "is_active": True, "market_type": "equity", "underlying_asset": "TSLA",
         "mark_price": "300"},
        {"instrument_type": "PERPETUAL", "is_active": True, "market_type": "crypto", "underlying_asset": "1000BTC",
         "mark_price": "60"},
        {"instrument_type": "PERPETUAL", "is_active": True, "market_type": "crypto", "underlying_asset": "JITO",
         "mark_price": "0.55"}]
PM = {"events": [{"title": "Newton FDV one day after launch?", "slug": "newton-fdv", "closed": False},
                 {"title": "Viejo FDV one day after launch?", "slug": "viejo", "closed": True}]}
BYBIT = {"result": {"list": [{"title": "Bybit to List Newton (NEWT) on Spot", "url": "https://bybit/a"},
                             {"title": "New listing: BTCUSDT Perpetual Contract", "url": "https://bybit/b"},
                             {"title": "USDC Token Splash", "url": "https://bybit/c"}]}}
BTT = f"""<table><tr><td><span id="msg_1"><a href="https://bitcointalk.org/index.php?topic=1.0">[ANN] Kitty Coin (KIT) | fair launch | CA {MINT}</a></span></td></tr>
<tr><td><span id="msg_2"><a href="https://bitcointalk.org/index.php?topic=2.0">Reglas del foro</a></span></td></tr>
<tr><td><span id="msg_3"><a href="https://bitcointalk.org/index.php?topic=3.0">[ANN] Tarcoin (TAR) | PoW | Mobile Wallets Live! | 300M Mined!</a></span></td></tr></table>"""
REFS = {"ref_bybit": {"result": {"list": [{"baseCoin": "BTC"}, {"baseCoin": "ETH"}]}},
        "ref_okx": {"data": [{"baseCcy": "BTC"}, {"baseCcy": "SOL"}]},
        "ref_binance": {"symbols": [{"baseAsset": "BNB"}]}}
DEX_FART = {"pairs": [{"chainId": "solana", "baseToken": {"symbol": "FART ", "address": "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"},
                       "liquidity": {"usd": 8800000}, "priceUsd": "0.175", "url": "https://dexscreener.com/x"}]}
DEX_SCAM = {"pairs": [{"chainId": "solana", "baseToken": {"symbol": "NEWT", "address": "So1scam111111111111111111111111111111111111"},
                       "liquidity": {"usd": 900}, "priceUsd": "0.0001"}]}


class FakeHTTP:
    def __init__(self, overrides=None, dex=None, spot_hl=("PURR",)):
        self.get_routes = {pc.URLS["aevo"]: (200, json.dumps(AEVO)), pc.URLS["polymarket"]: (200, json.dumps(PM)),
                           pc.URLS["bybit"]: (200, json.dumps(BYBIT)), pc.URLS["binance"]: (451, None),
                           pc.URLS["bitcointalk"]: (200, BTT)}
        self.get_routes.update({pc.URLS[k]: (200, json.dumps(v)) for k, v in REFS.items()})
        self.get_routes.update(overrides or {})
        jito = {"pairs": [{"chainId": "solana", "baseToken": {"symbol": "JTO", "name": "Jito", "address": "jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL"},
                           "liquidity": {"usd": 2500000}, "priceUsd": "0.55"}]}
        self.dex = {"FART": DEX_FART, "NEWT": DEX_SCAM, "JITO": jito, **(dex or {})}
        self.spot_hl, self.calls = spot_hl, []

    def get(self, url):
        self.calls.append(url)
        if url.startswith(pc.URLS["dex"]):
            return 200, json.dumps(self.dex.get(url[len(pc.URLS["dex"]):], {"pairs": []}))
        st, body = self.get_routes.get(url, (404, None))
        if isinstance(st, Exception):
            raise st
        return st, body

    def post(self, url, payload):
        self.calls.append(f"POST {payload['type']}")
        if payload["type"] == "metaAndAssetCtxs":
            return 200, json.dumps(HL)
        return 200, json.dumps({"tokens": [{"name": n} for n in self.spot_hl]})


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="prelaunch_"))
        self.addCleanup(shutil.rmtree, self.root, True)

    def run_cal(self, now=T0, http=None, **kw):
        return pc.run(CFG, self.root, http or FakeHTTP(), now=now, sleep=lambda s: None, **kw)

    def evs(self, type, now):
        return events.read_events(types=type, now=now, root=self.root)


@requires_bs4
class Calendario(Base):
    def test_alta_confirmacion_y_fusion_por_nombre(self):
        out = self.run_cal()
        a = out["calendar"]["assets"]
        self.assertEqual(sorted(a), ["sym:KIT", "sym:NEWT"])
        newt = a["sym:NEWT"]
        self.assertEqual((newt["state"], newt["name"]), ("confirmado", "Newton"))
        self.assertEqual(sorted(newt["sources"]), ["aevo", "bybit", "hyperliquid", "polymarket"])   # Polymarket solo trae nombre
        self.assertEqual(newt["precio_preventa"], 0.52)                                            # el último perp observado
        self.assertEqual((a["sym:KIT"]["state"], a["sym:KIT"]["contract"]), ("anunciado", MINT))
        self.assertEqual(sorted(e["data"]["key"] for e in self.evs("token_anunciado", T0 + 60)), ["sym:KIT", "sym:NEWT"])
        self.assertEqual([e["data"]["key"] for e in self.evs("token_confirmado", T0 + 60)], ["sym:NEWT"])
        again = self.run_cal(now=T0 + 6 * H)
        self.assertEqual(again["state"]["emitted"], 0)                                             # sin eventos repetidos

    def test_filtro_ya_nacido_spot_dex_y_excluidos(self):
        out = self.run_cal()
        keys = set(out["calendar"]["assets"])
        for born in ("sym:BTC", "sym:PURR", "sym:FART", "sym:BSV", "sym:OLD", "sym:TSLA", "sym:1000BTC", "sym:JITO",
                     "sym:TAR"):
            self.assertNotIn(born, keys)       # spot · spot HL · DEX ≥ 100k · excluido · delistado · equity · 1000BTC = BTC
        self.assertEqual(keys, {"sym:KIT", "sym:NEWT"})       # JITO = "Jito" (JTO) en DEX · TAR "Mined!" ya existe
        self.assertIn("sym:NEWT", keys)                        # el par "scam" de 900 USD no lo hace nacer
        # KIT tiene una sola fuente: si aparece en spot, no era un no nacido → se purga sin emitir nacimiento
        http = FakeHTTP(overrides={pc.URLS["ref_okx"]: (200, json.dumps({"data": [{"baseCcy": "KIT"}]}))})
        out = self.run_cal(now=T0 + 6 * H, http=http)
        self.assertNotIn("sym:KIT", out["calendar"]["assets"])
        self.assertEqual(out["calendar"]["purged"]["sym:KIT"]["motivo"], "nacio_sin_confirmacion")
        self.assertEqual(self.evs("prelaunch_nacido", T0 + 6 * H), [])

    def test_emparejamiento_por_contrato_al_nacer(self):
        self.run_cal()
        events.write_event("token_nacido", MINT, 2, {"symbol": "KIT", "name": "Kitty Coin", "chain": "solana",
                                                     "price_usd": 0.03}, writer="early_watch_a", now=T0 + H, root=self.root)
        out = self.run_cal(now=T0 + 2 * H)
        kit = out["calendar"]["assets"]["sym:KIT"]
        self.assertEqual((kit["state"], kit["prelaunch_known"], kit["born"]["match"], kit["born"]["alertable"]),
                         ("seguimiento", True, "contrato", True))
        self.assertEqual([h[0] for h in kit["history"]], ["anunciado", "nacido", "seguimiento"])
        (ev,) = self.evs("prelaunch_nacido", T0 + 2 * H)
        self.assertEqual((ev["subject"], ev["severity"], ev["data"]["alertable"], ev["data"]["via"]),
                         (MINT, 2, True, "token_nacido"))

    def test_emparejamiento_por_simbolo_solo_con_dos_fuentes(self):
        self.run_cal()
        other = "7cnqaJLZaSD1s2PchXuYjauGSk6c8Nuj9Zcd1V5aMdKU"
        events.write_event("token_nacido", other, 2, {"symbol": "NEWT", "name": "Newton", "chain": "solana",
                                                      "price_usd": 0.65}, writer="multichain_scanner", now=T0 + H, root=self.root)
        events.write_event("token_nacido", "So1other11111111111111111111111111111111111", 2,
                           {"symbol": "ZZZ", "name": "Zeta"}, writer="early_watch_a", now=T0 + H, root=self.root)
        out = self.run_cal(now=T0 + 2 * H)
        newt = out["calendar"]["assets"]["sym:NEWT"]
        self.assertEqual((newt["state"], newt["born"]["match"], newt["born"]["alertable"], newt["contract"]),
                         ("seguimiento", "simbolo", False, other))
        self.assertEqual(newt["born"]["delta_preventa_apertura_pct"], 25.0)              # 0,52 → 0,65
        (ev,) = self.evs("prelaunch_nacido", T0 + 2 * H)
        self.assertEqual((ev["severity"], ev["data"]["candidato"]), (1, True))          # sin contrato: no alertable
        cal = pc.Calendar(self.root, CFG, T0 + 3 * H, emit=False)
        cal.assets["sym:SOLO"] = {"key": "sym:SOLO", "symbol": "SOLO", "state": "anunciado", "sources": {"bybit": {}},
                                  "first_seen": T0}
        self.assertEqual(cal.match_birth(None, "SOLO", None, None)[1], "insuficiente")   # 1 fuente: no empareja

    def test_nacimiento_observado_en_dex(self):
        self.run_cal()
        dex = {"NEWT": {"pairs": [{"chainId": "solana", "baseToken": {"symbol": "NEWT", "address": MINT.replace("6", "8")},
                                   "liquidity": {"usd": 450000}, "priceUsd": "0.39"}]}}
        out = self.run_cal(now=T0 + 25 * H, http=FakeHTTP(dex=dex))                      # caché DEX vencida (24 h)
        newt = out["calendar"]["assets"]["sym:NEWT"]
        self.assertEqual((newt["state"], newt["born"]["via"], newt["born"]["chain"]), ("seguimiento", "observado_dex", "solana"))
        self.assertEqual(newt["born"]["delta_preventa_apertura_pct"], -25.0)             # 0,52 → 0,39

    def test_purga_72h_despues_de_nacer_va_a_memoria_episodica(self):
        self.run_cal()
        events.write_event("token_nacido", MINT, 2, {"symbol": "KIT", "price_usd": 0.03}, writer="early_watch_a",
                           now=T0 + H, root=self.root)
        self.run_cal(now=T0 + 2 * H)
        self.assertIn("sym:KIT", self.run_cal(now=T0 + 73 * H)["calendar"]["assets"])  # 71 h: sigue
        out = self.run_cal(now=T0 + 75 * H)
        self.assertNotIn("sym:KIT", out["calendar"]["assets"])
        self.assertEqual(out["calendar"]["purged"]["sym:KIT"]["motivo"], "seguimiento_cerrado")
        (ep,) = episodes.query_episodes({"tipo": "prelaunch_cerrado"}, self.root)
        self.assertEqual((ep["entidad"], ep["resultado"], ep["contexto"]["born"]["match"]), (MINT, "seguimiento_cerrado", "contrato"))
        self.assertEqual([e["data"]["motivo"] for e in self.evs("token_purgado", T0 + 75 * H)], ["seguimiento_cerrado"])
        self.assertNotIn("sym:KIT", self.run_cal(now=T0 + 81 * H)["calendar"]["assets"])  # no vuelve a entrar

    def test_purga_30_dias_sin_nacer(self):
        self.run_cal()
        self.assertIn("sym:NEWT", self.run_cal(now=T0 + 29 * D)["calendar"]["assets"])
        out = self.run_cal(now=T0 + 30 * D)
        self.assertEqual(out["calendar"]["purged"]["sym:NEWT"]["motivo"], "no_nacido")
        self.assertEqual(out["calendar"]["assets"], {})

    def test_fallo_de_una_fuente_no_rompe_la_corrida(self):
        http = FakeHTTP(overrides={pc.URLS["polymarket"]: (200, "{esto no es json"),
                                   pc.URLS["aevo"]: (ConnectionError("caída"), None)})
        out = self.run_cal(http=http)
        st = out["state"]["sources"]
        self.assertEqual((st["binance"]["status"], st["binance"]["note"]), (451, "[P] bloqueado desde runners US"))
        self.assertEqual(st["polymarket"]["status"], "parse_error")
        self.assertEqual(st["aevo"]["status"], "parse_error")
        self.assertEqual((st["hyperliquid"]["status"], st["bybit"]["status"], st["bitcointalk"]["status"]), (200, 200, 200))
        self.assertEqual(out["calendar"]["assets"]["sym:NEWT"]["state"], "confirmado")      # hyperliquid + bybit alcanzan
        saved = json.loads((self.root / "02_Analisis/prelaunch/_state.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["sources"]["binance"]["fails"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
