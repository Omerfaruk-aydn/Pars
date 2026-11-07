"""
PARS Python Modu (parspy)
-------------------------
`python` komutu yerine kullanılan PARS markalı Python çalıştırıcısı.

Kullanım:
  parspy dosya.py           Python dosyası çalıştır
  parspy -c "print(1)"      Tek satır Python kodu çalıştır
  parspy -m http.server     Modül çalıştır
  parspy                     Etkileşimli Python konsolu
"""

import argparse
import code
import runpy
import sys
from typing import Iterable, Optional

from pars import __version__

PROGRAM = 'parspy'

BANNER = (
    f'PARS Python Modu v{__version__}\n'
    'Python sürümü: ' + sys.version.split()[0] + '\n'
    'Çıkmak için exit() veya Ctrl+Z yazın.\n'
)


def kod_calistir(kod: str, ad: str = '<parspy>') -> int:
    """Python kodunu çalıştır."""
    try:
        derlenmis = compile(kod, ad, 'exec')
        exec(derlenmis, {'__name__': '__main__', '__file__': ad})
        return 0
    except SystemExit as e:
        return int(e.code or 0)
    except Exception:
        import traceback
        traceback.print_exc()
        return 1


def dosya_calistir(yol: str, argumanlar: Optional[Iterable[str]] = None) -> int:
    """Python dosyasını çalıştır."""
    eski_argv = sys.argv
    try:
        sys.argv = [yol] + list(argumanlar or [])
        runpy.run_path(yol, run_name='__main__')
        return 0
    except SystemExit as e:
        return int(e.code or 0)
    except Exception:
        import traceback
        traceback.print_exc()
        return 1
    finally:
        sys.argv = eski_argv


def modul_calistir(modul: str, argumanlar: Optional[Iterable[str]] = None) -> int:
    """Python modülünü çalıştır (-m)."""
    eski_argv = sys.argv
    try:
        sys.argv = [modul] + list(argumanlar or [])
        runpy.run_module(modul, run_name='__main__', alter_sys=True)
        return 0
    except SystemExit as e:
        return int(e.code or 0)
    except Exception:
        import traceback
        traceback.print_exc()
        return 1
    finally:
        sys.argv = eski_argv


def konsol() -> None:
    """Etkileşimli Python konsolu."""
    code.interact(banner=BANNER, local={})


def main(argv: Optional[Iterable[str]] = None) -> int:
    """parspy giriş noktası."""
    ay = argparse.ArgumentParser(
        prog=PROGRAM,
        description='PARS Python Modu — python komutu yerine parspy',
        add_help=True,
    )
    ay.add_argument('--surum', '--version', '-V', action='version',
                    version=f'{PROGRAM} (PARS {__version__}) '
                            f'Python {sys.version.split()[0]}')
    ay.add_argument('-c', '--kod', default=None,
                    help='Verilen Python kodunu çalıştır')
    ay.add_argument('-m', '--modul', default=None,
                    help='Python modülünü çalıştır')
    ay.add_argument('dosya', nargs='?', default=None)
    ay.add_argument('argumanlar', nargs=argparse.REMAINDER)

    secenekler = ay.parse_args(list(argv) if argv is not None else None)

    if secenekler.kod is not None:
        return kod_calistir(secenekler.kod)
    if secenekler.modul is not None:
        return modul_calistir(secenekler.modul, secenekler.argumanlar)
    if secenekler.dosya:
        return dosya_calistir(secenekler.dosya, secenekler.argumanlar)

    konsol()
    return 0


if __name__ == '__main__':
    sys.exit(main())
