"""
PARS Etkileşimli Konsol (REPL)
------------------------------
Özellikler:
  - code.compile_command() ile eksik blok tespiti
  - Çok satırlı giriş (fonksiyon, sınıf, döngü)
  - Sonuç değerleri otomatik yazdırılır
  - Türkçe boolean/None gösterimi
  - Standart kütüphane modülleri hazır yüklü
  - Özel REPL komutları
"""

import code
from .ceviri import cevir
from .hatalar import hata_goster
from .yurutucu import ad_alani_olustur, PARS_SURUM

BANNER = f"""
============================================================
    PARS  Turkce Programlama Dili  v{PARS_SURUM}
    "Pars gibi hizli. Turkce gibi guzel."

    Yardim icin: .yardim    Cikmak icin: .cikis
    Standart kutuphane hazir: matematik, metin, liste, dosya,
    zaman, isletim, veri, ag, veritabani ve daha fazlasi.
============================================================
"""

YARDIM = """
+----------------------------+------------------------------------------+
|  PARS - HIZLI BASVURU     |                                          |
+----------------------------+------------------------------------------+
|  eger x > 0:              |  if x > 0:                               |
|  degilse:                 |  else:                                   |
|  yoksa x == 0:            |  elif x == 0:                            |
|  iken x < 10:             |  while x < 10:                           |
|  icin i icinde ...:       |  for i in ...:                           |
|  fonksiyon ad(...):       |  def ad(...)                             |
|  dondur sonuc             |  return sonuc                            |
|  sinif Ad(Ana):           |  class Ad(Ana):                          |
|  ice_aktar numpy ...      |  import numpy ...                        |
|  den_aktar x ice ...      |  from x import ...                       |
|  dene: / haric E:         |  try: / except E:                        |
|  ile f(...) olarak x      |  with f(...) as x:                       |
|  yukselt Hata(...)        |  raise Exception(...)                    |
|  ve / veya / degil        |  and / or / not                          |
|  dogru / yanlis / yok     |  True / False / None                     |
|  esezamansiz / bekle      |  async / await                           |
|  ver sonuc                |  yield sonuc                             |
+----------------------------+------------------------------------------+
|  YERLESIK                 |                                          |
|  yaz(...)                 |  Ekrana yaz                              |
|  girdial(...)             |  Kullanicidan giris al                   |
|  uzunluk(x)               |  Uzunluk                                 |
|  aralik(n)                |  0'dan n-1'e tamsayilar                  |
|  tip(x)                   |  Veri tipini goster                      |
|  tam_sayi(x)              |  Tamsayiya cevir                         |
|  ondalikli(x)             |  Ondalikliya cevir                       |
|  yaziya_cevir(x)          |  Yaziya cevir                            |
|  sirala(liste)            |  Sirali kopya dondur                     |
|  paket_yukle("numpy")     |  parskur yukle numpy                     |
+----------------------------+------------------------------------------+
|  REPL KOMUTLARI           |                                          |
|  .yardim                  |  Bu ekrani goster                        |
|  .cikis                   |  Programi kapat                          |
|  .temiz                   |  Ekrani temizle                          |
|  .python                  |  Son girisin Python karsiligi            |
|  .sozdizimi               |  Son girisin Python karsiligi (alias)    |
|  .degiskenler             |  Tanimli degiskenleri listele            |
|  .gecmis                  |  Komut gecmisini goster                  |
|  .surum                   |  Versiyon bilgisi                        |
+----------------------------+------------------------------------------+
"""


def _goster(deger: object) -> str:
    """Değeri Türkçe formatla."""
    if deger is True:
        return 'doğru'
    if deger is False:
        return 'yanlış'
    if deger is None:
        return 'yok'
    if isinstance(deger, list):
        return '[' + ', '.join(_goster(i) for i in deger) + ']'
    if isinstance(deger, dict):
        return '{' + ', '.join(
            f'{_goster(k)}: {_goster(v)}' for k, v in deger.items()) + '}'
    return repr(deger)


def repl_baslat() -> None:
    """PARS REPL konsolunu başlatır."""
    print(BANNER)

    alan = ad_alani_olustur('<repl>')
    alan['__name__'] = '__console__'

    komut_gecmisi: list = []

    while True:
        try:
            giris = input('>>> ')
        except (EOFError, KeyboardInterrupt):
            print('\nGörüşürüz!')
            break

        if not giris.strip():
            continue

        # Özel REPL komutları
        if giris.strip().startswith('.'):
            komut = giris.strip().lower()
            if komut in ('.cikis', '.çıkış', '.exit', '.quit'):
                print('Görüşürüz!')
                break
            elif komut in ('.yardim', '.yardım', '.help'):
                print(YARDIM)
                continue
            elif komut in ('.temiz', '.clear'):
                print('\033[2J\033[H', end='')
                continue
            elif komut in ('.surum', '.sürüm', '.version'):
                print(f'PARS v{PARS_SURUM}')
                continue
            elif komut in ('.degiskenler', '.değişkenler', '.vars'):
                ozel = {'__name__', '__file__', '__builtins__', '__doc__',
                        'PARS_SURUM'}
                for k, v in sorted(alan.items()):
                    if k not in ozel and not k.startswith('_'):
                        print(f'  {k} = {_goster(v)}')
                continue
            elif komut in ('.gecmis', '.geçmiş', '.history'):
                for i, eski in enumerate(komut_gecmisi, 1):
                    print(f'  {i}: {eski}')
                continue
            elif komut in ('.python', '.sozdizimi', '.sözdizimi'):
                if komut_gecmisi:
                    son = komut_gecmisi[-1]
                    print(cevir(son))
                continue
            else:
                print(f'Bilinmeyen komut: {giris.strip()}')
                continue

        # Çok satırlı blok tespiti
        tam_giris = giris
        while True:
            try:
                code.compile_command(tam_giris, '<repl>', 'exec')
                break
            except SyntaxError:
                if tam_giris.rstrip().endswith(':'):
                    pass
                elif not tam_giris.rstrip().endswith('\\'):
                    break
                try:
                    devam = input('... ')
                except (EOFError, KeyboardInterrupt):
                    print()
                    break
                tam_giris += '\n' + devam

        komut_gecmisi.append(tam_giris)

        # Çevir ve çalıştır
        try:
            python_kodu = cevir(tam_giris)
        except Exception as e:
            print(f'Çevirme hatası: {e}')
            continue

        # ifade olarak değerlendir (sonucu yazdır)
        try:
            derlenmis = compile(python_kodu, '<repl>', 'eval')
            sonuc = eval(derlenmis, alan)
            if sonuc is not None:
                print(_goster(sonuc))
            continue
        except SyntaxError:
            pass
        except Exception as exc:
            hata_goster(exc, tam_giris, '<repl>')
            continue

        # ifade değilse çalıştır
        try:
            derlenmis = compile(python_kodu, '<repl>', 'exec')
            exec(derlenmis, alan)
        except SystemExit:
            break
        except KeyboardInterrupt:
            print('\nDurduruldu.')
        except Exception as exc:
            hata_goster(exc, tam_giris, '<repl>')


__all__ = ['repl_baslat']
