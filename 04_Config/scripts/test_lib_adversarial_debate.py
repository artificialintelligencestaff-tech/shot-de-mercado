#!/usr/bin/env python3
"""Tests del debate adversario (patrón #8): lib_adversarial_debate. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_adversarial_debate.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_adversarial_debate as deb  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

T0 = 1791000000                    # 2026-10-03 (semana ISO 40)
WEEK = 7 * 86400
TWO = {"test": "fisher_one_sided", "min_n": 40, "group_field": "sig", "group_a": "si", "group_b": "no",
       "outcome_field": "primary"}


def cell(chain, week, group, hits, total):
    return [{"chain": chain, "t0": T0 + week * WEEK, "sig": group, "primary": "hit" if i < hits else "miss"}
            for i in range(total)]


def grid(spec):
    """spec: {(chain, week): (hits_si, n_si, hits_no, n_no)}"""
    rows = []
    for (chain, week), (ks, ns, kn, nn) in sorted(spec.items()):
        rows += cell(chain, week, "si", ks, ns) + cell(chain, week, "no", kn, nn)
    return rows


STRONG = {(c, w): (7, 10, 3, 10) for c in ("solana", "base") for w in (0, 1)}
FLAT = {(c, w): (4, 10, 4, 10) for c in ("solana", "base") for w in (0, 1)}


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="debate_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        sm.register_hypothesis("H-a1", "la señal sí supera a la señal no", TWO,
                               {"all": [["p_value", "<", 0.10], ["diff_pp", ">=", 10]]},
                               {"all": [["p_value", ">=", 0.10]]}, group="a", root=self.root, now=T0)

    def rules(self, out, role):
        return {a["rule"] for a in out[role]}


class Debate(Base):
    def test_efecto_robusto_queda_sostenido(self):
        out = deb.run_debate("H-a1", {"rows": grid(STRONG), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["verdict"], "sostenida")
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")
        self.assertTrue({"A1_significancia", "A2_efecto", "A4_consistencia", "A5_placebo_nulo",
                         "A7_estabilidad"} <= self.rules(out, "advocate"))
        self.assertFalse(any(a["fatal"] for a in out["challenger"]))
        self.assertGreaterEqual(out["confidence"], 0.8)
        self.assertEqual(out["reasons"][0], "el efecto es estadísticamente significativo")

    def test_submuestra_que_invierte_el_signo_con_significancia_refuta(self):
        spec = {("solana", w): (18, 20, 4, 20) for w in (0, 1)}
        spec.update({("base", w): (1, 10, 6, 10) for w in (0, 1)})       # base: 2/20 contra 12/20
        out = deb.run_debate("H-a1", {"rows": grid(spec), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")       # la prueba sola la aceptaría
        self.assertEqual(out["verdict"], "refutada")
        inv = [a for a in out["challenger"] if a["rule"] == "C4_inversion"]
        self.assertTrue(inv and inv[0]["fatal"])
        self.assertLess(inv[0]["evidence"]["subsamples"]["chain=base"]["p_against"], deb.ALPHA)
        self.assertEqual(out["reasons"], ["una submuestra invierte el signo con significancia"])

    def test_regresion_c4_efecto_real_con_submuestra_ruidosa_no_refuta(self):
        spec = {("solana", w): (18, 20, 4, 20) for w in (0, 1)}
        spec.update({("base", w): (3, 10, 5, 10) for w in (0, 1)})       # base: 6/20 contra 10/20, p en contra 0,17
        out = deb.run_debate("H-a1", {"rows": grid(spec), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["verdict"], "sostenida")                    # antes de D-058: refutada (C4 sin control)
        noise = [a for a in out["challenger"] if a["rule"] == "C4n_inversion_ruido"]
        self.assertTrue(noise and noise[0]["weight"] == 0 and not noise[0]["fatal"])
        self.assertGreaterEqual(noise[0]["evidence"]["subsamples"]["chain=base"]["p_against"], deb.ALPHA)

    def test_placebo_que_rinde_igual_refuta_y_placebo_nulo_no(self):
        rows = grid(STRONG)
        out = deb.run_debate("H-a1", {"rows": rows, "placebo_rows": rows}, self.root)
        self.assertEqual(out["verdict"], "refutada")
        self.assertIn("C5_placebo", {a["rule"] for a in out["challenger"] if a["fatal"]})
        # Regresión C5: placebo ruidoso con la mitad del efecto real (+20 pp contra +40 pp) pero NO significativo.
        # Antes de D-058 bastaba "efecto placebo ≥ la mitad" para refutar.
        placebo = grid({("solana", 0): (3, 5, 2, 5), ("solana", 1): (3, 5, 2, 5)})
        ok = deb.run_debate("H-a1", {"rows": rows, "placebo_rows": placebo}, self.root)
        self.assertFalse(ok["features"]["placebo"]["significant"])
        self.assertEqual(ok["verdict"], "sostenida")
        self.assertNotIn("C5_placebo", self.rules(ok, "challenger"))
        sin_placebo = deb.run_debate("H-a1", {"rows": rows}, self.root)
        self.assertIn("C10_sin_placebo", self.rules(sin_placebo, "challenger"))

    def test_placebo_vs_real_es_exacto(self):
        """El test hipergeométrico coincide con enumerar todas las permutaciones real/placebo por grupo."""
        from itertools import combinations
        real = grid({("solana", 0): (3, 4, 1, 4)})
        plac = grid({("solana", 1): (1, 4, 2, 4)})
        p = deb.placebo_gap_p(TWO, real, plac, seed=0)

        def eff(rows):
            a = [r["primary"] == "hit" for r in rows if r["sig"] == "si"]
            b = [r["primary"] == "hit" for r in rows if r["sig"] == "no"]
            return sum(a) / len(a) - sum(b) / len(b)
        obs = eff(real) - eff(plac)
        pools = {g: [r for r in real + plac if r["sig"] == g] for g in ("si", "no")}
        ge = total = 0
        for ia in combinations(range(8), 4):
            for ib in combinations(range(8), 4):
                r = [pools["si"][i] for i in ia] + [pools["no"][i] for i in ib]
                q = [pools["si"][i] for i in range(8) if i not in ia] + [pools["no"][i] for i in range(8) if i not in ib]
                total += 1
                ge += eff(r) - eff(q) >= obs - 1e-12
        self.assertAlmostEqual(p, round(ge / total, 4), places=4)
        rate = {"test": "rate_vs_baseline", "baseline": 0.3, "outcome_field": "primary"}
        self.assertEqual(deb.placebo_gap_p(rate, real, plac, 0), round(sm.fisher_one_sided(4, 8, 3, 8), 4))

    def test_muestra_insuficiente_no_debate(self):
        out = deb.run_debate("H-a1", {"rows": grid({("solana", 0): (7, 10, 3, 10)})}, self.root)
        self.assertEqual((out["verdict"], out["evaluation"]["verdict"]), ("insuficiente", "pendiente"))
        self.assertEqual([a["rule"] for a in out["challenger"]], ["C1_muestra"])
        with self.assertRaises(KeyError):
            deb.run_debate("H-zz", {"rows": []}, self.root)

    def test_tasa_inestable_en_el_tiempo_y_determinismo(self):
        sm.register_hypothesis("H-r1", "la tasa supera 30 %", {"test": "rate_vs_baseline", "min_n": 20,
                               "baseline": 0.30}, {"all": [["wilson_lo", ">", "$baseline"]]},
                               {"all": [["wilson_hi", "<", "$baseline"]]}, root=self.root, now=T0)
        rows = [{"t0": T0, "primary": "hit"} for _ in range(20)] + \
               [{"t0": T0 + WEEK, "primary": "hit" if i < 2 else "miss"} for i in range(20)]
        out = deb.run_debate("H-r1", {"rows": rows}, self.root)
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")
        self.assertEqual(out["verdict"], "refutada")
        self.assertTrue({"C7_inestable", "C4_inversion"} <= self.rules(out, "challenger"))
        again = deb.run_debate("H-r1", {"rows": rows}, self.root)
        self.assertEqual(json.dumps(out, sort_keys=True), json.dumps(again, sort_keys=True))

    def test_sin_significancia_es_inconclusa_no_refutada(self):
        weak = {(c, w): (5, 10, 4, 10) for c in ("solana", "base") for w in (0, 1)}     # +10 pp, n = 80: p ≈ 0,32
        out = deb.run_debate("H-a1", {"rows": grid(weak), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["verdict"], "inconclusa")                   # falta de potencia ≠ evidencia en contra
        self.assertFalse(any(a["fatal"] for a in out["challenger"]))
        against = {(c, w): (2, 10, 7, 10) for c in ("solana", "base") for w in (0, 1)}  # significativo en contra
        self.assertEqual(deb.run_debate("H-a1", {"rows": grid(against)}, self.root)["verdict"], "refutada")


class Calibracion(unittest.TestCase):
    """D-058: 200 escenarios con efecto real de 20–30 pp y placebo nulo + 200 nulos. Objetivo: refutar < 10 % de
    los efectos reales y aceptar < 10 % de los nulos. Antes del fix, con los mismos escenarios: 34/200 y 67/200
    reales refutados (n = 102 y 42 por grupo)."""

    def check(self, per_cell):
        out = deb.calibrate(200, per_cell=per_cell)
        rates = out["rates"]
        self.assertLess(rates["real_refutada"], 0.10, out)
        self.assertLess(rates["null_aceptada"], 0.10, out)
        self.assertEqual(sum(out["real"][k] for k in ("sostenida", "refutada", "inconclusa", "insuficiente")), 200)
        return rates

    def test_calibracion_n102_por_grupo(self):
        self.assertEqual(self.check(17), {"real_refutada": 0.04, "real_no_sostenida": 0.075, "null_aceptada": 0.07})

    def test_calibracion_n42_por_grupo(self):
        self.assertEqual(self.check(7), {"real_refutada": 0.06, "real_no_sostenida": 0.245, "null_aceptada": 0.055})


if __name__ == "__main__":
    unittest.main(verbosity=2)
