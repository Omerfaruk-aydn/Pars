# Başlangıç

## Kurulum

```bash
pip install pars-turkce-dil
```

## İlk Program

```pars
# merhaba.pars
yaz("Merhaba, Dünya!")

isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

```bash
pars merhaba.pars
```

## Etkileşimli Mod (REPL)

```bash
pars -g
```

REPL'de standart kütüphane hazır yüklüdür; `.yardim`, `.gecmis`,
`.sozdizimi`, `.degiskenler` komutlarını kullanabilirsiniz.

## Komut Satırı

```bash
pars dosya.pars          # Çalıştır
pars -g                  # REPL
pars -cevir dosya.pars   # Python karşılığını göster
pars -kontrol dosya.pars # Sözdizimi kontrolü
pars derle dosya.pars    # Python dosyasına derle
pars yeni projem         # Yeni proje oluştur
```

## Paketler ve Python

```bash
parskur yükle requests     # pip install yerine
parskur listele            # pip list yerine
parspy dosya.py            # python dosya.py yerine
parspy -c "print('selam')" # python -c yerine
```

## Standart Kütüphane

```pars
içe_aktar matematik
içe_aktar koleksiyonlar

yaz(matematik.asal_mi(97))
yaz(koleksiyonlar.en_sik("pars gibi pars"))
```
