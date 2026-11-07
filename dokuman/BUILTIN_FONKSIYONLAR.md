# Yerleşik Fonksiyonlar

PARS, Python'un yerleşik fonksiyonlarını Türkçe karşılıklarıyla sunar.
ASCII yazımlar da geçerlidir (örn. `tam_sayi`).

## Giriş / Çıkış

| PARS | Python | Açıklama |
|---|---|---|
| `yaz(...)` | `print(...)` | Ekrana yazdır |
| `girdial(...)` / `oku(...)` | `input()` | Kullanıcıdan giriş al |
| `açık(...)` | `open()` | Dosya aç |

`yaz` Türkçe değer gösterir: `doğru`, `yanlış`, `yok`.
`yaz("a", "b", ayraç="-")` Türkçe parametre kabul eder.

## Tip Dönüşümü

| PARS | Python |
|---|---|
| `tam_sayı(x)` | `int(x)` |
| `ondalıklı(x)` | `float(x)` |
| `yazıya_çevir(x)` | `str(x)` |
| `mantıksal(x)` | `bool(x)` |
| `karmaşık(x)` | `complex(x)` |
| `bayt(x)` | `bytes(x)` |
| `bayt_dizisi(x)` | `bytearray(x)` |

## Veri Yapıları

| PARS | Python |
|---|---|
| `liste()` | `list()` |
| `demet()` | `tuple()` |
| `küme()` | `set()` |
| `sözlük()` | `dict()` |
| `dondurulmuş_küme()` | `frozenset()` |

## İterasyon

| PARS | Python |
|---|---|
| `aralık(n)` | `range(n)` |
| `numaralandır(l)` | `enumerate(l)` |
| `sıkıştır(a, b)` | `zip(a, b)` |
| `harita(f, l)` | `map(f, l)` |
| `filtre(f, l)` | `filter(f, l)` |
| `sırala(l)` | `sorted(l)` |
| `tersine(l)` | `reversed(l)` |
| `tümü(l)` | `all(l)` |
| `herhangi(l)` | `any(l)` |
| `sonraki(it)` | `next(it)` |
| `iter_et(x)` | `iter(x)` |
| `dilimle(...)` | `slice(...)` |

## Matematik

| PARS | Python |
|---|---|
| `mutlak(x)` | `abs(x)` |
| `yuvarlak(x)` | `round(x)` |
| `toplam(l)` | `sum(l)` |
| `maksimum(l)` | `max(l)` |
| `minimum(l)` | `min(l)` |
| `güç(a, b)` | `pow(a, b)` |

## Metin / Dizi

| PARS | Python |
|---|---|
| `uzunluk(x)` | `len(x)` |
| `karakter(n)` | `chr(n)` |
| `karakter_kodu(c)` | `ord(c)` |
| `onaltılık(n)` | `hex(n)` |
| `sekizlik(n)` | `oct(n)` |
| `ikili(n)` | `bin(n)` |
| `biçimle(...)` | `format(...)` |
| `yazdır(x)` | `repr(x)` |

## İnceleyiciler

| PARS | Python |
|---|---|
| `tip(x)` | `type(x)` |
| `kimlik(x)` | `id(x)` |
| `dir(x)` | `dir(x)` |
| `yardım(x)` | `help(x)` |
| `özellikler(x)` | `vars(x)` |
| `nitelik_al(...)` | `getattr(...)` |
| `nitelik_ata(...)` | `setattr(...)` |
| `nitelik_sil(...)` | `delattr(...)` |
| `nitelik_var_mı(...)` | `hasattr(...)` |
| `türünden_mi(x, t)` | `isinstance(x, t)` |
| `alt_sınıfı_mı(...)` | `issubclass(...)` |
| `çağrılabilir_mi(f)` | `callable(f)` |

> Not: v1.0.1 öncesinde `dir` yanlışlıkla `is` anahtar kelimesine
> çevriliyordu. Artık `dir(x)` beklendiği gibi çalışır.

## Nesne Yönelimli

| PARS | Python |
|---|---|
| `nesne()` | `object()` |
| `süper()` | `super()` |
| `özellik()` | `property()` |
| `statik_metot()` | `staticmethod()` |
| `sınıf_metot()` | `classmethod()` |

`süper()` doğrudan `super()`'a çevrilir; sıfır argümanlı kullanım
(`süper().__init__()`) kalıtımda doğru çalışır.

## Sistem

| PARS | Python |
|---|---|
| `çıkış()` | `exit()` |
| `değerlendir(x)` | `eval(x)` |
| `çalıştır_kod(x)` | `exec(x)` |
| `derle(...)` | `compile(...)` |
| `modül_yükle(...)` | `__import__(...)` |
| `modül_al(ad)` | `importlib.import_module(ad)` |

## Paket Yönetimi

| PARS | Açıklama |
|---|---|
| `paket_yükle("numpy")` | `parskur yükle numpy` |
| `paket_listele()` | `parskur listele` |

Komut satırında `pip` yerine `parskur`, `python` yerine `parspy` kullanın.
