"""
PARS Liste Modülü — list/dict/set yardımcıları
"""

from typing import Any, Callable, Tuple
from collections import defaultdict, OrderedDict
from functools import reduce

__all__ = [
    'duzlestir', 'tekil', 'grupla', 'dondur_liste',
    'zip_ile_birlestir', 'sirala_ters', 'filtrele', 'haritala', 'azalt',
    'bolustur', 'ortak_elemanlar', 'fark', 'birlesim',
    'anahtarlar', 'degerler', 'ciftler',
    'sozluk_filtrele', 'sozluk_harita', 'sozluk_birlestir', 'tersle',
    'varsayilan_sozluk', 'sirali_sozluk',
    'yigin_olustur', 'yigina_ekle', 'yigindan_al',
    'kuyruk_olustur', 'kuyruga_ekle', 'kuyruktan_al',
    'ilk', 'son', 'orta', 'pencere', 'parcala', 'sikistir', 'zip_uzun',
    'karistir', 'ornek', 'indeks', 'sayim', 'kesisim',
    'sozluk_anahtar_degistir', 'sozluk_derin_birlestir', 'liste_esitle',
]


# ── LİSTE İŞLEMLERİ ──────────────────────────────────────────────────────

def duzlestir(iç_içe_liste: list, derinlik: int = 1) -> list:
    """İç içe listeyi düzleştir."""
    sonuc = []
    for eleman in iç_içe_liste:
        if isinstance(eleman, list) and derinlik > 0:
            sonuc.extend(duzlestir(eleman, derinlik - 1))
        else:
            sonuc.append(eleman)
    return sonuc


def tekil(liste: list) -> list:
    """Benzersiz elemanları döndür (sırayı korur)."""
    goruldu = set()
    sonuc = []
    for eleman in liste:
        if eleman not in goruldu:
            goruldu.add(eleman)
            sonuc.append(eleman)
    return sonuc


def grupla(liste: list, n: int) -> list:
    """Listeyi n'li gruplara böl."""
    return [liste[i:i + n] for i in range(0, len(liste), n)]


def dondur_liste(liste: list, n: int) -> list:
    """Listeyi döngüsel olarak kaydır."""
    if not liste:
        return liste
    n = n % len(liste)
    return liste[n:] + liste[:n]


def zip_ile_birlestir(*listeler) -> list:
    """Birden fazla listeyi zip ile birleştir."""
    return list(zip(*listeler))


def sirala_ters(liste: list) -> list:
    """Listeyi tersten sıralı döndür."""
    return sorted(liste, reverse=True)


def filtrele(fonk: Callable, liste: list) -> list:
    """Fonksiyona uyan elemanları filtrele."""
    return list(filter(fonk, liste))


def haritala(fonk: Callable, liste: list) -> list:
    """Fonksiyonu her elemana uygula."""
    return list(map(fonk, liste))


def azalt(fonk: Callable, liste: list, baslangic: Any = None) -> Any:
    """Reduce işlemi."""
    if baslangic is not None:
        return reduce(fonk, liste, baslangic)
    return reduce(fonk, liste)


def bolustur(liste: list, kosul: Callable) -> Tuple[list, list]:
    """Listeyi koşula göre ikiye böl: (doğrular, yanlışlar)."""
    dogrular = [x for x in liste if kosul(x)]
    yanlislar = [x for x in liste if not kosul(x)]
    return dogrular, yanlislar


def ortak_elemanlar(*listeler) -> list:
    """Tüm listelerde ortak olan elemanları döndür."""
    if not listeler:
        return []
    kume = set(listeler[0])
    for l in listeler[1:]:
        kume &= set(l)
    return list(kume)


def fark(*listeler) -> list:
    """İlk listede olup diğerlerinde olmayan elemanlar."""
    if not listeler:
        return []
    sonuc = set(listeler[0])
    for l in listeler[1:]:
        sonuc -= set(l)
    return list(sonuc)


def birlesim(*listeler) -> list:
    """Tüm listelerin birleşimi (benzersiz)."""
    sonuc = []
    goruldu = set()
    for l in listeler:
        for eleman in l:
            if eleman not in goruldu:
                goruldu.add(eleman)
                sonuc.append(eleman)
    return sonuc


# ── SÖZLÜK İŞLEMLERİ ─────────────────────────────────────────────────────

def anahtarlar(sozluk: dict) -> list:
    """Sözlüğün anahtarlarını döndür."""
    return list(sozluk.keys())


def degerler(sozluk: dict) -> list:
    """Sözlüğün değerlerini döndür."""
    return list(sozluk.values())


def ciftler(sozluk: dict) -> list:
    """Sözlüğün anahtar-değer çiftlerini döndür."""
    return list(sozluk.items())


def sozluk_filtrele(sozluk: dict, kosul: Callable) -> dict:
    """Sözlüğü koşula göre filtrele."""
    return {k: v for k, v in sozluk.items() if kosul(k, v)}


def sozluk_harita(sozluk: dict, fonk: Callable) -> dict:
    """Sözlüğün değerlerine fonksiyon uygula."""
    return {k: fonk(v) for k, v in sozluk.items()}


def sozluk_birlestir(*sozlukler) -> dict:
    """Birden fazla sözlüğü birleştir."""
    sonuc = {}
    for s in sozlukler:
        sonuc.update(s)
    return sonuc


def tersle(sozluk: dict) -> dict:
    """Anahtar-değer yerlerini değiştir."""
    return {v: k for k, v in sozluk.items()}


def varsayilan_sozluk(varsayilan: Any) -> dict:
    """Varsayılan değerli sözlük (defaultdict)."""
    return defaultdict(varsayilan)


def sirali_sozluk() -> dict:
    """Sıralı sözlük (OrderedDict)."""
    return OrderedDict()


# ── YIĞIN VE KUYRUK ──────────────────────────────────────────────────────

def yigin_olustur() -> list:
    """Yığın (stack) oluştur."""
    return []


def yigina_ekle(yigin: list, eleman: Any) -> None:
    """Yığına eleman ekle (push)."""
    yigin.append(eleman)


def yigindan_al(yigin: list) -> Any:
    """Yığından eleman al (pop)."""
    if not yigin:
        raise IndexError('Yığın boş')
    return yigin.pop()


def kuyruk_olustur() -> list:
    """Kuyruk (queue) oluştur."""
    return []


def kuyruga_ekle(kuyruk: list, eleman: Any) -> None:
    """Kuyruğa eleman ekle."""
    kuyruk.append(eleman)


def kuyruktan_al(kuyruk: list) -> Any:
    """Kuyruktan eleman al."""
    if not kuyruk:
        raise IndexError('Kuyruk boş')
    return kuyruk.pop(0)

# ── GENİŞLETİLMİŞ YARDIMCILAR (v1.0.1) ──────────────────────────────────

def ilk(liste: list, n: int = 1):
    """İlk eleman(lar)."""
    return liste[0] if n == 1 else liste[:n]


def son(liste: list, n: int = 1):
    """Son eleman(lar)."""
    return liste[-1] if n == 1 else liste[-n:]


def orta(liste: list):
    """Orta eleman(lar)."""
    n = len(liste)
    if n == 0:
        return None
    if n % 2:
        return liste[n // 2]
    return liste[n // 2 - 1:n // 2 + 1]


def pencere(liste: list, n: int) -> list:
    """Kayan pencere: [[1,2,3],[2,3,4],...]"""
    if n <= 0 or n > len(liste):
        return []
    return [liste[i:i + n] for i in range(len(liste) - n + 1)]


def parcala(liste: list, n: int) -> list:
    """Listeyi n parçaya böl (boyutlar dengeli)."""
    if n <= 0:
        return []
    k, m = divmod(len(liste), n)
    sonuc, bas = [], 0
    for i in range(n):
        bit = bas + k + (1 if i < m else 0)
        sonuc.append(liste[bas:bit])
        bas = bit
    return sonuc


def sikistir(*listeler) -> list:
    """zip takma adı."""
    return list(zip(*listeler))


def zip_uzun(*listeler, dolgu=None) -> list:
    """En uzun listeye göre zip."""
    from itertools import zip_longest
    return list(zip_longest(*listeler, fillvalue=dolgu))


def karistir(liste: list) -> list:
    """Karıştırılmış kopya."""
    import random
    kopya = list(liste)
    random.shuffle(kopya)
    return kopya


def ornek(liste: list, n: int) -> list:
    """Rastgele n eleman."""
    import random
    return random.sample(liste, n)


def indeks(liste: list, deger) -> int:
    """Değerin indeksi; yoksa -1."""
    try:
        return liste.index(deger)
    except ValueError:
        return -1


def sayim(liste: list, deger) -> int:
    """Değerin tekrar sayısı."""
    return liste.count(deger)


def kesisim(*listeler) -> list:
    """Kesişim (sıra korunur)."""
    if not listeler:
        return []
    sonuc = []
    for eleman in listeler[0]:
        if all(eleman in l for l in listeler[1:]) and eleman not in sonuc:
            sonuc.append(eleman)
    return sonuc


def sozluk_anahtar_degistir(sozluk: dict, esleme: dict) -> dict:
    """Sözlük anahtarlarını eşlemeye göre değiştir."""
    return {esleme.get(k, k): v for k, v in sozluk.items()}


def sozluk_derin_birlestir(a: dict, b: dict) -> dict:
    """İç içe sözlükleri derin birleştir."""
    sonuc = dict(a)
    for k, v in b.items():
        if k in sonuc and isinstance(sonuc[k], dict) and isinstance(v, dict):
            sonuc[k] = sozluk_derin_birlestir(sonuc[k], v)
        else:
            sonuc[k] = v
    return sonuc


def liste_esitle(liste: list, uzunluk: int, dolgu=None) -> list:
    """Listeyi belirtilen uzunluğa getir (kırp/doldur)."""
    sonuc = list(liste[:uzunluk])
    sonuc.extend([dolgu] * (uzunluk - len(sonuc)))
    return sonuc
