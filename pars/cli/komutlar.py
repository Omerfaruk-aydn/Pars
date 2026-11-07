"""
PARS CLI Komutları
------------------
Komut satırı arayüzü.

Kullanım:
  pars <dosya.pars>          → .pars dosyası çalıştır
  pars <dosya.prs>           → Eski .prs dosyası çalıştır (uyumluluk)
  pars <dosya.kolay>         → Kolay PARS dosyası çalıştır
  pars <dosya.py>            → Python dosyası çalıştır (parspy gibi)
  pars -g                    → Etkileşimli mod (REPL)
  pars -cevir <dosya.pars>   → Python karşılığını göster
  pars -p <dosya.pars>       → Çalıştır + Python kodunu göster
  pars -kontrol <dosya.pars> → Sözdizimi kontrolü
  pars derle <dosya.pars>    → .py dosyasına derle
  pars köprü <modül>         → Python kütüphanesini PARS'a uyarla
  pars -s / --surum          → Versiyon bilgisi
  pars paket ...             → Paket yönetimi (parskur / parspip)
  pars python ...            → Python modu (parspy)
  pars yeni <proje_adı>      → Yeni proje iskeleti oluştur
  pars çalıştır <komut>      → Sistem komutu çalıştır
"""

import sys
import argparse
from pathlib import Path

from pars import __version__
from pars.cekirdek.ceviri import cevir, cevir_ve_goster, syntax_kontrol
from pars.cekirdek.yurutucu import calistir
from pars.cekirdek.repl import repl_baslat
from pars.cekirdek.kolay import kolay_dosya_calistir

PARS_UZANTILARI = ('.pars', '.prs')
KOLAY_UZANTILARI = ('.kolay',)


def _dosya_oku(dosya_yolu: str) -> str:
    """Dosyayı UTF-8 ile oku."""
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        return f.read()


def _yeni_proje_olustur(proje_adi: str) -> None:
    """Yeni PARS proje iskeleti oluştur."""
    yol = Path(proje_adi)
    if yol.exists():
        print(f'Hata: "{proje_adi}" dizini zaten var.', file=sys.stderr)
        sys.exit(1)

    yol.mkdir(parents=True)
    (yol / 'testler').mkdir()

    (yol / 'ana.pars').write_text(
        f'# {proje_adi} — PARS Projesi\n'
        f'# "Pars gibi hızlı. Türkçe gibi güzel."\n\n'
        f'yaz("{proje_adi} projesine hoş geldiniz!")\n\n'
        f'fonksiyon merhaba(isim: str) -> str:\n'
        f'    döndür f"Merhaba, {{isim}}!"\n\n'
        f'yaz(merhaba("Dünya"))\n',
        encoding='utf-8'
    )

    (yol / 'kutuphane.pars').write_text(
        f'# {proje_adi} — Ortak Fonksiyonlar\n\n'
        f'fonksiyon bilgi() -> str:\n'
        f'    döndür "{proje_adi} v1.0.0"\n',
        encoding='utf-8'
    )

    (yol / 'testler' / 'test_ana.pars').write_text(
        f'# {proje_adi} Testleri\n\n'
        f'den_aktar kutuphane içe_aktar bilgi\n\n'
        f'iddia bilgi() == "{proje_adi} v1.0.0"\n'
        f'yaz("Tüm testler geçti!")\n',
        encoding='utf-8'
    )

    (yol / 'README.md').write_text(
        f'# {proje_adi}\n\n'
        f'PARS ile yazılmış bir proje.\n\n'
        f'## Çalıştırma\n\n'
        f'```bash\npars ana.pars\n```\n\n'
        f'## Bağımlılıklar\n\n'
        f'```bash\nparskur yükle <paket>\n```\n',
        encoding='utf-8'
    )

    (yol / '.gitignore').write_text(
        '__pycache__/\n*.pyc\n.env\n*.egg-info/\ndist/\nbuild/\n',
        encoding='utf-8'
    )

    (yol / 'gereksinimler.txt').write_text(
        '# PARS projesi bağımlılıkları\n'
        '# Yüklemek için: parskur içe gereksinimler.txt\n',
        encoding='utf-8'
    )

    print(f'Proje oluşturuldu: {proje_adi}/')
    print(f'  cd {proje_adi}')
    print('  pars ana.pars')


def _derle(dosya_yolu: str, hedef: str = None) -> None:
    """PARS dosyasını Python dosyasına derle."""
    kod = _dosya_oku(dosya_yolu)
    python_kodu = cevir(kod)
    if hedef is None:
        hedef = str(Path(dosya_yolu).with_suffix('.py'))
    Path(hedef).write_text(python_kodu, encoding='utf-8')
    print(f'Derlendi: {hedef}')


def _yardim_metni() -> str:
    return f"""
PARS v{__version__} — Türkçe Programlama Dili
"Pars gibi hızlı. Türkçe gibi güzel."

Kullanım:
  pars <dosya.pars>           .pars (ve eski .prs) dosyası çalıştır
  pars <dosya.kolay>          Kolay PARS dosyası çalıştır
  pars <dosya.py>             Python dosyası çalıştır
  pars -g                     Etkileşimli mod (REPL)
  pars -cevir <dosya.pars>    Python karşılığını göster
  pars -p <dosya.pars>        Çalıştır + Python kodunu göster
  pars -kontrol <dosya.pars>  Sözdizimi kontrolü
  pars derle <dosya.pars>     Python dosyasına derle
  pars köprü <modül>          Python kütüphanesini PARS'a uyarla
  pars köprü dışa <modül>     PARS sarmalayıcı (.pars) dosyası üret
  pars -s                     Versiyon bilgisi
  pars yeni <proje_adı>       Yeni proje oluştur
  pars çalıştır <komut>       Sistem komutu çalıştır

Ayrı komutlar:
  parskur yükle <paket>       Paket yükle (pip yerine)
  parspip yükle <paket>       parskur ile aynı (pip yerine)
  parskur kaldır <paket>      Paket kaldır
  parskur listele             Yüklü paketleri listele
  parspy <dosya.py>           Python dosyası çalıştır (python yerine)
  parspy -c "kod"             Python kodu çalıştır

Daha fazla: https://parsdil.com
"""


def _arguman_ayristirici() -> argparse.ArgumentParser:
    ay = argparse.ArgumentParser(
        prog='pars',
        description='PARS — Türkçe Programlama Dili',
        add_help=False,
    )
    ay.add_argument('komut', nargs='?')
    ay.add_argument('argumanlar', nargs=argparse.REMAINDER)
    return ay


def main(argv=None) -> None:
    """CLI giriş noktası."""
    argumanlar = list(sys.argv[1:] if argv is None else argv)

    if not argumanlar:
        repl_baslat()
        return

    komut = argumanlar[0]
    kalan = argumanlar[1:]

    # Sürüm
    if komut in ('-s', '--surum', '--sürüm', '--version'):
        print(f'PARS v{__version__}')
        return

    # Yardım
    if komut in ('-h', '--help', '--yardım', '--yardim', 'yardim', 'yardım'):
        print(_yardim_metni())
        return

    # Etkileşimli mod
    if komut in ('-g', '--giris', '--giriş', '--repl'):
        repl_baslat()
        return

    # Paket yönetimi → parskur / parspip
    if komut in ('paket', 'parskur', 'parspip', 'pip'):
        from pars.cli.paket import main as paket_main
        sys.exit(paket_main(kalan))
        return

    # Python modu → parspy
    if komut in ('python', 'parspy'):
        from pars.cli.python_modu import main as python_main
        sys.exit(python_main(kalan))
        return

    # Python kütüphanesi köprüsü
    if komut in ('köprü', 'kopru', 'bridge'):
        from pars.cli.kopru import main as kopru_main
        sys.exit(kopru_main(kalan))
        return

    # Yeni proje
    if komut in ('yeni', 'new'):
        if not kalan:
            print('Kullanım: pars yeni <proje_adı>', file=sys.stderr)
            sys.exit(1)
        _yeni_proje_olustur(kalan[0])
        return

    # Sistem komutu çalıştır (güvenli: kabuk yok)
    if komut in ('calistir', 'çalıştır'):
        if not kalan:
            print('Kullanım: pars çalıştır <komut>', file=sys.stderr)
            sys.exit(1)
        from pars.standart.surec import calistir as surec_calistir
        sonuc = surec_calistir(kalan)
        sys.stdout.write(sonuc['cikti'])
        sys.stderr.write(sonuc['hata'])
        sys.exit(sonuc['kod'])
        return

    # Dosya çevir
    if komut in ('-cevir', 'cevir', 'çevir'):
        if not kalan:
            print('Kullanım: pars -cevir <dosya.pars>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(kalan[0])
        print(cevir_ve_goster(kod))
        return

    # Python kodunu göster + çalıştır
    if komut == '-p':
        if not kalan:
            print('Kullanım: pars -p <dosya.pars>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(kalan[0])
        calistir(kod, dosya_adi=kalan[0], python_goster=True)
        return

    # Sözdizimi kontrolü
    if komut in ('-kontrol', 'kontrol'):
        if not kalan:
            print('Kullanım: pars -kontrol <dosya.pars>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(kalan[0])
        gecerli, hata = syntax_kontrol(kod, kalan[0])
        if gecerli:
            print('Sözdizimi doğru.')
        else:
            print(f'Sözdizimi hatası: {hata}', file=sys.stderr)
            sys.exit(1)
        return

    # Derle
    if komut in ('derle', 'compile'):
        if not kalan:
            print('Kullanım: pars derle <dosya.pars> [-o çıktı.py]',
                  file=sys.stderr)
            sys.exit(1)
        hedef = None
        if '-o' in kalan:
            i = kalan.index('-o')
            if i + 1 < len(kalan):
                hedef = kalan[i + 1]
        _derle(kalan[0], hedef)
        return

    # .kolay dosyası çalıştır
    if komut.endswith(KOLAY_UZANTILARI):
        kod = kolay_dosya_calistir(komut)
        basarili = calistir(kod, dosya_adi=komut)
        if not basarili:
            sys.exit(1)
        return

    # .py dosyası → parspy gibi çalıştır
    if komut.endswith('.py') and Path(komut).exists():
        from pars.cli.python_modu import main as python_main
        sys.exit(python_main([komut] + list(kalan)))
        return

    # .pars / .prs (uyumluluk) / diğer mevcut dosyalar
    if komut.endswith(PARS_UZANTILARI) or Path(komut).exists():
        dosya_yolu = komut
        if not Path(dosya_yolu).exists():
            print(f'Dosya bulunamadı: {dosya_yolu}', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(dosya_yolu)
        basarili = calistir(kod, dosya_adi=dosya_yolu)
        if not basarili:
            sys.exit(1)
        return

    print(f'Bilinmeyen komut: {komut}', file=sys.stderr)
    print('Yardım için: pars --yardım', file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main()
