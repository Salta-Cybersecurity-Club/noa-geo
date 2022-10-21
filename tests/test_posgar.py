import math

import pytest

from noa_geo.gauss_krueger import faja_para_lon, latlon_a_gk, meridiano_central


def test_meridiano_faja3():
    assert meridiano_central(3) == pytest.approx(math.radians(-66.0))


def test_faja_invalida():
    with pytest.raises(ValueError):
        meridiano_central(9)


def test_salta_este_norte():
    e, n = latlon_a_gk(-24.7829, -65.4232, faja=3)
    # valores de referencia calculados con pyproj (jun-2021)
    assert e == pytest.approx(359812.3, abs=50)
    assert n == pytest.approx(7259184.1, abs=50)


def test_faja_por_longitud():
    assert faja_para_lon(-67.6) == 2
    assert faja_para_lon(-65.4) == 3
    assert faja_para_lon(-64.0) == 4


def test_borde_faja():
    e, n = latlon_a_gk(-24.5, -67.4, faja=2)
    assert 0 < e < 1_000_000
