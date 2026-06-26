# Sözdizimi Rehberi

## Değişkenler

```pars
# Basit atama
isim = "Ahmet"
yaş = 25
boy = 1.75
öğrenci_mi = doğru

# Türkçe değişken isimleri
şehir = "İstanbul"
öğrenci_adı = "Ayşe"
dosya_yolu = "/tmp/test.txt"
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

## Döngüler

```pars
# for döngüsü
için i içinde aralık(10):
    yaz(i)

# while döngüsü
iken x > 0:
    yaz(x)
    x -= 1

# Liste üzerinde
için meyve içinde ["elma", "armut", "muz"]:
    yaz(meyve)
```

## Fonksiyonlar

```pars
# Basit fonksiyon
fonksiyon selamla(isim: str) -> str:
    döndür f"Merhaba, {isim}!"

# Varsayılan parametre
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
# Basit sınıf
 sınıf Araba:
    fonksiyon __init__(öz, marka: str, yıl: int):
        öz.marka = marka
        öz.yıl = yıl

    fonksiyon bilgi(öz) -> str:
        döndür f"{öz.marka} ({öz.yıl})"

# Kalıtım
 sınıf ElektrikliAraba(Araba):
    fonksiyon __init__(öz, marka: str, yıl: int, batarya: int):
        süper().__init__(marka, yıl)
        öz.batarya = batarya
```

## İstisna Yönetimi

```pars
# try-except-finally
dene:
    sonuç = 10 / 0
hariç SıfıraBölmeHatası:
    yaz("Sıfıra bölme!")
sonunda:
    yaz("İşlem tamamlandı")

# Özel istisna
 sınıf GeçersizHata(Hata):
    pass

yükselt GeçersizHata("Geçersiz değer")
```

## Modüller

```pars
# Standart kütüphane
içe_aktar os
içe_aktar json

# Üçüncü parti
içe_aktar numpy olarak np
den_aktar flask içe_aktar Flask

# PARS modülleri
içe_aktar matematik
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
ile açık("dosya.txt", "w") as f:
    f.write("Merhaba PARS!")
```

## Lambda

```pars
kare = lambda x: x ** 2
toplam = lambda x, y: x + y

# Yüksek dereceli fonksiyonlar
sayılar = [1, 2, 3, 4, 5]
kareler = liste(harita(lambda x: x**2, sayılar))
```
