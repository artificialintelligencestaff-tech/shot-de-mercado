#!/usr/bin/env python3
"""
lib_alerts.py — dominio de alertas (D-105). Única puerta de lectura/escritura de 02_Analisis/alerts/ para los
consumidores (script_97, script_98, script_116, early_review). Si cambia el esquema de _all_alerts.json se cambia
acá y los consumidores no se tocan.

  SCHEMA_VERSION                  versión del contrato de _all_alerts.json (lista de registros)
  read_alerts(path=None, strict=True)   [] si no existe; ilegible o no-lista: CorruptAlertsError (strict) o []
  write_alerts(alerts, path=None) escritura atómica, mismo formato de siempre (indent=2, ASCII)
  write_alert(record, path=None)  agrega un registro y persiste; devuelve la lista
  detail_path(name, ts) · read_detail(name, ts, default) · write_detail(name, ts, data, ensure_ascii=True); root= opcional
  trust_path(name) · write_trust(name, updates)
Solo biblioteca estándar.
"""
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_paths as P  # noqa: E402

SCHEMA_VERSION = "alerts-1"
REQUIRED = ("mint", "timestamp")


class CorruptAlertsError(Exception):
    """El historial de alertas existe pero no se puede leer: no se lo pisa con una lista vacía."""


def all_path(root=None):
    return P.path("alerts.all", root)


def alerts_dir(root=None):
    return P.path("alerts.dir", root)


def read_alerts(path=None, strict=True):
    path = Path(path or all_path())
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        if strict:
            raise CorruptAlertsError(f"{path}: {e}") from e
        return []
    if not isinstance(data, list):
        if strict:
            raise CorruptAlertsError(f"{path}: se esperaba una lista, llegó {type(data).__name__}")
        return []
    return data


def write_json_atomic(path, data, **dump):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, **dump)
    os.replace(tmp, path)


def write_alerts(alerts, path=None):
    if not isinstance(alerts, list):
        raise TypeError("write_alerts: se espera una lista de registros")
    write_json_atomic(path or all_path(), alerts)


def write_alert(record, path=None):
    missing = [k for k in REQUIRED if not record.get(k)]
    if missing:
        raise ValueError(f"write_alert: faltan {missing}")
    alerts = read_alerts(path)
    alerts.append(record)
    write_alerts(alerts, path)
    return alerts


def _safe(name):
    return re.sub(r"[^A-Za-z0-9]+", "_", str(name))


def detail_path(name, ts, safe=False, root=None):
    return P.path("alerts.detail", root, mint=_safe(name) if safe else name, ts=ts)


def read_detail(name, ts, default=None, root=None):
    try:
        return json.loads(detail_path(name, ts, root=root).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_detail(name, ts, data, ensure_ascii=True, safe=False, root=None):
    p = detail_path(name, ts, safe, root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=ensure_ascii)
    return p


def trust_path(name, root=None):
    return P.path("alerts.trust", root, mint=_safe(name))


def write_trust(name, updates, root=None):
    p = trust_path(name, root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        json.dump(updates, f, indent=2)
    return p
