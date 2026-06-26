"""
PARS Matematik Modülü — math kütüphanesi Türkçe sarmalayıcısı
"""

import math
import cmath
import statistics
from typing import Union, Sequence

Sayi = Union[int, float]

PI = math.pi
E = math.e
TAU = math.tau
SONSUZ = math.inf
NAN = math.nan

__all__ = [
    'PI', 'E', 'TAU', 'SONSUZ', 'NAN',
    'kare_kok', 'us', 'mutlak', 'yuvarlak', 'tavan', 'taban_al', 'mod',
    'sinus', 'kosinus', 'tanjant', 'ark_sinus', 'ark_kosinus', 'ark_tanjant',
    'ark_tanjant2', 'derece_radyan', 'radyan_derece', 'hipotenus',
    'logaritma', 'log10', 'log2', 'exp',
    'faktoriyel', 'kombinasyon', 'permutasyon', 'obeb', 'okek',
    'ortalama', 'medyan', 'mod_istatistik', 'standart_sapma', 'varyans',
    'kovaryans',
]


def kare_kok(x: Sayi) -> float:
    """Karekök hesapla."""
    return math.sqrt(x)


def us(taban: Sayi, ust: Sayi) -> float:
    """Üs alma."""
    return math.pow(taban, ust)


def mutlak(x: Sayi) -> Sayi:
    """Mutlak değer."""
    return abs(x)


def yuvarlak(x: Sayi, basamak: int = 0) -> float:
    """Yuvarlama."""
    return round(x, basamak)


def tavan(x: Sayi) -> int:
    """Tavan (yukarı yuvarla)."""
    return math.ceil(x)


def taban_al(x: Sayi) -> int:
    """Taban (aşağı yuvarla)."""
    return math.floor(x)


def mod(x: Sayi, y: Sayi) -> Sayi:
    """Mod alma."""
    return x % y


# ── TRİGONOMETRİ ─────────────────────────────────────────────────────────

def sinus(x: Sayi) -> float:
    """Sinüs (radyan)."""
    return math.sin(x)


def kosinus(x: Sayi) -> float:
    """Kosinüs (radyan)."""
    return math.cos(x)


def tanjant(x: Sayi) -> float:
    """Tanjant (radyan)."""
    return math.tan(x)


def ark_sinus(x: Sayi) -> float:
    """Ark sinüs."""
    return math.asin(x)


def ark_kosinus(x: Sayi) -> float:
    """Ark kosinüs."""
    return math.acos(x)


def ark_tanjant(x: Sayi) -> float:
    """Ark tanjant."""
    return math.atan(x)


def ark_tanjant2(y: Sayi, x: Sayi) -> float:
    """İki değişkenli ark tanjant."""
    return math.atan2(y, x)


def derece_radyan(d: Sayi) -> float:
    """Dereceyi radyana çevir."""
    return math.radians(d)


def radyan_derece(r: Sayi) -> float:
    """Radyanı dereceye çevir."""
    return math.degrees(r)


def hipotenus(*sayilar: Sayi) -> float:
    """Hipotenüs hesapla."""
    return math.hypot(*sayilar)


# ── LOGARİTMA / ÜS ───────────────────────────────────────────────────────

def logaritma(x: Sayi, taban: Sayi = None) -> float:
    """Logaritma. Taban belirtilmezse doğal logaritma."""
    if taban is None:
        return math.log(x)
    return math.log(x, taban)


def log10(x: Sayi) -> float:
    """10 tabanında logaritma."""
    return math.log10(x)


def log2(x: Sayi) -> float:
    """2 tabanında logaritma."""
    return math.log2(x)


def exp(x: Sayi) -> float:
    """Doğal üstel (e^x)."""
    return math.exp(x)


# ── KOMBİNATORİK ─────────────────────────────────────────────────────────

def faktoriyel(n: int) -> int:
    """Faktöriyel hesapla."""
    return math.factorial(n)


def kombinasyon(n: int, k: int) -> int:
    """Kombinasyon C(n, k)."""
    return math.comb(n, k)


def permutasyon(n: int, k: int = None) -> int:
    """Permütasyon P(n, k)."""
    return math.perm(n, k)


def obeb(a: int, b: int) -> int:
    """Ortak bölenlerin en büyüğü."""
    return math.gcd(a, b)


def okek(a: int, b: int) -> int:
    """Ortak katların en küçüğü."""
    return math.lcm(a, b)


# ── İSTATİSTİK ───────────────────────────────────────────────────────────

def ortalama(sayilar: Sequence[Sayi]) -> float:
    """Aritmetik ortalama."""
    return statistics.mean(sayilar)


def medyan(sayilar: Sequence[Sayi]) -> float:
    """Medyan."""
    return statistics.median(sayilar)


def mod_istatistik(sayilar: Sequence[Sayi]):
    """Mod (en sık tekrar eden değer)."""
    return statistics.mode(sayilar)


def standart_sapma(sayilar: Sequence[Sayi]) -> float:
    """Standart sapma."""
    return statistics.stdev(sayilar)


def varyans(sayilar: Sequence[Sayi]) -> float:
    """Varyans."""
    return statistics.variance(sayilar)


def kovaryans(x: Sequence[Sayi], y: Sequence[Sayi]) -> float:
    """İki veri seti arasındaki kovaryans."""
    return statistics.covariance(x, y)
