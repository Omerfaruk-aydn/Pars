"""
PARS Çekirdek Motor

Bu modül PARS dilinin temel motor bileşenlerini içerir:
  - esleme: Anahtar kelime ve built-in eşlemeleri
  - tokenizer: Regex tabanlı tokenizer
  - ceviri: Türkçe → Python çevirici (transpiler)
  - yurutucu: Kod derleme ve çalıştırma motoru
  - hatalar: Türkçe hata yakalama ve gösterimi
  - repl: Etkileşimli konsol (REPL)
"""

__all__ = [
    "esleme",
    "tokenizer",
    "ceviri",
    "yurutucu",
    "hatalar",
    "repl",
]
