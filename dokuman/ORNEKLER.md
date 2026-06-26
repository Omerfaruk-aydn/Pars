# Örnekler

PARS ile yazılmış 20 örnek program.

## 01 — Merhaba Dünya

```pars
yaz("Merhaba, Dünya!")
isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

## 02 — Değişkenler ve Tipler

```pars
yaş = 25
boy = 1.75
ad = "Ahmet"
öğrenci_mi = doğru
yaz(f"{ad}, {yaş} yaşında, {boy}m")
```

## 03 — Koşul İfadeleri

```pars
eğer yaş >= 18:
    yaz("Yetişkin")
yoksa yaş >= 13:
    yaz("Genç")
değilse:
    yaz("Çocuk")
```

## 04 — Döngüler

```pars
için i içinde aralık(10):
    yaz(i)
```

## 05 — Fonksiyonlar

```pars
fonksiyon topla(a, b):
    döndür a + b

yaz(topla(3, 4))  # 7
```

## 06 — Sınıflar ve OOP

```pars
 sınıf Araba:
    fonksiyon __init__(öz, marka):
        öz.marka = marka

    fonksiyon bilgi(öz):
        döndür f"Araba: {öz.marka}"
```

## 07 — Miras

```pars
 sınıf ElektrikliAraba(Araba):
    fonksiyon __init__(öz, marka, batarya):
        süper().__init__(marka)
        öz.batarya = batarya
```

## 08 — İstisna Yönetimi

```pars
dene:
    1/0
hariç SıfıraBölmeHatası:
    yaz("Sıfıra bölme!")
```

## 09 — Dosya İşleme

```pars
ile açık("test.txt", "w") as f:
    f.write("Merhaba PARS!")
```

## 10 — Modüller

```pars
içe_aktar os
içe_aktar json
```

## 11 — Liste, Sözlük, Küme

```pars
meyveler = ["elma", "armut", "muz"]
kişi = {"ad": "Ahmet", "yaş": 25}
renkler = küme(["kırmızı", "mavi", "yeşil"])
```

## 12 — Üreteçler

```pars
fonksiyon fibonacci(n):
    a, b = 0, 1
    için _ içinde aralık(n):
        ver a
        a, b = b, a + b
```

## 13 — Dekoratörler

```pars
fonksiyon zamanlayıcı(f):
    fonksiyon sarmalayıcı(*args):
        içe_aktar zaman
        başlangıç = zaman.time()
        sonuç = f(*args)
        yaz(f"Süre: {zaman.time() - başlangıç}s")
        döndür sonuç
    döndür sarmalayıcı
```

## 14 — Context Manager

```pars
ile açık("dosya.txt", "w") as f:
    f.write("Merhaba!")
```

## 15 — Async/Await

```pars
eşzamansız fonksiyon veri_getir(url):
    bekle asyncio.sleep(1)
    döndür "Veri"
```

## 16 — NumPy ve Pandas

```pars
içe_aktar numpy olarak np
a = np.array([1, 2, 3])
yaz(np.mean(a))
```

## 17 — Flask Web Uygulaması

```pars
den_aktar flask içe_aktar Flask
uygulama = Flask(__name__)
```

## 18 — SQLite Veritabanı

```pars
içe_aktar sqlite3
baglanti = sqlite3.connect(":memory:")
```

## 19 — API İstekleri

```pars
içe_aktar urllib.request
içe_aktar json
yanit = urllib.request.urlopen("https://api.ornek.com")
```

## 20 — Tam Proje

Kütüphane yönetim sistemi — `ornekler/20_tam_proje_ornegi.prs`
