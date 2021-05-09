"""Carga y búsqueda de la base de localidades del NOA."""

import csv
import unicodedata
from dataclasses import dataclass
from pathlib import Path

DATA = Path(__file__).parent / "data" / "localidades_noa.csv"


@dataclass
class Localidad:
    nombre: str
    provincia: str
    lat: float
    lon: float
    faja: int


def _norm(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn"
    )


def cargar(path=None):
    """Devuelve la lista de localidades del CSV."""
    path = Path(path) if path else DATA
    out = []
    with open(path, encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if not row or row[0].startswith("#"):
                continue
            out.append(Localidad(row[0], row[1], float(row[2]), float(row[3]), int(row[4])))
    return out


def buscar(nombre, localidades=None):
    """Búsqueda difusa (substring sin tildes) sobre la base."""
    locs = localidades if localidades is not None else cargar()
    q = _norm(nombre)
    return [l for l in locs if q in _norm(l.nombre)]
