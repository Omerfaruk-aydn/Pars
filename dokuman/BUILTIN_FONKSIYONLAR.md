# Yerleşik Fonksiyonlar

PARS, Python'un yerleşik fonksiyonlarını Türkçe karşılıklarıyla sunar.

## Giriş / Çıkış

| PARS | Python | Açıklama |
|---|---|---|
| `yaz(...)` | `print(...)` | Ekrana yazdır |
| `girdial(...)` | `input()` | Kullanıcıdan giriş al |
| `açık(...)` | `open()` | Dosya aç |

## Tip Dönüşümü

| PARS | Python | Açıklama |
|---|---|---|
| `tam_sayı(x)` | `int(x)` | Tamsayıya çevir |
| `ondalıklı(x)` | `float(x)` | Ondalıklıya çevir |
| `yazıya_çevir(x)` | `str(x)` | Yazıya çevir |
| `mantıksal(x)` | `bool(x)` | Boolean'a çevir |
| `karmaşık(x)` | `complex(x)` | Karmaşık sayıya çevir |

## Veri Yapıları

| PARS | Python | Açıklama |
|---|---|---|
| `liste()` | `list()` | Liste oluştur |
| `demet()` | `tuple()` | Demet oluştur |
| `küme()` | `set()` | Küme oluştur |
| `sözlük()` | `dict()` | Sözlük oluştur |

## İterasyon

| PARS | Python | Açıklama |
|---|---|---|
| `aralık(n)` | `range(n)` | Sayı aralığı |
| `numaralandır(l)` | `enumerate(l)` | İndeksli iterasyon |
| `sıkıştır(a, b)` | `zip(a, b)` | Paralel iterasyon |
| `harita(f, l)` | `map(f, l)` | Fonksiyon uygula |
| `filtre(f, l)` | `filter(f, l)` | Eleman filtrele |
| `sırala(l)` | `sorted(l)` | Sıralı kopya |
| `tersine(l)` | `reversed(l)` | Ters çevrilmiş |

## Matematik

| PARS | Python | Açıklama |
|---|---|---|
| `mutlak(x)` | `abs(x)` | Mutlak değer |
| `yuvarlak(x)` | `round(x)` | Yuvarla |
| `toplam(l)` | `sum(l)` | Toplam |
| `maksimum(l)` | `max(l)` | En büyük |
| `minimum(l)` | `min(l)` | En küçük |
| `güç(a, b)` | `pow(a, b)` | Üs alma |

## Metin / Dizi

| PARS | Python | Açıklama |
|---|---|---|
| `uzunluk(x)` | `len(x)` | Uzunluk |
| `karakter(n)` | `chr(n)` | Karakter |
| `karakter_kodu(c)` | `ord(c)` | Karakter kodu |
| `onaltılık(n)` | `hex(n)` | Onaltılık |
| `sekizlik(n)` | `oct(n)` | Sekizlik |
| `ikili(n)` | `bin(n)` | İkili |

## İnceleyiciler

| PARS | Python | Açıklama |
|---|---|---|
| `tip(x)` | `type(x)` | Veri tipi |
| `kimlik(x)` | `id(x)` | Kimlik |
| `dir(x)` | `dir(x)` | Özellikler |
| `yardım(x)` | `help(x)` | Yardım |
| `özellikler(x)` | `vars(x)` | Özellikler |
| `türünden_mi(x, t)` | `isinstance(x, t)` | Tür kontrolü |
| `çağrılabilir_mi(f)` | `callable(f)` | Çağrılabilir mi? |

## Nesne Yönelimli

| PARS | Python | Açıklama |
|---|---|---|
| `nesne()` | `object()` | Temel nesne |
| `süper()` | `super()` | Üst sınıf |
| `özellik()` | `property()` | Özellik |
| `statik_metot()` | `staticmethod()` | Statik metot |
| `sınıf_metot()` | `classmethod()` | Sınıf metot |

## Sistem

| PARS | Python | Açıklama |
|---|---|---|
| `çıkış()` | `exit()` | Çıkış |
| `değerlendir(x)` | `eval(x)` | Değerlendir |
| `çalıştır(x)` | `exec(x)` | Çalıştır |
| `derle(x)` | `compile(x)` | Derle |

## Paket Yönetimi

| PARS | Açıklama |
|---|---|
| `paket_yükle(...)` | pip install |
| `paket_listele()` | pip list |
