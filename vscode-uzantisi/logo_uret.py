#!/usr/bin/env python3
"""PNG logoyu base64 olarak gomulmus bir SVG'ye cevirir.

Kullanim:
    python logo_uret.py [kaynak.png] [cikti.svg]

Varsayilanlar:
    icons/pars.png -> icons/pars.svg

Sabit /mnt/data yolu yoktur; kaynak ve cikti komut satirindan
veya betigin bulundugu klasorden cozulur.
"""

from __future__ import annotations

import base64
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent


def main() -> int:
    kaynak = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else KOK / "icons" / "pars.png"
    cikti = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else KOK / "icons" / "pars.svg"

    if not kaynak.is_file():
        sys.stderr.write("HATA: PNG bulunamadi: %s\n" % kaynak)
        return 1

    veri = base64.b64encode(kaynak.read_bytes()).decode("ascii")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" '
        'viewBox="0 0 128 128" role="img" aria-label="PARS">\n'
        '  <title>PARS programlama dili</title>\n'
        '  <image width="128" height="128" '
        'href="data:image/png;base64,%s"/>\n'
        '</svg>\n' % veri
    )

    cikti.parent.mkdir(parents=True, exist_ok=True)
    cikti.write_text(svg, encoding="utf-8")
    sys.stdout.write("Yazildi: %s (%d bayt)\n" % (cikti, cikti.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
