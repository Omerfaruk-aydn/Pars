"""
PARS Veritabanı Modülü — sqlite3 Türkçe sarmalayıcısı
"""

import sqlite3
from typing import Any, List, Optional, Tuple

__all__ = ['Veritabani']


class Veritabani:
    """
    SQLite veritabanı Türkçe sarmalayıcısı.

    Kullanım:
        vt = Veritabani('veriler.db')
        vt.tablo_olustur('kullanicilar', {'isim': 'TEXT', 'yas': 'INTEGER'})
        vt.ekle('kullanicilar', {'isim': 'Ahmet', 'yas': 25})
        sonuclar = vt.bul('kullanicilar')
        vt.kapat()
    """

    def __init__(self, dosya: str = ':memory:') -> None:
        """
        Veritabanı bağlantısı oluştur.

        Args:
            dosya: Veritabanı dosya yolu. ':memory:' ile bellek tabanlı.
        """
        self._dosya = dosya
        self._baglanti: Optional[sqlite3.Connection] = None
        self.baglan()

    def baglan(self) -> None:
        """Veritabanına bağlan."""
        self._baglanti = sqlite3.connect(self._dosya)
        self._baglanti.row_factory = sqlite3.Row

    def kapat(self) -> None:
        """Bağlantıyı kapat."""
        if self._baglanti:
            self._baglanti.close()
            self._baglanti = None

    def tablo_olustur(self, isim: str, sutunlar: dict) -> None:
        """
        Tablo oluştur.

        Args:
            isim: Tablo adı
            sutunlar: {sütun_adı: veri_tipi} sözlüğü
        """
        sutun_listesi = ', '.join(
            f'{ad} {tip}' for ad, tip in sutunlar.items()
        )
        sql = f'CREATE TABLE IF NOT EXISTS {isim} ({sutun_listesi})'
        self._baglanti.execute(sql)
        self._baglanti.commit()

    def ekle(self, tablo: str, veri: dict) -> int:
        """
        Tabloya kayıt ekle.

        Args:
            tablo: Tablo adı
            veri: {sütun_adı: değer} sözlüğü

        Returns:
            int: Eklenen satırın ID'si
        """
        anahtarlar = ', '.join(veri.keys())
        yer_tutucular = ', '.join(['?'] * len(veri))
        sql = f'INSERT INTO {tablo} ({anahtarlar}) VALUES ({yer_tutucular})'
        cursor = self._baglanti.execute(sql, list(veri.values()))
        self._baglanti.commit()
        return cursor.lastrowid

    def bul(self, tablo: str, kosul: str = None,
            parametreler: tuple = ()) -> list:
        """
        Tabloda kayıt ara.

        Args:
            tablo: Tablo adı
            kosul: WHERE koşulu (opsiyonel)
            parametreler: Koşul parametreleri

        Returns:
            list: Bulunan kayıtlar (sözlük listesi)
        """
        sql = f'SELECT * FROM {tablo}'
        if kosul:
            sql += f' WHERE {kosul}'
        cursor = self._baglanti.execute(sql, parametreler)
        return [dict(row) for row in cursor.fetchall()]

    def guncelle(self, tablo: str, veri: dict, kosul: str,
                 parametreler: tuple = ()) -> None:
        """
        Kayıt güncelle.

        Args:
            tablo: Tablo adı
            veri: Güncellenecek alanlar
            kosul: WHERE koşulu
            parametreler: Koşul parametreleri
        """
        atamalar = ', '.join(f'{k} = ?' for k in veri.keys())
        sql = f'UPDATE {tablo} SET {atamalar} WHERE {kosul}'
        tum_parametreler = list(veri.values()) + list(parametreler)
        self._baglanti.execute(sql, tum_parametreler)
        self._baglanti.commit()

    def sil(self, tablo: str, kosul: str,
            parametreler: tuple = ()) -> None:
        """
        Kayıt sil.

        Args:
            tablo: Tablo adı
            kosul: WHERE koşulu
            parametreler: Koşul parametreleri
        """
        sql = f'DELETE FROM {tablo} WHERE {kosul}'
        self._baglanti.execute(sql, parametreler)
        self._baglanti.commit()

    def sorgu(self, sql: str, parametreler: tuple = ()) -> list:
        """
        Ham SQL sorgusu çalıştır.

        Args:
            sql: SQL sorgusu
            parametreler: Sorgu parametreleri

        Returns:
            list: Sonuç satırları
        """
        cursor = self._baglanti.execute(sql, parametreler)
        return [dict(row) for row in cursor.fetchall()]

    def islem_baslat(self) -> None:
        """İşlem başlat (BEGIN TRANSACTION)."""
        self._baglanti.execute('BEGIN TRANSACTION')

    def islem_kaydet(self) -> None:
        """İşlemi kaydet (COMMIT)."""
        self._baglanti.commit()

    def islem_geri_al(self) -> None:
        """İşlemi geri al (ROLLBACK)."""
        self._baglanti.rollback()

    def tablo_listele(self) -> list:
        """Tabloları listele."""
        cursor = self._baglanti.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        return [row[0] for row in cursor.fetchall()]

    def tablo_sil(self, isim: str) -> None:
        """Tabloyu sil."""
        self._baglanti.execute(f'DROP TABLE IF EXISTS {isim}')
        self._baglanti.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.kapat()
        return False

    def __repr__(self) -> str:
        return f'Veritabani(dosya={self._dosya!r})'
