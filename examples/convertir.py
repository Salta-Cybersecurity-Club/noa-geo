"""Ejemplo: convertir coordenadas de localidades del NOA a GK."""

from noa_geo.gauss_krueger import latlon_a_gk
from noa_geo.localidades import cargar

for loc in cargar():
    e, n = latlon_a_gk(loc.lat, loc.lon, loc.faja)
    print("%-32s faja %d  este %12.1f  norte %12.1f" % (loc.nombre, loc.faja, e, n))
