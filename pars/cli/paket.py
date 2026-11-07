"""
PARS Paket Yöneticisi (parskur)
-------------------------------
`pip` yerine kullanılan Türkçe paket yönetim arayüzü.

Kullanım:
  parskur yükle requests numpy
  parskur kaldır requests
  parskur güncelle requests
  parskur listele
  parskur göster requests
  parskur dışa gereksinimler.txt
  parskur içe gereksinimler.txt

Bu araç Python paketlerini yönetir; arka planda `python -m pip` kullanır.
Kullanıcıya her zaman PARS markalı, Türkçe çıktı verir.
"""

import argparse
import subprocess
import sys
from typing import Iterable, List, Optional

from pars import __version__

PROGRAM = 'parskur'

_YUKLE = 'yükle'
_KALDIR = 'kaldır'
_GUNCELLE = 'güncelle'
_LISTELE = 'listele'
_GOSTER = 'göster'
_DISA = 'dışa'
_ICE = 'içe'
_ARA = 'ara'


def _pip_calistir(argumanlar: List[str]) -> int:
    """pip'i alt süreç olarak çalıştır ve dönüş kodunu ver."""
    komut = [sys.executable, '-m', 'pip'] + argumanlar
    try:
        return subprocess.call(komut)
    except FileNotFoundError:
        print('Hata: pip bulunamadı. Python kurulumunuzu kontrol edin.',
              file=sys.stderr)
        return 1


def paket_yukle(*paketler: str, gereksinim: Optional[str] = None,
                sessiz: bool = False) -> bool:
    """Paket(ler)i yükle. Başarılıysa True döndür."""
    if not paketler and not gereksinim:
        print('Hata: yüklenecek paket belirtilmedi.', file=sys.stderr)
        return False

    argumanlar = ['install']
    if sessiz:
        argumanlar.append('--quiet')
    if gereksinim:
        argumanlar += ['-r', gereksinim]
    argumanlar += list(paketler)

    etiket = ', '.join(paketler) if paketler else gereksinim
    print(f'▶  PARS paketi yükleniyor: {etiket}')
    kod = _pip_calistir(argumanlar)
    if kod == 0:
        print('✓  Paket yükleme tamamlandı.')
        return True
    print('✗  Paket yüklenemedi.', file=sys.stderr)
    return False


def paket_kaldir(*paketler: str) -> bool:
    if not paketler:
        print('Hata: kaldırılacak paket belirtilmedi.', file=sys.stderr)
        return False
    print(f'▶  PARS paketi kaldırılıyor: {", ".join(paketler)}')
    kod = _pip_calistir(['uninstall', '-y', *paketler])
    if kod == 0:
        print('✓  Paket kaldırma tamamlandı.')
        return True
    print('✗  Paket kaldırılamadı.', file=sys.stderr)
    return False


def paket_guncelle(*paketler: str) -> bool:
    hedef = list(paketler) if paketler else ['--all']
    print(f'▶  PARS paketi güncelleniyor: {", ".join(hedef)}')
    kod = _pip_calistir(['install', '--upgrade', *hedef])
    if kod == 0:
        print('✓  Güncelleme tamamlandı.')
        return True
    print('✗  Güncelleme başarısız.', file=sys.stderr)
    return False


def paket_listele(eski: bool = False) -> int:
    argumanlar = ['list', '--outdated'] if eski else ['list']
    return _pip_calistir(argumanlar)


def paket_goster(paket: str) -> int:
    return _pip_calistir(['show', paket])


def paket_disa(dosya: Optional[str] = None) -> int:
    if dosya:
        try:
            with open(dosya, 'w', encoding='utf-8') as f:
                return subprocess.call(
                    [sys.executable, '-m', 'pip', 'freeze'], stdout=f)
        except OSError as e:
            print(f'Hata: {e}', file=sys.stderr)
            return 1
    return _pip_calistir(['freeze'])


def paket_ice(dosya: str) -> bool:
    return paket_yukle(gereksinim=dosya)


def paket_ara(terim: str) -> int:
    """Yüklü paketler içinde ara (pip search kaldırıldı)."""
    try:
        sonuc = subprocess.run(
            [sys.executable, '-m', 'pip', 'list'],
            capture_output=True, text=True, check=False)
    except OSError as e:
        print(f'Hata: {e}', file=sys.stderr)
        return 1

    terim = terim.lower()
    bulunan = [satir for satir in sonuc.stdout.splitlines()
               if terim in satir.lower()]
    if bulunan:
        print('\n'.join(bulunan))
    else:
        print(f'Yüklü paketler arasında "{terim}" bulunamadı.')
    return 0


def _arguman_ayristirici() -> argparse.ArgumentParser:
    ay = argparse.ArgumentParser(
        prog=PROGRAM,
        description='PARS Paket Yöneticisi — pip yerine parskur',
    )
    ay.add_argument('--surum', '--version', action='version',
                    version=f'{PROGRAM} (PARS {__version__})')
    alt = ay.add_subparsers(dest='komut')

    p = alt.add_parser('yükle', aliases=['yukle', 'kur'])
    p.add_argument('paketler', nargs='*')
    p.add_argument('-r', '--gereksinim', default=None)
    p.add_argument('--sessiz', action='store_true')

    p = alt.add_parser('kaldır', aliases=['kaldir', 'sil'])
    p.add_argument('paketler', nargs='+')

    p = alt.add_parser('güncelle', aliases=['guncelle', 'yenile'])
    p.add_argument('paketler', nargs='*')

    p = alt.add_parser('listele', aliases=['liste'])
    p.add_argument('--eski', action='store_true')

    p = alt.add_parser('göster', aliases=['goster', 'bilgi'])
    p.add_argument('paket')

    p = alt.add_parser('dışa', aliases=['disa', 'dondur'])
    p.add_argument('dosya', nargs='?', default=None)

    p = alt.add_parser('içe', aliases=['ice'])
    p.add_argument('dosya')

    p = alt.add_parser('ara', aliases=['search'])
    p.add_argument('terim')

    return ay


def main(argv: Optional[Iterable[str]] = None) -> int:
    """parskur giriş noktası."""
    ay = _arguman_ayristirici()
    secenekler = ay.parse_args(list(argv) if argv is not None else None)

    if not secenekler.komut:
        ay.print_help()
        return 0

    komut = secenekler.komut
    if komut in ('yükle', 'yukle', 'kur'):
        basarili = paket_yukle(
            *secenekler.paketler,
            gereksinim=secenekler.gereksinim,
            sessiz=secenekler.sessiz,
        )
        return 0 if basarili else 1
    if komut in ('kaldır', 'kaldir', 'sil'):
        return 0 if paket_kaldir(*secenekler.paketler) else 1
    if komut in ('güncelle', 'guncelle', 'yenile'):
        return 0 if paket_guncelle(*secenekler.paketler) else 1
    if komut in ('listele', 'liste'):
        return paket_listele(eski=secenekler.eski)
    if komut in ('göster', 'goster', 'bilgi'):
        return paket_goster(secenekler.paket)
    if komut in ('dışa', 'disa', 'dondur'):
        return paket_disa(secenekler.dosya)
    if komut in ('içe', 'ice'):
        return 0 if paket_ice(secenekler.dosya) else 1
    if komut in ('ara', 'search'):
        return paket_ara(secenekler.terim)

    ay.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
