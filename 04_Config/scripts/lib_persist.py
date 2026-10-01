#!/usr/bin/env python3
"""
lib_persist.py — Auto-persistencia por operación (Fase 9, T6). Solo biblioteca estándar.

Cada operación significativa deja una línea en 02_Analisis/operations/<operación>.jsonl con: momento, script,
archivos que escribió (con sha256 corto), contadores y la referencia de git/Actions (GITHUB_SHA, GITHUB_RUN_ID).
Un archivo por operación: cada workflow escribe solo el suyo y nunca hay conflictos de rebase entre workflows.

También expone el dataset propio (T5): 02_Analisis/datasets/historical_alerts.jsonl, append-only, una línea por
alerta emitida y una por resultado a 48 h. Lo escriben script_97 y script_98, que comparten el grupo de concurrencia
repo-write-main (corren de a uno), así que el append es seguro.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
OPS_DIR = ROOT / "02_Analisis" / "operations"
DATASETS_DIR = ROOT / "02_Analisis" / "datasets"
HISTORICAL_ALERTS = DATASETS_DIR / "historical_alerts.jsonl"


def _root():
    """SHOT_ROOT se lee en cada llamada: los tests y los workflows lo fijan después de importar."""
    return Path(os.environ.get("SHOT_ROOT") or ROOT)


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def file_digest(path):
    """sha256 corto (16) del archivo, o None si no existe."""
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()[:16]
    except OSError:
        return None


def append_jsonl(path, record):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":"), default=str) + "\n")
    return path


def read_jsonl(path):
    out = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except ValueError:
                        continue
    except OSError:
        pass
    return out


def log_operation(op, script, outputs=(), **counts):
    """Registra una operación. `outputs`: rutas escritas (se guardan relativas a SHOT_ROOT, con su sha256 corto).
    Nunca lanza: la persistencia no puede tumbar la operación que registra."""
    root = _root()
    try:
        files = []
        for p in outputs or ():
            p = Path(p)
            try:
                rel = p.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                rel = str(p)
            files.append({"path": rel, "sha256_16": file_digest(p)})
        record = {"at": now_iso(), "op": op, "script": script, "outputs": files, "counts": counts,
                  "git_sha": os.environ.get("GITHUB_SHA"), "run_id": os.environ.get("GITHUB_RUN_ID"),
                  "workflow": os.environ.get("GITHUB_WORKFLOW")}
        return append_jsonl(root / "02_Analisis" / "operations" / f"{op}.jsonl", record)
    except Exception as e:      # noqa: BLE001
        print(f"[WARN] lib_persist.log_operation({op}): {type(e).__name__}: {e}")
        return None


def historical_path():
    return _root() / "02_Analisis" / "datasets" / "historical_alerts.jsonl"


def record_alert(alert, components=None, reasons=None, source="script_97"):
    """Una línea 'alert' del dataset propio. `alert` = registro de _all_alerts.json."""
    rec = {"type": "alert", "at": now_iso(), "source": source,
           "key": alert.get("asset_key") or alert.get("mint"), "mint": alert.get("mint"),
           "timestamp": alert.get("timestamp"), "symbol": alert.get("symbol"), "chain": alert.get("chain") or "solana",
           "group": alert.get("group") or "a", "scoring_version": alert.get("scoring_version"),
           "score": alert.get("score"), "initial_price": alert.get("initial_price"), "status": alert.get("status"),
           "telegram_sent": alert.get("telegram_sent"), "reasons": list(reasons or [])[:12],
           "components": [{k: c.get(k) for k in ("name", "s", "w", "value")} for c in (components or [])]}
    try:
        return append_jsonl(historical_path(), rec)
    except Exception as e:      # noqa: BLE001
        print(f"[WARN] historical_alerts (alert): {type(e).__name__}: {e}")
        return None


def record_outcome(alert, price_now, horizon_h=48, source="script_98"):
    """Una línea 'outcome' del dataset propio: precio a ~48 h contra la entrada (métrica secundaria del doc 19)."""
    p0 = alert.get("initial_price")
    change = (price_now / p0 - 1) * 100 if p0 and price_now else None
    rec = {"type": "outcome", "at": now_iso(), "source": source, "horizon_h": horizon_h,
           "key": alert.get("asset_key") or alert.get("mint"), "timestamp": alert.get("timestamp"),
           "symbol": alert.get("symbol"), "group": alert.get("group") or "a", "initial_price": p0,
           "price": price_now, "change_pct": round(change, 4) if change is not None else None,
           "secondary_hit": (change is not None and change >= 20.0),
           "trust_updates": [{k: u.get(k) for k in ("stage", "price", "change_pct", "timestamp") if k in u}
                             for u in alert.get("trust_updates") or []]}
    try:
        return append_jsonl(historical_path(), rec)
    except Exception as e:      # noqa: BLE001
        print(f"[WARN] historical_alerts (outcome): {type(e).__name__}: {e}")
        return None
