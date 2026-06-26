"""
PARS Çevirici (Transpiler)
--------------------------
Türkçe PARS kodunu Python koduna çevirir.

Kurallar:
  - Satır numaraları korunur (hata mesajları için kritik)
  - String ve yorum içleri asla değiştirilmez
  - f-string'lerin {} bölümleri korunur
  - Türkçe değişken isimleri korunur (Python 3 Unicode desteği)
  - Hem Türkçe karakterli hem ASCII versiyonlar desteklenir
"""

from typing import Tuple
from .esleme import KELIME_ESLEME, PARS_ISTISNALAR
from .tokenizer import tokenize


def cevir(pars_kodu: str) -> str:
    """
    PARS kodunu Python koduna çevirir.

    Args:
        pars_kodu: Kaynak PARS kodu

    Returns:
        str: Python kodu (satır numaraları korunmuş)
    """
    tum_esleme = {
        **KELIME_ESLEME,
        **{k: v.__name__ for k, v in PARS_ISTISNALAR.items()},
    }
    tokenlar = tokenize(pars_kodu)

    parcalar = []
    for tur, metin in tokenlar:
        if tur in ('STR', 'YORUM'):
            parcalar.append(metin)
        elif tur == 'ISIM':
            parcalar.append(tum_esleme.get(metin, metin))
        else:
            parcalar.append(metin)

    return ''.join(parcalar)


def cevir_ve_goster(pars_kodu: str) -> str:
    """
    Türkçe ve Python karşılıklarını yan yana gösterir.
    CLI'nin -cevir komutu için kullanılır.
    """
    python_kodu = cevir(pars_kodu)
    tr_satirlar = pars_kodu.splitlines()
    py_satirlar = python_kodu.splitlines()

    en_uzun = max((len(s) for s in tr_satirlar), default=0)
    satirlar = []
    for i, (tr, py) in enumerate(zip(tr_satirlar, py_satirlar), 1):
        if tr.strip() != py.strip():
            satirlar.append(f'{i:4} │ {tr:<{en_uzun}}  →  {py}')
        else:
            satirlar.append(f'{i:4} │ {tr}')

    return '\n'.join(satirlar)


def syntax_kontrol(pars_kodu: str,
                   dosya_adi: str = '<pars>') -> Tuple[bool, str]:
    """
    Kodu çevir ve Python sözdizimi kontrolü yap.

    Returns:
        Tuple[bool, str]: (geçerli_mi, hata_mesajı)
    """
    try:
        python_kodu = cevir(pars_kodu)
        compile(python_kodu, dosya_adi, 'exec')
        return True, ''
    except SyntaxError as e:
        return False, f'Satır {e.lineno}: {e.msg}'


__all__ = ['cevir', 'cevir_ve_goster', 'syntax_kontrol']
