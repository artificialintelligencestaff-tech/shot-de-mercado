#!/usr/bin/env python3
"""Tests de bot_telegram_public (D-041 T5). unittest, sin red: HTML sintético de t.me/s/<canal>.

Uso: python 04_Config/scripts/test_bot_telegram_public.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_orchestrator as orch  # noqa: E402
import bot_telegram_public as tg  # noqa: E402
import lib_sources_store as store  # noqa: E402

NOW = 1791000000
MINT = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"


def message(channel, num, text, iso="2026-10-03T03:20:00+00:00", views="1.2K", link=None):
    a = f'<a href="{link}">ver</a>' if link else ""
    return (f'<div class="tgme_widget_message_wrap"><div class="tgme_widget_message js-widget_message" '
            f'data-post="{channel}/{num}"><div class="tgme_widget_message_text js-message_text">{text}<br/>{a}</div>'
            f'<div class="tgme_widget_message_footer"><span class="tgme_widget_message_views">{views}</span>'
            f'<a class="tgme_widget_message_date"><time datetime="{iso}"></time></a></div></div></div>')


def page(channel, *nums):
    return "<html><body>" + "".join(message(channel, n, f"post {n} sobre $WIF memecoin") for n in nums) + "</body></html>"


CONFIG = {"channels": [{"name": "canal_uno"}, {"name": "sin_preview"}], "pause_s": 0, "recheck_hours": 24,
          "loop_minutes": 40, "poll_minutes": 4}


class Fetch:
    def __init__(self, pages):
        self.pages, self.calls = pages, []

    def __call__(self, channel):
        self.calls.append(channel)
        if channel == "sin_preview":                          # Telegram redirige a t.me/<canal>
            return 200, "<html>canal</html>", f"https://t.me/{channel}"
        return 200, self.pages[channel], f"https://t.me/s/{channel}"


class Parser(unittest.TestCase):
    def test_parser_bs4_texto_enlaces_fecha_y_vistas(self):
        html = message("canal_uno", 41, "Nuevo token <b>VSOF</b>", views="1.2K",
                       link=f"https://pump.fun/coin/{MINT}")
        (m,) = tg.parse_preview(html)
        self.assertEqual((m["post"], m["num"], m["views"]), ("canal_uno/41", 41, 1200))
        self.assertEqual(m["ts"], 1790997600)                          # 2026-10-03T03:20:00Z
        self.assertIn("Nuevo token VSOF", m["text"])
        self.assertIn(MINT, m["text"])                                  # el contrato llega por el enlace
        r = tg.poll({"channels": [{"name": "canal_uno"}]}, {}, NOW, fetch=lambda c: (200, html, f"https://t.me/s/{c}"),
                    sleep=lambda s: None)[0][0]
        self.assertEqual((r["kind"], r["a"], r["title"], r["m"]), ("message", [MINT], None, {"views": 1200}))
        self.assertEqual(tg.parse_views("15M"), 15_000_000)


class Poll(unittest.TestCase):
    def test_sin_vista_previa_se_apaga_y_se_reintenta_a_las_24_h(self):
        f = Fetch({"canal_uno": page("canal_uno", 1)})
        _, st = tg.poll(CONFIG, {}, NOW, fetch=f, sleep=lambda s: None)
        self.assertEqual((st["sources"]["sin_preview"]["preview"], st["sources"]["sin_preview"]["next_check"]),
                         (False, NOW + 24 * 3600))
        f.calls.clear()
        tg.poll(CONFIG, st, NOW + 600, fetch=f, sleep=lambda s: None)
        self.assertEqual(f.calls, ["canal_uno"])                        # no se consulta hasta el recheck
        f.calls.clear()
        tg.poll(CONFIG, st, NOW + 24 * 3600 + 1, fetch=f, sleep=lambda s: None)
        self.assertEqual(f.calls, ["canal_uno", "sin_preview"])

    def test_cursor_solo_lo_nuevo_y_auto_off_del_reparador(self):
        f = Fetch({"canal_uno": page("canal_uno", 10, 11)})
        recs, st = tg.poll(CONFIG, {}, NOW, fetch=f, sleep=lambda s: None)
        self.assertEqual(len(recs), 2)
        self.assertEqual(st["sources"]["canal_uno"]["cursor"], 11)
        f.pages["canal_uno"] = page("canal_uno", 10, 11, 12)
        recs, st = tg.poll(CONFIG, st, NOW + 240, fetch=f, sleep=lambda s: None)
        self.assertEqual([r["id"] for r in recs], ["canal_uno/12"])
        f.calls.clear()
        _, st = tg.poll(CONFIG, st, NOW + 480, fetch=f, sleep=lambda s: None,
                        auto_off={"canal_uno": {"until": NOW + 9999}})
        self.assertNotIn("canal_uno", f.calls)
        self.assertEqual(st["sources"]["canal_uno"]["auto_off_until"], NOW + 9999)


class Instancias(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="tg_"))
        self.addCleanup(shutil.rmtree, self.root, True)

    def test_dos_instancias_no_duplican_en_el_merge_y_el_orquestador_las_combina(self):
        f = Fetch({"canal_uno": page("canal_uno", 1, 2, 3)})
        for inst, t in (("a", NOW), ("b", NOW + 60)):
            tg.run_loop(CONFIG, inst, root=self.root, loop_minutes=0, fetch=f, clock=lambda t=t: t,
                        sleep=lambda s: None)
        base = store.sources_dir(self.root) / "telegram"
        self.assertEqual(sorted(p.name for p in base.glob("*.jsonl") if not p.name.startswith("_")),
                         ["2026-10-03_a.jsonl", "2026-10-03_b.jsonl"])
        merged = store.collect(NOW + 120, root=self.root)
        self.assertEqual(len(merged), 3)                               # 6 escritos, 3 únicos
        state = orch.read_bot_state(store.sources_dir(self.root), "telegram")
        self.assertEqual((state["last_run"], state["instances"]), (NOW + 60, 2))
        self.assertEqual(state["sources"]["canal_uno"]["checked_at"], NOW + 60)

    def test_loop_de_40_min_commitea_cada_3_pasadas_y_audita(self):
        f = Fetch({"canal_uno": page("canal_uno", 1)})
        t = {"now": float(NOW)}

        def sleep(s):
            t["now"] += s
        commits = []
        totals = tg.run_loop(CONFIG, "a", root=self.root, fetch=f, clock=lambda: t["now"], sleep=sleep,
                             commit=lambda paths, msg: commits.append(msg) or True)
        self.assertEqual(totals["polls"], 10)                           # 40 min / 4 min
        self.assertEqual(len(commits), 4)                               # pasadas 3, 6, 9 y la última
        self.assertEqual(totals["items_new"], 1)
        base = store.sources_dir(self.root) / "telegram"
        (line,) = [json.loads(x) for x in (base / "_audit_a.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual((line["bot"], line["items_new"], line["sources"]), ("telegram_a", 1, 11))
        self.assertTrue((base / "_metrics_a.json").exists())
        self.assertTrue((base / "_state_a.json").exists())

    def test_config_real(self):
        cfg = tg.load_config(tg.config_path(SCRIPTS.parents[1]))
        names = [c["name"] for c in cfg["channels"]]
        self.assertEqual(len(names), 15)
        self.assertNotIn("memecoins", names)                            # alias de 'crypto'
        with self.assertRaises(ValueError):
            bad = self.root / "bad.yaml"
            bad.write_text("channels:\n  - {name: uno_dos}\n  - {name: UNO_DOS}\n", encoding="utf-8")
            tg.load_config(bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
