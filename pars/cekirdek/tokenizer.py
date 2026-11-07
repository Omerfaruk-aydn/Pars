"""
PARS Tokenizer
--------------
Türkçe kaynak kodu güvenli biçimde tokenlarına ayıran modül.
String içleri, yorumlar ve f-string'ler asla bozulmaz.

Token türleri:
  STR   → "...", '...', f"...", r'...', b"...", rb'...', üçlü tırnaklar
  YORUM → # ... (satır sonu)
  ISIM  → Türkçe/İngilizce tanımlayıcı (anahtar kelime kontrolü yapılır)
  DIGER → operatör, boşluk, sayı, noktalama

Tokenizasyon kayıpsızdır: ''.join(metin for _, metin in tokenize(kod)) == kod
"""

import re
from typing import List, Tuple

# Python'un desteklediği string önekleri (büyük/küçük harf duyarsız).
# Uzun kombinasyonlar önce gelmeli: fr, rf, rb, br, ...
_ONEK = r'(?:[fF][rR]?|[rR][fF]?|[bB][rR]?|[rR][bB]?|[uU])?'

# Sayılar: hex, bin, oct, ondalık, üs, alt çizgi ayıracı, karmaşık sonek
_SAYI = (
    r'(?:0[xX][0-9a-fA-F_]+'
    r'|0[bB][01_]+'
    r'|0[oO][0-7_]+'
    r'|(?:\d[\d_]*(?:\.[\d_]*)?|\.[\d_]+)(?:[eE][+-]?\d[\d_]*)?[jJ]?)'
)

TOKEN_RE = re.compile(
    _ONEK + r'(?:"""[\s\S]*?"""'
    r"|'''[\s\S]*?'''"
    r'|"(?:[^"\\\n]|\\.)*"'
    r"|'(?:[^'\\\n]|\\.)*')"
    r'|#[^\n]*'
    r'|' + _SAYI +
    r'|[^\W\d]\w*'
    r'|.',
    re.DOTALL | re.UNICODE
)

TokenListesi = List[Tuple[str, str]]

_STRING_BASLANGIC = re.compile(_ONEK + r'(?:"""|\'\'\'|"|\')')


def _string_mi(tok: str) -> bool:
    """Token gerçekten bir string literali mi? (önek + tırnak)"""
    return _STRING_BASLANGIC.match(tok) is not None


def _sayi_mi(tok: str) -> bool:
    return re.fullmatch(_SAYI, tok) is not None


def tokenize(kod: str) -> TokenListesi:
    """
    Kodu (tur, metin) çiftlerinden oluşan token listesine ayırır.

    Args:
        kod: PARS kaynak kodu

    Returns:
        List[Tuple[str, str]]: (tur, metin) çiftleri
        Türler: 'STR' | 'YORUM' | 'ISIM' | 'DIGER'
    """
    tokenlar: TokenListesi = []

    for m in TOKEN_RE.finditer(kod):
        tok = m.group()

        if _string_mi(tok):
            tokenlar.append(('STR', tok))
        elif tok[0] == '#':
            tokenlar.append(('YORUM', tok))
        elif _sayi_mi(tok):
            # Geriye dönük uyumluluk: sayılar DIGER olarak kalır
            tokenlar.append(('DIGER', tok))
        elif tok[0].isalpha() or tok[0] == '_' or (
            len(tok[0]) == 1 and ord(tok[0]) > 127
        ):
            tokenlar.append(('ISIM', tok))
        else:
            tokenlar.append(('DIGER', tok))

    return tokenlar


__all__ = ['tokenize', 'TokenListesi']
