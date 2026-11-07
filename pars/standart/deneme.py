"""
PARS Deneme Modülü — unittest kütüphanesi Türkçe sarmalayıcısı
"""

import unittest
from typing import Any, Callable, Optional, Sequence, Type

__all__ = [
    'Deneme', 'TestDurumu', 'kosum', 'calistir', 'iddia_esit',
    'iddia_dogru', 'iddia_yanlis', 'iddia_icinde', 'atla',
]


class Deneme(unittest.TestCase):
    """unittest.TestCase Türkçe sarmalayıcısı."""

    def iddia_esit(self, a: Any, b: Any, mesaj: Optional[str] = None) -> None:
        self.assertEqual(a, b, mesaj)

    def iddia_esit_degil(self, a: Any, b: Any,
                         mesaj: Optional[str] = None) -> None:
        self.assertNotEqual(a, b, mesaj)

    def iddia_dogru(self, deger: Any, mesaj: Optional[str] = None) -> None:
        self.assertTrue(deger, mesaj)

    def iddia_yanlis(self, deger: Any, mesaj: Optional[str] = None) -> None:
        self.assertFalse(deger, mesaj)

    def iddia_icinde(self, uye: Any, kap: Any,
                     mesaj: Optional[str] = None) -> None:
        self.assertIn(uye, kap, mesaj)

    def iddia_hata(self, istisna: Type[BaseException],
                   fonksiyon: Callable, *args: Any, **kwargs: Any) -> None:
        with self.assertRaises(istisna):
            fonksiyon(*args, **kwargs)


TestDurumu = unittest.TestResult


def calistir(test_sinifi: Type[Deneme], ayrinti: int = 2) -> unittest.TestResult:
    """Test sınıfını çalıştır."""
    yukleyici = unittest.TestLoader()
    takim = yukleyici.loadTestsFromTestCase(test_sinifi)
    kosucu = unittest.TextTestRunner(verbosity=ayrinti)
    return kosucu.run(takim)


def kosum(testler: Sequence[Any], ayrinti: int = 2) -> unittest.TestResult:
    takim = unittest.TestSuite(testler)
    kosucu = unittest.TextTestRunner(verbosity=ayrinti)
    return kosucu.run(takim)


def iddia_esit(a: Any, b: Any, mesaj: Optional[str] = None) -> None:
    if a != b:
        raise AssertionError(mesaj or f'{a!r} != {b!r}')


def iddia_dogru(deger: Any, mesaj: Optional[str] = None) -> None:
    if not deger:
        raise AssertionError(mesaj or f'doğru bekleniyordu: {deger!r}')


def iddia_yanlis(deger: Any, mesaj: Optional[str] = None) -> None:
    if deger:
        raise AssertionError(mesaj or f'yanlış bekleniyordu: {deger!r}')


def iddia_icinde(uye: Any, kap: Any, mesaj: Optional[str] = None) -> None:
    if uye not in kap:
        raise AssertionError(mesaj or f'{uye!r} içinde değil')


def atla(sebep: str = '') -> None:
    raise unittest.SkipTest(sebep)
