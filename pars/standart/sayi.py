"""
PARS Sayı Modülü — decimal / fractions Türkçe sarmalayıcısı
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction
from typing import Any, Union

Ondalik = Decimal
Kesir = Fraction
Sayi = Union[int, float, str, Decimal, Fraction]

__all__ = [
    'Ondalik', 'Kesir', 'ondalik', 'kesir', 'ondalik_yuvarla',
    'kesin_topla', 'kesin_cikar', 'kesin_carp', 'kesin_bol',
    'yuzde', 'sinirla', 'bilimsel', 'hassasiyet',
]


def ondalik(deger: Sayi) -> Decimal:
    """Decimal nesnesi oluştur."""
    return Decimal(str(deger))


def kesir(pay: Any, payda: Any = None) -> Fraction:
    """Kesir oluştur."""
    if payda is None:
        return Fraction(pay)
    return Fraction(pay, payda)


def ondalik_yuvarla(deger: Sayi, basamak: int = 2) -> Decimal:
    """Ondalığı belirtilen basamağa yuvarla."""
    kuantum = Decimal(1).scaleb(-basamak)
    return ondalik(deger).quantize(kuantum, rounding=ROUND_HALF_UP)


def kesin_topla(*sayilar: Sayi) -> Decimal:
    return sum((ondalik(s) for s in sayilar), Decimal(0))


def kesin_cikar(a: Sayi, b: Sayi) -> Decimal:
    return ondalik(a) - ondalik(b)


def kesin_carp(a: Sayi, b: Sayi) -> Decimal:
    return ondalik(a) * ondalik(b)


def kesin_bol(a: Sayi, b: Sayi, basamak: int = 10) -> Decimal:
    kuantum = Decimal(1).scaleb(-basamak)
    return (ondalik(a) / ondalik(b)).quantize(
        kuantum, rounding=ROUND_HALF_UP)


def yuzde(deger: Sayi, oran: Sayi) -> Decimal:
    """deger'in %oran'ı."""
    return kesin_carp(deger, ondalik(oran) / Decimal(100))


def sinirla(deger: Sayi, alt: Sayi, ust: Sayi) -> Sayi:
    """Değeri [alt, ust] aralığına sıkıştır."""
    return max(alt, min(ust, deger))


def bilimsel(deger: Sayi, basamak: int = 6) -> str:
    return f'{float(deger):.{basamak}e}'


def hassasiyet(basamak: int = 28) -> None:
    """Ondalık hesaplama hassasiyetini ayarla."""
    getcontext().prec = basamak
