"""
PARS Yürütücü
-------------
PARS kodunu çevirir, derler ve Python runtime ile çalıştırır.
Türkçe built-in'ler + standart kütüphane ad alanına eklenir.
"""

import os
import sys
import importlib
from typing import Tuple
from .esleme import PARS_BUILTINS, PARS_ISTISNALAR
from .ceviri import cevir
from .hatalar import hata_goster
from . import ice_aktarma

from pars import __version__ as PARS_SURUM

#: PARS standart kütüphane modülleri.
#: (Türkçe ad, ASCII takma ad, modül yolu)
STANDART_MODULLER: Tuple[Tuple[str, str, str], ...] = (
    ('matematik',       'matematik',       'pars.standart.matematik'),
    ('istatistik',      'istatistik',      'pars.standart.istatistik'),
    ('metin',           'metin',           'pars.standart.metin'),
    ('liste',           'liste',           'pars.standart.liste'),
    ('koleksiyonlar',   'koleksiyonlar',   'pars.standart.koleksiyonlar'),
    ('yinelenebilirler', 'yinelenebilirler', 'pars.standart.yinelenebilirler'),
    ('fonksiyonel',     'fonksiyonel',     'pars.standart.fonksiyonel'),
    ('dosya',           'dosya',           'pars.standart.dosya'),
    ('yol',             'yol',             'pars.standart.yol'),
    ('zaman',           'zaman',           'pars.standart.zaman'),
    ('takvim',          'takvim',          'pars.standart.takvim'),
    ('sistem',          'sistem',          'pars.standart.sistem'),
    ('isletim',         'işletim',         'pars.standart.isletim'),
    ('surec',           'süreç',           'pars.standart.surec'),
    ('iplik',           'iplik',           'pars.standart.iplik'),
    ('gunluk',          'günlük',          'pars.standart.gunluk'),
    ('rastgele',        'rastgele',        'pars.standart.rastgele'),
    ('sifreleme',       'şifreleme',       'pars.standart.sifreleme'),
    ('sikistirma',      'sıkıştırma',      'pars.standart.sikistirma'),
    ('sayi',            'sayı',            'pars.standart.sayi'),
    ('kopya',           'kopya',           'pars.standart.kopya'),
    ('veri',            'veri',            'pars.standart.veri'),
    ('veri_siniflari',  'veri_sınıfları',  'pars.standart.veri_siniflari'),
    ('ag',              'ağ',              'pars.standart.ag'),
    ('veritabani',      'veritabanı',      'pars.standart.veritabani'),
    ('arguman',         'argüman',         'pars.standart.arguman'),
    ('deneme',          'deneme',          'pars.standart.deneme'),
    ('kopru',           'köprü',           'pars.standart.kopru'),
)


class _CagrilabilirModul:
    """Hem fonksiyon gibi ?a?r?labilen hem mod?l gibi davranan sarmalay?c?.

    `liste(...)` built-in liste d?n???m?n?, `liste.tekil(...)` ise
    standart k?t?phane fonksiyonunu destekler.
    """

    def __init__(self, modul, cagri):
        self._modul = modul
        self._cagri = cagri

    def __call__(self, *args, **kwargs):
        return self._cagri(*args, **kwargs)

    def __getattr__(self, ad):
        return getattr(self._modul, ad)

    def __repr__(self):
        return repr(self._modul)


def ad_alani_olustur(dosya_adi: str = '<pars>') -> dict:
    """
    PARS programının çalışacağı Python ad alanını oluşturur.

    İçerir:
      - Tüm PARS built-in fonksiyonları
      - Türkçe istisna sınıfları
      - PARS standart kütüphane modülleri
      - Python __builtins__
    """
    # Yerel `.pars` modüllerinin içe aktarılabilmesi için kanca.
    ice_aktarma.kur()
    if dosya_adi and not dosya_adi.startswith('<'):
        ice_aktarma.yol_ekle(os.path.dirname(os.path.abspath(dosya_adi)))

    alan = {
        '__name__':     '__main__',
        '__file__':     dosya_adi,
        '__builtins__': __builtins__,
        '__doc__':      None,
        'PARS_SURUM':   PARS_SURUM,
    }
    _standart_yukle(alan)
    liste_modulu = alan.get('liste')
    alan.update(PARS_BUILTINS)
    alan.update(PARS_ISTISNALAR)

    # 'liste' hem built-in d?n??t?r?c? hem standart k?t?phane mod?l?d?r.
    if liste_modulu is not None:
        alan['liste'] = _CagrilabilirModul(liste_modulu, list)

    return alan


def _standart_yukle(alan: dict) -> None:
    """
    PARS standart kütüphane modüllerini ad alanına ekler ve
    `içe_aktar matematik` gibi ifadelerin çalışması için
    sys.modules'a Türkçe/ASCII takma adları kaydeder.
    """
    for tr_ad, ascii_ad, yol in STANDART_MODULLER:
        try:
            modul = importlib.import_module(yol)
        except ImportError:
            continue

        # Doğrudan kullanım: matematik.PI
        alan[tr_ad] = modul
        if ascii_ad != tr_ad:
            alan[ascii_ad] = modul

        # `içe_aktar matematik` / `import matematik` desteği
        sys.modules.setdefault(tr_ad, modul)
        sys.modules.setdefault(ascii_ad, modul)


def modul_yukle(ad: str):
    """Herhangi bir Python modülünü yükler (Türkçe takma adlar dahil)."""
    return importlib.import_module(ad)


def calistir(pars_kodu: str,
             dosya_adi: str = '<pars>',
             python_goster: bool = False,
             hatayi_yukselt: bool = False) -> bool:
    """
    PARS kodunu çalıştırır.

    Args:
        pars_kodu:     Kaynak kod metni
        dosya_adi:     Hata mesajlarında görünecek dosya adı
        python_goster: True ise üretilen Python kodunu da gösterir
        hatayi_yukselt: True ise hatayı Türkçe gösterip yeniden fırlatır

    Returns:
        bool: True = başarılı, False = hata oluştu
    """
    try:
        python_kodu = cevir(pars_kodu)
    except Exception as e:
        print(f'Çevirme hatası: {e}', file=sys.stderr)
        if hatayi_yukselt:
            raise
        return False

    if python_goster:
        print('\n-- Uretilen Python Kodu ' + '-' * 36)
        for i, satir in enumerate(python_kodu.splitlines(), 1):
            print(f'{i:4} | {satir}')
        print('-' * 60 + '\n')

    alan = ad_alani_olustur(dosya_adi)

    try:
        derlenmis = compile(python_kodu, dosya_adi, 'exec')
        exec(derlenmis, alan)
        return True

    except SystemExit:
        return True

    except KeyboardInterrupt:
        print(
            '\nProgram kullanıcı tarafından durduruldu.',
            file=sys.stderr
        )
        return False

    except Exception as exc:
        hata_goster(exc, pars_kodu, dosya_adi)
        if hatayi_yukselt:
            raise
        return False


__all__ = [
    'calistir',
    '_CagrilabilirModul',
    'ad_alani_olustur',
    'modul_yukle',
    'STANDART_MODULLER',
    'PARS_SURUM',
]
