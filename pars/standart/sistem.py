"""
PARS Sistem Modülü — os/sys/platform Türkçe sarmalayıcısı
"""

import os
import sys
import platform
import subprocess
import getpass
from typing import List, Optional

__all__ = [
    'ortam_degiskeni', 'ortam_degiskeni_ata', 'calisma_dizini',
    'dizin_degistir', 'komut_calistir', 'islem_id', 'islem_sonlandir',
    'argumanlar', 'platform_bilgisi', 'isletim_sistemi', 'kullanici_adi',
    'ev_dizini', 'cpu_sayisi', 'bellek_kullanimi',
    'python_surumu', 'pars_surumu',
]


def ortam_degiskeni(isim: str, varsayilan: str = None) -> Optional[str]:
    """Ortam değişkenini oku."""
    return os.environ.get(isim, varsayilan)


def ortam_degiskeni_ata(isim: str, deger: str) -> None:
    """Ortam değişkeni ata."""
    os.environ[isim] = deger


def calisma_dizini() -> str:
    """Çalışma dizinini döndür."""
    return os.getcwd()


def dizin_degistir(yol: str) -> None:
    """Çalışma dizinini değiştir."""
    os.chdir(yol)


def komut_calistir(komut: str) -> tuple:
    """
    Sistem komutu çalıştır.

    Returns:
        tuple: (çıktı, hata, dönüş_kodu)
    """
    sonuc = subprocess.run(
        komut, shell=True,
        capture_output=True, text=True
    )
    return sonuc.stdout, sonuc.stderr, sonuc.returncode


def islem_id() -> int:
    """Mevcut işlem kimliği (PID)."""
    return os.getpid()


def islem_sonlandir(kod: int = 0) -> None:
    """Programı sonlandır."""
    sys.exit(kod)


def argumanlar() -> list:
    """Komut satırı argümanlarını döndür."""
    return sys.argv


def platform_bilgisi() -> str:
    """Platform bilgisi."""
    return platform.platform()


def isletim_sistemi() -> str:
    """İşletim sistemi adı."""
    return platform.system()


def kullanici_adi() -> str:
    """Mevcut kullanıcı adı."""
    return getpass.getuser()


def ev_dizini() -> str:
    """Kullanıcının ev dizini."""
    return os.path.expanduser('~')


def cpu_sayisi() -> int:
    """CPU çekirdek sayısı."""
    return os.cpu_count() or 1


def bellek_kullanimi() -> dict:
    """Bellek kullanımı bilgisi (platform bağımlı)."""
    try:
        import psutil
        bellek = psutil.virtual_memory()
        return {
            'toplam': bellek.total,
            'kullanilan': bellek.available,
            'yuzde': bellek.percent,
        }
    except ImportError:
        return {'toplam': 0, 'kullanilan': 0, 'yuzde': 0}


def python_surumu() -> str:
    """Python versiyonu."""
    return platform.python_version()


def pars_surumu() -> str:
    """PARS versiyonu."""
    from pars import __version__
    return __version__
