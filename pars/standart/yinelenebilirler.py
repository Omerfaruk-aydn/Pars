"""
PARS Yinelenebilirler Modülü — itertools kütüphanesi Türkçe sarmalayıcısı
"""

import itertools
from typing import Any, Iterable, Optional

__all__ = [
    'say', 'dongu', 'tekrar', 'zincirle', 'kombinasyonlar',
    'kombinasyonlu_tekrar', 'permutasyonlar', 'carpim', 'grupla',
    'dilimle', 'ilk_n', 'tara', 'birikimli', 'sikistir_uzun',
    'sikistir', 'filtrele_yanlis', 'tekrarla',
]


def say(baslangic: int = 0, adim: int = 1):
    """Sonsuz sayıcı."""
    return itertools.count(baslangic, adim)


def dongu(yinelenebilir: Iterable[Any]):
    """Sonsuz döngü."""
    return itertools.cycle(yinelenebilir)


def tekrar(eleman: Any, n: Optional[int] = None):
    """Elemanı n kez (n yoksa sonsuz) tekrarla."""
    return itertools.repeat(eleman, n)


def zincirle(*yinelenebilirler: Iterable[Any]):
    """Birden fazla yinelenebiliri sırayla birleştir."""
    return itertools.chain(*yinelenebilirler)


def kombinasyonlar(yinelenebilir: Iterable[Any], r: int):
    """r'li kombinasyonlar."""
    return itertools.combinations(yinelenebilir, r)


def kombinasyonlu_tekrar(yinelenebilir: Iterable[Any], r: int):
    """Tekrarlı kombinasyonlar."""
    return itertools.combinations_with_replacement(yinelenebilir, r)


def permutasyonlar(yinelenebilir: Iterable[Any], r: Optional[int] = None):
    """r'li permütasyonlar."""
    return itertools.permutations(yinelenebilir, r)


def carpim(*yinelenebilirler: Iterable[Any], tekrar: int = 1):
    """Kartezyen çarpım."""
    return itertools.product(*yinelenebilirler, repeat=tekrar)


def grupla(yinelenebilir: Iterable[Any], anahtar=None) -> list:
    """Ardışık eşit anahtarlı gruplar: [(anahtar, [elemanlar])]."""
    return [(k, list(g)) for k, g in
            itertools.groupby(yinelenebilir, key=anahtar)]


def dilimle(yinelenebilir: Iterable[Any], baslangic: int,
            bitis: Optional[int] = None, adim: int = 1) -> list:
    """itertools.islice sarmalayıcısı."""
    return list(itertools.islice(yinelenebilir, baslangic, bitis, adim))


def ilk_n(yinelenebilir: Iterable[Any], n: int) -> list:
    return list(itertools.islice(yinelenebilir, n))


def tara(yinelenebilir: Iterable[Any], fonksiyon, baslangic=None) -> list:
    """Ardışık birikimli değerler."""
    if baslangic is None:
        return list(itertools.accumulate(yinelenebilir, fonksiyon))
    return list(itertools.accumulate(yinelenebilir, fonksiyon,
                                     initial=baslangic))


def birikimli(yinelenebilir: Iterable[Any]) -> list:
    """Kümülatif toplamlar."""
    return list(itertools.accumulate(yinelenebilir))


def sikistir_uzun(*yinelenebilirler: Iterable[Any], dolgu=None) -> list:
    """En uzun olana göre zip."""
    return list(itertools.zip_longest(*yinelenebilirler,
                                      fillvalue=dolgu))


def sikistir(*yinelenebilirler: Iterable[Any]) -> list:
    """zip."""
    return list(zip(*yinelenebilirler))


def filtrele_yanlis(fonksiyon, yinelenebilir: Iterable[Any]) -> list:
    """Koşulu sağlamayanları döndür."""
    return list(itertools.filterfalse(fonksiyon, yinelenebilir))


def tekrarla(yinelenebilir: Iterable[Any], n: int) -> list:
    """Aynı yinelenebiliri n kez tekrarla."""
    return list(itertools.chain.from_iterable(
        itertools.repeat(list(yinelenebilir), n)))
