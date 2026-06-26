"""
PARS Liste Modülü — list/dict/set yardımcıları
"""

from typing import Any, Callable, List, Dict, Tuple, Optional
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
