"""Conversión POSGAR 94 / Gauss-Krüger (fajas 2 y 3, las del NOA).

Implementación propia: no queríamos arrastrar pyproj como dependencia
obligatoria para deploys chicos. POSGAR 94 es ~WGS84 a efectos prácticos.
"""

import math

# Meridiano central por faja (grados)
FAJAS = {2: -69.0, 3: -66.0, 4: -63.0}

A = 6378137.0          # semieje mayor
F = 1 / 298.257223563  # achatamiento
E2 = F * (2 - F)       # excentricidad^2
K0 = 0.9996


def meridiano_central(faja):
    """Meridiano central (radianes) de la faja Gauss-Krüger."""
    if faja not in FAJAS:
        raise ValueError("faja %r fuera de rango para el NOA" % faja)
    return math.radians(FAJAS[faja])


def latlon_a_gk(lat, lon, faja=3):
    """Convierte lat/lon (grados) a (este, norte) en metros GK.

    Serie estándar de transverse mercator. Precisión ~mm para lo que necesitamos.
    """
    phi = math.radians(lat)
    lam = math.radians(lon) - meridiano_central(faja)

    sinp, cosp = math.sin(phi), math.cos(phi)
    t = math.tan(phi)
    n2 = E2 / (1 - E2)
    ep2 = n2 * cosp * cosp
    nu = A / math.sqrt(1 - E2 * sinp * sinp)

    # arco meridiano
    e4 = E2 * E2
    e6 = e4 * E2
    m = A * (
        (1 - E2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * phi
        - (3 * E2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * phi)
        + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * phi)
        - (35 * e6 / 3072) * math.sin(6 * phi)
    )

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
    # hemisferio sur
    norte += 10000000.0
    return este, norte


def faja_para_lon(lon):
    """Sugiere la faja GK según longitud (aprox NOA)."""
    if lon <= -67.5:
        return 2
    if lon <= -64.5:
        return 3
    return 4
