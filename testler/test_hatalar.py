"""
Hata yönetimi testleri
"""

import pytest
import sys
from io import StringIO
from pars.cekirdek.hatalar import hata_goster, HATA_TURLERI, HATA_IPUCLARI
from pars.cekirdek.yurutucu import calistir


class TestHataTurleri:

    def test_tum_hata_turleri_tanimli(self):
        beklenen_turler = [
            'SyntaxError', 'NameError', 'TypeError', 'ValueError',
            'IndexError', 'KeyError', 'AttributeError', 'ImportError',
            'ModuleNotFoundError', 'FileNotFoundError', 'PermissionError',
            'ZeroDivisionError', 'OverflowError', 'MemoryError',
            'RecursionError', 'TimeoutError', 'ConnectionError',
            'OSError', 'RuntimeError', 'NotImplementedError',
        ]
        for tur in beklenen_turler:
            assert tur in HATA_TURLERI

    def test_hata_turleri_turkce(self):
        for tur, turkce in HATA_TURLERI.items():
            assert len(turkce) > 0
            assert turkce[0].isalpha()


class TestHataIpuclari:

    def test_ipuclari_tanimli(self):
        assert len(HATA_IPUCLARI) > 10

    def test_ipuclari_turkce(self):
        for ipucu in HATA_IPUCLARI.values():
            assert len(ipucu) > 10


class TestHataGosterimi:

    def test_name_error_gosterilir(self, capsys):
        kod = "tanımsız_değişken"
        sonuc = calistir(kod)
        assert sonuc is False
        hata_cıktısı = capsys.readouterr().err
        assert 'Ad Hatası' in hata_cıktısı or 'NameError' in hata_cıktısı

    def test_type_error_gosterilir(self, capsys):
        kod = "'abc' + 5"
        sonuc = calistir(kod)
        assert sonuc is False
        hata_cıktısı = capsys.readouterr().err
        assert 'Tür Hatası' in hata_cıktısı or 'TypeError' in hata_cıktısı

    def test_zero_division_gosterilir(self, capsys):
        kod = "1/0"
        sonuc = calistir(kod)
        assert sonuc is False
        hata_cıktısı = capsys.readouterr().err
        assert 'Sıfıra Bölme' in hata_cıktısı or 'ZeroDivision' in hata_cıktısı

    def test_index_error_gosterilir(self, capsys):
        kod = "[1,2,3][10]"
        sonuc = calistir(kod)
        assert sonuc is False
        hata_cıktısı = capsys.readouterr().err
        assert 'İndeks Hatası' in hata_cıktısı or 'IndexError' in hata_cıktısı

    def test_syntax_error_gosterilir(self, capsys):
        kod = "eğer:"
        sonuc = calistir(kod)
        assert sonuc is False
        hata_cıktısı = capsys.readouterr().err
        assert len(hata_cıktısı) > 0

    def test_ipucu_gosterilir(self, capsys):
        kod = "tanımsız_değişken"
        calistir(kod)
        hata_cıktısı = capsys.readouterr().err
        assert 'İpucu' in hata_cıktısı or 'ipucu' in hata_cıktısı or 'Değişkeni' in hata_cıktısı
