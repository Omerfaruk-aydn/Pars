"""
PARS Veri Modülü — json/csv/pickle/base64 Türkçe sarmalayıcısı
"""

import json
import csv
import pickle
import base64
import hashlib
from typing import Any, List, Optional

__all__ = [
    'json_metin', 'json_cozumle', 'json_oku', 'json_yaz',
    'csv_oku', 'csv_yaz',
    'kaydet', 'yukle',
    'base64_kodla', 'base64_coz',
    'hash_hesapla',
]


def json_metin(veri: Any, girintili: bool = False) -> str:
    """Veriyi JSON metnine çevir."""
    return json.dumps(veri, ensure_ascii=False,
                      indent=4 if girintili else None)


def json_cozumle(metin: str) -> Any:
    """JSON metnini Python nesnesine çevir."""
    return json.loads(metin)


def json_oku(yol: str, kodlama: str = 'utf-8') -> Any:
    """JSON dosyasını oku."""
    with open(yol, 'r', encoding=kodlama) as f:
        return json.load(f)


def json_yaz(yol: str, veri: Any, kodlama: str = 'utf-8') -> None:
    """JSON dosyasına yaz."""
    with open(yol, 'w', encoding=kodlama) as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)


def csv_oku(yol: str, kodlama: str = 'utf-8') -> list:
    """CSV dosyasını oku (sözlük listesi döndürür)."""
    with open(yol, 'r', encoding=kodlama, newline='') as f:
        okuyucu = csv.DictReader(f)
        return list(okuyucu)


def csv_yaz(yol: str, veriler: list, kodlama: str = 'utf-8') -> None:
    """CSV dosyasına yaz."""
    if not veriler:
        return
    with open(yol, 'w', encoding=kodlama, newline='') as f:
        yazici = csv.DictWriter(f, fieldnames=veriler[0].keys())
        yazici.writeheader()
        yazici.writerows(veriler)


def kaydet(veri: Any, yol: str) -> None:
    """Veriyi pickle ile dosyaya kaydet."""
    with open(yol, 'wb') as f:
        pickle.dump(veri, f)


def yukle(yol: str) -> Any:
    """Pickle dosyasından veri yükle."""
    with open(yol, 'rb') as f:
        return pickle.load(f)


def base64_kodla(veri: bytes) -> str:
    """Bayt dizisini Base64 ile kodla."""
    return base64.b64encode(veri).decode('ascii')


def base64_coz(metin: str) -> bytes:
    """Base64 metnini bayt dizisine çevir."""
    return base64.b64decode(metin)


def hash_hesapla(metin: str, algoritma: str = 'sha256') -> str:
    """
    Metnin hash değerini hesapla.

    Args:
        metin: Hash'lenecek metin
        algoritma: Hash algoritması (md5, sha1, sha256, sha512)
    """
    h = hashlib.new(algoritma)
    h.update(metin.encode('utf-8'))
    return h.hexdigest()
