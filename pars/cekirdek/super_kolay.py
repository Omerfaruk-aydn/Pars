"""
PARS Süper Kolay Modül
----------------------
Doğal Türkçe cümlelerle kod yazma.
Neredeyse normal Türkçe konuşuyormuş gibi kod yazın.

Örnekler:
  merhaba dunya yazdir
  ismini ogren ve goster
  5 kere say
  sayilari sirala ve goster
"""

import re
from typing import List


def super_kolay_cevir(kod: str) -> str:
    """
    Doğal Türkçe cümleleri PARS koduna çevirir.

    Args:
        kod: Doğal Türkçe PARS kodu

    Returns:
        str: Standart PARS kodu
    """
    satirlar = kod.splitlines()
    sonuc: List[str] = []

    for satir in satirlar:
        temiz = satir.strip().lower()

        # Boş satır
        if not temiz:
            sonuc.append('')
            continue

        # Yorum
        if temiz.startswith('#'):
            sonuc.append(satir)
            continue

        # En basit komutları kontrol et
        donustur = _dogal_cevir(temiz, satir.strip())
        sonuc.append(donustur)

    return '\n'.join(sonuc)


def _dogal_cevir(temiz: str, orijinal: str) -> str:
    """Doğal Türkçe cümleyi PARS koduna çevirir."""

    # === YAZDIRMA KOMUTLARI ===

    # "merhaba dunya yaz" / "merhaba dunya yazdir"
    eslesme = re.match(r'^(.+?)\s+yaz(dir)?$', temiz)
    if eslesme:
        metin = eslesme.group(1).strip()
        return f'yaz("{_metin_duzenle(metin)}")'

    # "x ekrana yaz" / "x ekrana yazdir"
    eslesme = re.match(r'^(.+?)\s+ekrana\s+yaz(dir)?$', temiz)
    if eslesme:
        metin = eslesme.group(1).strip()
        return f'yaz("{_metin_duzenle(metin)}")'

    # "merhaba" (tek kelime, yazdır gibi davran)
    if re.match(r'^[a-zA-ZçğıöşüÇĞİÖÜ]+$', temiz) and len(temiz) > 2:
        if temiz not in ('son', 'degilse', 'değilse', 'ise'):
            return f'yaz("{temiz}")'

    # === GIRDI ALMA KOMUTLARI ===

    # "ismini ogren" / "isim al" / "isim gir"
    eslesme = re.match(r'^(\w+)\s+(ogren|al|gir|sor)$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'{degisken} = girdial("{degisken}: ")'

    # "kac yasin ogren"
    eslesme = re.match(r'^(.+?)\s+ogren$', temiz)
    if eslesme:
        mesaj = eslesme.group(1).strip()
        return f'girdial("{mesaj}: ")'

    # === DÖNGÜ KOMUTLARI ===

    # "5 kere say" / "5 kere tekrarla" / "5 kez say"
    eslesme = re.match(r'^(\d+)\s+(kere|kez)\s+(say|tekrarla|dondur|calistir)$', temiz)
    if eslesme:
        sayi = eslesme.group(1)
        return f'için i içinde aralık({sayi}):'

    # "1 den 10 a kadar say"
    eslesme = re.match(r'^(\d+)\s+den\s+(\d+)\s+a\s+kadar\s+(say|tekrarla)$', temiz)
    if eslesme:
        bas = eslesme.group(1)
        son = eslesme.group(2)
        return f'için i içinde aralık({bas}, {son} + 1):'

    # "her sayiyi goster" / "sayilari gez"
    eslesme = re.match(r'^her\s+(\w+)\s+(gez|goster|isle)$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'için {degisken} içinde {degisken}:'

    # === KOŞUL KOMUTLARI ===

    # "eger buyukse yaz" / "buyukse yaz"
    eslesme = re.match(r'^(eger|eğer)?\s*(\w+)\s+(\d+)\s+(buyukse|kucukse|esitse)$', temiz)
    if eslesme:
        degisken = eslesme.group(2)
        sayi = eslesme.group(3)
        operator = {
            'buyukse': '>',
            'kucukse': '<',
            'esitse': '=='
        }.get(eslesme.group(4), '==')
        return f'eğer {degisken} {operator} {sayi}:'

    # "sayi sifir buyuk mi?"
    eslesme = re.match(r'^(\w+)\s+(\d+)\s+(buyuk|kucuk|esit)\s+mi\?$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        sayi = eslesme.group(2)
        operator = {
            'buyuk': '>',
            'kucuk': '<',
            'esit': '=='
        }.get(eslesme.group(3), '==')
        return f'eğer {degisken} {operator} {sayi}:'

    # === FONKSİYON KOMUTLARI ===

    # "topla a ve b yap" / "topla a b yap"
    eslesme = re.match(r'^(\w+)\s+(\w+)(?:\s+ve\s+(\w+))?\s+yap$', temiz)
    if eslesme:
        ad = eslesme.group(1)
        p1 = eslesme.group(2)
        p2 = eslesme.group(3)
        parametreler = f'{p1}, {p2}' if p2 else p1
        return f'fonksiyon {ad}({parametreler}):'

    # "sonuc dondur" / "cevap dondur"
    eslesme = re.match(r'^(\w+)\s+dondur$', temiz)
    if eslesme:
        deger = eslesme.group(1)
        return f'döndür {deger}'

    # === İŞLEM KOMUTLARI ===

    # "x i 2 ile carp" / "x i 2 ye carp"
    eslesme = re.match(r'^(\w+)\s+i\s+(\d+)\s+(ile|ye)\s+carp$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        sayi = eslesme.group(2)
        return f'{degisken} = {degisken} * {sayi}'

    # "x i 2 ye bol"
    eslesme = re.match(r'^(\w+)\s+i\s+(\d+)\s+(ile|ye)\s+bol$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        sayi = eslesme.group(2)
        return f'{degisken} = {degisken} / {sayi}'

    # "x e 1 ekle" / "x e 5 ekle"
    eslesme = re.match(r'^(\w+)\s+e\s+(\d+)\s+ekle$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        sayi = eslesme.group(2)
        return f'{degisken} = {degisken} + {sayi}'

    # "x ten 1 cikar"
    eslesme = re.match(r'^(\w+)\s+ten\s+(\d+)\s+cikar$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        sayi = eslesme.group(2)
        return f'{degisken} = {degisken} - {sayi}'

    # === LİSTE KOMUTLARI ===

    # "sayilari sirala"
    eslesme = re.match(r'^(\w+)\s+sirala$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'{degisken} = sırala({degisken})'

    # "sayilari tersle"
    eslesme = re.match(r'^(\w+)\s+tersle$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'{degisken} = list(reversed({degisken}))'

    # "x toplamini bul"
    eslesme = re.match(r'^(\w+)\s+toplamini\s+bul$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'yaz(toplam({degisken}))'

    # "x uzunlugunu bul"
    eslesme = re.match(r'^(\w+)\s+uzunlugunu\s+bul$', temiz)
    if eslesme:
        degisken = eslesme.group(1)
        return f'yaz(uzunluk({degisken}))'

    # === HATA YÖNETİMİ ===

    # "dene ve hata yakala"
    if temiz in ('dene', 'dene ve hata yakala', 'guvenli calistir'):
        return 'dene:'

    # "hata olursa goster"
    if temiz in ('hata olursa goster', 'hata yakala', 'hatayi yakala'):
        return 'hariç Hata:'

    # "bitir" / "son"
    if temiz in ('bitir', 'son', 'kapat', 'tamamla'):
        return 'son'

    # "degilse" / "yoksa"
    if temiz in ('degilse', 'değilse', 'yoksa'):
        return 'değilse:'

    # === GERI KALAN ===
    return orijinal


def _metin_duzenle(metin: str) -> str:
    """Metni düzenler (büyük harf, noktalama vb.)."""
    # İlk harfi büyük yap
    if metin:
        metin = metin[0].upper() + metin[1:]
    return metin


__all__ = ['super_kolay_cevir']
