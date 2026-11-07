"""
PARS Takvim Modülü — calendar kütüphanesi Türkçe sarmalayıcısı
"""

import calendar
from datetime import date, datetime
from typing import List, Union

TURKCE_GUNLER = [
    'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe',
    'Cuma', 'Cumartesi', 'Pazar',
]
TURKCE_AYLAR = [
    'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
    'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık',
]

__all__ = [
    'TURKCE_GUNLER', 'TURKCE_AYLAR', 'artik_yil', 'ay_gun_sayisi',
    'ay_takvimi', 'hafta_gunu', 'gun_adi', 'ay_adi', 'yil_haftalari',
    'tarih_araligi', 'ay_basi', 'ay_sonu',
]


def artik_yil(yil: int) -> bool:
    return calendar.isleap(yil)


def ay_gun_sayisi(yil: int, ay: int) -> int:
    return calendar.monthrange(yil, ay)[1]


def ay_takvimi(yil: int, ay: int) -> str:
    metin = calendar.month(yil, ay)
    for i, gun in enumerate(TURKCE_GUNLER):
        metin = metin.replace(calendar.day_abbr[i], gun[:3])
    for i, ay_adi_ in enumerate(TURKCE_AYLAR):
        metin = metin.replace(calendar.month_name[i + 1], ay_adi_)
    return metin


def hafta_gunu(tarih: Union[date, datetime, str]) -> int:
    if isinstance(tarih, str):
        tarih = date.fromisoformat(tarih)
    return tarih.weekday()


def gun_adi(tarih: Union[date, datetime, str]) -> str:
    return TURKCE_GUNLER[hafta_gunu(tarih)]


def ay_adi(tarih: Union[date, datetime, str]) -> str:
    if isinstance(tarih, str):
        tarih = date.fromisoformat(tarih)
    return TURKCE_AYLAR[tarih.month - 1]


def yil_haftalari(yil: int) -> List[list]:
    """Y?l?n t?m haftalar?n? g?n listeleri olarak d?nd?r."""
    haftalar: List[list] = []
    for ay in calendar.Calendar().yeardatescalendar(yil, width=1):
        for hafta in ay:
            haftalar.append(hafta)
    return haftalar


def tarih_araligi(baslangic: date, bitis: date) -> List[date]:
    if bitis < baslangic:
        baslangic, bitis = bitis, baslangic
    return [date.fromordinal(o)
            for o in range(baslangic.toordinal(), bitis.toordinal() + 1)]


def ay_basi(yil: int, ay: int) -> date:
    return date(yil, ay, 1)


def ay_sonu(yil: int, ay: int) -> date:
    return date(yil, ay, ay_gun_sayisi(yil, ay))
