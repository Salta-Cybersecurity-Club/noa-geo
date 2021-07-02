import pytest

from noa_geo.utm import latlon_a_utm, zona_utm


def test_zona_utm_salta():
    assert zona_utm(-65.4) == 20


def test_utm_basico():
    e, n, z = latlon_a_utm(-24.78, -65.42)
    assert z == 20
    assert 500_000 < e < 900_000
