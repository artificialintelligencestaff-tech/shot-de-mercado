#!/usr/bin/env python3
"""Tests de D-089-R T4: CoinMarketCap (calendario ICO) e ICO Drops como fuentes de bot_prelaunch_calendar. unittest,
sin red (HTTP simulado con la forma real de las páginas verificadas el 2026-10-04).

Uso: python 04_Config/scripts/test_d089_prelaunch_fuentes.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_prelaunch_calendar as pc  # noqa: E402
import lib_events as events  # noqa: E402
from test_bot_prelaunch_calendar import FakeHTTP, T0, H, D  # noqa: E402


def cmc_html(ongoing=(), upcoming=(), ended=()):
    def ico(sym, name, price=None, slug=None, chain="Ethereum", stage="ICO"):
        return {"icoPriceUsd": price, "currentStage": stage, "start": "2026-08-01T00:00:00.000Z",
                "end": "2026-11-09T12:00:00.000Z", "goalUsd": 350000, "launchPad": {"exchangeName": "Launchpad X"},
                "crypto": {"name": name, "symbol": sym, "slug": slug or name.lower(),
                           "contracts": [{"id": 1027, "name": chain}] if chain else []}}
    pp = {"ongoing": {"icoList": [ico(*x) for x in ongoing]}, "upcoming": {"icoList": [ico(*x) for x in upcoming]},
          "ended": {"icoList": [ico(*x) for x in ended]}}
    return f'<html><script id="__NEXT_DATA__" type="application/json">{json.dumps({"props": {"pageProps": pp}})}</script></html>'


def icd_list(rows):
    """rows: [(slug, nombre, ronda, pre_valuacion, fecha)] con el marcado real de la tabla de ICO Drops."""
    out = ['<html><section><ul class="Tbl">']
    for slug, name, ronda, preval, fecha in rows:
        out.append(f'''<li class="Tbl-Row Tbl-Row--usual" tabindex="0" @keydown.enter="window.location.assign('/{slug}/')">
  <div class="Tbl-Row__item Tbl-Row__item--avt Tbl-Row__item--sticky"><a class="Cll-Avt" href="/{slug}/" tabindex="-1"></a></div>
  <div class="Tbl-Row__item Tbl-Row__item--project"><div class="Cll-Project"><a class="Cll-Project__link" href="/{slug}/">
    <p class="Cll-Project__name ">
        {name}
    </p><ul class="Tags-List"></ul></a></div></div>
  <div class="Tbl-Row__item Tbl-Row__item--round"><p class="Cll-Value Cll-Value--ellipsis">
  {ronda}
</p></div>
  <div class="Tbl-Row__item Tbl-Row__item--raised"><p class="Cll-Value">—</p></div>
  <div class="Tbl-Row__item Tbl-Row__item--pre-valuation"><p class="Cll-Value">{preval} &nbsp</p></div>
  <div class="Tbl-Row__item Tbl-Row__item--date"><p class="Cll-Value">{fecha}</p></div>
</li>''')
    return "\n".join(out) + "</ul></section></html>"


def icd_project(name, sym=None, price=None):
    title = f"{name}\n     ({sym}) - All information" if sym else f"{name} - All information"
    rnd = (f'<div class="Cpsl-Items"><span class="Cpsl-Items__item Cpsl-Items__item--pale">Price</span> '
           f'<span class="Cpsl-Items__item">${price}</span></div>') if price else ""
    return f"<html><head><title>\n    {title}\n    about {name} ICO (Token Sale) - ICO Drops\n  </title></head><body>{rnd}</body></html>"


CMC_URL, ICD_URL = pc.URLS["coinmarketcap"], pc.URLS["icodrops"]
PROJ = lambda slug: pc.URLS["icodrops_project"].format(slug=slug)  # noqa: E731
ROWS = [("credible", "Credible", "TGE and Distribution", "$200 M", "Upcoming"),
        ("konnex", "Konnex", "TGE and Distribution", "—", "Upcoming"),
        ("newton-protocol", "Newton", "IDO on Kommunitas", "$60 M", "Dec 1, 2026")]
PAGES = {PROJ("credible"): (200, icd_project("Credible", "CRED", "0.2")), PROJ("konnex"): (200, icd_project("Konnex")),
         PROJ("newton-protocol"): (200, icd_project("Newton", "NEWT", "0.1"))}


class TestFuentesD089(unittest.TestCase):
    def test_1_coinmarketcap_calendario_ico(self):
        html = cmc_html(ongoing=[("CRED", "Credible", 0.2, "credible")], upcoming=[("ZZZ", "Zeta", None, "zeta", None)],
                        ended=[("OLD", "Viejo", 1.0)])
        obs = pc.parse_coinmarketcap(html)
        self.assertEqual([(o["symbol"], o["name"], o["price"], o["chain"], o["extra"]["etapa"]) for o in obs],
                         [("CRED", "Credible", 0.2, "ethereum", "ongoing"), ("ZZZ", "Zeta", None, None, "upcoming")])
        self.assertEqual(obs[0]["url"], "https://coinmarketcap.com/currencies/credible/")
        self.assertEqual((obs[0]["extra"]["ronda"], obs[0]["extra"]["meta_usd"]), ("ICO", 350000))   # las ended no entran
        for bad in ("<html>sin datos</html>", '<script id="__NEXT_DATA__" type="application/json">{"props": {"pageProps": {}}}</script>'):
            with self.assertRaises(ValueError):
                pc.parse_coinmarketcap(bad)
        with self.assertRaises(pc.SourceError):
            pc.fetch_source("coinmarketcap", FakeHTTP(overrides={CMC_URL: (403, None)}))

    def test_2_icodrops_lista_detalle_tope_y_cache(self):
        rows = pc.parse_icodrops_list(icd_list(ROWS))
        self.assertEqual([(r["slug"], r["name"], r["ronda"], r["pre_valuacion"], r["fecha"]) for r in rows],
                         [("credible", "Credible", "TGE and Distribution", "$200 M", "Upcoming"),
                          ("konnex", "Konnex", "TGE and Distribution", None, "Upcoming"),
                          ("newton-protocol", "Newton", "IDO on Kommunitas", "$60 M", "Dec 1, 2026")])
        self.assertEqual(pc.parse_icodrops_project(icd_project("Credible", "CRED", "0.2")), {"symbol": "CRED", "price": 0.2})
        self.assertEqual(pc.parse_icodrops_project(icd_project("Konnex")), {"symbol": None, "price": None})
        with self.assertRaises(ValueError):
            pc.parse_icodrops_list("<html>rediseño</html>")
        http = FakeHTTP(overrides={ICD_URL: (200, icd_list(ROWS)), **PAGES})
        ctx = {"cache": {}, "now": T0, "sleep": lambda s: None, "detalle_max": 2}
        obs = pc.fetch_source("icodrops", http, ctx)
        self.assertEqual([(o["symbol"], o["name"], o["price"]) for o in obs],
                         [("CRED", "Credible", 0.2), (None, "Konnex", None), (None, "Newton", None)])   # tope de 2 páginas
        self.assertEqual(sorted(ctx["cache"]), ["credible", "konnex"])
        self.assertEqual(obs[0]["url"], "https://icodrops.com/credible/")
        http.calls.clear()
        obs = pc.fetch_source("icodrops", http, dict(ctx, now=T0 + 6 * H))
        self.assertEqual([c for c in http.calls if c != ICD_URL], [PROJ("newton-protocol")])   # solo la que faltaba
        self.assertEqual(obs[2]["symbol"], "NEWT")
        http.calls.clear()
        pc.fetch_source("icodrops", http, dict(ctx, now=T0 + 8 * D, detalle_max=5))
        self.assertEqual(len([c for c in http.calls if c != ICD_URL]), 3)                    # caché de 7 d vencida

    def test_3_integracion_calendario_precio_y_fallas(self):
        root = Path(tempfile.mkdtemp(prefix="prelaunch_d089_"))
        try:
            cfg = {"min_sources_confirm": 2, "purge_born_hours": 72, "purge_unborn_days": 30, "purged_memory_days": 90,
                   "liq_born_usd": 100000, "pause_s": 0,
                   "sources": {"hyperliquid": {"enabled": True}, "coinmarketcap": {"enabled": True},
                               "icodrops": {"enabled": True, "detalle_max": 15}}}
            routes = {CMC_URL: (200, cmc_html(ongoing=[("CRED", "Credible", 0.2, "credible")])),
                      ICD_URL: (200, icd_list(ROWS)), **PAGES}
            out = pc.run(cfg, root, FakeHTTP(overrides=routes), now=T0, sleep=lambda s: None)
            a = out["calendar"]["assets"]
            cred = a["sym:CRED"]
            self.assertEqual((cred["state"], sorted(cred["sources"])), ("confirmado", ["coinmarketcap", "icodrops"]))
            self.assertEqual((cred["precio_preventa"], cred["precio_venta"]["usd"]), (0.2, 0.2))
            newt = a["sym:NEWT"]                                    # perp de Hyperliquid + venta en ICO Drops
            self.assertEqual((newt["precio_preventa"], newt["precio_preventa_fuente"]), (0.5, "hyperliquid"))   # el perp manda
            self.assertEqual(newt["precio_venta"], {"usd": 0.1, "fuente": "icodrops", "ts": T0})
            self.assertEqual(newt["state"], "confirmado")
            self.assertIn("name:konnex", a)                         # sin ticker publicado: entra por nombre
            st = out["state"]
            self.assertEqual((st["sources"]["coinmarketcap"]["items"], st["sources"]["icodrops"]["items"]), (1, 3))
            self.assertEqual(sorted(st["icodrops_cache"]), ["credible", "konnex", "newton-protocol"])
            # ICO Drops cae: CMC sigue y el calendario conserva lo que tenía
            routes[ICD_URL] = (500, None)
            out = pc.run(cfg, root, FakeHTTP(overrides=routes), now=T0 + 6 * H, sleep=lambda s: None)
            self.assertEqual((out["state"]["sources"]["icodrops"]["status"], out["state"]["sources"]["icodrops"]["fails"]), (500, 1))
            self.assertTrue(out["state"]["sources"]["coinmarketcap"]["ok"])
            self.assertIn("sym:CRED", out["calendar"]["assets"])
            # nace por token_nacido (por símbolo, 2 fuentes): el delta usa el precio de la venta
            events.write_event("token_nacido", "So1cred111111111111111111111111111111111111", 2,
                               {"symbol": "CRED", "name": "Credible", "price_usd": 0.3}, writer="early_watch_a",
                               now=T0 + 7 * H, root=root)
            out = pc.run(cfg, root, FakeHTTP(overrides=routes), now=T0 + 8 * H, sleep=lambda s: None)
            born = out["calendar"]["assets"]["sym:CRED"]["born"]
            self.assertEqual((born["match"], born["precio_preventa"], born["precio_apertura"], born["delta_preventa_apertura_pct"]),
                             ("simbolo", 0.2, 0.3, 50.0))
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
