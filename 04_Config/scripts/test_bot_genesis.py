#!/usr/bin/env python3
"""Tests del bot padre (Ola 3): bot_genesis. unittest, sin red (HTTP simulado).

Uso: python 04_Config/scripts/test_bot_genesis.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_genesis as gen  # noqa: E402
import bot_runner as br  # noqa: E402

T0 = 1791000000
FICHA = """# DexPaprika

**Licencia:** MIT

```yaml
recipe:
  kind: json_api
  url_base: https://api.dexpaprika.com/networks/solana/pools/search?limit=50
  cadencia_min: 30
  extractores:
    - items: "$.results[*]"
    - id: "$.id"
  grupo: a
```
"""
RSS_YAML = 'feeds:\n  - {name: cointelegraph_solana, url: "https://cointelegraph.com/rss/tag/solana"}\n'
TG_YAML = "channels:\n  - {name: pumpfun}\n"


def pools(n):
    return json.dumps({"results": [{"id": f"P{i}"} for i in range(n)]})


class FakeHTTP:
    def __init__(self, body, status=200):
        self.body, self.status, self.calls = body, status, []

    def __call__(self, url, headers=None):
        self.calls.append(url)
        return self.status, (self.body if self.status == 200 else None), url


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="genesis_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        (self.root / "_servicios_open_source/03_data_blockchain").mkdir(parents=True)
        (self.root / "04_Config/sources").mkdir(parents=True)
        (self.root / "04_Config/sources/rss.yaml").write_text(RSS_YAML, encoding="utf-8")
        (self.root / "04_Config/sources/telegram.yaml").write_text(TG_YAML, encoding="utf-8")

    def ficha(self, name, text):
        (self.root / "_servicios_open_source/03_data_blockchain" / f"{name}.md").write_text(text, encoding="utf-8")

    def manual(self, name, recipe):
        import yaml
        d = self.root / br.RECIPES_REL
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{name}.yaml").write_text(yaml.safe_dump(recipe), encoding="utf-8")

    def run_gen(self, http, now=T0, env=None):
        return gen.run(self.root, now=now, fetch=http, env=env or {})["recipes"]


class Genesis(Base):
    def test_ficha_con_bloque_genera_receta_y_la_habilita(self):
        self.ficha("dexpaprika", FICHA)
        self.ficha("sin_bloque", "# Otra ficha\n\nsin receta\n")
        st = self.run_gen(FakeHTTP(pools(7)))
        path = self.root / br.RECIPES_REL / "dexpaprika.yaml"
        self.assertTrue(path.read_text(encoding="utf-8").startswith(gen.GENERATED))
        self.assertEqual(br.load_recipe(path)["name"], "dexpaprika")
        self.assertEqual((st["dexpaprika"]["enabled"], st["dexpaprika"]["status"], st["dexpaprika"]["items"]),
                         (True, "enabled", 7))
        self.assertEqual(st["dexpaprika"]["since"], T0)
        self.assertNotIn("sin_bloque", st)
        self.assertEqual(br.plan(self.root, now=T0), ["dexpaprika"])                   # el runner ya la ve

    def test_falla_va_a_probation_con_motivo(self):
        self.ficha("dexpaprika", FICHA)
        st = self.run_gen(FakeHTTP(pools(3)))
        self.assertEqual((st["dexpaprika"]["enabled"], st["dexpaprika"]["status"]), (False, "probation"))
        self.assertIn("3 ítems (< 5)", st["dexpaprika"]["reason"])
        st = self.run_gen(FakeHTTP(None, status=403))
        self.assertIn("HTTP 403", st["dexpaprika"]["reason"])
        self.manual("helius_free", {"name": "helius_free", "kind": "json_api", "cadencia_min": 60,
                                    "secreto": "HELIUS_API_KEY", "url_base": "https://api.helius.xyz/v0/x?api-key={secreto}",
                                    "extractores": {"items": "$[*]", "id": "$.signature"}})
        http = FakeHTTP(pools(9))
        st = self.run_gen(http)
        self.assertIn("falta el secret HELIUS_API_KEY", st["helius_free"]["reason"])
        self.assertFalse(any("helius" in u for u in http.calls))                       # sin secret ni siquiera prueba

    def test_dominio_duplicado(self):
        self.manual("ct_extra", {"name": "ct_extra", "kind": "rss", "cadencia_min": 20,
                                 "url_base": "https://www.cointelegraph.com/rss/tag/memecoin"})
        self.manual("tg_pump", {"name": "tg_pump", "kind": "telegram_preview", "cadencia_min": 30,
                                "url_base": "https://t.me/s/pumpfun"})
        self.manual("tg_otro", {"name": "tg_otro", "kind": "telegram_preview", "cadencia_min": 30,
                                "url_base": "https://t.me/s/otro_canal"})
        self.ficha("dexpaprika", FICHA)
        self.manual("dexp_bis", {"name": "dexp_bis", "kind": "json_api", "cadencia_min": 30,
                                 "url_base": "https://api.dexpaprika.com/networks/base/pools/search",
                                 "extractores": {"items": "$.results[*]", "id": "$.id"}})
        st = self.run_gen(FakeHTTP(pools(6)))
        self.assertIn("ya lo cubre rss:cointelegraph_solana", st["ct_extra"]["reason"])
        self.assertIn("ya lo cubre telegram:pumpfun", st["tg_pump"]["reason"])
        self.assertIn("ya lo cubre receta:dexp_bis", st["dexpaprika"]["reason"])        # alfabético: dexp_bis < dexpaprika
        self.assertTrue(st["dexp_bis"]["enabled"])
        self.assertNotIn("dominio", st["tg_otro"]["reason"] or "")                       # otro canal de t.me: sin choque

    def test_esquema_invalido_y_receta_manual_no_se_pisa(self):
        self.ficha("roto", FICHA.replace("cadencia_min: 30", "cadencia_min: 2").replace('    - id: "$.id"\n', ""))
        self.manual("dexpaprika", {"name": "dexpaprika", "kind": "json_api", "cadencia_min": 45,
                                   "url_base": "https://api.dexpaprika.com/networks/solana/pools/search",
                                   "extractores": {"items": "$.results[*]", "id": "$.id"}})
        self.ficha("dexpaprika", FICHA)
        st = self.run_gen(FakeHTTP(pools(8)))
        self.assertIn("esquema", st["roto"]["reason"])
        self.assertIn("cadencia_min < 10", st["roto"]["reason"])
        self.assertIn("extractores.id es obligatorio", st["roto"]["reason"])
        manual = (self.root / br.RECIPES_REL / "dexpaprika.yaml").read_text(encoding="utf-8")
        self.assertFalse(manual.startswith(gen.GENERATED))                              # la manual sigue igual
        self.assertTrue(st["dexpaprika"]["enabled"])
        self.assertIn("receta manual", st["dexpaprika"]["note"])

    def test_dos_strikes_retiro_e_idempotencia(self):
        self.ficha("dexpaprika", FICHA)
        self.run_gen(FakeHTTP(pools(6)))
        recipe = self.root / br.RECIPES_REL / "dexpaprika.yaml"
        mtime = recipe.stat().st_mtime_ns
        st = self.run_gen(FakeHTTP(None, status=503), now=T0 + 86400)                  # 1.ª falla: sigue habilitada
        self.assertEqual((st["dexpaprika"]["enabled"], st["dexpaprika"]["strikes"]), (True, 1))
        self.assertEqual(recipe.stat().st_mtime_ns, mtime)                               # misma ficha: no reescribe
        st = self.run_gen(FakeHTTP(None, status=503), now=T0 + 2 * 86400)              # 2.ª: probation
        self.assertEqual((st["dexpaprika"]["enabled"], st["dexpaprika"]["status"]), (False, "probation"))
        st = self.run_gen(FakeHTTP(pools(6)), now=T0 + 3 * 86400)                       # se recupera
        self.assertEqual((st["dexpaprika"]["enabled"], st["dexpaprika"]["strikes"], st["dexpaprika"]["since"]),
                         (True, 0, T0 + 3 * 86400))
        self.ficha("dexpaprika", "# DexPaprika\n\n(el bloque se quitó)\n")
        doc = gen.run(self.root, now=T0 + 4 * 86400, fetch=FakeHTTP(pools(6)), env={})
        self.assertFalse(recipe.exists())                                                # receta generada retirada
        self.assertEqual((doc["recipes"], doc["retired"]), ({}, ["dexpaprika"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
