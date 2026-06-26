"""
PARS Dosya Modülü — pathlib + os Türkçe sarmalayıcısı
"""

import os
import json
import csv
import shutil
import tempfile
from pathlib import Path
from typing import List, Optional, Any

__all__ = [
    'oku', 'yaz', 'ekle', 'satirlari_oku', 'satirlari_yaz',
    'var_mi', 'klasor_mu', 'dosya_mi', 'sil', 'tasi', 'kopyala',
    'yeniden_adlandir', 'klasor_olustur', 'klasor_sil',
    'listele', 'boyut', 'uzanti', 'dosya_adi', 'ana_klasor', 'tam_yol',
    'gecici_dosya', 'gecici_klasor',
    'json_oku', 'json_yaz', 'csv_oku', 'csv_yaz',
]


def oku(yol: str, kodlama: str = 'utf-8') -> str:
    """Dosyayı oku ve metin olarak döndür."""
    with open(yol, 'r', encoding=kodlama) as f:
        return f.read()


def yaz(yol: str, icerik: str, kodlama: str = 'utf-8') -> None:
    """Dosyaya yaz (var olanı üzerine yazar)."""
    with open(yol, 'w', encoding=kodlama) as f:
        f.write(icerik)


def ekle(yol: str, icerik: str, kodlama: str = 'utf-8') -> None:
    """Dosyanın sonuna ekle."""
    with open(yol, 'a', encoding=kodlama) as f:
        f.write(icerik)


def satirlari_oku(yol: str, kodlama: str = 'utf-8') -> list:
    """Dosyayı satır satır oku."""
    with open(yol, 'r', encoding=kodlama) as f:
        return f.readlines()


def satirlari_yaz(yol: str, satirlar: list, kodlama: str = 'utf-8') -> None:
    """Satır listesini dosyaya yaz."""
    with open(yol, 'w', encoding=kodlama) as f:
        f.writelines(satirlar)


def var_mi(yol: str) -> bool:
    """Dosya veya klasör var mı?"""
    return Path(yol).exists()


def klasor_mu(yol: str) -> bool:
    """Klasör mü?"""
    return Path(yol).is_dir()


def dosya_mi(yol: str) -> bool:
    """Dosya mı?"""
    return Path(yol).is_file()


def sil(yol: str) -> None:
    """Dosyayı sil."""
    os.remove(yol)


def tasi(kaynak: str, hedef: str) -> None:
    """Dosyayı taşı."""
    shutil.move(kaynak, hedef)


def kopyala(kaynak: str, hedef: str) -> None:
    """Dosyayı kopyala."""
    shutil.copy2(kaynak, hedef)


def yeniden_adlandir(eski: str, yeni: str) -> None:
    """Dosyayı yeniden adlandır."""
    os.rename(eski, yeni)


def klasor_olustur(yol: str, aradakiler: bool = True) -> None:
    """Klasör oluştur."""
    os.makedirs(yol, exist_ok=aradakiler)


def klasor_sil(yol: str) -> None:
    """Klasörü ve içeriğini sil."""
    shutil.rmtree(yol)


def listele(yol: str = '.', desen: str = '*') -> list:
    """Klasördeki dosyaları listele."""
    return [str(p) for p in Path(yol).glob(desen)]


def boyut(yol: str) -> int:
    """Dosya boyutu (bayt)."""
    return Path(yol).stat().st_size


def uzanti(yol: str) -> str:
    """Dosya uzantısı."""
    return Path(yol).suffix


def dosya_adi(yol: str) -> str:
    """Dosya adı (uzantısız)."""
    return Path(yol).stem


def ana_klasor(yol: str) -> str:
    """Üst klasör yolu."""
    return str(Path(yol).parent)


def tam_yol(yol: str) -> str:
    """Tam yolu çöz."""
    return str(Path(yol).resolve())


def gecici_dosya() -> str:
    """Geçici dosya yolu oluştur."""
    return tempfile.mktemp()


def gecici_klasor() -> str:
    """Geçici klasör yolu oluştur."""
    return tempfile.mkdtemp()


# ── JSON YARDIMCILARI ────────────────────────────────────────────────────

def json_oku(yol: str, kodlama: str = 'utf-8') -> Any:
    """JSON dosyasını oku."""
    with open(yol, 'r', encoding=kodlama) as f:
        return json.load(f)


def json_yaz(yol: str, veri: Any, kodlama: str = 'utf-8',
             girintili: bool = True) -> None:
    """JSON dosyasına yaz."""
    with open(yol, 'w', encoding=kodlama) as f:
        json.dump(veri, f, ensure_ascii=False,
                  indent=4 if girintili else None)


# ── CSV YARDIMCILARI ─────────────────────────────────────────────────────

def csv_oku(yol: str, kodlama: str = 'utf-8',
            baslik: bool = True) -> list:
    """CSV dosyasını oku."""
    with open(yol, 'r', encoding=kodlama, newline='') as f:
        okuyucu = csv.DictReader(f) if baslik else csv.reader(f)
        return list(okuyucu)


def csv_yaz(yol: str, veriler: list, kodlama: str = 'utf-8',
            baslik: list = None) -> None:
    """CSV dosyasına yaz."""
    with open(yol, 'w', encoding=kodlama, newline='') as f:
        if baslik:
            yazici = csv.DictWriter(f, fieldnames=baslik)
            yazici.writeheader()
            yazici.writerows(veriler)
        else:
            yazici = csv.writer(f)
            yazici.writerows(veriler)
