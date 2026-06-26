"""
PARS Test Fixtures
"""

import pytest
from pars.cekirdek.yurutucu import calistir, ad_alani_olustur


@pytest.fixture
def pars_alani():
    """PARS çalıştırma alanı oluştur."""
    return ad_alani_olustur('<test>')


@pytest.fixture
def calistir_helper():
    """PARS kodunu çalıştır ve sonucu döndür."""
    def _calistir(kod: str, python_goster: bool = False) -> bool:
        return calistir(kod, dosya_adi='<test>', python_goster=python_goster)
    return _calistir
