#!/usr/bin/env python3
"""
lib_scientific_method.py — método científico automatizado (patrón #2, doc 36 §1).

Una hipótesis se preregistra ANTES de ver resultados y no se edita: una variante es un id nuevo. Se evalúa con una
prueba explícita (sin IA) y reglas de aceptación / rechazo legibles por máquina.

Registro append-only: 02_Analisis/hypotheses/_registry.jsonl. Una línea por evento:
  {"v":1, "event":"register", "id", "ts", "statement", "prediction", "acceptance", "rejection", "group", "labels",
   "source", "registered_at", "hash"}
  {"v":1, "event":"evaluate", "id", "ts", "hash", "data_hash", "result", "verdict", "label"}

prediction = {"test": <nombre en TESTS>, "min_n": int, ...parámetros de la prueba}
acceptance / rejection = {"all"|"any": [[campo, op, valor], ...]} sobre el resultado de la prueba.
  op ∈ < <= > >= == !=; un valor "$campo" compara contra otro campo del resultado.
Veredicto: pendiente (n < min_n o prueba no válida) · aceptada · rechazada · inconclusa (ninguna regla se cumple).
`labels` traduce el veredicto al vocabulario propio de la hipótesis (H-0: "H-0 rechazada" / "H-0 no rechazada").

La H-0 (doc 32 §6, early_review.evaluate_h0) se migra como referencia con `migrate_h0`: mismos parámetros, misma
prueba, mismo veredicto. early_review.py sigue siendo el evaluador de producción de la H-0.
Cada evaluación persistida deja además un episodio `hipotesis_evaluada` (patrón #12, lib_episodic_memory).
Solo biblioteca estándar.
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_episodic_memory as episodes  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
REGISTRY_REL = "02_Analisis/hypotheses/_registry.jsonl"
SCHEMA = 1
ID_RE = re.compile(r"^H-[A-Za-z0-9_.-]{1,40}$")
VERDICTS = ("pendiente", "aceptada", "rechazada", "inconclusa")
OPS = {"<": lambda a, b: a < b, "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, ">=": lambda a, b: a >= b,
       "==": lambda a, b: a == b, "!=": lambda a, b: a != b}
Z90 = 1.645


def registry_path(root=None):
    return Path(root or ROOT) / REGISTRY_REL


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()[:16]


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# Estadística (misma fórmula que early_review y calibrate_threshold_v72)
# ---------------------------------------------------------------------------

def fisher_one_sided(k1, n1, k2, n2):
    """P(X >= k1) con X hipergeométrica: ¿la tasa del grupo 1 supera a la del 2?"""
    K, N = k1 + k2, n1 + n2
    total = math.comb(N, K)
    return sum(math.comb(n1, x) * math.comb(n2, K - x) for x in range(k1, min(n1, K) + 1)) / total if total else 1.0


def wilson(k, n, z=Z90):
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def median_ci(values, conf=0.90):
    """Mediana con IC por estadísticos de orden (binomial n, 1/2): sin supuestos de distribución ni azar."""
    xs = sorted(values)
    n = len(xs)
    if not n:
        return None, None
    med = xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2
    tail = (1 - conf) / 2
    cdf, j = 0.0, 0
    for i in range(n + 1):                       # mayor j con P(B <= j-1) <= tail
        cdf_next = cdf + math.comb(n, i) / 2 ** n
        if cdf_next > tail:
            j = i
            break
        cdf = cdf_next
    if j < 1:
        return med, None
    return med, [xs[j - 1], xs[n - j]]


# ---------------------------------------------------------------------------
# Pruebas: cada una recibe (filas, parámetros) y devuelve el resultado con "n" y "valid"
# ---------------------------------------------------------------------------

def _resolved(rows, p):
    field, hit, miss = p.get("outcome_field", "primary"), p.get("hit", "hit"), p.get("miss", "miss")
    return [r for r in rows if isinstance(r, dict) and r.get(field) in (hit, miss)], field, hit


def run_fisher_one_sided(rows, p):
    """Grupo A vs grupo B en tasa de acierto. params: group_field, group_a, group_b, outcome_field, hit, miss."""
    res, field, hit = _resolved(rows, p)
    gf = p.get("group_field", "group")
    groups = {}
    for name in (p["group_a"], p["group_b"]):
        g = [r for r in res if r.get(gf) == name]
        k = sum(r[field] == hit for r in g)
        groups[name] = {"n": len(g), "k_hit": k, "rate": round(k / len(g), 4) if g else None}
    a, b = groups[p["group_a"]], groups[p["group_b"]]
    out = {"n": a["n"] + b["n"], "groups": groups, "valid": bool(a["n"] and b["n"])}
    if out["valid"]:
        out["p_value"] = round(fisher_one_sided(a["k_hit"], a["n"], b["k_hit"], b["n"]), 4)
        out["diff_pp"] = round(100 * (a["rate"] - b["rate"]), 2)
    return out


def run_rate_vs_baseline(rows, p):
    """Tasa de acierto contra una tasa base fija. params: baseline, outcome_field, hit, miss."""
    res, field, hit = _resolved(rows, p)
    k = sum(r[field] == hit for r in res)
    out = {"n": len(res), "k_hit": k, "baseline": p["baseline"], "valid": bool(res)}
    if res:
        lo, hi = wilson(k, len(res))
        out.update(rate=round(k / len(res), 4), wilson_lo=lo, wilson_hi=hi,
                   diff_pp=round(100 * (k / len(res) - p["baseline"]), 2))
    return out


def run_median_ci(rows, p):
    """Mediana de un valor numérico con IC90. params: value_field."""
    vals = [r[p["value_field"]] for r in rows if isinstance(r, dict)
            and isinstance(r.get(p["value_field"]), (int, float)) and not isinstance(r.get(p["value_field"]), bool)]
    med, ci = median_ci(vals)
    out = {"n": len(vals), "valid": ci is not None}
    if med is not None:
        out["median"] = round(med, 6)
    if ci:
        out.update(ci_lo=round(ci[0], 6), ci_hi=round(ci[1], 6))
    return out


TESTS = {"fisher_one_sided": run_fisher_one_sided, "rate_vs_baseline": run_rate_vs_baseline,
         "median_ci": run_median_ci}


# ---------------------------------------------------------------------------
# Reglas de decisión
# ---------------------------------------------------------------------------

def check_rules(spec):
    if not isinstance(spec, dict) or len(spec) != 1 or next(iter(spec)) not in ("all", "any"):
        raise ValueError("regla: {'all'|'any': [[campo, op, valor], ...]}")
    conds = next(iter(spec.values()))
    if not conds or not all(isinstance(c, (list, tuple)) and len(c) == 3 and c[1] in OPS for c in conds):
        raise ValueError(f"condiciones inválidas: {conds!r}")


def rule_holds(spec, result):
    def one(cond):
        field, op, value = cond
        left = result.get(field)
        right = result.get(value[1:]) if isinstance(value, str) and value.startswith("$") else value
        if left is None or right is None:
            return False
        try:
            return OPS[op](left, right)
        except TypeError:
            return False
    mode, conds = next(iter(spec.items()))
    return all(map(one, conds)) if mode == "all" else any(map(one, conds))


def decide(reg, result):
    if result.get("n", 0) < reg["prediction"].get("min_n", 1) or not result.get("valid"):
        return "pendiente"
    if rule_holds(reg["acceptance"], result):
        return "aceptada"
    if rule_holds(reg["rejection"], result):
        return "rechazada"
    return "inconclusa"


# ---------------------------------------------------------------------------
# Registro append-only
# ---------------------------------------------------------------------------

def read_registry(root=None):
    out = []
    try:
        lines = registry_path(root).read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for line in lines:
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if isinstance(r, dict) and r.get("id"):
            out.append(r)
    return out


def load_registry(root=None):
    """{id: {"registration": línea register, "evaluations": [líneas evaluate]}}; la primera registración manda."""
    hyps = {}
    for r in read_registry(root):
        h = hyps.setdefault(r["id"], {"registration": None, "evaluations": []})
        if r.get("event") == "register" and h["registration"] is None:
            h["registration"] = r
        elif r.get("event") == "evaluate":
            h["evaluations"].append(r)
    return {k: v for k, v in hyps.items() if v["registration"]}


def get_hypothesis(hyp_id, root=None):
    return load_registry(root).get(hyp_id)


def append_line(line, root=None):
    path = registry_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(line, ensure_ascii=False, sort_keys=True) + "\n")


def register_hypothesis(id, statement, prediction, acceptance, rejection, group=None, labels=None, source=None,
                        registered_at=None, root=None, now=None):
    """Preregistra. Mismo id y mismo contenido → devuelve la existente sin escribir. Mismo id con contenido distinto
    → ValueError (el preregistro es inmutable: una variante es una hipótesis nueva)."""
    if not ID_RE.match(str(id)):
        raise ValueError(f"id inválido {id!r}: se espera H-<grupo><n> (p. ej. H-0, H-a1)")
    if not str(statement).strip():
        raise ValueError("statement vacío")
    if not isinstance(prediction, dict) or prediction.get("test") not in TESTS:
        raise ValueError(f"prediction.test debe ser uno de {sorted(TESTS)}")
    check_rules(acceptance)
    check_rules(rejection)
    body = {"statement": str(statement).strip(), "prediction": prediction, "acceptance": acceptance,
            "rejection": rejection, "group": group, "labels": labels or {}}
    digest = sha(body)
    prev = get_hypothesis(id, root)
    if prev:
        if prev["registration"]["hash"] != digest:
            raise ValueError(f"{id} ya está preregistrada con otro contenido: registrar la variante con un id nuevo")
        return prev["registration"]
    now = int(now if now is not None else time.time())
    line = dict(body, v=SCHEMA, event="register", id=id, ts=now, hash=digest, source=source,
                registered_at=registered_at or iso(now))
    append_line(line, root)
    return line


def evaluate_hypothesis(id, data, root=None, now=None, persist=True):
    """Corre la prueba preregistrada sobre `data` (lista de filas) y decide. Devuelve
    {id, result, verdict, label, data_hash, ts}. Con persist=True agrega la evaluación al registro."""
    h = get_hypothesis(id, root)
    if not h:
        raise KeyError(f"{id} no está preregistrada")
    reg = h["registration"]
    rows = list(data or [])
    result = TESTS[reg["prediction"]["test"]](rows, reg["prediction"])
    verdict = decide(reg, result)
    now = int(now if now is not None else time.time())
    out = {"v": SCHEMA, "event": "evaluate", "id": id, "ts": now, "hash": reg["hash"], "data_hash": sha(rows),
           "result": result, "verdict": verdict, "label": (reg.get("labels") or {}).get(verdict, verdict)}
    if persist:
        append_line(out, root)
        episodes.write_episodes([episodes.hypothesis_episode(out, reg)], root, "method")
    return out


# ---------------------------------------------------------------------------
# H-0 (doc 32 §6) migrada como referencia
# ---------------------------------------------------------------------------

H0 = {
    "id": "H-0",
    "statement": "H-0: info_score >= 20 no supera a info_score < 20 en tasa primaria (tokens < 60 min)",
    "prediction": {"test": "fisher_one_sided", "min_n": 40, "group_field": "h0_group", "group_a": "info_ge20",
                   "group_b": "info_lt20", "outcome_field": "primary", "hit": "hit", "miss": "miss",
                   "alpha": 0.10, "population": "alertas del scorer joven (scorer = young), grupo fijado al emitir",
                   "event": "+20% antes de -30% en 48 h desde el precio de la alerta (velas 15 min GeckoTerminal)"},
    "acceptance": {"all": [["p_value", ">=", 0.10]]},
    "rejection": {"all": [["p_value", "<", 0.10]]},
    "group": "a",
    "labels": {"aceptada": "H-0 no rechazada", "rechazada": "H-0 rechazada", "pendiente": "pendiente"},
    "source": "doc 32 §6 (D-014-R-5); evaluador de producción: early_review.evaluate_h0",
    "registered_at": "2026-10-02",
}


def migrate_h0(root=None, now=None):
    return register_hypothesis(root=root, now=now, **H0)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Registro de hipótesis (patrón #2)")
    ap.add_argument("--migrate-h0", action="store_true", help="preregistra la H-0 como referencia (idempotente)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--evaluate", metavar="ID")
    ap.add_argument("--data", help="JSON (lista) o JSONL con las filas a evaluar")
    ap.add_argument("--dry-run", action="store_true", help="no escribe la evaluación")
    a = ap.parse_args(argv)
    if a.migrate_h0:
        print(json.dumps(migrate_h0(), ensure_ascii=False))
    if a.list:
        for hid, h in sorted(load_registry().items()):
            last = h["evaluations"][-1] if h["evaluations"] else {}
            print(f"{hid}\t{h['registration']['registered_at']}\t{last.get('label', 'sin evaluar')}")
    if a.evaluate:
        text = Path(a.data).read_text(encoding="utf-8") if a.data else "[]"
        try:
            rows = json.loads(text)
        except ValueError:
            rows = [json.loads(x) for x in text.splitlines() if x.strip()]
        print(json.dumps(evaluate_hypothesis(a.evaluate, rows, persist=not a.dry_run), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
