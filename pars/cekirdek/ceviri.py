"""
PARS Çevirici (Transpiler)
--------------------------
Türkçe PARS kodunu Python koduna çevirir.

Kurallar:
  - Satır numaraları korunur (hata mesajları için kritik)
  - String ve yorum içleri asla değiştirilmez
  - f-string'lerin {} bölümleri de Türkçe anahtar kelimelerden çevrilir
  - Türkçe değişken isimleri korunur (Python 3 Unicode desteği)
  - Noktadan sonra gelen nitelik/metot adları çevrilmez
    (dosya.sil → dosya.del DEĞİL, dosya.sil olarak kalır)
  - Hem Türkçe karakterli hem ASCII versiyonlar desteklenir
"""

import re
from typing import Tuple
from .esleme import KELIME_ESLEME, PARS_ISTISNALAR
from .tokenizer import tokenize

_ONEK_RE = re.compile(r'^([rRbBuUfF]{0,2})(.*)$', re.DOTALL)


def cevir(pars_kodu: str) -> str:
    """
    PARS kodunu Python koduna çevirir.

    Args:
        pars_kodu: Kaynak PARS kodu

    Returns:
        str: Python kodu (satır numaraları korunmuş)
    """
    # Windows editörlerinin eklediği UTF-8 BOM'u yok say.
    if pars_kodu.startswith('\ufeff'):
        pars_kodu = pars_kodu[1:]

    tum_esleme = {
        **KELIME_ESLEME,
        **{k: v.__name__ for k, v in PARS_ISTISNALAR.items()},
    }
    tokenlar = tokenize(pars_kodu)

    parcalar = []

    for i, (tur, metin) in enumerate(tokenlar):
        if tur == 'STR':
            parcalar.append(_string_cevir(metin))
        elif tur == 'YORUM':
            parcalar.append(metin)
        elif tur == 'ISIM':
            # Noktadan sonra gelen isim bir nitelik/metottur; çevrilmez.
            # Örn: dosya.sil, vt.sil, kayit.geç
            # NOT: '...' (ellipsis) bir nitelik noktası değildir.
            if _nitelik_mi(tokenlar, i):
                parcalar.append(metin)
            else:
                parcalar.append(tum_esleme.get(metin, metin))
        else:
            parcalar.append(metin)

    return ''.join(parcalar)


def _nitelik_mi(tokenlar, indeks: int) -> bool:
    """Bu ISIM token'ı bir nokta niteliği mi (a.b)?"""
    j = indeks - 1
    while j >= 0 and tokenlar[j][1].isspace():
        j -= 1
    if j < 0 or tokenlar[j][1] != '.':
        return False
    # '...' veya '..' gibi ardışık noktalar nitelik değildir
    k = j - 1
    while k >= 0 and tokenlar[k][1].isspace():
        k -= 1
    if k >= 0 and tokenlar[k][1] == '.':
        return False
    return True


# ── f-string çevirisi ────────────────────────────────────────────────────

def _string_cevir(tok: str) -> str:
    """String literalini döndürür; f-string ise {ifade} bölümlerini çevirir."""
    eslesme = _ONEK_RE.match(tok)
    if not eslesme:
        return tok
    onek, govde = eslesme.group(1), eslesme.group(2)

    if 'f' not in onek.lower():
        return tok

    if govde.startswith('"""') or govde.startswith("'''"):
        tirnak = govde[:3]
    elif govde[:1] in ('"', "'"):
        tirnak = govde[0]
    else:
        return tok

    if not govde.endswith(tirnak) or len(govde) < 2 * len(tirnak):
        return tok

    icerik = govde[len(tirnak):-len(tirnak)]
    return onek + tirnak + _fstring_cevir(icerik) + tirnak


def _fstring_cevir(icerik: str) -> str:
    """f-string içindeki {ifade} bölümlerindeki Türkçe kodu çevirir."""
    sonuc = []
    i = 0
    n = len(icerik)

    while i < n:
        karakter = icerik[i]

        # Kaçışlı süslü parantezler: {{ ve }}
        if karakter == '{' and i + 1 < n and icerik[i + 1] == '{':
            sonuc.append('{{')
            i += 2
            continue
        if karakter == '}' and i + 1 < n and icerik[i + 1] == '}':
            sonuc.append('}}')
            i += 2
            continue

        if karakter != '{':
            sonuc.append(karakter)
            i += 1
            continue

        # Eşleşen kapanış parantezini bul
        bitis = _eslesen_kapanis(icerik, i)
        if bitis is None:
            sonuc.append(karakter)
            i += 1
            continue

        ifade = icerik[i + 1:bitis]
        sonuc.append('{' + _fstring_ifade_cevir(ifade) + '}')
        i = bitis + 1

    return ''.join(sonuc)


def _eslesen_kapanis(metin: str, baslangic: int):
    """baslangic'taki '{' için eşleşen '}' indeksini döndürür."""
    derinlik = 0
    i = baslangic
    tirnak = None
    while i < len(metin):
        karakter = metin[i]

        if tirnak:
            if karakter == '\\':
                i += 2
                continue
            if karakter == tirnak:
                tirnak = None
            i += 1
            continue

        if karakter in ('"', "'"):
            tirnak = karakter
        elif karakter in '([{':
            derinlik += 1
        elif karakter in ')]}':
            derinlik -= 1
            if derinlik == 0 and karakter == '}':
                return i
        i += 1

    return None


def _fstring_ifade_cevir(ifade: str) -> str:
    """Tek bir f-string ifadesini (dönüşüm/biçim eki hariç) çevirir."""
    if not ifade.strip():
        return ifade

    # Sondaki hata ayıklama '=' işaretini koru
    kirpik = ifade.rstrip()
    sonek = ifade[len(kirpik):]
    if kirpik.endswith('='):
        kirpik = kirpik[:-1]

    # Üst düzey '!' dönüşümü veya ':' biçim belirtecini bul
    ayrac = _ust_duzey_ayrac(kirpik)
    if ayrac is None:
        cevrilmis = cevir(kirpik)
        if ifade.rstrip().endswith('='):
            return cevrilmis + '=' + sonek
        return cevrilmis + sonek

    kesme, ayrac_karakteri = ayrac
    ifade_kismi = kirpik[:kesme]
    ek = kirpik[kesme:]
    return cevir(ifade_kismi) + ek + sonek


def _ust_duzey_ayrac(ifade: str):
    """Parantez/string dışındaki ilk ':' veya '!' konumunu döndürür."""
    derinlik = 0
    tirnak = None
    i = 0
    while i < len(ifade):
        karakter = ifade[i]
        if tirnak:
            if karakter == '\\':
                i += 2
                continue
            if karakter == tirnak:
                tirnak = None
            i += 1
            continue
        if karakter in ('"', "'"):
            tirnak = karakter
        elif karakter in '([{':
            derinlik += 1
        elif karakter in ')]}':
            derinlik -= 1
        elif derinlik == 0 and karakter in (':', '!'):
            # !=, := gibi operatörleri biçim/dönüşüm ayracı sanma
            if i + 1 < len(ifade) and ifade[i + 1] == '=':
                i += 2
                continue
            return i, karakter
        i += 1
    return None


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
