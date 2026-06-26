<div align="center">

# PARS

**Türkçe Programlama Dili**

*"Pars gibi hızlı. Türkçe gibi güzel."*

[![PyPI](https://img.shields.io/pypi/v/pars-dil.svg)](https://pypi.org/project/pars-dil/)
[![Python](https://img.shields.io/pypi/pyversions/pars-dil.svg)](https://pypi.org/project/pars-dil/)
[![Lisans](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)

</div>

## PARS nedir?

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir programlama dilidir.
Python'un tüm gücünü Türkçe ile yazabilirsiniz.

## Kurulum

```bash
pip install pars-dil
```

## İlk Program

```pars
# merhaba.prs
yaz("Merhaba, Dünya!")

isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

```bash
pars merhaba.prs
```

## Sözdizimi Karşılaştırması

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

## Python Kütüphaneleri

PARS, tüm Python kütüphanelerini destekler:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
den_aktar flask içe_aktar Flask

a = np.array([1, 2, 3])
yaz(np.mean(a))
```

## Paket Yönetimi

```bash
pars paket yükle numpy pandas flask
pars paket listele
pars paket kaldır eski-paket
```

## CLI

```bash
pars dosya.prs          # Çalıştır
pars -g                  # Etkileşimli mod
pars -cevir dosya.prs   # Python karşılığını göster
pars -kontrol dosya.prs # Sözdizimi kontrolü
pars yeni projem         # Yeni proje oluştur
```

## Özellikler

- Tamamen Türkçe sözdizimi
- Python 3.8+ uyumluluğu
- Tüm Python kütüphanelerini destekler
- Türkçe hata mesajları
- Etkileşimli REPL konsolu
- VS Code sözdizimi renklendirme
- Standart kütüphane (matematik, metin, dosya, zaman, vb.)
- 20+ örnek program

## Standart Kütüphane

| Modül | Açıklama |
|---|---|
| `matematik` | Matematik fonksiyonları |
| `metin` | Metin işlemleri |
| `liste` | Liste/sözlük yardımcıları |
| `dosya` | Dosya I/O |
| `zaman` | Tarih ve saat |
| `sistem` | Sistem işlemleri |
| `rastgele` | Rastgele sayı üretimi |
| `veri` | JSON/CSV/pickle |
| `ag` | HTTP istekleri |
| `veritabani` | SQLite veritabanı |

## Örnekler

```bash
# Tüm örnekleri çalıştır
pars ornekler/01_merhaba_dunya.prs
pars ornekler/06_siniflar_ve_oop.prs
pars ornekler/15_async_await.prs
pars ornekler/20_tam_proje_ornegi.prs
```

## Geliştirme

```bash
# Depoyu klonla
git clone https://github.com/pars-lang/pars.git
cd pars

# Geliştirme bağımlılıklarını kur
pip install -e ".[dev]"

# Testleri çalıştır
pytest testler/

# Linting
flake8 pars/
mypy pars/
```

## Katkı

Katkı rehberi için [KATKI_REHBERI.md](dokuman/KATKI_REHBERI.md) dosyasına bakın.

## Lisans

MIT — Özgürce kullanın, değiştirin, dağıtın.

---

<div align="center">

**"Pars gibi hızlı. Türkçe gibi güzel."**

</div>
