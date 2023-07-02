# noa-geo

> **⚠️ SIN MANTENIMIENTO (jul-2023).** Este proyecto quedó archivado: la
> funcionalidad se migró a un monorepo privado y acá ya nadie revisa PRs.
> El código queda publicado por si le sirve a alguien. — @mdelgado-noa

[![tests](https://github.com/Salta-Cybersecurity-Club/noa-geo/actions/workflows/tests.yml/badge.svg)](https://github.com/Salta-Cybersecurity-Club/noa-geo/actions/workflows/tests.yml)

Utilidades geo para el NOA (noroeste argentino).

- Conversión lat/lon <-> POSGAR 94 / Gauss-Krüger (fajas 1 a 4).
- Conversión a UTM (con hemisferio sur).
- Base de localidades del NOA compilada a mano (IGN + censos).
- CLI mínima: `python -m noa_geo.cli`.

## Uso rápido

```python
from noa_geo.gauss_krueger import latlon_a_gk

este, norte = latlon_a_gk(-24.7829, -65.4232, faja=3)  # Salta Capital
```

Sin dependencias obligatorias. Si `pyproj` está instalado se usa como
backend alternativo (ver `docs/api.md`).
