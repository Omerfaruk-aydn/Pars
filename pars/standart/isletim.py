"""
PARS İşletim Sistemi Modülü — os kütüphanesi Türkçe sarmalayıcısı
"""

import os
import shutil
import tempfile
from typing import Iterator, List, Optional

__all__ = [
    'ortam', 'ortam_ata', 'ortam_sil', 'ortam_hepsi', 'calisma_dizini',
    'dizin_degistir', 'listele', 'gez', 'olustur', 'sil', 'sil_agac',
    'yeniden_adlandir', 'kopyala', 'tasi', 'istatistik', 'yol_birlestir',
    'yol_ayir', 'mutlak_yol', 'var_mi', 'dosya_mi', 'klasor_mi',
    'cpu_sayisi', 'isletim_sistemi', 'kullanici', 'ev_dizini',
    'gecici_dizin', 'gecici_dosya', 'ayrac', 'satir_ayrac',
]


def ortam(isim: str, varsayilan: Optional[str] = None) -> Optional[str]:
    return os.environ.get(isim, varsayilan)


def ortam_ata(isim: str, deger: str) -> None:
    os.environ[isim] = deger


def ortam_sil(isim: str) -> None:
    os.environ.pop(isim, None)


def ortam_hepsi() -> dict:
    return dict(os.environ)


def calisma_dizini() -> str:
    return os.getcwd()


def dizin_degistir(y: str) -> None:
    os.chdir(y)


def listele(y: str = '.') -> List[str]:
    return os.listdir(y)


def gez(y: str = '.') -> Iterator[tuple]:
    """Dizin ağacında yürü: (dizin, alt_dizinler, dosyalar)."""
    return iter(os.walk(y))


def olustur(y: str, aradakiler: bool = True) -> None:
    os.makedirs(y, exist_ok=aradakiler)


def sil(y: str) -> None:
    os.remove(y)


def sil_agac(y: str) -> None:
    shutil.rmtree(y)


def yeniden_adlandir(eski: str, yeni: str) -> None:
    os.rename(eski, yeni)


def kopyala(kaynak: str, hedef: str) -> None:
    shutil.copy2(kaynak, hedef)


def tasi(kaynak: str, hedef: str) -> None:
    shutil.move(kaynak, hedef)


def istatistik(y: str) -> dict:
    s = os.stat(y)
    return {
        'boyut': s.st_size,
        'degisme': s.st_mtime,
        'erisim': s.st_atime,
        'olusturma': s.st_ctime,
        'mod': s.st_mode,
        'dosya_mi': os.path.isfile(y),
        'klasor_mu': os.path.isdir(y),
    }


def yol_birlestir(*parcalar: str) -> str:
    return os.path.join(*parcalar)


def yol_ayir(y: str) -> tuple:
    return os.path.split(y)


def mutlak_yol(y: str) -> str:
    return os.path.abspath(y)


def var_mi(y: str) -> bool:
    return os.path.exists(y)


def dosya_mi(y: str) -> bool:
    return os.path.isfile(y)


def klasor_mi(y: str) -> bool:
    return os.path.isdir(y)


def cpu_sayisi() -> int:
    return os.cpu_count() or 1


def isletim_sistemi() -> str:
    return os.name


def kullanici() -> str:
    return os.environ.get('USERNAME') or os.environ.get('USER') or 'kullanici'


def ev_dizini() -> str:
    return os.path.expanduser('~')


def gecici_dizin(onek: str = 'pars_') -> str:
    return tempfile.mkdtemp(prefix=onek)


def gecici_dosya(onek: str = 'pars_', sonek: str = '') -> str:
    fd, yol_ = tempfile.mkstemp(prefix=onek, suffix=sonek)
    os.close(fd)
    return yol_


ayrac = os.sep
satir_ayrac = os.linesep
