# Kurulum

## pip ile Kurulum

```bash
pip install pars-dil
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
```

Çıktı:
```
PARS v1.0.0
```

## İlk Program

```bash
echo 'yaz("Merhaba, Dünya!")' > merhaba.prs
pars merhaba.prs
```

Çıktı:
```
Merhaba, Dünya!
```
