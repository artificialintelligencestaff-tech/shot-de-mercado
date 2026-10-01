#!/usr/bin/env python3
"""
lib_repetition.py — Métrica de repetición mediática (doc 26 v0.1): parsers de fuentes públicas y fórmula.

Solo biblioteca estándar y SIN red: las funciones reciben el texto ya descargado. La usan la sonda de fuentes
(probe_narrative_sources.py) y, cuando Dirección habilite la Fase 0, el registro en sombra.
NO está conectada al pipeline ni modifica ningún score.

Ítem normalizado: {"source", "id", "ts" (epoch UTC o None), "text", "author" (o None)}.

Fórmulas (doc 26 §3):
  v0   intensity = (m_1h / m̄_24h) × (S_1h / S̄_24h)                          (directiva; None si un baseline es 0)
  v0.1 intensity = (m_1h+α)/(m̄_24h+α) × S_eff,1h / max(1, S̄_eff,24h) × ((m_1h+α)/(m_prev+α))^β
       sorpresa  = −ln P(X ≥ m_1h | Poisson(max(m̄_24h, λ_min)))
Parámetros HEURÍSTICOS, NO CALIBRADOS: α = 1 · β = 0,5 · λ_min = 0,25 · mínimo 5 menciones · sorpresa ≥ 4,6 nats
(p ≤ 0,01) · S_eff ≥ 2 · autores distintos / menciones ≥ 0,3.
"""
import hashlib
import html
import math
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from typing import Any, Dict, Iterable, List, Mapping, Optional

ALPHA = 1.0
BETA = 0.5
LAMBDA_MIN = 0.25
MIN_MENTIONS = 5
SURPRISE_MIN = -math.log(0.01)        # 4,6 nats = p ≤ 0,01
SEFF_MIN = 2.0
AUTHORS_MIN = 0.3
TIERS = ((10, "saturación"), (6, "muy alta"), (3, "alta"))
MATCH_WEIGHTS = {"ca": 1.0, "cashtag": 0.5, "name": 0.25}
VERSION = "rep-0.1"


# ---------------------------------------------------------------------------
# Parsers (texto descargado -> ítems normalizados)
# ---------------------------------------------------------------------------

def _epoch(value):
    """RFC 822 (RSS) o ISO 8601 (Atom, Telegram) -> epoch UTC; None si no se puede leer."""
    if not value:
        return None
    text = value.strip()
    try:
        dt = parsedate_to_datetime(text)
    except (TypeError, ValueError, IndexError):
        try:
            dt = datetime.fromisoformat(re.sub(r"(\.\d{6})\d+", r"\1", text).replace("Z", "+00:00"))
        except ValueError:
            return None
    if dt is None:
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def strip_html(text):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", text or "")).split())


def _local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_feed(xml_text, source):
    """RSS 2.0 (`item`) o Atom (`entry`), sin depender del namespace."""
    root = ET.fromstring(xml_text)
    items = []
    for node in root.iter():
        if _local(node.tag) not in ("item", "entry"):
            continue
        fields = {}
        for child in node:
            name = _local(child.tag)
            if name == "author":                       # Atom: <author><name>…</name></author>
                fields["author"] = "".join(child.itertext()).strip() or None
            elif name not in fields:
                fields[name] = (child.text or "").strip() if name != "content" else "".join(child.itertext())
        when = fields.get("pubDate") or fields.get("published") or fields.get("updated") or fields.get("date")
        text = " ".join(x for x in (fields.get("title"), strip_html(fields.get("description") or fields.get("summary")
                                                                    or fields.get("content") or "")) if x)
        items.append({"source": source, "id": fields.get("guid") or fields.get("id") or fields.get("link"),
                      "ts": _epoch(when), "text": text, "author": fields.get("author") or fields.get("creator")})
    return items


class _TelegramPreview(HTMLParser):
    """Vista web pública de un canal (t.me/s/<canal>): un ítem por mensaje (data-post, <time>, texto)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.current, self.text_depth, self.depth = [], None, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "div" and "tgme_widget_message" in classes and a.get("data-post"):
            self.current = {"id": a["data-post"], "ts": None, "text": [], "author": None}
            self.items.append(self.current)
        if self.current is None:
            return
        if tag == "time" and a.get("datetime") and self.current["ts"] is None:
            self.current["ts"] = _epoch(a["datetime"])
        if tag == "div":
            if self.text_depth:
                self.text_depth += 1
            elif "tgme_widget_message_text" in classes:
                self.text_depth = 1
        if tag == "br" and self.text_depth:
            self.current["text"].append(" ")

    def handle_endtag(self, tag):
        if tag == "div" and self.text_depth:
            self.text_depth -= 1

    def handle_data(self, data):
        if self.current is not None and self.text_depth:
            self.current["text"].append(data)


def parse_telegram_preview(html_text, source):
    parser = _TelegramPreview()
    parser.feed(html_text)
    return [{"source": source, "id": m["id"], "ts": m["ts"], "text": " ".join("".join(m["text"]).split()),
             "author": m["id"].split("/")[0]} for m in parser.items]


def parse_4chan_catalog(data, source):
    items = []
    for page in data or []:
        for t in page.get("threads") or []:
            items.append({"source": source, "id": str(t.get("no")), "ts": t.get("last_modified") or t.get("time"),
                          "text": " ".join(x for x in (strip_html(t.get("sub")), strip_html(t.get("com"))) if x),
                          "author": None})        # anónimo: sin autor
    return items


def parse_hn(data, source):
    return [{"source": source, "id": h.get("objectID"), "ts": h.get("created_at_i"),
             "text": " ".join(x for x in (h.get("title"), strip_html(h.get("story_text"))) if x),
             "author": h.get("author")} for h in (data or {}).get("hits") or []]


def parse_coingecko_trending(data, source):
    """Top de búsquedas de 24 h: atención, no menciones (sin timestamp por ítem)."""
    return [{"source": source, "id": (c.get("item") or {}).get("id"), "ts": None,
             "text": f"{(c.get('item') or {}).get('name', '')} ${(c.get('item') or {}).get('symbol', '')}",
             "author": None} for c in (data or {}).get("coins") or []]


def parse_gdelt_timeline(data, source):
    """GDELT DOC timelinevolraw: un ítem por punto de la serie (volumen de artículos por intervalo)."""
    points = []
    for serie in (data or {}).get("timeline") or []:
        points += serie.get("data") or []
    return [{"source": source, "id": p.get("date"), "ts": _epoch(_gdelt_date(p.get("date"))),
             "text": str(p.get("value")), "author": None} for p in points]


def _gdelt_date(value):
    m = re.fullmatch(r"(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z", str(value or ""))
    return f"{m[1]}-{m[2]}-{m[3]}T{m[4]}:{m[5]}:{m[6]}+00:00" if m else None


PARSERS = {"feed": parse_feed, "telegram": parse_telegram_preview, "4chan": parse_4chan_catalog, "hn": parse_hn,
           "coingecko": parse_coingecko_trending, "gdelt": parse_gdelt_timeline}


# ---------------------------------------------------------------------------
# Menciones
# ---------------------------------------------------------------------------

def normalized_hash(text):
    """Huella del texto normalizado (minúsculas, sin URLs ni espacios repetidos): un reenvío cuenta una vez."""
    clean = " ".join(re.sub(r"https?://\S+", " ", (text or "").lower()).split())
    return hashlib.sha1(clean.encode("utf-8")).hexdigest()


def match_weight(text, address, symbol=None, name=None):
    """Peso de la mención más fuerte del ítem: contrato exacto 1,0 · cashtag 0,5 · nombre (≥ 2 palabras) 0,25."""
    if address and address in (text or ""):
        return MATCH_WEIGHTS["ca"]
    if symbol and re.search(rf"(?<![\w$])\${re.escape(symbol)}(?!\w)", text or "", re.IGNORECASE):
        return MATCH_WEIGHTS["cashtag"]
    if name and len(name.split()) >= 2 and re.search(rf"(?<!\w){re.escape(name)}(?!\w)", text or "", re.IGNORECASE):
        return MATCH_WEIGHTS["name"]
    return 0.0


def mentions(items, address, symbol=None, name=None):
    """Menciones del activo, deduplicadas por (fuente, texto normalizado). Cada una: ts, source, weight, author."""
    seen, out = set(), []
    for it in items:
        w = match_weight(it.get("text"), address, symbol, name)
        key = (it.get("source"), normalized_hash(it.get("text")))
        if w and it.get("ts") and key not in seen:
            seen.add(key)
            out.append({"ts": it["ts"], "source": it.get("source"), "weight": w, "author": it.get("author")})
    return out


# ---------------------------------------------------------------------------
# Fórmula (doc 26 §3)
# ---------------------------------------------------------------------------

def effective_sources(counts):
    """exp(H), H = entropía de Shannon del reparto por fuente: 'fuentes efectivas'."""
    total = sum(v for v in counts.values() if v > 0)
    if total <= 0:
        return 0.0
    probs = [v / total for v in counts.values() if v > 0]
    return math.exp(-sum(p * math.log(p) for p in probs))


def poisson_log_sf(k, lam):
    """ln P(X ≥ k) para X ~ Poisson(lam), estable en espacio logarítmico."""
    if k <= 0:
        return 0.0
    log_pmf = [-lam + i * math.log(lam) - math.lgamma(i + 1) for i in range(k)]   # P(X < k), término a término
    top = max(log_pmf)
    below = math.exp(top) * sum(math.exp(x - top) for x in log_pmf)
    if below < 0.5:
        return math.log1p(-below)
    # cola chica: sumar los términos desde k hasta que no aporten (evita 1 − casi 1)
    terms, i = [], k
    while True:
        t = -lam + i * math.log(lam) - math.lgamma(i + 1)
        terms.append(t)
        if t < max(terms) - 40 or i > k + 10_000:
            break
        i += 1
    top = max(terms)
    return top + math.log(sum(math.exp(x - top) for x in terms))


def surprise(k, mean_24h):
    """−ln P(X ≥ k | λ), con λ = max(m̄_24h, λ_min): nats de sorpresa de la hora actual."""
    return -poisson_log_sf(int(round(k)), max(mean_24h, LAMBDA_MIN))


def intensity_v0(m_1h, m_24h_mean, sources_1h, sources_24h_mean):
    """Fórmula de la directiva. None si algún baseline es 0 (división por cero: token sin historia)."""
    if not m_24h_mean or not sources_24h_mean:
        return None
    return (m_1h / m_24h_mean) * (sources_1h / sources_24h_mean)


def intensity_v01(m_1h, m_24h_mean, m_prev, seff_1h, seff_24h_mean, alpha=ALPHA, beta=BETA):
    ratio = (m_1h + alpha) / (m_24h_mean + alpha)
    diversity = seff_1h / max(1.0, seff_24h_mean)
    velocity = ((m_1h + alpha) / (m_prev + alpha)) ** beta
    return ratio * diversity * velocity


def tier(value):
    return next((label for limit, label in TIERS if value is not None and value >= limit), "normal")


def repetition_snapshot(found, now, sources_total=None):
    """Métrica de la última hora completa contra las 24 h previas, a partir de `mentions(...)`."""
    hour = 3600.0
    cur = [m for m in found if now - hour < m["ts"] <= now]
    prev = [m for m in found if now - 2 * hour < m["ts"] <= now - hour]
    base = [m for m in found if now - 25 * hour < m["ts"] <= now - hour]
    m_1h = sum(m["weight"] for m in cur)
    m_prev = sum(m["weight"] for m in prev)
    m_24h_mean = sum(m["weight"] for m in base) / 24

    def by_source(ms):
        out = {}
        for m in ms:
            out[m["source"]] = out.get(m["source"], 0.0) + m["weight"]
        return out

    hourly_seff, hourly_sources = [], []
    for h in range(1, 25):
        bucket = [m for m in base if now - (h + 1) * hour < m["ts"] <= now - h * hour]
        hourly_seff.append(effective_sources(by_source(bucket)))
        hourly_sources.append(len({m["source"] for m in bucket}))
    seff_1h = effective_sources(by_source(cur))
    authors = [m["author"] for m in cur if m["author"]]
    value = intensity_v01(m_1h, m_24h_mean, m_prev, seff_1h, sum(hourly_seff) / 24)
    s = surprise(m_1h, m_24h_mean)
    signal = (m_1h >= MIN_MENTIONS and s >= SURPRISE_MIN and seff_1h >= SEFF_MIN
              and (not authors or len(set(authors)) / len(authors) >= AUTHORS_MIN))
    return {"version": VERSION, "m_1h": m_1h, "m_prev_1h": m_prev, "m_24h_mean": m_24h_mean,
            "sources_1h": len({m["source"] for m in cur}), "seff_1h": seff_1h,
            "intensity_v0": intensity_v0(m_1h, m_24h_mean, len({m["source"] for m in cur}), sum(hourly_sources) / 24),
            "intensity": value, "surprise_nats": s,
            "authors_ratio": len(set(authors)) / len(authors) if authors else None,
            "tier": tier(value) if signal else "normal", "signal": signal, "sources_total": sources_total}
