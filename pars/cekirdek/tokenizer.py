"""
PARS Tokenizer
--------------
Türkçe kaynak kodu güvenli biçimde tokenlarına ayıran modül.
String içleri, yorumlar ve f-string'ler asla değiştirilmez.

Token türleri:
  STR   → "...", '...', f"...", f'...', \"\"\"...\"\"\", '''...'''
  YORUM → # ... (satır sonu)
  ISIM  → Türkçe/İngilizce tanımlayıcı (anahtar kelime kontrolü yapılır)
  DIGER → operatör, boşluk, sayı, noktalama
"""

import re
from typing import List, Tuple

TOKEN_RE = re.compile(
    r'"""[\s\S]*?"""'
    r"|'''[\s\S]*?'''"
    r'|f"(?:[^"\\]|\\.)*"'
    r"|f'(?:[^'\\]|\\.)*'"
    r'|"(?:[^"\\]|\\.)*"'
    r"|'(?:[^'\\]|\\.)*'"
    r'|#[^\n]*'
    r'|\d+\.?\d*'
    r'|[\w][\w\d]*'
    r'|.',
    re.DOTALL | re.UNICODE
)

TokenListesi = List[Tuple[str, str]]


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
        ilk = tok[0]

        if ilk in ('"', "'"):
            tokenlar.append(('STR', tok))
        elif ilk == 'f' and len(tok) > 1 and tok[1] in ('"', "'"):
            tokenlar.append(('STR', tok))
        elif ilk == '#':
            tokenlar.append(('YORUM', tok))
        elif ilk.isdigit():
            tokenlar.append(('DIGER', tok))
        elif ilk.isalpha() or ilk == '_' or (len(ilk) == 1 and ord(ilk) > 127):
            tokenlar.append(('ISIM', tok))
        else:
            tokenlar.append(('DIGER', tok))

    return tokenlar


__all__ = ['tokenize', 'TokenListesi']
