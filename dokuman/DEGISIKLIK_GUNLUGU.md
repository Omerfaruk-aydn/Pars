# Değişiklik Günlüğü

## v1.0.1 (Hata düzeltmeleri + genişletilmiş standart kütüphane)

### Yeni komutlar
- `parskur` — `pip` yerine PARS paket yöneticisi
  (`yükle`, `kaldır`, `güncelle`, `listele`, `göster`, `dışa`, `içe`, `ara`)
- `parspip` — `parskur` ile birebir aynı (`pip` yerine)
- `parspy` — `python` yerine PARS Python çalıştırıcısı
  (`dosya.py`, `-c`, `-m`, etkileşimli konsol)
- `pars derle` — PARS kodunu `.py` dosyasına derler
- `pars <dosya.kolay>` — Kolay PARS dosyalarını doğrudan çalıştırır
- `pars köprü` — Python kütüphanelerini PARS sözdizimine uyarlar
  (`<modül>`, `ara`, `dışa`, `doğrula`)
- `parskopru` — `pars köprü` için ayrı giriş noktası

### Uzantı ve adlandırma
- PARS kaynak uzantısı artık **`.pars`** (eski `.prs` uyumluluk için desteklenir)
- Tüm örnekler, testler, dokümanlar ve VS Code tanımı `.pars`'a geçirildi
- `pars` komutu `.pars`, `.prs`, `.kolay` ve `.py` dosyalarını çalıştırır
- Yerel `.pars`/`.prs` dosyaları `içe_aktar` ve `den_aktar` ile modül
  olarak yüklenebilir (paketler için `__init__.pars` desteklenir)
- UTF-8 BOM içeren kaynak dosyalar otomatik olarak normalize edilir

### Çekirdek düzeltmeleri
- Noktadan sonraki nitelikler artık çevrilmiyor (`dosya.sil` bozulmuyor)
- `süper()` doğru şekilde `super()`'a çevriliyor (kalıtım hatası giderildi)
- `dir()` yerleşik fonksiyonu `is` anahtar kelimesiyle çakışmıyor
- `...` sonrası anahtar kelimeler nitelik sanılmıyor
- f-string içindeki Türkçe ifadeler çevriliyor (`f"{doğru}"` → `f"{True}"`)
- Sayı tokenları: hex, binary, octal, üs, alt çizgi ve karmaşık sayılar
- String önekleri: `r`, `b`, `rb`, `br`, `f`, `fr` ve üçlü tırnaklar
- Türkçe üçlü koşul: `A eğer koşul değilse B`
- Dekoratör adları (`@sınıf_metot`, `@statik_metot`) çevriliyor
- `girdial` artık dinamik `input()` çağırıyor (test/mock uyumlu)
- REPL standart kütüphaneyi hazır yükler; `.gecmis`, `.sozdizimi` eklendi
- `zaman.sleep`, `zaman.time`, `zaman.perf_counter` uyumluluk takma adları
- `yaz(..., ayraç="-")` Türkçe parametre desteği

### Standart kütüphane (10 → 28 modül)
- Yeni: `istatistik`, `koleksiyonlar`, `yinelenebilirler`, `fonksiyonel`,
  `yol`, `takvim`, `isletim`, `surec`, `iplik`, `gunluk`, `sifreleme`,
  `sikistirma`, `sayi`, `kopya`, `veri_siniflari`, `arguman`, `deneme`,
  `kopru`
- Genişletildi: `matematik`, `metin`, `liste`, `zaman`
- `içe_aktar matematik` artık sys.modules üzerinden çalışıyor
- `zaman.__all__` uyuşmazlığı giderildi

### Köprü sistemi (Python kütüphanesi uyarlama)
- `pars.kopru.bagla("modül")` bir Python kütüphanesini sarmalar
- Öznitelikler hem özgün (İngilizce) hem Türkçe adla erişilebilir
  (`yanit.status_code` ve `yanit.durum_kodu`)
- Çağrılarda anahtar sözcük argümanları da çevrilir
- Türkçe karakter normalizasyonu (`kullanıcı_adı` → `username`)
- `isinstance` korunur (`__class__` bildirilir); kapsayıcı/aritmetik
  protokolleri devredilir
- `pars köprü dışa <modül>` ile `.pars` sarmalayıcı dosyası üretilir
- Çeviri sözlüğü `sozluk_ekle` ile genişletilebilir

### Örnekler ve testler
- Bozuk 10 örnek düzeltildi; tümü gerçekten çalışıyor
- 21–30 arası 10 yeni örnek eklendi (toplam 31 `.pars`)
- `test_ornekler` artık başarısız örnekleri gizlemiyor
- Uzantı (`.pars`) ve köprü sistemi için yeni testler
- Toplam 332 test geçiyor

### Dokümantasyon
- README, sözdizimi rehberi ve standart kütüphane belgeleri güncellendi
- Ayrılmış sözcükler ve yeni komutlar belgelendi

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
