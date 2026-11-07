"""
PARS Sıkıştırma Modülü — gzip / zlib / zipfile / tarfile Türkçe sarmalayıcısı
"""

import gzip
import tarfile
import zipfile
import zlib
from typing import List

__all__ = [
    'gzip_sikistir', 'gzip_ac', 'zlib_sikistir', 'zlib_ac',
    'zip_olustur', 'zip_ac', 'zip_listele', 'zip_oku',
    'tar_olustur', 'tar_ac', 'tar_listele',
]


def gzip_sikistir(veri: bytes) -> bytes:
    return gzip.compress(veri)


def gzip_ac(veri: bytes) -> bytes:
    return gzip.decompress(veri)


def zlib_sikistir(veri: bytes, seviye: int = -1) -> bytes:
    return zlib.compress(veri, seviye)


def zlib_ac(veri: bytes) -> bytes:
    return zlib.decompress(veri)


def zip_olustur(hedef: str, dosyalar: List[str],
                sikistirma: int = zipfile.ZIP_DEFLATED) -> str:
    """Dosyaları ZIP arşivine ekle."""
    with zipfile.ZipFile(hedef, 'w', compression=sikistirma) as zf:
        for dosya in dosyalar:
            zf.write(dosya)
    return hedef


def zip_ac(arsiv: str, hedef_dizin: str = '.') -> List[str]:
    """ZIP arşivini çıkar, çıkarılan yolları döndür."""
    with zipfile.ZipFile(arsiv, 'r') as zf:
        zf.extractall(hedef_dizin)
        return zf.namelist()


def zip_listele(arsiv: str) -> List[str]:
    with zipfile.ZipFile(arsiv, 'r') as zf:
        return zf.namelist()


def zip_oku(arsiv: str, uye: str) -> bytes:
    with zipfile.ZipFile(arsiv, 'r') as zf:
        return zf.read(uye)


def tar_olustur(hedef: str, dosyalar: List[str],
                mod: str = 'w:gz') -> str:
    with tarfile.open(hedef, mod) as tf:
        for dosya in dosyalar:
            tf.add(dosya)
    return hedef


def tar_ac(arsiv: str, hedef_dizin: str = '.') -> None:
    with tarfile.open(arsiv, 'r:*') as tf:
        tf.extractall(hedef_dizin)


def tar_listele(arsiv: str) -> List[str]:
    with tarfile.open(arsiv, 'r:*') as tf:
        return tf.getnames()
