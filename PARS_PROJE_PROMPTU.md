
> **"Pars gibi hızlı. Türkçe gibi güzel."**
>
> Sen kıdemli bir programlama dili tasarımcısı ve Python mimarısın.
> Senden **PARS** adında, Python altyapısını kullanan, eksiksiz,
> profesyonel ve yayına hazır bir Türkçe programlama dili geliştirmeni istiyorum.
> Aşağıdaki her madde eksiksiz uygulanacak. Yarım iş kabul edilmez.

---

## 1. KİMLİK VE MARKA

| Alan | Değer |
|---|---|
| Dil adı | **PARS** |
| Slogan | **"Pars gibi hızlı. Türkçe gibi güzel."** |
| Dosya uzantısı | `.pars` |
| Komut | `pars` |
| pip paketi | `pars-dil` |
| GitHub org | `pars-lang` |
| GitHub repo | `pars-lang/pars` |
| Website | `parsdil.com` |
| Python min. | `3.8+` |
| Lisans | MIT |
| İlk versiyon | `1.0.0` |
| Ana renk | `#EF9F27` (Pars Altını) |
| Arka plan | `#1a1a2e` (Gece Mavisi) |
| Vurgu rengi | `#9FE1CB` (Kod Yeşili) |
| Anahtar kelime rengi | `#7F77DD` (Mor) |

---

## 2. MİMARİ: TRANSPILER + EXEC

### Akış
```
Kullanıcı Kodu (.pars)
        │
   [Tokenizer]          → string/yorum içeriğini koru
        │
   [Çevirici]           → Türkçe anahtar kelime → Python anahtar kelime
        │
   Python Kodu          → bellekte, diske yazılmaz
        │
 compile() + exec()     → Python runtime
        │
      Çıktı
```

### Temel ilkeler
- Türkçe anahtar kelimeler Python karşılıklarına bire bir çevrilir
- Python 3 Unicode tanımlayıcılar desteklediğinden `yaş`, `öğrenci`, `şehir`, `öz` gibi değişken isimleri hiçbir dönüşüm gerektirmez
- Satır numaraları korunur — hata mesajları doğru satırı gösterir
- String ve yorum içleri asla değiştirilmez
- f-string içindeki `{değişken}` bölümleri korunur
- `öz` kelimesi Python'daki `self` gibi kullanılır (dönüşüm gerekmez, Python Unicode kabul eder)
- Tüm PyPI paketleri doğrudan çalışır: `içe_aktar numpy olarak np`
- `pars paket yükle <paket>` → `pip install <paket>` ile eşdeğerdir

---

## 3. TAM KLASÖR YAPISI

Her dosya aşağıdaki yapıda olacak. Hiçbir dosya eksik bırakılmayacak:

```
pars/
│
├── pars/                              # Ana Python paketi
│   ├── __init__.py                    # Versiyon, __all__, paket meta
│   │
│   ├── cekirdek/                      # Dilin motoru
│   │   ├── __init__.py
│   │   ├── esleme.py                  # Tüm anahtar kelime + built-in eşlemeleri
│   │   ├── tokenizer.py               # Regex tabanlı tokenizer
│   │   ├── ceviri.py                  # Transpiler (Türkçe → Python)
│   │   ├── yurutucu.py                # Kod derleme ve çalıştırma motoru
│   │   ├── hatalar.py                 # Türkçe hata yakalama + gösterimi
│   │   └── repl.py                    # Etkileşimli konsol (REPL)
│   │
│   ├── standart/                      # PARS standart kütüphanesi
│   │   ├── __init__.py
│   │   ├── matematik.py               # math → Türkçe
│   │   ├── metin.py                   # str işlemleri → Türkçe
│   │   ├── liste.py                   # list/dict/set yardımcıları
│   │   ├── dosya.py                   # dosya I/O → Türkçe
│   │   ├── zaman.py                   # datetime → Türkçe
│   │   ├── sistem.py                  # os/sys/platform → Türkçe
│   │   ├── ag.py                      # urllib/requests → Türkçe
│   │   ├── veri.py                    # json/csv/pickle → Türkçe
│   │   ├── rastgele.py                # random/secrets → Türkçe
│   │   ├── eszamanli.py               # threading/asyncio → Türkçe
│   │   ├── veritabani.py              # sqlite3 → Türkçe
│   │   ├── sifreleme.py               # hashlib/hmac → Türkçe
│   │   └── test.py                    # unittest → Türkçe
│   │
│   └── cli/
│       ├── __init__.py
│       └── komutlar.py                # Argparse tabanlı CLI giriş noktası
│
├── ornekler/                          # 20 adet tam çalışan .pars programı
│   ├── 01_merhaba_dunya.pars
│   ├── 02_degiskenler_ve_tipler.pars
│   ├── 03_kosul_ifadeleri.pars
│   ├── 04_donguler.pars
│   ├── 05_fonksiyonlar_ve_lambda.pars
│   ├── 06_siniflar_ve_oop.pars
│   ├── 07_miras_ve_cok_bicimllik.pars
│   ├── 08_istisna_yonetimi.pars
│   ├── 09_dosya_isleme.pars
│   ├── 10_modüller_ve_paketler.pars
│   ├── 11_liste_sozluk_kume.pars
│   ├── 12_uretecler_ve_iteratorler.pars
│   ├── 13_dekoratorler.pars
│   ├── 14_context_manager.pars
│   ├── 15_async_await.pars
│   ├── 16_numpy_ve_pandas.pars
│   ├── 17_flask_web_uygulamasi.pars
│   ├── 18_sqlite_veritabani.pars
│   ├── 19_api_istekleri.pars
│   └── 20_tam_proje_ornegi.pars
│
├── testler/
│   ├── __init__.py
│   ├── conftest.py                    # pytest fixtures
│   ├── test_tokenizer.py              # Tokenizer birim testleri
│   ├── test_ceviri.py                 # Transpiler birim testleri
│   ├── test_yurutucu.py               # Executor entegrasyon testleri
│   ├── test_hatalar.py                # Hata mesajı testleri
│   ├── test_standart_matematik.py
│   ├── test_standart_metin.py
│   ├── test_standart_liste.py
│   ├── test_standart_dosya.py
│   ├── test_standart_zaman.py
│   ├── test_repl.py
│   └── test_ornekler.py               # Tüm .pars örnekleri çalıştırma testi
│
├── vscode-uzantisi/                   # VS Code sözdizimi renklendirme
│   ├── package.json
│   ├── language-configuration.json
│   └── syntaxes/
│       └── pars.tmLanguage.json
│
├── dokuman/
│   ├── README.md                      # Ana README (TR + EN)
│   ├── KURULUM.md
│   ├── SOZDIZIMI_REHBERI.md           # Tam sözdizimi kılavuzu
│   ├── BUILTIN_FONKSIYONLAR.md
│   ├── STANDART_KUTUPHANE.md
│   ├── PYTHON_KUTUPHANELERI.md        # Popüler paketlerle kullanım
│   ├── ORNEKLER.md
│   ├── SSS.md
│   ├── KATKI_REHBERI.md
│   └── DEGISIKLIK_GUNLUGU.md
│
├── website/                           # Statik dokümantasyon sitesi (MkDocs)
│   ├── mkdocs.yml
│   └── docs/
│       ├── index.md
│       ├── baslangic.md
│       └── referans.md
│
├── .github/
│   └── workflows/
│       ├── test.yml                   # Her push'ta pytest
│       ├── yayin.yml                  # PyPI otomatik yayın
│       └── docs.yml                   # GitHub Pages dokümantasyon
│
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── requirements.txt                   # Çalışma bağımlılıkları (boş olabilir)
├── requirements-dev.txt               # Geliştirme bağımlılıkları
├── .gitignore
├── .editorconfig
├── LICENSE
└── README.md
```

---

## 4. ANAHTAR KELİME EŞLEMESİ (TAM LİSTE)

`pars/cekirdek/esleme.py` dosyasına aşağıdaki sözlüğü yaz.
Her kelimenin hem Türkçe karakterli hem ASCII versiyonu olacak:

```python
KELIME_ESLEME = {

    # ── KOŞUL ─────────────────────────────────────────────────────────────
    'eğer':             'if',
    'eger':             'if',
    'değilse':          'else',
    'degilse':          'else',
    'yoksa':            'elif',

    # ── DÖNGÜ ─────────────────────────────────────────────────────────────
    'iken':             'while',
    'için':             'for',
    'icin':             'for',
    'içinde':           'in',
    'icinde':           'in',

    # ── FONKSİYON & SINIF ─────────────────────────────────────────────────
    'fonksiyon':        'def',
    'döndür':           'return',
    'dondur':           'return',
    'sınıf':            'class',
    'sinif':            'class',
    'lambda':           'lambda',
    'ver':              'yield',

    # ── MODÜL ─────────────────────────────────────────────────────────────
    'içe_aktar':        'import',
    'ice_aktar':        'import',
    'den_aktar':        'from',
    'olarak':           'as',

    # ── İSTİSNA YÖNETİMİ ──────────────────────────────────────────────────
    'dene':             'try',
    'hariç':            'except',
    'haric':            'except',
    'sonunda':          'finally',
    'yükselt':          'raise',
    'yukselt':          'raise',

    # ── BAĞLAM YÖNETİCİSİ ─────────────────────────────────────────────────
    'ile':              'with',

    # ── AKIŞ KONTROL ──────────────────────────────────────────────────────
    'geç':              'pass',
    'gec':              'pass',
    'kes':              'break',
    'devam':            'continue',
    'sil':              'del',
    'iddia':            'assert',

    # ── KAPSAM ────────────────────────────────────────────────────────────
    'global':           'global',
    'yerel_değil':      'nonlocal',
    'yerel_degil':      'nonlocal',

    # ── ASYNC / AWAIT ─────────────────────────────────────────────────────
    'eşzamansız':       'async',
    'esezamansiz':      'async',
    'bekle':            'await',

    # ── MANTIKSAL ─────────────────────────────────────────────────────────
    've':               'and',
    'veya':             'or',
    'değil':            'not',
    'degil':            'not',

    # ── KİMLİK / ÜYELİK ───────────────────────────────────────────────────
    'içindedir':        'in',
    'dır':              'is',
    'dir':              'is',

    # ── DEĞERLERi ─────────────────────────────────────────────────────────
    'doğru':            'True',
    'dogru':            'True',
    'yanlış':           'False',
    'yanlis':           'False',
    'yok':              'None',
}
```

---

## 5. TÜRKÇE YERLEŞİK FONKSİYONLAR (TAM LİSTE)

```python
# pars/cekirdek/esleme.py — devamı

def _yaz(*args, sep=' ', son='\n', dosya=None, temizle=False):
    """
    Türkçe print.
    True  → doğru
    False → yanlış
    None  → yok
    Liste → [eleman1, eleman2, ...]
    """
    import sys
    def _goster(v):
        if v is True:   return 'doğru'
        if v is False:  return 'yanlış'
        if v is None:   return 'yok'
        if isinstance(v, list):
            return '[' + ', '.join(_goster(i) for i in v) + ']'
        if isinstance(v, dict):
            return '{' + ', '.join(f'{_goster(k)}: {_goster(val)}' for k,val in v.items()) + '}'
        if isinstance(v, tuple):
            return '(' + ', '.join(_goster(i) for i in v) + ')'
        if isinstance(v, set):
            return '{' + ', '.join(_goster(i) for i in v) + '}'
        return str(v)
    print(*[_goster(a) for a in args],
          sep=sep, end=son,
          file=dosya or sys.stdout,
          flush=temizle)

def _paket_yukle(*paketler):
    """pip install wrapper"""
    import subprocess, sys
    for paket in paketler:
        print(f'▶  pip install {paket}')
        subprocess.run([sys.executable, '-m', 'pip', 'install', paket])

def _paket_listele():
    """pip list wrapper"""
    import subprocess, sys
    subprocess.run([sys.executable, '-m', 'pip', 'list'])

PARS_BUILTINS = {

    # ── GİRİŞ / ÇIKIŞ ─────────────────────────────────────────────────────
    'yaz':                  _yaz,
    'girdial':              input,
    'açık':                 open,
    'acik':                 open,

    # ── TİP DÖNÜŞÜMÜ ──────────────────────────────────────────────────────
    'tam_sayı':             int,
    'tam_sayi':             int,
    'ondalıklı':            float,
    'ondalikli':            float,
    'yazıya_çevir':         str,
    'yaziya_cevir':         str,
    'mantıksal':            bool,
    'mantiksal':            bool,
    'karmaşık':             complex,
    'karmasik':             complex,
    'bayt':                 bytes,
    'bayt_dizisi':          bytearray,
    'bellek_görünümü':      memoryview,

    # ── VERİ YAPILARI ─────────────────────────────────────────────────────
    'liste':                list,
    'demet':                tuple,
    'küme':                 set,
    'kume':                 set,
    'dondurulmuş_küme':     frozenset,
    'dondurulmus_kume':     frozenset,
    'sözlük':               dict,
    'sozluk':               dict,
    'listeye_çevir':        list,
    'listeye_cevir':        list,
    'demete_çevir':         tuple,
    'demete_cevir':         tuple,
    'kümeye_çevir':         set,
    'kumeye_cevir':         set,
    'sözlüğe_çevir':        dict,
    'sozluge_cevir':        dict,

    # ── İTERASYON ─────────────────────────────────────────────────────────
    'aralık':               range,
    'aralik':               range,
    'numaralandır':         enumerate,
    'numaralandir':         enumerate,
    'sıkıştır':             zip,
    'sikistir':             zip,
    'harita':               map,
    'filtre':               filter,
    'sırala':               sorted,
    'sirala':               sorted,
    'tersine':              reversed,
    'tümü':                 all,
    'tumu':                 all,
    'herhangi':             any,
    'sonraki':              next,
    'iter_et':              iter,
    'dilimle':              slice,

    # ── MATEMATİK ─────────────────────────────────────────────────────────
    'mutlak':               abs,
    'yuvarlak':             round,
    'toplam':               sum,
    'maksimum':             max,
    'minimum':              min,
    'güç':                  pow,
    'guc':                  pow,

    # ── METİN / DİZİ ──────────────────────────────────────────────────────
    'uzunluk':              len,
    'karakter':             chr,
    'karakter_kodu':        ord,
    'onaltılık':            hex,
    'onaltili':             hex,
    'sekizlik':             oct,
    'ikili':                bin,
    'biçimle':              format,
    'bicimle':              format,
    'yazdır':               repr,
    'yazdir':               repr,

    # ── İNCELEYİCİLER ─────────────────────────────────────────────────────
    'tip':                  type,
    'kimlik':               id,
    'dir':                  dir,
    'yardım':               help,
    'yardim':               help,
    'özellikler':           vars,
    'ozellikler':           vars,
    'nitelik_al':           getattr,
    'nitelik_ata':          setattr,
    'nitelik_sil':          delattr,
    'nitelik_var_mı':       hasattr,
    'nitelik_var_mi':       hasattr,
    'türünden_mi':          isinstance,
    'turundan_mi':          isinstance,
    'alt_sınıfı_mı':        issubclass,
    'alt_sinifi_mi':        issubclass,
    'çağrılabilir_mi':      callable,
    'cagrılabilir_mi':      callable,
    'repr':                 repr,

    # ── NESNE YÖNELİMLİ ───────────────────────────────────────────────────
    'nesne':                object,
    'süper':                super,
    'super':                super,
    'özellik':              property,
    'ozellik':              property,
    'statik_metot':         staticmethod,
    'sınıf_metot':          classmethod,
    'sinif_metot':          classmethod,

    # ── SİSTEM ────────────────────────────────────────────────────────────
    'çıkış':                exit,
    'cikis':                exit,
    'değerlendir':          eval,
    'degerlendir':          eval,
    'çalıştır':             exec,
    'calistir_kod':         exec,
    'derle':                compile,
    'modül_yükle':          __import__,

    # ── PAKET YÖNETİMİ ────────────────────────────────────────────────────
    'paket_yükle':          _paket_yukle,
    'paket_yukle':          _paket_yukle,
    'paket_listele':        _paket_listele,

    # ── DEĞERLER ──────────────────────────────────────────────────────────
    'doğru':                True,
    'dogru':                True,
    'yanlış':               False,
    'yanlis':               False,
    'yok':                  None,
}

# İstisna sınıfı eşlemeleri
PARS_ISTISNALAR = {
    'Hata':                     Exception,
    'SözDizimiHatası':          SyntaxError,
    'SozdizimHatasi':           SyntaxError,
    'AdHatası':                 NameError,
    'AdHatasi':                 NameError,
    'TürHatası':                TypeError,
    'TurHatasi':                TypeError,
    'DeğerHatası':              ValueError,
    'DegerHatasi':              ValueError,
    'İndeksHatası':             IndexError,
    'IndeksHatasi':             IndexError,
    'AnahtarHatası':            KeyError,
    'AnahtarHatasi':            KeyError,
    'NitelikHatası':            AttributeError,
    'NitelikHatasi':            AttributeError,
    'İçeAktarmaHatası':         ImportError,
    'IceAktarmaHatasi':         ImportError,
    'ModülBulunamadı':          ModuleNotFoundError,
    'ModulBulunamadi':          ModuleNotFoundError,
    'DosyaBulunamadı':          FileNotFoundError,
    'DosyaBulunamadi':          FileNotFoundError,
    'İzinHatası':               PermissionError,
    'IzinHatasi':               PermissionError,
    'ZamanAşımı':               TimeoutError,
    'ZamanAsimi':               TimeoutError,
    'SıfıraBölmeHatası':        ZeroDivisionError,
    'SifiraBolmeHatasi':        ZeroDivisionError,
    'TaşmaHatası':              OverflowError,
    'TasmaHatasi':              OverflowError,
    'BellekHatası':             MemoryError,
    'BellekHatasi':             MemoryError,
    'ÖzyinelemeSınırı':         RecursionError,
    'OzyinelemeSiniri':         RecursionError,
    'KlayvyeKesmesi':           KeyboardInterrupt,
    'DurdurmaIsareti':          KeyboardInterrupt,
    'SistemÇıkışı':             SystemExit,
    'SistemCikisi':             SystemExit,
    'IterasyonBitti':           StopIteration,
    'ÜreticiÇıkışı':            GeneratorExit,
    'UreticiCikisi':            GeneratorExit,
    'Uyarı':                    Warning,
    'Uyari':                    Warning,
    'KullanimUyarisi':          DeprecationWarning,
    'KullanimUyarısı':          DeprecationWarning,
    'RuntimeHatası':            RuntimeError,
    'RuntimeHatasi':            RuntimeError,
    'SistemHatası':             OSError,
    'SistemHatasi':             OSError,
    'UygulanmadiHatasi':        NotImplementedError,
    'UygulanmadıHatası':        NotImplementedError,
}
```

---

## 6. TOKENIZER (pars/cekirdek/tokenizer.py)

Türkçe kaynak kodu güvenli biçimde tokenlarına ayıran modül.
String içleri, yorumlar ve f-string'ler asla değiştirilmez.

```python
"""
PARS Tokenizer
--------------
Token türleri:
  STR   → "...", '...', \"\"\"...\"\"\", '''...'''
  YORUM → # ... (satır sonu)
  ISIM  → Türkçe/İngilizce tanımlayıcı (anahtar kelime kontrolü yapılır)
  DIGER → operatör, boşluk, sayı, noktalama
"""

import re
from typing import List, Tuple

TR_HARF = 'çğışöüÇĞİŞÖÜ'

TOKEN_RE = re.compile(
    r'"""[\s\S]*?"""'
    r"|'''[\s\S]*?'''"
    r'|"(?:[^"\\]|\\.)*"'
    r"|'(?:[^'\\]|\\.)*'"
    r'|#[^\n]*'
    rf'|[a-zA-Z{TR_HARF}_][a-zA-Z0-9{TR_HARF}_]*'
    r'|.',
    re.DOTALL
)

TokenListesi = List[Tuple[str, str]]

def tokenize(kod: str) -> TokenListesi:
    """
    Kodu (tur, metin) çiftlerinden oluşan token listesine ayırır.

    Args:
        kod: PARS kaynak kodu

    Returns:
        List[Tuple[str, str]]: (tur, metin) çiftleri
        Türler: 'STR' | 'YORUM' | 'ISIM' | 'DIGER'
    """
    tokenlar: TokenListesi = []
    _tr_harf_kume = set(TR_HARF)

    for m in TOKEN_RE.finditer(kod):
        tok = m.group()
        ilk = tok[0]

        if ilk in ('"', "'"):
            tokenlar.append(('STR', tok))
        elif ilk == '#':
            tokenlar.append(('YORUM', tok))
        elif ilk.isalpha() or ilk in '_' or ilk in _tr_harf_kume:
            tokenlar.append(('ISIM', tok))
        else:
            tokenlar.append(('DIGER', tok))

    return tokenlar
```

---

## 7. ÇEVİRİCİ (pars/cekirdek/ceviri.py)

```python
"""
PARS Çevirici (Transpiler)
--------------------------
Türkçe PARS kodunu Python koduna çevirir.

Kurallar:
  - Satır numaraları korunur (hata mesajları için kritik)
  - String ve yorum içleri asla değiştirilmez
  - f-string'lerin {} bölümleri korunur
  - Türkçe değişken isimleri korunur (Python 3 Unicode desteği)
  - Hem Türkçe karakterli hem ASCII versiyonlar desteklenir
"""

from typing import Tuple
from .esleme import KELIME_ESLEME, PARS_ISTISNALAR
from .tokenizer import tokenize


def cevir(pars_kodu: str) -> str:
    """
    PARS kodunu Python koduna çevirir.

    Args:
        pars_kodu: Kaynak PARS kodu

    Returns:
        str: Python kodu (satır numaraları korunmuş)
    """
    tum_esleme = {**KELIME_ESLEME, **{k: v.__name__ for k, v in PARS_ISTISNALAR.items()}}
    tokenlar = tokenize(pars_kodu)

    parcalar = []
    for tur, metin in tokenlar:
        if tur in ('STR', 'YORUM'):
            parcalar.append(metin)
        elif tur == 'ISIM':
            parcalar.append(tum_esleme.get(metin, metin))
        else:
            parcalar.append(metin)

    return ''.join(parcalar)


def cevir_ve_goster(pars_kodu: str) -> str:
    """
    Türkçe ve Python karşılıklarını yan yana gösterir.
    CLI'nin -cevir komutu için kullanılır.
    """
    python_kodu = cevir(pars_kodu)
    tr_satirlar = pars_kodu.splitlines()
    py_satirlar = python_kodu.splitlines()

    en_uzun = max((len(s) for s in tr_satirlar), default=0)
    satirlar = []
    for i, (tr, py) in enumerate(zip(tr_satirlar, py_satirlar), 1):
        if tr.strip() != py.strip():
            satirlar.append(f'{i:4} │ {tr:<{en_uzun}}  →  {py}')
        else:
            satirlar.append(f'{i:4} │ {tr}')

    return '\n'.join(satirlar)


def syntax_kontrol(pars_kodu: str, dosya_adi: str = '<pars>') -> Tuple[bool, str]:
    """
    Kodu çevir ve Python sözdizimi kontrolü yap.

    Returns:
        Tuple[bool, str]: (geçerli_mi, hata_mesajı)
    """
    try:
        python_kodu = cevir(pars_kodu)
        compile(python_kodu, dosya_adi, 'exec')
        return True, ''
    except SyntaxError as e:
        return False, f'Satır {e.lineno}: {e.msg}'
```

---

## 8. HATA YÖNETİMİ (pars/cekirdek/hatalar.py)

Tüm Python hata türlerini Türkçe mesajlarla gösterir.
Stack trace sadece kullanıcı kodunu gösterir.
Yaygın hatalarda "İpucu" öneri mekanizması bulunur.

```python
"""
PARS Türkçe Hata Yönetimi
--------------------------
Özellikler:
  1. Her Python hata tipini Türkçe karşılığıyla göster
  2. Hatalı satırı PARS kaynak kodundan göster
  3. Yalnızca kullanıcı koduna ait stack frame'leri göster
  4. Yaygın hatalarda akıllı ipucu ver
  5. Renkli terminal çıktısı (ANSI)
"""

import sys
import traceback
from typing import Optional

HATA_TURLERI = {
    'SyntaxError':          '🔴 Sözdizimi Hatası',
    'NameError':            '🔴 Ad Hatası',
    'TypeError':            '🔴 Tür Hatası',
    'ValueError':           '🔴 Değer Hatası',
    'IndexError':           '🔴 İndeks Hatası',
    'KeyError':             '🔴 Anahtar Hatası',
    'AttributeError':       '🔴 Nitelik Hatası',
    'ImportError':          '🔴 İçe Aktarma Hatası',
    'ModuleNotFoundError':  '🔴 Modül Bulunamadı',
    'FileNotFoundError':    '🔴 Dosya Bulunamadı',
    'PermissionError':      '🔴 İzin Hatası',
    'ZeroDivisionError':    '🔴 Sıfıra Bölme Hatası',
    'OverflowError':        '🔴 Taşma Hatası',
    'MemoryError':          '🔴 Bellek Hatası',
    'RecursionError':       '🔴 Özyineleme Sınırı Aşıldı',
    'TimeoutError':         '🔴 Zaman Aşımı',
    'ConnectionError':      '🔴 Bağlantı Hatası',
    'OSError':              '🔴 İşletim Sistemi Hatası',
    'RuntimeError':         '🔴 Çalışma Zamanı Hatası',
    'NotImplementedError':  '🔴 Uygulanmadı Hatası',
    'AssertionError':       '🔴 İddia Hatası',
    'UnicodeDecodeError':   '🔴 Unicode Çözümleme Hatası',
    'UnicodeEncodeError':   '🔴 Unicode Kodlama Hatası',
    'StopIteration':        'ℹ️  İterasyon Bitti',
    'KeyboardInterrupt':    '⚠️  Kullanıcı Durdurdu',
    'SystemExit':           'ℹ️  Program Sonlandı',
    'Exception':            '🔴 Genel Hata',
}

HATA_IPUCLARI = {
    'is not defined':
        '💡 Değişkeni daha önce tanımladınız mı? Büyük/küçük harf farkına dikkat edin.',
    'is not callable':
        '💡 Bu değer bir fonksiyon değil. Parantezleri kaldırın.',
    'division by zero':
        '💡 Bir sayıyı sıfıra bölemezsiniz. Bölmeden önce kontrol edin.',
    'list index out of range':
        '💡 Liste indeksi sınır dışı. uzunluk() ile eleman sayısını kontrol edin.',
    'has no attribute':
        '💡 Bu nesnenin böyle bir özelliği yok. dir() ile özellikleri listeleyin.',
    'No module named':
        '💡 Modül yüklü değil. Şunu deneyin: pars paket yükle <modül_adı>',
    'takes':
        '💡 Fonksiyon yanlış sayıda argüman alıyor. Parametre sayısını kontrol edin.',
    'unsupported operand':
        '💡 Bu operatör bu veri tipleriyle kullanılamaz. tip() ile kontrol edin.',
    'cannot unpack':
        '💡 Çoklu atama için sağ taraftaki değer uygun değil.',
    'object is not iterable':
        '💡 Bu nesne üzerinde döngü kurulamaz. liste veya aralık kullanın.',
    'string indices must be integers':
        '💡 Yazı indeksleme tamsayı gerektirir.',
    'maximum recursion':
        '💡 Fonksiyon kendini çok derin çağırıyor. Taban durumu kontrol edin.',
    'global name':
        "💡 Global değişkeni fonksiyon içinde kullanmak için 'global değişken_adı' yazın.",
    'NoneType':
        "💡 'yok' (None) değeri üzerinde işlem yapılamaz. Değerin atanmış olduğundan emin olun.",
}

# ANSI renk kodları
KIRMIZI   = '\033[91m'
SARI      = '\033[93m'
YESIL     = '\033[92m'
MAVI      = '\033[94m'
MOR       = '\033[95m'
BEYAZ     = '\033[97m'
GRI       = '\033[90m'
SIFIRLA   = '\033[0m'
KALIN     = '\033[1m'


def _renkli(metin: str, renk: str) -> str:
    """Terminal renkli metin (Windows uyumlu)"""
    try:
        if sys.stderr.isatty() or sys.stdout.isatty():
            return f'{renk}{metin}{SIFIRLA}'
    except Exception:
        pass
    return metin


def hata_goster(exc: Exception, pars_kodu: str,
                dosya_adi: str = '<pars>') -> None:
    """
    Bir exception'ı Türkçe formatta stderr'e yazar.

    Args:
        exc:       Oluşan exception
        pars_kodu: Orijinal PARS kaynak kodu
        dosya_adi: Hata mesajında gösterilecek dosya adı
    """
    tur_adi = type(exc).__name__
    turkce_tur = HATA_TURLERI.get(tur_adi, f'🔴 {tur_adi}')
    satirlar = pars_kodu.splitlines()

    ayrac = _renkli('─' * 60, GRI)
    print(f'\n{ayrac}', file=sys.stderr)

    if isinstance(exc, SyntaxError):
        satir_no = exc.lineno or 0
        print(
            _renkli(f'{turkce_tur}', KIRMIZI) +
            _renkli(f'  (satır {satir_no})', GRI),
            file=sys.stderr
        )
        if 0 < satir_no <= len(satirlar):
            satir = satirlar[satir_no - 1]
            print(f'  {_renkli(satir.rstrip(), BEYAZ)}', file=sys.stderr)
            if exc.offset:
                isaret = ' ' * (exc.offset - 1) + '^'
                print(f'  {_renkli(isaret, SARI)}', file=sys.stderr)
        print(f'  {exc.msg}', file=sys.stderr)

    else:
        tb = traceback.extract_tb(exc.__traceback__)
        kullanici_kareleri = [f for f in tb if f.filename == dosya_adi]

        if kullanici_kareleri:
            son = kullanici_kareleri[-1]
            satir_no = son.lineno
            print(
                _renkli(f'{turkce_tur}', KIRMIZI) +
                _renkli(f'  (satır {satir_no})', GRI),
                file=sys.stderr
            )
            if 0 < satir_no <= len(satirlar):
                satir = satirlar[satir_no - 1]
                print(f'  {_renkli(satir.rstrip(), BEYAZ)}', file=sys.stderr)
        else:
            print(_renkli(f'{turkce_tur}', KIRMIZI), file=sys.stderr)

        print(f'  {_renkli(str(exc), GRI)}', file=sys.stderr)

        mesaj = str(exc).lower()
        for anahtar, ipucu in HATA_IPUCLARI.items():
            if anahtar in mesaj:
                print(f'\n{_renkli(ipucu, YESIL)}', file=sys.stderr)
                break

    print(f'{ayrac}\n', file=sys.stderr)
```

---

## 9. YÜRÜTÜCÜ (pars/cekirdek/yurutucu.py)

```python
"""
PARS Yürütücü
-------------
PARS kodunu çevirir, derler ve Python runtime ile çalıştırır.
Türkçe built-in'ler + standart kütüphane ad alanına eklenir.
"""

import sys
from typing import Optional
from .esleme import PARS_BUILTINS, PARS_ISTISNALAR
from .ceviri import cevir, cevir_ve_goster
from .hatalar import hata_goster


def ad_alani_olustur(dosya_adi: str = '<pars>') -> dict:
    """
    PARS programının çalışacağı Python ad alanını oluşturur.

    İçerir:
      - Tüm PARS built-in fonksiyonları
      - Türkçe istisna sınıfları
      - PARS standart kütüphane modülleri
      - Python __builtins__
    """
    alan = {
        '__name__':     '__main__',
        '__file__':     dosya_adi,
        '__builtins__': __builtins__,
        '__doc__':      None,
        'PARS_SURUM':   '1.0.0',
    }
    alan.update(PARS_BUILTINS)
    alan.update(PARS_ISTISNALAR)
    _standart_yukle(alan)
    return alan


def _standart_yukle(alan: dict) -> None:
    """PARS standart kütüphane modüllerini ad alanına ekler."""
    moduller = [
        ('matematik', 'pars.standart.matematik'),
        ('metin',     'pars.standart.metin'),
        ('liste',     'pars.standart.liste'),
        ('dosya',     'pars.standart.dosya'),
        ('zaman',     'pars.standart.zaman'),
        ('sistem',    'pars.standart.sistem'),
        ('rastgele',  'pars.standart.rastgele'),
        ('veri',      'pars.standart.veri'),
    ]
    for isim, yol in moduller:
        try:
            import importlib
            modul = importlib.import_module(yol)
            alan[isim] = modul
        except ImportError:
            pass


def calistir(pars_kodu: str,
             dosya_adi: str = '<pars>',
             python_goster: bool = False) -> bool:
    """
    PARS kodunu çalıştırır.

    Args:
        pars_kodu:    Kaynak kod metni
        dosya_adi:    Hata mesajlarında görünecek dosya adı
        python_goster: True ise üretilen Python kodunu da gösterir

    Returns:
        bool: True = başarılı, False = hata oluştu
    """
    try:
        python_kodu = cevir(pars_kodu)
    except Exception as e:
        print(f'❌  Çevirme hatası: {e}', file=sys.stderr)
        return False

    if python_goster:
        print('\n── Üretilen Python Kodu ' + '─' * 36)
        for i, satir in enumerate(python_kodu.splitlines(), 1):
            print(f'{i:4} │ {satir}')
        print('─' * 60 + '\n')

    alan = ad_alani_olustur(dosya_adi)

    try:
        derlenmiş = compile(python_kodu, dosya_adi, 'exec')
        exec(derlenmiş, alan)
        return True

    except SystemExit:
        return True

    except KeyboardInterrupt:
        print(
            '\n⚠️   Program kullanıcı tarafından durduruldu.',
            file=sys.stderr
        )
        return False

    except Exception as exc:
        hata_goster(exc, pars_kodu, dosya_adi)
        return False
```

---

## 10. REPL (pars/cekirdek/repl.py)

Tam özellikli etkileşimli konsol.

**Özellikler:**
- `code.compile_command()` ile eksik blok tespiti
- Çok satırlı giriş (fonksiyon, sınıf, döngü)
- `readline` ile ok tuşu geçmişi
- Sonuç değerleri otomatik yazdırılır
- Türkçe boolean/None gösterimi
- Özel REPL komutları:
  - `.yardım` → sözdizimi kılavuzu
  - `.çıkış` → çıkış
  - `.temiz` → ekran temizle
  - `.python` → son girişin Python karşılığını göster
  - `.değişkenler` → tanımlı değişkenleri listele
  - `.sürüm` → PARS versiyon bilgisi
  - `.geçmiş` → komut geçmişi

```python
PARS_SURUM = '1.0.0'

BANNER = f"""
╔══════════════════════════════════════════════════════════════╗
║    🐆  PARS  Türkçe Programlama Dili  v{PARS_SURUM}          ║
║    "Pars gibi hızlı. Türkçe gibi güzel."                   ║
║                                                             ║
║    Yardım için: .yardım    Çıkmak için: .çıkış             ║
╚══════════════════════════════════════════════════════════════╝
"""

YARDIM = """
┌─────────────────────────────────────────────────────────────────┐
│                   PARS — HIZLI BAŞVURU                         │
├──────────────────────┬──────────────────────────────────────────┤
│  eğer x > 0:         │  if x > 0:                              │
│  yoksa x == 0:       │  elif x == 0:                           │
│  değilse:            │  else:                                  │
│  iken x < 10:        │  while x < 10:                          │
│  için i içinde ...:  │  for i in ...:                          │
│  fonksiyon ad(...):  │  def ad(...):                           │
│  döndür sonuç        │  return sonuç                           │
│  sınıf Ad(Ana):      │  class Ad(Ana):                         │
│  içe_aktar numpy ... │  import numpy ...                       │
│  den_aktar x içe ... │  from x import ...                      │
│  dene: / hariç E:    │  try: / except E:                       │
│  ile f(...) olarak x │  with f(...) as x:                      │
│  yükselt Hata(...)   │  raise Exception(...)                   │
│  ve / veya / değil   │  and / or / not                        │
│  doğru / yanlış / yok│  True / False / None                   │
│  eşzamansız / bekle  │  async / await                         │
│  ver sonuç           │  yield sonuç                            │
├──────────────────────┼──────────────────────────────────────────┤
│  YERLEŞİK            │                                         │
│  yaz(...)            │  Ekrana yaz                             │
│  girdial(...)        │  Kullanıcıdan giriş al                  │
│  uzunluk(x)          │  Uzunluk                                │
│  aralık(n)           │  0'dan n-1'e tamsayılar                 │
│  tip(x)              │  Veri tipini göster                     │
│  tam_sayı(x)         │  Tamsayıya çevir                        │
│  ondalıklı(x)        │  Ondalıklıya çevir                      │
│  yazıya_çevir(x)     │  Yazıya çevir                           │
│  sırala(liste)       │  Sıralı kopya döndür                    │
│  paket_yükle("numpy")│  pip install numpy                      │
├──────────────────────┼──────────────────────────────────────────┤
│  REPL KOMUTLARI      │                                         │
│  .yardım             │  Bu ekranı göster                       │
│  .çıkış              │  Programı kapat                         │
│  .temiz              │  Ekranı temizle                         │
│  .python             │  Son girişin Python karşılığı           │
│  .değişkenler        │  Tanımlı değişkenleri listele           │
│  .sürüm              │  Versiyon bilgisi                       │
└──────────────────────┴──────────────────────────────────────────┘
"""
```

---

## 11. CLI (pars/cli/komutlar.py)

```
KULLANIM:
  pars <dosya.pars>                     → .pars dosyası çalıştır
  pars -g                              → Etkileşimli mod (REPL)
  pars -cevir <dosya.pars>              → Python karşılığını göster
  pars -p <dosya.pars>                  → Çalıştır + Python kodunu göster
  pars -kontrol <dosya.pars>            → Sözdizimi kontrolü (çalıştırma)
  pars -s / --surum                    → Versiyon bilgisi
  pars paket yükle <paket>             → pip install <paket>
  pars paket kaldır <paket>            → pip uninstall <paket>
  pars paket listele                   → pip list
  pars paket güncelle <paket>          → pip install --upgrade <paket>
  pars paket ara <paket>               → pip search <paket>
  pars yeni <proje_adı>                → Yeni proje iskeleti oluştur
  pars çalıştır <komut>                → Shell komutu çalıştır
```

`yeni` komutu aşağıdaki iskelet yapısını oluşturur:

```
proje_adi/
├── ana.pars          # Giriş noktası
├── kutuphane.pars    # Ortak fonksiyonlar
├── testler/
│   └── test_ana.pars
├── README.md
├── .gitignore
└── gereksinimler.txt
```

---

## 12. STANDART KÜTÜPHANE — TAM MODÜL LİSTESİ

Her modül `pars/standart/<isim>.py` dosyasına yazılır.
Her fonksiyon Türkçe isimli, docstring'li ve tip ipuçlu olacak.

### 12.1 matematik.py

```python
"""PARS Matematik Modülü — math kütüphanesi Türkçe sarmalayıcısı"""
import math, cmath, statistics

PI           = math.pi
E            = math.e
TAU          = math.tau
SONSUZ       = math.inf
NAN          = math.nan

# Temel
def kare_kok(x: float) -> float: ...
def us(taban: float, ust: float) -> float: ...
def mutlak(x: float) -> float: ...
def yuvarlak(x: float, basamak: int = 0) -> float: ...
def tavan(x: float) -> int: ...
def taban_al(x: float) -> int: ...
def mod(x: float, y: float) -> float: ...

# Trigonometri
def sinus(x: float) -> float: ...
def kosinus(x: float) -> float: ...
def tanjant(x: float) -> float: ...
def ark_sinus(x: float) -> float: ...
def ark_kosinus(x: float) -> float: ...
def ark_tanjant(x: float) -> float: ...
def ark_tanjant2(y: float, x: float) -> float: ...
def derece_radyan(d: float) -> float: ...
def radyan_derece(r: float) -> float: ...
def hipotenüs(*sayilar: float) -> float: ...

# Logaritma / Üs
def logaritma(x: float, taban: float = None) -> float: ...
def log10(x: float) -> float: ...
def log2(x: float) -> float: ...
def exp(x: float) -> float: ...

# Kombinatorik
def faktoriyel(n: int) -> int: ...
def kombinasyon(n: int, k: int) -> int: ...
def permütasyon(n: int, k: int = None) -> int: ...
def obeb(a: int, b: int) -> int: ...       # gcd
def okek(a: int, b: int) -> int: ...       # lcm

# İstatistik
def ortalama(sayilar) -> float: ...
def medyan(sayilar) -> float: ...
def mod_istatistik(sayilar): ...
def standart_sapma(sayilar) -> float: ...
def varyans(sayilar) -> float: ...
def kovaryans(x, y) -> float: ...
```

### 12.2 metin.py

```python
"""PARS Metin Modülü — str işlemleri Türkçe sarmalayıcısı"""

def büyük_harf(s: str) -> str: ...
def küçük_harf(s: str) -> str: ...
def baş_büyük(s: str) -> str: ...
def her_baş_büyük(s: str) -> str: ...
def boşluk_temizle(s: str, taraf: str = 'her') -> str: ...    # sol/sağ/her
def böl(s: str, ayraç: str = None, kez: int = -1) -> list: ...
def satırlara_böl(s: str) -> list: ...
def birleştir(ayraç: str, liste: list) -> str: ...
def değiştir(s: str, eski: str, yeni: str, kez: int = -1) -> str: ...
def içeriyor_mu(s: str, aranan: str) -> bool: ...
def ile_başlıyor_mu(s: str, önek: str) -> bool: ...
def ile_bitiyor_mu(s: str, sonek: str) -> bool: ...
def bul(s: str, aranan: str, baş: int = 0) -> int: ...
def bul_sağdan(s: str, aranan: str) -> int: ...
def say(s: str, aranan: str) -> int: ...
def tekrarla(s: str, n: int) -> str: ...
def tersine_çevir(s: str) -> str: ...
def doldur_sola(s: str, genişlik: int, doldurma: str = ' ') -> str: ...
def doldur_sağa(s: str, genişlik: int, doldurma: str = ' ') -> str: ...
def ortala(s: str, genişlik: int) -> str: ...
def sayı_mı(s: str) -> bool: ...
def harf_mi(s: str) -> bool: ...
def alfanümerik_mi(s: str) -> bool: ...
def boş_mu(s: str) -> bool: ...
def büyük_harf_mi(s: str) -> bool: ...
def küçük_harf_mi(s: str) -> bool: ...
def şifrele(s: str, kodlama: str = 'utf-8') -> bytes: ...
def çöz(b: bytes, kodlama: str = 'utf-8') -> str: ...
def regex_bul(metin: str, desen: str, tümü: bool = False): ...
def regex_değiştir(metin: str, desen: str, yeni: str) -> str: ...
def regex_böl(metin: str, desen: str) -> list: ...
```

### 12.3 liste.py

```python
"""PARS Liste Modülü — list/dict/set yardımcıları"""

# Liste işlemleri
def düzleştir(iç_içe_liste: list, derinlik: int = 1) -> list: ...
def tekil(liste: list) -> list: ...          # benzersiz elemanlar
def grupla(liste: list, n: int) -> list: ...  # n'li gruplar
def döndür(liste: list, n: int) -> list: ...  # döngüsel kaydır
def zip_ile_birleştir(*listeler) -> list: ...
def sırala_ters(liste: list) -> list: ...
def filtrele(fonk, liste: list) -> list: ...
def haritala(fonk, liste: list) -> list: ...
def azalt(fonk, liste, başlangıç=None): ...  # reduce
def bölüştür(liste: list, koşul) -> tuple: ... # (doğrular, yanlışlar)
def ortak_elemanlar(*listeler) -> list: ...
def fark(*listeler) -> list: ...
def birleşim(*listeler) -> list: ...

# Sözlük işlemleri
def anahtarlar(sözlük: dict) -> list: ...
def değerler(sözlük: dict) -> list: ...
def çiftler(sözlük: dict) -> list: ...
def sözlük_filtrele(sözlük: dict, koşul) -> dict: ...
def sözlük_harita(sözlük: dict, fonk) -> dict: ...
def sözlük_birleştir(*sözlükler) -> dict: ...
def tersle(sözlük: dict) -> dict: ...       # anahtar-değer yer değiştir
def varsayılan_sözlük(varsayılan) -> dict: ... # defaultdict
def sıralı_sözlük() -> dict: ...             # OrderedDict

# Yığın (Stack) ve Kuyruk (Queue) yardımcıları
def yığın_oluştur() -> list: ...
def yığına_ekle(yığın: list, eleman) -> None: ...
def yığından_al(yığın: list): ...
def kuyruk_oluştur(): ...
def kuyruğa_ekle(kuyruk, eleman) -> None: ...
def kuyruktan_al(kuyruk): ...
```

### 12.4 dosya.py

```python
"""PARS Dosya Modülü — pathlib + os Türkçe sarmalayıcısı"""
from pathlib import Path

def oku(yol: str, kodlama: str = 'utf-8') -> str: ...
def yaz(yol: str, içerik: str, kodlama: str = 'utf-8') -> None: ...
def ekle(yol: str, içerik: str, kodlama: str = 'utf-8') -> None: ...
def satırları_oku(yol: str) -> list: ...
def satırları_yaz(yol: str, satırlar: list) -> None: ...
def var_mı(yol: str) -> bool: ...
def klasör_mü(yol: str) -> bool: ...
def dosya_mı(yol: str) -> bool: ...
def sil(yol: str) -> None: ...
def taşı(kaynak: str, hedef: str) -> None: ...
def kopyala(kaynak: str, hedef: str) -> None: ...
def yeniden_adlandır(eski: str, yeni: str) -> None: ...
def klasör_oluştur(yol: str, aradakiler: bool = True) -> None: ...
def klasör_sil(yol: str) -> None: ...
def listele(yol: str = '.', desen: str = '*') -> list: ...
def boyut(yol: str) -> int: ...
def uzantı(yol: str) -> str: ...
def dosya_adı(yol: str) -> str: ...
def ana_klasör(yol: str) -> str: ...
def tam_yol(yol: str) -> str: ...
def geçici_dosya() -> str: ...
def geçici_klasör() -> str: ...

# JSON yardımcıları
def json_oku(yol: str) -> dict: ...
def json_yaz(yol: str, veri, girintili: bool = True) -> None: ...

# CSV yardımcıları
def csv_oku(yol: str, başlık: bool = True) -> list: ...
def csv_yaz(yol: str, veriler: list, başlık: list = None) -> None: ...
```

### 12.5 zaman.py

```python
"""PARS Zaman Modülü — datetime Türkçe sarmalayıcısı"""

TÜRKÇE_GÜNLER  = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
TÜRKÇE_AYLAR   = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran',
                   'Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

def şimdi(): ...
def bugün(): ...
def zaman_damgası() -> float: ...
def bekle(saniye: float) -> None: ...
def tarih(yıl, ay, gün): ...
def saat_oluştur(saat, dakika=0, saniye=0): ...
def fark(başlangıç, bitiş): ...
def biçimle(tarih, şablon: str = '%d.%m.%Y %H:%M:%S') -> str: ...
def çözümle(metin: str, şablon: str = '%d.%m.%Y'): ...
def gün_adı(tarih) -> str: ...
def ay_adı(tarih) -> str: ...
def yıl(tarih) -> int: ...
def ay(tarih) -> int: ...
def gün(tarih) -> int: ...
def saat(tarih_saat) -> int: ...
def dakika(tarih_saat) -> int: ...
def saniye(tarih_saat) -> int: ...
def iş_günü_mü(tarih) -> bool: ...
def hafta_sonu_mu(tarih) -> bool: ...
def gün_ekle(tarih, n: int): ...
def ay_ekle(tarih, n: int): ...
def geçti_mi(tarih) -> bool: ...
def kalan_süre(tarih) -> str: ...
```

### 12.6 sistem.py

```python
"""PARS Sistem Modülü — os/sys/platform Türkçe sarmalayıcısı"""

def ortam_değişkeni(isim: str, varsayılan: str = None) -> str: ...
def ortam_değişkeni_ata(isim: str, değer: str) -> None: ...
def çalışma_dizini() -> str: ...
def dizin_değiştir(yol: str) -> None: ...
def komut_çalıştır(komut: str) -> tuple: ...   # (çıktı, hata, kod)
def işlem_id() -> int: ...
def işlem_sonlandır(kod: int = 0) -> None: ...
def argümanlar() -> list: ...
def platform() -> str: ...
def işletim_sistemi() -> str: ...
def kullanıcı_adı() -> str: ...
def ev_dizini() -> str: ...
def cpu_sayısı() -> int: ...
def bellek_kullanımı() -> dict: ...
def python_sürümü() -> str: ...
def pars_sürümü() -> str: ...
```

### 12.7 rastgele.py

```python
"""PARS Rastgele Modülü — random/secrets Türkçe sarmalayıcısı"""

def rastgele_sayı(başlangıç: int, son: int) -> int: ...
def rastgele_ondalıklı(başlangıç: float = 0.0, son: float = 1.0) -> float: ...
def rastgele_seç(liste: list): ...
def rastgele_karıştır(liste: list) -> list: ...
def rastgele_örnek(liste: list, n: int) -> list: ...
def rastgele_ağırlıklı(liste: list, ağırlıklar: list): ...
def rastgele_metin(uzunluk: int = 16) -> str: ...   # secrets kullanır
def rastgele_id() -> str: ...                        # UUID4
def tohum_ata(tohum: int) -> None: ...
```

### 12.8 veri.py

```python
"""PARS Veri Modülü — json/csv/pickle Türkçe sarmalayıcısı"""

def json_metin(veri, girintili: bool = False) -> str: ...
def json_çözümle(metin: str) -> dict: ...
def json_oku(yol: str) -> dict: ...
def json_yaz(yol: str, veri) -> None: ...
def csv_oku(yol: str) -> list: ...
def csv_yaz(yol: str, veriler: list) -> None: ...
def kaydet(veri, yol: str) -> None: ...      # pickle dump
def yükle(yol: str): ...                      # pickle load
def base64_kodla(veri: bytes) -> str: ...
def base64_çöz(metin: str) -> bytes: ...
def hash_hesapla(metin: str, algoritma: str = 'sha256') -> str: ...
```

### 12.9 ag.py

```python
"""PARS Ağ Modülü — urllib/requests Türkçe sarmalayıcısı"""

def get(url: str, başlıklar: dict = None, zaman_aşımı: int = 30) -> dict: ...
def post(url: str, veri=None, json=None, başlıklar: dict = None) -> dict: ...
def put(url: str, veri=None, json=None) -> dict: ...
def sil_istek(url: str) -> dict: ...
def dosya_indir(url: str, yol: str) -> None: ...
def url_kodla(parametreler: dict) -> str: ...
def json_al(url: str) -> dict: ...
```

### 12.10 veritabani.py

```python
"""PARS Veritabanı Modülü — sqlite3 Türkçe sarmalayıcısı"""

sınıf Veritabani:
    fonksiyon __init__(öz, dosya: str = ':memory:'): ...
    fonksiyon bağlan(öz) -> None: ...
    fonksiyon kapat(öz) -> None: ...
    fonksiyon tablo_oluştur(öz, isim: str, sütunlar: dict) -> None: ...
    fonksiyon ekle(öz, tablo: str, veri: dict) -> int: ...
    fonksiyon bul(öz, tablo: str, koşul: str = None) -> list: ...
    fonksiyon güncelle(öz, tablo: str, veri: dict, koşul: str) -> None: ...
    fonksiyon sil(öz, tablo: str, koşul: str) -> None: ...
    fonksiyon sorgu(öz, sql: str, parametreler: tuple = ()) -> list: ...
    fonksiyon işlem_başlat(öz) -> None: ...
    fonksiyon işlem_kaydet(öz) -> None: ...
    fonksiyon işlem_geri_al(öz) -> None: ...
    fonksiyon tablo_listele(öz) -> list: ...
    fonksiyon tablo_sil(öz, isim: str) -> None: ...
```

---

## 13. ÖRNEK .pars DOSYALARI (TAM İÇERİK)

Aşağıdaki 20 örnek dosyanın tamamını eksiksiz yaz.

### ornekler/01_merhaba_dunya.pars
```python
# Merhaba Dünya — PARS'a hoş geldiniz!
yaz("Merhaba, Dünya! 🐆")
yaz("PARS — Pars gibi hızlı. Türkçe gibi güzel.")

isim = girdial("Adın ne? ")
yaş  = tam_sayı(girdial("Kaç yaşındasın? "))

yaz(f"Hoş geldin, {isim}! {yaş} yaşındasın.")

eğer yaş >= 18:
    yaz("Yetişkinsin.")
yoksa yaş >= 13:
    yaz("Genç birisin.")
değilse:
    yaz("Çocuksun.")
```

### ornekler/05_fonksiyonlar_ve_lambda.pars
```python
# Fonksiyonlar, lambda, *args, **kwargs, dekoratör

fonksiyon selamla(isim: str, ünvan: str = "Sayın") -> str:
    döndür f"{ünvan} {isim}, hoş geldiniz!"

fonksiyon faktöriyel(n: int) -> int:
    """Özyinelemeli faktöriyel"""
    eğer n <= 1:
        döndür 1
    döndür n * faktöriyel(n - 1)

fonksiyon fibonacci(n: int) -> liste:
    """Fibonacci dizisi"""
    eğer n <= 0:
        döndür []
    yoksa n == 1:
        döndür [0]
    dizi = [0, 1]
    için _ içinde aralık(n - 2):
        dizi.append(dizi[-1] + dizi[-2])
    döndür dizi

# *args ve **kwargs
fonksiyon toplam(*sayılar):
    döndür toplam_builtin(sayılar)

fonksiyon bilgi_göster(**bilgiler):
    için anahtar, değer içinde bilgiler.items():
        yaz(f"{anahtar}: {değer}")

# Lambda
kare  = lambda x: x ** 2
küp   = lambda x: x ** 3
çarp  = lambda x, y: x * y

# Yüksek dereceli fonksiyonlar
sayılar   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
çiftler   = liste(filtre(lambda x: x % 2 == 0, sayılar))
kareler   = liste(harita(lambda x: x ** 2, sayılar))

# Dekoratör
fonksiyon zamanlayıcı(f):
    içe_aktar zaman
    fonksiyon sarmalayıcı(*args, **kwargs):
        başlangıç = zaman.time()
        sonuç = f(*args, **kwargs)
        yaz(f"⏱  {f.__name__}: {zaman.time() - başlangıç:.6f}s")
        döndür sonuç
    döndür sarmalayıcı

@zamanlayıcı
fonksiyon yavaş_fonksiyon():
    içe_aktar zaman
    zaman.sleep(0.1)
    döndür "bitti"

yavaş_fonksiyon()
```

### ornekler/06_siniflar_ve_oop.pars
```python
# Sınıflar ve Nesne Yönelimli Programlama
# 'öz' kelimesi Python'daki 'self' yerine kullanılır

sınıf Hayvan:
    """Tüm hayvanlar için temel sınıf"""
    toplam_hayvan = 0

    fonksiyon __init__(öz, isim: str, yaş: int, ses: str):
        öz.isim = isim
        öz.yaş  = yaş
        öz.ses  = ses
        Hayvan.toplam_hayvan += 1

    fonksiyon konuş(öz) -> str:
        döndür f"{öz.isim}: {öz.ses}!"

    fonksiyon bilgi(öz) -> str:
        döndür f"{öz.isim} ({öz.yaş} yaş)"

    @sınıf_metot
    fonksiyon toplam(sınıf) -> int:
        döndür sınıf.toplam_hayvan

    @statik_metot
    fonksiyon hayvan_mı(nesne) -> bool:
        döndür türünden_mi(nesne, Hayvan)

    fonksiyon __repr__(öz) -> str:
        döndür f"Hayvan({öz.isim!r}, {öz.yaş})"

    fonksiyon __str__(öz) -> str:
        döndür öz.isim

    fonksiyon __eq__(öz, diğer) -> bool:
        döndür öz.isim == diğer.isim ve öz.yaş == diğer.yaş

# Kalıtım
sınıf Köpek(Hayvan):
    fonksiyon __init__(öz, isim: str, yaş: int, cins: str):
        süper().__init__(isim, yaş, "Hav hav")
        öz.cins = cins

    fonksiyon getir(öz, nesne: str) -> str:
        döndür f"{öz.isim} {nesne}i getirdi! 🐕"

sınıf Kedi(Hayvan):
    fonksiyon __init__(öz, isim: str, yaş: int):
        süper().__init__(isim, yaş, "Miyav")
        öz._uyku_sayısı = 0

    @özellik
    fonksiyon uyku_sayısı(öz) -> int:
        döndür öz._uyku_sayısı

    fonksiyon uyu(öz) -> str:
        öz._uyku_sayısı += 1
        döndür f"{öz.isim} uyuyor... ({öz._uyku_sayısı}. uyku)"

# Soyut sınıf
den_aktar abc içe_aktar ABC, abstractmethod

sınıf Şekil(ABC):
    @abstractmethod
    fonksiyon alan(öz) -> float: ...

    @abstractmethod
    fonksiyon çevre(öz) -> float: ...

    fonksiyon tanım(öz) -> str:
        döndür f"Alan: {öz.alan():.2f}, Çevre: {öz.çevre():.2f}"

sınıf Daire(Şekil):
    içe_aktar matematik
    fonksiyon __init__(öz, yarıçap: float):
        öz.yarıçap = yarıçap

    fonksiyon alan(öz) -> float:
        döndür matematik.pi * öz.yarıçap ** 2

    fonksiyon çevre(öz) -> float:
        döndür 2 * matematik.pi * öz.yarıçap

sınıf Dikdörtgen(Şekil):
    fonksiyon __init__(öz, uzunluk: float, genişlik: float):
        öz.uzunluk  = uzunluk
        öz.genişlik = genişlik

    fonksiyon alan(öz) -> float:
        döndür öz.uzunluk * öz.genişlik

    fonksiyon çevre(öz) -> float:
        döndür 2 * (öz.uzunluk + öz.genişlik)

# Test
köpek = Köpek("Karabaş", 3, "Labrador")
kedi  = Kedi("Tekir", 5)

yaz(köpek.konuş())
yaz(kedi.uyu())
yaz(köpek.getir("topu"))

şekiller = [Daire(5), Dikdörtgen(4, 6), Daire(3)]
için şekil içinde şekiller:
    yaz(şekil.tanım())

yaz(f"Toplam hayvan: {Hayvan.toplam()}")
```

### ornekler/12_async_await.pars
```python
# Async / Await — Eşzamansız programlama
içe_aktar asyncio

eşzamansız fonksiyon veri_getir(url: str) -> str:
    """Simüle edilmiş ağ isteği"""
    bekle asyncio.sleep(1)
    döndür f"Veri: {url}"

eşzamansız fonksiyon paralel_getir():
    """Birden fazla isteği eş zamanlı çalıştır"""
    görevler = [
        veri_getir("https://api.ornek.com/1"),
        veri_getir("https://api.ornek.com/2"),
        veri_getir("https://api.ornek.com/3"),
    ]
    sonuçlar = bekle asyncio.gather(*görevler)
    için sonuç içinde sonuçlar:
        yaz(sonuç)

eşzamansız fonksiyon ana():
    yaz("Paralel istekler başlıyor...")
    bekle paralel_getir()
    yaz("Tamamlandı!")

asyncio.run(ana())
```

### ornekler/16_numpy_ve_pandas.pars
```python
# NumPy ve Pandas ile PARS
# Önce: pars paket yükle numpy pandas

dene:
    içe_aktar numpy olarak np
    içe_aktar pandas olarak pd

    # NumPy
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    yaz("NumPy Dizisi:", a)
    yaz("Toplam:", a + b)
    yaz("Ortalama:", np.mean(a))
    yaz("Standart Sapma:", np.std(a))

    matris = np.random.randint(1, 10, size=(3, 3))
    yaz("Matris:\n", matris)
    yaz("Transpozu:\n", matris.T)
    yaz("Determinant:", round(np.linalg.det(matris), 2))

    # Pandas
    veriler = {
        "isim":  ["Ahmet", "Ayşe", "Mehmet", "Fatma"],
        "yaş":   [25, 30, 22, 28],
        "şehir": ["İstanbul", "Ankara", "İzmir", "Bursa"],
        "maaş":  [5000, 7000, 4500, 6000],
    }
    df = pd.DataFrame(veriler)

    yaz("\nVeri Çerçevesi:")
    yaz(df)
    yaz(f"\nOrtalama maaş: {df['maaş'].mean():.0f} TL")
    yaz(f"En yaşlı: {df.loc[df['yaş'].idxmax(), 'isim']}")
    yaz("\nŞehirlere göre ortalama maaş:")
    yaz(df.groupby('şehir')['maaş'].mean())

hariç ImportError olarak e:
    yaz(f"Modül eksik: {e}")
    yaz("Şunu çalıştırın: pars paket yükle numpy pandas")
```

### ornekler/17_flask_web_uygulamasi.pars
```python
# Flask Web Uygulaması
# Önce: pars paket yükle flask

dene:
    den_aktar flask içe_aktar Flask, jsonify, request, render_template_string

    uygulama = Flask(__name__)

    ANA_SAYFA = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>PARS Web Uygulaması</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 50px auto; }
            .pars { color: #EF9F27; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🐆 <span class="pars">PARS</span> ile Flask!</h1>
        <p>Türkçe programlama dili ile web uygulaması.</p>
        <ul>
            <li><a href="/api/merhaba/Dünya">GET /api/merhaba/Dünya</a></li>
            <li><a href="/api/hesapla?a=5&b=3">GET /api/hesapla?a=5&b=3</a></li>
        </ul>
    </body>
    </html>
    """

    @uygulama.route('/')
    fonksiyon ana_sayfa():
        döndür render_template_string(ANA_SAYFA)

    @uygulama.route('/api/merhaba/<isim>')
    fonksiyon merhaba(isim):
        döndür jsonify({
            "mesaj":   f"Merhaba, {isim}! 🐆",
            "dil":     "PARS",
            "durum":   "başarılı",
        })

    @uygulama.route('/api/hesapla')
    fonksiyon hesapla():
        a = ondalıklı(request.args.get('a', 0))
        b = ondalıklı(request.args.get('b', 0))
        döndür jsonify({
            "a":       a,
            "b":       b,
            "toplam":  a + b,
            "çarpım":  a * b,
        })

    @uygulama.route('/api/kullanicilar', methods=['GET', 'POST'])
    fonksiyon kullanicilar():
        eğer request.method == 'GET':
            döndür jsonify({"kullanicilar": []})
        veri = request.get_json()
        döndür jsonify({"oluşturulan": veri}), 201

    eğer __name__ == '__main__':
        yaz("🌐 Sunucu: http://localhost:5000")
        uygulama.run(debug=doğru, port=5000)

hariç ImportError:
    yaz("Flask kurulu değil.")
    yaz("Şunu çalıştırın: pars paket yükle flask")
```

### ornekler/20_tam_proje_ornegi.pars

Kütüphane yönetim sistemi — tam uçtan uca uygulama:
- `Kitap`, `Üye`, `Kütüphane` sınıfları
- SQLite veritabanı entegrasyonu (pars.standart.veritabani)
- Kitap ekleme, üye kayıt, ödünç verme, iade alma
- Komut satırı menüsü
- Hata yönetimi
- Raporlama

Bu örnek tamamen çalışır halde yazılmalı ve minimum 100 satır olmalı.

---

## 14. TEST DOSYALARI (TAM KAPSAM)

### testler/test_ceviri.py — Zorunlu test senaryoları

```python
"""
Çevirici birim testleri.
Her test izole ve bağımsız olmalı.
"""

import pytest
from pars.cekirdek.ceviri import cevir, syntax_kontrol

class TestTemelCeviri:

    def test_eger_cevirisi(self):
        assert cevir("eğer x > 0:") == "if x > 0:"

    def test_eger_ascii_cevirisi(self):
        assert cevir("eger x > 0:") == "if x > 0:"

    def test_degilse_cevirisi(self):
        assert cevir("değilse:") == "else:"

    def test_yoksa_cevirisi(self):
        assert cevir("yoksa x == 0:") == "elif x == 0:"

    def test_iken_cevirisi(self):
        assert cevir("iken x < 10:") == "while x < 10:"

    def test_icin_cevirisi(self):
        assert cevir("için i içinde aralık(10):") == "for i in range(10):"

    def test_fonksiyon_cevirisi(self):
        assert cevir("fonksiyon ad():") == "def ad():"

    def test_dondur_cevirisi(self):
        assert cevir("döndür sonuç") == "return sonuç"

    def test_sinif_cevirisi(self):
        assert cevir("sınıf Ad:") == "class Ad:"

    def test_iceaktar_cevirisi(self):
        assert cevir("içe_aktar numpy olarak np") == "import numpy as np"

    def test_dogru_cevirisi(self):
        assert cevir("doğru") == "True"

    def test_yanlis_cevirisi(self):
        assert cevir("yanlış") == "False"

    def test_yok_cevirisi(self):
        assert cevir("yok") == "None"

    def test_ve_cevirisi(self):
        assert cevir("x ve y") == "x and y"

    def test_veya_cevirisi(self):
        assert cevir("x veya y") == "x or y"

    def test_degil_cevirisi(self):
        assert cevir("değil x") == "not x"


class TestStringKoruma:

    def test_string_icinde_degismez_cift_tirnak(self):
        assert cevir('"eğer bu değişmemeli"') == '"eğer bu değişmemeli"'

    def test_string_icinde_degismez_tek_tirnak(self):
        assert cevir("'için iken değilse'") == "'için iken değilse'"

    def test_uclu_string_korunur(self):
        kod = '"""eğer yoksa değilse"""'
        assert cevir(kod) == kod

    def test_fstring_ic_kisim_korunur(self):
        assert cevir('f"Merhaba {isim}"') == 'f"Merhaba {isim}"'

    def test_yorum_satiri_korunur(self):
        assert cevir("# eğer bu yorum değilse") == "# eğer bu yorum değilse"


class TestTurkceKarakter:

    def test_turkce_degisken_korunur(self):
        assert cevir("yaş = 25") == "yaş = 25"

    def test_turkce_fonksiyon_ismi_korunur(self):
        assert cevir("fonksiyon selamla():") == "def selamla():"

    def test_oz_korunur(self):
        assert cevir("fonksiyon __init__(öz):") == "def __init__(öz):"

    def test_unicode_donusum_gerekmez(self):
        # Python 3 Unicode tanımlayıcıları destekler
        kod = "öğrenci_adı = 'Ahmet'"
        assert cevir(kod) == kod


class TestCokSatirli:

    def test_if_else_blok(self):
        kod = "eğer x > 0:\n    yaz('pozitif')\ndeğilse:\n    yaz('negatif')"
        beklenen = "if x > 0:\n    yaz('pozitif')\nelse:\n    yaz('negatif')"
        assert cevir(kod) == beklenen

    def test_satir_numaralari_korunur(self):
        kod = "x = 1\neğer x:\n    yaz(x)"
        python = cevir(kod)
        assert python.count('\n') == kod.count('\n')


class TestSyntaxKontrol:

    def test_gecerli_kod(self):
        gecerli, _ = syntax_kontrol("yaz('merhaba')")
        assert gecerli is True

    def test_gecersiz_kod(self):
        gecerli, hata = syntax_kontrol("eğer:")
        assert gecerli is False
        assert hata != ''
```

### testler/test_yurutucu.py — Zorunlu test senaryoları

```python
import pytest
from unittest.mock import patch
from io import StringIO
from pars.cekirdek.yurutucu import calistir

class TestTemelCalistirma:

    def test_basit_yaz(self, capsys):
        assert calistir("yaz('merhaba')") is True
        çıktı = capsys.readouterr().out
        assert 'merhaba' in çıktı

    def test_dogru_degeri_turkce(self, capsys):
        calistir("yaz(doğru)")
        çıktı = capsys.readouterr().out
        assert 'doğru' in çıktı

    def test_yanlis_degeri_turkce(self, capsys):
        calistir("yaz(yanlış)")
        çıktı = capsys.readouterr().out
        assert 'yanlış' in çıktı

    def test_yok_degeri_turkce(self, capsys):
        calistir("yaz(yok)")
        çıktı = capsys.readouterr().out
        assert 'yok' in çıktı

    def test_degisken_atama(self):
        assert calistir("x = 5\nassert x == 5") is True

    def test_turkce_degisken(self):
        assert calistir("yaş = 25\nassert yaş == 25") is True

    def test_kosul(self, capsys):
        calistir("eğer 1 > 0:\n    yaz('doğru')")
        assert 'doğru' in capsys.readouterr().out

    def test_dongu(self, capsys):
        calistir("için i içinde aralık(3):\n    yaz(i)")
        çıktı = capsys.readouterr().out
        assert '0' in çıktı and '1' in çıktı and '2' in çıktı

    def test_fonksiyon_tanim_ve_cagri(self, capsys):
        calistir("fonksiyon selamla(isim):\n    yaz(f'Merhaba {isim}')\nselamla('PARS')")
        assert 'Merhaba PARS' in capsys.readouterr().out

    def test_sinif_tanimlama(self):
        kod = """
sınıf Araba:
    fonksiyon __init__(öz, marka):
        öz.marka = marka
araba = Araba("Toyota")
assert araba.marka == "Toyota"
"""
        assert calistir(kod) is True

    def test_hata_yonetimi(self):
        # Runtime hata False döndürmeli
        assert calistir("1/0") is False

    def test_syntax_hatasi(self):
        assert calistir("eğer:") is False

    def test_iceaktar(self):
        assert calistir("içe_aktar os\nassert os.getcwd()") is True

    def test_numpy_iceaktar(self):
        pytest.importorskip("numpy")
        assert calistir("içe_aktar numpy olarak np\nassert np.__version__") is True
```

### testler/test_ornekler.py — Tüm .pars örneklerini çalıştır

```python
"""
Ornekler klasöründeki tüm .pars dosyalarını çalıştırır.
Hata veren dosya testi başarısız sayar.
"""
import pytest
from pathlib import Path
from pars.cekirdek.yurutucu import calistir
from unittest.mock import patch

ORNEKLER_DIZIN = Path(__file__).parent.parent / 'ornekler'

def ornek_dosyalari():
    return list(ORNEKLER_DIZIN.glob('*.pars'))

@pytest.mark.parametrize('dosya', ornek_dosyalari(),
                         ids=lambda d: d.name)
def test_ornek_calisir(dosya, monkeypatch, capsys):
    # girdial çağrılarını mockla
    monkeypatch.setattr('builtins.input', lambda *a, **k: 'test_girdisi')
    # Flask, asyncio gibi blocking çağrıları engelle
    with patch('time.sleep'):
        kod = dosya.read_text(encoding='utf-8')
        # Import hataları (numpy yok vb.) başarısız sayılmaz
        # Gerçek PARS hataları başarısız sayılır
        sonuc = calistir(kod, dosya_adi=str(dosya))
        # ModuleNotFoundError hariç tüm hatalar başarısız
```

---

## 15. VS CODE EKLENTİSİ

`vscode-uzantisi/` klasörü tam çalışır VS Code dil eklentisi içerir.

### vscode-uzantisi/syntaxes/pars.tmLanguage.json

`.pars` dosyaları için TextMate dil grameri tanımı.
Renklendirme kapsamı:

- **Anahtar kelimeler:** `eğer`, `değilse`, `yoksa`, `iken`, `için`, `içinde`, `fonksiyon`, `döndür`, `sınıf`, `dene`, `hariç`, `sonunda`, `yükselt`, `ile`, `olarak`, `geç`, `kes`, `devam`, `sil`, `ver`, `bekle`, `eşzamansız`, `içe_aktar`, `den_aktar`, `global`, `yerel_değil`, `iddia`, `lambda`
- **Değerler:** `doğru`, `yanlış`, `yok`
- **Mantıksal:** `ve`, `veya`, `değil`
- **Sayılar:** tam sayı ve ondalıklı
- **Yazılar:** tek tırnak, çift tırnak, üçlü tırnak, f-string
- **Yorumlar:** `#` ile başlayan satırlar
- **Yerleşik fonksiyonlar:** `yaz`, `girdial`, `uzunluk`, `tip`, `aralık`, `sırala` vb.
- **Öz:** `öz` — farklı renk (self gibi)

### vscode-uzantisi/language-configuration.json

- Yorum: `#`
- Parantez çiftleri: `()`, `[]`, `{}`
- String çiftleri: `""`, `''`
- Otomatik tamamlama parantezleri
- Girinti artırma: `:` ile biten satırlardan sonra

### vscode-uzantisi/package.json

```json
{
  "name": "pars-dil",
  "displayName": "PARS — Türkçe Programlama Dili",
  "description": "PARS dili sözdizimi renklendirme ve dil desteği",
  "version": "1.0.0",
  "publisher": "pars-lang",
  "engines": { "vscode": "^1.70.0" },
  "categories": ["Programming Languages"],
  "contributes": {
    "languages": [{
      "id": "pars",
      "aliases": ["PARS", "pars"],
      "extensions": [".pars"],
      "configuration": "./language-configuration.json"
    }],
    "grammars": [{
      "language": "pars",
      "scopeName": "source.pars",
      "path": "./syntaxes/pars.tmLanguage.json"
    }]
  }
}
```

---

## 16. CI / CD — GitHub Actions

### .github/workflows/test.yml

Her `push` ve `pull_request`'te çalışır:
- Python 3.8, 3.9, 3.10, 3.11, 3.12 matris testi
- Ubuntu, macOS, Windows üzerinde
- `pip install -e ".[dev]"` kurulum
- `pytest testler/ --cov=pars --cov-report=xml -v`
- Kapsam raporu Codecov'a yüklenir
- Linting: `flake8 pars/ --max-line-length=100`
- Tip kontrolü: `mypy pars/`

### .github/workflows/yayin.yml

Sadece `v*` etiketlerinde tetiklenir (örn: `v1.0.0`):
- `python -m build` ile paket derleme
- `twine upload dist/*` ile PyPI yayını
- GitHub Release oluşturma
- CHANGELOG.md içeriğini Release notlarına ekleme

### .github/workflows/docs.yml

`main` branch'e her push'ta:
- `mkdocs build` ile statik site oluşturma
- `mkdocs gh-deploy` ile GitHub Pages yayını

---

## 17. pyproject.toml (TAM)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "pars-dil"
version = "1.0.0"
description = "PARS — Türkçe Programlama Dili. Pars gibi hızlı. Türkçe gibi güzel."
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.8"
keywords = ["türkçe", "programlama", "dil", "pars", "turkish", "programming", "language"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: Turkish",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Compilers",
    "Topic :: Software Development :: Interpreters",
]

[project.scripts]
pars = "pars.cli.komutlar:main"

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "flake8>=6.0",
    "mypy>=1.0",
    "black>=23.0",
    "isort>=5.0",
    "mkdocs-material>=9.0",
    "twine>=4.0",
    "build>=0.10",
]

[tool.pytest.ini_options]
testpaths = ["testler"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true

[tool.black]
line-length = 100
target-version = ["py38"]
```

---

## 18. README.md (ANA — TR + EN)

```markdown
<div align="center">

# 🐆 PARS

**Türkçe Programlama Dili**

*"Pars gibi hızlı. Türkçe gibi güzel."*

[![PyPI](https://img.shields.io/pypi/v/pars-dil.svg)](https://pypi.org/project/pars-dil/)
[![Python](https://img.shields.io/pypi/pyversions/pars-dil.svg)](https://pypi.org/project/pars-dil/)
[![Lisans](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)
[![Testler](https://github.com/pars-lang/pars/actions/workflows/test.yml/badge.svg)](...)

</div>

## PARS nedir?

PARS, Python altyapısını kullanan, tamamen Türkçe sözdizimli bir programlama dilidir.
Python'un tüm gücünü Türkçe ile yazabilirsiniz.

## Kurulum

```bash
pip install pars-dil
```

## İlk Program

```pars
# merhaba.pars
yaz("Merhaba, Dünya! 🐆")

isim = girdial("Adın ne? ")
yaz(f"Hoş geldin, {isim}!")
```

```bash
pars merhaba.pars
```

## Sözdizimi Karşılaştırması

| PARS | Python |
|---|---|
| `eğer x > 0:` | `if x > 0:` |
| `değilse:` | `else:` |
| `yoksa x == 0:` | `elif x == 0:` |
| `için i içinde aralık(10):` | `for i in range(10):` |
| `iken x < 5:` | `while x < 5:` |
| `fonksiyon topla(a, b):` | `def topla(a, b):` |
| `döndür sonuç` | `return sonuç` |
| `sınıf Araba:` | `class Araba:` |
| `içe_aktar numpy olarak np` | `import numpy as np` |
| `dene: / hariç Hata:` | `try: / except Exception:` |
| `doğru / yanlış / yok` | `True / False / None` |
| `ve / veya / değil` | `and / or / not` |

## Python Kütüphaneleri

PARS, tüm Python kütüphanelerini destekler:

```pars
içe_aktar numpy olarak np
içe_aktar pandas olarak pd
den_aktar flask içe_aktar Flask

a = np.array([1, 2, 3])
yaz(np.mean(a))
```

## Paket Yönetimi

```bash
pars paket yükle numpy pandas flask
pars paket listele
pars paket kaldır eski-paket
```

## CLI

```bash
pars dosya.pars          # Çalıştır
pars -g                  # Etkileşimli mod
pars -cevir dosya.pars   # Python karşılığını göster
pars -kontrol dosya.pars # Sözdizimi kontrolü
pars yeni projem         # Yeni proje oluştur
```

## Lisans

MIT — Özgürce kullanın, değiştirin, dağıtın.
```

---

## 19. MkDocs DOKÜMANTASYON SİTESİ

### website/mkdocs.yml

```yaml
site_name: PARS — Türkçe Programlama Dili
site_url: https://parsdil.com
site_description: Pars gibi hızlı. Türkçe gibi güzel.
repo_url: https://github.com/pars-lang/pars
repo_name: pars-lang/pars

theme:
  name: material
  language: tr
  palette:
    - scheme: default
      primary: custom
      accent: custom
  features:
    - navigation.tabs
    - navigation.sections
    - content.code.copy
    - search.highlight

extra_css:
  - stylesheets/pars.css

nav:
  - Ana Sayfa: index.md
  - Başlangıç:
      - Kurulum: baslangic/kurulum.md
      - İlk Program: baslangic/ilk_program.md
      - Hızlı Başlangıç: baslangic/hizli_baslangic.md
  - Sözdizimi:
      - Değişkenler ve Tipler: sozdizimi/degiskenler.md
      - Koşullar: sozdizimi/kosullar.md
      - Döngüler: sozdizimi/donguler.md
      - Fonksiyonlar: sozdizimi/fonksiyonlar.md
      - Sınıflar: sozdizimi/siniflar.md
      - İstisna Yönetimi: sozdizimi/istisnalar.md
      - Modüller: sozdizimi/moduller.md
      - Async/Await: sozdizimi/async.md
  - Yerleşik Fonksiyonlar: referans/builtins.md
  - Standart Kütüphane:
      - matematik: standart/matematik.md
      - metin: standart/metin.md
      - liste: standart/liste.md
      - dosya: standart/dosya.md
      - zaman: standart/zaman.md
      - sistem: standart/sistem.md
      - rastgele: standart/rastgele.md
      - veri: standart/veri.md
      - ag: standart/ag.md
      - veritabani: standart/veritabani.md
  - Python Kütüphaneleri:
      - NumPy: kutuphane/numpy.md
      - Pandas: kutuphane/pandas.md
      - Flask: kutuphane/flask.md
      - Requests: kutuphane/requests.md
  - CLI Referansı: referans/cli.md
  - Örnekler: ornekler/index.md
  - Katkı: katki.md
```

---

## 20. KALİTE GEREKSİNİMLERİ (ZORUNLU)

### Kod Kalitesi
- Her `fonksiyon` ve `sınıf` için Türkçe docstring zorunlu
- Tüm fonksiyonlarda `typing` modülü ile tip ipuçları
- Maksimum satır uzunluğu: 100 karakter
- PEP 8 uyumlu (Türkçe tanımlayıcılar hariç)
- `black` ile otomatik biçimlendirme uyumlu
- `flake8` ile linting uyarısı sıfır
- `mypy` ile tip hatası sıfır
- Her modülde `__all__` tanımlı

### Test Kapsamı
- Birim test kapsamı minimum **%90**
- Tokenizer: tüm token türleri test edilmiş
- Çevirici: her anahtar kelime için en az 2 test (Türkçe + ASCII)
- String koruma: 10+ test senaryosu
- Hata yönetimi: her hata tipi için test
- Tüm örnek `.pars` dosyaları çalıştırma testi

### Güvenlik
- `exec()` namespace'i izole — dışarıya sızma yok
- Kullanıcı kodundan sistem komutlarına doğrudan erişim yok
- `__builtins__` yalnızca güvenli alt kümesi açık
- Dosya yolu traversal koruması

### Performans
- Tokenizer regex'i modül yüklenirken bir kez `compile()` edilir
- `KELIME_ESLEME` dict araması O(1)
- Büyük `.pars` dosyaları için satır satır okuma (chunk)
- REPL her girişte tokenizer'ı yeniden derlemiyor

### Hata Mesajları
- Tüm Python exception tipleri Türkçe karşılıkları var
- Hatalı satır her zaman gösteriliyor
- Yaygın hatalarda akıllı ipucu veriliyor
- Stack trace sadece kullanıcı kodunu gösteriyor
- ANSI renk kodları kullanılıyor (Windows uyumlu kontrol ile)

---

## 21. SON KONTROL LİSTESİ

Projeyi teslim etmeden önce her madde tıklanmalı:

### Temel İşlevsellik
- [ ] `pip install -e .` hatasız çalışıyor
- [ ] `pars ornekler/01_merhaba_dunya.pars` çalışıyor
- [ ] `pars -g` REPL açılıyor ve `.yardım` komutu çalışıyor
- [ ] `pars -cevir dosya.pars` Python kodunu gösteriyor
- [ ] `pars -kontrol dosya.pars` sözdizimi hatası varsa buluyor
- [ ] `pars paket yükle requests` çalışıyor
- [ ] `pars yeni benim_projem` iskelet oluşturuyor

### Dil Özellikleri
- [ ] Türkçe değişken isimleri çalışıyor (`yaş = 25`)
- [ ] `öz` parametresi sınıflarda çalışıyor
- [ ] `içe_aktar numpy olarak np` çalışıyor
- [ ] `den_aktar flask içe_aktar Flask` çalışıyor
- [ ] `eşzamansız / bekle` çalışıyor
- [ ] `dene / hariç / sonunda` çalışıyor
- [ ] `ile ... olarak ...:` (context manager) çalışıyor
- [ ] `ver` (yield) ile üretec çalışıyor
- [ ] `@` ile dekoratör çalışıyor
- [ ] Liste kavrayışı (list comprehension) çalışıyor
- [ ] f-string içindeki değişkenler bozulmuyor
- [ ] Üçlü tırnak string'leri korunuyor
- [ ] Yorum satırları korunuyor

### Hata Yönetimi
- [ ] Sözdizimi hatası Türkçe gösteriliyor
- [ ] Runtime hatası Türkçe gösteriliyor
- [ ] Hatalı satır kaynak koddan gösteriliyor
- [ ] `NameError` için ipucu veriliyor
- [ ] `ZeroDivisionError` için ipucu veriliyor
- [ ] `ModuleNotFoundError` için `pars paket yükle` önerisi veriliyor

### Testler
- [ ] `pytest testler/` tüm testler geçiyor
- [ ] Test kapsamı %90 üzerinde
- [ ] `flake8 pars/` sıfır uyarı
- [ ] `mypy pars/` sıfır hata
- [ ] Tüm 20 örnek dosyası hatasız çalışıyor

### Dokümantasyon
- [ ] README.md eksiksiz (TR + EN)
- [ ] Her modülün docstring'i var
- [ ] `dokuman/SOZDIZIMI_REHBERI.md` eksiksiz
- [ ] `dokuman/BUILTIN_FONKSIYONLAR.md` eksiksiz
- [ ] `mkdocs build` hatasız çalışıyor

### Paket
- [ ] `python -m build` başarılı
- [ ] `twine check dist/*` uyarı sıfır
- [ ] `pyproject.toml` eksiksiz
- [ ] `MANIFEST.in` doğru dosyaları dahil ediyor
- [ ] VS Code eklentisi `.pars` dosyalarını renklendirir

---

## 22. YAPILMAYACAKLAR (KESİN YASAK)

- Her şeyi tek dosyaya sıkıştırma
- Python kütüphanelerini yeniden yazma
- Kendi AST/interpreter motoru (transpiler yeterli ve daha iyi)
- Gereksiz bağımlılık ekleme (`requirements.txt` olabildiğince boş)
- Hata mesajlarını İngilizce bırakma
- Test yazmayı atlama
- Docstring'leri boş bırakma
- Tip ipuçlarını atlatma
- `exec()` ile güvensiz kod çalıştırma
- String içindeki Türkçe kelimeleri değiştirme
- Yorum satırlarını değiştirme
- Satır numaralarını kaydırma

---

**BAŞLAYINIZ.**

Her dosyayı tam, çalışır ve test edilmiş halde yaz.
Eksik bırakılan her dosya veya yarım uygulama kabul edilmez.
Kod kalitesi PyPI'ye yayınlanmaya hazır seviyede olacak.