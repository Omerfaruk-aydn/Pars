"""
PARS Modül İçe Aktarma Kancası
------------------------------
Yerel ``.pars`` (ve eski ``.prs``) dosyalarının ``içe_aktar`` /
``den_aktar`` ile normal Python modülü gibi yüklenmesini sağlar.

Modül yüklenirken PARS built-in'leri, Türkçe istisnalar ve standart
kütüphane ad alanı modülün globallerine eklenir.
"""

import importlib.abc
import importlib.util
import os
import sys

from .ceviri import cevir

_UZANTILAR = ('.pars', '.prs')


class ParsYukleyici(importlib.abc.Loader):
    """Tek bir PARS kaynak dosyasını modül olarak yürütür."""

    def __init__(self, tam_ad: str, yol: str):
        self.tam_ad = tam_ad
        self.yol = yol

    def create_module(self, spec):
        return None

    def exec_module(self, modul) -> None:
        with open(self.yol, encoding='utf-8') as dosya:
            kaynak = dosya.read()

        python_kodu = cevir(kaynak)

        # Döngüsel import'u önlemek için tembel içe aktarma.
        from .yurutucu import ad_alani_olustur

        temel = ad_alani_olustur(self.yol)
        for anahtar, deger in temel.items():
            modul.__dict__.setdefault(anahtar, deger)

        kod = compile(python_kodu, self.yol, 'exec')
        exec(kod, modul.__dict__)


class ParsBulucu(importlib.abc.MetaPathFinder):
    """``sys.path`` üzerinde ``.pars`` dosyalarını arar."""

    def __init__(self):
        self.ek_yollar = []

    def _dizinler(self, yol=None):
        gorulen = set()
        adaylar = list(yol) if yol else list(sys.path)
        adaylar = list(self.ek_yollar) + adaylar
        for dizin in adaylar:
            dizin = dizin or os.getcwd()
            if dizin not in gorulen:
                gorulen.add(dizin)
                yield dizin

    def find_spec(self, tam_ad, yol=None, hedef=None):
        parca = tam_ad.rpartition('.')[2]
        for dizin in self._dizinler(yol):
            paket = os.path.join(dizin, parca)
            for uzanti in _UZANTILAR:
                baslangic = os.path.join(paket, '__init__' + uzanti)
                if os.path.isfile(baslangic):
                    return importlib.util.spec_from_file_location(
                        tam_ad, baslangic,
                        loader=ParsYukleyici(tam_ad, baslangic),
                        submodule_search_locations=[paket],
                    )
                aday = os.path.join(dizin, parca + uzanti)
                if os.path.isfile(aday):
                    return importlib.util.spec_from_file_location(
                        tam_ad, aday,
                        loader=ParsYukleyici(tam_ad, aday),
                    )
        return None


_bulucu = ParsBulucu()
_kuruldu = False


def kur():
    """Kancayı bir kez ``sys.meta_path`` sonuna ekler."""
    global _kuruldu
    if not _kuruldu:
        sys.meta_path.append(_bulucu)
        _kuruldu = True
    return _bulucu


def yol_ekle(dizin: str) -> None:
    """Yerel modül aramasına ek bir dizin ekler."""
    kur()
    if dizin and dizin not in _bulucu.ek_yollar:
        _bulucu.ek_yollar.insert(0, dizin)


def kaldir() -> None:
    """Kancayı ve ek yolları temizler (testler için)."""
    global _kuruldu
    if _bulucu in sys.meta_path:
        sys.meta_path.remove(_bulucu)
    _bulucu.ek_yollar.clear()
    _kuruldu = False
