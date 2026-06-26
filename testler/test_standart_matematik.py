"""
Standart kütüphane — matematik modülü testleri
"""

import pytest
import math
from pars.standart.matematik import (
    PI, E, TAU, SONSUZ, NAN,
    kare_kok, us, mutlak, yuvarlak, tavan, taban_al, mod,
    sinus, kosinus, tanjant,
    logaritma, log10, log2, exp,
    faktoriyel, kombinasyon, permutasyon, obeb, okek,
    ortalama, medyan, standart_sapma, varyans,
)


class TestSabitler:

    def test_pi(self):
        assert PI == math.pi

    def test_e(self):
        assert E == math.e

    def test_tau(self):
        assert TAU == math.tau

    def test_sonsuz(self):
        assert SONSUZ == math.inf

    def test_nan(self):
        assert math.isnan(NAN)


class TestTemelIslemler:

    def test_kare_kok(self):
        assert kare_kok(16) == 4.0
        assert kare_kok(0) == 0.0
        assert kare_kok(2) == pytest.approx(math.sqrt(2))

    def test_us(self):
        assert us(2, 10) == 1024.0
        assert us(5, 0) == 1.0
        assert us(9, 0.5) == 3.0

    def test_mutlak(self):
        assert mutlak(-5) == 5
        assert mutlak(5) == 5
        assert mutlak(0) == 0

    def test_yuvarlak(self):
        assert yuvarlak(3.14159, 2) == 3.14
        assert yuvarlak(3.5) == 4
        assert yuvarlak(3.14159, 4) == 3.1416

    def test_tavan(self):
        assert tavan(3.2) == 4
        assert tavan(3.0) == 3
        assert tavan(-3.2) == -3

    def test_taban_al(self):
        assert taban_al(3.8) == 3
        assert taban_al(3.0) == 3
        assert taban_al(-3.8) == -4

    def test_mod(self):
        assert mod(10, 3) == 1
        assert mod(10, 2) == 0
        assert mod(7, 5) == 2


class TestTrigonometri:

    def test_sinus(self):
        assert sinus(0) == 0.0
        assert sinus(math.pi / 2) == pytest.approx(1.0)

    def test_kosinus(self):
        assert kosinus(0) == 1.0
        assert kosinus(math.pi) == pytest.approx(-1.0)

    def test_tanjant(self):
        assert tanjant(0) == 0.0
        assert tanjant(math.pi / 4) == pytest.approx(1.0)


class TestLogaritma:

    def test_logaritma(self):
        assert logaritma(1) == 0.0
        assert logaritma(math.e) == pytest.approx(1.0)
        assert logaritma(100, 10) == pytest.approx(2.0)

    def test_log10(self):
        assert log10(1) == 0.0
        assert log10(10) == pytest.approx(1.0)
        assert log10(100) == pytest.approx(2.0)

    def test_log2(self):
        assert log2(1) == 0.0
        assert log2(2) == pytest.approx(1.0)
        assert log2(8) == pytest.approx(3.0)

    def test_exp(self):
        assert exp(0) == 1.0
        assert exp(1) == pytest.approx(math.e)


class TestKombinatorik:

    def test_faktoriyel(self):
        assert faktoriyel(0) == 1
        assert faktoriyel(1) == 1
        assert faktoriyel(5) == 120
        assert faktoriyel(10) == 3628800

    def test_kombinasyon(self):
        assert kombinasyon(5, 2) == 10
        assert kombinasyon(10, 3) == 120
        assert kombinasyon(5, 0) == 1

    def test_permutasyon(self):
        assert permutasyon(5, 2) == 20
        assert permutasyon(5) == 120

    def test_obeb(self):
        assert obeb(12, 8) == 4
        assert obeb(15, 25) == 5
        assert obeb(7, 13) == 1

    def test_okek(self):
        assert okek(4, 6) == 12
        assert okek(3, 5) == 15


class TestIstatistik:

    def test_ortalama(self):
        assert ortalama([1, 2, 3, 4, 5]) == 3.0
        assert ortalama([10, 20]) == 15.0

    def test_medyan(self):
        assert medyan([1, 2, 3, 4, 5]) == 3
        assert medyan([1, 2, 3, 4]) == 2.5

    def test_standart_sapma(self):
        sapma = standart_sapma([2, 4, 4, 4, 5, 5, 7, 9])
        assert sapma == pytest.approx(2.138, abs=0.01)

    def test_varyans(self):
        v = varyans([2, 4, 4, 4, 5, 5, 7, 9])
        assert v == pytest.approx(4.571, abs=0.01)
