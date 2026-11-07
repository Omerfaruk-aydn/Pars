"""
PARS Süreç Modülü — subprocess kütüphanesi güvenli Türkçe sarmalayıcısı
"""

import shlex
import subprocess
import sys
from typing import Any, List, Optional, Sequence, Union

__all__ = [
    'calistir', 'cikti_al', 'kontrol_et', 'boru', 'kabuk_calistir',
    'python_calistir', 'pars_calistir', 'bekle',
]

Komut = Union[str, Sequence[str]]


def _komut_listesi(komut: Komut,
                   kabuk: bool = False) -> Union[str, List[str]]:
    """Metin komutu güvenli biçimde argüman listesine çevir."""
    if isinstance(komut, str) and not kabuk:
        return shlex.split(komut, posix=(sys.platform != 'win32'))
    if isinstance(komut, tuple):
        return list(komut)
    return komut


def calistir(komut: Komut,
             kabuk: bool = False,
             girdi: Optional[str] = None,
             zaman_asimi: Optional[float] = None,
             ortam: Optional[dict] = None,
             calisma_dizini: Optional[str] = None) -> dict:
    """
    Komut çalıştır ve sonucu sözlük olarak döndür.

    Returns:
        {'cikti': str, 'hata': str, 'kod': int}
    """
    sonuc = subprocess.run(
        _komut_listesi(komut, kabuk),
        shell=kabuk,
        input=girdi,
        capture_output=True,
        text=True,
        timeout=zaman_asimi,
        env=ortam,
        cwd=calisma_dizini,
    )
    return {
        'cikti': sonuc.stdout,
        'hata': sonuc.stderr,
        'kod': sonuc.returncode,
    }


def cikti_al(komut: Komut, kabuk: bool = False,
             zaman_asimi: Optional[float] = None) -> str:
    """Komutun standart çıktısını döndür."""
    return calistir(komut, kabuk=kabuk,
                    zaman_asimi=zaman_asimi)['cikti']


def kontrol_et(komut: Komut, kabuk: bool = False,
               zaman_asimi: Optional[float] = None) -> str:
    """Komut başarısızsa hata fırlat, çıktıyı döndür."""
    sonuc = subprocess.run(
        _komut_listesi(komut, kabuk),
        shell=kabuk,
        capture_output=True,
        text=True,
        timeout=zaman_asimi,
        check=True,
    )
    return sonuc.stdout


def boru(komut: Komut, kabuk: bool = False, **kwargs: Any) -> subprocess.Popen:
    """Arka planda süreç başlat (Popen)."""
    return subprocess.Popen(_komut_listesi(komut, kabuk),
                            shell=kabuk, **kwargs)


def kabuk_calistir(komut: str, zaman_asimi: Optional[float] = None) -> dict:
    """Kabuk üzerinden komut çalıştır (güvenilmeyen girdiyle kullanmayın)."""
    return calistir(komut, kabuk=True, zaman_asimi=zaman_asimi)


def python_calistir(kod: str) -> dict:
    """Python kodunu ayrı süreçte çalıştır."""
    return calistir([sys.executable, '-c', kod])


def pars_calistir(dosya: str) -> dict:
    """PARS dosyasını ayrı süreçte çalıştır."""
    return calistir([sys.executable, '-m', 'pars.cli.komutlar', dosya])


def bekle(surec: subprocess.Popen,
          zaman_asimi: Optional[float] = None) -> int:
    """Sürecin bitmesini bekle, dönüş kodunu ver."""
    return surec.wait(timeout=zaman_asimi)
