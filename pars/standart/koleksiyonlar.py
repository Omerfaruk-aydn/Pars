"""
PARS Koleksiyonlar Modülü — collections kütüphanesi Türkçe sarmalayıcısı
"""

from collections import (
    Counter,
    OrderedDict,
    ChainMap,
    defaultdict,
    deque,
    namedtuple,
)
from typing import Any, Iterable, List, Optional

__all__ = [
    'Sayac', 'sayaç', 'SiraliSozluk', 'sirali_sozluk', 'ZincirSozluk',
    'VarsayilanSozluk', 'CiftUclu', 'AdliDemet', 'say',
    'en_sik', 'en_az', 'elemanlar', 'ilk_n', 'son_n', 'dondur',
]


# ── Sınıf takma adları ───────────────────────────────────────────────────

Sayac = Counter
sayaç = Counter
SiraliSozluk = OrderedDict
sirali_sozluk = OrderedDict
ZincirSozluk = ChainMap
VarsayilanSozluk = defaultdict
CiftUclu = deque
AdliDemet = namedtuple


# ── Yardımcı fonksiyonlar ────────────────────────────────────────────────

def say(koleksiyon: Iterable[Any]) -> dict:
    """Elemanların tekrar sayısını sözlük olarak döndür."""
    return dict(Counter(koleksiyon))


def en_sik(koleksiyon: Iterable[Any], n: Optional[int] = None):
    """En sık geçen eleman(lar)."""
    sayac = Counter(koleksiyon)
    if n is None:
        return sayac.most_common(1)[0][0]
    return sayac.most_common(n)


def en_az(koleksiyon: Iterable[Any], n: Optional[int] = None):
    """En az geçen eleman(lar)."""
    sayac = Counter(koleksiyon)
    sirali = sorted(sayac.items(), key=lambda x: x[1])
    if n is None:
        return sirali[0][0]
    return sirali[:n]


def elemanlar(sayac: 'Counter') -> List[Any]:
    """Sayacı tekrar sayılarına göre aç."""
    return list(sayac.elements())


def ilk_n(koleksiyon: Iterable[Any], n: int) -> list:
    """İlk n eleman."""
    return list(koleksiyon)[:n]


def son_n(koleksiyon: Iterable[Any], n: int) -> list:
    """Son n eleman."""
    return list(koleksiyon)[-n:] if n else []


def dondur(koleksiyon: Iterable[Any], n: int) -> list:
    """CiftUclu üzerinde döndürme."""
    kuyruk = deque(koleksiyon)
    kuyruk.rotate(n)
    return list(kuyruk)
