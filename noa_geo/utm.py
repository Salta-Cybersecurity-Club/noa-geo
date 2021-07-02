"""Conversión a UTM reutilizando la maquinaria de Gauss-Krüger.

UTM y GK son la misma proyección (transverse Mercator); cambia la
numeración de zonas y el meridiano central.
"""

import math

from .gauss_krueger import A, E2, K0, _arco_meridiano


def zona_utm(lon):
    """Zona UTM (1-60) para una longitud en grados."""
    return int(math.floor((lon + 180.0) / 6.0)) + 1


def meridiano_zona(zona):
    return math.radians(zona * 6.0 - 183.0)


def latlon_a_utm(lat, lon, zona=None):
    """lat/lon -> (este, norte, zona). Hemisferio sur TODO: ver issue #5."""
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
        lam * cosp + lam**3 * cosp**3 / 6 * (1 - t * t + ep2)
    )
    norte = K0 * (m + nu * t * lam**2 * cosp**2 / 2)
    # TODO(issue #5): en hemisferio sur hay que sumar 10.000.000 al norte
    return este, norte, zona
