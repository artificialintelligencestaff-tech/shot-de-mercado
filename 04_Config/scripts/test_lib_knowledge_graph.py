#!/usr/bin/env python3
"""Tests de lib_knowledge_graph (patrón #7). unittest, sin red, ítems src-1 sintéticos.

Uso: python 04_Config/scripts/test_lib_knowledge_graph.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_knowledge_graph as kg  # noqa: E402

NOW = 1791000000
MINT_A = "6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump"
MINT_B = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
EVM = "0x532f27101965dd16442e59d40670faf5ebb142e4"


def item(src, ts, a=(), c=(), k=(), bot="rss"):
    return {"v": "src-1", "bot": bot, "src": src, "ts": ts, "a": list(a), "c": list(c), "k": list(k)}


RECORDS = [
    item("gnews", NOW - 600, a=[MINT_A], c=["VSOF"], k=["memecoin", "solana"]),
    item("gnews", NOW - 1200, a=[MINT_A], k=["memecoin"]),
    item("ctg", NOW - 30 * 3600, a=[MINT_B], c=["WIF"], k=["memecoin"]),
    item("ctg", NOW - 40 * 3600, a=[EVM], k=["rwa"]),
    item("tg", NOW - 300, c=["VSOF"], k=["solana"], bot="telegram"),
]


class Grafo(unittest.TestCase):
    def setUp(self):
        self.g = kg.KnowledgeGraph.build(RECORDS, NOW)

    def test_nodos_y_aristas(self):
        self.assertEqual(self.g.nodes[f"t:{MINT_A}"]["count"], 2)
        self.assertEqual(self.g.nodes["k:memecoin"]["count"], 3)
        self.assertEqual(self.g.nodes["s:rss:gnews"]["type"], "source")
        self.assertEqual(self.g.co_occurrence(MINT_A, "memecoin")["count"], 2)
        self.assertEqual(self.g.co_occurrence(MINT_A, "s:rss:gnews")["count"], 2)
        self.assertEqual(self.g.to_json()["counts"], {"token": 3, "cashtag": 2, "keyword": 3, "source": 3})

    def test_peso_junta_frecuencia_y_recencia(self):
        recent = self.g.co_occurrence(MINT_A, "memecoin")                    # 2 menciones de hace minutos
        old = self.g.co_occurrence(MINT_B, "memecoin")                       # 1 mención de hace 30 h
        self.assertAlmostEqual(old["weight"], 2.718281828 ** (-30 / 24), places=6)
        self.assertGreater(recent["weight"], 1.9)
        self.assertEqual(recent["last_ts"], NOW - 600)

    def test_neighbors_ordenados_y_por_tipo(self):
        top = self.g.neighbors("memecoin", limit=3)
        self.assertEqual({n for n, _ in top[:2]}, {f"t:{MINT_A}", "s:rss:gnews"})   # mismos 2 ítems: empate
        self.assertGreaterEqual(top[1][1]["weight"], top[2][1]["weight"])    # orden por peso
        self.assertEqual(self.g.neighbors("memecoin", limit=1, type="token")[0][0], f"t:{MINT_A}")
        tokens = [n for n, _ in self.g.neighbors("Meme Coin", limit=0, type="token")]   # forma cruda: se normaliza
        self.assertEqual(sorted(tokens), sorted([f"t:{MINT_A}", f"t:{MINT_B}"]))

    def test_co_occurrence_simetrica_y_cero(self):
        self.assertEqual(self.g.co_occurrence("$vsof", "solana"), self.g.co_occurrence("solana", "$VSOF"))
        self.assertEqual(self.g.co_occurrence("$vsof", "solana")["count"], 2)
        self.assertEqual(self.g.co_occurrence(MINT_A, EVM), {"count": 0, "weight": 0.0, "last_ts": 0})

    def test_top_keywords_por_ventana(self):
        self.assertEqual(self.g.top_keywords(window_h=2), [("memecoin", 2), ("solana", 2)])
        self.assertEqual(dict(self.g.top_keywords(window_h=48))["memecoin"], 3)
        self.assertEqual(dict(self.g.top_keywords(window_h=48))["rwa"], 1)
        self.assertEqual(self.g.related(MINT_A), [(f"t:{MINT_B}", self.g.related(MINT_A)[0][1])])  # vía 'memecoin'

    def test_json_y_orquestador(self):
        g2 = kg.KnowledgeGraph.from_json(json.loads(json.dumps(self.g.to_json())))
        self.assertEqual(g2.co_occurrence(MINT_A, "memecoin")["count"], 2)
        self.assertEqual(g2.top_keywords(2), self.g.top_keywords(2))
        import bot_orchestrator as orch
        import lib_sources_store as store
        root = Path(tempfile.mkdtemp(prefix="kg_"))
        self.addCleanup(shutil.rmtree, root, True)
        (root / "04_Config" / "sources").mkdir(parents=True)
        (root / "04_Config" / "sources" / "_bots.yaml").write_text("bots:\n  rss: {workflow: x.yml, stale_min: 60}\n",
                                                                   encoding="utf-8")
        recs = [store.make_record("rss", "gnews", "news", f"nuevo memecoin {MINT_A}", ts=NOW - 600, seen=NOW - 500)]
        store.append_records("rss", recs, NOW - 500, root=root)
        doc = orch.run(root, now=NOW)
        self.assertEqual(doc["graph"]["token"], 1)
        loaded = kg.load_graph(root)
        self.assertEqual(loaded.co_occurrence(MINT_A, "memecoin")["count"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
