# Başlangıç

## Kurulum

```bash
pip install pars-dil
```

## İlk Program

```pars
# merhaba.prs
yaz("Merhaba, Dünya!")

isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

```bash
pars merhaba.prs
```

## Etkileşimli Mod (REPL)

```bash
pars -g
```

## Komut Satırı

```bash
pars dosya.prs          # Çalıştır
pars -g                  # REPL
pars -cevir dosya.prs   # Python karşılığını göster
pars -kontrol dosya.prs # Sözdizimi kontrolü
pars yeni projem         # Yeni proje oluştur
```
