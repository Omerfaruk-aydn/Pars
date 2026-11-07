"""
PARS Ağ Modülü — urllib Türkçe sarmalayıcısı
"""

import urllib.request
import urllib.parse
import json
from typing import Any

__all__ = [
    'get', 'post', 'put', 'sil_istek',
    'dosya_indir', 'url_kodla', 'json_al',
]


def get(url: str, basliklar: dict = None,
        zaman_asimi: int = 30) -> dict:
    """
    HTTP GET isteği gönder.

    Returns:
        dict: {'durum': int, 'basliklar': dict, 'govde': str}
    """
    istek = urllib.request.Request(url, method='GET')
    if basliklar:
        for k, v in basliklar.items():
            istek.add_header(k, v)
    try:
        with urllib.request.urlopen(istek, timeout=zaman_asimi) as yanit:
            return {
                'durum': yanit.status,
                'basliklar': dict(yanit.headers),
                'govde': yanit.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'durum': e.code,
            'basliklar': {},
            'govde': e.read().decode('utf-8'),
        }


def post(url: str, veri: Any = None, json_veri: Any = None,
         basliklar: dict = None) -> dict:
    """
    HTTP POST isteği gönder.

    Args:
        url: Hedef URL
        veri: Form verisi (dict veya bytes)
        json_veri: JSON verisi
        basliklar: HTTP başlıkları
    """
    istek = urllib.request.Request(url, method='POST')
    if basliklar:
        for k, v in basliklar.items():
            istek.add_header(k, v)

    if json_veri is not None:
        govde = json.dumps(json_veri).encode('utf-8')
        istek.add_header('Content-Type', 'application/json')
        istek.data = govde
    elif veri is not None:
        if isinstance(veri, dict):
            istek.data = urllib.parse.urlencode(veri).encode('utf-8')
        elif isinstance(veri, bytes):
            istek.data = veri
        else:
            istek.data = str(veri).encode('utf-8')

    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            return {
                'durum': yanit.status,
                'basliklar': dict(yanit.headers),
                'govde': yanit.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'durum': e.code,
            'basliklar': {},
            'govde': e.read().decode('utf-8'),
        }


def put(url: str, veri: Any = None,
        json_veri: Any = None) -> dict:
    """HTTP PUT isteği gönder."""
    istek = urllib.request.Request(url, method='PUT')
    if json_veri is not None:
        govde = json.dumps(json_veri).encode('utf-8')
        istek.add_header('Content-Type', 'application/json')
        istek.data = govde
    elif veri is not None:
        istek.data = str(veri).encode('utf-8')

    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            return {
                'durum': yanit.status,
                'basliklar': dict(yanit.headers),
                'govde': yanit.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'durum': e.code,
            'basliklar': {},
            'govde': e.read().decode('utf-8'),
        }


def sil_istek(url: str) -> dict:
    """HTTP DELETE isteği gönder."""
    istek = urllib.request.Request(url, method='DELETE')
    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            return {
                'durum': yanit.status,
                'basliklar': dict(yanit.headers),
                'govde': yanit.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'durum': e.code,
            'basliklar': {},
            'govde': e.read().decode('utf-8'),
        }


def dosya_indir(url: str, yol: str) -> None:
    """Dosyayı URL'den indir."""
    urllib.request.urlretrieve(url, yol)


def url_kodla(parametreler: dict) -> str:
    """Parametreleri URL kodlaması ile çevir."""
    return urllib.parse.urlencode(parametreler)


def json_al(url: str, basliklar: dict = None) -> Any:
    """URL'den JSON verisi al."""
    yanit = get(url, basliklar)
    return json.loads(yanit['govde'])
