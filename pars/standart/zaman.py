"""
PARS Zaman Modülü — datetime Türkçe sarmalayıcısı
"""

from datetime import datetime, date, time as _saat_tipi, timedelta
from typing import Union
import time as _time

__all__ = [
    'TURKCE_GUNLER', 'TURKCE_AYLAR',
    'simdi', 'simdi_utc', 'bugun', 'zaman_damgasi', 'bekle', 'uyu',
    'sure_olc', 'monotonik',
    'tarih', 'saat_olustur', 'fark', 'bicimle', 'biçimle', 'cozmle',
    'çözümle', 'iso_metin', 'turkce_tarih', 'hafta_numarasi',
    'gun_adi', 'ay_adi', 'yil', 'ay', 'gun', 'saat', 'dakika', 'saniye',
    'is_gunu_mu', 'hafta_sonu_mu', 'gun_ekle', 'ay_ekle',
    'gecti_mi', 'gec_ti_mi', 'kalan_sure',
]

TURKCE_GUNLER = [
    'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe',
    'Cuma', 'Cumartesi', 'Pazar'
]
TURKCE_AYLAR = [
    'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
    'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'
]


def simdi() -> datetime:
    """Şu anki tarih ve saat."""
    return datetime.now()


def bugun() -> date:
    """Bugünün tarihi."""
    return date.today()


def zaman_damgasi() -> float:
    """Unix zaman damgası."""
    return _time.time()


def bekle(saniye: float) -> None:
    """Belirtilen saniye kadar bekle."""
    _time.sleep(saniye)


def uyu(saniye: float) -> None:
    """bekle() takma adı."""
    _time.sleep(saniye)


# Python uyumluluğu: zaman.sleep(...), zaman.time(...), zaman.perf_counter()
sleep = bekle
time = _time.time
perf_counter = _time.perf_counter
monotonic = _time.monotonic


def simdi_utc() -> datetime:
    """UTC tarih ve saat."""
    from datetime import timezone
    return datetime.now(timezone.utc)


def sure_olc() -> float:
    """Yüksek çözünürlüklü sayaç (performans ölçümü)."""
    return _time.perf_counter()


def monotonik() -> float:
    """Tek yönlü artan saat."""
    return _time.monotonic()


def iso_metin(tarih_nesne: Union[datetime, date]) -> str:
    """ISO 8601 metni."""
    return tarih_nesne.isoformat()


def turkce_tarih(tarih_nesne: Union[datetime, date]) -> str:
    """Türkçe uzun tarih: 6 Kasım 2026 Cuma."""
    return (f'{tarih_nesne.day} {ay_adi(tarih_nesne)} '
            f'{tarih_nesne.year} {gun_adi(tarih_nesne)}')


def hafta_numarasi(tarih_nesne: Union[datetime, date]) -> int:
    """ISO hafta numarası."""
    return tarih_nesne.isocalendar()[1]


def gecti_mi(tarih_nesne: Union[datetime, date]) -> bool:
    """Tarih geçmişte mi? (doğru yazım)"""
    return gec_ti_mi(tarih_nesne)


def tarih(yil: int, ay: int, gun: int) -> date:
    """Tarih nesnesi oluştur."""
    return date(yil, ay, gun)


def saat_olustur(saat: int, dakika: int = 0,
                 saniye: int = 0) -> _saat_tipi:
    """Saat nesnesi oluştur."""
    return _saat_tipi(saat, dakika, saniye)


def fark(baslangic: Union[datetime, date],
         bitis: Union[datetime, date]) -> timedelta:
    """İki tarih arasındaki fark."""
    return bitis - baslangic


def bicimle(tarih_nesne: Union[datetime, date],
            sablon: str = '%d.%m.%Y %H:%M:%S') -> str:
    """Tarihi biçimlendir."""
    return tarih_nesne.strftime(sablon)


def cozmle(metin: str, sablon: str = '%d.%m.%Y') -> datetime:
    """Metni tarih nesnesine çevir."""
    return datetime.strptime(metin, sablon)


# Türkçe karakterli takma adlar
biçimle = bicimle
çözümle = cozmle


def gun_adi(tarih_nesne: Union[datetime, date]) -> str:
    """Günün Türkçe adı."""
    return TURKCE_GUNLER[tarih_nesne.weekday()]


def ay_adi(tarih_nesne: Union[datetime, date]) -> str:
    """Ayın Türkçe adı."""
    return TURKCE_AYLAR[tarih_nesne.month - 1]


def yil(tarih_nesne: Union[datetime, date]) -> int:
    """Yıl."""
    return tarih_nesne.year


def ay(tarih_nesne: Union[datetime, date]) -> int:
    """Ay."""
    return tarih_nesne.month


def gun(tarih_nesne: Union[datetime, date]) -> int:
    """Gün."""
    return tarih_nesne.day


def saat(tarih_saat: datetime) -> int:
    """Saat."""
    return tarih_saat.hour


def dakika(tarih_saat: datetime) -> int:
    """Dakika."""
    return tarih_saat.minute


def saniye(tarih_saat: datetime) -> int:
    """Saniye."""
    return tarih_saat.second


def is_gunu_mu(tarih_nesne: Union[datetime, date]) -> bool:
    """İş günü mü? (Pazartesi-Cuma)"""
    return tarih_nesne.weekday() < 5


def hafta_sonu_mu(tarih_nesne: Union[datetime, date]) -> bool:
    """Hafta sonu mu?"""
    return tarih_nesne.weekday() >= 5


def gun_ekle(tarih_nesne: Union[datetime, date], n: int) -> Union[datetime, date]:
    """Tarihe gün ekle."""
    return tarih_nesne + timedelta(days=n)


def ay_ekle(tarih_nesne: date, n: int) -> date:
    """Tarihe ay ekle."""
    yeni_ay = tarih_nesne.month + n
    yeni_yil = tarih_nesne.year + (yeni_ay - 1) // 12
    yeni_ay = ((yeni_ay - 1) % 12) + 1
    return date(yeni_yil, yeni_ay, tarih_nesne.day)


def gec_ti_mi(tarih_nesne: Union[datetime, date]) -> bool:
    """Tarih geçmişte mi?"""
    if isinstance(tarih_nesne, datetime):
        return tarih_nesne < datetime.now()
    return tarih_nesne < date.today()


def kalan_sure(tarih_nesne: Union[datetime, date]) -> str:
    """Tarihe kalan süreyi Türkçe göster."""
    if isinstance(tarih_nesne, datetime):
        fark_nesne = tarih_nesne - datetime.now()
    else:
        fark_nesne = tarih_nesne - date.today()

    gunler = fark_nesne.days
    if gunler < 0:
        return 'Geçmiş'
    if gunler == 0:
        return 'Bugün'
    if gunler == 1:
        return 'Yarın'
    if gunler < 7:
        return f'{gunler} gün kaldı'
    if gunler < 30:
        return f'{gunler // 7} hafta kaldı'
    if gunler < 365:
        return f'{gunler // 30} ay kaldı'
    return f'{gunler // 365} yıl kaldı'
