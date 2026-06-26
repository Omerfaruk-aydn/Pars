"""
Çevirici birim testleri.
Her test izole ve bağımsız olmalı.
"""

import pytest
from pars.cekirdek.ceviri import cevir, syntax_kontrol


class TestTemelCeviri:

    def test_eger_cevirisi(self):
        assert cevir("eğer x > 0:") == "if x > 0:"

    def test_eger_ascii_cevirisi(self):
        assert cevir("eger x > 0:") == "if x > 0:"

    def test_degilse_cevirisi(self):
        assert cevir("değilse:") == "else:"

    def test_degilse_ascii_cevirisi(self):
        assert cevir("degilse:") == "else:"

    def test_yoksa_cevirisi(self):
        assert cevir("yoksa x == 0:") == "elif x == 0:"

    def test_iken_cevirisi(self):
        assert cevir("iken x < 10:") == "while x < 10:"

    def test_icin_cevirisi(self):
        assert cevir("için i içinde aralık(10):") == "for i in aralık(10):"

    def test_icin_ascii_cevirisi(self):
        assert cevir("icin i icinde aralik(10):") == "for i in aralik(10):"

    def test_fonksiyon_cevirisi(self):
        assert cevir("fonksiyon ad():") == "def ad():"

    def test_dondur_cevirisi(self):
        assert cevir("döndür sonuç") == "return sonuç"

    def test_dondur_ascii_cevirisi(self):
        assert cevir("dondur sonuc") == "return sonuc"

    def test_sinif_cevirisi(self):
        assert cevir("sınıf Ad:") == "class Ad:"

    def test_sinif_ascii_cevirisi(self):
        assert cevir("sinif Ad:") == "class Ad:"

    def test_iceaktar_cevirisi(self):
        assert cevir("içe_aktar numpy olarak np") == "import numpy as np"

    def test_iceaktar_ascii_cevirisi(self):
        assert cevir("ice_aktar numpy olarak np") == "import numpy as np"

    def test_denaktar_cevirisi(self):
        assert cevir("den_aktar flask içe_aktar Flask") == "from flask import Flask"

    def test_dene_cevirisi(self):
        assert cevir("dene:") == "try:"

    def test_haric_cevirisi(self):
        assert cevir("hariç Hata:") == "except Exception:"

    def test_haric_ascii_cevirisi(self):
        assert cevir("haric Hata:") == "except Exception:"

    def test_sonunda_cevirisi(self):
        assert cevir("sonunda:") == "finally:"

    def test_yukselt_cevirisi(self):
        assert cevir("yükselt Hata()") == "raise Exception()"

    def test_yukselt_ascii_cevirisi(self):
        assert cevir("yukselt Hata()") == "raise Exception()"

    def test_ile_cevirisi(self):
        assert cevir("ile f() olarak x:") == "with f() as x:"

    def test_gec_cevirisi(self):
        assert cevir("geç") == "pass"

    def test_gec_ascii_cevirisi(self):
        assert cevir("gec") == "pass"

    def test_kes_cevirisi(self):
        assert cevir("kes") == "break"

    def test_devam_cevirisi(self):
        assert cevir("devam") == "continue"

    def test_sil_cevirisi(self):
        assert cevir("sil x") == "del x"

    def test_iddia_cevirisi(self):
        assert cevir("iddia x > 0") == "assert x > 0"


class TestMantiksalCeviri:

    def test_ve_cevirisi(self):
        assert cevir("x ve y") == "x and y"

    def test_veya_cevirisi(self):
        assert cevir("x veya y") == "x or y"

    def test_degil_cevirisi(self):
        assert cevir("değil x") == "not x"

    def test_degil_ascii_cevirisi(self):
        assert cevir("degil x") == "not x"


class TestDegerCeviri:

    def test_dogru_cevirisi(self):
        assert cevir("doğru") == "True"

    def test_dogru_ascii_cevirisi(self):
        assert cevir("dogru") == "True"

    def test_yanlis_cevirisi(self):
        assert cevir("yanlış") == "False"

    def test_yanlis_ascii_cevirisi(self):
        assert cevir("yanlis") == "False"

    def test_yok_cevirisi(self):
        assert cevir("yok") == "None"


class TestAsyncCeviri:

    def test_eszamansiz_cevirisi(self):
        assert cevir("eşzamansız fonksiyon ad():") == "async def ad():"

    def test_eszamansiz_ascii_cevirisi(self):
        assert cevir("esezamansiz fonksiyon ad():") == "async def ad():"

    def test_bekle_cevirisi(self):
        assert cevir("bekle asyncio.sleep(1)") == "await asyncio.sleep(1)"


class TestStringKoruma:

    def test_string_icinde_degismez_cift_tirnak(self):
        assert cevir('"eğer bu değişmemeli"') == '"eğer bu değişmemeli"'

    def test_string_icinde_degismez_tek_tirnak(self):
        assert cevir("'için iken değilse'") == "'için iken değilse'"

    def test_uclu_string_korunur(self):
        kod = '"""eğer yoksa değilse"""'
        assert cevir(kod) == kod

    def test_fstring_ic_kisim_korunur(self):
        assert cevir('f"Merhaba {isim}"') == 'f"Merhaba {isim}"'

    def test_yorum_satiri_korunur(self):
        assert cevir("# eğer bu yorum değilse") == "# eğer bu yorum değilse"

    def test_string_icinde_tum_anahtar_kelimeler(self):
        kod = '"eğer iken için sınıf fonksiyon döndür"'
        assert cevir(kod) == kod


class TestTurkceKarakter:

    def test_turkce_degisken_korunur(self):
        assert cevir("yaş = 25") == "yaş = 25"

    def test_turkce_fonksiyon_ismi_korunur(self):
        assert cevir("fonksiyon selamla():") == "def selamla():"

    def test_oz_korunur(self):
        assert cevir("fonksiyon __init__(öz):") == "def __init__(öz):"

    def test_unicode_donusum_gerekmez(self):
        kod = "öğrenci_adı = 'Ahmet'"
        assert cevir(kod) == kod

    def test_turkce_karakterli_degiskenler(self):
        kod = "şehir = 'İstanbul'\nçağrı = 42"
        assert cevir(kod) == kod


class TestCokSatirli:

    def test_if_else_blok(self):
        kod = "eğer x > 0:\n    yaz('pozitif')\ndeğilse:\n    yaz('negatif')"
        beklenen = "if x > 0:\n    yaz('pozitif')\nelse:\n    yaz('negatif')"
        assert cevir(kod) == beklenen

    def test_satir_numaralari_korunur(self):
        kod = "x = 1\neğer x:\n    yaz(x)"
        python = cevir(kod)
        assert python.count('\n') == kod.count('\n')

    def test_fonksiyon_tanimi(self):
        kod = "fonksiyon topla(a, b):\n    döndür a + b"
        beklenen = "def topla(a, b):\n    return a + b"
        assert cevir(kod) == beklenen

    def test_sinif_tanimi(self):
        kod = "sınıf Araba:\n    fonksiyon __init__(öz):\n        öz.renk = 'kırmızı'"
        beklenen = "class Araba:\n    def __init__(öz):\n        öz.renk = 'kırmızı'"
        assert cevir(kod) == beklenen


class TestIstisnaCeviri:

    def test_hata_sinifi(self):
        assert cevir("hariç Hata:") == "except Exception:"

    def test_sozdizimi_hatasi(self):
        assert cevir("hariç SözDizimiHatası:") == "except SyntaxError:"

    def test_ad_hatasi(self):
        assert cevir("hariç AdHatası:") == "except NameError:"

    def test_tur_hatasi(self):
        assert cevir("hariç TürHatası:") == "except TypeError:"

    def test_deger_hatasi(self):
        assert cevir("hariç DeğerHatası:") == "except ValueError:"

    def test_indeks_hatasi(self):
        assert cevir("hariç İndeksHatası:") == "except IndexError:"

    def test_anahtar_hatasi(self):
        assert cevir("hariç AnahtarHatası:") == "except KeyError:"

    def test_nitelik_hatasi(self):
        assert cevir("hariç NitelikHatası:") == "except AttributeError:"

    def test_iceaktarma_hatasi(self):
        assert cevir("hariç İçeAktarmaHatası:") == "except ImportError:"


class TestSyntaxKontrol:

    def test_gecerli_kod(self):
        gecerli, _ = syntax_kontrol("yaz('merhaba')")
        assert gecerli is True

    def test_gecersiz_kod(self):
        gecerli, hata = syntax_kontrol("eğer:")
        assert gecerli is False
        assert hata != ''

    def test_gecerli_fonksiyon(self):
        kod = "fonksiyon topla(a, b):\n    döndür a + b"
        gecerli, _ = syntax_kontrol(kod)
        assert gecerli is True

    def test_gecerli_sinif(self):
        kod = "sınıf Araba:\n    fonksiyon __init__(öz):\n        öz.renk = 'kırmızı'"
        gecerli, _ = syntax_kontrol(kod)
        assert gecerli is True
