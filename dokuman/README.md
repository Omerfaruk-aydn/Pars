# PARS — Türkçe Programlama Dili

*"Pars gibi hızlı. Türkçe gibi güzel."*

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir programlama dilidir.

## Kurulum

```bash
pip install pars-turkce-dil
```

## İlk Program

```pars
# merhaba.pars
yaz("Merhaba, Dünya!")

isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

```bash
pars merhaba.pars
```

## Sözdizimi

| PARS | Python |
|---|---|
| `eğer x > 0:` | `if x > 0:` |
| `değilse:` | `else:` |
| `yoksa x == 0:` | `elif x == 0:` |
| `için i içinde aralık(10):` | `for i in range(10):` |
| `iken x < 5:` | `while x < 5:` |
| `fonksiyon topla(a, b):` | `def topla(a, b):` |
| `döndür sonuç` | `return sonuç` |
| `sınıf Araba:` | `class Araba:` |
| `içe_aktar numpy olarak np` | `import numpy as np` |
| `dene: / hariç Hata:` | `try: / except Exception:` |
| `doğru / yanlış / yok` | `True / False / None` |
| `ve / veya / değil` | `and / or / not` |

## CLI Komutları

```bash
pars dosya.pars          # Çalıştır
pars -g                  # Etkileşimli mod (REPL)
pars -cevir dosya.pars   # Python karşılığını göster
pars -p dosya.pars       # Çalıştır + Python kodunu göster
pars -kontrol dosya.pars # Sözdizimi kontrolü
pars -s                  # Versiyon bilgisi
pars paket yükle <paket> # pip install
pars yeni <proje_adı>   # Yeni proje oluştur
```

## Python Kütüphaneleri

PARS, tüm Python kütüphanelerini destekler:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
den_aktar flask içe_aktar Flask

a = np.array([1, 2, 3])
yaz(np.mean(a))
```

## Standart Kütüphane

| Modül | Açıklama |
|---|---|
| `matematik` | math kütüphanesi Türkçe sarmalayıcısı |
| `metin` | str işlemleri Türkçe sarmalayıcısı |
| `liste` | list/dict/set yardımcıları |
| `dosya` | pathlib + os Türkçe sarmalayıcısı |
| `zaman` | datetime Türkçe sarmalayıcısı |
| `sistem` | os/sys/platform Türkçe sarmalayıcısı |
| `rastgele` | random/secrets Türkçe sarmalayıcısı |
| `veri` | json/csv/pickle Türkçe sarmalayıcısı |
| `ag` | urllib Türkçe sarmalayıcısı |
| `veritabani` | sqlite3 Türkçe sarmalayıcısı |

## Örnekler

```bash
pars ornekler/01_merhaba_dunya.pars
pars ornekler/06_siniflar_ve_oop.pars
pars ornekler/15_async_await.pars
pars ornekler/20_tam_proje_ornegi.pars
```

## Geliştirme

```bash
git clone https://github.com/pars-lang/pars.git
cd pars
pip install -e ".[dev]"
pytest testler/
```

## Lisans

MIT — Özgürce kullanın, değiştirin, dağıtın.
