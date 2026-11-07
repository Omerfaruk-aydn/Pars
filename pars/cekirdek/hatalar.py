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

HATA_TURLERI = {
    'SyntaxError':          'Sözdizimi Hatası',
    'NameError':            'Ad Hatası',
    'TypeError':            'Tür Hatası',
    'ValueError':           'Değer Hatası',
    'IndexError':           'İndeks Hatası',
    'KeyError':             'Anahtar Hatası',
    'AttributeError':       'Nitelik Hatası',
    'ImportError':          'İçe Aktarma Hatası',
    'ModuleNotFoundError':  'Modül Bulunamadı',
    'FileNotFoundError':    'Dosya Bulunamadı',
    'PermissionError':      'İzin Hatası',
    'ZeroDivisionError':    'Sıfıra Bölme Hatası',
    'OverflowError':        'Taşma Hatası',
    'MemoryError':          'Bellek Hatası',
    'RecursionError':       'Özyineleme Sınırı Aşıldı',
    'TimeoutError':         'Zaman Aşımı',
    'ConnectionError':      'Bağlantı Hatası',
    'OSError':              'İşletim Sistemi Hatası',
    'RuntimeError':         'Çalışma Zamanı Hatası',
    'NotImplementedError':  'Uygulanmadı Hatası',
    'AssertionError':       'İddia Hatası',
    'UnicodeDecodeError':   'Unicode Çözümleme Hatası',
    'UnicodeEncodeError':   'Unicode Kodlama Hatası',
    'StopIteration':        'İterasyon Bitti',
    'KeyboardInterrupt':    'Kullanıcı Durdurdu',
    'SystemExit':           'Program Sonlandı',
    'Exception':            'Genel Hata',
    'BrokenPipeError':      'Kırık Boru Hatası',
    'FileExistsError':      'Dosya Zaten Var',
    'IsADirectoryError':    'Bu Bir Klasör',
    'NotADirectoryError':   'Klasör Değil',
    'UnicodeError':         'Unicode Hatası',
    'FloatingPointError':   'Kayan Nokta Hatası',
    'EOFError':             'Girdi Bitti',
}

HATA_IPUCLARI = {
    'is not defined':
        'Değişkeni daha önce tanımladınız mı? Büyük/küçük harf farkına dikkat edin.',
    'is not callable':
        'Bu değer bir fonksiyon değil. Parantezleri kaldırın.',
    'division by zero':
        'Bir sayıyı sıfıra bölemezsiniz. Bölmeden önce kontrol edin.',
    'list index out of range':
        'Liste indeksi sınır dışı. uzunluk() ile eleman sayısını kontrol edin.',
    'has no attribute':
        'Bu nesnenin böyle bir özelliği yok. dir() ile özellikleri listeleyin.',
    'No module named':
        'Modül yüklü değil. Şunu deneyin: pars paket yükle <modül_adı>',
    'takes':
        'Fonksiyon yanlış sayıda argüman alıyor. Parametre sayısını kontrol edin.',
    'unsupported operand':
        'Bu operatör bu veri tipleriyle kullanılamaz. tip() ile kontrol edin.',
    'cannot unpack':
        'Çoklu atama için sağ taraftaki değer uygun değil.',
    'object is not iterable':
        'Bu nesne üzerinde döngü kurulamaz. liste veya aralık kullanın.',
    'string indices must be integers':
        'Yazı indeksleme tamsayı gerektirir.',
    'maximum recursion':
        'Fonksiyon kendini çok derin çağırıyor. Taban durumu kontrol edin.',
    'global name':
        'Global değişkeni fonksiyon içinde kullanmak için \'global değişken_adı\' yazın.',
    'NoneType':
        '\'yok\' (None) değeri üzerinde işlem yapılamaz. Değerin atanmış olduğundan emin olun.',
}

# ANSI renk kodları
KIRMIZI = '\033[91m'
SARI = '\033[93m'
YESIL = '\033[92m'
MAVI = '\033[94m'
MOR = '\033[95m'
BEYAZ = '\033[97m'
GRI = '\033[90m'
SIFIRLA = '\033[0m'
KALIN = '\033[1m'


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
    turkce_tur = HATA_TURLERI.get(tur_adi, f'{tur_adi}')
    satirlar = pars_kodu.splitlines()

    ayrac = _renkli('-' * 60, GRI)
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
                print(f'\n  {_renkli("İpucu: " + ipucu, YESIL)}', file=sys.stderr)
                break

    print(f'{ayrac}\n', file=sys.stderr)


__all__ = ['hata_goster', 'HATA_TURLERI', 'HATA_IPUCLARI']
