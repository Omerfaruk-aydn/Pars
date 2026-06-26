# Sıkça Sorulan Sorular

## PARS nedir?

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir programlama dilidir.

## PARS neden Python kullanıyor?

Python'un tüm gücünü Türkçe ile kullanabilmeniz için. Kendi interpreter'ınızı yazmak yerine Python'un olgun ekosisteminden yararlanır.

## PARS ile Python kütüphanelerini kullanabilir miyim?

Evet! Tüm Python kütüphanelerini doğrudan kullanabilirsiniz:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
```

## Türkçe değişken isimleri çalışır mı?

Evet! Python 3 Unicode tanımlayıcıları destekler:

```pars
yaş = 25
şehir = "İstanbul"
öğrenci_adı = "Ahmet"
```

## `öz` nedir?

`öz`, Python'daki `self` yerine kullanılır. Sınıf metodlarında nesneye referans vermek için kullanılır:

```pars
 sınıf Araba:
    fonksiyon __init__(öz, marka):
        öz.marka = marka
```

## Hata mesajları Türkçe mi?

Evet! Tüm Python hata tipleri Türkçe karşılıklarıyla gösterilir:

```
Sıfıra Bölme Hatası (satır 5)
  sonuç = 10 / 0

İpucu: Bir sayıyı sıfıra bölemezsiniz.
```

## PARS dosyasını Python'a çevirebilir miyim?

Evet! `-cevir` komutu ile:

```bash
pars -cevir dosya.prs
```

## PARS'ı nasıl kurarım?

```bash
pip install pars-dil
```

## Hangi Python sürümlerini destekler?

Python 3.8 ve üzeri.

## PARS ücretsiz mi?

Evet! MIT lisansı ile tamamen ücretsiz ve açık kaynak.

## Katkıda bulunabilir miyim?

Evet! GitHub'dan forklayıp PR gönderebilirsiniz: https://github.com/pars-lang/pars

## VS Code desteği var mı?

Evet! `vscode-uzantisi/` klasöründe sözdizimi renklendirme eklentisi bulunur.

## PARS yavaş mı?

PARS, Python kodunu bellekte çevirip çalıştırır. Çeviri overhead'i minimaldir. Python'un hızı neyse PARS'ın hızı odur.

## Kendi modülümü yazabilir miyim?

Evet! Normal Python modülleri gibi `.py` dosyaları yazıp `içe_aktar` ile kullanabilirsiniz.
