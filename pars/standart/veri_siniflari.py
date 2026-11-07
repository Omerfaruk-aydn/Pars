"""
PARS Veri Sınıfları Modülü — dataclasses kütüphanesi Türkçe sarmalayıcısı
"""

import dataclasses
from typing import Any, Callable

alan = dataclasses.field
alan_varsayilan = dataclasses.field
alan_varsayilan_fabrika = dataclasses.field
Alan = dataclasses.field

__all__ = [
    'veri_sinifi', 'alan', 'Alan', 'alan_varsayilan',
    'alan_varsayilan_fabrika', 'degismez', 'sirali', 'yuvalanmis',
    'sozluge_cevir', 'demete_cevir', 'degistir', 'alanlar',
]


def veri_sinifi(_sinif: Callable = None, **secenekler: Any):
    """
    Sınıfı veri sınıfına çevir (dataclass dekoratörü).

    Kullanım:
        @veri_sinifi
        sınıf Kisi:
            ad: str
            yas: int = 0
    """
    if _sinif is None:
        return lambda s: dataclasses.dataclass(s, **secenekler)
    return dataclasses.dataclass(_sinif, **secenekler)


def degismez(_sinif: Callable = None, **secenekler: Any):
    """Değiştirilemez veri sınıfı (frozen=True)."""
    secenekler.setdefault('frozen', True)
    return veri_sinifi(_sinif, **secenekler)


def sirali(_sinif: Callable = None, **secenekler: Any):
    """Sıralanabilir veri sınıfı (order=True)."""
    secenekler.setdefault('order', True)
    return veri_sinifi(_sinif, **secenekler)


def yuvalanmis(_sinif: Callable = None):
    """Yuvalanmış sözlük/sözlük desteği (slots yok, basit sarmalayıcı)."""
    return veri_sinifi(_sinif)


def sozluge_cevir(nesne: Any) -> dict:
    return dataclasses.asdict(nesne)


def demete_cevir(nesne: Any) -> tuple:
    return dataclasses.astuple(nesne)


def degistir(nesne: Any, **degisiklikler: Any) -> Any:
    return dataclasses.replace(nesne, **degisiklikler)


def alanlar(sinif: Any) -> tuple:
    return dataclasses.fields(sinif)
