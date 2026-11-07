"""
REPL testleri
"""

import pytest
from pars import __version__
from pars.cekirdek.repl import repl_baslat, PARS_SURUM, BANNER, YARDIM


class TestREPL:

    def test_surum(self):
        assert PARS_SURUM == __version__

    def test_banner(self):
        assert "PARS" in BANNER
        assert __version__ in BANNER
        assert "Pars gibi" in BANNER

    def test_yardim(self):
        assert "PARS" in YARDIM
        assert "fonksiyon" in YARDIM
        assert "yaz" in YARDIM
        assert ".yardim" in YARDIM or ".yardım" in YARDIM
