"""
PARS Matematik Modülü — math kütüphanesi Türkçe sarmalayıcısı
"""

import math
import statistics
from typing import Union, Sequence

Sayi = Union[int, float]

PI = math.pi
E = math.e
TAU = math.tau
SONSUZ = math.inf
NAN = math.nan

__all__ = [
    'PI', 'E', 'TAU', 'SONSUZ', 'NAN',
    'kare_kok', 'us', 'mutlak', 'yuvarlak', 'tavan', 'taban_al', 'mod',
    'kare', 'kup', 'isaret', 'olcek', 'sinirla', 'yaklasik_esit',
    'asal_mi', 'tam_bolenler', 'kare_kok_tam', 'olcek_log',
    'sinus', 'kosinus', 'tanjant', 'ark_sinus', 'ark_kosinus', 'ark_tanjant',
    'ark_tanjant2', 'derece_radyan', 'radyan_derece', 'hipotenus',
    'logaritma', 'log10', 'log2', 'log1p', 'exp', 'expm1',
    'faktoriyel', 'kombinasyon', 'permutasyon', 'obeb', 'okek',
    'ortalama', 'medyan', 'mod_istatistik', 'standart_sapma', 'varyans',
    'kovaryans', 'toplam', 'carpanlar', 'en_yakin', 'dizi_toplami',
]


def kare_kok(x: Sayi) -> float:
    """Karekök hesapla."""
    return math.sqrt(x)


def us(taban: Sayi, ust: Sayi) -> float:
    """Üs alma."""
    return math.pow(taban, ust)


def mutlak(x: Sayi) -> Sayi:
    """Mutlak değer."""
    return abs(x)


def yuvarlak(x: Sayi, basamak: int = 0) -> float:
    """Yuvarlama."""
    return round(x, basamak)


def tavan(x: Sayi) -> int:
    """Tavan (yukarı yuvarla)."""
    return math.ceil(x)


def taban_al(x: Sayi) -> int:
    """Taban (aşağı yuvarla)."""
    return math.floor(x)


def mod(x: Sayi, y: Sayi) -> Sayi:
    """Mod alma."""
    return x % y


# ── TRİGONOMETRİ ─────────────────────────────────────────────────────────

def sinus(x: Sayi) -> float:
    """Sinüs (radyan)."""
    return math.sin(x)


def kosinus(x: Sayi) -> float:
    """Kosinüs (radyan)."""
    return math.cos(x)


def tanjant(x: Sayi) -> float:
    """Tanjant (radyan)."""
    return math.tan(x)


def ark_sinus(x: Sayi) -> float:
    """Ark sinüs."""
    return math.asin(x)


def ark_kosinus(x: Sayi) -> float:
    """Ark kosinüs."""
    return math.acos(x)


def ark_tanjant(x: Sayi) -> float:
    """Ark tanjant."""
    return math.atan(x)


def ark_tanjant2(y: Sayi, x: Sayi) -> float:
    """İki değişkenli ark tanjant."""
    return math.atan2(y, x)


def derece_radyan(d: Sayi) -> float:
    """Dereceyi radyana çevir."""
    return math.radians(d)


def radyan_derece(r: Sayi) -> float:
    """Radyanı dereceye çevir."""
    return math.degrees(r)


def hipotenus(*sayilar: Sayi) -> float:
    """Hipotenüs hesapla."""
    return math.hypot(*sayilar)


# ── LOGARİTMA / ÜS ───────────────────────────────────────────────────────

def logaritma(x: Sayi, taban: Sayi = None) -> float:
    """Logaritma. Taban belirtilmezse doğal logaritma."""
    if taban is None:
        return math.log(x)
    return math.log(x, taban)


def log10(x: Sayi) -> float:
    """10 tabanında logaritma."""
    return math.log10(x)


def log2(x: Sayi) -> float:
    """2 tabanında logaritma."""
    return math.log2(x)


def exp(x: Sayi) -> float:
    """Doğal üstel (e^x)."""
    return math.exp(x)


# ── KOMBİNATORİK ─────────────────────────────────────────────────────────

def faktoriyel(n: int) -> int:
    """Faktöriyel hesapla."""
    return math.factorial(n)


def kombinasyon(n: int, k: int) -> int:
    """Kombinasyon C(n, k)."""
    return math.comb(n, k)


def permutasyon(n: int, k: int = None) -> int:
    """Permütasyon P(n, k)."""
    return math.perm(n, k)


def obeb(a: int, b: int) -> int:
    """Ortak bölenlerin en büyüğü."""
    return math.gcd(a, b)


def okek(a: int, b: int) -> int:
    """Ortak katların en küçüğü."""
    return math.lcm(a, b)


# ── İSTATİSTİK ───────────────────────────────────────────────────────────

def ortalama(sayilar: Sequence[Sayi]) -> float:
    """Aritmetik ortalama."""
    return statistics.mean(sayilar)


def medyan(sayilar: Sequence[Sayi]) -> float:
    """Medyan."""
    return statistics.median(sayilar)


def mod_istatistik(sayilar: Sequence[Sayi]):
    """Mod (en sık tekrar eden değer)."""
    return statistics.mode(sayilar)


def standart_sapma(sayilar: Sequence[Sayi]) -> float:
    """Standart sapma."""
    return statistics.stdev(sayilar)


def varyans(sayilar: Sequence[Sayi]) -> float:
    """Varyans."""
    return statistics.variance(sayilar)


def kovaryans(x: Sequence[Sayi], y: Sequence[Sayi]) -> float:
    """İki veri seti arasındaki kovaryans."""
    return statistics.covariance(x, y)

# ── GENİŞLETİLMİŞ YARDIMCILAR (v1.0.1) ──────────────────────────────────

def kare(x: Sayi) -> Sayi:
    """Karesini al."""
    return x * x


def kup(x: Sayi) -> Sayi:
    """Küpünü al."""
    return x * x * x


def isaret(x: Sayi) -> int:
    """İşaret: -1, 0 veya 1."""
    return (x > 0) - (x < 0)


def olcek(x: Sayi, alt: Sayi, ust: Sayi,
          yeni_alt: Sayi = 0, yeni_ust: Sayi = 1) -> float:
    """Bir aralıktaki değeri başka aralığa ölçekle."""
    if ust == alt:
        return yeni_alt
    return yeni_alt + (x - alt) * (yeni_ust - yeni_alt) / (ust - alt)


def sinirla(x: Sayi, alt: Sayi, ust: Sayi) -> Sayi:
    """Değeri [alt, ust] aralığına sıkıştır."""
    return max(alt, min(ust, x))


def yaklasik_esit(a: Sayi, b: Sayi, tolerans: float = 1e-9) -> bool:
    """İki sayı tolerans içinde eşit mi?"""
    return abs(a - b) <= tolerans


def asal_mi(n: int) -> bool:
    """Asal sayı mı?"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def tam_bolenler(n: int) -> list:
    """Pozitif tam bölenler."""
    if n == 0:
        return []
    n = abs(n)
    kucuk = [i for i in range(1, int(math.isqrt(n)) + 1) if n % i == 0]
    buyuk = [n // i for i in kucuk if i != n // i]
    return sorted(kucuk + buyuk)


def kare_kok_tam(n: int) -> int:
    """Tamsayı karekök (aşağı yuvarlanmış)."""
    return math.isqrt(n)


def olcek_log(x: Sayi, taban: Sayi = 10) -> float:
    """Logaritmik ölçek."""
    return math.log(x, taban)


def log1p(x: Sayi) -> float:
    """log(1 + x), küçük x için hassas."""
    return math.log1p(x)


def expm1(x: Sayi) -> float:
    """e^x - 1, küçük x için hassas."""
    return math.expm1(x)


def toplam(sayilar: Sequence[Sayi]) -> Sayi:
    return sum(sayilar)


def carpanlar(n: int) -> list:
    """Asal çarpanlar."""
    n = abs(n)
    sonuc = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            sonuc.append(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        sonuc.append(n)
    return sonuc


def en_yakin(deger: Sayi, secenekler: Sequence[Sayi]) -> Sayi:
    """Değere en yakın seçeneği döndür."""
    return min(secenekler, key=lambda s: abs(s - deger))


def dizi_toplami(sayilar: Sequence[Sayi]) -> float:
    """Hassas (Kahan) toplam."""
    return math.fsum(sayilar)
