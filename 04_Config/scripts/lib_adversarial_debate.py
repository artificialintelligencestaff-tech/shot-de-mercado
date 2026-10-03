#!/usr/bin/env python3
"""
lib_adversarial_debate.py — debate adversario formalizado (patrón #8, doc 36 §1 paso 6 y §4.1).

Antes de aceptar que una señal funciona, dos roles discuten sobre LA MISMA evidencia:
  advocate    busca soporte: significancia, tamaño del efecto, n holgado, consistencia por submuestra, placebo que
              el real supera con significancia, estabilidad temporal.
  challenger  intenta romperla: n insuficiente, efecto chico o en contra, una submuestra que invierte el signo CON
              significancia, placebo que rinde con significancia y que el real no supera, inestabilidad temporal
              significativa, datos faltantes, dependencia de una sola submuestra, ausencia de placebo.
Sin LLM: cada argumento sale de una regla explícita con su peso. Determinista: los tests son exactos (Fisher,
hipergeométrica); solo el placebo de medianas usa Monte Carlo, con semilla derivada del hash de los datos.

Control de error (D-058, auditoría Claude1): una regla del challenger solo refuta con un test formal detrás.
  C4  la submuestra invertida debe ser significativa EN CONTRA (Fisher a una cola invertido, α = 0,10); si no lo
      es, se registra como ruido con peso 0.
  C5  placebo vs real con test de permutación exacto (hipergeométrico, estratificado por grupo): refuta solo si el
      placebo es significativo por sí mismo Y el real no lo supera con significancia (p ≥ α).
  A6/C6 (permutación de etiquetas de grupo) eliminadas: con resultados binarios son el mismo test exacto de Fisher
      y contaban dos veces la misma evidencia.
  C7  igual que C4 para la mitad del periodo con el signo cambiado.
  C9  sin la submuestra más grande, el efecto restante tiene que invertirse (no alcanza con perder significancia:
      eso es pérdida de potencia, no evidencia).
Sin significancia en el total y sin fatales, el veredicto es "inconclusa" (doc 36 paso 7: se sigue midiendo), no
"refutada": la falta de potencia no es evidencia en contra.
Calibración por simulación: `calibrate()`; los pesos y cortes son [H] hasta calibrar con datos reales (doc 36 §4.1).

Afirmación que se debate: "el efecto que predice la hipótesis es real".
  fisher_one_sided  → tasa(grupo A) − tasa(grupo B) > 0
  rate_vs_baseline  → tasa − baseline > 0
  median_ci         → mediana > 0
(Para H-0, que es una nula, "sostenida" significa que el efecto informacional es real, es decir, H-0 rechazada con
robustez.)

Veredicto:
  insuficiente  n < min_n (no hay debate posible)
  refutada      algún argumento fatal del challenger, o el challenger pesa más o igual que el advocate
  inconclusa    sin significancia en el total y sin fatales
  sostenida     hay significancia, no hay fatales y el advocate pesa más
confianza = peso del lado ganador / peso total (0–1).

Entrada: run_debate(hypothesis_id, evidence_set, root=None)
  evidence_set = {"rows": [...],                       filas como las de evaluate_hypothesis
                  "placebo_rows": [...] (opcional),    mismas filas medidas en fechas desplazadas ±6–24 h
                  "subsample_fields": ["chain", "week"] (opcional; "week" sale del tiempo de cada fila)}
Solo biblioteca estándar.
"""
import argparse
import json
import math
import random
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_normalize as norm  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

# Pesos y cortes: [H] hasta calibrar con datos reales (doc 36 §4.1). La calibración sintética está en calibrate().
ALPHA = 0.10
EFFECT_MIN_PP = 10.0          # doc 36 §2: diferencia ≥ 10 pp
EFFECT_TINY_PP = 5.0
SUB_MIN_N = 10                # una submuestra con menos filas resueltas no vota
CONSISTENT_SHARE = 0.75
MISSING_MAX = 0.30
PERMUTATIONS = 500              # solo placebo vs real con medianas (Monte Carlo)
TIME_FIELDS = ("t0", "ts", "alert_ts", "timestamp")


# ---------------------------------------------------------------------------
# Lectura de la evidencia
# ---------------------------------------------------------------------------

def effect_of(test, result):
    """(efecto en pp o unidades, ¿significativo a favor?, p o None) según la prueba preregistrada."""
    if not result.get("valid"):
        return None, False, None
    if test == "fisher_one_sided":
        p = result.get("p_value")
        return result.get("diff_pp"), p is not None and p < ALPHA, p
    if test == "rate_vs_baseline":
        return result.get("diff_pp"), result.get("wilson_lo", 0) > result.get("baseline", 1), None
    if test == "median_ci":
        return result.get("median"), (result.get("ci_lo") or 0) > 0, None
    return None, False, None


def against_of(pred, result):
    """(¿significativo EN CONTRA de lo predicho?, p o None): el mismo test con la dirección invertida."""
    if not result.get("valid"):
        return False, None
    if pred["test"] == "fisher_one_sided":
        a, b = result["groups"][pred["group_a"]], result["groups"][pred["group_b"]]
        p = round(sm.fisher_one_sided(b["k_hit"], b["n"], a["k_hit"], a["n"]), 4)
        return p < ALPHA, p
    if pred["test"] == "rate_vs_baseline":
        return result.get("wilson_hi", 1) < result.get("baseline", 0), None
    if pred["test"] == "median_ci":
        return result.get("ci_hi") is not None and result["ci_hi"] < 0, None
    return False, None


def row_time(r):
    for f in TIME_FIELDS:
        t = norm.timestamp(r.get(f)) if r.get(f) is not None else None
        if t:
            return t
    return None


def week_of(r):
    t = row_time(r)
    if not t:
        return None
    y, w, _ = datetime.fromtimestamp(t, timezone.utc).isocalendar()
    return f"{y}-W{w:02d}"


def resolved_rows(rows, pred):
    if pred["test"] == "median_ci":
        f = pred["value_field"]
        return [r for r in rows if isinstance(r.get(f), (int, float)) and not isinstance(r.get(f), bool)]
    f, hit, miss = pred.get("outcome_field", "primary"), pred.get("hit", "hit"), pred.get("miss", "miss")
    res = [r for r in rows if r.get(f) in (hit, miss)]
    if pred["test"] == "fisher_one_sided":
        gf = pred.get("group_field", "group")
        res = [r for r in res if r.get(gf) in (pred["group_a"], pred["group_b"])]
    return res


def run_test(pred, rows):
    return sm.TESTS[pred["test"]](rows, pred)


def judge(pred, rows):
    """Resultado + lectura en ambas direcciones de un subconjunto de filas."""
    res = run_test(pred, rows)
    eff, sig, p = effect_of(pred["test"], res)
    against, p_against = against_of(pred, res)
    return {"n": res.get("n", 0), "effect": eff, "significant": sig, "p_value": p, "against": against,
            "p_against": p_against}


def sub_key(r, field):
    key = week_of(r) if field == "week" else r.get(field)
    return None if key is None else str(key)


def subsamples(pred, rows, fields):
    """Lectura por submuestra. Un campo con una sola submuestra evaluable no prueba nada y no vota."""
    out = {}
    for field in fields:
        groups, votes = {}, {}
        for r in rows:
            key = sub_key(r, field)
            if key is not None:
                groups.setdefault(key, []).append(r)
        for key, g in sorted(groups.items()):
            if len(g) < SUB_MIN_N:
                continue
            j = judge(pred, g)
            if j["effect"] is not None:
                votes[f"{field}={key}"] = {k: j[k] for k in ("n", "effect", "against", "p_against")}
        if len(votes) >= 2:
            out.update(votes)
    return out


# ---------------------------------------------------------------------------
# Placebo vs real: test formal de que el efecto real supera al del placebo (C5 / A5)
# ---------------------------------------------------------------------------
# Es un test de permutación de la pertenencia real/placebo. Con resultados binarios su distribución es exacta
# (hipergeométrica), así que se calcula sin azar. Para medianas se usa Monte Carlo con semilla.
# (La permutación de etiquetas de grupo de la versión anterior, A6/C6, se eliminó: con resultados binarios y
# márgenes fijos ES el test exacto de Fisher, así que duplicaba A1/C2.)

def _hits(pred, rows):
    f, hit = pred.get("outcome_field", "primary"), pred.get("hit", "hit")
    return sum(r.get(f) == hit for r in rows), len(rows)


def _hyper(N, K, n):
    """P(X = x) de una hipergeométrica: x éxitos al sacar n de N con K éxitos."""
    total = math.comb(N, n)
    return {x: math.comb(K, x) * math.comb(N - K, n - x) / total
            for x in range(max(0, n - (N - K)), min(n, K) + 1)}


def placebo_gap_p(pred, rows, placebo, seed):
    """p (una cola) de que efecto(real) − efecto(placebo) sea tan grande como el observado si real y placebo
    fueran intercambiables. En Fisher se permuta dentro de cada grupo (A y B), así cada lado conserva su
    composición."""
    if pred["test"] == "fisher_one_sided":
        gf = pred.get("group_field", "group")
        side = {}
        for name, data in (("r", rows), ("p", placebo)):
            for g in (pred["group_a"], pred["group_b"]):
                side[name, g] = _hits(pred, [r for r in data if r.get(gf) == g])
        (kar, nar), (kbr, nbr) = side["r", pred["group_a"]], side["r", pred["group_b"]]
        (kap, nap), (kbp, nbp) = side["p", pred["group_a"]], side["p", pred["group_b"]]
        if not all((nar, nbr, nap, nbp)):
            return None
        ka, kb = kar + kap, kbr + kbp

        def gap(x, y):                         # x, y: aciertos del lado real en A y en B
            return (x / nar - y / nbr) - ((ka - x) / nap - (kb - y) / nbp)
        observed = gap(kar, kbr)
        pa, pb = _hyper(nar + nap, ka, nar), _hyper(nbr + nbp, kb, nbr)
        p = sum(px * py for x, px in pa.items() for y, py in pb.items() if gap(x, y) >= observed - 1e-12)
        return round(min(1.0, p), 4)
    if pred["test"] == "rate_vs_baseline":
        (kr, nr), (kp, np_) = _hits(pred, rows), _hits(pred, placebo)
        return round(sm.fisher_one_sided(kr, nr, kp, np_), 4) if nr and np_ else None
    f = pred["value_field"]
    real, plac = [r[f] for r in rows], [r[f] for r in placebo]
    if not real or not plac:
        return None
    observed = statistics.median(real) - statistics.median(plac)
    pool, n_r, rng, ge = real + plac, len(real), random.Random(seed), 0
    for _ in range(PERMUTATIONS):
        rng.shuffle(pool)
        if statistics.median(pool[:n_r]) - statistics.median(pool[n_r:]) >= observed - 1e-12:
            ge += 1
    return round((ge + 1) / (PERMUTATIONS + 1), 4)


def halves(pred, rows):
    timed = sorted((r for r in rows if row_time(r)), key=row_time)
    if len(timed) < 2 * SUB_MIN_N:
        return None
    mid = len(timed) // 2
    a, b = judge(pred, timed[:mid]), judge(pred, timed[mid:])
    return None if a["effect"] is None or b["effect"] is None else (a, b)


def features(reg, evidence):
    pred = reg["prediction"]
    rows = [r for r in evidence.get("rows") or [] if isinstance(r, dict)]
    res_rows = resolved_rows(rows, pred)
    result = run_test(pred, rows)
    effect, significant, p = effect_of(pred["test"], result)
    against, p_against = against_of(pred, result)
    fx = {"test": pred["test"], "n": result.get("n", 0), "min_n": pred.get("min_n", 1), "effect": effect,
          "significant": significant, "p_value": p, "against": against, "p_against": p_against,
          "valid": bool(result.get("valid")),
          "missing_share": round(1 - len(res_rows) / len(rows), 4) if rows else 0.0}
    if effect is None:
        return fx, result
    seed = int(sm.sha(res_rows), 16)
    fx["subsamples"] = subsamples(pred, res_rows, evidence.get("subsample_fields") or ["chain", "week"])
    h = halves(pred, res_rows)
    fx["halves"] = [{k: x[k] for k in ("n", "effect", "against", "p_against")} for x in h] if h else None
    if fx["subsamples"]:                       # dependencia: ¿sin la submuestra más grande sigue el signo?
        big = max(fx["subsamples"].items(), key=lambda kv: kv[1]["n"])[0]
        field, key = big.split("=", 1)
        rest = [r for r in res_rows if sub_key(r, field) != key]
        j = judge(pred, rest) if rest else {"effect": None, "significant": False}
        fx["without_largest"] = {"dropped": big, "effect": j["effect"], "significant": j["significant"]}
    placebo = resolved_rows([r for r in evidence.get("placebo_rows") or [] if isinstance(r, dict)], pred)
    if placebo:
        jp = judge(pred, placebo)
        fx["placebo"] = {"effect": jp["effect"], "significant": jp["significant"], "p_value": jp["p_value"],
                         "gap_p": placebo_gap_p(pred, res_rows, placebo, seed + 1)}
    return fx, result


# ---------------------------------------------------------------------------
# Roles
# ---------------------------------------------------------------------------

def arg(role, rule, claim, weight, fatal=False, **evidence):
    return {"role": role, "rule": rule, "claim": claim, "weight": weight, "fatal": fatal, "evidence": evidence}


def advocate(fx):
    out = []
    eff = fx["effect"]
    if fx["significant"]:
        out.append(arg("advocate", "A1_significancia", "el efecto es estadísticamente significativo", 2,
                       p_value=fx["p_value"]))
    if fx["test"] != "median_ci" and eff >= EFFECT_MIN_PP:
        out.append(arg("advocate", "A2_efecto", f"el efecto supera {EFFECT_MIN_PP:g} pp", 1, effect=eff))
    if fx["n"] >= 2 * fx["min_n"]:
        out.append(arg("advocate", "A3_muestra", "la muestra duplica el mínimo preregistrado", 1, n=fx["n"]))
    subs = fx.get("subsamples") or {}
    if len(subs) >= 2:
        same = sum((s["effect"] > 0) == (eff > 0) for s in subs.values())
        if same / len(subs) >= CONSISTENT_SHARE:
            out.append(arg("advocate", "A4_consistencia", "el signo se repite en las submuestras", 1,
                           same=same, total=len(subs)))
    pl = fx.get("placebo")
    if pl and not pl["significant"] and pl["gap_p"] is not None and pl["gap_p"] < ALPHA:
        out.append(arg("advocate", "A5_placebo_nulo", "el placebo no rinde y el real lo supera con significancia",
                       1, **pl))
    h = fx.get("halves")
    if h and (h[0]["effect"] > 0) == (h[1]["effect"] > 0) == (eff > 0):
        out.append(arg("advocate", "A7_estabilidad", "las dos mitades del periodo tienen el mismo signo", 1,
                       first=h[0]["effect"], second=h[1]["effect"]))
    return out


def challenger(fx):
    out = []
    eff = fx["effect"]
    if not fx["significant"]:
        out.append(arg("challenger", "C2_no_significativo", "el efecto no es significativo", 2, p_value=fx["p_value"]))
    if fx["test"] != "median_ci" and abs(eff) < EFFECT_TINY_PP:
        out.append(arg("challenger", "C3_efecto_chico", f"el efecto es menor a {EFFECT_TINY_PP:g} pp", 1, effect=eff))
    if eff <= 0:
        if fx["against"]:
            out.append(arg("challenger", "C3s_en_contra", "el efecto va significativamente en contra de lo predicho",
                           3, fatal=True, effect=eff, p_against=fx["p_against"]))
        else:
            out.append(arg("challenger", "C3b_signo", "el efecto no va en la dirección predicha", 2, effect=eff))
    inverted = {k: s for k, s in (fx.get("subsamples") or {}).items()
                if eff and s["effect"] != 0 and (s["effect"] > 0) != (eff > 0)}
    strong = {k: s for k, s in inverted.items() if s["against"]}
    if strong:
        out.append(arg("challenger", "C4_inversion", "una submuestra invierte el signo con significancia", 3,
                       fatal=True, subsamples=strong))
    elif inverted:
        out.append(arg("challenger", "C4n_inversion_ruido", "una submuestra invierte el signo sin significancia "
                       "(ruido)", 0, subsamples=inverted))
    pl = fx.get("placebo")
    if pl:
        real_beats = pl["gap_p"] is not None and pl["gap_p"] < ALPHA
        if pl["significant"] and not real_beats:
            out.append(arg("challenger", "C5_placebo", "el placebo rinde con significancia y el real no lo supera",
                           3, fatal=True, **pl))
        elif pl["significant"] or not real_beats:
            out.append(arg("challenger", "C5n_placebo_cercano", "el real no se separa con claridad del placebo", 1,
                           **pl))
    else:
        out.append(arg("challenger", "C10_sin_placebo", "no hay control placebo", 1))
    h = fx.get("halves")
    if h and eff:
        flipped = [x for x in h if x["effect"] != 0 and (x["effect"] > 0) != (eff > 0)]
        if any(x["against"] for x in flipped):
            out.append(arg("challenger", "C7_inestable", "una mitad del periodo va en contra con significancia", 2,
                           first=h[0]["effect"], second=h[1]["effect"]))
    if fx["missing_share"] > MISSING_MAX:
        out.append(arg("challenger", "C8_faltantes", "faltan resultados en más del 30 % de las filas", 1,
                       missing_share=fx["missing_share"]))
    wl = fx.get("without_largest")
    if wl and fx["significant"] and (wl["effect"] is None or wl["effect"] <= 0):
        out.append(arg("challenger", "C9_dependencia", "sin la submuestra más grande el efecto desaparece", 2, **wl))
    return out


def debate(reg, evidence_set, hypothesis_id=None):
    """Debate sobre una registración ya cargada (run_debate la busca en el registro; calibrate la arma)."""
    ev = evidence_set or {}
    fx, result = features(reg, ev)
    verdict = sm.decide(reg, result)
    base = {"hypothesis_id": hypothesis_id or reg.get("id"), "hash": reg.get("hash"),
            "data_hash": sm.sha(ev.get("rows") or []),
            "evaluation": {"verdict": verdict, "label": (reg.get("labels") or {}).get(verdict, verdict)},
            "features": fx}
    if fx["n"] < fx["min_n"] or fx["effect"] is None:
        a = [arg("challenger", "C1_muestra", "n menor al mínimo preregistrado: no hay debate", 3, fatal=True,
                 n=fx["n"], min_n=fx["min_n"])]
        return dict(base, verdict="insuficiente", confidence=1.0, advocate=[], challenger=a,
                    reasons=[a[0]["claim"]])
    adv, cha = advocate(fx), challenger(fx)
    wa, wc = sum(x["weight"] for x in adv), sum(x["weight"] for x in cha)
    fatal = [x for x in cha if x["fatal"]]
    by_weight = sorted((x for x in cha if x["weight"] > 0), key=lambda x: -x["weight"])
    if fatal:
        verdict, conf, reasons = "refutada", wc / (wa + wc), [x["claim"] for x in fatal]
    elif not fx["significant"]:
        verdict, conf, reasons = "inconclusa", wc / (wa + wc) if wa + wc else 1.0, [x["claim"] for x in by_weight]
    elif wc >= wa:
        verdict, conf, reasons = "refutada", wc / (wa + wc), [x["claim"] for x in by_weight]
    else:
        verdict, conf = "sostenida", wa / (wa + wc)
        reasons = [x["claim"] for x in sorted(adv, key=lambda x: -x["weight"])]
    return dict(base, verdict=verdict, confidence=round(conf, 2), weights={"advocate": wa, "challenger": wc},
                advocate=adv, challenger=cha, reasons=reasons)


def run_debate(hypothesis_id, evidence_set, root=None):
    h = sm.get_hypothesis(hypothesis_id, root)
    if not h:
        raise KeyError(f"{hypothesis_id} no está preregistrada")
    return debate(h["registration"], evidence_set, hypothesis_id)


# ---------------------------------------------------------------------------
# Calibración por simulación (D-058)
# ---------------------------------------------------------------------------

SIM_PRED = {"test": "fisher_one_sided", "min_n": 40, "group_field": "sig", "group_a": "si", "group_b": "no",
            "outcome_field": "primary", "hit": "hit", "miss": "miss"}
SIM_T0, SIM_WEEK = 1791000000, 7 * 86400


def simulate_rows(rng, p_a, p_b, per_cell, chains=3, weeks=2):
    """Filas sintéticas: chains × semanas × {si, no}, `per_cell` filas por celda y grupo."""
    rows = []
    for c in range(chains):
        for w in range(weeks):
            for group, p in (("si", p_a), ("no", p_b)):
                for i in range(per_cell):
                    rows.append({"chain": f"chain{c}", "t0": SIM_T0 + w * SIM_WEEK + i * 60, "sig": group,
                                 "primary": "hit" if rng.random() < p else "miss"})
    return rows


def calibrate(n_sims=200, effect=(0.20, 0.30), base=(0.25, 0.40), per_cell=17, chains=3, weeks=2, seed=20261003):
    """Corre el debate sobre n_sims escenarios con efecto real (p_a = p_b + U(effect)) y n_sims nulos (p_a = p_b),
    los dos con placebo nulo. Devuelve conteos y tasas: refutación de reales y aceptación de nulos."""
    reg = {"id": "H-sim", "hash": "sim", "prediction": dict(SIM_PRED),
           "acceptance": {"all": [["p_value", "<", ALPHA]]}, "rejection": {"all": [["p_value", ">=", ALPHA]]}}
    rng = random.Random(seed)
    out = {"params": {"n_sims": n_sims, "effect": list(effect), "base": list(base), "per_cell": per_cell,
                      "chains": chains, "weeks": weeks, "n_per_group": per_cell * chains * weeks, "seed": seed}}
    for kind in ("real", "null"):
        counts = {"sostenida": 0, "refutada": 0, "inconclusa": 0, "insuficiente": 0}
        causes = {}
        for _ in range(n_sims):
            p_b = rng.uniform(*base)
            p_a = p_b + (rng.uniform(*effect) if kind == "real" else 0.0)
            ev = {"rows": simulate_rows(rng, p_a, p_b, per_cell, chains, weeks),
                  "placebo_rows": simulate_rows(rng, p_b, p_b, per_cell, chains, weeks)}
            d = debate(reg, ev)
            counts[d["verdict"]] += 1
            if d["verdict"] == "refutada":
                for a in d["challenger"]:
                    if a["fatal"] or a["weight"] >= 2:
                        causes[a["rule"]] = causes.get(a["rule"], 0) + 1
        out[kind] = dict(counts, causes_refutada=causes)
    out["rates"] = {"real_refutada": round(out["real"]["refutada"] / n_sims, 4),
                    "real_no_sostenida": round(1 - out["real"]["sostenida"] / n_sims, 4),
                    "null_aceptada": round(out["null"]["sostenida"] / n_sims, 4)}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Debate adversario (patrón #8)")
    ap.add_argument("hypothesis_id", nargs="?")
    ap.add_argument("--evidence", help='JSON {"rows": [...], "placebo_rows": [...]}')
    ap.add_argument("--calibrate", action="store_true", help="simulación de calibración (D-058)")
    ap.add_argument("--per-cell", type=int, default=17)
    ap.add_argument("--sims", type=int, default=200)
    a = ap.parse_args(argv)
    if a.calibrate:
        print(json.dumps(calibrate(a.sims, per_cell=a.per_cell), ensure_ascii=False, indent=1))
        return 0
    if not (a.hypothesis_id and a.evidence):
        ap.error("hypothesis_id y --evidence, o --calibrate")
    ev = json.loads(Path(a.evidence).read_text(encoding="utf-8"))
    print(json.dumps(run_debate(a.hypothesis_id, ev), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
