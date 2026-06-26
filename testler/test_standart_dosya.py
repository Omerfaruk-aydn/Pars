"""
Standart kütüphane — dosya modülü testleri
"""

import pytest
import os
import tempfile
from pathlib import Path
from pars.standart.dosya import (
    oku, yaz, ekle, satirlari_oku, satirlari_yaz,
    var_mi, klasor_mu, dosya_mi, sil,
    klasor_olustur, klasor_sil, listele, boyut,
    uzanti, dosya_adi, tam_yol,
)


@pytest.fixture
def gecici_dizin(tmp_path):
    """Geçici dizin oluştur."""
    return tmp_path


class TestDosyaOkumaYazma:

    def test_yaz_ve_oku(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "merhaba dünya")
        assert oku(dosya) == "merhaba dünya"

    def test_ekle(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "satır 1\n")
        ekle(dosya, "satır 2\n")
        assert oku(dosya) == "satır 1\nsatır 2\n"

    def test_satirlari_oku(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "a\nb\nc")
        satirlar = satirlari_oku(dosya)
        assert len(satirlar) == 3
        assert satirlar[0].strip() == "a"

    def test_satirlari_yaz(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        satirlari_yaz(dosya, ["x\n", "y\n", "z\n"])
        assert oku(dosya) == "x\ny\nz\n"

    def test_turkce_karakter(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "çğıöşü ÇĞİÖŞÜ")
        assert oku(dosya) == "çğıöşü ÇĞİÖŞÜ"


class TestDosyaKontrol:

    def test_var_mi(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        assert var_mi(dosya) is False
        yaz(dosya, "test")
        assert var_mi(dosya) is True

    def test_klasor_mu(self, gecici_dizin):
        assert klasor_mu(str(gecici_dizin)) is True

    def test_dosya_mi(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "test")
        assert dosya_mi(dosya) is True


class TestDosyaIslemleri:

    def test_sil(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "test")
        assert var_mi(dosya) is True
        sil(dosya)
        assert var_mi(dosya) is False

    def test_klasor_olustur(self, gecici_dizin):
        klasor = str(gecici_dizin / "yeni_klasor")
        klasor_olustur(klasor)
        assert var_mi(klasor) is True
        assert klasor_mu(klasor) is True

    def test_listele(self, gecici_dizin):
        yaz(str(gecici_dizin / "a.txt"), "a")
        yaz(str(gecici_dizin / "b.txt"), "b")
        sonuclar = listele(str(gecici_dizin), "*.txt")
        assert len(sonuclar) == 2

    def test_boyut(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "merhaba")
        assert boyut(dosya) == 7

    def test_uzanti(self):
        assert uzanti("dosya.txt") == ".txt"
        assert uzanti("dosya.py") == ".py"

    def test_dosya_adi(self):
        assert dosya_adi("/yol/dosya.txt") == "dosya"
        assert dosya_adi("dosya.py") == "dosya"

    def test_tam_yol(self, gecici_dizin):
        dosya = str(gecici_dizin / "test.txt")
        yaz(dosya, "test")
        tam = tam_yol(dosya)
        assert os.path.isabs(tam)
