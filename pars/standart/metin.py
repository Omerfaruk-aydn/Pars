"""
PARS Metin Modülü — str işlemleri Türkçe sarmalayıcısı
"""

import re

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
    'kelimeler', 'satir_sayisi', 'kisalt', 'sar', 'girintile',
    'girinti_kaldir', 'slug', 'yilan_case', 'deve_case', 'yuzde_kodla',
    'yuzde_coz', 'html_kacis', 'html_coz', 'benzerlik', 'farklar',
    'bicim', 'tersten', 'sayi_metni', 'kirp', 'son',
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

# ── GENİŞLETİLMİŞ YARDIMCILAR (v1.0.1) ──────────────────────────────────

def kelimeler(s: str) -> list:
    """Metni kelimelere ayır."""
    return s.split()


def satir_sayisi(s: str) -> int:
    """Satır sayısı."""
    return len(s.splitlines()) if s else 0


def kisalt(s: str, uzunluk: int = 30, sonek: str = '...') -> str:
    """Metni belirtilen uzunlukta kısalt."""
    if len(s) <= uzunluk:
        return s
    return s[:max(0, uzunluk - len(sonek))] + sonek


def sar(s: str, genislik: int = 70) -> str:
    """Metni satırlara sar."""
    import textwrap
    return textwrap.fill(s, width=genislik)


def girintile(s: str, onek: str = '    ') -> str:
    """Her satırın başına önek ekle."""
    import textwrap
    return textwrap.indent(s, onek)


def girinti_kaldir(s: str) -> str:
    """Ortak girintiyi kaldır."""
    import textwrap
    return textwrap.dedent(s)


def slug(s: str) -> str:
    """URL dostu metin üret."""
    tablo = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
    s = s.translate(tablo).lower()
    import re as _re
    s = _re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def yilan_case(s: str) -> str:
    """snake_case biçimine çevir."""
    import re as _re
    s = _re.sub(r'(?<!^)(?=[A-Z])', '_', s)
    return _re.sub(r'[\s\-]+', '_', s).lower()


def deve_case(s: str) -> str:
    """camelCase biçimine çevir."""
    parcalar = yilan_case(s).split('_')
    return parcalar[0] + ''.join(p.capitalize() for p in parcalar[1:])


def yuzde_kodla(s: str, guvenli: str = '') -> str:
    """URL yüzde kodlaması."""
    from urllib.parse import quote
    return quote(s, safe=guvenli)


def yuzde_coz(s: str) -> str:
    """URL yüzde kodunu çöz."""
    from urllib.parse import unquote
    return unquote(s)


def html_kacis(s: str) -> str:
    """HTML özel karakterlerini kaçır."""
    import html
    return html.escape(s)


def html_coz(s: str) -> str:
    """HTML kaçışlarını çöz."""
    import html
    return html.unescape(s)


def benzerlik(a: str, b: str) -> float:
    """İki metin arasındaki benzerlik oranı (0-1)."""
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()


def farklar(a: str, b: str) -> list:
    """İki metin arasındaki fark satırları."""
    import difflib
    return list(difflib.unified_diff(a.splitlines(), b.splitlines(),
                                     lineterm=''))


def bicim(sablon: str, **degerler) -> str:
    """Metin şablonunu doldur."""
    return sablon.format(**degerler)


def tersten(s: str) -> str:
    """tersine_cevir takma adı."""
    return s[::-1]


def sayi_metni(n, basamak: int = 2) -> str:
    """Say?y? T?rk?e binlik/ondal?k ayra?l? metne ?evir (1.234,56)."""
    metin = f'{n:,.{basamak}f}'
    metin = metin.replace(',', '\x00').replace('.', ',').replace('\x00', '.')
    return metin


def kirp(s: str, uzunluk: int) -> str:
    """İlk n karakter."""
    return s[:uzunluk]


def son(s: str, uzunluk: int) -> str:
    """Son n karakter."""
    return s[-uzunluk:] if uzunluk else ''
