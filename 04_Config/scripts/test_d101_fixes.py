#!/usr/bin/env python3
"""Tests de D-101 (doc 38 §5): fix A (retención por carpeta), fix B (precio de preventa vs venta) y fix C (filtros
de falsos positivos del aporte, 2 tests por capa + la muestra etiquetada). unittest, sin red.

Uso: python 04_Config/scripts/test_d101_fixes.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_influencer_tracker as bit  # noqa: E402
import bot_orchestrator as orch  # noqa: E402
import bot_prelaunch_calendar as pc  # noqa: E402
import lib_sources_store as store  # noqa: E402
from test_d091_aporte import MAJORS, VIG, as_record, tipos  # noqa: E402

ROOT = SCRIPTS.parents[1]
NOW = 1_791_000_000
DAY = 86400


def day(offset_days):
    return datetime.fromtimestamp(NOW - offset_days * DAY, timezone.utc).strftime("%Y-%m-%d")


class FixA(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="d101_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.src = self.root / "02_Analisis" / "sources"
        for bot in ("rss", "x_influencers"):
            (self.src / bot).mkdir(parents=True)
        shutil.copy(ROOT / "02_Analisis" / "sources" / "_retention.yaml", self.src)
        shutil.copy(ROOT / "02_Analisis" / "sources" / "x_influencers" / "_retention.yaml", self.src / "x_influencers")

    def touch(self, bot, age):
        p = self.src / bot / f"{day(age)}.jsonl"
        p.write_text("{}\n")
        return p

    def test_x_influencers_35_dias_y_el_resto_7(self):
        keep_x, cut_rss, keep_rss = self.touch("x_influencers", 20), self.touch("rss", 20), self.touch("rss", 3)
        old_x = self.touch("x_influencers", 36)
        audit = self.src / "rss" / "_audit.jsonl"
        audit.write_text("{}\n")
        orch.prune(self.root, NOW)
        self.assertTrue(keep_x.exists() and keep_rss.exists() and audit.exists())
        self.assertFalse(cut_rss.exists() or old_x.exists())

    def test_sin_poda_yaml_roto_y_sin_archivo(self):
        self.assertEqual(orch.retention_for(self.src / "x_influencers", self.root), 35)
        self.assertEqual(orch.retention_for(self.src / "rss", self.root), 7)
        (self.src / "rss" / "_retention.yaml").write_text("keep_days: null\n")
        self.assertIsNone(orch.retention_for(self.src / "rss", self.root))       # sin poda (patrimonio)
        p = self.touch("rss", 400)
        orch.prune(self.root, NOW)
        self.assertTrue(p.exists())
        (self.src / "rss" / "_retention.yaml").write_text("keep_days: [roto\n")
        (self.src / "_retention.yaml").unlink()
        self.assertEqual(orch.retention_for(self.src / "rss", self.root), orch.KEEP_DAYS)   # roto: default
        self.assertTrue(orch.DAY_FILE.match("2026-10-05_a.jsonl") and not orch.DAY_FILE.match("_falsos_positivos.jsonl"))

    def test_cubre_la_historia_del_bot(self):
        import yaml
        keep = yaml.safe_load((ROOT / "02_Analisis/sources/x_influencers/_retention.yaml").read_text())["keep_days"]
        hist = yaml.safe_load((ROOT / "04_Config/influencers.yaml").read_text())["historia_dias"]
        self.assertGreaterEqual(keep, hist)


class FixB(unittest.TestCase):
    def test_venta_nunca_es_preventa_y_migracion(self):
        a = {"precio_preventa": 0.2, "precio_preventa_ts": 5, "precio_preventa_fuente": "icodrops"}
        self.assertTrue(pc.split_sale_price(a))
        self.assertEqual(a, {"precio_venta": {"usd": 0.2, "fuente": "icodrops", "ts": 5}})
        self.assertFalse(pc.split_sale_price(a))                                  # idempotente
        perp = {"precio_preventa": 0.5, "precio_preventa_fuente": "hyperliquid"}
        self.assertFalse(pc.split_sale_price(perp))
        self.assertEqual(perp["precio_preventa"], 0.5)

    def test_script_97_no_llama_preventa_a_la_venta(self):
        import script_97_emit_alerts as s97
        tmp = Path(tempfile.mkdtemp(prefix="d101b_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        mint = "So1cred111111111111111111111111111111111111"
        cal = tmp / "02_Analisis" / "prelaunch" / "_calendar.json"
        cal.parent.mkdir(parents=True)
        born = {"contract": mint, "alertable": True, "precio_preventa": None, "precio_venta": 0.2, "precio_apertura": 0.3,
                "delta_preventa_apertura_pct": None, "delta_venta_apertura_pct": 50.0}
        cal.write_text(json.dumps({"assets": {"k": {"prelaunch_known": True, "contract": mint, "born": born}}}))
        line = s97.prelaunch_line(mint, tmp)
        self.assertIn("precio de venta (ICO)", line)
        self.assertNotIn("precio preventa", line)
        born.update(precio_preventa=0.25, delta_preventa_apertura_pct=20.0)
        cal.write_text(json.dumps({"assets": {"k": {"prelaunch_known": True, "contract": mint, "born": born}}}))
        self.assertIn("precio preventa $0.25, delta vs apertura +20.0%", s97.prelaunch_line(mint, tmp))


class FixC(unittest.TestCase):
    # capa 1: validación de ticker
    def test_capa1_minimo_3_y_prefijo(self):
        self.assertFalse(bit.ticker_valido("ME", {"ME"}))
        self.assertFalse(bit.ticker_valido("hype", {"hype"}))
        self.assertTrue(bit.ticker_valido("HYPE", {"HYPE"}))
        self.assertEqual(tipos("Launching today: HYPE vaults"), set())            # sin $ ni #
        self.assertEqual(tipos("#HYPE season is here"), {"ticker"})

    def test_capa1_vigente_y_no_mayor(self):
        self.assertEqual(tipos("Launching our podcast ($ABC) next week"), set())  # no vigente
        self.assertEqual(tipos("listing $BTC pairs for margin"), set())           # mayor
        self.assertEqual(tipos("Bybit to list $NEWT tomorrow"), {"anuncio", "cashtag"})

    # capa 2: keyword sectorial con activo vigente
    def test_capa2_sector_sin_activo_no_cuenta(self):
        self.assertEqual(tipos("DePIN is the future of infrastructure"), set())
        self.assertEqual(tipos("RWA tokenization is booming this year"), set())

    def test_capa2_sector_con_activo_vigente(self):
        self.assertEqual(tipos("DePIN keeps growing: $HNT added 10k hotspots"), {"cashtag", "sector"})
        self.assertEqual(bit.aporte_tipos(as_record("DePIN keeps growing: $HNT added 10k hotspots"), VIG, MAJORS),
                         {"cashtag", "sector"})                                   # sobrevive sin el texto

    # capa 3: dedup por sha256 del texto normalizado
    def test_capa3_mismo_texto_normalizado(self):
        a = bit.sha256_normalizado("$HNT sube fuerte! https://t.co/abc")
        b = bit.sha256_normalizado("$hnt   SUBE fuerte https://x.com/otra")
        self.assertEqual(a, b)
        self.assertNotEqual(a, bit.sha256_normalizado("$HNT baja fuerte"))

    def test_capa3_un_texto_aporta_una_vez(self):
        def rec(pid, text):
            r = store.make_record(bit.BOT, "anal", "tweet", text, id=str(pid), ts=NOW - 3600)
            r["m"] = {"shn": bit.sha256_normalizado(text), "sg": bit.senales_aporte(text, VIG["names"])}
            return r
        posts = [rec(1, "$HNT sube https://t.co/1"), rec(2, "$hnt sube https://t.co/2"), rec(3, "$NEWT lista")]
        health = {"anal": {"checked_at": NOW}}
        cfg = {"evaluacion": {"ventana_dias": 30, "dias_sin_post": 30, "dias_revision_yang": 60,
                              "posts_min_sin_aporte": 10}, "cashtags_mayores": MAJORS}
        bit.evaluar_cuentas([{"cuenta": "anal"}], health, posts, NOW, cfg, VIG)
        self.assertEqual((health["anal"]["posts_30d"], health["anal"]["aporte_estimado"]), (3, 2))

    def test_muestra_etiquetada(self):
        path = ROOT / "02_Analisis" / "sources" / "x_influencers" / "_falsos_positivos.jsonl"
        rows = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
        self.assertGreaterEqual(len(rows), 12)
        for r in rows:
            got = tipos(r["texto"])
            self.assertEqual((bool(got), sorted(got)), (r["aporta"], sorted(r["tipos"])), r["texto"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
