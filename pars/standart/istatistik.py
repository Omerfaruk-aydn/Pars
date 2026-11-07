"""
PARS İstatistik Modülü — statistics kütüphanesi Türkçe sarmalayıcısı
"""

import statistics
from typing import Any, List, Sequence

Sayi = Any

__all__ = [
    'ortalama', 'medyan', 'mod', 'cok_mod', 'harmonik_ortalama',
    'geometrik_ortalama', 'varyans', 'standart_sapma', 'sapma',
    'yakinlik', 'ceyrekler', 'korelasyon', 'dogrusal_regresyon',
    'aralik', 'siklik', 'toplam', 'buyuk', 'kucuk',
]


def ortalama(sayilar: Sequence[Sayi]) -> float:
    """Aritmetik ortalama."""
    return statistics.mean(sayilar)


def medyan(sayilar: Sequence[Sayi]) -> float:
    """Medyan (ortanca)."""
    return statistics.median(sayilar)


def mod(sayilar: Sequence[Sayi]) -> Any:
    """En sık tekrar eden değer."""
    return statistics.mode(sayilar)


def cok_mod(sayilar: Sequence[Sayi]) -> List[Any]:
    """Birden fazla mod değeri."""
    return statistics.multimode(sayilar)


def harmonik_ortalama(sayilar: Sequence[Sayi]) -> float:
    """Harmonik ortalama."""
    return statistics.harmonic_mean(sayilar)


def geometrik_ortalama(sayilar: Sequence[Sayi]) -> float:
    """Geometrik ortalama (Python 3.8+)."""
    return statistics.geometric_mean(sayilar)


def varyans(sayilar: Sequence[Sayi]) -> float:
    """Örneklem varyansı."""
    return statistics.variance(sayilar)


def standart_sapma(sayilar: Sequence[Sayi]) -> float:
    """Örneklem standart sapması."""
    return statistics.stdev(sayilar)


def sapma(sayilar: Sequence[Sayi]) -> float:
    """Kütle (popülasyon) standart sapması."""
    return statistics.pstdev(sayilar)


def yakinlik(sayilar: Sequence[Sayi], n: int = 4) -> List[float]:
    """Veriyi n eşit dilime böl (çeyrekler, yüzdelikler)."""
    return statistics.quantiles(sayilar, n=n)


def ceyrekler(sayilar: Sequence[Sayi]) -> List[float]:
    """Çeyreklikler (Q1, Q2, Q3)."""
    return statistics.quantiles(sayilar, n=4)


def korelasyon(x: Sequence[Sayi], y: Sequence[Sayi]) -> float:
    """Pearson korelasyon katsayısı."""
    return statistics.correlation(x, y)


def dogrusal_regresyon(x: Sequence[Sayi],
                       y: Sequence[Sayi]) -> tuple:
    """Basit doğrusal regresyon: (egim, kesisim)."""
    return statistics.linear_regression(x, y)


def aralik(sayilar: Sequence[Sayi]) -> float:
    """En büyük - en küçük."""
    return max(sayilar) - min(sayilar)


def siklik(sayilar: Sequence[Sayi]) -> dict:
    """Değer → tekrar sayısı sözlüğü."""
    sonuc = {}
    for s in sayilar:
        sonuc[s] = sonuc.get(s, 0) + 1
    return sonuc


def toplam(sayilar: Sequence[Sayi]) -> Sayi:
    return sum(sayilar)


def buyuk(sayilar: Sequence[Sayi]) -> Sayi:
    return max(sayilar)


def kucuk(sayilar: Sequence[Sayi]) -> Sayi:
    return min(sayilar)
