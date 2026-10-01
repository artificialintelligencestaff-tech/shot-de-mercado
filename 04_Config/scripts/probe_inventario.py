#!/usr/bin/env python3
"""
probe_inventario.py — Sonda del inventario del doc 28 (Fase 8, T2), pensada para correr desde Actions.

Lee 04_Config/inventario.json y hace UNA request por servicio con endpoint de prueba (GET, o POST si la API es
GraphQL / JSON-RPC). Registra: estado HTTP, latencia, tamaño, tipo de contenido, encabezados de límite de tasa y si
la respuesta indica que hace falta autenticación o un plan pago (401/402/403 o texto "api key", "subscription"...).
Solo lectura, sin cuentas ni keys, con pausa entre requests. No instala nada.

Salida: 02_Analisis/diagnostics/inventario_probe.json (última corrida completa + historial resumido de 10).
Uso: python 04_Config/scripts/probe_inventario.py [--only id1,id2] [--out RUTA]
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
INVENTORY = ROOT / "04_Config" / "inventario.json"
OUT_FILE = ROOT / "02_Analisis" / "diagnostics" / "inventario_probe.json"
# Solo ASCII: con un User-Agent no ASCII algunos sitios respondían 403 [V, doc 26].
HEADERS = {"User-Agent": "shot-de-mercado-probe/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)",
           "Accept": "application/json, application/xml, text/xml, text/html;q=0.8, */*;q=0.5"}
TIMEOUT_S = 20
PAUSE_S = 1.5
HISTORY_MAX = 10
AUTH_HINTS = ("api key", "apikey", "api-key", "unauthorized", "subscription", "upgrade to", "pro api", "x-api-key",
              "authentication required", "invalid key", "missing key")


def classify(status, body_head):
    """ok (2xx sin pedido de auth) · auth (401/402/403 o texto de key/plan) · blocked (451) · rate_limited (429) ·
    error (resto)."""
    text = (body_head or "").lower()
    if isinstance(status, int) and 200 <= status < 300:
        return "auth" if any(h in text for h in AUTH_HINTS) and len(text) < 400 else "ok"
    if status in (401, 402, 403) or any(h in text for h in AUTH_HINTS):
        return "auth"
    if status == 451:
        return "blocked"
    if status == 429:
        return "rate_limited"
    return "error"


def probe_entry(session, entry):
    url, method = entry["probe"], (entry.get("method") or "GET").upper()
    out = {"id": entry["id"], "name": entry["name"], "category": entry["category"], "url": url, "method": method,
           "api_key_declared": entry.get("api_key")}
    t0 = time.monotonic()
    try:
        if method == "POST":
            r = session.post(url, json=entry.get("body") or {}, headers=HEADERS, timeout=TIMEOUT_S)
        else:
            r = session.get(url, headers=HEADERS, timeout=TIMEOUT_S, stream=False)
    except requests.RequestException as e:
        out.update(status=f"error {type(e).__name__}", latency_ms=int((time.monotonic() - t0) * 1000), result="error")
        return out
    body = r.content[:2000].decode("utf-8", "replace")
    out.update(status=r.status_code, latency_ms=int((time.monotonic() - t0) * 1000), bytes=len(r.content),
               content_type=(r.headers.get("content-type") or "")[:60],
               rate_limit={k: v for k, v in r.headers.items() if "ratelimit" in k.lower() or k.lower() == "retry-after"},
               result=classify(r.status_code, body))
    if out["result"] != "ok":
        out["body_head"] = " ".join(body.split())[:200]
    return out


def run(session=None, only=None, sleep=time.sleep, inventory=None):
    inv = inventory or json.loads(Path(INVENTORY).read_text(encoding="utf-8"))
    entries = [e for e in inv["entries"] if e.get("probe") and (not only or e["id"] in only)]
    session = session or requests.Session()
    results = []
    for i, e in enumerate(entries):
        if i:
            sleep(PAUSE_S)
        results.append(probe_entry(session, e))
    by_result, by_cat = {}, {}
    for r in results:
        by_result[r["result"]] = by_result.get(r["result"], 0) + 1
        c = by_cat.setdefault(r["category"], {"total": 0, "ok": 0})
        c["total"] += 1
        c["ok"] += r["result"] == "ok"
    groups_ok = sorted({g for e in entries for r in results if r["id"] == e["id"] and r["result"] == "ok"
                        for g in e.get("groups") or []})
    return {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "runner": "github-actions" if os.environ.get("GITHUB_ACTIONS") == "true" else "local",
            "github_run_id": os.environ.get("GITHUB_RUN_ID"), "inventory_version": inv.get("version"),
            "summary": {"probed": len(results), "ok": by_result.get("ok", 0), "by_result": by_result,
                        "by_category": by_cat, "groups_with_ok_source": groups_ok,
                        "inventory_total": len(inv["entries"])},
            "results": results}


def save(report, path):
    path = Path(path)
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {}
    history = ((previous.get("history") or []) if isinstance(previous, dict) else [])[-(HISTORY_MAX - 1):]
    history.append({"generated_at": report["generated_at"], "runner": report["runner"],
                    "github_run_id": report["github_run_id"], "ok": report["summary"]["ok"],
                    "probed": report["summary"]["probed"]})
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps({**report, "history": history}, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, path)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Sonda del inventario (doc 28).")
    ap.add_argument("--only", default="", help="ids separados por coma")
    ap.add_argument("--out", default=str(OUT_FILE))
    args = ap.parse_args(argv)
    report = run(only={x for x in args.only.split(",") if x} or None)
    for r in report["results"]:
        print(f"[{r['result']:<12}] {r['id']:<24} {r['status']} · {r.get('latency_ms')} ms")
    s = report["summary"]
    print(f"[RESUMEN] {report['runner']}: OK {s['ok']}/{s['probed']} · {s['by_result']} · grupos con fuente OK: "
          f"{','.join(s['groups_with_ok_source'])}")
    print(f"[OK] {save(report, args.out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
