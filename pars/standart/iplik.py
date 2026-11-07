"""
PARS İplik Modülü — threading / concurrent.futures Türkçe sarmalayıcısı
"""

import queue
import threading
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
    as_completed,
    wait,
)
from typing import Any, Callable, Iterable, List, Optional

__all__ = [
    'Iplik', 'Kilit', 'Olay', 'Kosul', 'Semafor', 'Kuyruk',
    'Havuz', 'SurecHavuzu', 'paralel_calistir', 'tamamlananlar',
    'bekle_hepsi', 'gecikmeli',
]


class Iplik:
    """threading.Thread Türkçe sarmalayıcısı."""

    def __init__(self, hedef: Callable, *args: Any,
                 isim: Optional[str] = None,
                 daemon: bool = False, **kwargs: Any) -> None:
        self._iplik = threading.Thread(
            target=hedef, args=args, kwargs=kwargs,
            name=isim, daemon=daemon,
        )

    def baslat(self) -> 'Iplik':
        self._iplik.start()
        return self

    def katil(self, zaman_asimi: Optional[float] = None) -> None:
        self._iplik.join(timeout=zaman_asimi)

    def calisiyor_mu(self) -> bool:
        return self._iplik.is_alive()

    @property
    def isim(self) -> str:
        return self._iplik.name


Kilit = threading.Lock
Olay = threading.Event
Kosul = threading.Condition
Semafor = threading.Semaphore
Kuyruk = queue.Queue


class Havuz:
    """ThreadPoolExecutor Türkçe sarmalayıcısı (bağlam yöneticisi)."""

    def __init__(self, isci_sayisi: Optional[int] = None) -> None:
        self._havuz = ThreadPoolExecutor(max_workers=isci_sayisi)

    def gonder(self, fonksiyon: Callable, *args: Any, **kwargs: Any):
        return self._havuz.submit(fonksiyon, *args, **kwargs)

    def haritala(self, fonksiyon: Callable, yinelenebilir: Iterable[Any]):
        return self._havuz.map(fonksiyon, yinelenebilir)

    def kapat(self, bekle: bool = True) -> None:
        self._havuz.shutdown(wait=bekle)

    def __enter__(self) -> 'Havuz':
        return self

    def __exit__(self, *args: Any) -> bool:
        self.kapat()
        return False


class SurecHavuzu:
    """ProcessPoolExecutor Türkçe sarmalayıcısı."""

    def __init__(self, isci_sayisi: Optional[int] = None) -> None:
        self._havuz = ProcessPoolExecutor(max_workers=isci_sayisi)

    def gonder(self, fonksiyon: Callable, *args: Any, **kwargs: Any):
        return self._havuz.submit(fonksiyon, *args, **kwargs)

    def kapat(self, bekle: bool = True) -> None:
        self._havuz.shutdown(wait=bekle)

    def __enter__(self) -> 'SurecHavuzu':
        return self

    def __exit__(self, *args: Any) -> bool:
        self.kapat()
        return False


def paralel_calistir(fonksiyon: Callable,
                     yinelenebilir: Iterable[Any],
                     isci_sayisi: Optional[int] = None) -> List[Any]:
    """Fonksiyonu elemanlara paralel uygula."""
    with ThreadPoolExecutor(max_workers=isci_sayisi) as havuz:
        return list(havuz.map(fonksiyon, yinelenebilir))


def tamamlananlar(gorevler: Iterable[Any]) -> list:
    """Tamamlanan görevleri döndür."""
    return list(as_completed(gorevler))


def bekle_hepsi(gorevler: Iterable[Any],
                zaman_asimi: Optional[float] = None) -> tuple:
    """Tüm görevlerin bitmesini bekle: (bitti, bitmedi)."""
    return wait(gorevler, timeout=zaman_asimi)


def gecikmeli(saniye: float, fonksiyon: Optional[Callable] = None,
              *args: Any) -> None:
    """Belirtilen süre sonra çalıştır (zamanlayıcı)."""
    if fonksiyon is None:
        import time
        time.sleep(saniye)
        return
    zamanlayici = threading.Timer(saniye, fonksiyon, args=args)
    zamanlayici.start()
