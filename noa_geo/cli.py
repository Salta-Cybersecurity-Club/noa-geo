"""CLI mínima de noa-geo.

    python -m noa_geo.cli convert --lat -24.78 --lon -65.42 --faja 3
    python -m noa_geo.cli localidad cafayate
"""

import argparse

from .gauss_krueger import faja_para_lon, latlon_a_gk
from .localidades import buscar


def main(argv=None):
    p = argparse.ArgumentParser(prog="noa-geo")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("convert", help="lat/lon -> GK")
    c.add_argument("--lat", type=float, required=True)
    c.add_argument("--lon", type=float, required=True)
    c.add_argument("--faja", type=int, default=None)

    b = sub.add_parser("localidad", help="buscar localidad")
    b.add_argument("nombre")

    args = p.parse_args(argv)
    if args.cmd == "convert":
        faja = args.faja or faja_para_lon(args.lon)
        e, n = latlon_a_gk(args.lat, args.lon, faja)
        print("este=%.2f  norte=%.2f  (faja %d)" % (e, n, faja))
    else:
        for l in buscar(args.nombre):
            print("%s — %s — lat %s, lon %s (faja %d)" % (l.nombre, l.provincia, l.lat, l.lon, l.faja))


if __name__ == "__main__":
    main()
