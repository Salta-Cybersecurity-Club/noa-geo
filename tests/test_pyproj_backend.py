"""Validación opcional contra pyproj (si está instalado)."""

import pytest

# sin pyproj estos tests se skipean en vez de romper
pyproj = pytest.importorskip("pyproj")

from noa_geo.gauss_krueger import latlon_a_gk


def test_contra_epsg_22183():
    from pyproj import Transformer

    t = Transformer.from_crs("EPSG:4326", "EPSG:22183", always_xy=True)
    e_ref, n_ref = t.transform(-65.4232, -24.7829)
    e, n = latlon_a_gk(-24.7829, -65.4232, faja=3)
    assert e == pytest.approx(e_ref, abs=0.5)
    assert n == pytest.approx(n_ref, abs=0.5)
