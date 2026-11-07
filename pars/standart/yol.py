"""
PARS Yol Modülü — pathlib kütüphanesi Türkçe sarmalayıcısı
"""

import shutil
from pathlib import Path
from typing import List, Optional, Union

Yol = Path
YolTipi = Union[str, Path]

__all__ = [
    'Yol', 'yol', 'simdiki', 'ev', 'birlestir', 'var_mi', 'dosya_mi',
    'klasor_mi', 'baglanti_mi', 'oku', 'oku_bayt', 'yaz', 'yaz_bayt',
    'ekle', 'listele', 'glob', 'uzanti', 'ad', 'kok', 'ust', 'coz',
    'boyut', 'olustur', 'sil', 'kopyala', 'tasi', 'goreli', 'mutlak',
    'parcalar', 'degistir',
]


def yol(*parcalar: YolTipi) -> Path:
    """Yol nesnesi oluştur."""
    return Path(*parcalar)


def simdiki() -> Path:
    """Geçerli çalışma dizini."""
    return Path.cwd()


def ev() -> Path:
    """Kullanıcının ev dizini."""
    return Path.home()


def birlestir(*parcalar: YolTipi) -> Path:
    """Yol parçalarını birleştir."""
    sonuc = Path(parcalar[0])
    for parca in parcalar[1:]:
        sonuc = sonuc / parca
    return sonuc


def var_mi(y: YolTipi) -> bool:
    return Path(y).exists()


def dosya_mi(y: YolTipi) -> bool:
    return Path(y).is_file()


def klasor_mi(y: YolTipi) -> bool:
    return Path(y).is_dir()


def baglanti_mi(y: YolTipi) -> bool:
    return Path(y).is_symlink()


def oku(y: YolTipi, kodlama: str = 'utf-8') -> str:
    return Path(y).read_text(encoding=kodlama)


def oku_bayt(y: YolTipi) -> bytes:
    return Path(y).read_bytes()


def yaz(y: YolTipi, icerik: str, kodlama: str = 'utf-8') -> int:
    return Path(y).write_text(icerik, encoding=kodlama)


def yaz_bayt(y: YolTipi, veri: bytes) -> int:
    return Path(y).write_bytes(veri)


def ekle(y: YolTipi, icerik: str, kodlama: str = 'utf-8') -> None:
    with open(y, 'a', encoding=kodlama) as f:
        f.write(icerik)


def listele(y: YolTipi = '.', desen: str = '*') -> List[Path]:
    return sorted(Path(y).glob(desen))


def glob(y: YolTipi, desen: str) -> List[Path]:
    return sorted(Path(y).glob(desen))


def uzanti(y: YolTipi) -> str:
    return Path(y).suffix


def ad(y: YolTipi) -> str:
    return Path(y).name


def kok(y: YolTipi) -> str:
    return Path(y).stem


def ust(y: YolTipi) -> Path:
    return Path(y).parent


def coz(y: YolTipi) -> Path:
    return Path(y).resolve()


def boyut(y: YolTipi) -> int:
    return Path(y).stat().st_size


def olustur(y: YolTipi, ebeveynler: bool = True,
            var_olan: bool = True) -> None:
    Path(y).mkdir(parents=ebeveynler, exist_ok=var_olan)


def sil(y: YolTipi, zorla: bool = False) -> None:
    p = Path(y)
    if p.is_dir():
        if zorla:
            shutil.rmtree(p)
        else:
            p.rmdir()
    else:
        p.unlink()


def kopyala(kaynak: YolTipi, hedef: YolTipi) -> None:
    shutil.copy2(kaynak, hedef)


def tasi(kaynak: YolTipi, hedef: YolTipi) -> None:
    shutil.move(str(kaynak), str(hedef))


def goreli(y: YolTipi, baslangic: Optional[YolTipi] = None) -> Path:
    if baslangic is None:
        return Path(y)
    return Path(y).relative_to(baslangic)


def mutlak(y: YolTipi) -> Path:
    return Path(y).absolute()


def parcalar(y: YolTipi) -> tuple:
    return Path(y).parts


def degistir(y: YolTipi, uzanti: str) -> Path:
    return Path(y).with_suffix(uzanti)
