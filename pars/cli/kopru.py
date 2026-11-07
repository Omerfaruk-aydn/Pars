"""
PARS Köprü CLI
--------------
Python kütüphanelerini PARS sözdizimine uyarlayan komutlar.

Kullanım:
  pars köprü <modül>                 → Öznitelikler + Türkçe karşılıklar
  pars köprü ara <modül> <terim>     → Ada göre ara
  pars köprü dışa <modül>            → .pars sarmalayıcı dosyası üret
  pars köprü doğrula <modül>         → Kurulu mu, sürümü ne?
"""

import sys

from pars.cekirdek import kopru as _kopru


def _yaz_ozellikler(modul_adi: str) -> int:
    try:
        liste = _kopru.ozellik_listesi(modul_adi)
    except Exception as hata:
        print(f'Köprü hatası: {hata}', file=sys.stderr)
        return 1
    print(f'# {modul_adi} — {len(liste)} genel öznitelik')
    print(f'# {"İngilizce":<32} Türkçe karşılık')
    print('-' * 60)
    for en in sorted(liste):
        tr = liste[en]
        if tr != en:
            print(f'  {en:<32} {tr}')
        else:
            print(f'  {en}')
    return 0


def _ara(modul_adi: str, terim: str) -> int:
    try:
        liste = _kopru.ozellik_listesi(modul_adi)
    except Exception as hata:
        print(f'Köprü hatası: {hata}', file=sys.stderr)
        return 1
    terim = terim.lower()
    bulunan = {en: tr for en, tr in liste.items()
               if terim in en.lower() or terim in tr.lower()}
    if not bulunan:
        print(f'"{terim}" için eşleşme yok.', file=sys.stderr)
        return 1
    print(f'# "{terim}" için {len(bulunan)} eşleşme')
    for en in sorted(bulunan):
        print(f'  {en:<32} {bulunan[en]}')
    return 0


def _disa(modul_adi: str, hedef: str = None, takma: str = None) -> int:
    try:
        yol = _kopru.disa_aktar(modul_adi, hedef, takma)
    except Exception as hata:
        print(f'Köprü hatası: {hata}', file=sys.stderr)
        return 1
    print(f'Sarmalayıcı üretildi: {yol}')
    print(f'Kullanım: içe_aktar {takma or modul_adi.replace(".", "_")}_kopru')
    return 0


def _dogrula(modul_adi: str) -> int:
    sonuc = _kopru._dogrula(modul_adi)
    if not sonuc['basarili']:
        print(f'Kurulu değil veya içe aktarılamıyor: {sonuc["hata"]}',
              file=sys.stderr)
        return 1
    surum = sonuc.get('surum')
    print(f'{sonuc["ad"]} — sürüm: {surum if surum else "bilinmiyor"}')
    print(f'{sonuc["ozellik_sayisi"]} genel öznitelik')
    return 0


def _yardim() -> str:
    return """
Kullanım:
  pars köprü <modül>                 Öznitelikleri ve Türkçe karşılıkları listele
  pars köprü ara <modül> <terim>     Ada göre ara
  pars köprü dışa <modül> [-o yol]   .pars sarmalayıcı dosyası üret
  pars köprü doğrula <modül>         Modül kurulu mu?

Örnek:
  pars köprü requests
  pars köprü ara requests durum
  pars köprü dışa requests -o istek_kopru.pars
"""


def main(argv=None) -> int:
    argumanlar = list(sys.argv[1:] if argv is None else argv)
    if not argumanlar or argumanlar[0] in ('-h', '--help', '--yardım',
                                           '--yardim'):
        print(_yardim())
        return 0

    alt = argumanlar[0]
    if alt in ('ara', 'search'):
        if len(argumanlar) < 3:
            print('Kullanım: pars köprü ara <modül> <terim>', file=sys.stderr)
            return 1
        return _ara(argumanlar[1], argumanlar[2])

    if alt in ('dışa', 'disa', 'export'):
        if len(argumanlar) < 2:
            print('Kullanım: pars köprü dışa <modül> [-o yol]',
                  file=sys.stderr)
            return 1
        hedef = None
        takma = None
        geri = argumanlar[2:]
        if '-o' in geri:
            i = geri.index('-o')
            if i + 1 < len(geri):
                hedef = geri[i + 1]
        if '--ad' in geri:
            i = geri.index('--ad')
            if i + 1 < len(geri):
                takma = geri[i + 1]
        return _disa(argumanlar[1], hedef, takma)

    if alt in ('doğrula', 'dogrula', 'check'):
        if len(argumanlar) < 2:
            print('Kullanım: pars köprü doğrula <modül>', file=sys.stderr)
            return 1
        return _dogrula(argumanlar[1])

    return _yaz_ozellikler(argumanlar[0])


if __name__ == '__main__':
    sys.exit(main())
