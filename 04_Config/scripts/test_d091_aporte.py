#!/usr/bin/env python3
"""Tests de D-091 en bot_influencer_tracker: métrica de aporte ampliada (un test por tipo: cashtag, contrato,
(TICKER)/#TICKER, keyword sectorial + activo, anuncio) y la política de NO eliminación con revisión de Yang a los 60 d.
unittest, sin red.

Uso: python 04_Config/scripts/test_d091_aporte.py
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
from test_bot_influencer_tracker import FX, MINT, MINT2, T0, D, H, Http, cfg, fx_body, fx_post  # noqa: E402

VIG = {"symbols": {"HNT", "NEWT", "HYPE", "ONDO", "BTC", "RENDER"}, "contracts": {MINT2},
       "names": {"helium": "HNT", "ondo": "ONDO", "render network": "RENDER", "render": "RENDER"}, "fuentes": {}}
MAJORS = ["BTC", "ETH", "SOL"]


def tipos(text):
    return bit.aporte_tipos({"text": text}, VIG, MAJORS)


def as_record(text):
    """El mismo post como lo ve la evaluación días después: registro src-1 de un diario, sin el texto."""
    rec = store.make_record(bit.BOT, "x", "tweet", text, id="1", ts=T0)
    rec["m"] = {"tok": bit.post_fields(text)[1], "ext": bit.extracto(text), "sg": bit.senales_aporte(text, VIG["names"])}
    return rec


class TestAporte(unittest.TestCase):
    def test_1_cashtag_de_activo_vigente(self):
        self.assertEqual(tipos("$HNT is pumping hard"), {"cashtag"})
        self.assertEqual(bit.calculate_aporte({"text": "$HNT is pumping hard"}, VIG, MAJORS), 1)
        self.assertEqual(tipos("$RANDOM to the moon"), set())                    # no vigente
        self.assertEqual(tipos("$BTC to the moon"), set())                       # vigente pero mayor
        self.assertEqual(bit.calculate_aporte({"c": ["HNT"], "m": {}}, VIG, MAJORS), 1)   # registro de un diario

    def test_2_contrato(self):
        self.assertEqual(tipos(f"new gem CA: {MINT}"), {"contrato"})            # contrato de token explícito
        self.assertEqual(tipos(f"https://pump.fun/coin/{MINT}"), {"contrato"})
        self.assertEqual(bit.aporte_tipos({"a": [MINT2], "c": [], "m": {}}, VIG, MAJORS), {"contrato"})  # dirección vigente
        self.assertEqual(bit.aporte_tipos({"a": ["So1wallet11111111111111111111111111111111"], "c": [], "m": {}},
                                          VIG, MAJORS), set())                  # una wallet cualquiera no

    def test_3_ticker_entre_parentesis_o_hashtag(self):
        # D-101 capa 1: solo prefijo $ o #; "(HNT)" suelto ya no cuenta como ticker
        self.assertEqual(tipos("Helium Mobile (HNT) adds subscribers"), set())
        self.assertEqual(tipos("Helium Mobile ($HNT) adds subscribers"), {"cashtag"})
        self.assertEqual(tipos("#HYPE season is here"), {"ticker"})
        self.assertEqual(tipos("#Hyperliquid volume record"), set())            # hashtag de nombre, no de ticker
        self.assertEqual(tipos("Event at 14:00 (UTC)"), set())                  # sigla en la lista de exclusión
        self.assertEqual(tipos("New project (ZZZQ) teaser"), set())             # ticker que no es vigente
        self.assertEqual(bit.aporte_tipos(as_record("Helium Mobile (HNT) adds subscribers"), VIG, MAJORS), set())

    def test_4_keyword_sectorial_mas_activo_vigente(self):
        self.assertEqual(tipos("DePIN keeps growing: Helium added 10k hotspots this week"), {"sector"})   # por nombre
        self.assertEqual(tipos("RWA demand is rising, ONDO leads the pack"), {"sector"})                # por ticker suelto
        self.assertEqual(tipos("Render Network is the backbone of decentralized AI compute"), {"sector"})
        self.assertEqual(tipos("DePIN is the future of infrastructure"), set())  # sector sin activo
        self.assertEqual(tipos("Helium hotspots are everywhere"), set())         # activo sin sector
        self.assertEqual(tipos("go touch grass, the ai hype is loud"), set())    # "ai" en minúscula no es el sector
        self.assertEqual(bit._name_variants("Render Network"), {"render network", "render"})
        self.assertEqual(bit._name_variants("Bitcoin Cash"), {"bitcoin cash"})   # "bitcoin" no apunta a BCH
        self.assertEqual(bit._name_variants("Blockchain Capital"), {"blockchain capital"})
        self.assertEqual(bit._name_variants("SOON"), set())                      # palabra común
        self.assertEqual(bit.aporte_tipos(as_record("DePIN keeps growing: Helium added 10k hotspots"), VIG, MAJORS),
                         {"sector"})                                             # sobrevive sin el texto (m.sg)

    def test_5_anuncio_oficial_con_ticker(self):
        # D-101 capa 1: el anuncio cuenta solo con un ticker vigente con prefijo $ o # (antes: cualquier ticker explícito)
        self.assertEqual(tipos("Binance Will List Newton ($NEWT) with seed tag"), {"anuncio", "cashtag"})
        self.assertEqual(tipos("Binance Will List Newton (NEWT) with seed tag"), set())   # sin prefijo
        self.assertEqual(tipos("Bybit to list $ZZZQ on spot tomorrow"), set())   # no vigente: ya no aporta
        self.assertEqual(tipos("TGE for #NEWT is set for Friday"), {"anuncio", "ticker"})
        self.assertEqual(tipos("TGE for #QQQZ is set for Friday"), set())
        self.assertEqual(tipos("Launching today: HYPE vaults for everyone"), set())   # suelto, sin prefijo
        self.assertEqual(tipos("HeliumOS lets you launch and scale your MVNO"), set())   # MVNO no es un ticker
        self.assertEqual(tipos("Japan Launches New Tax System. TOP10 news"), set())
        self.assertEqual(tipos("listing $BTC pairs for margin"), set())          # mayor
        self.assertEqual(bit.aporte_tipos(as_record("Bybit to list $NEWT on spot tomorrow"), VIG, MAJORS),
                         {"anuncio", "cashtag"})


class TestNoEliminacion(unittest.TestCase):
    def test_6_inactiva_mas_de_60_dias_sigue_y_decide_yang(self):
        c = cfg([("dormida", "depin", 3), ("lenta", "rwa", 3), ("activa", "cex", 1)])
        http = Http({FX.format("dormida"): (200, fx_body("dormida", [fx_post(1, T0 - 70 * D)]), {}),
                     FX.format("lenta"): (200, fx_body("lenta", [fx_post(2, T0 - 45 * D)]), {}),
                     FX.format("activa"): (200, fx_body("activa", [fx_post(3, T0 - H, "$HNT")]), {})})
        st = {}
        for i in range(3):                                                      # tres días seguidos
            _, _, st = bit.run(c, st, fetch=http, now=T0 + i * 25 * H, sleep=lambda s: None, vig=VIG)
            d, lenta = st["sources"]["dormida"], st["sources"]["lenta"]
            self.assertEqual(d["evaluar_motivo"], ["sin_post_30d", "inactiva_60d_decide_yang"])
            self.assertTrue(d["evaluar"] and d["revision_yang"])
            self.assertEqual((lenta["evaluar_motivo"], lenta["revision_yang"]), (["sin_post_30d"], False))
            self.assertNotIn("auto_off_until", d)                               # marcar no apaga
            self.assertEqual(d["next_check"] - d["checked_at"], 24 * 3600)      # su turno normal de congelada
        self.assertEqual(http.count(FX.format("dormida")), 3)                   # se sigue consultando
        self.assertEqual(sorted(st["sources"]), ["activa", "dormida", "lenta"])  # nadie sale del estado
        self.assertEqual([x["cuenta"] for x in c["cuentas"]], ["dormida", "lenta", "activa"])   # ni de la config
        md, log = bit.reporte_semanal(st, c)
        self.assertIn("## Revisión de Yang: 1 cuentas con > 60 días sin publicar", md)
        self.assertIn("- dormida (depin, prioridad 3)", md)
        self.assertIn("decisión de Yang, no de la máquina", md)
        self.assertEqual([f["cuenta"] for f in log["evaluar"] if f["revision_yang"]], ["dormida"])
        # corrida completa: influencers.yaml queda byte a byte igual
        tmp = Path(tempfile.mkdtemp(prefix="xinf_d091_"))
        root, http_get = store.ROOT, bit.http_get
        try:
            (tmp / "04_Config").mkdir()
            yaml_text = "pause_s: 0\nmecanismos: [fxembed]\ncuentas:\n  - {cuenta: dormida, categoria: depin, prioridad: 3}\n"
            cfg_file = tmp / "04_Config" / "influencers.yaml"
            cfg_file.write_text(yaml_text, encoding="utf-8")
            store.ROOT = tmp
            bit.http_get = Http({FX.format("dormida"): (200, fx_body("dormida", [fx_post(1, int(time.time()) - 70 * D)]), {})})
            self.assertEqual(bit.main(["--reporte"]), 0)
            self.assertEqual(cfg_file.read_text(encoding="utf-8"), yaml_text)
            state = json.loads((tmp / "02_Analisis" / "sources" / "x_influencers" / "_state.json").read_text(encoding="utf-8"))
            self.assertTrue(state["sources"]["dormida"]["revision_yang"])
        finally:
            store.ROOT, bit.http_get = root, http_get
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
