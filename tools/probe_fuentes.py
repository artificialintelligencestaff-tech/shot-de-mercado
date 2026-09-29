#!/usr/bin/env python3
"""Sonda de alcanzabilidad (solo lectura) de fuentes gratuitas candidatas — Proyecto Shot de Mercado.

Verifica DESDE EL RUNNER (IP de datacenter) qué fuentes responden, con qué latencia, si exponen
los campos esperados y si hay bloqueo de Cloudflare. No usa API keys, no envía datos del proyecto,
no escribe en ninguna API y no depende de paquetes externos (solo biblioteca estándar).

Uso:
    python3 tools/probe_fuentes.py [--sample-mint MINT] [--out probe_report.json]
                                   [--timeout 15] [--gap 2.5] [--only SUBCADENA ...]

Variables de entorno opcionales:
    PROBE_SAMPLE_MINT    mint (base58) para RugCheck/GoPlus/Trench; por defecto BONK.
    GITHUB_STEP_SUMMARY  si existe (GitHub Actions), agrega la tabla Markdown al resumen del job.

Código de salida: 0 si la sonda termina (es un reporte, no un test); 2 si hay error de uso o escritura.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import http.client
import json
import os
import re
import secrets
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

USER_AGENT = (
    "shot-de-mercado-probe/1.0 "
    "(+https://github.com/artificialintelligencestaff-tech/shot-de-mercado)"
)
SOL_MINT = "So11111111111111111111111111111111111111112"
DEFAULT_SAMPLE_MINT = "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"  # BONK
BASE58_MINT = re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}")
MAX_BODY_BYTES = 2_000_000
SSE_WAIT_SECONDS = 12.0
WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
INTERESTING_HEADERS = ("ratelimit", "retry-after", "cf-ray", "server", "x-cache")
NETWORK_ERRORS = (OSError, http.client.HTTPException)

Check = Callable[[bytes], tuple[bool, str]]


@dataclass(frozen=True)
class Probe:
    name: str
    problem: str
    kind: str  # "http" | "sse" | "ws"
    url: str
    check: Check | None = None


@dataclass
class Result:
    name: str
    problem: str
    kind: str
    url: str
    ok: bool = False
    status: int | None = None
    latency_ms: int | None = None
    body_bytes: int = 0
    detail: str = ""
    headers: dict[str, str] = field(default_factory=dict)


def json_path(*path: str) -> Check:
    """Valida JSON y, si se indica, un camino de claves (en listas desciende por el primer elemento)."""

    def _check(body: bytes) -> tuple[bool, str]:
        try:
            node = json.loads(body)
        except ValueError:
            return False, "respuesta no es JSON"
        walked: list[str] = []
        for key in path:
            if isinstance(node, list):
                if not node:
                    return False, f"lista vacía en '{'.'.join(walked) or 'raíz'}'"
                node = node[0]
            if not isinstance(node, dict) or key not in node:
                return False, f"falta el campo '{'.'.join([*walked, key])}'"
            node = node[key]
            walked.append(key)
        return True, (f"campo '{'.'.join(path)}' presente" if path else "JSON válido")

    return _check


def text_contains(marker: str) -> Check:
    def _check(body: bytes) -> tuple[bool, str]:
        found = marker.encode() in body
        return found, (f"contiene '{marker}'" if found else f"no contiene '{marker}'")

    return _check


def headers_of_interest(headers: object) -> dict[str, str]:
    items = getattr(headers, "items", None)
    if items is None:
        return {}
    return {k.lower(): v for k, v in items() if any(t in k.lower() for t in INTERESTING_HEADERS)}


def is_cloudflare_block(status: int | None, body: bytes) -> bool:
    if status not in (403, 429, 503):
        return False
    head = body[:20_000].lower()
    return any(m in head for m in (b"cf-chl", b"just a moment", b"attention required"))


def elapsed_ms(start: float) -> int:
    return int((time.monotonic() - start) * 1000)


def run_http(probe: Probe, timeout: float) -> Result:
    res = Result(probe.name, probe.problem, probe.kind, probe.url)
    req = urllib.request.Request(
        probe.url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, application/rss+xml, text/html;q=0.8, */*;q=0.5",
        },
    )
    start = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(MAX_BODY_BYTES)
            res.status = resp.status
            res.headers = headers_of_interest(resp.headers)
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(MAX_BODY_BYTES)
        except NETWORK_ERRORS:
            body = b""
        res.status = exc.code
        res.headers = headers_of_interest(exc.headers)
    except NETWORK_ERRORS as exc:
        res.latency_ms = elapsed_ms(start)
        res.detail = f"error de red: {getattr(exc, 'reason', exc)}"
        return res
    res.latency_ms = elapsed_ms(start)
    res.body_bytes = len(body)
    if is_cloudflare_block(res.status, body):
        res.detail = "bloqueo/desafío de Cloudflare (probable filtro de IP de datacenter)"
        return res
    if res.status != 200:
        snippet = body[:160].decode("utf-8", "replace").strip()
        res.detail = f"HTTP {res.status}: {snippet}"
        return res
    res.ok, res.detail = probe.check(body) if probe.check else (True, "HTTP 200")
    return res


def run_sse(probe: Probe, timeout: float) -> Result:
    res = Result(probe.name, probe.problem, probe.kind, probe.url)
    req = urllib.request.Request(
        probe.url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/event-stream", "Cache-Control": "no-cache"},
    )
    start = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            res.status = resp.status
            res.headers = headers_of_interest(resp.headers)
            while time.monotonic() - start < SSE_WAIT_SECONDS:
                line = resp.readline()
                if not line:
                    break
                res.body_bytes += len(line)
                if line.startswith(b"data:"):
                    res.latency_ms = elapsed_ms(start)
                    res.ok = True
                    res.detail = "primer evento: " + line[:120].decode("utf-8", "replace").strip()
                    return res
            res.detail = f"sin eventos 'data:' en {SSE_WAIT_SECONDS:.0f}s"
    except urllib.error.HTTPError as exc:
        res.status = exc.code
        res.detail = f"HTTP {exc.code} al abrir el stream"
    except NETWORK_ERRORS as exc:
        res.detail = f"error de red/timeout: {getattr(exc, 'reason', exc)}"
    res.latency_ms = elapsed_ms(start)
    return res


def run_ws_handshake(probe: Probe, timeout: float) -> Result:
    """Solo verifica el handshake (101 + Sec-WebSocket-Accept correcto); no se suscribe a nada."""
    res = Result(probe.name, probe.problem, probe.kind, probe.url)
    parsed = urllib.parse.urlsplit(probe.url)
    if parsed.scheme != "wss" or not parsed.hostname:
        res.detail = "URL WebSocket inválida (se espera wss://)"
        return res
    path = (parsed.path or "/") + (f"?{parsed.query}" if parsed.query else "")
    key = base64.b64encode(secrets.token_bytes(16)).decode()
    expected = base64.b64encode(hashlib.sha1((key + WS_GUID).encode()).digest()).decode()
    conn = http.client.HTTPSConnection(
        parsed.hostname, parsed.port or 443, timeout=timeout, context=ssl.create_default_context()
    )
    start = time.monotonic()
    try:
        conn.request(
            "GET",
            path,
            headers={
                "User-Agent": USER_AGENT,
                "Upgrade": "websocket",
                "Connection": "Upgrade",
                "Sec-WebSocket-Key": key,
                "Sec-WebSocket-Version": "13",
            },
        )
        resp = conn.getresponse()
        res.latency_ms = elapsed_ms(start)
        res.status = resp.status
        res.headers = headers_of_interest(resp.headers)
        accept_ok = resp.getheader("Sec-WebSocket-Accept") == expected
        res.ok = resp.status == 101 and accept_ok
        if res.ok:
            res.detail = "handshake 101 válido"
        elif resp.status == 101:
            res.detail = "101 pero Sec-WebSocket-Accept no coincide"
        else:
            res.detail = f"HTTP {resp.status} {resp.reason}"
    except NETWORK_ERRORS as exc:
        res.latency_ms = elapsed_ms(start)
        res.detail = f"error de red: {exc}"
    finally:
        conn.close()
    return res


def build_probes(sample_mint: str) -> list[Probe]:
    m = urllib.parse.quote(sample_mint, safe="")
    return [
        Probe("DexScreener tokens (línea base actual)", "P2.6", "http",
              f"https://api.dexscreener.com/latest/dex/tokens/{SOL_MINT}", json_path("pairs")),
        Probe("GeckoTerminal new_pools", "P2.6/P0.1", "http",
              "https://api.geckoterminal.com/api/v2/networks/solana/new_pools?page=1",
              json_path("data", "attributes", "transactions")),
        Probe("GeckoTerminal trending_pools", "P2.6", "http",
              "https://api.geckoterminal.com/api/v2/networks/solana/trending_pools",
              json_path("data", "attributes")),
        Probe("DexPaprika token", "P2.6", "http",
              f"https://api.dexpaprika.com/networks/solana/tokens/{SOL_MINT}", json_path()),
        Probe("DexPaprika pools/search", "P2.6", "http",
              "https://api.dexpaprika.com/networks/solana/pools/search"
              "?order_by=volume_usd_24h&sort=desc&limit=5", json_path()),
        Probe("DexPaprika SSE streaming", "P0.2", "sse",
              f"https://streaming.dexpaprika.com/stream?method=t_p&chain=solana&address={SOL_MINT}"),
        Probe("Jupiter Tokens V2 search (sin key)", "P0.1/P2.6", "http",
              f"https://api.jup.ag/tokens/v2/search?query={SOL_MINT}", json_path("organicScore")),
        Probe("Jupiter toporganicscore/5m (sin key)", "P0.1", "http",
              "https://api.jup.ag/tokens/v2/toporganicscore/5m?limit=5", json_path("stats5m")),
        Probe("Jupiter recent (sin key)", "P0.2", "http",
              "https://api.jup.ag/tokens/v2/recent", json_path()),
        Probe("RugCheck report/summary", "P1.5", "http",
              f"https://api.rugcheck.xyz/v1/tokens/{m}/report/summary", json_path("risks")),
        Probe("RugCheck stats/new_tokens", "P1.5", "http",
              "https://api.rugcheck.xyz/v1/stats/new_tokens", json_path()),
        Probe("GoPlus Solana token_security", "P1.5", "http",
              f"https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses={m}",
              json_path("result")),
        Probe("Trench.bot bundle (NO oficial)", "P1.5", "http",
              f"https://trench.bot/api/bundle/bundle_advanced/{m}", json_path()),
        Probe("GDELT DOC 2.0 artlist", "P1.4", "http",
              "https://api.gdeltproject.org/api/v2/doc/doc?query=solana%20memecoin"
              "&mode=artlist&maxrecords=5&format=json&timespan=24h", json_path()),
        Probe("Google News RSS", "P1.4", "http",
              "https://news.google.com/rss/search?q=solana+memecoin&hl=en-US&gl=US&ceid=US:en",
              text_contains("<rss")),
        Probe("Reddit RSS r/solana", "P1.4", "http",
              "https://www.reddit.com/r/solana/new/.rss", text_contains("<feed")),
        Probe("Telegram vista pública t.me/s", "P1.3/P1.4", "http",
              "https://t.me/s/durov", text_contains("tgme_widget_message")),
        Probe("PumpPortal WS (handshake)", "P0.2", "ws", "wss://pumpportal.fun/api/data"),
        Probe("PumpDev WS (handshake, redundancia)", "P2.6", "ws", "wss://pumpdev.io/ws"),
    ]


def render_markdown(results: list[Result], ok: int, total: int) -> str:
    lines = [
        f"### Sonda de fuentes — {ok}/{total} OK",
        "",
        "| Fuente | Problema | Tipo | OK | HTTP | ms | Detalle |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        detail = r.detail.replace("|", "\\|").replace("\n", " ")[:140]
        latency = "-" if r.latency_ms is None else str(r.latency_ms)
        lines.append(
            f"| {r.name} | {r.problem} | {r.kind} | {'✅' if r.ok else '❌'} "
            f"| {r.status or '-'} | {latency} | {detail} |"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sonda de solo lectura de fuentes gratuitas.")
    parser.add_argument("--sample-mint",
                        default=os.environ.get("PROBE_SAMPLE_MINT", "").strip() or DEFAULT_SAMPLE_MINT)
    parser.add_argument("--out", default="probe_report.json")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--gap", type=float, default=2.5,
                        help="segundos entre sondas (respeta 0.5 RPS de Jupiter sin key y 1 req/5 s de GDELT)")
    parser.add_argument("--only", nargs="*", default=None,
                        help="ejecuta solo sondas cuyo nombre contenga estas subcadenas")
    args = parser.parse_args(argv)

    if not BASE58_MINT.fullmatch(args.sample_mint):
        parser.error(f"--sample-mint no parece un mint base58 válido: {args.sample_mint!r}")
    if args.timeout <= 0 or args.gap < 0:
        parser.error("--timeout debe ser > 0 y --gap >= 0")

    probes = build_probes(args.sample_mint)
    if args.only:
        needles = [n.lower() for n in args.only]
        probes = [p for p in probes if any(n in p.name.lower() for n in needles)]
    runners: dict[str, Callable[[Probe, float], Result]] = {
        "http": run_http, "sse": run_sse, "ws": run_ws_handshake,
    }

    results: list[Result] = []
    for index, probe in enumerate(probes):
        if index:
            time.sleep(args.gap)
        result = runners[probe.kind](probe, args.timeout)
        results.append(result)
        print(f"[{'OK   ' if result.ok else 'FALLA'}] {probe.name}: {result.detail}", flush=True)

    ok = sum(r.ok for r in results)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "runner": {
            "github_actions": os.environ.get("GITHUB_ACTIONS") == "true",
            "runner_os": os.environ.get("RUNNER_OS"),
            "python": sys.version.split()[0],
        },
        "sample_mint": args.sample_mint,
        "summary": {"ok": ok, "total": len(results)},
        "results": [asdict(r) for r in results],
    }
    markdown = render_markdown(results, ok, len(results))
    print("\n" + markdown)
    try:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "a", encoding="utf-8") as fh:
                fh.write(markdown + "\n")
    except OSError as exc:
        print(f"No se pudo escribir el reporte: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())