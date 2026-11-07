# Sıkça Sorulan Sorular

## PARS nedir?

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir
programlama dilidir.

## PARS neden Python kullanıyor?

Python'un tüm gücünü Türkçe ile kullanabilmeniz için. Kendi interpreter'ını
yazmak yerine Python'un olgun ekosisteminden yararlanır.

## PARS ile Python kütüphanelerini kullanabilir miyim?

Evet! Tüm Python kütüphanelerini doğrudan kullanabilirsiniz:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
```

Kurulum: `parskur yükle numpy pandas`

## Türkçe değişken isimleri çalışır mı?

Evet! Python 3 Unicode tanımlayıcıları destekler:

```pars
yaş = 25
şehir = "İstanbul"
öğrenci_adı = "Ahmet"
```

## `öz` nedir?

`öz`, Python'daki `self` yerine kullanılır (sıradan bir parametre adıdır):

```pars
sınıf Araba:
    fonksiyon __init__(öz, marka):
        öz.marka = marka
```

## Hata mesajları Türkçe mi?

Evet! Tüm Python hata tipleri Türkçe karşılıklarıyla, hatalı satır ve
akıllı ipucuyla gösterilir.

## PARS dosyasını Python'a çevirebilir miyim?

Evet:

```bash
pars -cevir dosya.pars
pars derle dosya.pars        # dosya.py üretir
```

## PARS'ı nasıl kurarım?

```bash
pip install pars-turkce-dil
```

## Hangi Python sürümlerini destekler?

Python 3.8 ve üzeri.

## `pip` ve `python` yerine ne kullanmalıyım?

PARS kendi araçlarını sunar:

```bash
parskur yükle requests      # pip install yerine
parskur listele             # pip list yerine
parspy dosya.py             # python dosya.py yerine
parspy -c "print(1)"        # python -c yerine
```

## Standart kütüphanede neler var?

v1.0.1 ile 28 modül: matematik, istatistik, metin, liste, koleksiyonlar,
yinelenebilirler, fonksiyonel, dosya, yol, zaman, takvim, sistem, isletim,
surec, iplik, gunluk, rastgele, sifreleme, sikistirma, sayi, kopya, veri,
veri_siniflari, ag, veritabani, arguman, deneme, kopru.

## PARS ücretsiz mi?

Evet! MIT lisansı ile tamamen ücretsiz ve açık kaynak.

## Katkıda bulunabilir miyim?

Evet! GitHub'dan forklayıp PR gönderebilirsiniz:
https://github.com/pars-lang/pars

## VS Code desteği var mı?

Evet! `vscode-uzantisi/` klasöründe sözdizimi renklendirme eklentisi bulunur.

## PARS yavaş mı?

PARS, Python kodunu bellekte çevirip çalıştırır. Çeviri overhead'i
minimaldir. Python'un hızı neyse PARS'ın hızı odur.

## Kendi modülümü yazabilir miyim?

Evet! Normal Python modülleri gibi `.py` dosyaları yazıp `içe_aktar` ile
kullanabilirsiniz. Kendi `.pars` dosyalarınızı da aynı klasöre koyup
`içe_aktar yardimci` veya `den_aktar yardimci içe_aktar fonksiyon` ile
yükleyebilirsiniz; PARS yerel `.pars` modüllerini otomatik çevirir.

## Ayrılmış sözcükler neler?

`sınıf`, `fonksiyon`, `sil`, `döndür`, `eğer`, `için` gibi anahtar kelimeler
değişken adı olarak kullanılamaz. Noktadan sonra gelen adlar güvenlidir
(`dosya.sil`).
