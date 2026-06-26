# Değişiklik Günlüğü

## v1.0.0 (İlk Yayın)

### Dil Özellikleri
- Türkçe anahtar kelimeler (eğer, değilse, yoksa, iken, için, vb.)
- Türkçe yerleşik fonksiyonlar (yaz, girdial, uzunluk, tip, vb.)
- Türkçe veri yapıları (liste, sözlük, küme, demet)
- Türkçe mantıksal operatörler (ve, veya, değil)
- Türkçe değerler (doğru, yanlış, yok)
- `öz` parametresi (self yerine)
- Async/await desteği (eşzamansız/bekle)

### Motor
- Regex tabanlı tokenizer
- Türkçe → Python çevirici (transpiler)
- Satır numarası koruması
- String/yorum koruması
- f-string desteği

### Standart Kütüphane
- matematik: Math kütüphanesi Türkçe sarmalayıcısı
- metin: String işlemleri Türkçe sarmalayıcısı
- liste: List/dict/set yardımcıları
- dosya: Dosya I/O Türkçe sarmalayıcısı
- zaman: DateTime Türkçe sarmalayıcısı
- sistem: OS/Sys Türkçe sarmalayıcısı
- rastgele: Random/Secrets Türkçe sarmalayıcısı
- veri: JSON/CSV/Pickle Türkçe sarmalayıcısı
- ag: urllib Türkçe sarmalayıcısı
- veritabani: SQLite3 Türkçe sarmalayıcısı

### CLI
- Dosya çalıştırma
- Etkileşimli mod (REPL)
- Python karşılığını gösterme
- Sözdizimi kontrolü
- Paket yönetimi
- Proje iskeleti oluşturma

### Hata Yönetimi
- Tüm Python exception tipleri Türkçe karşılıkları
- Hatalı satır gösterimi
- Akıllı ipucu sistemi
- ANSI renkli terminal çıktısı

### Testler
- Tokenizer birim testleri
- Çevirici birim testleri
- Yürütücü entegrasyon testleri
- Hata yönetimi testleri
- Standart kütüphane testleri
- Tüm örnek dosyaları çalıştırma testi

### VS Code Eklentisi
- Sözdizimi renklendirme
- Otomatik tamamlama parantezleri
- Girinti desteği

### Dokümantasyon
- README.md (TR + EN)
- Sözdizimi Rehberi
- Yerleşik Fonksiyonlar referansı
- MkDocs dokümantasyon sitesi

### CI/CD
- GitHub Actions test workflow
- PyPI otomatik yayın
- GitHub Pages dokümantasyon
