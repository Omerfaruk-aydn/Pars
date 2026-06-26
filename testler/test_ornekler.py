"""
Ornekler klasöründeki tüm .prs dosyalarını çalıştırır.
Hata veren dosya testi başarısız sayar.
"""

import pytest
from pathlib import Path
from pars.cekirdek.yurutucu import calistir
from unittest.mock import patch

ORNEKLER_DIZIN = Path(__file__).parent.parent / 'ornekler'


def ornek_dosyalari():
    return list(ORNEKLER_DIZIN.glob('*.prs'))


@pytest.mark.parametrize('dosya', ornek_dosyalari(),
                         ids=lambda d: d.name)
def test_ornek_calisir(dosya, monkeypatch, capsys):
    """Örnek dosya çalıştırılabilir olmalı."""
    # girdial çağrılarını mockla
    monkeypatch.setattr('builtins.input', lambda *a, **k: 'test_girdisi')

    # Flask, asyncio gibi blocking çağrıları engelle
    with patch('time.sleep'):
        kod = dosya.read_text(encoding='utf-8')

        # Import hataları (numpy yok vb.) başarısız sayılmaz
        # Gerçek PARS hataları başarısız sayılır
        try:
            sonuc = calistir(kod, dosya_adi=str(dosya))
        except ImportError:
            # Eksik kütüphane - test atlanır
            pytest.skip(f"Eksik kütüphane: {dosya.name}")
