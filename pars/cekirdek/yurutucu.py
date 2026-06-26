"""
PARS Yürütücü
-------------
PARS kodunu çevirir, derler ve Python runtime ile çalıştırır.
Türkçe built-in'ler + standart kütüphane ad alanına eklenir.
"""

import sys
import importlib
from typing import Optional
from .esleme import PARS_BUILTINS, PARS_ISTISNALAR
from .ceviri import cevir, cevir_ve_goster
from .hatalar import hata_goster


def ad_alani_olustur(dosya_adi: str = '<pars>') -> dict:
    """
    PARS programının çalışacağı Python ad alanını oluşturur.

    İçerir:
      - Tüm PARS built-in fonksiyonları
      - Türkçe istisna sınıfları
      - PARS standart kütüphane modülleri
      - Python __builtins__
    """
    alan = {
        '__name__':     '__main__',
        '__file__':     dosya_adi,
        '__builtins__': __builtins__,
        '__doc__':      None,
        'PARS_SURUM':   '1.0.0',
    }
    _standart_yukle(alan)
    alan.update(PARS_BUILTINS)
    alan.update(PARS_ISTISNALAR)
    return alan


def _standart_yukle(alan: dict) -> None:
    """PARS standart kütüphane modüllerini ad alanına ekler."""
    moduller = [
        ('matematik', 'pars.standart.matematik'),
        ('metin',     'pars.standart.metin'),
        ('liste',     'pars.standart.liste'),
        ('dosya',     'pars.standart.dosya'),
        ('zaman',     'pars.standart.zaman'),
        ('sistem',    'pars.standart.sistem'),
        ('rastgele',  'pars.standart.rastgele'),
        ('veri',      'pars.standart.veri'),
    ]
    for isim, yol in moduller:
        try:
            modul = importlib.import_module(yol)
            # Modül adını built-in ile çakışmaması için ekle
            alan[isim] = modul
        except ImportError:
            pass


def calistir(pars_kodu: str,
             dosya_adi: str = '<pars>',
             python_goster: bool = False) -> bool:
    """
    PARS kodunu çalıştırır.

    Args:
        pars_kodu:    Kaynak kod metni
        dosya_adi:    Hata mesajlarında görünecek dosya adı
        python_goster: True ise üretilen Python kodunu da gösterir

    Returns:
        bool: True = başarılı, False = hata oluştu
    """
    try:
        python_kodu = cevir(pars_kodu)
    except Exception as e:
        print(f'Çevirme hatası: {e}', file=sys.stderr)
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
            '\nProgram kullanicininca durduruldu.',
            file=sys.stderr
        )
        return False

    except Exception as exc:
        hata_goster(exc, pars_kodu, dosya_adi)
        return False


__all__ = ['calistir', 'ad_alani_olustur']
