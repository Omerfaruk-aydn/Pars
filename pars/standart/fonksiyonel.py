"""
PARS Fonksiyonel Modülü — functools kütüphanesi Türkçe sarmalayıcısı
"""

import functools
from typing import Any, Callable, Iterable

__all__ = [
    'kismi', 'azalt', 'onbellek', 'sarmala', 'karsilastirici',
    'tek_yonlu_ozellik', 'toplam_azalt', 'boru', 'calistir_baglam',
    'sirala_anahtar',
]


def kismi(fonksiyon: Callable, *args: Any, **kwargs: Any) -> Callable:
    """Fonksiyonun bazı argümanlarını sabitle (partial)."""
    return functools.partial(fonksiyon, *args, **kwargs)


def azalt(fonksiyon: Callable, yinelenebilir: Iterable[Any],
          baslangic: Any = None) -> Any:
    """reduce."""
    if baslangic is None:
        return functools.reduce(fonksiyon, yinelenebilir)
    return functools.reduce(fonksiyon, yinelenebilir, baslangic)


def onbellek(azami: int = 128) -> Callable:
    """Fonksiyon sonuçlarını önbelleğe al (lru_cache)."""
    return functools.lru_cache(maxsize=azami)


def sarmala(fonksiyon: Callable) -> Callable:
    """Fonksiyon metadatasını koru (wraps) — dekoratör olarak kullanılır."""
    return functools.wraps(fonksiyon)


def karsilastirici(fonksiyon: Callable) -> Callable:
    """Karşılaştırma fonksiyonunu anahtara çevir."""
    return functools.cmp_to_key(fonksiyon)


def tek_yonlu_ozellik(fonksiyon: Callable) -> Callable:
    """Önbellekli özellik (cached_property)."""
    return functools.cached_property(fonksiyon)


def toplam_azalt(yinelenebilir: Iterable[Any]) -> Any:
    """Elemanları topla (reduce +)."""
    return functools.reduce(lambda a, b: a + b, yinelenebilir)


def boru(*fonksiyonlar: Callable) -> Callable:
    """Fonksiyonları soldan sağa zincirle."""
    def _boru(deger):
        for fonksiyon in fonksiyonlar:
            deger = fonksiyon(deger)
        return deger
    return _boru


def calistir_baglam(fonksiyon: Callable) -> Callable:
    """Fonksiyonu tek seferlik çağrı için hazırla."""
    return functools.partial(fonksiyon)


def sirala_anahtar(anahtar: Callable) -> Callable:
    """sorted(key=...) için yardımcı."""
    return functools.cmp_to_key(anahtar)
