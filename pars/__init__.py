"""
PARS — Türkçe Programlama Dili

"Pars gibi hızlı. Türkçe gibi güzel."

Python altyapısını kullanan, tamamen Türkçe sözdizimli programlama dili.
"""

__version__ = "1.0.1"
__author__ = "PARS Topluluğu"
__license__ = "MIT"
__url__ = "https://github.com/pars-lang/pars"


def calistir(kod: str, dosya_adi: str = '<pars>',
             python_goster: bool = False) -> bool:
    """PARS kodunu çalıştır (kısayol)."""
    from pars.cekirdek.yurutucu import calistir as _calistir
    return _calistir(kod, dosya_adi=dosya_adi,
                     python_goster=python_goster)


def cevir(kod: str) -> str:
    """PARS kodunu Python koduna çevir (kısayol)."""
    from pars.cekirdek.ceviri import cevir as _cevir
    return _cevir(kod)


__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "__url__",
    "calistir",
    "cevir",
]
