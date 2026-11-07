<div align="center">

# PARS

**Türkçe Programlama Dili**

*"Pars gibi hızlı. Türkçe gibi güzel."*

[![PyPI](https://img.shields.io/pypi/v/pars-turkce-dil.svg)](https://pypi.org/project/pars-turkce-dil/)
[![Python](https://img.shields.io/pypi/pyversions/pars-turkce-dil.svg)](https://pypi.org/project/pars-turkce-dil/)
[![Lisans](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)

</div>

## PARS nedir?

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir
programlama dilidir. Python'un tüm gücünü Türkçe ile yazabilirsiniz.

Sürüm **1.0.1** ile birlikte çekirdek hatalar giderildi, standart
kütüphane 10 modülden 28 modüle çıkarıldı ve `pip`/`python` yerine
kendi komutları (`parskur`/`parspip`, `parspy`) eklendi. PARS kaynak
uzantısı artık **`.pars`** (eski `.prs` uyumlu). Python kütüphanelerini
Türkçe sözdizimine uyarlayan bir **köprü** sistemi de eklendi.

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

## Komutlar

PARS artık Python araçlarını kendi adlarıyla sunar:

| PARS komutu | Karşılığı | Açıklama |
|---|---|---|
| `pars dosya.pars` | `python dosya.py` | PARS dosyasını çalıştırır |
| `pars -g` | `python` | Etkileşimli PARS konsolu |
| `parskur yükle paket` | `pip install paket` | Paket yükler |
| `parspip yükle paket` | `pip install paket` | `parskur` ile aynı |
| `parskur kaldır paket` | `pip uninstall paket` | Paket kaldırır |
| `parskur listele` | `pip list` | Yüklü paketleri listeler |
| `parskur dışa` | `pip freeze` | Bağımlılıkları dışa aktarır |
| `pars köprü modül` | — | Python kütüphanesini PARS'a uyarlar |
| `parspy dosya.py` | `python dosya.py` | Python dosyasını çalıştırır |
| `parspy -c "kod"` | `python -c "kod"` | Python kodu çalıştırır |
| `parspy -m modül` | `python -m modül` | Python modülü çalıştırır |

Ek PARS komutları:

```bash
pars -cevir dosya.pars     # Python karşılığını göster
pars -kontrol dosya.pars   # Sözdizimi kontrolü
pars -p dosya.pars         # Çalıştır + üretilen Python'u göster
pars derle dosya.pars      # .py dosyasına derle
pars yeni projem          # Yeni proje iskeleti
pars çalıştır <komut>     # Sistem komutu (kabuk yok)
pars köprü requests       # Python kütüphanesini PARS'a uyarla
pars köprü dışa requests -o istek_kopru.pars
```

## Köprü: Python kütüphanelerini Türkçe kullanma

```pars
içe_aktar köprü

istek = köprü.bagla("requests")
yanit = istek.al("https://api.ornek.com")
yaz(yanit.durum_kodu)          # status_code
yaz(yanit.icerik)              # content
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
| `süper().__init__()` | `super().__init__()` |
| `içe_aktar numpy olarak np` | `import numpy as np` |
| `dene: / hariç Hata:` | `try: / except Exception:` |
| `doğru / yanlış / yok` | `True / False / None` |
| `ve / veya / değil` | `and / or / not` |
| `"çift" eğer x % 2 == 0 değilse "tek"` | `"çift" if x % 2 == 0 else "tek"` |

> **Not:** `sınıf`, `fonksiyon`, `sil`, `döndür` gibi kelimeler ayrılmış
> sözcüklerdir; değişken/parametre adı olarak kullanılamaz.
> Noktadan sonra gelen adlar (`dosya.sil`) çevrilmez.

## Python Kütüphaneleri

PARS, tüm Python kütüphanelerini destekler:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
den_aktar flask içe_aktar Flask

a = np.array([1, 2, 3])
yaz(np.mean(a))
```

Kurulum: `parskur yükle numpy pandas flask`

## Standart Kütüphane (28 modül)

| Modül | Açıklama |
|---|---|
| `matematik` | Matematik, trigonometri, logaritma, asallık |
| `istatistik` | Ortalama, medyan, varyans, korelasyon, regresyon |
| `metin` | Metin işlemleri, regex, slug, HTML, benzerlik |
| `liste` | Liste/sözlük/küme yardımcıları, pencereler |
| `koleksiyonlar` | Counter, deque, namedtuple, ChainMap |
| `yinelenebilirler` | itertools: kombinasyon, permütasyon, zincir |
| `fonksiyonel` | partial, reduce, lru_cache, pipe |
| `dosya` | Dosya G/Ç, JSON, CSV |
| `yol` | pathlib: yol nesneleri ve dosya işlemleri |
| `zaman` | Tarih/saat, biçimlendirme, süre ölçümü |
| `takvim` | Takvim, artık yıl, ay takvimi, gün adları |
| `sistem` | OS/sys/platform bilgileri |
| `isletim` / `işletim` | os: dizin, ortam, dosya gezinme |
| `surec` / `süreç` | subprocess: güvenli komut çalıştırma |
| `iplik` | threading, kuyruk, thread/process havuzu |
| `gunluk` / `günlük` | logging: seviyeli günlük sistemi |
| `rastgele` | random/secrets: rastgele üretim |
| `sifreleme` / `şifreleme` | hashlib, hmac, base64, UUID |
| `sikistirma` / `sıkıştırma` | gzip, zlib, zip, tar arşivleri |
| `sayi` / `sayı` | Decimal, Fraction, kesin hesaplama |
| `kopya` | Sığ/derin kopya |
| `veri` | JSON/CSV/pickle/base64 |
| `veri_siniflari` / `veri_sınıfları` | dataclasses |
| `ag` / `ağ` | HTTP GET/POST/PUT/DELETE |
| `veritabani` / `veritabanı` | SQLite |
| `arguman` / `argüman` | argparse |
| `deneme` | unittest |
| `kopru` / `köprü` | Python kütüphanelerini PARS'a uyarlar |

```pars
içe_aktar matematik
içe_aktar koleksiyonlar

yaz(matematik.asal_mi(97))              # doğru
yaz(koleksiyonlar.en_sik("pars gibi pars"))  # pars
```

## Örnekler (31 program)

```bash
pars ornekler/01_merhaba_dunya.pars
pars ornekler/15_async_await.pars
pars ornekler/21_koleksiyonlar.pars
pars ornekler/25_iplik_havuz.pars
pars ornekler/30_arguman_test.pars
```

Ek olarak `ornekler/cocuklar/` altında 10 adet `.kolay` örneği vardır.

## Geliştirme

```bash
git clone https://github.com/pars-lang/pars.git
cd pars
pip install -e ".[dev]"
pytest testler/
flake8 pars/ --max-line-length=100 --ignore=E501,W503
```

## Katkı

Katkı rehberi için [KATKI_REHBERI.md](dokuman/KATKI_REHBERI.md) dosyasına bakın.

## Lisans

MIT — Özgürce kullanın, değiştirin, dağıtın.

---

<div align="center">

**"Pars gibi hızlı. Türkçe gibi güzel."**

</div>
