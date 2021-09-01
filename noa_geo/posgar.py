"""DEPRECADO: usar `noa_geo.gauss_krueger`.

Queda como shim por compatibilidad hasta la 0.3.
"""

import warnings

from .gauss_krueger import (  # noqa: F401
    FALSO_NORTE_SUR,
    MERIDIANOS,
    faja_para_lon,
    gk_a_latlon,
    latlon_a_gk,
    meridiano_central,
)

warnings.warn(
    "noa_geo.posgar está deprecado; usar noa_geo.gauss_krueger",
    DeprecationWarning,
    stacklevel=2,
)

# alias histórico: antes exponíamos FAJAS en vez de MERIDIANOS
FAJAS = dict(MERIDIANOS)
