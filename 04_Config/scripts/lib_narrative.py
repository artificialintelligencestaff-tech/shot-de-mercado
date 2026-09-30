#!/usr/bin/env python3
"""
lib_narrative.py — Capa de Anticipación Narrativa (Capítulo VII, Proyecto Shot de Mercado).

PROTOTIPO. Solo biblioteca estándar. Agnóstico a chain: `chain` y `address` son strings
opacos que vienen del registro de narrativas o de las fuentes; ninguna función asume una
chain. Toda la red pasa por un `fetcher` inyectable: en dry-run se usa FixtureFetcher con
respuestas guardadas y el prototipo funciona sin llamar a ninguna API.

Capas
  A  fetch_eventos_calendario()     eventos programados (Wikidata P577 + calendario manual)
  B  detect_narrative_emerging()    picos de atención (Wikipedia Pageviews, GDELT timelinevol)
  C  map_narrative_to_tokens()      narrativa -> tokens (registro curado + coincidencia de nombre)
  D  verify_quantitative()          "modo lupa": ¿la narrativa se traduce en flujo real?
  E  narrative_evidence()           LLR con el mismo contrato que script_112 -> lib_fusion
Método científico
  event_study(), bootstrap_ci(), placebo_days(), walk_forward_splits(), evaluate_hypothesis()

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

Parámetros — TODOS HEURÍSTICOS NO CALIBRADOS (ver El cerebro de dios/18_CAPITULO_VII_NARRATIVA.md):
    SPIKE_RATIO          = 5.0   pico si valor >= 5x la mediana de los 28 días previos
    SPIKE_ROBUST_Z       = 3.5   y z robusto (MAD) >= 3.5
    SPIKE_BASELINE_DAYS  = 28
    MIN_BASELINE         = {"wikipedia_pageviews": 50}  mediana mínima para no leer ruido
    ANTICIPATION_DAYS    = 14    ventana de anticipación antes de un evento programado
    POST_EVENT_DAYS      = 7
    LINK_WEIGHTS         = direct 1.0 · thematic 0.5 · name_match 0.0 (solo aporta riesgo)
    NARRATIVE_LLR_MAX    = 1.0   nats, antes del recorte ±c de lib_fusion
    COPYCAT_LLR          = -1.0  token con coincidencia de nombre y < 30 días de vida
    Lupa: liquidez < $10k -> -0.75 · rotación >= 1 con precio al alza -> +0.5 · par < 7 días -> -0.5
    VERTICAL_MOVE        = 0.20  aceleración vertical = +20% en la ventana
    ACCEPT_HIT_RATE      = 0.55  y ACCEPT_MIN_N = 20 (criterio de aceptación de Dirección)
"""
import json
import math
import random
import re
import statistics
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

SPIKE_RATIO = 5.0
SPIKE_ROBUST_Z = 3.5
SPIKE_BASELINE_DAYS = 28
MIN_BASELINE = {"wikipedia_pageviews": 50.0}
ANTICIPATION_DAYS = 14
POST_EVENT_DAYS = 7
LINK_WEIGHTS = {"direct": 1.0, "thematic": 0.5, "name_match": 0.0}
NARRATIVE_LLR_MAX = 1.0
COPYCAT_LLR = -1.0
COPYCAT_MAX_AGE_DAYS = 30
LUPA_MIN_LIQUIDITY = 10_000.0
LUPA_HIGH_LIQUIDITY = 100_000.0
LUPA_TURNOVER_CONFIRM = 1.0
LUPA_TURNOVER_DEAD = 0.05
LUPA_NEW_PAIR_DAYS = 7
VERTICAL_MOVE = 0.20
ACCEPT_HIT_RATE = 0.55
ACCEPT_MIN_N = 20
LABEL = "HEURISTICA_NO_CALIBRADA"

WIKIPEDIA_PAGEVIEWS = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
                       "{project}/all-access/user/{article}/daily/{start}/{end}")
GDELT_DOC = "https://api.gdeltproject.org/api/v2/doc/doc"
WIKIDATA_SPARQL = "https://query.wikidata.org/sparql"
DEXSCREENER_TOKENS = "https://api.dexscreener.com/latest/dex/tokens/{address}"
DEXSCREENER_SEARCH = "https://api.dexscreener.com/latest/dex/search"
USER_AGENT = ("shot-de-mercado-narrative/0.1 "
              "(+https://github.com/artificialintelligencestaff-tech/shot-de-mercado)")

_EVM_ADDRESS = re.compile(r"0x[0-9a-fA-F]{40}")

Fetcher = Callable[[str, Optional[Mapping[str, Any]]], Dict[str, Any]]


# ---------------------------------------------------------------------------
# Acceso a red (inyectable)
# ---------------------------------------------------------------------------

def request_key(url: str, params: Optional[Mapping[str, Any]] = None) -> str:
    """Clave canónica de una consulta (URL + parámetros ordenados). Indexa las fixtures."""
    if not params:
        return url
    return url + "?" + urllib.parse.urlencode(sorted((k, str(v)) for k, v in params.items()))


class FixtureFetcher:
    """Dry-run: responde desde un dict {request_key: json}. Nunca toca la red."""

    def __init__(self, fixtures: Mapping[str, Any]):
        self.fixtures = dict(fixtures)
        self.calls: List[str] = []

    def __call__(self, url: str, params: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        key = request_key(url, params)
        self.calls.append(key)
        if key not in self.fixtures:
            return {"status": "error", "http_status": None, "data": None, "detail": f"fixture ausente: {key}"}
        return {"status": "ok", "http_status": 200, "data": self.fixtures[key], "detail": "fixture"}


class HttpFetcher:
    """Modo live: urllib, User-Agent propio, intervalo mínimo por host. Nunca lanza."""

    DEFAULT_INTERVALS = {"api.gdeltproject.org": 6.0, "api.coingecko.com": 7.0,
                         "api.dexscreener.com": 1.0, "query.wikidata.org": 1.0, "wikimedia.org": 0.2}

    def __init__(self, timeout: float = 20.0, intervals: Optional[Mapping[str, float]] = None):
        self.timeout = timeout
        self.intervals = dict(self.DEFAULT_INTERVALS, **(intervals or {}))
        self._last: Dict[str, float] = {}

    def __call__(self, url: str, params: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        full = request_key(url, params)
        host = urllib.parse.urlsplit(url).hostname or ""
        wait = self.intervals.get(host, 1.0) - (time.monotonic() - self._last.get(host, -1e9))
        if wait > 0:
            time.sleep(wait)
        self._last[host] = time.monotonic()
        req = urllib.request.Request(full, headers={"User-Agent": USER_AGENT,
                                                    "Accept": "application/sparql-results+json, application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read(5_000_000)
                status = resp.status
        except urllib.error.HTTPError as e:
            return {"status": "error", "http_status": e.code, "data": None, "detail": f"HTTP {e.code}"}
        except (OSError, ValueError) as e:
            return {"status": "error", "http_status": None, "data": None, "detail": f"red: {e}"}
        try:
            return {"status": "ok", "http_status": status, "data": json.loads(body), "detail": ""}
        except ValueError:
            text = body[:200].decode("utf-8", "replace")
            kind = "rate_limited" if "limit requests" in text.lower() else "error"
            return {"status": kind, "http_status": status, "data": None, "detail": text}


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def normalize_address(address: str) -> str:
    """Direcciones 0x (EVM) sin distinción de mayúsculas; cualquier otro formato, exacto."""
    address = (address or "").strip()
    return address.lower() if _EVM_ADDRESS.fullmatch(address) else address


def token_key(chain: str, address: str) -> str:
    return f"{chain}:{normalize_address(address)}"


def _parse_day(value: Any) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    s = str(value)
    if len(s) >= 8 and s[:8].isdigit():                       # 20231205 / 2023120500
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    return datetime.fromisoformat(s.replace("Z", "+00:00")[:25]).date()


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


# ---------------------------------------------------------------------------
# Capa A — Calendario de eventos conocidos
# ---------------------------------------------------------------------------

WIKIDATA_CLASSES = {"game_release": "Q7889", "film_release": "Q11424"}


def _wikidata_query(klass: str, start: date, end: date, min_sitelinks: int) -> str:
    return (
        "SELECT ?item ?itemLabel ?date ?links WHERE { "
        f"?item wdt:P31 wd:{klass}; wdt:P577 ?date; wikibase:sitelinks ?links . "
        f'FILTER(?date >= "{start.isoformat()}T00:00:00Z"^^xsd:dateTime && '
        f'?date <= "{end.isoformat()}T00:00:00Z"^^xsd:dateTime) '
        f"FILTER(?links >= {int(min_sitelinks)}) "
        'SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } '
        "} ORDER BY DESC(?links) LIMIT 50"
    )


def event_phase(event_day: date, today: date,
                anticipation_days: int = ANTICIPATION_DAYS, post_days: int = POST_EVENT_DAYS) -> Tuple[str, int]:
    """(fase, días hasta el evento). Fases: lejano · anticipacion · evento · post · pasado."""
    d = (event_day - today).days
    if d > anticipation_days:
        return "lejano", d
    if d > 0:
        return "anticipacion", d
    if d == 0:
        return "evento", d
    if d >= -post_days:
        return "post", d
    return "pasado", d


def fetch_eventos_calendario(today: date, horizon_days: int, fetcher: Fetcher,
                             categories: Sequence[str] = ("game_release",), min_sitelinks: int = 15,
                             manual_events: Sequence[Mapping[str, Any]] = ()) -> Dict[str, Any]:
    """Eventos programados entre hoy y hoy+horizon.

    Fuentes: Wikidata (P577 = fecha de publicación; popularidad = sitelinks) [V 2026-09-30] y un
    calendario manual para lo que no tiene API gratuita (FOMC, CPI, TGEs) [P].
    Wikidata puede traer varias fechas por ítem (plataforma/región): se conserva la más temprana
    dentro del rango y se marca `date_quality: "multiple"`.
    """
    end = today + timedelta(days=horizon_days)
    events: Dict[str, Dict[str, Any]] = {}
    sources: List[Dict[str, Any]] = []
    for category in categories:
        klass = WIKIDATA_CLASSES[category]
        res = fetcher(WIKIDATA_SPARQL, {"query": _wikidata_query(klass, today, end, min_sitelinks),
                                        "format": "json"})
        sources.append({"source": f"wikidata:{category}", "status": res["status"], "detail": res["detail"]})
        if res["status"] != "ok":
            continue
        for row in (res["data"] or {}).get("results", {}).get("bindings", []):
            item = row["item"]["value"].rsplit("/", 1)[-1]
            day = _parse_day(row["date"]["value"])
            label = row.get("itemLabel", {}).get("value", item)
            prev = events.get(item)
            if prev:
                prev["date_quality"] = "multiple"
                if day.isoformat() < prev["date"]:
                    prev["date"] = day.isoformat()
                continue
            events[item] = {
                "id": f"wikidata:{item}", "wikidata_item": item, "title": label,
                "date": day.isoformat(), "category": category,
                "popularity_sitelinks": int(row["links"]["value"]),
                "source": "wikidata", "source_url": f"https://www.wikidata.org/wiki/{item}",
                "label_quality": "sin_etiqueta_en" if label == item else "ok",
                "date_quality": "single", "evidence": "[V] fuente pública, fecha puede cambiar",
            }
    for ev in manual_events:
        day = _parse_day(ev["date"])
        if today <= day <= end:
            events[ev["id"]] = dict(ev, date=day.isoformat(), source=ev.get("source", "manual"),
                                    evidence=ev.get("evidence", "[I] calendario manual"))
    out = sorted(events.values(), key=lambda e: (e["date"], -e.get("popularity_sitelinks", 0)))
    for ev in out:
        ev["phase"], ev["days_to_event"] = event_phase(_parse_day(ev["date"]), today)
    return {"generated_for": today.isoformat(), "horizon_days": horizon_days, "events": out, "sources": sources}


# ---------------------------------------------------------------------------
# Capa B — Detección de narrativa emergente
# ---------------------------------------------------------------------------

def fetch_attention_series(topic: str, source: str, start: date, end: date, fetcher: Fetcher,
                           article: Optional[str] = None, query: Optional[str] = None,
                           project: str = "en.wikipedia") -> Dict[str, Any]:
    """Serie diaria de atención: {"topic", "source", "status", "points": [{"date", "value"}]}.

    wikipedia_pageviews [V]: gratis, sin key, historia desde 2015-07.
    gdelt_timelinevol   [V con reservas]: gratis, pero devolvió límite de tasa en 2/2 intentos.
    """
    series = {"topic": topic, "source": source, "status": "error", "detail": "", "points": []}
    if source == "wikipedia_pageviews":
        url = WIKIPEDIA_PAGEVIEWS.format(project=project, article=urllib.parse.quote(article or topic, safe=""),
                                         start=start.strftime("%Y%m%d"), end=end.strftime("%Y%m%d"))
        res = fetcher(url, None)
        if res["status"] == "ok":
            series["points"] = [{"date": _parse_day(x["timestamp"]).isoformat(), "value": float(x["views"])}
                                for x in (res["data"] or {}).get("items", [])]
    elif source == "gdelt_timelinevol":
        res = fetcher(GDELT_DOC, {"query": query or f'"{topic}"', "mode": "timelinevol", "format": "json",
                                  "startdatetime": start.strftime("%Y%m%d000000"),
                                  "enddatetime": end.strftime("%Y%m%d235959")})
        if res["status"] == "ok":
            timeline = (res["data"] or {}).get("timeline") or [{}]
            series["points"] = [{"date": _parse_day(x["date"]).isoformat(), "value": float(x["value"])}
                                for x in timeline[0].get("data", [])]
    else:
        raise ValueError(f"fuente de atención desconocida: {source}")
    series["status"], series["detail"] = res["status"], res["detail"]
    return series


def _robust_stats(window: Sequence[float]) -> Tuple[float, float]:
    med = statistics.median(window)
    mad = statistics.median(abs(x - med) for x in window)
    return med, mad


def detect_narrative_emerging(series: Mapping[str, Any], ratio: float = SPIKE_RATIO,
                              robust_z: float = SPIKE_ROBUST_Z, baseline_days: int = SPIKE_BASELINE_DAYS,
                              min_baseline: Optional[float] = None) -> Dict[str, Any]:
    """Picos de atención de una serie diaria.

    Pico en el día t si: mediana(t-28..t-1) >= min_baseline, valor/mediana >= ratio y
    z_robusto = 0.6745·(valor − mediana)/MAD >= robust_z (MAD = 0 cuenta como z infinito).
    Solo usa datos PREVIOS a t (sin look-ahead). También informa el estado del último día.
    """
    pts = sorted(series.get("points", []), key=lambda p: p["date"])
    values = [p["value"] for p in pts]
    floor = MIN_BASELINE.get(series.get("source", ""), 0.0) if min_baseline is None else min_baseline
    spikes, last = [], None
    for i in range(baseline_days, len(pts)):
        med, mad = _robust_stats(values[i - baseline_days:i])
        v = values[i]
        r = v / med if med > 0 else (math.inf if v > 0 else 0.0)
        z = 0.6745 * (v - med) / mad if mad > 0 else (math.inf if v > med else 0.0)
        info = {"topic": series.get("topic"), "source": series.get("source"), "date": pts[i]["date"],
                "value": v, "baseline_median": med, "ratio": round(r, 3) if math.isfinite(r) else None,
                "robust_z": round(z, 3) if math.isfinite(z) else None}
        last = info
        if med >= floor and r >= ratio and z >= robust_z:
            spikes.append(info)
    return {"topic": series.get("topic"), "source": series.get("source"), "status": series.get("status"),
            "n_points": len(pts), "spikes": spikes, "latest": last,
            "emerging_now": bool(spikes and last and spikes[-1]["date"] == last["date"]),
            "params": {"ratio": ratio, "robust_z": robust_z, "baseline_days": baseline_days, "min_baseline": floor}}


# ---------------------------------------------------------------------------
# Capa C — Mapeo narrativa -> activo
# ---------------------------------------------------------------------------

class KeywordMatcher:
    """Extracción determinística de narrativas en texto (alternativa stdlib a pyahocorasick).

    Coincidencia por palabra completa, sin distinción de mayúsculas. Para miles de patrones,
    pyahocorasick (BSD-3) es el reemplazo directo con la misma interfaz de resultados.
    """

    def __init__(self, registry: Mapping[str, Any]):
        self.patterns: List[Tuple[re.Pattern, str, str]] = []
        for nid, spec in registry.get("narratives", {}).items():
            for kw in spec.get("keywords", []):
                rx = re.compile(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", re.IGNORECASE)
                self.patterns.append((rx, nid, kw))

    def extract(self, text: str) -> List[Dict[str, Any]]:
        hits = []
        for rx, nid, kw in self.patterns:
            for m in rx.finditer(text or ""):
                hits.append({"narrative": nid, "keyword": kw, "start": m.start(), "end": m.end()})
        return sorted(hits, key=lambda h: h["start"])


def map_narrative_to_tokens(narrative: str, registry: Mapping[str, Any],
                            search_pairs: Sequence[Mapping[str, Any]] = (),
                            now_ms: Optional[float] = None) -> List[Dict[str, Any]]:
    """Tokens vinculados a una narrativa.

    - direct / thematic: vínculos curados del registro, con su fuente (p.ej. categoría CoinGecko).
    - name_match: pares de una búsqueda por nombre (DexScreener) que NO están en el registro.
      Nunca suman evidencia: se devuelven con flags de riesgo, porque la literatura midió
      >=10% de copias en el launchpad más grande (arXiv 2609.10246) y en "GTA6" 15/28 tokens tienen < $10k
      de liquidez [V 2026-09-30].
    """
    spec = registry.get("narratives", {}).get(narrative)
    if spec is None:
        raise KeyError(f"narrativa no registrada: {narrative}")
    links: Dict[str, Dict[str, Any]] = {}
    for tok in spec.get("tokens", []):
        key = token_key(tok["chain"], tok["address"])
        links[key] = {"chain": tok["chain"], "address": tok["address"], "symbol": tok.get("symbol", ""),
                      "link_type": tok.get("link_type", "thematic"), "evidence": tok.get("evidence", []),
                      "risk_flags": []}
    keywords = [k.lower().replace(" ", "") for k in spec.get("name_keywords", spec.get("keywords", []))]
    now_ms = time.time() * 1000 if now_ms is None else now_ms
    for pair in search_pairs:
        base = pair.get("baseToken") or {}
        chain, address = pair.get("chainId"), base.get("address")
        if not chain or not address:
            continue
        key = token_key(chain, address)
        name = f"{base.get('symbol', '')} {base.get('name', '')}".lower().replace(" ", "")
        if key in links or not any(k and k in name for k in keywords):
            continue
        age_days = (now_ms - pair["pairCreatedAt"]) / 86_400_000 if pair.get("pairCreatedAt") else None
        liq = (pair.get("liquidity") or {}).get("usd") or 0.0
        flags = ["copycat_suspect"]
        if age_days is not None and age_days < COPYCAT_MAX_AGE_DAYS:
            flags.append("new_token")
        if liq < LUPA_MIN_LIQUIDITY:
            flags.append("low_liquidity")
        links[key] = {"chain": chain, "address": address, "symbol": base.get("symbol", ""),
                      "link_type": "name_match", "evidence": [f"coincidencia de nombre ({pair.get('dexId')})"],
                      "risk_flags": flags, "pair_age_days": round(age_days, 1) if age_days is not None else None,
                      "liquidity_usd": liq}
    order = {"direct": 0, "thematic": 1, "name_match": 2}
    return sorted(links.values(), key=lambda t: (order.get(t["link_type"], 9), t["chain"], t["symbol"]))


# ---------------------------------------------------------------------------
# Capa D — Verificación cuantitativa ("modo lupa")
# ---------------------------------------------------------------------------

def pair_metrics(pairs: Sequence[Mapping[str, Any]], chain: str, now_ms: Optional[float] = None) -> Optional[Dict[str, Any]]:
    """Métricas del par más líquido de `chain` (formato DexScreener /tokens)."""
    own = [p for p in pairs if p.get("chainId") == chain]
    if not own:
        return None
    best = max(own, key=lambda p: float((p.get("liquidity") or {}).get("usd") or 0))
    txns = (best.get("txns") or {}).get("h24") or {}
    now_ms = time.time() * 1000 if now_ms is None else now_ms
    return {
        "pair": best.get("pairAddress"), "dex": best.get("dexId"),
        "price_usd": float(best.get("priceUsd") or 0),
        "liquidity_usd": float((best.get("liquidity") or {}).get("usd") or 0),
        "volume_24h_usd": float((best.get("volume") or {}).get("h24") or 0),
        "price_change_24h_pct": float((best.get("priceChange") or {}).get("h24") or 0),
        "buys_24h": int(txns.get("buys") or 0), "sells_24h": int(txns.get("sells") or 0),
        "pair_age_days": round((now_ms - best["pairCreatedAt"]) / 86_400_000, 1) if best.get("pairCreatedAt") else None,
        "n_pairs_chain": len(own),
    }


def lupa_evidence(metrics: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    """LLR heurístico (nats) a favor de 'la narrativa se traduce en flujo real y absorbible'."""
    comps: List[Dict[str, Any]] = []

    def add(feature: str, value: Any, llr: float, rule: str) -> None:
        comps.append({"feature": feature, "value": value, "llr": round(llr, 4), "rule": rule})

    if not metrics:
        return {"source": "lupa", "label": LABEL, "llr_raw": None, "components": [], "verdict": "sin_datos"}
    liq, vol = metrics["liquidity_usd"], metrics["volume_24h_usd"]
    if liq < LUPA_MIN_LIQUIDITY:
        add("liquidity_usd", liq, -0.75, "< $10k: no absorbe flujo, alto riesgo de rug")
    elif liq >= LUPA_HIGH_LIQUIDITY:
        add("liquidity_usd", liq, 0.25, ">= $100k")
    else:
        add("liquidity_usd", liq, 0.0, "$10k-$100k: neutro")
    turnover = vol / liq if liq > 0 else 0.0
    if turnover >= LUPA_TURNOVER_CONFIRM and metrics["price_change_24h_pct"] > 0:
        add("turnover_24h", round(turnover, 3), 0.5, "rotación >= 1x con precio al alza: flujo confirmado")
    elif turnover < LUPA_TURNOVER_DEAD:
        add("turnover_24h", round(turnover, 3), -0.25, "rotación < 5%: sin flujo")
    else:
        add("turnover_24h", round(turnover, 3), 0.0, "neutro")
    b, s = metrics["buys_24h"], metrics["sells_24h"]
    if b + s > 0:
        ratio = b / max(s, 1)
        add("buys_sells_24h", round(ratio, 3), 0.25 if ratio > 1.2 else (-0.25 if ratio < 0.8 else 0.0),
            "> 1.2 compra dominante · < 0.8 venta dominante")
    age = metrics.get("pair_age_days")
    if age is not None and age < LUPA_NEW_PAIR_DAYS:
        add("pair_age_days", age, -0.5, "< 7 días: la mayoría de los tokens nuevos rugea (arXiv 2608.20271)")
    llr = round(sum(c["llr"] for c in comps), 4)
    verdict = "flujo_confirmado" if llr > 0.25 else ("riesgo" if llr < -0.5 else "sin_confirmar")
    return {"source": "lupa", "label": LABEL, "llr_raw": llr, "components": comps, "verdict": verdict}


def verify_quantitative(token: Mapping[str, Any], fetcher: Fetcher, now_ms: Optional[float] = None) -> Dict[str, Any]:
    """Modo lupa sobre un token {chain, address}: consulta DexScreener y evalúa flujo real."""
    res = fetcher(DEXSCREENER_TOKENS.format(address=token["address"]), None)
    pairs = (res["data"] or {}).get("pairs") or [] if res["status"] == "ok" else []
    metrics = pair_metrics(pairs, token["chain"], now_ms)
    return {"chain": token["chain"], "address": token["address"], "symbol": token.get("symbol", ""),
            "status": res["status"] if metrics or res["status"] != "ok" else "sin_par_en_chain",
            "detail": res["detail"], "metrics": metrics, "evidence": lupa_evidence(metrics)}


# ---------------------------------------------------------------------------
# Capa E — Evidencia narrativa para lib_fusion
# ---------------------------------------------------------------------------

def link_weights_for(narrative_spec: Mapping[str, Any]) -> Dict[str, float]:
    """LINK_WEIGHTS con los overrides calibrados de la narrativa (si el registro los declara)."""
    overrides = {k: v for k, v in (narrative_spec.get("link_weight_overrides") or {}).items()
                 if k in LINK_WEIGHTS and isinstance(v, (int, float))}
    return dict(LINK_WEIGHTS, **overrides)


def narrative_evidence(link: Mapping[str, Any], emergence: Optional[Mapping[str, Any]] = None,
                       event: Optional[Mapping[str, Any]] = None,
                       weights: Optional[Mapping[str, float]] = None) -> Dict[str, Any]:
    """LLR (nats) de la narrativa para UN token, con el contrato {llr_raw, label, components}.

    fuerza = max(atención, calendario) en [−0.25, 1]:
      atención   = clamp(log10(ratio último día), 0, 1)  -> 10x la mediana = 1.0
      calendario = anticipacion 0.5 · evento 0.25 · post −0.25 ("sell the news" [H]) · resto 0
    llr = LINK_WEIGHTS[link_type] · NARRATIVE_LLR_MAX · fuerza
    name_match no suma: aporta COPYCAT_LLR si el token es nuevo.
    """
    comps: List[Dict[str, Any]] = []

    def add(feature: str, value: Any, llr: float, rule: str) -> None:
        comps.append({"feature": feature, "value": value, "llr": round(llr, 4), "rule": rule})

    latest = (emergence or {}).get("latest") or {}
    r = latest.get("ratio")
    attention = _clamp(math.log10(r), 0.0, 1.0) if r and r > 0 else 0.0
    phase = (event or {}).get("phase")
    calendar = {"anticipacion": 0.5, "evento": 0.25, "post": -0.25}.get(phase, 0.0)
    strength = calendar if calendar < 0 else max(attention, calendar)
    weight = (weights or LINK_WEIGHTS).get(link.get("link_type"), 0.0)
    add("attention_ratio", r, 0.0, f"componente atención = {attention:.3f}")
    add("event_phase", phase, 0.0, f"componente calendario = {calendar:+.2f}")
    add("link_type", link.get("link_type"), round(weight * NARRATIVE_LLR_MAX * strength, 4),
        f"peso {weight} x fuerza {strength:.3f}")
    if link.get("link_type") == "name_match" and "new_token" in link.get("risk_flags", []):
        add("copycat", True, COPYCAT_LLR, "coincidencia de nombre + token < 30 días")
    return {"source": "narrative", "label": LABEL, "llr_raw": round(sum(c["llr"] for c in comps), 4),
            "components": comps}


# ---------------------------------------------------------------------------
# Método científico: estudio de eventos, bootstrap, placebo, walk-forward
# ---------------------------------------------------------------------------

def forward_return(prices: Mapping[str, float], day: date, start_offset: int, end_offset: int) -> Optional[float]:
    """close(day+end)/close(day+start) − 1 con precios diarios {YYYY-MM-DD: close}."""
    a = prices.get((day + timedelta(days=start_offset)).isoformat())
    b = prices.get((day + timedelta(days=end_offset)).isoformat())
    return b / a - 1.0 if a and b else None


def event_study(event_days: Iterable[date], prices: Mapping[str, Mapping[str, float]],
                benchmark: Mapping[str, float], start_offset: int, end_offset: int) -> List[Dict[str, Any]]:
    """Retorno anormal por evento: canasta equiponderada − benchmark en [day+start, day+end].

    Además `vertical`: algún activo de la canasta superó +20% en la ventana.
    """
    rows = []
    for day in sorted(set(event_days)):
        rets = {sym: forward_return(p, day, start_offset, end_offset) for sym, p in prices.items()}
        rets = {k: v for k, v in rets.items() if v is not None}
        bench = forward_return(benchmark, day, start_offset, end_offset)
        if not rets or bench is None:
            continue
        basket = sum(rets.values()) / len(rets)
        rows.append({"date": day.isoformat(), "basket_return": round(basket, 6), "benchmark_return": round(bench, 6),
                     "abnormal_return": round(basket - bench, 6), "vertical": any(v >= VERTICAL_MOVE for v in rets.values()),
                     "n_assets": len(rets)})
    return rows


def bootstrap_ci(values: Sequence[float], stat: Callable[[Sequence[float]], float] = statistics.fmean,
                 n_boot: int = 5000, level: float = 0.90, seed: int = 20260930) -> Optional[Tuple[float, float]]:
    """IC por bootstrap de percentiles, con semilla fija."""
    if not values:
        return None
    rng = random.Random(seed)
    k = len(values)
    boots = sorted(stat([values[rng.randrange(k)] for _ in range(k)]) for _ in range(n_boot))
    lo = boots[int((1 - level) / 2 * (n_boot - 1))]
    hi = boots[int((1 + level) / 2 * (n_boot - 1))]
    return round(lo, 6), round(hi, 6)


def placebo_days(candidates: Iterable[date], exclude: Iterable[date], exclusion_radius: int,
                 n: Optional[int] = None, seed: int = 20260930) -> List[date]:
    """Días de control: candidatos a más de `exclusion_radius` días de cualquier evento."""
    ex = sorted(set(exclude))
    ok = [d for d in sorted(set(candidates)) if all(abs((d - e).days) > exclusion_radius for e in ex)]
    if n is None or n >= len(ok):
        return ok
    return sorted(random.Random(seed).sample(ok, n))


def walk_forward_splits(days: Sequence[date], train_days: int, test_days: int,
                        purge_days: int = 2) -> List[Tuple[List[date], List[date]]]:
    """Ventanas train/test consecutivas con purga de `purge_days` entre ambas (48h por defecto).

    Evita que eventos del borde de train compartan la ventana de retorno con test.
    """
    ds = sorted(set(days))
    if not ds:
        return []
    splits, cursor, last = [], ds[0] + timedelta(days=train_days), ds[-1]
    while cursor + timedelta(days=purge_days) <= last:
        test_start = cursor + timedelta(days=purge_days)
        test_end = test_start + timedelta(days=test_days)
        train = [d for d in ds if cursor - timedelta(days=train_days) <= d < cursor]
        test = [d for d in ds if test_start <= d < test_end]
        if train and test:
            splits.append((train, test))
        cursor = test_end
    return splits


def merge_close_events(days: Iterable[date], min_gap_days: int) -> List[date]:
    """Deja el primer evento de cada racha: eventos a <= min_gap días comparten ventana."""
    out: List[date] = []
    for d in sorted(set(days)):
        if not out or (d - out[-1]).days > min_gap_days:
            out.append(d)
    return out


def evaluate_hypothesis(event_rows: Sequence[Mapping[str, Any]], placebo_rows: Sequence[Mapping[str, Any]],
                        hit_rate_threshold: float = ACCEPT_HIT_RATE, min_n: int = ACCEPT_MIN_N) -> Dict[str, Any]:
    """Criterio de aceptación: n >= min_n, P(retorno anormal > 0) > umbral y la cota inferior
    del IC 90% del hit rate por encima del hit rate placebo."""
    hits = [1.0 if r["abnormal_return"] > 0 else 0.0 for r in event_rows]
    p_hits = [1.0 if r["abnormal_return"] > 0 else 0.0 for r in placebo_rows]
    ar = [r["abnormal_return"] for r in event_rows]
    n = len(event_rows)
    hit_rate = statistics.fmean(hits) if hits else None
    placebo_hit = statistics.fmean(p_hits) if p_hits else None
    ci = bootstrap_ci(hits) if hits else None
    reasons = []
    if n < min_n:
        reasons.append(f"n={n} < {min_n}")
    if hit_rate is None or hit_rate <= hit_rate_threshold:
        reasons.append(f"hit_rate={hit_rate} <= {hit_rate_threshold}")
    if ci is None or placebo_hit is None or ci[0] <= placebo_hit:
        reasons.append("IC90 inferior del hit rate no supera al placebo")
    return {
        "n_events": n, "n_placebo": len(placebo_rows),
        "hit_rate": round(hit_rate, 4) if hit_rate is not None else None, "hit_rate_ci90": ci,
        "placebo_hit_rate": round(placebo_hit, 4) if placebo_hit is not None else None,
        "mean_abnormal": round(statistics.fmean(ar), 6) if ar else None,
        "mean_abnormal_ci90": bootstrap_ci(ar),
        "placebo_mean_abnormal": round(statistics.fmean([r["abnormal_return"] for r in placebo_rows]), 6) if placebo_rows else None,
        "vertical_rate": round(statistics.fmean([1.0 if r["vertical"] else 0.0 for r in event_rows]), 4) if event_rows else None,
        "placebo_vertical_rate": round(statistics.fmean([1.0 if r["vertical"] else 0.0 for r in placebo_rows]), 4) if placebo_rows else None,
        "accepted": not reasons, "rejection_reasons": reasons,
        "criteria": {"min_n": min_n, "hit_rate_threshold": hit_rate_threshold},
    }
