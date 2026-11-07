# Örnekler

PARS ile yazılmış 31 örnek program (`ornekler/*.pars`) ve 10 çocuk örneği
(`ornekler/cocuklar/*.kolay`).

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

durum = "çift" eğer yaş % 2 == 0 değilse "tek"
```

## 04 — Döngüler

```pars
için i içinde aralık(10):
    yaz(i)
```

## 05 — Fonksiyonlar ve Lambda

```pars
fonksiyon topla(a, b):
    döndür a + b

kare = lambda x: x ** 2
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
ile açık("test.txt", "w") olarak f:
    f.write("Merhaba PARS!")
```

## 10 — Modüller

```pars
içe_aktar os
içe_aktar json
içe_aktar matematik
```

## 11 — Liste, Sözlük, Küme

```pars
meyveler = ["elma", "armut", "muz"]
kişi = {"ad": "Ahmet", "yaş": 25}
renkler = küme(["kırmızı", "mavi", "yeşil"])
```

## 12 — Üreteçler ve İteratörler

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
        başlangıç = zaman.sure_olc()
        sonuç = f(*args)
        yaz(f"Süre: {zaman.sure_olc() - başlangıç}s")
        döndür sonuç
    döndür sarmalayıcı
```

## 14 — Context Manager

```pars
ile açık("dosya.txt", "w") olarak f:
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

Kütüphane yönetim sistemi — `ornekler/20_tam_proje_ornegi.pars`

## 21 — Koleksiyonlar

`Sayac`, `CiftUclu`, `AdliDemet`, `ZincirSozluk`, `VarsayilanSozluk`.

## 22 — Yinelenebilirler

Kombinasyon, permütasyon, zincirleme, birikimli toplam, gruplama.

## 23 — Fonksiyonel Programlama

`kismi`, `azalt`, `onbellek`, `boru`, `karsilastirici`.

## 24 — İşletim Sistemi ve Süreç

Dosya sistemi, ortam değişkenleri, geçici dosya, alt süreç.

## 25 — İplikler ve Havuz

`Iplik`, `Kilit`, `Kuyruk`, `Havuz`, `Olay`, `paralel_calistir`.

## 26 — Günlük ve Şifreleme

`gunluk`, hash/HMAC, Base64, güvenli rastgele değerler.

## 27 — Sıkıştırma ve Arşivleme

Gzip, zlib, ZIP ve TAR oluşturma/çıkarma.

## 28 — Sayı ve İstatistik

Decimal/Fraction ile kesin hesap; ortalama, medyan, korelasyon.

## 29 — Takvim ve Zaman

Türkçe tarih, ay takvimi, artık yıl, iş günü hesabı.

## 30 — Argüman ve Test

`ArgumanAyristirici`, veri sınıfları ve `deneme` ile birim testleri.

## Çalıştırma

```bash
pars ornekler/21_koleksiyonlar.pars
pars ornekler/25_iplik_havuz.pars
pars ornekler/30_arguman_test.pars
```

Ağ erişimi gerektiren 19. örnek varsayılan olarak atlanır:

```bash
PARS_ORNEK_AG=1 pars ornekler/19_api_istekleri.pars
```
