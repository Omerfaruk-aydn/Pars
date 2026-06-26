# Standart Kütüphane

PARS standart kütüphanesi, Python modüllerini Türkçe sarmalayıcılarla sunar.

## matematik

```pars
içe_aktar matematik

yaz(matematik.PI)           # 3.14159...
yaz(matematik.kare_kok(16)) # 4.0
yaz(matematik.faktoriyel(5)) # 120
yaz(matematik.ortalama([1,2,3,4,5])) # 3.0
```

### Fonksiyonlar
- `kare_kok(x)` — Karekök
- `us(taban, üst)` — Üs alma
- `mutlak(x)` — Mutlak değer
- `yuvarlak(x, basamak)` — Yuvarlama
- `tavan(x)` — Yukarı yuvarla
- `taban_al(x)` — Aşağı yuvarla
- `sinus(x)`, `kosinus(x)`, `tanjant(x)` — Trigonometri
- `logaritma(x)` — Logaritma
- `faktoriyel(n)` — Faktöriyel
- `kombinasyon(n, k)` — Kombinasyon
- `ortalama(sayilar)` — Aritmetik ortalama
- `medyan(sayilar)` — Medyan
- `standart_sapma(sayilar)` — Standart sapma

## metin

```pars
içe_aktar metin

yaz(metin.buyuk_harf("merhaba"))  # "MERHABA"
yaz(metin.bol("a,b,c", ","))      # ['a', 'b', 'c']
yaz(metin.iceriyor_mu("test", "es")) # doğru
```

### Fonksiyonlar
- `buyuk_harf(s)` — Büyük harfe çevir
- `kucuk_harf(s)` — Küçük harfe çevir
- `bas_buyuk(s)` — İlk harfi büyük yap
- `bol(s, ayraç)` — Ayıraç ile böl
- `birlestir(ayraç, liste)` — Ayraç ile birleştir
- `degistir(s, eski, yeni)` — Alt dizgi değiştir
- `bul(s, aranan)` — Alt dizgi bul
- `say(s, aranan)` — Tekrar sayısını say

## liste

```pars
içe_aktar liste

yaz(liste.tekil([1,2,2,3,3,3]))  # [1, 2, 3]
yaz(liste.grupla([1,2,3,4,5], 2)) # [[1,2], [3,4], [5]]
yaz(liste.duzlestir([[1,2],[3,4]])) # [1, 2, 3, 4]
```

### Fonksiyonlar
- `duzlestir(liste)` — İç içe listeyi düzleştir
- `tekil(liste)` — Benzersiz elemanlar
- `grupla(liste, n)` — N'li gruplara böl
- `filtrele(fonk, liste)` — Filtrele
- `haritala(fonk, liste)` — Fonksiyon uygula
- `anahtarlar(sozluk)` — Sözlük anahtarları
- `degerler(sozluk)` — Sözlük değerleri

## dosya

```pars
içe_aktar dosya

dosya.yaz("test.txt", "merhaba")
yaz(dosya.oku("test.txt"))
yaz(dosya.var_mi("test.txt"))  # doğru
```

### Fonksiyonlar
- `oku(yol)` — Dosyayı oku
- `yaz(yol, icerik)` — Dosyaya yaz
- `ekle(yol, icerik)` — Dosyaya ekle
- `var_mi(yol)` — Dosya var mı?
- `klasor_mu(yol)` — Klasör mü?
- `sil(yol)` — Dosyayı sil
- `listele(yol, desen)` — Dosyaları listele

## zaman

```pars
içe_aktar zaman

yaz(zaman.simdi())
yaz(zaman.bugun())
yaz(zaman.bicimle(zaman.simdi(), "%d.%m.%Y"))
```

### Fonksiyonlar
- `simdi()` — Şu anki tarih ve saat
- `bugun()` — Bugünün tarihi
- `bicimle(tarih, sablon)` — Tarihi biçimlendir
- `cozmle(metin, sablon)` — Metni tarihe çevir
- `gun_adi(tarih)` — Günün Türkçe adı
- `ay_adi(tarih)` — Ayın Türkçe adı

## sistem

```pars
içe_aktar sistem

yaz(sistem.calisma_dizini())
yaz(sistem.isletim_sistemi())
yaz(sistem.kullanici_adi())
```

### Fonksiyonlar
- `calisma_dizini()` — Çalışma dizini
- `isletim_sistemi()` — İşletim sistemi
- `kullanici_adi()` — Kullanıcı adı
- `cpu_sayisi()` — CPU sayısı
- `python_surumu()` — Python versiyonu

## rastgele

```pars
içe_aktar rastgele

yaz(rastgele.rastgele_sayi(1, 100))
yaz(rastgele.rastgele_sec(["elma", "armut", "muz"]))
```

### Fonksiyonlar
- `rastgele_sayi(bas, son)` — Rastgele tamsayı
- `rastgele_ondalikli()` — Rastgele ondalıklı
- `rastgele_sec(liste)` — Rastgele seçim
- `rastgele_karistir(liste)` — Karıştır
- `rastgele_metin(uzunluk)` — Rastgele metin

## veri

```pars
içe_aktar veri

json_metin = veri.json_metin({"ad": "Ahmet"}, doğruluk=doğru)
yaz(json_metin)
```

### Fonksiyonlar
- `json_metin(veri)` — JSON metnine çevir
- `json_cozumle(metin)` — JSON metnini çözümle
- `json_oku(yol)` — JSON dosyasını oku
- `csv_oku(yol)` — CSV dosyasını oku
- `hash_hesapla(metin)` — Hash hesapla

## ag

```pars
içe_aktar ag

yanit = ag.get("https://api.ornek.com")
yaz(yanit['govde'])
```

### Fonksiyonlar
- `get(url)` — HTTP GET
- `post(url, veri)` — HTTP POST
- `dosya_indir(url, yol)` — Dosya indir
- `json_al(url)` — JSON al

## veritabani

```pars
içe_aktar veritabani

vt = veritabani.Veritabani("veriler.db")
vt.tablo_olustur("kullanicilar", {"isim": "TEXT", "yas": "INTEGER"})
vt.ekle("kullanicilar", {"isim": "Ahmet", "yas": 25})
sonuclar = vt.bul("kullanicilar")
vt.kapat()
```

### Sınıf: Veritabani
- `tablo_olustur(isim, sutunlar)` — Tablo oluştur
- `ekle(tablo, veri)` — Kayıt ekle
- `bul(tablo, kosul)` — Kayıt ara
- `guncelle(tablo, veri, kosul)` — Kayıt güncelle
- `sil(tablo, kosul)` — Kayıt sil
- `sorgu(sql)` — Ham SQL çalıştır
