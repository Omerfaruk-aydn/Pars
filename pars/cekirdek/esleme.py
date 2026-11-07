"""
PARS Anahtar Kelime ve Yerleşik Fonksiyon Eşlemeleri
-----------------------------------------------------
Türkçe anahtar kelimelerin Python karşılıkları.
Hem Türkçe karakterli hem ASCII versiyonlar desteklenir.
"""

from typing import Any, Dict
import asyncio

# ── ANAHTAR KELİME EŞLEMESİ ─────────────────────────────────────────────

KELIME_ESLEME: Dict[str, str] = {

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
    'icindedir':        'in',
    # NOT: 'dir' bilerek eşlenmez; dir() yerleşik fonksiyonu ile çakışıyordu.
    'dır':              'is',
    'özdeş':            'is',
    'ozdes':            'is',

    # ── ÜST SINIF ─────────────────────────────────────────────────────────
    # ÖNEMLİ: süper mutlaka 'super'e çevrilmeli. Aksi halde sıfır argümanlı
    # super() çağrısı için derleyici __class__ hücresi oluşturmaz ve
    # "super(): __class__ cell not found" hatası alınır.
    'süper':            'super',
    'super':            'super',

    # ── DEĞERLER ──────────────────────────────────────────────────────────
    'doğru':            'True',
    'dogru':            'True',
    'yanlış':           'False',
    'yanlis':           'False',
    'yok':              'None',
}


# ── YERLEŞİK FONKSİYONLAR ────────────────────────────────────────────────

def _yaz(*args: Any, sep: str = ' ', son: str = '\n',
         dosya: Any = None, temizle: bool = False,
         ayraç: Any = None, **kwargs: Any) -> None:
    """
    Türkçe print.

    True  → doğru
    False → yanlış
    None  → yok
    Liste → [eleman1, eleman2, ...]

    Türkçe parametre adları da kabul edilir:
        yaz("a", "b", ayraç="-")
    """
    import sys

    if ayraç is not None:
        sep = ayraç

    def _goster(v: Any) -> str:
        if v is True:
            return 'doğru'
        if v is False:
            return 'yanlış'
        if v is None:
            return 'yok'
        if isinstance(v, list):
            return '[' + ', '.join(_goster(i) for i in v) + ']'
        if isinstance(v, dict):
            return '{' + ', '.join(
                f'{_goster(k)}: {_goster(val)}' for k, val in v.items()
            ) + '}'
        if isinstance(v, tuple):
            return '(' + ', '.join(_goster(i) for i in v) + ')'
        if isinstance(v, set):
            return '{' + ', '.join(_goster(i) for i in v) + '}'
        return str(v)

    print(*[_goster(a) for a in args],
          sep=sep, end=son,
          file=dosya or sys.stdout,
          flush=temizle)


def _girdial(istem: str = '') -> str:
    """Türkçe input. builtins.input'ı dinamik çağırır (test/mock uyumlu)."""
    return input(istem)


def _paket_yukle(*paketler: str) -> bool:
    """PARS paket yöneticisi ile paket yükle (pip yerine parskur)."""
    from pars.cli.paket import paket_yukle
    return paket_yukle(*paketler)


def _paket_listele() -> None:
    """PARS paket yöneticisi ile yüklü paketleri listele."""
    from pars.cli.paket import paket_listele
    paket_listele()


def _modul_al(ad: str, takma: str = None) -> Any:
    """Herhangi bir Python modülünü Türkçe kod içinden içe aktar."""
    import importlib
    modul = importlib.import_module(ad)
    if takma:
        return {takma: modul}
    return modul


PARS_BUILTINS: Dict[str, Any] = {

    # ── GİRİŞ / ÇIKIŞ ─────────────────────────────────────────────────────
    'yaz':                  _yaz,
    'girdial':              _girdial,
    'oku':                  _girdial,
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
    'modul_yukle':          __import__,
    'modül_al':             _modul_al,
    'modul_al':             _modul_al,

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


# ── İSTİSNA SINIFI EŞLEMELERİ ────────────────────────────────────────────

PARS_ISTISNALAR: Dict[str, type] = {
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
    'İddiaHatası':              AssertionError,
    'IddiaHatasi':              AssertionError,
    'BağlantıHatası':           ConnectionError,
    'BaglantiHatasi':           ConnectionError,
    'ZamanAşımıHatası':         TimeoutError,
    'ZamanAsimiHatasi':         TimeoutError,
    'YenidenBaşlatma':          StopAsyncIteration,
    'YenidenBaslatma':          StopAsyncIteration,
    'İptalHatası':              asyncio.CancelledError,
    'IptalHatasi':              asyncio.CancelledError,
    'EşzamanlamaHatası':        RuntimeError,
    'EszamanlamaHatasi':        RuntimeError,
    'UnicodeÇözümlemeHatası':   UnicodeDecodeError,
    'UnicodeCozumlemeHatasi':   UnicodeDecodeError,
    'UnicodeKodlamaHatası':     UnicodeEncodeError,
    'UnicodeKodlamaHatasi':     UnicodeEncodeError,
}

__all__ = [
    'KELIME_ESLEME',
    'PARS_BUILTINS',
    'PARS_ISTISNALAR',
]
