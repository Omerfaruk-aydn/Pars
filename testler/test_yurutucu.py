"""
Yürütücü entegrasyon testleri
"""

import pytest
from unittest.mock import patch
from io import StringIO
from pars.cekirdek.yurutucu import calistir


class TestTemelCalistirma:

    def test_basit_yaz(self, capsys):
        assert calistir("yaz('merhaba')") is True
        çıktı = capsys.readouterr().out
        assert 'merhaba' in çıktı

    def test_dogru_degeri_turkce(self, capsys):
        calistir("yaz(doğru)")
        çıktı = capsys.readouterr().out
        assert 'doğru' in çıktı

    def test_yanlis_degeri_turkce(self, capsys):
        calistir("yaz(yanlış)")
        çıktı = capsys.readouterr().out
        assert 'yanlış' in çıktı

    def test_yok_degeri_turkce(self, capsys):
        calistir("yaz(yok)")
        çıktı = capsys.readouterr().out
        assert 'yok' in çıktı

    def test_degisken_atama(self):
        assert calistir("x = 5\niddia x == 5") is True

    def test_turkce_degisken(self):
        assert calistir("yaş = 25\niddia yaş == 25") is True

    def test_turkce_karakterli_degisken(self):
        assert calistir("şehir = 'İstanbul'\niddia şehir == 'İstanbul'") is True


class TestKosullar:

    def test_kosul(self, capsys):
        calistir("eğer 1 > 0:\n    yaz('doğru')")
        assert 'doğru' in capsys.readouterr().out

    def test_if_else(self, capsys):
        calistir("x = 5\neğer x > 10:\n    yaz('büyük')\ndeğilse:\n    yaz('küçük')")
        assert 'küçük' in capsys.readouterr().out

    def test_if_elif_else(self, capsys):
        calistir("x = 5\neğer x > 10:\n    yaz('büyük')\nyoksa x > 3:\n    yaz('orta')\ndeğilse:\n    yaz('küçük')")
        assert 'orta' in capsys.readouterr().out


class TestDonguler:

    def test_dongu(self, capsys):
        calistir("için i içinde aralık(3):\n    yaz(i)")
        çıktı = capsys.readouterr().out
        assert '0' in çıktı and '1' in çıktı and '2' in çıktı

    def test_iken_dongu(self, capsys):
        calistir("x = 3\niken x > 0:\n    yaz(x)\n    x -= 1")
        çıktı = capsys.readouterr().out
        assert '3' in çıktı and '2' in çıktı and '1' in çıktı


class TestFonksiyonlar:

    def test_fonksiyon_tanim_ve_cagri(self, capsys):
        calistir("fonksiyon selamla(isim):\n    yaz(f'Merhaba {isim}')\nselamla('PARS')")
        assert 'Merhaba PARS' in capsys.readouterr().out

    def test_fonksiyon_dondur(self):
        assert calistir("fonksiyon topla(a, b):\n    döndür a + b\niddia topla(3, 4) == 7") is True

    def test_lambda(self):
        assert calistir("kare = lambda x: x ** 2\niddia kare(5) == 25") is True


class TestSiniflar:

    def test_sinif_tanimlama(self):
        kod = 'sınıf Araba:\n    fonksiyon __init__(öz, marka):\n        öz.marka = marka\naraba = Araba("Toyota")\niddia araba.marka == "Toyota"'
        assert calistir(kod) is True

    def test_sinif_metot(self, capsys):
        kod = 'sınıf Hayvan:\n    fonksiyon __init__(öz, isim):\n        öz.isim = isim\n    fonksiyon konus(öz):\n        döndür f"{öz.isim} konuşuyor"\nhayvan = Hayvan("Kedi")\nyaz(hayvan.konus())'
        calistir(kod)
        assert 'Kedi konuşuyor' in capsys.readouterr().out


class TestHataYonetimi:

    def test_hata_yonetimi(self):
        assert calistir("1/0") is False

    def test_syntax_hatasi(self):
        assert calistir("eğer:") is False

    def test_dene_haric(self, capsys):
        kod = "dene:\n    1/0\nhariç SıfıraBölmeHatası:\n    yaz('hata yakalandı')"
        calistir(kod)
        assert 'hata yakalandı' in capsys.readouterr().out


class TestIceAktarma:

    def test_iceaktar(self):
        assert calistir("içe_aktar os\niddia os.getcwd()") is True

    def test_numpy_iceaktar(self):
        pytest.importorskip("numpy")
        assert calistir("içe_aktar numpy olarak np\niddia np.__version__") is True


class TestBuiltins:

    def test_uzunluk(self):
        assert calistir("iddia uzunluk([1,2,3]) == 3") is True

    def test_tip(self, capsys):
        calistir("yaz(tip(42))")
        assert 'int' in capsys.readouterr().out

    def test_aralik(self):
        assert calistir("iddia uzunluk(liste(aralık(5))) == 5") is True

    def test_sirala(self):
        assert calistir("iddia sırala([3,1,2]) == [1,2,3]") is True

    def test_tumu(self):
        assert calistir("iddia tümü([True, True, True]) is True") is True

    def test_herhangi(self):
        assert calistir("iddia herhangi([False, True, False]) is True") is True
