"""
PARS Kolay Modül
----------------
5 yaşında bir çocuğun bile kullanabileceği ultra basit sözdizimi.

Kurallar:
  - Parantez gerekmez
  - Tırnak gerekmez (otomatik eklenir)
  - İki nokta üst üste gerekmez
  - Girinti yerine 'son' ile blok kapatılır
  - Doğal Türkçe cümle yapısı

Örnekler:
  yaz Merhaba Dünya
  isim = oku Adın ne?
  5 kez tekrarla i
      yaz i
  son
"""

import re
from typing import List


def kolay_cevir(kod: str) -> str:
    """
    Kolay PARS kodunu standart PARS koduna çevirir.

    Args:
        kod: Kolay PARS kaynak kodu

    Returns:
        str: Standart PARS kodu
    """
    satirlar = kod.splitlines()
    sonuc: List[str] = []
    blok_yigini: List[str] = []  # 'dongu', 'kosul', 'fonk', 'sinif'
    girinti = 0

    for satir in satirlar:
        temiz = satir.strip()

        # Boş satır
        if not temiz:
            sonuc.append('')
            continue

        # Yorum
        if temiz.startswith('#'):
            sonuc.append('    ' * girinti + temiz)
            continue

        # 'son' blok kapatıcı
        if temiz == 'son':
            if blok_yigini:
                blok_yigini.pop()
                girinti = max(0, girinti - 1)
            continue

        # 'değilse' / 'degilse'
        if temiz in ('değilse', 'degilse'):
            sonuc.append('    ' * max(0, girinti - 1) + 'değilse:')
            continue

        # 'yoksa ... ise'
        yoksa_eslesme = re.match(r'^yoksa\s+(.+?)\s+ise$', temiz)
        if yoksa_eslesme:
            kosul = _kosul_cevir(yoksa_eslesme.group(1))
            sonuc.append('    ' * max(0, girinti - 1) + f'yoksa {kosul}:')
            continue

        # Döngü: X kez tekrarla [degisken]
        dongu_eslesme = re.match(r'^(\d+)\s+kez\s+tekrarla\s*(\w*)$', temiz)
        if dongu_eslesme:
            sayi = dongu_eslesme.group(1)
            degisken = dongu_eslesme.group(2) or 'i'
            sonuc.append('    ' * girinti + f'için {degisken} içinde aralık({sayi}):')
            blok_yigini.append('dongu')
            girinti += 1
            continue

        # Döngü: her X için
        her_eslesme = re.match(r'^her\s+(\w+)\s+için\s+(.+)$', temiz)
        if her_eslesme:
            degisken = her_eslesme.group(1)
            dizi = her_eslesme.group(2)
            sonuc.append('    ' * girinti + f'için {degisken} içinde {dizi}:')
            blok_yigini.append('dongu')
            girinti += 1
            continue

        # Döngü: her X için
        her_eslesme2 = re.match(r'^her\s+(\w+)\s+icin\s+(.+)$', temiz)
        if her_eslesme2:
            degisken = her_eslesme2.group(1)
            dizi = her_eslesme2.group(2)
            sonuc.append('    ' * girinti + f'için {degisken} içinde {dizi}:')
            blok_yigini.append('dongu')
            girinti += 1
            continue

        # Fonksiyon: ... yap
        fonk_eslesme = re.match(r'^(\w+(?:\s+\w+)*)\s+yap$', temiz)
        if fonk_eslesme:
            parcalar = fonk_eslesme.group(1).split()
            ad = parcalar[0]
            parametreler = ', '.join(parcalar[1:]) if len(parcalar) > 1 else ''
            sonuc.append('    ' * girinti + f'fonksiyon {ad}({parametreler}):')
            blok_yigini.append('fonk')
            girinti += 1
            continue

        # Koşul: eğer ... ise / büyükse / küçükse / eşitse
        kosul_eslesme = re.match(r'^eğer\s+(.+)$', temiz)
        if kosul_eslesme:
            kosul = _kosul_cevir(kosul_eslesme.group(1))
            sonuc.append('    ' * girinti + f'eğer {kosul}:')
            blok_yigini.append('kosul')
            girinti += 1
            continue

        # Koşul: eger ... (ASCII)
        kosul_eslesme2 = re.match(r'^eger\s+(.+)$', temiz)
        if kosul_eslesme2:
            kosul = _kosul_cevir(kosul_eslesme2.group(1))
            sonuc.append('    ' * girinti + f'eger {kosul}:')
            blok_yigini.append('kosul')
            girinti += 1
            continue

        # Atama: X = say oku ... (sayıya çevirerek oku)
        say_oku_eslesme = re.match(r'^(\w+)\s*=\s*say\s+oku\s+(.+)$', temiz)
        if say_oku_eslesme:
            degisken = say_oku_eslesme.group(1)
            mesaj = say_oku_eslesme.group(2).strip()
            sonuc.append('    ' * girinti + f'{degisken} = tam_sayı(girdial("{mesaj}"))')
            continue

        # Atama: X = oku ...
        oku_eslesme = re.match(r'^(\w+)\s*=\s*oku\s+(.+)$', temiz)
        if oku_eslesme:
            degisken = oku_eslesme.group(1)
            mesaj = oku_eslesme.group(2).strip()
            sonuc.append('    ' * girinti + f'{degisken} = girdial("{mesaj}")')
            continue

        # Atama: X = listele ...
        listele_eslesme = re.match(r'^(\w+)\s*=\s*listele\s+(.+)$', temiz)
        if listele_eslesme:
            degisken = listele_eslesme.group(1)
            icerik = listele_eslesme.group(2).strip()
            elemanlar = [f'"{e.strip()}"' for e in icerik.split(',')]
            sonuc.append('    ' * girinti + f'{degisken} = [{", ".join(elemanlar)}]')
            continue

        # Özel komutlar
        ozel = _ozel_komut(temiz, girinti)
        if ozel:
            sonuc.append(ozel)
            continue

        # Diğer (olduğu gibi bırak)
        sonuc.append('    ' * girinti + temiz)

    return '\n'.join(sonuc)


def _kosul_cevir(kosul: str) -> str:
    """Basit koşul ifadesini standart PARS koşuluna çevirir."""
    kosul = kosul.strip()

    # ... ise (ise kelimesini kaldır)
    if kosul.endswith(' ise'):
        kosul = kosul[:-4].strip()

    # X N büyükse → X > N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+büyükse$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} > {eslesme.group(2)}'

    # X N küçükse → X < N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+küçükse$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} < {eslesme.group(2)}'

    # X N eşitse → X == N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+eşitse$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} == {eslesme.group(2)}'

    # X N eşit değilse → X != N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+eşit\s+değilse$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} != {eslesme.group(2)}'

    # X N büyük eşit → X >= N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+büyük\s+eşit$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} >= {eslesme.group(2)}'

    # X N küçük eşit → X <= N
    eslesme = re.match(r'^(.+?)\s+(\S+)\s+küçük\s+eşit$', kosul)
    if eslesme:
        return f'{eslesme.group(1)} <= {eslesme.group(2)}'

    # eşittir operatörü
    kosul = kosul.replace(' eşittir ', ' == ')
    kosul = kosul.replace(' esittir ', ' == ')

    return kosul.strip()


def _ozel_komut(satir: str, girinti: int) -> str:
    """Özel kısa komutları çevirir."""
    on_ek = '    ' * girinti

    # yaz: ... (tüm satırı yazdır)
    if satir.startswith('yaz:'):
        icerik = satir[4:].strip()
        return f'{on_ek}yaz("{icerik}")'

    # yaz ... (basit yazdırma)
    if satir.startswith('yaz '):
        icerik = satir[4:].strip()
        # Eğer zaten parantez içindeyse dokunma
        if icerik.startswith('(') and icerik.endswith(')'):
            return f'{on_ek}yaz{icerik}'
        # Eğer f-string ise
        if icerik.startswith('f"') or icerik.startswith("f'"):
            return f'{on_ek}yaz({icerik})'
        # Eğer değişken adı ise (boşluk yok, tırnak yok)
        if ' ' not in icerik and '"' not in icerik and "'" not in icerik:
            return f'{on_ek}yaz({icerik})'
        # Çok kelimeli metin → tırnak içine al
        return f'{on_ek}yaz("{icerik}")'

    # oku ... (girdi al)
    if satir.startswith('oku '):
        mesaj = satir[4:].strip()
        return f'{on_ek}girdial("{mesaj}")'

    # bekle ... (saniye bekle)
    if satir.startswith('bekle '):
        sure = satir[6:].strip()
        return f'{on_ek}zaman.bekle({sure})'

    # listele ... (liste oluştur)
    if satir.startswith('listele '):
        icerik = satir[8:].strip()
        elemanlar = [f'"{e.strip()}"' for e in icerik.split(',')]
        return f'{on_ek}[{", ".join(elemanlar)}]'

    # say ... (sayıya çevir)
    if satir.startswith('say '):
        icerik = satir[4:].strip()
        return f'{on_ek}tam_sayı({icerik})'

    # ekle ... (listeye ekle)
    if satir.startswith('ekle '):
        parcalar = satir[5:].strip().split(' ', 1)
        if len(parcalar) == 2:
            return f'{on_ek}{parcalar[0]}.append({parcalar[1]})'

    return ''


def kolay_dosya_calistir(dosya_yolu: str) -> str:
    """
    Kolay PARS dosyasını oku ve standart PARS koduna çevir.

    Args:
        dosya_yolu: .kolay uzantılı dosya yolu

    Returns:
        str: Standart PARS kodu
    """
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        kod = f.read()
    return kolay_cevir(kod)


__all__ = ['kolay_cevir', 'kolay_dosya_calistir']
