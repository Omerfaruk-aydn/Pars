"""
PARS Kopya Modülü — copy kütüphanesi Türkçe sarmalayıcısı
"""

import copy
from typing import Any

__all__ = ['kopyala', 'derin_kopyala', 'yedek_al', 'geri_yukle', 'esit_mi']


def kopyala(nesne: Any) -> Any:
    """Sığ kopya."""
    return copy.copy(nesne)


def derin_kopyala(nesne: Any) -> Any:
    """Derin kopya."""
    return copy.deepcopy(nesne)


def yedek_al(nesne: Any):
    """Nesnenin derin kopyasını yedek olarak döndür."""
    return copy.deepcopy(nesne)


def geri_yukle(hedef: dict, yedek: dict) -> dict:
    """Sözlüğü yedekten geri yükle."""
    hedef.clear()
    hedef.update(yedek)
    return hedef


def esit_mi(a: Any, b: Any) -> bool:
    return a == b
