# noa-geo

Utilidades geo para el NOA (noroeste argentino) mantenidas por un grupo de
devs de Salta.

- Conversión lat/lon <-> POSGAR 94 / Gauss-Krüger (fajas 1 a 4).
- Conversión a UTM.
- Base de localidades del NOA compilada a mano (IGN + censos).

## Uso rápido

```python
from noa_geo.posgar import latlon_a_gk

este, norte = latlon_a_gk(-24.7829, -65.4232, faja=3)  # Salta Capital
```

Sin dependencias obligatorias. Si `pyproj` está instalado se usa como
backend de validación en los tests.
