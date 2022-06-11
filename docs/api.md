# API de noa-geo

## `noa_geo.gauss_krueger`

- `latlon_a_gk(lat, lon, faja=3)` -> `(este, norte)` en metros.
- `gk_a_latlon(este, norte, faja=3)` -> `(lat, lon)` en grados.
- `meridiano_central(faja)` -> radianes.
- `faja_para_lon(lon)` -> faja sugerida para el NOA.

## `noa_geo.utm`

- `latlon_a_utm(lat, lon, zona=None)` -> `(este, norte, zona)`. En hemisferio
  sur suma el falso norte (10.000.000 m).
- `zona_utm(lon)` -> número de zona UTM.

## `noa_geo.localidades`

- `cargar(path=None)` -> lista de `Localidad` desde el CSV interno.
- `buscar(nombre)` -> búsqueda difusa sin tildes.
- `cercanas(lat, lon, radio_km=50)` -> localidades en un radio aproximado.

## Backend opcional con pyproj

Si `pyproj` está instalado, los tests lo usan para validar contra EPSG:22183
(POSGAR 94 faja 3) y EPSG:22182 (faja 2). No es dependencia de runtime.
