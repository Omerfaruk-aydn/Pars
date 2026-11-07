"""
PARS Günlük Modülü — logging kütüphanesi Türkçe sarmalayıcısı
"""

import logging
from typing import Any, Optional

__all__ = [
    'Seviye', 'temel_yapilandir', 'gunlukcu_al', 'bilgi', 'uyari',
    'hata', 'kritik', 'ayikla', 'seviye_ata', 'dosyaya_yaz',
    'gunlukcu_ekle', 'bicim',
]

Seviye = logging
DEBUG = logging.DEBUG
BILGI = logging.INFO
UYARI = logging.WARNING
HATA = logging.ERROR
KRITIK = logging.CRITICAL

_SEVIYELER = {
    'hata_ayikla': logging.DEBUG,
    'debug': logging.DEBUG,
    'bilgi': logging.INFO,
    'info': logging.INFO,
    'uyari': logging.WARNING,
    'warning': logging.WARNING,
    'hata': logging.ERROR,
    'error': logging.ERROR,
    'kritik': logging.CRITICAL,
    'critical': logging.CRITICAL,
}


def temel_yapilandir(seviye: Any = BILGI,
                     bicim_metni: str = '%(asctime)s | %(levelname)s | %(message)s',
                     dosya: Optional[str] = None) -> None:
    """Günlük sistemini yapılandır."""
    if isinstance(seviye, str):
        seviye = _SEVIYELER.get(seviye.lower(), logging.INFO)
    kwargs = {
        'level': seviye,
        'format': bicim_metni,
    }
    if dosya:
        kwargs['filename'] = dosya
        kwargs['encoding'] = 'utf-8'
    logging.basicConfig(**kwargs)


def gunlukcu_al(isim: Optional[str] = None) -> logging.Logger:
    """Günlükçü nesnesi al."""
    return logging.getLogger(isim)


def _seviye(seviye: Any) -> int:
    if isinstance(seviye, str):
        return _SEVIYELER.get(seviye.lower(), logging.INFO)
    return seviye


def bilgi(mesaj: str, *args: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).info(mesaj, *args)


def uyari(mesaj: str, *args: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).warning(mesaj, *args)


def hata(mesaj: str, *args: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).error(mesaj, *args)


def kritik(mesaj: str, *args: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).critical(mesaj, *args)


def ayikla(mesaj: str, *args: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).debug(mesaj, *args)


def seviye_ata(seviye: Any, gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).setLevel(_seviye(seviye))


def dosyaya_yaz(dosya: str, seviye: Any = BILGI,
                gunlukcu: Optional[str] = None) -> None:
    """Günlüğü dosyaya yaz."""
    lg = gunlukcu_al(gunlukcu)
    isleyici = logging.FileHandler(dosya, encoding='utf-8')
    isleyici.setLevel(_seviye(seviye))
    isleyici.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s'))
    lg.addHandler(isleyici)


def gunlukcu_ekle(isleyici: logging.Handler,
                  gunlukcu: Optional[str] = None) -> None:
    gunlukcu_al(gunlukcu).addHandler(isleyici)


def bicim(metin: str) -> logging.Formatter:
    return logging.Formatter(metin)
