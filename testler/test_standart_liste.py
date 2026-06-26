"""
Standart kütüphane — liste modülü testleri
"""

import pytest
from pars.standart.liste import (
    duzlestir, tekil, grupla, dondur_liste,
    sirala_ters, filtrele, haritala,
    bolustur, ortak_elemanlar, fark, birlesim,
    anahtarlar, degerler, ciftler,
    sozluk_filtrele, sozluk_birlestir, tersle,
    yigin_olustur, yigina_ekle, yigindan_al,
    kuyruk_olustur, kuyruga_ekle, kuyruktan_al,
)


class TestListeIslemleri:

    def test_duzlestir(self):
        assert duzlestir([[1, 2], [3, 4]]) == [1, 2, 3, 4]
        assert duzlestir([[1, [2, 3]], 4], 2) == [1, 2, 3, 4]

    def test_tekil(self):
        assert tekil([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
        assert tekil(["a", "b", "a", "c"]) == ["a", "b", "c"]

    def test_grupla(self):
        assert grupla([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
        assert grupla([1, 2, 3], 1) == [[1], [2], [3]]

    def test_dondur_liste(self):
        assert dondur_liste([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
        assert dondur_liste([1, 2, 3], 0) == [1, 2, 3]

    def test_sirala_ters(self):
        assert sirala_ters([3, 1, 2]) == [3, 2, 1]

    def test_filtrele(self):
        assert filtrele(lambda x: x > 3, [1, 2, 3, 4, 5]) == [4, 5]

    def test_haritala(self):
        assert haritala(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]

    def test_bolustur(self):
        dogrular, yanlislar = bolustur([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        assert dogrular == [2, 4]
        assert yanlislar == [1, 3, 5]

    def test_ortak_elemanlar(self):
        assert ortak_elemanlar([1, 2, 3], [2, 3, 4]) == [2, 3]

    def test_fark(self):
        assert fark([1, 2, 3, 4], [2, 4]) == [1, 3]

    def test_birlesim(self):
        assert birlesim([1, 2], [3, 4]) == [1, 2, 3, 4]
        assert birlesim([1, 2], [2, 3]) == [1, 2, 3]


class TestSozlukIslemleri:

    def test_anahtarlar(self):
        assert anahtarlar({"a": 1, "b": 2}) == ["a", "b"]

    def test_degerler(self):
        assert degerler({"a": 1, "b": 2}) == [1, 2]

    def test_ciftler(self):
        assert ciftler({"a": 1}) == [("a", 1)]

    def test_sozluk_filtrele(self):
        sonuc = sozluk_filtrele({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
        assert sonuc == {"b": 2, "c": 3}

    def test_sozluk_birlestir(self):
        assert sozluk_birlestir({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    def test_tersle(self):
        assert tersle({"a": 1, "b": 2}) == {1: "a", 2: "b"}


class TestYiginKuyruk:

    def test_yigin(self):
        yigin = yigin_olustur()
        yigina_ekle(yigin, 1)
        yigina_ekle(yigin, 2)
        yigina_ekle(yigin, 3)
        assert yigindan_al(yigin) == 3
        assert yigindan_al(yigin) == 2
        assert yigindan_al(yigin) == 1

    def test_yigin_bos(self):
        yigin = yigin_olustur()
        with pytest.raises(IndexError):
            yigindan_al(yigin)

    def test_kuyruk(self):
        kuyruk = kuyruk_olustur()
        kuyruga_ekle(kuyruk, 1)
        kuyruga_ekle(kuyruk, 2)
        kuyruga_ekle(kuyruk, 3)
        assert kuyruktan_al(kuyruk) == 1
        assert kuyruktan_al(kuyruk) == 2
        assert kuyruktan_al(kuyruk) == 3

    def test_kuyruk_bos(self):
        kuyruk = kuyruk_olustur()
        with pytest.raises(IndexError):
            kuyruktan_al(kuyruk)
