"""
PARS Metin Modülü — str işlemleri Türkçe sarmalayıcısı
"""

import re
from typing import List, Optional, Union

__all__ = [
    'buyuk_harf', 'kucuk_harf', 'bas_buyuk', 'her_bas_buyuk',
    'bosluk_temizle', 'bol', 'satirlara_bol', 'birlestir',
    'degistir', 'iceriyor_mu', 'ile_basliyor_mu', 'ile_bitiyor_mu',
    'bul', 'bul_sagdan', 'say', 'tekrarla', 'tersine_cevir',
    'doldur_sola', 'doldur_saga', 'ortala',
    'sayi_mi', 'harf_mi', 'alfanumerik_mi', 'bos_mu',
    'buyuk_harf_mi', 'kucuk_harf_mi',
    'sifrele', 'coz',
    'regex_bul', 'regex_degistir', 'regex_bol',
]


def buyuk_harf(s: str) -> str:
    """Tüm harfleri büyük yap."""
    return s.upper()


def kucuk_harf(s: str) -> str:
    """Tüm harfleri küçük yap."""
    return s.lower()


def bas_buyuk(s: str) -> str:
    """Yalnızca ilk harfi büyük yap."""
    return s.capitalize()


def her_bas_buyuk(s: str) -> str:
    """Her kelimenin ilk harfini büyük yap."""
    return s.title()


def bosluk_temizle(s: str, taraf: str = 'her') -> str:
    """
    Boşlukları temizle.

    Args:
        s: Girdi metni
        taraf: 'sol', 'sag' veya 'her'
    """
    if taraf == 'sol':
        return s.lstrip()
    elif taraf == 'sag':
        return s.rstrip()
    return s.strip()


def bol(s: str, ayraç: str = None, kez: int = -1) -> list:
    """Metni ayıraç ile böl."""
    return s.split(ayraç, kez)


def satirlara_bol(s: str) -> list:
    """Metni satırlara böl."""
    return s.splitlines()


def birlestir(ayraç: str, liste: list) -> str:
    """Listeyi ayraç ile birleştir."""
    return ayraç.join(str(i) for i in liste)


def degistir(s: str, eski: str, yeni: str, kez: int = -1) -> str:
    """Alt dizgi değiştir."""
    return s.replace(eski, yeni, kez)


def iceriyor_mu(s: str, aranan: str) -> bool:
    """Metin aranan ifadeyi içeriyor mu?"""
    return aranan in s


def ile_basliyor_mu(s: str, onek: str) -> bool:
    """Belirtilen önek ile başlıyor mu?"""
    return s.startswith(onek)


def ile_bitiyor_mu(s: str, sonek: str) -> bool:
    """Belirtilen sonek ile bitiyor mu?"""
    return s.endswith(sonek)


def bul(s: str, aranan: str, bas: int = 0) -> int:
    """Alt dizgiyi bul, indeks döndür. Bulamazsa -1."""
    return s.find(aranan, bas)


def bul_sagdan(s: str, aranan: str) -> int:
    """Alt dizgiyi sağdan bul."""
    return s.rfind(aranan)


def say(s: str, aranan: str) -> int:
    """Alt dizginin tekrar sayısını say."""
    return s.count(aranan)


def tekrarla(s: str, n: int) -> str:
    """Metni n kez tekrarla."""
    return s * n


def tersine_cevir(s: str) -> str:
    """Metni ters çevir."""
    return s[::-1]


def doldur_sola(s: str, genislik: int, doldurma: str = ' ') -> str:
    """Sola doldur."""
    return s.rjust(genislik, doldurma)


def doldur_saga(s: str, genislik: int, doldurma: str = ' ') -> str:
    """Sağa doldur."""
    return s.ljust(genislik, doldurma)


def ortala(s: str, genislik: int) -> str:
    """Metni ortala."""
    return s.center(genislik)


def sayi_mi(s: str) -> bool:
    """Metin sayı mı?"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def harf_mi(s: str) -> bool:
    """Metin yalnızca harflerden mi oluşuyor?"""
    return s.isalpha()


def alfanumerik_mi(s: str) -> bool:
    """Metin alfanümerik mi?"""
    return s.isalnum()


def bos_mu(s: str) -> bool:
    """Metin boş mu?"""
    return len(s.strip()) == 0


def buyuk_harf_mi(s: str) -> bool:
    """Metin yalnızca büyük harflerden mi?"""
    return s.isupper()


def kucuk_harf_mi(s: str) -> bool:
    """Metin yalnızca küçük harflerden mi?"""
    return s.islower()


def sifrele(s: str, kodlama: str = 'utf-8') -> bytes:
    """Metni bayt dizisine çevir (encode)."""
    return s.encode(kodlama)


def coz(b: bytes, kodlama: str = 'utf-8') -> str:
    """Bayt dizisini metne çevir (decode)."""
    return b.decode(kodlama)


def regex_bul(metin: str, desen: str, tumu: bool = False):
    """Regex ile ara."""
    if tumu:
        return re.findall(desen, metin)
    return re.search(desen, metin)


def regex_degistir(metin: str, desen: str, yeni: str) -> str:
    """Regex ile değiştir."""
    return re.sub(desen, yeni, metin)


def regex_bol(metin: str, desen: str) -> list:
    """Regex ile böl."""
    return re.split(desen, metin)
