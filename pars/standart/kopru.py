"""
PARS Köprü Modülü
-----------------
Python kütüphanelerini PARS sözdizimine uyarlayan köprü sistemi.

Kullanım::

    içe_aktar köprü
    istek = köprü.bagla("requests")
    yanit = istek.al("https://ornek.com")
    yaz(yanit.durum_kodu)
"""

from pars.cekirdek.kopru import (
    Kopru,
    bagla,
    kutuphane_yukle,
    turkce_ad,
    ingilizce_ad,
    ceviri_sozlugu,
    sozluk_ekle,
    disa_aktar,
    ozellik_listesi,
)

__all__ = [
    'Kopru', 'bagla', 'kutuphane_yukle', 'turkce_ad', 'ingilizce_ad',
    'ceviri_sozlugu', 'sozluk_ekle', 'disa_aktar', 'ozellik_listesi',
]
