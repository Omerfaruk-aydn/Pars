# Katkı Rehberi

PARS'a katkıda bulunmak için bu rehberi izleyin.

## Başlangıç

1. Depoyu forklayın
2. Klonlayın: `git clone https://github.com/kullanici/pars.git`
3. Branch oluşturun: `git checkout -b ozellik/yeni-ozellik`
4. Değişikliklerinizi yapın
5. Testleri çalıştırın: `pytest testler/`
6. Commit edin: `git commit -m "Yeni özellik eklendi"`
7. Push edin: `git push origin ozellik/yeni-ozellik`
8. PR oluşturun

## Geliştirme Ortamı

```bash
# Depoyu klonla
git clone https://github.com/pars-lang/pars.git
cd pars

# Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Bağımlılıkları kur
pip install -e ".[dev]"

# Testleri çalıştır
pytest testler/
```

## Kod Standartları

- PEP 8 uyumlu (Türkçe tanımlayıcılar hariç)
- Maksimum satır uzunluğu: 100 karakter
- Her fonksiyon ve sınıf için Türkçe docstring
- Tüm fonksiyonlarda tip ipuçları
- `black` ile otomatik biçimlendirme
- `flake8` ile linting

## Test Yazma

```python
# testler/test_ornek.py
import pytest
from pars.cekirdek.ceviri import cevir

class TestOrnek:
    def test_ornek(self):
        assert cevir("eğer x > 0:") == "if x > 0:"
```

## Pull Request Kuralları

- Her PR için test ekleyin
- Dokümantasyonu güncelleyin
- CHANGELOG.md'yi güncelleyin
- Tek bir konuya odaklanın
- Açıklama yazın

## Hata Raporlama

GitHub Issues üzerinden hata bildirin:
- PARS sürümü
- Python sürümü
- İşletim sistemi
- Hata mesajı
- Beklenen davranış
- Gerçek davranış

## Özellik Önerisi

GitHub Discussions üzerinden önerin:
- Ne yapmak istiyorsunuz?
- Neden bu özellik gerekli?
- Örnek kullanım senaryosu

## Sorular

GitHub Discussions üzerinden sorun: https://github.com/pars-lang/pars/discussions
