# Kurulum

## pip ile Kurulum

```bash
pip install pars-turkce-dil
```

## Kaynak Koddan Kurulum

```bash
git clone https://github.com/pars-lang/pars.git
cd pars
pip install -e .
```

## Geliştirme Kurulumu

```bash
pip install -e ".[dev]"
```

## Doğrulama

```bash
pars --surum
parskur --surum
parspy --surum
```

Çıktı:

```
PARS v1.0.1
```

## İlk Program

```bash
echo 'yaz("Merhaba, Dünya!")' > merhaba.pars
pars merhaba.pars
```

Çıktı:

```
Merhaba, Dünya!
```

## Komutlar

```bash
pars merhaba.pars          # PARS çalıştır
pars -g                   # PARS REPL
parskur yükle requests    # pip install yerine
parspip yükle requests    # pip install yerine
pars köprü json           # Python kütüphanesini PARS'a uyarla
parspy dosya.py           # python dosya.py yerine
parspy -c "print(1)"      # python -c yerine
```
