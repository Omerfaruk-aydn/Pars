"""
PARS Şifreleme Modülü — hashlib / hmac / base64 / secrets Türkçe sarmalayıcısı
"""

import base64
import hashlib
import hmac
import secrets
import uuid
from typing import Optional

__all__ = [
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
    'hash_hesapla', 'dosya_hash', 'hmac_hesapla', 'sabit_karsilastir',
    'base64_kodla', 'base64_coz', 'url_base64_kodla', 'url_base64_coz',
    'rastgele_metin', 'rastgele_bayt', 'rastgele_sayi', 'uuid4', 'uuid_hex',
]


def _hash(metin, algoritma: str) -> str:
    if isinstance(metin, str):
        metin = metin.encode('utf-8')
    return hashlib.new(algoritma, metin).hexdigest()


def md5(metin) -> str:
    return _hash(metin, 'md5')


def sha1(metin) -> str:
    return _hash(metin, 'sha1')


def sha224(metin) -> str:
    return _hash(metin, 'sha224')


def sha256(metin) -> str:
    return _hash(metin, 'sha256')


def sha384(metin) -> str:
    return _hash(metin, 'sha384')


def sha512(metin) -> str:
    return _hash(metin, 'sha512')


def hash_hesapla(metin, algoritma: str = 'sha256') -> str:
    return _hash(metin, algoritma)


def dosya_hash(yol: str, algoritma: str = 'sha256',
               blok_boyutu: int = 65536) -> str:
    """Dosyanın hash değerini hesapla."""
    h = hashlib.new(algoritma)
    with open(yol, 'rb') as f:
        while True:
            blok = f.read(blok_boyutu)
            if not blok:
                break
            h.update(blok)
    return h.hexdigest()


def hmac_hesapla(anahtar, mesaj, algoritma: str = 'sha256') -> str:
    """HMAC imzası üret."""
    if isinstance(anahtar, str):
        anahtar = anahtar.encode('utf-8')
    if isinstance(mesaj, str):
        mesaj = mesaj.encode('utf-8')
    return hmac.new(anahtar, mesaj, algoritma).hexdigest()


def sabit_karsilastir(a, b) -> bool:
    """Zamanlama saldırılarına dayanıklı karşılaştırma."""
    if isinstance(a, str):
        a = a.encode('utf-8')
    if isinstance(b, str):
        b = b.encode('utf-8')
    return hmac.compare_digest(a, b)


def base64_kodla(veri) -> str:
    if isinstance(veri, str):
        veri = veri.encode('utf-8')
    return base64.b64encode(veri).decode('ascii')


def base64_coz(metin: str) -> bytes:
    return base64.b64decode(metin)


def url_base64_kodla(veri) -> str:
    if isinstance(veri, str):
        veri = veri.encode('utf-8')
    return base64.urlsafe_b64encode(veri).decode('ascii')


def url_base64_coz(metin: str) -> bytes:
    return base64.urlsafe_b64decode(metin)


def rastgele_metin(uzunluk: int = 16,
                   alfabe: Optional[str] = None) -> str:
    if alfabe is None:
        alfabe = ('abcdefghijklmnopqrstuvwxyz'
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return ''.join(secrets.choice(alfabe) for _ in range(uzunluk))


def rastgele_bayt(uzunluk: int = 16) -> bytes:
    return secrets.token_bytes(uzunluk)


def rastgele_sayi(baslangic: int, son: int) -> int:
    return baslangic + secrets.randbelow(son - baslangic + 1)


def uuid4() -> str:
    return str(uuid.uuid4())


def uuid_hex() -> str:
    return uuid.uuid4().hex
