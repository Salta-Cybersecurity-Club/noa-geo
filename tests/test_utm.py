import math

import pytest

from noa_geo.utm import latlon_a_utm, zona_utm


def test_zona_utm_salta():
    assert zona_utm(-65.4) == 20


def test_hemisferio_sur_suma_falso_norte():
    _, n_sur, _ = latlon_a_utm(-24.78, -65.42)
    _, n_norte, _ = latlon_a_utm(24.78, -65.42)
    assert n_sur > 7_000_000
    assert n_norte < 4_000_000


def test_localidades_cargan():
    from noa_geo.localidades import buscar

    res = buscar("cafayate")
    assert len(res) == 1
    assert res[0].provincia == "Salta"
