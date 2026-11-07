"""
Örnek dosyaların gerçekten çalıştığını doğrular.

v1.0.1: Bu test önceden calistir() sonucunu kontrol etmiyordu ve
bozuk örnekler bile "geçiyor" görünüyordu. Artık her örnek True dönmeli.
"""

import pytest
from pathlib import Path
from unittest.mock import patch

from pars.cekirdek.yurutucu import calistir

ORNEKLER_DIZIN = Path(__file__).parent.parent / 'ornekler'


def ornek_dosyalari():
    return sorted(ORNEKLER_DIZIN.glob('*.pars'))


@pytest.mark.parametrize('dosya', ornek_dosyalari(),
                         ids=lambda d: d.name)
def test_ornek_calisir(dosya, monkeypatch, capsys):
    """Her örnek dosya hatasız çalışmalı (çıktı yakalanır)."""
    # Girdi bekleyen örnekler için güvenli sahte girdi
    monkeypatch.setattr('builtins.input', lambda *a, **k: '0')

    kod = dosya.read_text(encoding='utf-8')

    # Ağ ve sunucu örnekleri ortam değişkeniyle atlanır
    monkeypatch.delenv('PARS_ORNEK_AG', raising=False)
    monkeypatch.delenv('PARS_ORNEK_FLASK', raising=False)

    with patch('time.sleep'):
        sonuc = calistir(kod, dosya_adi=str(dosya))

    assert sonuc is True, f'{dosya.name} çalıştırılamadı'
    capsys.readouterr()


def test_en_az_30_ornek_var():
    """Standart kütüphane genişledikçe örnek sayısı da artmalı."""
    assert len(ornek_dosyalari()) >= 30
