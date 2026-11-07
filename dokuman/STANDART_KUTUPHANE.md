# Standart Kütüphane

PARS standart kütüphanesi, Python modüllerini Türkçe sarmalayıcılarla sunar.
v1.0.1 ile 28 modüle çıkmıştır.

Modüller `içe_aktar <modül>` ile veya doğrudan ad alanında hazır gelir.

## matematik

```pars
yaz(matematik.PI)
yaz(matematik.kare_kok(16))      # 4.0
yaz(matematik.faktoriyel(5))     # 120
yaz(matematik.asal_mi(97))       # doğru
yaz(matematik.tam_bolenler(12))  # [1, 2, 3, 4, 6, 12]
```

Temel: `kare_kok`, `us`, `mutlak`, `yuvarlak`, `tavan`, `taban_al`, `mod`,
`kare`, `kup`, `isaret`, `sinirla`, `yaklasik_esit`, `asal_mi`, `tam_bolenler`.
Trigonometri: `sinus`, `kosinus`, `tanjant`, `ark_sinus`, `derece_radyan`,
`radyan_derece`, `hipotenus`.
Logaritma: `logaritma`, `log10`, `log2`, `log1p`, `exp`, `expm1`.
Kombinatorik: `faktoriyel`, `kombinasyon`, `permutasyon`, `obeb`, `okek`.
İstatistik: `ortalama`, `medyan`, `mod_istatistik`, `standart_sapma`,
`varyans`, `kovaryans`, `toplam`, `carpanlar`, `en_yakin`, `dizi_toplami`.

## istatistik

```pars
notlar = [85, 92, 78, 95, 88]
yaz(istatistik.ortalama(notlar))
yaz(istatistik.ceyrekler(notlar))
yaz(istatistik.korelasyon([1,2,3], [2,4,6]))
```

`ortalama`, `medyan`, `mod`, `cok_mod`, `harmonik_ortalama`,
`geometrik_ortalama`, `varyans`, `standart_sapma`, `sapma`, `yakinlik`,
`ceyrekler`, `korelasyon`, `dogrusal_regresyon`, `aralik`, `siklik`.

## metin

```pars
yaz(metin.buyuk_harf("merhaba"))
yaz(metin.bol("a,b,c", ","))
yaz(metin.slug("PARS Türkçe Dil"))
yaz(metin.benzerlik("pars", "pars-dil"))
```

`buyuk_harf`, `kucuk_harf`, `bas_buyuk`, `her_bas_buyuk`, `bosluk_temizle`,
`bol`, `satirlara_bol`, `birlestir`, `degistir`, `iceriyor_mu`,
`ile_basliyor_mu`, `ile_bitiyor_mu`, `bul`, `bul_sagdan`, `say`, `tekrarla`,
`tersine_cevir`, `doldur_sola`, `doldur_saga`, `ortala`, `sayi_mi`, `harf_mi`,
`alfanumerik_mi`, `bos_mu`, `buyuk_harf_mi`, `kucuk_harf_mi`, `sifrele`,
`coz`, `regex_bul`, `regex_degistir`, `regex_bol`, `kelimeler`,
`satir_sayisi`, `kisalt`, `sar`, `girintile`, `girinti_kaldir`, `slug`,
`yilan_case`, `deve_case`, `yuzde_kodla`, `yuzde_coz`, `html_kacis`,
`html_coz`, `benzerlik`, `farklar`, `bicim`, `tersten`, `sayi_metni`,
`kirp`, `son`.

## liste

```pars
yaz(liste.tekil([1,2,2,3]))
yaz(liste.grupla([1,2,3,4,5], 2))
yaz(liste.pencere([1,2,3,4], 2))
yaz(liste.parcala([1,2,3,4,5], 2))
```

Liste: `duzlestir`, `tekil`, `grupla`, `dondur_liste`, `zip_ile_birlestir`,
`sirala_ters`, `filtrele`, `haritala`, `azalt`, `bolustur`, `ortak_elemanlar`,
`fark`, `birlesim`, `ilk`, `son`, `orta`, `pencere`, `parcala`, `sikistir`,
`zip_uzun`, `karistir`, `ornek`, `indeks`, `sayim`, `kesisim`, `liste_esitle`.
Sözlük: `anahtarlar`, `degerler`, `ciftler`, `sozluk_filtrele`,
`sozluk_harita`, `sozluk_birlestir`, `tersle`, `varsayilan_sozluk`,
`sirali_sozluk`, `sozluk_anahtar_degistir`, `sozluk_derin_birlestir`.
Yığın/kuyruk: `yigin_olustur`, `yigina_ekle`, `yigindan_al`,
`kuyruk_olustur`, `kuyruga_ekle`, `kuyruktan_al`.

## koleksiyonlar

```pars
sayac = koleksiyonlar.Sayac(["a", "a", "b"])
yaz(sayac.most_common())
yaz(koleksiyonlar.en_sik(["a", "a", "b"]))   # a

q = koleksiyonlar.CiftUclu([1, 2, 3])
q.appendleft(0)
```

`Sayac`/`sayaç`, `SiraliSozluk`, `ZincirSozluk`, `VarsayilanSozluk`,
`CiftUclu`, `AdliDemet`, `say`, `en_sik`, `en_az`, `elemanlar`, `ilk_n`,
`son_n`, `dondur`.

## yinelenebilirler

```pars
yaz(list(yinelenebilirler.kombinasyonlar([1,2,3], 2)))
yaz(yinelenebilirler.birikimli([1,2,3]))     # [1, 3, 6]
yaz(yinelenebilirler.ilk_n(yinelenebilirler.say(10), 3))
```

`say`, `dongu`, `tekrar`, `zincirle`, `kombinasyonlar`,
`kombinasyonlu_tekrar`, `permutasyonlar`, `carpim`, `grupla`, `dilimle`,
`ilk_n`, `tara`, `birikimli`, `sikistir_uzun`, `sikistir`,
`filtrele_yanlis`, `tekrarla`.

## fonksiyonel

```pars
kare = fonksiyonel.kismi(lambda a, b: a ** b, b=2)
yaz(kare(5))                                  # 25
yaz(fonksiyonel.azalt(lambda a, b: a + b, [1,2,3]))
```

`kismi`, `azalt`, `onbellek`, `sarmala`, `karsilastirici`,
`tek_yonlu_ozellik`, `toplam_azalt`, `boru`, `calistir_baglam`,
`sirala_anahtar`.

## dosya

```pars
dosya.yaz("test.txt", "merhaba")
yaz(dosya.oku("test.txt"))
yaz(dosya.json_oku("veri.json"))
```

`oku`, `yaz`, `ekle`, `satirlari_oku`, `satirlari_yaz`, `var_mi`,
`klasor_mu`, `dosya_mi`, `sil`, `tasi`, `kopyala`, `yeniden_adlandir`,
`klasor_olustur`, `klasor_sil`, `listele`, `boyut`, `uzanti`, `dosya_adi`,
`ana_klasor`, `tam_yol`, `gecici_dosya`, `gecici_klasor`, `json_oku`,
`json_yaz`, `csv_oku`, `csv_yaz`.

## yol

```pars
y = yol.birlestir("klasor", "dosya.txt")
yol.yaz(y, "içerik")
yaz(yol.oku(y))
yaz(yol.listele(".", "*.pars"))
```

`Yol`, `yol`, `simdiki`, `ev`, `birlestir`, `var_mi`, `dosya_mi`,
`klasor_mi`, `baglanti_mi`, `oku`, `oku_bayt`, `yaz`, `yaz_bayt`, `ekle`,
`listele`, `glob`, `uzanti`, `ad`, `kok`, `ust`, `coz`, `boyut`, `olustur`,
`sil`, `kopyala`, `tasi`, `goreli`, `mutlak`, `parcalar`, `degistir`.

## zaman

```pars
yaz(zaman.simdi())
yaz(zaman.turkce_tarih(zaman.simdi()))
yaz(zaman.bicimle(zaman.simdi(), "%d.%m.%Y"))
zaman.bekle(0.1)
```

`simdi`, `simdi_utc`, `bugun`, `zaman_damgasi`, `bekle`, `uyu`, `sleep`,
`sure_olc`, `perf_counter`, `monotonik`, `tarih`, `saat_olustur`, `fark`,
`bicimle`/`biçimle`, `cozmle`/`çözümle`, `iso_metin`, `turkce_tarih`,
`hafta_numarasi`, `gun_adi`, `ay_adi`, `yil`, `ay`, `gun`, `saat`, `dakika`,
`saniye`, `is_gunu_mu`, `hafta_sonu_mu`, `gun_ekle`, `ay_ekle`, `gecti_mi`,
`kalan_sure`.

## takvim

```pars
yaz(takvim.artik_yil(2024))          # doğru
yaz(takvim.ay_gun_sayisi(2024, 2))   # 29
yaz(takvim.gun_adi("2026-11-06"))    # Cuma
```

`artik_yil`, `ay_gun_sayisi`, `ay_takvimi`, `hafta_gunu`, `gun_adi`,
`ay_adi`, `yil_haftalari`, `tarih_araligi`, `ay_basi`, `ay_sonu`.

## sistem

```pars
yaz(sistem.calisma_dizini())
yaz(sistem.isletim_sistemi())
yaz(sistem.kullanici_adi())
```

`ortam_degiskeni`, `ortam_degiskeni_ata`, `calisma_dizini`, `dizin_degistir`,
`komut_calistir`, `islem_id`, `islem_sonlandir`, `argumanlar`,
`platform_bilgisi`, `isletim_sistemi`, `kullanici_adi`, `ev_dizini`,
`cpu_sayisi`, `bellek_kullanimi`, `python_surumu`, `pars_surumu`.

## isletim / işletim

```pars
yaz(isletim.calisma_dizini())
yaz(isletim.cpu_sayisi())
for dizin, alt, dosyalar in isletim.gez("."):
    yaz(dizin)
```

`ortam`, `ortam_ata`, `ortam_sil`, `ortam_hepsi`, `calisma_dizini`,
`dizin_degistir`, `listele`, `gez`, `olustur`, `sil`, `sil_agac`,
`yeniden_adlandir`, `kopyala`, `tasi`, `istatistik`, `yol_birlestir`,
`yol_ayir`, `mutlak_yol`, `var_mi`, `dosya_mi`, `klasor_mi`, `cpu_sayisi`,
`isletim_sistemi`, `kullanici`, `ev_dizini`, `gecici_dizin`,
`gecici_dosya`, `ayrac`, `satir_ayrac`.

## surec / süreç

```pars
sonuc = surec.calistir(["python", "--version"])
yaz(sonuc["cikti"])
sonuc = surec.python_calistir("print('selam')")
```

`calistir`, `cikti_al`, `kontrol_et`, `boru`, `kabuk_calistir`,
`python_calistir`, `pars_calistir`, `bekle`.

## iplik

```pars
t = iplik.Iplik(fonksiyon_adi, arguman)
t.baslat(); t.katil()

with iplik.Havuz(4) as havuz:
    sonuclar = list(havuz.haritala(kare, range(10)))
```

`Iplik`, `Kilit`, `Olay`, `Kosul`, `Semafor`, `Kuyruk`, `Havuz`,
`SurecHavuzu`, `paralel_calistir`, `tamamlananlar`, `bekle_hepsi`,
`gecikmeli`.

## gunluk / günlük

```pars
gunluk.temel_yapilandir(seviye="bilgi")
gunluk.bilgi("mesaj")
gunluk.hata("hata")
```

`temel_yapilandir`, `gunlukcu_al`, `bilgi`, `uyari`, `hata`, `kritik`,
`ayikla`, `seviye_ata`, `dosyaya_yaz`, `gunlukcu_ekle`, `bicim`.

## rastgele

```pars
yaz(rastgele.rastgele_sayi(1, 100))
yaz(rastgele.rastgele_sec(["elma", "armut"]))
```

`rastgele_sayi`, `rastgele_ondalikli`, `rastgele_sec`, `rastgele_karistir`,
`rastgele_ornek`, `rastgele_agirlikli`, `rastgele_metin`, `rastgele_id`,
`tohum_ata`.

## sifreleme / şifreleme

```pars
yaz(sifreleme.sha256("metin"))
yaz(sifreleme.base64_kodla("PARS"))
yaz(sifreleme.hmac_hesapla("anahtar", "mesaj"))
```

`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `hash_hesapla`,
`dosya_hash`, `hmac_hesapla`, `sabit_karsilastir`, `base64_kodla`,
`base64_coz`, `url_base64_kodla`, `url_base64_coz`, `rastgele_metin`,
`rastgele_bayt`, `rastgele_sayi`, `uuid4`, `uuid_hex`.

## sikistirma / sıkıştırma

```pars
s = sikistirma.gzip_sikistir(b"veri")
yaz(sikistirma.gzip_ac(s))
sikistirma.zip_olustur("arsiv.zip", ["a.txt"])
```

`gzip_sikistir`, `gzip_ac`, `zlib_sikistir`, `zlib_ac`, `zip_olustur`,
`zip_ac`, `zip_listele`, `zip_oku`, `tar_olustur`, `tar_ac`, `tar_listele`.

## sayi / sayı

```pars
yaz(sayi.kesin_topla("0.1", "0.2"))   # 0.3
yaz(sayi.kesir(1, 3))
yaz(sayi.ondalik_yuvarla("3.14159", 2))
```

`Ondalik`, `Kesir`, `ondalik`, `kesir`, `ondalik_yuvarla`, `kesin_topla`,
`kesin_cikar`, `kesin_carp`, `kesin_bol`, `yuzde`, `sinirla`, `bilimsel`,
`hassasiyet`.

## kopya

`kopyala`, `derin_kopyala`, `yedek_al`, `geri_yukle`, `esit_mi`.

## veri

`json_metin`, `json_cozumle`, `json_oku`, `json_yaz`, `csv_oku`, `csv_yaz`,
`kaydet`, `yukle`, `base64_kodla`, `base64_coz`, `hash_hesapla`.

## veri_siniflari / veri_sınıfları

```pars
@veri_siniflari.veri_sinifi
sınıf Kisi:
    ad: str
    yas: int = 0
```

`veri_sinifi`, `alan`, `degismez`, `sirali`, `sozluge_cevir`, `demete_cevir`,
`degistir`, `alanlar`.

## ag / ağ

```pars
yanit = ag.get("https://api.ornek.com")
yaz(yanit["govde"])
yaz(ag.json_al("https://api.ornek.com/veri"))
```

`get`, `post`, `put`, `sil_istek`, `dosya_indir`, `url_kodla`, `json_al`.

## veritabani / veritabanı

```pars
vt = veritabani.Veritabani("veriler.db")
vt.tablo_olustur("kullanicilar", {"isim": "TEXT", "yas": "INTEGER"})
vt.ekle("kullanicilar", {"isim": "Ahmet", "yas": 25})
yaz(vt.bul("kullanicilar"))
vt.kapat()
```

Sınıf: `Veritabani` — `baglan`, `kapat`, `tablo_olustur`, `ekle`, `bul`,
`guncelle`, `sil`, `sorgu`, `islem_baslat`, `islem_kaydet`, `islem_geri_al`,
`tablo_listele`, `tablo_sil`.

## arguman / argüman

```pars
ay = arguman.ArgumanAyristirici("Uygulama", surum="1.0.1")
ay.konumlu("dosya", yardim="Girdi dosyası")
ay.secenek("--mod", varsayilan="hizli")
ay.bayrak("--ayrintili")
secenekler = ay.ayristir()
```

`ArgumanAyristirici`, `konumlu`, `secenek`, `bayrak`, `dizi`, `ayristir`,
`bilinenleri`, `yardim`, `alt_ayristirici`.

## deneme

```pars
sınıf Testler(deneme.Deneme):
    fonksiyon test_toplama(öz):
        öz.iddia_esit(1 + 1, 2)

deneme.calistir(Testler)
```

`Deneme`, `TestDurumu`, `calistir`, `kosum`, `iddia_esit`, `iddia_dogru`,
`iddia_yanlis`, `iddia_icinde`, `atla`.

## kopru / köprü

Python kütüphanelerini PARS sözdizimine uyarlar. Öznitelikler hem özgün
(İngilizce) hem Türkçe adla erişilebilir.

```pars
içe_aktar köprü

istek = köprü.bagla("requests")
yanit = istek.al("https://api.ornek.com")
yaz(yanit.durum_kodu)   # status_code
```

`pars köprü <modül>` öznitelikleri listeler, `pars köprü dışa <modül>`
bir `.pars` sarmalayıcı üretir.

`Kopru`, `bagla`, `kutuphane_yukle`, `turkce_ad`, `ingilizce_ad`,
`ceviri_sozlugu`, `sozluk_ekle`, `disa_aktar`, `ozellik_listesi`.
