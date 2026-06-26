"""
Standart kütüphane — zaman modülü testleri
"""

import pytest
from datetime import datetime, date, timedelta
from pars.standart.zaman import (
    TURKCE_GUNLER, TURKCE_AYLAR,
    simdi, bugun, zaman_damgasi,
    tarih, saat_olustur, fark, bicimle, cozmle,
    gun_adi, ay_adi, yil, ay, gun,
    is_gunu_mu, hafta_sonu_mu, gun_ekle,
)


class TestSabitler:

    def test_turkce_gunler(self):
        assert len(TURKCE_GUNLER) == 7
        assert TURKCE_GUNLER[0] == "Pazartesi"
        assert TURKCE_GUNLER[6] == "Pazar"

    def test_turkce_aylar(self):
        assert len(TURKCE_AYLAR) == 12
        assert TURKCE_AYLAR[0] == "Ocak"
        assert TURKCE_AYLAR[11] == "Aralık"


class TestZamanFonksiyonlari:

    def test_simdi(self):
        simdi_zaman = simdi()
        assert isinstance(simdi_zaman, datetime)

    def test_bugun(self):
        bugun_tarih = bugun()
        assert isinstance(bugun_tarih, date)

    def test_zaman_damgasi(self):
        damga = zaman_damgasi()
        assert isinstance(damga, float)
        assert damga > 0

    def test_tarih(self):
        t = tarih(2024, 1, 15)
        assert t.year == 2024
        assert t.month == 1
        assert t.day == 15

    def test_saat_olustur(self):
        s = saat_olustur(14, 30, 45)
        assert s.hour == 14
        assert s.minute == 30
        assert s.second == 45


class TestTarihIslemleri:

    def test_fark(self):
        baslangic = tarih(2024, 1, 1)
        bitis = tarih(2024, 1, 11)
        fark_sure = fark(baslangic, bitis)
        assert fark_sure.days == 10

    def test_bicimle(self):
        t = tarih(2024, 1, 15)
        assert bicimle(t, "%d.%m.%Y") == "15.01.2024"

    def test_cozmle(self):
        t = cozmle("15.01.2024", "%d.%m.%Y")
        assert t.year == 2024
        assert t.month == 1
        assert t.day == 15

    def test_gun_adi(self):
        # 15 Ocak 2024 = Pazartesi
        t = tarih(2024, 1, 15)
        assert gun_adi(t) == "Pazartesi"

    def test_ay_adi(self):
        t = tarih(2024, 3, 1)
        assert ay_adi(t) == "Mart"

    def test_yil_ay_gun(self):
        t = tarih(2024, 6, 15)
        assert yil(t) == 2024
        assert ay(t) == 6
        assert gun(t) == 15


class TestKontrolFonksiyonlari:

    def test_is_gunu_mu(self):
        # 15 Ocak 2024 = Pazartesi
        assert is_gunu_mu(tarih(2024, 1, 15)) is True
        # 13 Ocak 2024 = Cumartesi
        assert is_gunu_mu(tarih(2024, 1, 13)) is False

    def test_hafta_sonu_mu(self):
        assert hafta_sonu_mu(tarih(2024, 1, 13)) is True
        assert hafta_sonu_mu(tarih(2024, 1, 15)) is False

    def test_gun_ekle(self):
        t = tarih(2024, 1, 1)
        yeni = gun_ekle(t, 10)
        assert yeni.day == 11
