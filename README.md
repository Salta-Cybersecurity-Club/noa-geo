# noa-geo

[![tests](https://github.com/Salta-Cybersecurity-Club/noa-geo/actions/workflows/tests.yml/badge.svg)](https://github.com/Salta-Cybersecurity-Club/noa-geo/actions/workflows/tests.yml)
[![PyPI-ish](https://img.shields.io/badge/pypi-no--publicado-lightgrey)]()
[![version](https://img.shields.io/badge/tag-v0.4.2-blue)]()

Utilidades geo para el NOA (noroeste argentino) mantenidas por un grupo de
devs de Salta.

- Conversión lat/lon <-> POSGAR 94 / Gauss-Krüger (fajas 1 a 4).
- Conversión a UTM (con hemisferio sur).
- Base de localidades del NOA compilada a mano (IGN + censos).
- CLI mínima: `python -m noa_geo.cli`.

## Uso rápido

```python
from noa_geo.gauss_krueger import latlon_a_gk

este, norte = latlon_a_gk(-24.7829, -65.4232, faja=3)  # Salta Capital
```

```bash
$ python -m noa_geo.cli convert --lat -24.7829 --lon -65.4232 --faja 3
este=359812.34  norte=7259184.10  (faja 3)

$ python -m noa_geo.cli localidad cafayate
Cafayate — Salta — lat -26.073, lon -65.9764 (faja 3)
```

Sin dependencias obligatorias. Si `pyproj` está instalado se usa como
backend alternativo (ver `docs/api.md`).

## Estado del proyecto

Lo usamos internamente en varios proyectos nuestros (saeta-live, el mapa de
nodos, etc.). Issues y PRs bienvenidos pero no prometemos SLA.
