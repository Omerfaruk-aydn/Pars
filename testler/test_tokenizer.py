"""
Tokenizer birim testleri
"""

import pytest
from pars.cekirdek.tokenizer import tokenize


class TestTokenizer:

    def test_basit_metin(self):
        tokenlar = tokenize("merhaba")
        assert len(tokenlar) == 1
        assert tokenlar[0] == ('ISIM', 'merhaba')

    def test_string_cift_tirnak(self):
        tokenlar = tokenize('"merhaba dünya"')
        assert len(tokenlar) == 1
        assert tokenlar[0] == ('STR', '"merhaba dünya"')

    def test_string_tek_tirnak(self):
        tokenlar = tokenize("'test'")
        assert len(tokenlar) == 1
        assert tokenlar[0] == ('STR', "'test'")

    def test_uclu_string(self):
        kod = '"""üçlü string"""'
        tokenlar = tokenize(kod)
        assert len(tokenlar) == 1
        assert tokenlar[0] == ('STR', kod)

    def test_yorum(self):
        tokenlar = tokenize("# bu bir yorum")
        assert len(tokenlar) == 1
        assert tokenlar[0] == ('YORUM', '# bu bir yorum')

    def test_karma_kod(self):
        kod = 'yaz("merhaba")'
        tokenlar = tokenize(kod)
        turler = [t[0] for t in tokenlar]
        assert 'ISIM' in turler
        assert 'STR' in turler
        assert 'DIGER' in turler

    def test_turkce_karakterler(self):
        tokenlar = tokenize("yaş = 25")
        isimler = [t[1] for t in tokenlar if t[0] == 'ISIM']
        assert 'yaş' in isimler

    def test_turkce_buyuk_harf(self):
        tokenlar = tokenize("Şehir = 'İstanbul'")
        isimler = [t[1] for t in tokenlar if t[0] == 'ISIM']
        assert 'Şehir' in isimler

    def test_bos_kod(self):
        tokenlar = tokenize("")
        assert tokenlar == []

    def test_sadece_bosluk(self):
        tokenlar = tokenize("   ")
        assert len(tokenlar) == 3  # 3 boşluk karakteri

    def test_satir_atla(self):
        tokenlar = tokenize("x = 1\ny = 2")
        isimler = [t[1] for t in tokenlar if t[0] == 'ISIM']
        assert 'x' in isimler
        assert 'y' in isimler

    def test_fstring(self):
        kod = 'f"Merhaba {isim}"'
        tokenlar = tokenize(kod)
        assert tokenlar[0] == ('STR', 'f"Merhaba {isim}"')

    def test_sayilar(self):
        tokenlar = tokenize("42 3.14")
        sayilar = [t[1] for t in tokenlar if t[0] == 'DIGER']
        assert '42' in sayilar
        assert '3.14' in sayilar

    def test_operatorler(self):
        tokenlar = tokenize("x + y * 2")
        digerler = [t[1] for t in tokenlar if t[0] == 'DIGER']
        assert '+' in digerler
        assert '*' in digerler

    def test_string_icinde_yorum(self):
        kod = '"# bu yorum değil"'
        tokenlar = tokenize(kod)
        assert tokenlar[0] == ('STR', kod)
        # Yorum olarak algılanmamalı

    def test_string_icinde_anahtar_kelime(self):
        kod = '"eğer için sınıf"'
        tokenlar = tokenize(kod)
        assert tokenlar[0] == ('STR', kod)
        # Anahtar kelime olarak algılanmamalı

    def test_kacisli_string(self):
        kod = '"merhaba\\"dünya"'
        tokenlar = tokenize(kod)
        assert tokenlar[0] == ('STR', kod)

    def test_coklu_satir_string(self):
        kod = '''"""satır1
satır2
satır3"""'''
        tokenlar = tokenize(kod)
        assert len(tokenlar) == 1
        assert tokenlar[0][0] == 'STR'

    def test_pars_anahtar_kelimeler(self):
        kod = "eğer iken için sınıf fonksiyon"
        tokenlar = tokenize(kod)
        isimler = [t[1] for t in tokenlar if t[0] == 'ISIM']
        assert 'eğer' in isimler
        assert 'iken' in isimler
        assert 'için' in isimler
        assert 'sınıf' in isimler
        assert 'fonksiyon' in isimler

    def test_dogru_yanlis_yok(self):
        kod = "doğru yanlış yok"
        tokenlar = tokenize(kod)
        isimler = [t[1] for t in tokenlar if t[0] == 'ISIM']
        assert 'doğru' in isimler
        assert 'yanlış' in isimler
        assert 'yok' in isimler
