#!/usr/bin/env python3
"""Tests del colector de menciones (script_115, doc 26 Fase 0). unittest, sin red: HTTP simulado.

Uso: python 04_Config/scripts/test_script_115_collector.py
"""
import hashlib
import json
import math
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

TMP = tempfile.mkdtemp(prefix="s115_")
os.environ["SHOT_ROOT"] = TMP
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_repetition as rep  # noqa: E402
import script_115_narrative_collector as c  # noqa: E402

NOW = datetime(2026, 10, 1, 15, 0, tzinfo=timezone.utc).timestamp()
MINT = "4vEX32B4LLr2hL4tzdgz724rSYXGccAGT8MRSUaNpump"          # DEGEN (alerta real del 01/10)
MINT2 = "61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump"         # arc
EVM = "0xAbCdEf0123456789abcdef0123456789ABCDEF01"


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat(timespec="seconds")


def acc_record(mint, symbol, name, score, minutes_ago, version="7.2.1"):
    return {"source": "pumpportal", "token": {"mint": mint, "symbol": symbol, "name": name},
            "score": score, "detected_at": iso(NOW - minutes_ago * 60), "scoring_version": version}


class FakeResp:
    def __init__(self, status, text="", data=None):
        self.status_code, self.text, self._data = status, text, data

    def json(self):
        if self._data is None:
            raise ValueError("no json")
        return self._data


class FakeSession:
    """Responde por fragmento de URL; lo que no está en las rutas devuelve 404."""

    def __init__(self, routes):
        self.routes, self.urls, self.headers = routes, [], []

    def get(self, url, headers=None, timeout=None):
        self.urls.append(url)
        self.headers.append(headers)
        for key, resp in self.routes.items():
            if key in url:
                if isinstance(resp, Exception):
                    raise resp
                return resp
        return FakeResp(404)


def atom(entries):
    body = "".join(f"<entry><author><name>{a}</name></author><id>{i}</id><title>{t}</title>"
                   f"<updated>{iso(ts)}</updated></entry>" for i, (a, t, ts) in enumerate(entries))
    return f'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">{body}</feed>'


def telegram(channel, messages):
    body = "".join(f'<div class="tgme_widget_message" data-post="{channel}/{i}"><div class="tgme_widget_message_text">'
                   f'{t}</div><time datetime="{iso(ts)}"></time></div>' for i, (t, ts) in enumerate(messages))
    return f"<html><body>{body}</body></html>"


def routes_for_run():
    return {
        "reddit.com/r/solana": FakeResp(200, atom([("/u/alice", f"CA {MINT} sending", NOW - 600),
                                                   ("/u/bob", "nothing to see here", NOW - 700)])),
        "reddit.com/r/CryptoMoonShots": FakeResp(429),
        "t.me/s/pumpfun": FakeResp(200, telegram("pumpfun", [("$DEGEN otter is back", NOW - 300),
                                                               (f"Degen Otter live: {MINT}", NOW - 1200)])),
        "a.4cdn.org": FakeResp(200, data=[{"threads": [{"no": 1, "time": int(NOW - 900), "sub": "gem",
                                                        "com": f"ca {MINT}"}]}]),
        "hn.algolia.com": FakeResp(200, data={"hits": []}),
        "coindesk.com": FakeResp(200, "<html>not xml"),          # 200 que no se puede parsear
        "coingecko.com": FakeResp(200, data={"coins": [{"item": {"id": "degen-otter", "symbol": "degen",
                                                                 "name": "Degen Otter", "market_cap_rank": None}}]}),
    }


class IdentifiersTest(unittest.TestCase):
    def test_extrae_direcciones_y_cashtags(self):
        text = (f"buy {MINT} and {EVM} now $DEGEN $wif $100 $ 5 https://pump.fun/coin/{MINT2} "
                f"tx 0x{'ab' * 32} ipfs Qm{'a' * 44} pay$ME")
        addresses, cashtags = c.extract_identifiers(text)
        self.assertEqual(addresses, sorted([MINT, MINT2, EVM.lower()]))   # EVM en minúsculas; hash de tx afuera
        self.assertEqual(cashtags, ["DEGEN", "WIF"])                      # $100 no es cashtag; pay$ME tampoco

    def test_paridad_con_lib_repetition_match_weight(self):
        token = {"key": MINT, "address": MINT, "cashtag": "DEGEN", "name_match": "Degen Otter"}
        pattern = c.name_pattern("Degen Otter")
        for text in [f"ca: {MINT}", "$degen to the moon", "the degen otter army", "degen otter", "$DEGENX",
                     "sin nada", f"$DEGEN y {MINT}", "Degen Otters"]:
            addresses, cashtags = c.extract_identifiers(text)
            item = {"a": addresses, "c": cashtags, "n": [MINT] if pattern.search(text) else []}
            self.assertEqual(c.item_weight(item, token), rep.match_weight(text, MINT, "DEGEN", "Degen Otter"), text)

    def test_hash_de_autor_sin_handle(self):
        h = c.author_hash("/u/Alice")
        self.assertEqual(len(h), 12)
        self.assertEqual(h, c.author_hash("/u/alice "))
        self.assertNotIn("alice", h)
        self.assertIsNone(c.author_hash(None))

    def test_user_agent_ascii(self):
        c.HEADERS["User-Agent"].encode("ascii")

    def test_evm_no_confunde_con_base58(self):
        """EVM address 0x + 40 hex no debe producir falso positivo base58."""
        # EVM correcto: 0x + 40 hex = 42 chars total
        evm = "0x" + "AB" * 20
        addr, ct = c.extract_identifiers(evm)
        # Solo debe detectar la dirección EVM, ninguna base58
        self.assertEqual(addr, [evm.lower()])
        # Caso: EVM + Solana en mismo texto
        sol = "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"
        text = f"{evm} and {sol}"
        addr, ct = c.extract_identifiers(text)
        evm_found = [a for a in addr if a.startswith("0x")]
        sol_found = [a for a in addr if not a.startswith("0x")]
        self.assertEqual(evm_found, [evm.lower()])
        self.assertEqual(sol_found, [sol])
        # Caso: múltiples EVM
        text2 = f"{evm} 0x{'CD' * 20}"
        addr, ct = c.extract_identifiers(text2)
        self.assertEqual(len(addr), 2)
        self.assertTrue(all(a.startswith("0x") for a in addr))


class CandidatesTest(unittest.TestCase):
    def test_umbral_ventana_y_version_vigente(self):
        acc = {MINT: acc_record(MINT, "DEGEN", "Degen Otter", 100, 10),
               MINT2: acc_record(MINT2, "arc", "AI Rig Complex", 40, 60),
               "Low1111111111111111111111111111111111111": acc_record("x", "LOW", "Low Coin", 39, 5),
               "Old1111111111111111111111111111111111111": acc_record("x", "OLD", "Old Coin", 90, 49 * 60),
               "V72x111111111111111111111111111111111111": acc_record("x", "INF", "Inflated", 100, 30, "7.2")}
        tracked, stats = c.select_tracked(acc, {}, NOW)
        self.assertEqual(sorted(tracked), sorted([MINT, MINT2]))
        self.assertEqual((stats["new"], stats["other_version"], stats["scoring_version"]), (2, 1, "7.2.1"))
        self.assertEqual(tracked[MINT]["first_tracked_at"], iso(NOW))

    def test_se_sigue_48h_desde_la_entrada_aunque_baje_el_score(self):
        acc = {MINT: acc_record(MINT, "DEGEN", "Degen Otter", 10, 5)}
        prev = {MINT: {"first_tracked_at": iso(NOW - 47 * 3600), "address": MINT, "symbol": "DEGEN"},
                MINT2: {"first_tracked_at": iso(NOW - 48 * 3600), "address": MINT2, "symbol": "arc"}}
        tracked, stats = c.select_tracked(acc, prev, NOW)
        self.assertEqual(list(tracked), [MINT])
        self.assertEqual((stats["kept"], stats["expired"]), (1, 1))
        self.assertEqual(tracked[MINT]["score"], 10)                       # se refresca desde el acumulado

    def test_exclusiones_de_cashtag_y_nombre(self):
        names = {"degen otter": 1, "pepe coin": 2}
        t = c.describe_token(MINT, {"address": MINT, "symbol": "SOL", "name": "Pepe Coin", "chain": "solana"}, names)
        self.assertIsNone(t["cashtag"])
        self.assertIn("lista de exclusión", t["excluded"]["cashtag"])
        self.assertIsNone(t["name_match"])
        self.assertIn("compartido por 2", t["excluded"]["name"])
        t = c.describe_token(MINT, {"address": MINT, "symbol": "C@T", "name": "blob", "chain": "solana"}, names)
        self.assertIsNone(t["cashtag"])
        self.assertIn("menos de 2 palabras", t["excluded"]["name"])
        t = c.describe_token(MINT, {"address": MINT, "symbol": "degen", "name": "Degen Otter", "chain": "solana"}, names)
        self.assertEqual((t["cashtag"], t["name_match"], t["excluded"]), ("DEGEN", "Degen Otter", {}))

    def test_tope_por_score_y_clave_evm_normalizada(self):
        acc = {f"{chr(65 + i)}{'1' * 39}": acc_record("x", f"T{i}", f"Token {i}", 40 + i, 5) for i in range(5)}
        acc[EVM] = acc_record(EVM, "EVMT", "Evm Token", 99, 5)
        tracked, stats = c.select_tracked(acc, {}, NOW, cap=3)
        self.assertEqual(len(tracked), 3)
        self.assertIn(EVM.lower(), tracked)
        self.assertEqual(stats["capped"], 3)
        self.assertEqual(min(t["score"] for t in tracked.values()), 43)


class StoreTest(unittest.TestCase):
    def tokens(self):
        names = {"degen otter": 1}
        t = c.describe_token(MINT, {"address": MINT, "symbol": "DEGEN", "name": "Degen Otter", "chain": "solana"}, names)
        return {MINT: t}

    def raw(self, text, ts, source="r/solana", author="/u/alice"):
        return {"source": source, "family": "reddit_rss", "id": "x", "ts": ts, "text": text, "author": author}

    def test_dedup_privacidad_y_filtros(self):
        store = []
        raws = [self.raw(f"CA {MINT}", NOW - 60), self.raw(f"ca  {MINT} https://x.y", NOW - 50),   # mismo texto normalizado
                self.raw(f"CA {MINT}", NOW - 40, source="t.me/s/pumpfun"),                         # otra fuente: cuenta
                self.raw("sin identificadores", NOW - 30), self.raw(f"CA {MINT}", None),
                self.raw(f"futuro {MINT}", NOW + 3600), self.raw(f"viejo {MINT}", NOW - 27 * 3600)]
        stats = c.ingest(store, raws, self.tokens(), NOW)
        self.assertEqual((stats["added"], stats["seen"], stats["with_ids"]), (2, 4, 3))   # sin ts, futuro y viejo no se ven
        dump = json.dumps(store)
        for secret in ("alice", "CA ", "https://x.y"):
            self.assertNotIn(secret, dump)                                  # sin textos ni handles
        self.assertEqual(set(store[0]), {"k", "s", "f", "ts", "a", "c", "n", "u"})

    def test_nombre_retroactivo_mientras_el_item_sigue_en_el_feed(self):
        store = []
        c.ingest(store, [self.raw("the degen otter army $XYZ", NOW - 600)], {}, NOW)
        self.assertEqual(store[0]["n"], [])
        stats = c.ingest(store, [self.raw("the degen otter army $XYZ", NOW - 600)], self.tokens(), NOW)
        self.assertEqual((stats["added"], stats["updated"], store[0]["n"]), (0, 1, [MINT]))

    def test_prune_26h(self):
        store = [{"k": "a", "ts": NOW - 25 * 3600}, {"k": "b", "ts": NOW - 26 * 3600 - 1}]
        kept, pruned = c.prune(store, NOW)
        self.assertEqual(([i["k"] for i in kept], pruned), (["a"], 1))

    def test_snapshot_reproduce_caso_c_del_doc_26(self):
        # Caso C (doc 26 §3.3): 6 menciones de contrato en la última hora, sin historia -> ratio 7,0, p = 2,7e-7.
        token = self.tokens()[MINT]
        store = [{"k": f"s{i}|h", "s": f"src{i % 3}", "ts": NOW - 300 - i, "a": [MINT], "c": [], "n": [], "u": None}
                 for i in range(6)]
        snap = c.token_snapshot(token, store, NOW)
        self.assertAlmostEqual(snap["m_1h"], 6.0)
        self.assertAlmostEqual((snap["m_1h"] + 1) / (snap["m_24h_mean"] + 1), 7.0)
        self.assertAlmostEqual(math.exp(-snap["surprise_nats"]), 2.7e-7, delta=0.05e-7)
        self.assertEqual(snap["mentions_by_match_26h"], {"ca": 6})
        self.assertEqual(snap["by_source_1h"], {"src0": 2.0, "src1": 2.0, "src2": 2.0})
        found = [{"ts": it["ts"], "source": it["s"], "weight": 1.0, "author": None} for it in store]
        expected = rep.repetition_snapshot(found, NOW)
        self.assertEqual({k: snap[k] for k in expected}, expected)        # misma fórmula que la librería


class FamiliesTest(unittest.TestCase):
    def test_familias_de_la_sonda_y_gdelt_nunca(self):
        report = {"runner": "github-actions", "generated_at": "x",
                  "families": {"reddit_rss": {"ok": True}, "gdelt": {"ok": True}, "hn_algolia": {"ok": False},
                               "4chan_biz": {"ok": True}}}
        used, skipped, origin = c.select_families(report)
        self.assertEqual(used, ["reddit_rss", "4chan_biz"])
        self.assertIn("gdelt", skipped)
        self.assertIn("hn_algolia", skipped)
        self.assertIn("github-actions", origin)

    def test_sin_sonda_usa_todas_menos_gdelt_y_cli_valida(self):
        used, _, origin = c.select_families(None)
        self.assertNotIn("gdelt", used)
        self.assertEqual(len(used), len(c.probe.SOURCES) - 1)
        self.assertEqual(origin, "sin sonda: todas")
        with self.assertRaises(ValueError):
            c.select_families(None, ["twitter"])


class RunTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="run_", dir=TMP))
        self.acc = self.root / "acc.json"
        self.acc.write_text(json.dumps({MINT: acc_record(MINT, "DEGEN", "Degen Otter", 100, 30),
                                        MINT2: acc_record(MINT2, "arc", "AI Rig Complex", 72, 30),
                                        "Low1111111111111111111111111111111111111": acc_record("x", "L", "Low", 20, 5)}),
                            encoding="utf-8")
        self.probe = self.root / "probe.json"
        self.probe.write_text(json.dumps({"runner": "github-actions", "generated_at": "t", "families": {
            f: {"ok": f != "gdelt"} for f in c.probe.SOURCES}}), encoding="utf-8")
        self.out = self.root / "narrative"

    def run_once(self, now=NOW, routes=None, dry_run=False):
        self.session = FakeSession(routes if routes is not None else routes_for_run())
        return c.run(session=self.session, now=now, sleep=lambda s: None, accumulated_file=self.acc,
                     probe_file=self.probe, out_dir=self.out, dry_run=dry_run)

    def test_corrida_completa_escribe_solo_narrative(self):
        acc_hash = hashlib.sha256(self.acc.read_bytes()).hexdigest()
        index = self.run_once()
        self.assertEqual(hashlib.sha256(self.acc.read_bytes()).hexdigest(), acc_hash)   # el acumulado no se toca
        self.assertEqual(sorted(p.name for p in self.out.iterdir()),
                         sorted([f"{MINT}.json", f"{MINT2}.json", "_items.json", "_index.json"]))
        self.assertFalse(any("gdelt" in u for u in self.session.urls))
        doc = json.loads((self.out / f"{MINT}.json").read_text(encoding="utf-8"))
        snap = doc["snapshot"]
        # r/solana CA (1,0) + t.me cashtag (0,5) + t.me nombre y CA en el mismo mensaje (1,0) + 4chan CA (1,0)
        self.assertAlmostEqual(snap["m_1h"], 3.5)
        self.assertEqual(snap["mentions_by_match_26h"], {"ca": 3, "cashtag": 1})
        self.assertEqual(doc["coingecko_trending"], {"rank": 1, "id": "degen-otter"})
        self.assertEqual(doc["identifiers"]["cashtag"], "$DEGEN")
        self.assertEqual(len(doc["history"]), 1)
        self.assertEqual(doc["token"]["scoring_version"], "7.2.1")
        rows = {r["name"]: r for r in index["sources"]}
        self.assertEqual(rows["r/CryptoMoonShots"]["status"], 429)
        self.assertIn("parse_error", rows["CoinDesk"])
        self.assertEqual(index["store"]["baseline_coverage_h"], 0.0)
        self.assertEqual(index["summary"][0]["key"], MINT)
        for h in self.session.headers:
            h["User-Agent"].encode("ascii")

    def test_segunda_corrida_no_duplica_y_conserva_la_primera_foto(self):
        self.run_once()
        first = json.loads((self.out / f"{MINT}.json").read_text(encoding="utf-8"))["first_snapshot"]
        index = self.run_once(now=NOW + 1200)
        doc = json.loads((self.out / f"{MINT}.json").read_text(encoding="utf-8"))
        self.assertEqual(index["store"]["added"], 0)
        self.assertEqual(len(doc["history"]), 2)
        self.assertEqual(doc["first_snapshot"], first)
        self.assertEqual(len(index["runs"]), 2)
        self.assertAlmostEqual(index["store"]["baseline_coverage_h"], 0.33)

    def test_historial_de_24h(self):
        self.run_once()
        self.run_once(now=NOW + 25 * 3600, routes={})
        doc = json.loads((self.out / f"{MINT}.json").read_text(encoding="utf-8"))
        self.assertEqual(len(doc["history"]), 1)                            # la entrada de hace 25 h se descarta
        self.assertEqual(doc["first_snapshot"]["at"], iso(NOW))

    def test_sin_red_no_falla(self):
        import requests
        index = self.run_once(routes={"": requests.ConnectionError("sin red")})
        self.assertTrue(all(str(s["status"]).startswith("error") for s in index["sources"]))
        self.assertEqual(index["store"]["items"], 0)

    def test_dry_run_no_escribe(self):
        self.run_once(dry_run=True)
        self.assertFalse(self.out.exists())

    def test_main_rechaza_familia_desconocida(self):
        with self.assertRaises(SystemExit):
            c.main(["--families", "twitter", "--dry-run"])


def tearDownModule():
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
