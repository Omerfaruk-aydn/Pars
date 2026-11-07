"""
v1.0.1 genişletilmiş standart kütüphane testleri.
"""

import os
import tempfile

import pytest


def test_istatistik():
    from pars.standart import istatistik as m
    assert m.ortalama([1, 2, 3, 4]) == 2.5
    assert m.medyan([3, 1, 2]) == 2
    assert m.mod([1, 2, 2, 3]) == 2
    assert m.buyuk([1, 9, 3]) == 9
    assert m.aralik([1, 9, 3]) == 8
    assert m.korelasyon([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)


def test_koleksiyonlar():
    from pars.standart import koleksiyonlar as m
    assert m.say(['a', 'a', 'b']) == {'a': 2, 'b': 1}
    assert m.en_sik(['a', 'a', 'b']) == 'a'
    Nokta = m.AdliDemet('Nokta', ['x', 'y'])
    assert Nokta(1, 2).x == 1
    q = m.CiftUclu([1, 2, 3])
    q.appendleft(0)
    assert list(q) == [0, 1, 2, 3]


def test_yinelenebilirler():
    from pars.standart import yinelenebilirler as m
    assert list(m.kombinasyonlar([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]
    assert m.birikimli([1, 2, 3]) == [1, 3, 6]
    assert m.ilk_n(m.say(5), 3) == [5, 6, 7]
    assert m.sikistir_uzun([1, 2], ['a'], dolgu='-') == [(1, 'a'), (2, '-')]


def test_fonksiyonel():
    from pars.standart import fonksiyonel as m
    kare = m.kismi(lambda a, b: a ** b, b=2)
    assert kare(5) == 25
    assert m.azalt(lambda a, b: a + b, [1, 2, 3]) == 6
    assert m.boru(lambda x: x + 1, lambda x: x * 2)(3) == 8


def test_yol_ve_isletim():
    from pars.standart import yol, isletim
    gecici = isletim.gecici_dosya(onek='pars_test_', sonek='.txt')
    try:
        yol.yaz(gecici, 'merhaba')
        assert yol.oku(gecici) == 'merhaba'
        assert yol.boyut(gecici) == 7
        assert yol.var_mi(gecici)
    finally:
        if os.path.exists(gecici):
            os.remove(gecici)


def test_surec():
    from pars.standart import surec
    sonuc = surec.python_calistir("print('PARS')")
    assert sonuc['kod'] == 0
    assert 'PARS' in sonuc['cikti']


def test_iplik():
    from pars.standart import iplik
    sonuc = iplik.paralel_calistir(lambda x: x * x, range(5))
    assert sonuc == [0, 1, 4, 9, 16]
    olay = iplik.Olay()
    olay.set()
    assert olay.is_set()


def test_gunluk():
    from pars.standart import gunluk
    gunluk.temel_yapilandir(seviye='kritik')
    lg = gunluk.gunlukcu_al('pars_test')
    gunluk.seviye_ata('hata_ayikla', 'pars_test')
    assert lg.level is not None


def test_sifreleme():
    from pars.standart import sifreleme as m
    assert m.sha256('abc') == (
        'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
    assert m.base64_coz(m.base64_kodla('PARS')) == b'PARS'
    assert m.sabit_karsilastir('a', 'a') is True
    assert m.sabit_karsilastir('a', 'b') is False
    assert len(m.rastgele_metin(10)) == 10


def test_sikistirma():
    from pars.standart import sikistirma as m
    veri = b'PARS ' * 100
    assert m.gzip_ac(m.gzip_sikistir(veri)) == veri
    assert m.zlib_ac(m.zlib_sikistir(veri)) == veri


def test_takvim():
    from pars.standart import takvim as m
    assert m.artik_yil(2024) is True
    assert m.artik_yil(2023) is False
    assert m.ay_gun_sayisi(2024, 2) == 29
    assert m.gun_adi('2026-11-06') == 'Cuma'


def test_sayi():
    from pars.standart import sayi as m
    assert m.kesin_topla('0.1', '0.2') == m.ondalik('0.3')
    assert m.kesir(1, 2) + m.kesir(1, 2) == 1
    assert str(m.ondalik_yuvarla('3.14159', 2)) == '3.14'


def test_kopya():
    from pars.standart import kopya as m
    a = {'x': [1, 2]}
    b = m.derin_kopyala(a)
    b['x'].append(3)
    assert a['x'] == [1, 2]


def test_veri_siniflari():
    from pars.standart import veri_siniflari as m

    @m.veri_sinifi
    class Kisi:
        ad: str
        yas: int = 0

    k = Kisi('Ayşe', 30)
    assert m.sozluge_cevir(k) == {'ad': 'Ayşe', 'yas': 30}
    assert m.degistir(k, yas=31).yas == 31


def test_arguman():
    from pars.standart import arguman as m
    ay = m.ArgumanAyristirici('test')
    ay.konumlu('dosya', yardim='Dosya')
    ay.secenek('--mod', varsayilan='hizli')
    ay.bayrak('--ayrintili')
    s = ay.ayristir(['a.pars', '--mod', 'tam', '--ayrintili'])
    assert s.dosya == 'a.pars'
    assert s.mod == 'tam'
    assert s.ayrintili is True


def test_deneme():
    from pars.standart import deneme as m
    m.iddia_esit(1, 1)
    m.iddia_dogru(True)
    with pytest.raises(AssertionError):
        m.iddia_esit(1, 2)


def test_standart_moduller_kayitli():
    """içe_aktar matematik gibi ifadeler sys.modules üzerinden çalışmalı."""
    import pars.standart  # noqa: F401
    from pars.cekirdek.yurutucu import ad_alani_olustur
    alan = ad_alani_olustur()
    for ad in ('matematik', 'metin', 'koleksiyonlar', 'yinelenebilirler',
               'fonksiyonel', 'isletim', 'surec', 'iplik', 'gunluk',
               'sifreleme', 'sikistirma', 'takvim', 'sayi', 'kopya',
               'veri_siniflari', 'arguman', 'deneme'):
        assert ad in alan, f'{ad} ad alanında yok'


def test_liste_hem_fonksiyon_hem_modul():
    from pars.cekirdek.yurutucu import ad_alani_olustur
    a = ad_alani_olustur()
    assert a['liste']([1, 2]) == [1, 2]
    assert a['liste'].tekil([1, 1, 2]) == [1, 2]
