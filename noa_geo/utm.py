"""Conversión a UTM reutilizando la maquinaria de Gauss-Krüger.

UTM y GK son la misma proyección (transverse Mercator); cambia la
numeración de zonas y el meridiano central.
"""

import math

from .gauss_krueger import A, E2, K0, _arco_meridiano

FALSO_NORTE_SUR = 10000000.0


def zona_utm(lon):
    """Zona UTM (1-60) para una longitud en grados."""
    return int(math.floor((lon + 180.0) / 6.0)) + 1


def meridiano_zona(zona):
    return math.radians(zona * 6.0 - 183.0)


def latlon_a_utm(lat, lon, zona=None):
    """lat/lon -> (este, norte, zona).

    En hemisferio sur se suma el falso norte de 10.000.000 m (fix #5).
    """
    if zona is None:
        zona = zona_utm(lon)
    phi = math.radians(lat)
    lam = math.radians(lon) - meridiano_zona(zona)

    sinp, cosp = math.sin(phi), math.cos(phi)
    t = math.tan(phi)
    n2 = E2 / (1 - E2)
    ep2 = n2 * cosp * cosp
    nu = A / math.sqrt(1 - E2 * sinp * sinp)
    m = _arco_meridiano(phi)

    este = 500000.0 + K0 * nu * (
        lam * cosp
        + lam**3 * cosp**3 / 6 * (1 - t * t + ep2)
        + lam**5 * cosp**5 / 120 * (5 - 18 * t * t + t**4 + 14 * ep2 - 58 * t * t * ep2)
    )
    norte = K0 * (
        m
        + nu * t
        * (
            lam**2 * cosp**2 / 2
            + lam**4 * cosp**4 / 24 * (5 - t * t + 9 * ep2 + 4 * ep2 * ep2)
            + lam**6 * cosp**6 / 720 * (61 - 58 * t * t + t**4)
        )
    )
    if lat < 0:  # hemisferio sur — fix #5
        norte += FALSO_NORTE_SUR
    return este, norte, zona
