"""
CLI ve yeni komutlar (parskur / parspy) testleri.
"""

import sys

import pytest

from pars.cli import komutlar, python_modu


def test_surum(capsys):
    komutlar.main(['--surum'])
    assert 'PARS v1.0.1' in capsys.readouterr().out


def test_yardim(capsys):
    komutlar.main(['--yardim'])
    cikti = capsys.readouterr().out
    assert 'parskur' in cikti
    assert 'parspip' in cikti
    assert 'parspy' in cikti
    assert 'köprü' in cikti


def test_cevir_komutu(tmp_path, capsys):
    dosya = tmp_path / 'a.pars'
    dosya.write_text('eğer x > 0:\n    yaz("pozitif")\n', encoding='utf-8')
    komutlar.main(['-cevir', str(dosya)])
    cikti = capsys.readouterr().out
    assert 'if x > 0:' in cikti


def test_kontrol_basarili(tmp_path, capsys):
    dosya = tmp_path / 'a.pars'
    dosya.write_text('yaz("merhaba")\n', encoding='utf-8')
    komutlar.main(['-kontrol', str(dosya)])
    assert 'Sözdizimi doğru.' in capsys.readouterr().out


def test_kontrol_hatali(tmp_path, capsys):
    dosya = tmp_path / 'a.pars'
    dosya.write_text('eğer:\n', encoding='utf-8')
    with pytest.raises(SystemExit) as hata:
        komutlar.main(['-kontrol', str(dosya)])
    assert hata.value.code == 1


def test_derle(tmp_path, capsys):
    dosya = tmp_path / 'a.pars'
    dosya.write_text('yaz("merhaba")\n', encoding='utf-8')
    hedef = tmp_path / 'a.py'
    komutlar.main(['derle', str(dosya), '-o', str(hedef)])
    assert hedef.exists()
    assert 'yaz("merhaba")' in hedef.read_text(encoding='utf-8')


def test_python_modu_kod(capsys):
    assert python_modu.kod_calistir("print('PARS')") == 0
    assert 'PARS' in capsys.readouterr().out


def test_python_modu_dosya(tmp_path):
    dosya = tmp_path / 'a.py'
    dosya.write_text("print('merhaba')\n", encoding='utf-8')
    assert python_modu.dosya_calistir(str(dosya)) == 0


def test_paket_argumanlari():
    from pars.cli import paket
    ay = paket._arguman_ayristirici()
    s = ay.parse_args(['listele', '--eski'])
    assert s.komut == 'listele'
    assert s.eski is True
    s = ay.parse_args(['yükle', 'requests', '--sessiz'])
    assert s.paketler == ['requests']
    assert s.sessiz is True
    # Eski/ASCII takma adlar
    s = ay.parse_args(['yukle', 'numpy'])
    assert s.paketler == ['numpy']


def test_pars_uzantisi_calistir(tmp_path, capsys):
    dosya = tmp_path / 'program.pars'
    dosya.write_text('yaz("pars uzantisi")\n', encoding='utf-8')
    komutlar.main([str(dosya)])
    assert 'pars uzantisi' in capsys.readouterr().out


def test_utf8_bom_kaynak(tmp_path, capsys):
    dosya = tmp_path / 'bom.pars'
    dosya.write_bytes('\ufeffyaz("bom ok")\n'.encode('utf-8'))
    komutlar.main([str(dosya)])
    assert 'bom ok' in capsys.readouterr().out


def test_eski_prs_uzantisi_uyumlu(tmp_path, capsys):
    dosya = tmp_path / 'program.prs'
    dosya.write_text('yaz("eski uzanti")\n', encoding='utf-8')
    komutlar.main([str(dosya)])
    assert 'eski uzanti' in capsys.readouterr().out


def test_kopru_cevirileri():
    from pars.cekirdek import kopru
    assert kopru.turkce_ad('status_code') == 'durum_kodu'
    assert kopru.ingilizce_ad('durum_kodu') == 'status_code'
    assert kopru.turkce_ad('get_user_name') == 'al_kullanici_ad'
    # Türkçe karakter normalizasyonu
    assert kopru.ingilizce_ad('kullanıcı_adı') == 'username'
    assert kopru.ingilizce_ad('şifre') == 'password'


def test_kopru_bagla_standart_modul():
    from pars.cekirdek import kopru
    j = kopru.bagla('json')
    assert j.dok_metin({'a': 1}) == '{"a": 1}'
    assert j.yukle_metin('{"a": 1}') == {'a': 1}
    # Özgün adlar korunur
    assert j.dumps([1]) == '[1]'


def test_kopru_ozel_nesne():
    from pars.cekirdek import kopru

    class Yanit:
        def __init__(self):
            self.status_code = 200
            self.content = b'ok'

        def get_json(self):
            return {'ok': True}

    k = kopru.bagla(Yanit())
    assert k.durum_kodu == 200
    assert k.icerik == b'ok'
    assert k.al_json() == {'ok': True}
    assert isinstance(k, Yanit)


def test_kopru_disa_aktar(tmp_path):
    from pars.cekirdek import kopru
    hedef = tmp_path / 'istek_kopru.pars'
    yol = kopru.disa_aktar('json', str(hedef), 'json_k')
    assert hedef.read_text(encoding='utf-8')
    assert 'kopru.bagla("json")' in hedef.read_text(encoding='utf-8')
    assert yol == str(hedef)


def test_kopru_cli_ozellikler(capsys):
    from pars.cli import kopru as kopru_cli
    assert kopru_cli.main(['json']) == 0
    cikti = capsys.readouterr().out
    assert 'dumps' in cikti
    assert 'dok_metin' in cikti


def test_kopru_cli_dogrula(capsys):
    from pars.cli import kopru as kopru_cli
    assert kopru_cli.main(['doğrula', 'json']) == 0
    assert 'json' in capsys.readouterr().out


def test_standart_kopru_modulu():
    from pars.standart import kopru as std_kopru
    assert hasattr(std_kopru, 'bagla')
    assert hasattr(std_kopru, 'turkce_ad')


def test_yerel_pars_modulu_ice_aktar(tmp_path, capsys):
    sys.modules.pop('yardimci', None)
    (tmp_path / 'yardimci.pars').write_text(
        'fonksiyon iki_kat(x):\n    döndür x * 2\n', encoding='utf-8')
    ana = tmp_path / 'ana.pars'
    ana.write_text(
        'den_aktar yardimci içe_aktar iki_kat\n'
        'yaz(iki_kat(21))\n', encoding='utf-8')

    komutlar.main([str(ana)])
    assert '42' in capsys.readouterr().out


def test_yerel_pars_paketi_ice_aktar(tmp_path, capsys):
    sys.modules.pop('aritmetik', None)
    paket = tmp_path / 'aritmetik'
    paket.mkdir()
    (paket / '__init__.pars').write_text(
        'fonksiyon topla(a, b):\n    döndür a + b\n', encoding='utf-8')
    ana = tmp_path / 'ana2.pars'
    ana.write_text(
        'içe_aktar aritmetik\n'
        'yaz(aritmetik.topla(2, 3))\n', encoding='utf-8')

    komutlar.main([str(ana)])
    assert '5' in capsys.readouterr().out
