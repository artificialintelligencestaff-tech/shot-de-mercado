#!/usr/bin/env python3
"""
lib_adversarial_debate.py — debate adversario formalizado (patrón #8, doc 36 §1 paso 6 y §"Debate formalizado").

Antes de aceptar que una señal funciona, dos roles discuten sobre LA MISMA evidencia:
  advocate    busca soporte: significancia, tamaño del efecto, n holgado, consistencia por submuestra, placebo nulo,
              permutación, estabilidad temporal.
  challenger  intenta romperla: n insuficiente, p alto, efecto chico, una submuestra que invierte el signo, placebo
              que rinde igual, permutación que no separa, inestabilidad temporal, datos faltantes, dependencia de
              una sola submuestra, ausencia de placebo.
Sin LLM: cada argumento sale de una regla explícita con su peso. Determinista (la permutación usa una semilla
derivada del hash de los datos).

Afirmación que se debate: "el efecto que predice la hipótesis es real".
  fisher_one_sided  → tasa(grupo A) − tasa(grupo B) > 0
  rate_vs_baseline  → tasa − baseline > 0
  median_ci         → mediana > 0
(Para H-0, que es una nula, "sostenida" significa que el efecto informacional es real, es decir, H-0 rechazada con
robustez.)

Veredicto:
  insuficiente  n < min_n (no hay debate posible)
  refutada      algún argumento fatal del challenger (submuestra que invierte el signo, placebo que rinde igual)
                o el challenger pesa más o igual que el advocate
  sostenida     el advocate pesa más, hay significancia y no hay fatales
confianza = peso del lado ganador / peso total (0–1).

Entrada: run_debate(hypothesis_id, evidence_set, root=None)
  evidence_set = {"rows": [...],                       filas como las de evaluate_hypothesis
                  "placebo_rows": [...] (opcional),    mismas filas medidas en fechas desplazadas ±6–24 h
                  "subsample_fields": ["chain", "week"] (opcional; "week" sale del tiempo de cada fila)}
Solo biblioteca estándar.
"""
import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_normalize as norm  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

ALPHA = 0.10
EFFECT_MIN_PP = 10.0          # doc 36 §2: diferencia ≥ 10 pp
EFFECT_TINY_PP = 5.0
SUB_MIN_N = 10                # una submuestra con menos filas resueltas no vota
CONSISTENT_SHARE = 0.75
MISSING_MAX = 0.30
PERMUTATIONS = 500
TIME_FIELDS = ("t0", "ts", "alert_ts", "timestamp")


# ---------------------------------------------------------------------------
# Lectura de la evidencia
# ---------------------------------------------------------------------------

def effect_of(test, result):
    """(efecto en pp o unidades, ¿significativo?, p o None) según la prueba preregistrada."""
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
    return [r for r in rows if r.get(f) in (hit, miss)]


def run_test(pred, rows):
    return sm.TESTS[pred["test"]](rows, pred)


def sub_key(r, field):
    key = week_of(r) if field == "week" else r.get(field)
    return None if key is None else str(key)


def subsamples(pred, rows, fields):
    """Efecto por submuestra. Un campo con una sola submuestra evaluable no prueba nada y no vota."""
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
            eff, _, _ = effect_of(pred["test"], run_test(pred, g))
            if eff is not None:
                votes[f"{field}={key}"] = {"n": len(g), "effect": eff}
        if len(votes) >= 2:
            out.update(votes)
    return out


def permutation_p(pred, rows, observed, seed):
    """Solo para dos grupos: permuta las etiquetas de grupo y cuenta cuántas veces el efecto alcanza al observado."""
    gf = pred.get("group_field", "group")
    labels = [r.get(gf) for r in rows]
    rng = random.Random(seed)
    ge = 0
    for _ in range(PERMUTATIONS):
        rng.shuffle(labels)
        perm = [dict(r, **{gf: lab}) for r, lab in zip(rows, labels)]
        eff, _, _ = effect_of(pred["test"], run_test(pred, perm))
        if eff is not None and eff >= observed:
            ge += 1
    return round((ge + 1) / (PERMUTATIONS + 1), 4)


def halves(pred, rows):
    timed = sorted((r for r in rows if row_time(r)), key=row_time)
    if len(timed) < 2 * SUB_MIN_N:
        return None
    mid = len(timed) // 2
    a, _, _ = effect_of(pred["test"], run_test(pred, timed[:mid]))
    b, _, _ = effect_of(pred["test"], run_test(pred, timed[mid:]))
    return None if a is None or b is None else (a, b)


def features(reg, evidence):
    pred = reg["prediction"]
    rows = [r for r in evidence.get("rows") or [] if isinstance(r, dict)]
    res_rows = resolved_rows(rows, pred)
    result = run_test(pred, rows)
    effect, significant, p = effect_of(pred["test"], result)
    fx = {"test": pred["test"], "n": result.get("n", 0), "min_n": pred.get("min_n", 1), "effect": effect,
          "significant": significant, "p_value": p, "valid": bool(result.get("valid")),
          "missing_share": round(1 - len(res_rows) / len(rows), 4) if rows else 0.0}
    if effect is None:
        return fx, result
    fx["subsamples"] = subsamples(pred, res_rows, evidence.get("subsample_fields") or ["chain", "week"])
    fx["halves"] = halves(pred, res_rows)
    if pred["test"] == "fisher_one_sided":
        fx["permutation_p"] = permutation_p(pred, res_rows, effect, int(sm.sha(res_rows), 16))
    if fx["subsamples"]:                       # dependencia: ¿sin la submuestra más grande sigue el signo?
        big = max(fx["subsamples"].items(), key=lambda kv: kv[1]["n"])[0]
        field, key = big.split("=", 1)
        rest = [r for r in res_rows if sub_key(r, field) != key]
        eff_rest, sig_rest, _ = effect_of(pred["test"], run_test(pred, rest)) if rest else (None, False, None)
        fx["without_largest"] = {"dropped": big, "effect": eff_rest, "significant": sig_rest}
    placebo = [r for r in evidence.get("placebo_rows") or [] if isinstance(r, dict)]
    if placebo:
        pe, ps, pp = effect_of(pred["test"], run_test(pred, placebo))
        fx["placebo"] = {"effect": pe, "significant": ps, "p_value": pp}
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
    if pl and not pl["significant"] and (pl["effect"] or 0) < abs(eff) / 2:
        out.append(arg("advocate", "A5_placebo_nulo", "con fechas desplazadas la señal no rinde", 1, **pl))
    if fx.get("permutation_p") is not None and fx["permutation_p"] < ALPHA:
        out.append(arg("advocate", "A6_permutacion", "permutar las etiquetas no reproduce el efecto", 1,
                       permutation_p=fx["permutation_p"]))
    h = fx.get("halves")
    if h and (h[0] > 0) == (h[1] > 0) == (eff > 0):
        out.append(arg("advocate", "A7_estabilidad", "las dos mitades del periodo tienen el mismo signo", 1,
                       first=h[0], second=h[1]))
    return out


def challenger(fx):
    out = []
    eff = fx["effect"]
    if not fx["significant"]:
        out.append(arg("challenger", "C2_no_significativo", "el efecto no es significativo", 2, p_value=fx["p_value"]))
    if fx["test"] != "median_ci" and abs(eff) < EFFECT_TINY_PP:
        out.append(arg("challenger", "C3_efecto_chico", f"el efecto es menor a {EFFECT_TINY_PP:g} pp", 1, effect=eff))
    if eff <= 0:
        out.append(arg("challenger", "C3b_signo", "el efecto no va en la dirección predicha", 2, effect=eff))
    inverted = {k: s for k, s in (fx.get("subsamples") or {}).items() if eff and (s["effect"] > 0) != (eff > 0)
                and s["effect"] != 0}
    if inverted:
        out.append(arg("challenger", "C4_inversion", "una submuestra invierte el signo", 3, fatal=True,
                       subsamples=inverted))
    pl = fx.get("placebo")
    if pl and (pl["significant"] or (pl["effect"] is not None and eff > 0 and pl["effect"] >= eff / 2)):
        out.append(arg("challenger", "C5_placebo", "con fechas desplazadas la señal rinde parecido", 3, fatal=True,
                       **pl))
    if not pl:
        out.append(arg("challenger", "C10_sin_placebo", "no hay control placebo", 1))
    if fx.get("permutation_p") is not None and fx["permutation_p"] >= ALPHA:
        out.append(arg("challenger", "C6_permutacion", "permutar las etiquetas da efectos parecidos", 1,
                       permutation_p=fx["permutation_p"]))
    h = fx.get("halves")
    if h and (h[0] > 0) != (h[1] > 0):
        out.append(arg("challenger", "C7_inestable", "el signo cambia entre la primera y la segunda mitad", 2,
                       first=h[0], second=h[1]))
    if fx["missing_share"] > MISSING_MAX:
        out.append(arg("challenger", "C8_faltantes", "faltan resultados en más del 30 % de las filas", 1,
                       missing_share=fx["missing_share"]))
    wl = fx.get("without_largest")
    if wl and fx["significant"] and (wl["effect"] is None or wl["effect"] <= 0 or not wl["significant"]):
        out.append(arg("challenger", "C9_dependencia", "sin la submuestra más grande el efecto no se sostiene", 2,
                       **wl))
    return out


def run_debate(hypothesis_id, evidence_set, root=None):
    h = sm.get_hypothesis(hypothesis_id, root)
    if not h:
        raise KeyError(f"{hypothesis_id} no está preregistrada")
    reg = h["registration"]
    ev = evidence_set or {}
    fx, result = features(reg, ev)
    verdict = sm.decide(reg, result)
    base = {"hypothesis_id": hypothesis_id, "hash": reg["hash"], "data_hash": sm.sha(ev.get("rows") or []),
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
    if fatal or wc >= wa or not fx["significant"]:
        verdict, conf = "refutada", (wc / (wa + wc) if wa + wc else 1.0)
        reasons = [x["claim"] for x in (fatal or sorted(cha, key=lambda x: -x["weight"]))]
    else:
        verdict, conf = "sostenida", wa / (wa + wc)
        reasons = [x["claim"] for x in sorted(adv, key=lambda x: -x["weight"])]
    return dict(base, verdict=verdict, confidence=round(conf, 2), weights={"advocate": wa, "challenger": wc},
                advocate=adv, challenger=cha, reasons=reasons)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Debate adversario (patrón #8)")
    ap.add_argument("hypothesis_id")
    ap.add_argument("--evidence", required=True, help='JSON {"rows": [...], "placebo_rows": [...]}')
    a = ap.parse_args(argv)
    ev = json.loads(Path(a.evidence).read_text(encoding="utf-8"))
    print(json.dumps(run_debate(a.hypothesis_id, ev), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
