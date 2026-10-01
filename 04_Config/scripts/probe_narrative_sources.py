#!/usr/bin/env python3
"""
probe_narrative_sources.py — Sonda de las fuentes de menciones del doc 26, pensada para correr desde Actions.

Por cada endpoint: estado HTTP, latencia, tamaño, encabezados de límite de tasa y, sobre todo, si la respuesta se
puede PARSEAR (ítems leídos y antigüedad del más nuevo): una fuente sirve si responde 200 y trae ítems.
Solo GET de lectura a endpoints públicos (RSS, JSON públicos, vista web de canales públicos), sin cuentas ni
cookies, con pausas entre requests. Sin Telethon / Pyrogram (prohibidos).

Salida: 02_Analisis/diagnostics/narrative_sources_probe.json (última corrida completa + historial resumido de 20).
Criterio de la directiva (Fase 4 §4): la Fase 0 del doc 26 se habilita si ≥ 3 familias de fuentes de menciones
funcionan desde Actions.

Uso: python 04_Config/scripts/probe_narrative_sources.py [--out RUTA] [--quick]
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
sys.path.insert(0, str(SCRIPTS))
import lib_repetition as rep  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
OUT_FILE = ROOT / "02_Analisis" / "diagnostics" / "narrative_sources_probe.json"
# Solo ASCII: con un User-Agent no ASCII ("investigación"), 4chan y Decrypt respondían 403 [V, 01/10].
HEADERS = {"User-Agent": "shot-de-mercado-probe/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}
TIMEOUT_S = 20
HISTORY_MAX = 20
MIN_FAMILIES = 3          # criterio de la directiva para habilitar la Fase 0

SUBREDDITS = ["solana", "CryptoCurrency", "CryptoMoonShots", "memecoins", "SatoshiStreetBets"]
# Canales con vista previa pública verificada el 01/10 [V]; otros (solana, coindesk, dexscreener) redirigen.
TELEGRAM_CHANNELS = ["cointelegraph", "WatcherGuru", "whale_alert_io", "pumpfun"]
NEWS_RSS = {"CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
            "Cointelegraph": "https://cointelegraph.com/rss",
            "Decrypt": "https://decrypt.co/feed",
            "The Block": "https://www.theblock.co/rss.xml"}

# familia -> (es fuente de menciones, [(nombre, url, parser, pausa previa en s)])
SOURCES = {
    "reddit_rss": (True, [(f"r/{s}", f"https://www.reddit.com/r/{s}/new/.rss", "feed", 10) for s in SUBREDDITS]),   # Reddit limita el RSS anónimo por IP
    "telegram_web": (True, [(f"t.me/s/{c}", f"https://t.me/s/{c}", "telegram", 5) for c in TELEGRAM_CHANNELS]),
    "4chan_biz": (True, [("/biz/ catalog", "https://a.4cdn.org/biz/catalog.json", "4chan", 2)]),
    "hn_algolia": (True, [("search_by_date crypto",
                           "https://hn.algolia.com/api/v1/search_by_date?query=crypto&tags=story&hitsPerPage=50",
                           "hn", 2)]),
    "news_rss": (True, [(name, url, "feed", 2) for name, url in NEWS_RSS.items()]),
    "gdelt": (True, [("DOC timelinevolraw 24h",
                      "https://api.gdeltproject.org/api/v2/doc/doc?query=solana&mode=timelinevolraw&format=json&timespan=24h",
                      "gdelt", 6)]),
    "coingecko_trending": (False, [("search/trending", "https://api.coingecko.com/api/v3/search/trending",
                                    "coingecko", 2)]),
}


def probe_endpoint(session, name, url, parser, now=None):
    """Una request + parseo. Nunca lanza: los errores quedan en el registro."""
    out = {"name": name, "url": url, "parser": parser}
    t0 = time.monotonic()
    try:
        r = session.get(url, headers=HEADERS, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        out.update(status=f"error {type(e).__name__}", latency_ms=int((time.monotonic() - t0) * 1000), ok=False)
        return out
    out.update(status=r.status_code, latency_ms=int((time.monotonic() - t0) * 1000), bytes=len(r.content),
               content_type=(r.headers.get("content-type") or "")[:60], final_url=r.url if r.url != url else None,
               rate_limit={k: v for k, v in r.headers.items() if "ratelimit" in k.lower() or k.lower() == "retry-after"})
    items = []
    if r.status_code == 200:
        try:
            payload = r.json() if parser in ("4chan", "hn", "coingecko", "gdelt") else r.text
            items = rep.PARSERS[parser](payload, name)
        except Exception as e:   # respuesta 200 que no se puede leer (p. ej., HTML en lugar de JSON)
            out["parse_error"] = f"{type(e).__name__}: {str(e)[:120]}"
    stamps = [i["ts"] for i in items if i.get("ts")]
    now = now or time.time()
    out.update(items=len(items), with_timestamp=len(stamps),
               newest_age_min=round((now - max(stamps)) / 60, 1) if stamps else None,
               oldest_age_min=round((now - min(stamps)) / 60, 1) if stamps else None,
               ok=r.status_code == 200 and len(items) > 0)
    return out


def run_probe(session=None, quick=False, sleep=time.sleep):
    session = session or requests.Session()
    families, first = {}, True
    for family, (is_mentions, endpoints) in SOURCES.items():
        results = []
        for name, url, parser, pause in (endpoints[:1] if quick else endpoints):
            if not first:
                sleep(pause)
            first = False
            results.append(probe_endpoint(session, name, url, parser))
        families[family] = {"mentions_source": is_mentions, "ok": any(e["ok"] for e in results),
                            "endpoints_ok": sum(e["ok"] for e in results), "endpoints": results}
    mention_ok = sorted(f for f, v in families.items() if v["mentions_source"] and v["ok"])
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "runner": "github-actions" if os.environ.get("GITHUB_ACTIONS") == "true" else "local",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "summary": {"mention_families_ok": mention_ok,
                    "mention_families_ok_count": len(mention_ok),
                    "mention_families_total": sum(v["mentions_source"] for v in families.values()),
                    "endpoints_ok": sum(v["endpoints_ok"] for v in families.values()),
                    "endpoints_total": sum(len(v["endpoints"]) for v in families.values()),
                    "phase0_enabled_by_probe": len(mention_ok) >= MIN_FAMILIES,
                    "criterion": f">= {MIN_FAMILIES} familias de fuentes de menciones OK"},
        "families": families,
    }


def save(report, path):
    """Guarda la corrida y un historial resumido (para comparar IP local vs Actions)."""
    path = Path(path)
    previous = {}
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    history = (previous.get("history") or [])[-(HISTORY_MAX - 1):] if isinstance(previous, dict) else []
    history.append({"generated_at": report["generated_at"], "runner": report["runner"],
                    "github_run_id": report["github_run_id"], **report["summary"]})
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps({**report, "history": history}, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, path)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Sonda de fuentes de menciones (doc 26).")
    ap.add_argument("--out", default=str(OUT_FILE))
    ap.add_argument("--quick", action="store_true", help="un endpoint por familia")
    args = ap.parse_args(argv)
    report = run_probe(quick=args.quick)
    for family, v in report["families"].items():
        print(f"[{'OK' if v['ok'] else '--'}] {family}: {v['endpoints_ok']}/{len(v['endpoints'])}")
        for e in v["endpoints"]:
            print(f"      {e['name']}: {e['status']} · {e['latency_ms']} ms · ítems {e.get('items', 0)}"
                  f" · más nuevo hace {e.get('newest_age_min')} min{' · ' + e['parse_error'] if e.get('parse_error') else ''}")
    s = report["summary"]
    print(f"[RESUMEN] {report['runner']}: familias de menciones OK {s['mention_families_ok_count']}/"
          f"{s['mention_families_total']} ({', '.join(s['mention_families_ok']) or 'ninguna'}) · endpoints "
          f"{s['endpoints_ok']}/{s['endpoints_total']} · Fase 0 habilitada por la sonda: {s['phase0_enabled_by_probe']}")
    print(f"[OK] {save(report, args.out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
