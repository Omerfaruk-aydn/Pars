"""
Standart kütüphane — metin modülü testleri
"""

import pytest
from pars.standart.metin import (
    buyuk_harf, kucuk_harf, bas_buyuk, her_bas_buyuk,
    bosluk_temizle, bol, satirlara_bol, birlestir,
    degistir, iceriyor_mu, ile_basliyor_mu, ile_bitiyor_mu,
    bul, bul_sagdan, say, tekrarla, tersine_cevir,
    doldur_sola, doldur_saga, ortala,
    sayi_mi, harf_mi, alfanumerik_mi, bos_mu,
    buyuk_harf_mi, kucuk_harf_mi,
)


class TestBuyukKucukHarf:

    def test_buyuk_harf(self):
        assert buyuk_harf("merhaba") == "MERHABA"
        assert buyuk_harf("Merhaba Dünya") == "MERHABA DÜNYA"

    def test_kucuk_harf(self):
        assert kucuk_harf("MERHABA") == "merhaba"
        assert kucuk_harf("Merhaba Dünya") == "merhaba dünya"

    def test_bas_buyuk(self):
        assert bas_buyuk("merhaba") == "Merhaba"
        assert bas_buyuk("MERHABA") == "Merhaba"

    def test_her_bas_buyuk(self):
        assert her_bas_buyuk("merhaba dünya") == "Merhaba Dünya"


class TestBoslukIslemleri:

    def test_bosluk_temizle_her(self):
        assert bosluk_temizle("  merhaba  ") == "merhaba"

    def test_bosluk_temizle_sol(self):
        assert bosluk_temizle("  merhaba  ", "sol") == "merhaba  "

    def test_bosluk_temizle_sag(self):
        assert bosluk_temizle("  merhaba  ", "sag") == "  merhaba"


class TestBolmeBirlestirme:

    def test_bol(self):
        assert bol("a,b,c", ",") == ["a", "b", "c"]

    def test_bol_kez(self):
        assert bol("a,b,c,d", ",", 2) == ["a", "b", "c,d"]

    def test_satirlara_bol(self):
        assert satirlara_bol("a\nb\nc") == ["a", "b", "c"]

    def test_birlestir(self):
        assert birlestir(", ", ["a", "b", "c"]) == "a, b, c"


class TestArama:

    def test_iceriyor_mu(self):
        assert iceriyor_mu("merhaba dünya", "dünya") is True
        assert iceriyor_mu("merhaba", "dünya") is False

    def test_ile_basliyor_mu(self):
        assert ile_basliyor_mu("merhaba", "mer") is True
        assert ile_basliyor_mu("merhaba", "dünya") is False

    def test_ile_bitiyor_mu(self):
        assert ile_bitiyor_mu("merhaba", "haba") is True
        assert ile_bitiyor_mu("merhaba", "mer") is False

    def test_bul(self):
        assert bul("merhaba dünya", "dünya") == 8
        assert bul("merhaba", "x") == -1

    def test_bul_sagdan(self):
        assert bul_sagdan("abcabc", "abc") == 3

    def test_say(self):
        assert say("abcabc", "abc") == 2
        assert say("merhaba", "a") == 2


class TestDonusum:

    def test_degistir(self):
        assert degistir("merhaba dünya", "dünya", "PARS") == "merhaba PARS"

    def test_tersine_cevir(self):
        assert tersine_cevir("abc") == "cba"

    def test_tekrarla(self):
        assert tekrarla("abc", 3) == "abcabcabc"


class TestDoldurma:

    def test_doldur_sola(self):
        assert doldur_sola("42", 5, "0") == "00042"

    def test_doldur_saga(self):
        assert doldur_saga("42", 5, "0") == "42000"

    def test_ortala(self):
        assert ortala("abc", 7) == "  abc  "


class TestKontrol:

    def test_sayi_mi(self):
        assert sayi_mi("42") is True
        assert sayi_mi("3.14") is True
        assert sayi_mi("abc") is False

    def test_harf_mi(self):
        assert harf_mi("abc") is True
        assert harf_mi("abc123") is False

    def test_alfanumerik_mi(self):
        assert alfanumerik_mi("abc123") is True
        assert alfanumerik_mi("abc 123") is False

    def test_bos_mu(self):
        assert bos_mu("") is True
        assert bos_mu("   ") is True
        assert bos_mu("abc") is False

    def test_buyuk_harf_mi(self):
        assert buyuk_harf_mi("ABC") is True
        assert buyuk_harf_mi("Abc") is False

    def test_kucuk_harf_mi(self):
        assert kucuk_harf_mi("abc") is True
        assert kucuk_harf_mi("Abc") is False
