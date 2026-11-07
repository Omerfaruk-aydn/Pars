# Sözdizimi Rehberi

## Değişkenler

```pars
isim = "Ahmet"
yaş = 25
boy = 1.75
öğrenci_mi = doğru

şehir = "İstanbul"
öğrenci_adı = "Ayşe"
```

## Koşullar

```pars
# if-elif-else
eğer yaş >= 18:
    yaz("Yetişkin")
yoksa yaş >= 13:
    yaz("Genç")
değilse:
    yaz("Çocuk")

# İç içe koşullar
eğer şehir == "İstanbul" ve yaş >= 18:
    yaz("İstanbul'da yetişkin")
```

## Üçlü (ternary) koşul

```pars
durum = "çift" eğer sayı % 2 == 0 değilse "tek"
etiket = "pozitif" eğer x > 0 değilse "negatif"
```

## Döngüler

```pars
için i içinde aralık(10):
    yaz(i)

iken x > 0:
    yaz(x)
    x -= 1

için meyve içinde ["elma", "armut", "muz"]:
    yaz(meyve)

# Liste kavrayışı
kareler = [x ** 2 için x içinde aralık(1, 6)]
çiftler = [x için x içinde aralık(20) eğer x % 2 == 0]
```

## Fonksiyonlar

```pars
fonksiyon selamla(isim: str) -> str:
    döndür f"Merhaba, {isim}!"

fonksiyon topla(a: int, b: int = 0) -> int:
    döndür a + b

# *args ve **kwargs
fonksiyon hepsini_yaz(*args, **kwargs):
    için arg içinde args:
        yaz(arg)
    için k, v içinde kwargs.items():
        yaz(f"{k}: {v}")
```

## Sınıflar

```pars
sınıf Araba:
    fonksiyon __init__(öz, marka: str, yıl: int):
        öz.marka = marka
        öz.yıl = yıl

    fonksiyon bilgi(öz) -> str:
        döndür f"{öz.marka} ({öz.yıl})"

# Kalıtım — süper() doğrudan super()'a çevrilir
sınıf ElektrikliAraba(Araba):
    fonksiyon __init__(öz, marka: str, yıl: int, batarya: int):
        süper().__init__(marka, yıl)
        öz.batarya = batarya
```

`öz` Python'daki `self` yerine kullanılır; sıradan bir parametre adıdır.

## İstisna Yönetimi

```pars
dene:
    sonuç = 10 / 0
hariç SıfıraBölmeHatası:
    yaz("Sıfıra bölme!")
sonunda:
    yaz("İşlem tamamlandı")

dene:
    dosya.oku("yok.txt")
hariç DosyaBulunamadı olarak e:
    yaz(f"Dosya yok: {e}")
```

## Modüller

```pars
içe_aktar os
içe_aktar json

içe_aktar numpy olarak np
den_aktar flask içe_aktar Flask

# PARS standart kütüphanesi
içe_aktar matematik
içe_aktar koleksiyonlar
yaz(matematik.PI)
```

## Async/Await

```pars
içe_aktar asyncio

eşzamansız fonksiyon veri_getir(url: str) -> str:
    bekle asyncio.sleep(1)
    döndür f"Veri: {url}"

eşzamansız fonksiyon ana():
    sonuç = bekle veri_getir("https://api.ornek.com")
    yaz(sonuç)

asyncio.run(ana())
```

## Context Manager

```pars
ile açık("dosya.txt", "w") olarak f:
    f.write("Merhaba PARS!")

# Async context manager
eşzamansız ile Kaynak() olarak k:
    bekle k.kullan()
```

## Üreteçler

```pars
fonksiyon sayıcı(n):
    için i içinde aralık(n):
        ver i

fonksiyon düzleştir(liste):
    için eleman içinde liste:
        eğer türünden_mi(eleman, list):
            ver from düzleştir(eleman)
        değilse:
            ver eleman
```

## Lambda

```pars
kare = lambda x: x ** 2
toplam = lambda x, y: x + y

sayılar = [1, 2, 3, 4, 5]
kareler = liste(harita(lambda x: x ** 2, sayılar))
```

## Ayrılmış sözcükler

Aşağıdaki sözcükler anahtar kelimedir; değişken, parametre veya sınıf üyesi
adı olarak kullanılamaz:

`eğer`, `değilse`, `yoksa`, `iken`, `için`, `içinde`, `fonksiyon`,
`döndür`, `sınıf`, `ver`, `içe_aktar`, `den_aktar`, `olarak`, `dene`,
`hariç`, `sonunda`, `yükselt`, `ile`, `geç`, `kes`, `devam`, `sil`,
`iddia`, `global`, `yerel_değil`, `eşzamansız`, `bekle`, `ve`, `veya`,
`değil`, `doğru`, `yanlış`, `yok`, `süper`.

Noktadan sonra gelen adlar çevrilmez: `dosya.sil` güvenlidir.
ASCII alternatifleri de geçerlidir (`eger`, `degilse`, `icin`, ...).

## Hata mesajları

```pars
yaz(tanımsız)   # Ad Hatası + ipucu
```

PARS, Python hatalarını Türkçe adlarıyla, hatalı satırı ve akıllı ipucunu
gösterir.
