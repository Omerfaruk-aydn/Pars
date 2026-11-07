"""
PARS Argüman Modülü — argparse kütüphanesi Türkçe sarmalayıcısı
"""

import argparse
from typing import Any, Optional, Sequence

__all__ = ['ArgumanAyristirici', 'ayristirici']

_TURKCE_ANAHTARLAR = {
    'yardim': 'help',
    'varsayilan': 'default',
    'gerekli': 'required',
    'tip': 'type',
    'secimler': 'choices',
    'eylem': 'action',
    'hedef': 'dest',
    'ust_sinir': 'metavar',
}


def _secenekleri_cevir(secenekler: dict) -> dict:
    """T?rk?e argparse anahtar kelimelerini ?ngilizceye ?evir."""
    return {_TURKCE_ANAHTARLAR.get(k, k): v for k, v in secenekler.items()}


class ArgumanAyristirici:
    """
    argparse.ArgumentParser Türkçe sarmalayıcısı.

    Kullanım:
        ay = ArgumanAyristirici("Uygulamam")
        ay.konumlu("dosya", yardim="Girdi dosyası")
        ay.secenek("--ayar", varsayilan="x")
        ay.bayrak("--ayrintili", yardim="Ayrıntılı çıktı")
        secenekler = ay.ayristir()
    """

    def __init__(self, aciklama: str = '', surum: Optional[str] = None) -> None:
        self._ayristirici = argparse.ArgumentParser(description=aciklama)
        if surum:
            self._ayristirici.add_argument(
                '--surum', '--version', action='version',
                version=f'%(prog)s {surum}')

    def konumlu(self, isim: str, **secenekler: Any):
        self._ayristirici.add_argument(isim, **_secenekleri_cevir(secenekler))
        return self

    def secenek(self, isim: str, **secenekler: Any):
        self._ayristirici.add_argument(isim, **_secenekleri_cevir(secenekler))
        return self

    def bayrak(self, isim: str, **secenekler: Any):
        secenekler.setdefault('action', 'store_true')
        self._ayristirici.add_argument(isim, **_secenekleri_cevir(secenekler))
        return self

    def dizi(self, isim: str, **secenekler: Any):
        secenekler.setdefault('nargs', '+')
        self._ayristirici.add_argument(isim, **_secenekleri_cevir(secenekler))
        return self

    def ayristir(self, argumanlar: Optional[Sequence[str]] = None):
        return self._ayristirici.parse_args(argumanlar)

    def bilinenleri(self, argumanlar: Optional[Sequence[str]] = None):
        return self._ayristirici.parse_known_args(argumanlar)

    def yardim(self) -> str:
        return self._ayristirici.format_help()

    def alt_ayristirici(self, isim: str = 'komut', **secenekler: Any):
        return self._ayristirici.add_subparsers(dest=isim, **_secenekleri_cevir(secenekler))

    @property
    def ham(self):
        return self._ayristirici


def ayristirici(aciklama: str = '', surum: Optional[str] = None) -> ArgumanAyristirici:
    return ArgumanAyristirici(aciklama, surum)
