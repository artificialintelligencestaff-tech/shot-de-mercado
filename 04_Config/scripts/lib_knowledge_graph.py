#!/usr/bin/env python3
"""
lib_knowledge_graph.py — grafo de conocimiento de las menciones (patrón #7; doc 35 §6.3 "grafo de co-mención").

Input: los ítems src-1 de _merged.jsonl (todas las menciones de los bots de fuentes, 48 h).
Output: 02_Analisis/sources/_graph.json (dueño: bot_orchestrator, que lo escribe después del merge).

  Nodos    t:<dirección>  token (mint o contrato)       c:<CASHTAG>   cashtag
           k:<keyword>    palabra clave (canónica)      s:<bot>:<src> fuente
  Aristas  co-aparición en el mismo ítem. count = frecuencia; weight = Σ exp(−edad / τ) con τ = 24 h, que junta
           frecuencia y recencia (una mención de hace 24 h pesa 0,37; una de ahora, 1).

API: neighbors(node), co_occurrence(a, b), top_keywords(window_h) y related(token): tokens a dos saltos vía
keywords o cashtags compartidos (si uno del cluster se acelera, los demás son candidatos a mirar).
Los nodos se pueden pedir en forma cruda ("$WIF", "Meme Coin", una dirección): se normalizan con lib_normalize.
Solo biblioteca estándar.
"""
import json
import math
import sys
import time
from itertools import combinations
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_normalize as norm  # noqa: E402

VERSION = "kg-0.1"
TAU_H = 24.0
HOURS_KEPT = 48
MAX_ENTITIES = 20            # tope de nodos por ítem (un ítem con 200 keywords no arma 20.000 aristas)
TYPES = {"t": "token", "c": "cashtag", "k": "keyword", "s": "source"}


def node_id(value):
    """Id de nodo desde una forma cruda: 't:/c:/k:/s:' se respeta; dirección -> t; '$X' -> c; resto -> k."""
    s = str(value or "").strip()
    if len(s) > 2 and s[1] == ":" and s[0] in TYPES:
        return s
    a = norm.address(s)
    if a:
        return f"t:{a}"
    if s.startswith("$") and norm.cashtag(s):
        return f"c:{norm.cashtag(s)}"
    k = norm.keyword(s)
    return f"k:{k}" if k else None


def item_nodes(r):
    nodes = [f"t:{a}" for a in r.get("a") or []] + [f"c:{c}" for c in r.get("c") or []] + \
            [f"k:{k}" for k in r.get("k") or []]
    nodes = sorted(set(nodes))[:MAX_ENTITIES]
    if r.get("bot") and r.get("src"):
        nodes.append(f"s:{r['bot']}:{r['src']}")
    return nodes


def _when(r):
    return r.get("ts") if isinstance(r.get("ts"), (int, float)) else (r.get("seen") or 0)


class KnowledgeGraph:
    def __init__(self, now=None, tau_h=TAU_H):
        self.now = int(now if now is not None else time.time())
        self.tau_h = tau_h
        self.nodes, self.edges = {}, {}

    # -- construcción -----------------------------------------------------------------------------------------
    @classmethod
    def build(cls, records, now=None, tau_h=TAU_H):
        g = cls(now, tau_h)
        for r in records:
            g.add(r)
        return g

    def add(self, r):
        nodes = item_nodes(r)
        if len(nodes) < 1:
            return
        ts = int(_when(r) or self.now)
        w = math.exp(-max(0, self.now - ts) / (self.tau_h * 3600))
        hour = ts // 3600
        for n in nodes:
            d = self.nodes.setdefault(n, {"type": TYPES[n[0]], "count": 0, "weight": 0.0, "last_ts": 0, "hours": {}})
            d["count"] += 1
            d["weight"] += w
            d["last_ts"] = max(d["last_ts"], ts)
            if self.now // 3600 - hour < HOURS_KEPT:
                d["hours"][str(hour)] = d["hours"].get(str(hour), 0) + 1
        for a, b in combinations(sorted(nodes), 2):
            e = self.edges.setdefault((a, b), {"count": 0, "weight": 0.0, "last_ts": 0})
            e["count"] += 1
            e["weight"] += w
            e["last_ts"] = max(e["last_ts"], ts)

    # -- consultas --------------------------------------------------------------------------------------------
    def neighbors(self, node, limit=10, type=None):
        """[(vecino, {count, weight, last_ts})] ordenados por peso. `type`: token / cashtag / keyword / source."""
        n = node_id(node)
        out = []
        for (a, b), e in self.edges.items():
            if n in (a, b):
                other = b if a == n else a
                if type is None or TYPES[other[0]] == type:
                    out.append((other, e))
        out.sort(key=lambda x: (-x[1]["weight"], -x[1]["count"], x[0]))
        return out[:limit] if limit else out

    def co_occurrence(self, a, b):
        x, y = sorted((node_id(a), node_id(b)))
        return dict(self.edges.get((x, y)) or {"count": 0, "weight": 0.0, "last_ts": 0})

    def top_keywords(self, window_h=24, limit=10):
        """[(keyword, menciones en las últimas `window_h` horas)], de más a menos (máx. 48 h)."""
        cur = self.now // 3600
        out = []
        for n, d in self.nodes.items():
            if d["type"] != "keyword":
                continue
            c = sum(v for h, v in d["hours"].items() if cur - int(h) < window_h)
            if c:
                out.append((n[2:], c))
        out.sort(key=lambda x: (-x[1], x[0]))
        return out[:limit] if limit else out

    def related(self, token, limit=10):
        """Tokens a dos saltos vía keywords o cashtags compartidos, con peso Σ w(token–nexo) · w(nexo–otro)."""
        t = node_id(token)
        scores = {}
        for hub, e1 in self.neighbors(t, limit=0):
            if hub[0] not in ("k", "c"):
                continue
            for other, e2 in self.neighbors(hub, limit=0, type="token"):
                if other != t:
                    scores[other] = scores.get(other, 0.0) + e1["weight"] * e2["weight"]
        return sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:limit]

    # -- serialización ----------------------------------------------------------------------------------------
    def to_json(self):
        return {"version": VERSION, "generated_at": self.now, "tau_h": self.tau_h,
                "counts": {t: sum(1 for d in self.nodes.values() if d["type"] == t) for t in TYPES.values()},
                "nodes": {n: {**d, "weight": round(d["weight"], 6)} for n, d in sorted(self.nodes.items())},
                "edges": [{"a": a, "b": b, **{**e, "weight": round(e["weight"], 6)}}
                          for (a, b), e in sorted(self.edges.items())]}

    @classmethod
    def from_json(cls, doc):
        g = cls(doc.get("generated_at"), doc.get("tau_h") or TAU_H)
        g.nodes = {n: dict(d) for n, d in (doc.get("nodes") or {}).items()}
        g.edges = {(e["a"], e["b"]): {k: e[k] for k in ("count", "weight", "last_ts")} for e in doc.get("edges") or []}
        return g


def graph_path(root):
    return Path(root) / "02_Analisis" / "sources" / "_graph.json"


def write_graph(records, now, root):
    """Construye y escribe _graph.json. Devuelve el grafo."""
    g = KnowledgeGraph.build(records, now)
    path = graph_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(path) + ".tmp")
    tmp.write_text(json.dumps(g.to_json(), ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(path)
    return g


def load_graph(root):
    try:
        return KnowledgeGraph.from_json(json.loads(graph_path(root).read_text(encoding="utf-8")))
    except (OSError, ValueError, KeyError):
        return None
