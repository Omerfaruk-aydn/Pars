"""
PARS Rastgele Modülü — random/secrets Türkçe sarmalayıcısı
"""

import random
import secrets
import uuid
from typing import Any, Sequence

__all__ = [
    'rastgele_sayi', 'rastgele_ondalikli', 'rastgele_sec',
    'rastgele_karistir', 'rastgele_ornek', 'rastgele_agirlikli',
    'rastgele_metin', 'rastgele_id', 'tohum_ata',
]


def rastgele_sayi(baslangic: int, son: int) -> int:
    """Rastgele tamsayı üret [başlangıç, son]."""
    return random.randint(baslangic, son)


def rastgele_ondalikli(baslangic: float = 0.0,
                       son: float = 1.0) -> float:
    """Rastgele ondalıklı sayı üret."""
    return random.uniform(baslangic, son)


def rastgele_sec(liste: Sequence) -> Any:
    """Listeden rastgele bir eleman seç."""
    return random.choice(liste)


def rastgele_karistir(liste: list) -> list:
    """Listeyi karıştır (yeni kopya döndür)."""
    kopya = list(liste)
    random.shuffle(kopya)
    return kopya


def rastgele_ornek(liste: Sequence, n: int) -> list:
    """Listeden rastgele n eleman seç (tekrarsız)."""
    return random.sample(liste, n)


def rastgele_agirlikli(liste: Sequence, agirliklar: Sequence) -> Any:
    """Ağırlıklı rastgele seçim."""
    return random.choices(liste, weights=agirliklar, k=1)[0]


def rastgele_metin(uzunluk: int = 16) -> str:
    """Güvenli rastgele metin üret (secrets kullanır)."""
    karakterler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(secrets.choice(karakterler) for _ in range(uzunluk))


def rastgele_id() -> str:
    """Benzersiz kimlik üret (UUID4)."""
    return str(uuid.uuid4())


def tohum_ata(tohum: int) -> None:
    """Rastgele sayı üretecine tohum ata."""
    random.seed(tohum)
