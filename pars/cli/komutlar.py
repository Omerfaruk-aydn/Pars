"""
PARS CLI Komutları
------------------
Komut satırı arayüzü.

Kullanım:
  pars <dosya.prs>           → .prs dosyası çalıştır
  pars -g                    → Etkileşimli mod (REPL)
  pars -cevir <dosya.prs>    → Python karşılığını göster
  pars -p <dosya.prs>        → Çalıştır + Python kodunu göster
  pars -kontrol <dosya.prs>  → Sözdizimi kontrolü (çalıştırma)
  pars -s / --surum          → Versiyon bilgisi
  pars paket yükle <paket>   → pip install <paket>
  pars paket kaldır <paket>  → pip uninstall <paket>
  pars paket listele         → pip list
  pars paket güncelle <paket> → pip install --upgrade <paket>
  pars yeni <proje_adı>      → Yeni proje iskeleti oluştur
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

from pars import __version__
from pars.cekirdek.ceviri import cevir, cevir_ve_goster, syntax_kontrol
from pars.cekirdek.yurutucu import calistir
from pars.cekirdek.repl import repl_baslat


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

    # Dizinleri oluştur
    yol.mkdir(parents=True)
    (yol / 'testler').mkdir()

    # ana.prs
    (yol / 'ana.prs').write_text(
        f'# {proje_adi} — PARS Projesi\n'
        f'# "Pars gibi hızlı. Türkçe gibi güzel."\n\n'
        f'yaz("{proje_adi} projesine hoş geldiniz!")\n\n'
        f'fonksiyon merhaba(isim: str) -> str:\n'
        f'    döndür f"Merhaba, {{isim}}!"\n\n'
        f'yaz(merhaba("Dünya"))\n',
        encoding='utf-8'
    )

    # kutuphane.prs
    (yol / 'kutuphane.prs').write_text(
        f'# {proje_adi} — Ortak Fonksiyonlar\n\n'
        f'fonksiyon bilgi():\n'
        f'    döndür "{proje_adi} v1.0.0"\n',
        encoding='utf-8'
    )

    # testler/test_ana.prs
    (yol / 'testler' / 'test_ana.prs').write_text(
        f'# {proje_adi} Testleri\n\n'
        f'den_aktar kutuphane içe_aktar bilgi\n\n'
        f'iddia bilgi() == "{proje_adi} v1.0.0"\n'
        f'yaz("Tüm testler geçti!")\n',
        encoding='utf-8'
    )

    # README.md
    (yol / 'README.md').write_text(
        f'# {proje_adi}\n\n'
        f'PARS ile yazılmış bir proje.\n\n'
        f'## Çalıştırma\n\n'
        f'```bash\npars ana.prs\n```\n',
        encoding='utf-8'
    )

    # .gitignore
    (yol / '.gitignore').write_text(
        '__pycache__/\n*.pyc\n.env\n*.egg-info/\ndist/\nbuild/\n',
        encoding='utf-8'
    )

    # gereksinimler.txt
    (yol / 'gereksinimler.txt').write_text(
        '# PARS projesi bağımlılıkları\n# pars paket yükle <paket_adı>\n',
        encoding='utf-8'
    )

    print(f'Proje oluşturuldu: {proje_adi}/')
    print(f'  cd {proje_adi}')
    print(f'  pars ana.prs')


def _paket_komutu(komut: str, paketler: list) -> None:
    """pip komutlarını çalıştır."""
    pip_komutlari = {
        'yükle': 'install',
        'yukle': 'install',
        'kaldır': 'uninstall',
        'kaldir': 'uninstall',
        'güncelle': 'install --upgrade',
        'guncelle': 'install --upgrade',
        'listele': 'list',
        'ara': 'search',
    }

    pip_komut = pip_komutlari.get(komut)
    if not pip_komut:
        print(f'Bilinmeyen paket komutu: {komut}', file=sys.stderr)
        sys.exit(1)

    cmd = [sys.executable, '-m', 'pip'] + pip_komut.split()
    if komut != 'listele':
        cmd.extend(paketler)

    subprocess.run(cmd)


def main() -> None:
    """CLI giriş noktası."""
    if len(sys.argv) < 2:
        repl_baslat()
        return

    komut = sys.argv[1]

    # Sürüm
    if komut in ('-s', '--surum', '--sürüm', '--version'):
        print(f'PARS v{__version__}')
        return

    # Yardım
    if komut in ('-h', '--help', '--yardım'):
        print(_yardim_metni())
        return

    # Etkileşimli mod
    if komut in ('-g', '--giris', '--giriş', '--repl'):
        repl_baslat()
        return

    # Paket yönetimi
    if komut in ('paket', 'pip'):
        if len(sys.argv) < 3:
            print('Kullanım: pars paket <komut> [paketler]', file=sys.stderr)
            sys.exit(1)
        alt_komut = sys.argv[2]
        paketler = sys.argv[3:]
        _paket_komutu(alt_komut, paketler)
        return

    # Yeni proje
    if komut in ('yeni', 'new'):
        if len(sys.argv) < 3:
            print('Kullanım: pars yeni <proje_adı>', file=sys.stderr)
            sys.exit(1)
        _yeni_proje_olustur(sys.argv[2])
        return

    # Çalıştır
    if komut in ('calistir', 'çalıştır'):
        if len(sys.argv) < 3:
            print('Kullanım: pars çalıştır <komut>', file=sys.stderr)
            sys.exit(1)
        subprocess.run(' '.join(sys.argv[2:]), shell=True)
        return

    # Dosya çevir
    if komut == '-cevir':
        if len(sys.argv) < 3:
            print('Kullanım: pars -cevir <dosya.prs>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(sys.argv[2])
        print(cevir_ve_goster(kod))
        return

    # Python kodunu göster + çalıştır
    if komut == '-p':
        if len(sys.argv) < 3:
            print('Kullanım: pars -p <dosya.prs>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(sys.argv[2])
        calistir(kod, dosya_adi=sys.argv[2], python_goster=True)
        return

    # Sözdizimi kontrolü
    if komut == '-kontrol':
        if len(sys.argv) < 3:
            print('Kullanım: pars -kontrol <dosya.prs>', file=sys.stderr)
            sys.exit(1)
        kod = _dosya_oku(sys.argv[2])
        gecerli, hata = syntax_kontrol(kod, sys.argv[2])
        if gecerli:
            print('Sözdizimi doğru.')
        else:
            print(f'Sözdizimi hatası: {hata}', file=sys.stderr)
            sys.exit(1)
        return

    # .prs dosyası çalıştır
    if komut.endswith('.prs') or Path(komut).exists():
        dosya_yolu = komut
        if not os.path.exists(dosya_yolu):
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


def _yardim_metni() -> str:
    """Yardım metnini döndür."""
    return f"""
PARS v{__version__} — Türkçe Programlama Dili
"Pars gibi hızlı. Türkçe gibi güzel."

Kullanım:
  pars <dosya.prs>            .prs dosyası çalıştır
  pars -g                     Etkileşimli mod (REPL)
  pars -cevir <dosya.prs>     Python karşılığını göster
  pars -p <dosya.prs>         Çalıştır + Python kodunu göster
  pars -kontrol <dosya.prs>   Sözdizimi kontrolü
  pars -s                     Versiyon bilgisi
  pars paket yükle <paket>    pip install
  pars paket kaldır <paket>   pip uninstall
  pars paket listele          pip list
  pars yeni <proje_adı>       Yeni proje oluştur
  pars çalıştır <komut>       Shell komutu çalıştır
"""


if __name__ == '__main__':
    main()
