"""
v1.0.1 çekirdek regresyon testleri.

Kapsanan hatalar:
  - Noktadan sonraki niteliklerin yanlış çevrilmesi (dosya.sil)
  - dir() yerleşik fonksiyonunun 'is' anahtar kelimesine dönüşmesi
  - süper() / sıfır argümanlı super() hatası
  - f-string içindeki Türkçe ifadelerin çevrilmemesi
  - '...' sonrası anahtar kelimenin nitelik sanılması
"""

import pytest

from pars.cekirdek.ceviri import cevir, syntax_kontrol
from pars.cekirdek.tokenizer import tokenize
from pars.cekirdek.yurutucu import calistir


class TestNitelikKoruma:

    def test_dosya_sil_cevrilmez(self):
        assert cevir("dosya.sil('x')") == "dosya.sil('x')"

    def test_nesne_metodu_cevrilmez(self):
        assert cevir("vt.sil('tablo', 'id=1')") == "vt.sil('tablo', 'id=1')"

    def test_gercek_anahtar_kelime_cevrilir(self):
        assert cevir("sil x") == "del x"

    def test_ellipsis_sonrasi_fonksiyon(self):
        kod = "fonksiyon a(öz) -> int: ...\nfonksiyon b(öz) -> int:\n    döndür 1"
        py = cevir(kod)
        assert 'def b(' in py
        assert 'fonksiyon' not in py


class TestDirFonksiyonu:

    def test_dir_cevrilmez(self):
        assert cevir("dir(x)") == "dir(x)"

    def test_dir_calistirilabilir(self, capsys):
        assert calistir("yaz(dir([]))") is True

    def test_dır_operatoru(self):
        assert cevir("x dır yok") == "x is None"


class TestSuper:

    def test_super_cevrilir(self):
        assert cevir("süper().__init__()") == "super().__init__()"

    def test_kalitim_calisir(self):
        kod = (
            "sınıf Ana:\n"
            "    fonksiyon __init__(öz, ad):\n"
            "        öz.ad = ad\n"
            "sınıf Alt(Ana):\n"
            "    fonksiyon __init__(öz, ad, yas):\n"
            "        süper().__init__(ad)\n"
            "        öz.yas = yas\n"
            "a = Alt('PARS', 5)\n"
            "iddia a.ad == 'PARS' ve a.yas == 5"
        )
        assert calistir(kod) is True


class TestFString:

    def test_fstring_anahtar_kelime(self):
        assert cevir("f'{doğru} {yanlış} {yok}'") == \
            "f'{True} {False} {None}'"

    def test_fstring_kosullu_ifade(self):
        py = cevir("f'{x eğer x > 0 değilse 0}'")
        assert py == "f'{x if x > 0 else 0}'"

    def test_fstring_bicim_belirteci_korunur(self):
        assert cevir("f'{değer:.2f}'") == "f'{değer:.2f}'"

    def test_fstring_calistirilir(self, capsys):
        assert calistir("x = 5\nyaz(f'{doğru} ve {x}')") is True
        # f-string Python semantiğiyle True üretir; yaz(doğru) Türkçe gösterir.
        assert 'True ve 5' in capsys.readouterr().out


class TestCokluIfade:

    def test_turkce_ternary(self):
        assert cevir("y = 1 eğer x değilse 0") == "y = 1 if x else 0"

    def test_turkce_ternary_calistir(self):
        kod = "x = 0\ny = 'e' eğer x == 0 değilse 'h'\niddia y == 'e'"
        assert calistir(kod) is True


class TestSayiVeStringTokenlari:

    @pytest.mark.parametrize('kod', [
        "0x1F + 0b1010 + 0o17",
        "1_000_000 + 3.14e-2 + .5 + 2j",
        "rb'abc' + br'def' + r'x' + b'y'",
        "f'{x}' + fr'{y}'",
        "'''çok\nsatır'''",
    ])
    def test_kayipsiz(self, kod):
        assert ''.join(m for _, m in tokenize(kod)) == kod

    def test_sayi_tek_token(self):
        assert ('DIGER', '0x1F') in tokenize('0x1F')


class TestOrnekProgram:

    def test_ornek_kalitim(self):
        kod = (
            "sınıf Hayvan:\n"
            "    fonksiyon ses(öz):\n"
            "        döndür '...'\n"
            "sınıf Kedi(Hayvan):\n"
            "    fonksiyon ses(öz):\n"
            "        döndür 'miyav'\n"
            "iddia Kedi().ses() == 'miyav'"
        )
        assert calistir(kod) is True
