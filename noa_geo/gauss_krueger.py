"""Conversión lat/lon <-> Gauss-Krüger sobre POSGAR 94 (~WGS84).

Antes era `posgar.py`; quedó un shim con DeprecationWarning por
compatibilidad hasta la 0.3.
"""

import math

A = 6378137.0
F_INV = 298.257223563
F = 1.0 / F_INV
E2 = F * (2 - F)
K0 = 0.9996
FALSO_ESTE = 500000.0
FALSO_NORTE_SUR = 10000000.0

MERIDIANOS = {1: -72.0, 2: -69.0, 3: -66.0, 4: -63.0}


def meridiano_central(faja):
    if faja not in MERIDIANOS:
        raise ValueError("faja %r no soportada (1-4)" % faja)
    return math.radians(MERIDIANOS[faja])


def _arco_meridiano(phi):
    e4, e6 = E2 * E2, E2 * E2 * E2
    return A * (
        (1 - E2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * phi
        - (3 * E2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * phi)
        + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * phi)
        - (35 * e6 / 3072) * math.sin(6 * phi)
    )


def latlon_a_gk(lat, lon, faja=3):
    """lat/lon (grados) -> (este, norte) en metros GK.

    Cerca del borde entre fajas la serie diverge un poco — elegir la
    faja con `faja_para_lon` (oct-2022).
    """
    phi = math.radians(lat)
    lam = math.radians(lon) - meridiano_central(faja)

    sinp, cosp = math.sin(phi), math.cos(phi)
    t = math.tan(phi)
    n2 = E2 / (1 - E2)
    ep2 = n2 * cosp * cosp
    nu = A / math.sqrt(1 - E2 * sinp * sinp)
    m = _arco_meridiano(phi)

    este = FALSO_ESTE + K0 * nu * (
        lam * cosp
        + lam**3 * cosp**3 / 6 * (1 - t * t + ep2)
        + lam**5 * cosp**5 / 120 * (5 - 18 * t * t + t**4 + 14 * ep2 - 58 * t * t * ep2)
    )
    norte = FALSO_NORTE_SUR + K0 * (
        m
        + nu * t
        * (
            lam**2 * cosp**2 / 2
            + lam**4 * cosp**4 / 24 * (5 - t * t + 9 * ep2 + 4 * ep2 * ep2)
            + lam**6 * cosp**6 / 720 * (61 - 58 * t * t + t**4)
        )
    )
    # redondeo half-up a 4 decimales (mm de sobra para nosotros)
    return round(este, 4), round(norte, 4)


def gk_a_latlon(este, norte, faja=3):
    """(este, norte) GK -> (lat, lon) en grados. Iteración simple."""
    m = (norte - FALSO_NORTE_SUR) / K0
    mu = m / (A * (1 - E2 / 4 - 3 * E2 * E2 / 64 - 5 * E2**3 / 256))

    e1 = (1 - math.sqrt(1 - E2)) / (1 + math.sqrt(1 - E2))
    phi = (
        mu
        + (3 * e1 / 2 - 27 * e1**3 / 32) * math.sin(2 * mu)
        + (21 * e1**2 / 16 - 55 * e1**4 / 32) * math.sin(4 * mu)
        + (151 * e1**3 / 96) * math.sin(6 * mu)
        + (1097 * e1**4 / 512) * math.sin(8 * mu)
    )

    sinp, cosp = math.sin(phi), math.cos(phi)
    t = math.tan(phi)
    n2 = E2 / (1 - E2)
    ep2 = n2 * cosp * cosp
    nu = A / math.sqrt(1 - E2 * sinp * sinp)
    rho = A * (1 - E2) / (1 - E2 * sinp * sinp) ** 1.5
    d = (este - FALSO_ESTE) / (nu * K0)

    lat = phi - (nu * t / rho) * (
        d**2 / 2
        - d**4 / 24 * (5 + 3 * t * t + 10 * ep2 - 4 * ep2 * ep2 - 9 * n2)
        + d**6 / 720 * (61 + 90 * t * t + 298 * ep2 + 45 * t**4 - 252 * n2 - 3 * ep2 * ep2)
    )
    lon = meridiano_central(faja) + (
        d
        - d**3 / 6 * (1 + 2 * t * t + ep2)
        + d**5 / 120 * (5 - 2 * ep2 + 28 * t * t - 3 * ep2 * ep2 + 8 * n2 + 24 * t**4)
    ) / cosp
    return math.degrees(lat), math.degrees(lon)


def faja_para_lon(lon):
    if lon <= -67.5:
        return 2
    if lon <= -64.5:
        return 3
    return 4
