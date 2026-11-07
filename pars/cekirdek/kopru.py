"""
PARS Köprü Sistemi
------------------
Var olan Python kütüphanelerini PARS sözdizimine uyarlar.

Amaç: `pip` ile kurulmuş herhangi bir Python kütüphanesini, Türkçe
öznitelik adlarıyla kullanabilmek. Örneğin ``requests`` kütüphanesinde
``response.status_code`` yerine ``yanit.durum_kodu`` yazılabilir.

Tasarım:
  * ``bagla("modul")`` bir :class:`Kopru` sarmalayıcısı döndürür.
  * Sarmalayıcı, özgün (İngilizce) adları olduğu gibi destekler.
  * Ek olarak, bilinen sözcükler Türkçeye çevrilerek aranır
    (``status_code`` → ``durum_kodu``).
  * Çağrılarda anahtar sözcük argümanları da çevrilir.

Sınırlar:
  * Bu bir *isim/sözdizimi uyarlama* katmanıdır; kütüphanenin kendi
    dilbilgisini (DSL) çevirmez.
  * Çeviri sözlüğü kapsamı dışındaki adlar özgün hâliyle kullanılır.
  * ``isinstance`` çalışır (sarmalayıcı ``__class__`` bildirir), ancak
    bazı kimlik/performans davranışları özgün nesneden farklı olabilir.
"""

from __future__ import annotations

import importlib
import sys
import types
from typing import Any, Dict, Iterable, Optional

__all__ = [
    'Kopru', 'bagla', 'kutuphane_yukle', 'turkce_ad', 'ingilizce_ad',
    'ceviri_sozlugu', 'sozluk_ekle', 'disa_aktar', 'ozellik_listesi',
]


#: İngilizce -> Türkçe sözcük eşlemesi. Anahtar sözcükler alt çizgi ile
#: ayrılmış parçalar hâlinde çevrilir (``status_code`` → ``durum_kodu``).
KELIMELER: Dict[str, str] = {
    # --- temel fiiller ---
    'get': 'al', 'set': 'ayarla', 'put': 'koy', 'post': 'gonder',
    'delete': 'sil', 'remove': 'kaldir', 'add': 'ekle', 'insert': 'ekle',
    'append': 'ekle', 'extend': 'genislet', 'update': 'guncelle',
    'create': 'olustur', 'build': 'kur', 'make': 'yap', 'run': 'calistir',
    'start': 'baslat', 'stop': 'durdur', 'close': 'kapat', 'open': 'ac',
    'read': 'oku', 'write': 'yaz', 'load': 'yukle', 'save': 'kaydet',
    'dump': 'dok', 'dumps': 'dok_metin', 'loads': 'yukle_metin',
    'store': 'sakla', 'fetch': 'getir', 'send': 'gonder',
    'receive': 'al', 'push': 'it', 'pop': 'cikar', 'peek': 'bak',
    'find': 'bul', 'search': 'ara', 'query': 'sorgula', 'filter': 'filtrele',
    'sort': 'sirala', 'reverse': 'tersine', 'map': 'haritala',
    'reduce': 'indirge', 'merge': 'birlestir', 'split': 'bol',
    'join': 'birlestir', 'parse': 'ayristir', 'format': 'bicimle',
    'encode': 'kodla', 'decode': 'coz', 'encrypt': 'sifrele',
    'decrypt': 'sifre_coz', 'hash': 'ozetle', 'sign': 'imzala',
    'verify': 'dogrula', 'validate': 'dogrula', 'check': 'kontrol_et',
    'test': 'dene', 'call': 'cagir', 'invoke': 'cagir', 'apply': 'uygula',
    'execute': 'yurut', 'eval': 'degerlendir', 'compile': 'derle',
    'install': 'yukle', 'uninstall': 'kaldir', 'upgrade': 'guncelle',
    'download': 'indir', 'upload': 'yukle', 'connect': 'baglan',
    'disconnect': 'ayril', 'login': 'giris', 'logout': 'cikis',
    'register': 'kaydet', 'unregister': 'kaydi_sil', 'subscribe': 'abone_ol',
    'unsubscribe': 'abonelikten_cik', 'publish': 'yayinla',
    'notify': 'bildir', 'emit': 'yay', 'listen': 'dinle', 'wait': 'bekle',
    'sleep': 'uyu', 'lock': 'kilitle', 'unlock': 'kilidi_ac',
    'acquire': 'edin', 'release': 'birak', 'reset': 'sifirla',
    'clear': 'temizle', 'clean': 'temizle', 'flush': 'bosalt',
    'copy': 'kopyala', 'clone': 'klonla', 'move': 'tasi', 'rename': 'yeniden_adlandir',
    'replace': 'degistir', 'render': 'gorsellestir', 'draw': 'ciz',
    'plot': 'grafikle', 'show': 'goster', 'hide': 'gizle', 'display': 'goster',
    'print': 'yazdir', 'log': 'kaydet', 'debug': 'hata_ayikla',
    'warn': 'uyar', 'error': 'hata', 'info': 'bilgi', 'trace': 'izle',
    'init': 'baslat', 'initialize': 'baslat', 'setup': 'kur',
    'configure': 'yapilandir', 'register_hook': 'kanca_ekle',
    'enable': 'etkinlestir', 'disable': 'devre_disi',
    'activate': 'etkinlestir', 'deactivate': 'devre_disi',
    'subscribe_event': 'olay_abone_ol', 'dispatch': 'gonder',
    'handle': 'isle', 'process': 'isle', 'transform': 'donustur',
    'convert': 'donustur', 'normalize': 'normallestir',
    'analyze': 'analiz_et', 'calculate': 'hesapla', 'compute': 'hesapla',
    'evaluate': 'degerlendir', 'score': 'puanla', 'predict': 'tahmin_et',
    'fit': 'uyarla', 'train': 'egit', 'test_model': 'modeli_dene',
    'open_file': 'dosya_ac', 'read_file': 'dosya_oku',
    'write_file': 'dosya_yaz', 'save_file': 'dosya_kaydet',
    # --- isimler ---
    'name': 'ad', 'names': 'adlar', 'title': 'baslik', 'label': 'etiket',
    'value': 'deger', 'values': 'degerler', 'data': 'veri', 'dataset': 'veri_kumesi',
    'result': 'sonuc', 'results': 'sonuclar', 'response': 'yanit',
    'request': 'istek', 'status': 'durum', 'code': 'kod',
    'status_code': 'durum_kodu', 'message': 'mesaj', 'error': 'hata',
    'errors': 'hatalar', 'warning': 'uyari', 'info': 'bilgi',
    'type': 'tur', 'kind': 'cesit', 'category': 'kategori',
    'size': 'boyut', 'length': 'uzunluk', 'count': 'sayi', 'total': 'toplam',
    'amount': 'miktar', 'number': 'sayi', 'index': 'dizin',
    'key': 'anahtar', 'keys': 'anahtarlar', 'item': 'oge', 'items': 'ogeler',
    'element': 'oge', 'elements': 'ogeler', 'entry': 'girdi',
    'entries': 'girdiler', 'record': 'kayit', 'records': 'kayitlar',
    'row': 'satir', 'rows': 'satirlar', 'column': 'sutun',
    'columns': 'sutunlar', 'field': 'alan', 'fields': 'alanlar',
    'table': 'tablo', 'tables': 'tablolar', 'database': 'veritabani',
    'file': 'dosya', 'files': 'dosyalar', 'folder': 'klasor',
    'directory': 'dizin', 'path': 'yol', 'filename': 'dosya_adi',
    'filepath': 'dosya_yolu', 'line': 'satir', 'lines': 'satirlar',
    'text': 'metin', 'string': 'metin', 'character': 'karakter',
    'char': 'karakter', 'word': 'kelime', 'words': 'kelimeler',
    'letter': 'harf', 'content': 'icerik', 'contents': 'icerik',
    'body': 'govde', 'header': 'baslik', 'headers': 'basliklar',
    'url': 'adres', 'uri': 'adres', 'link': 'baglanti', 'host': 'sunucu',
    'port': 'port', 'user': 'kullanici', 'username': 'kullanici_adi',
    'password': 'sifre', 'email': 'eposta', 'address': 'adres',
    'phone': 'telefon', 'id': 'kimlik', 'identifier': 'kimlik',
    'uuid': 'tekil_kimlik', 'token': 'jeton', 'session': 'oturum',
    'cookie': 'cerez', 'cookies': 'cerezler', 'cache': 'onbellek',
    'time': 'zaman', 'date': 'tarih', 'datetime': 'tarih_zaman',
    'timestamp': 'zaman_damgasi', 'duration': 'sure', 'interval': 'aralik',
    'start_time': 'baslangic_zamani', 'end_time': 'bitis_zamani',
    'created_at': 'olusturulma', 'updated_at': 'guncellenme',
    'day': 'gun', 'week': 'hafta', 'month': 'ay', 'year': 'yil',
    'hour': 'saat', 'minute': 'dakika', 'second': 'saniye',
    'min': 'en_az', 'max': 'en_cok', 'minimum': 'en_az', 'maximum': 'en_cok',
    'average': 'ortalama', 'mean': 'ortalama', 'median': 'medyan',
    'sum': 'toplam', 'product': 'carpim',
    'variance': 'varyans', 'std': 'std_sapma', 'deviation': 'sapma',
    'percentile': 'yuzdelik', 'rank': 'sira', 'order': 'duzen',
    'sort_order': 'siralama', 'limit': 'sinir', 'offset': 'kayma',
    'page': 'sayfa', 'pages': 'sayfalar', 'page_size': 'sayfa_boyutu',
    'end': 'bitis', 'first': 'ilk', 'last': 'son',
    'next': 'sonraki', 'previous': 'onceki', 'current': 'gecerli',
    'parent': 'ust', 'child': 'alt', 'children': 'altlar',
    'root': 'kok', 'node': 'dugum', 'nodes': 'dugumler',
    'tree': 'agac', 'graph': 'grafik', 'edge': 'kenar', 'edges': 'kenarlar',
    'vertex': 'tepe', 'vertices': 'tepeler', 'weight': 'agirlik',
    'shape': 'sekil', 'width': 'genislik', 'height': 'yukseklik',
    'color': 'renk', 'background': 'arka_plan', 'font': 'yazi_tipi',
    'image': 'resim', 'images': 'resimler', 'photo': 'fotograf',
    'video': 'video', 'audio': 'ses', 'sound': 'ses', 'media': 'medya',
    'model': 'model', 'models': 'modeller', 'layer': 'katman',
    'layers': 'katmanlar', 'input': 'girdi', 'inputs': 'girdiler',
    'output': 'cikti', 'outputs': 'ciktilar', 'target': 'hedef',
    'feature': 'ozellik', 'features': 'ozellikler', 'class': 'sinif',
    'classes': 'siniflar', 'object': 'nesne', 'objects': 'nesneler',
    'instance': 'ornek', 'method': 'yontem', 'methods': 'yontemler',
    'function': 'fonksiyon', 'functions': 'fonksiyonlar',
    'module': 'modul', 'modules': 'moduller', 'package': 'paket',
    'version': 'surum', 'config': 'yapilandirma', 'settings': 'ayarlar',
    'option': 'secenek', 'options': 'secenekler', 'default': 'varsayilan',
    'flag': 'bayrak', 'state': 'durum',
    'mode': 'kip', 'event': 'olay', 'events': 'olaylar',
    'handler': 'isleyici', 'callback': 'geri_cagri', 'listener': 'dinleyici',
    'worker': 'isci', 'workers': 'isciler', 'task': 'gorev', 'tasks': 'gorevler',
    'job': 'is', 'jobs': 'isler', 'queue': 'kuyruk', 'stack': 'yigin',
    'thread': 'is_parcacigi', 'pool': 'havuz',
    'mutex': 'kilit', 'semaphore': 'isaret',
    'connection': 'baglanti', 'client': 'istemci', 'server': 'sunucu',
    'socket': 'yuva', 'stream': 'akis', 'channel': 'kanal',
    'event_loop': 'olay_dongusu', 'loop': 'dongu', 'iter': 'yinele',
    'iterator': 'yineleyici', 'generator': 'uretec', 'sequence': 'dizi',
    'collection': 'koleksiyon', 'container': 'kap', 'buffer': 'tampon',
    'array': 'dizi', 'matrix': 'matris', 'vector': 'vektor',
    'tensor': 'tensor', 'frame': 'cerceve', 'window': 'pencere',
    'screen': 'ekran', 'view': 'gorunum', 'widget': 'bilesen',
    'button': 'dugme', 'menu': 'menu', 'dialog': 'ileti_penceresi',
    'form': 'form', 'panel': 'panel', 'layout': 'yerlesim',
    'style': 'bicim', 'theme': 'tema', 'icon': 'simge',
    'base': 'temel', 'default_value': 'varsayilan_deger',
    'required': 'zorunlu', 'optional': 'istege_bagli',
    'valid': 'gecerli', 'invalid': 'gecersiz', 'empty': 'bos',
    'full': 'dolu', 'null': 'bos', 'none': 'yok',
    'true': 'dogru', 'false': 'yanlis', 'yes': 'evet', 'no': 'hayir',
    'success': 'basarili', 'failure': 'basarisiz', 'failed': 'basarisiz',
    'enabled': 'etkin', 'disabled': 'devre_disi', 'active': 'etkin',
    'visible': 'gorunur', 'hidden': 'gizli',
    'closed': 'kapali', 'readonly': 'salt_okunur',
    'public': 'genel', 'private': 'ozel', 'protected': 'korunmus',
    'static': 'statik', 'async': 'eszamansiz', 'await': 'bekle',
    'source': 'kaynak', 'destination': 'hedef', 'target_path': 'hedef_yol',
    'source_path': 'kaynak_yol', 'template': 'sablon', 'pattern': 'desen',
    'regex': 'duzenli_ifade', 'match': 'eslesme', 'matches': 'eslesmeler',
    'group': 'grup', 'groups': 'gruplar', 'section': 'bolum',
    'chapter': 'bolum', 'part': 'parca', 'piece': 'parca',
    'chunk': 'parca', 'block': 'blok', 'segment': 'kesim',
    'unit': 'birim', 'units': 'birimler', 'scale': 'olcek',
    'ratio': 'oran', 'rate': 'oran', 'percent': 'yuzde',
    'level': 'seviye', 'priority': 'oncelik',
}

#: Türkçe -> İngilizce ters eşleme (aynı Türkçe karşılık birden fazla
#: İngilizce sözcüğe denk gelebilir; ilk kayıt kazanır).
_TERS: Dict[str, str] = {}
for _en, _tr in KELIMELER.items():
    _TERS.setdefault(_tr, _en)

#: Tek bir Türkçe sözcüğe karşılık gelen ek İngilizce adaylar. Sözlükte
#: aynı anahtar birden çok kez geçtiğinde (örn. ``start`` → ``baslat`` ve
#: ``baslangic``) kaybolan eşanlamları burada topluyoruz.
_ESANLAM: Dict[str, list] = {
    'baslat': ['start', 'run', 'begin'],
    'baslangic': ['start'],
    'ac': ['open'],
    'acik': ['open'],
    'isle': ['process', 'handle'],
    'surec': ['process'],
    'puanla': ['score'],
    'puan': ['score'],
    'tepe_deger': ['mode'],
    'kip': ['mode'],
    'durum': ['status', 'state'],
    'sil': ['delete', 'remove'],
    'kaldir': ['remove', 'delete'],
    'ekle': ['add', 'append', 'insert'],
    'al': ['get', 'receive', 'fetch'],
    'ver': ['set', 'put', 'send'],
    'gonder': ['send', 'post'],
    'guncelle': ['update'],
    'kaydet': ['save', 'store', 'log', 'register'],
    'yukle': ['load', 'install', 'upload'],
    'ara': ['search', 'find'],
    'bul': ['find', 'search'],
    'sirala': ['sort', 'order'],
    'boyut': ['size', 'length'],
    'uzunluk': ['length', 'size'],
    'sayi': ['count', 'number'],
    'toplam': ['total', 'sum'],
    'oku': ['read'],
    'yaz': ['write'],
    'kapat': ['close'],
    'baglan': ['connect'],
    'cagir': ['call', 'invoke'],
    'calistir': ['run', 'execute'],
    'yapilandir': ['configure', 'config'],
    'temizle': ['clear', 'clean'],
    'sifirla': ['reset'],
    'kilit': ['lock'],
    'kilitle': ['lock'],
}


#: Türkçe harfleri ASCII karşılıklarına indirger (ters arama için).
_TR_HARF = str.maketrans(
    'çğıöşüâîûÇĞİÖŞÜÂÎÛ',
    'cgiosuaiucgiosuaiu',
)


def _ascii(ad: str) -> str:
    return ad.translate(_TR_HARF)


def _birlestir(parcalar: Iterable[str]) -> str:
    return '_'.join(parcalar)


def _ayir(ad: str):
    """Baştaki/sondaki alt çizgileri gövdeden ayır."""
    onek = ''
    while ad.startswith('_'):
        onek += '_'
        ad = ad[1:]
    son_ek = ''
    while ad.endswith('_') and ad:
        son_ek += '_'
        ad = ad[:-1]
    return onek, ad, son_ek


def _cevir_ad(ad: str, sozluk: Dict[str, str]) -> str:
    if not ad:
        return ad
    if ad.startswith('__') and ad.endswith('__'):
        return ad
    onek, govde, son_ek = _ayir(ad)
    if govde in sozluk:
        return onek + sozluk[govde] + son_ek
    ascii_govde = _ascii(govde)
    if ascii_govde in sozluk:
        return onek + sozluk[ascii_govde] + son_ek
    parcalar = [sozluk.get(_ascii(p), p) for p in govde.split('_')]
    return onek + _birlestir(parcalar) + son_ek


def turkce_ad(ad: str) -> str:
    """İngilizce bir adı Türkçeye çevir (tam ad, sonra parça parça)."""
    return _cevir_ad(ad, KELIMELER)


def ingilizce_ad(ad: str) -> str:
    """Türkçe bir adı İngilizceye çevir (tam ad, sonra parça parça)."""
    return _cevir_ad(ad, _TERS)


def ingilizce_adlar(ad: str) -> list:
    """Bir Türkçe ad için denenecek İngilizce adayların listesi."""
    if not ad:
        return [ad]
    if ad.startswith('__') and ad.endswith('__'):
        return [ad]
    onek, govde, son_ek = _ayir(ad)
    adaylar = []

    def _ekle(aday: str):
        tam = onek + aday + son_ek
        if tam not in adaylar:
            adaylar.append(tam)

    ascii_govde = _ascii(govde)
    for anahtar in (govde, ascii_govde):
        if anahtar in _TERS:
            _ekle(_TERS[anahtar])
        for es in _ESANLAM.get(anahtar, ()):
            _ekle(es)
    parcalar = [_TERS.get(_ascii(p), _ascii(p)) for p in govde.split('_')]
    _ekle(_birlestir(parcalar))
    if not adaylar:
        _ekle(ad)
    return adaylar


def ceviri_sozlugu() -> Dict[str, str]:
    """Etkin İngilizce->Türkçe sözlüğün kopyasını döndür."""
    return dict(KELIMELER)


def sozluk_ekle(esleme: Dict[str, str]) -> None:
    """Köprü sözlüğüne yeni çeviriler ekle."""
    for en, tr in esleme.items():
        KELIMELER[en] = tr
        _TERS.setdefault(tr, en)


def _kw_cevir(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    if not kwargs:
        return kwargs
    return {ingilizce_ad(k): v for k, v in kwargs.items()}


class Kopru:
    """Bir Python nesnesini Türkçe adlarla kullanılabilir kılan sarmalayıcı."""

    __slots__ = ('_hedef', '_ad')

    def __init__(self, hedef: Any, ad: Optional[str] = None):
        object.__setattr__(self, '_hedef', hedef)
        object.__setattr__(self, '_ad', ad or getattr(hedef, '__name__', 'kopru'))

    # --- ad çözümleme ---
    def _coz(self, ad: str) -> Any:
        hedef = object.__getattribute__(self, '_hedef')
        if hasattr(hedef, ad):
            return getattr(hedef, ad)
        adaylar = ingilizce_adlar(ad)
        for aday in adaylar:
            if aday != ad and hasattr(hedef, aday):
                return getattr(hedef, aday)
        ozel = _OZEL.get(ad)
        if ozel is not None:
            return ozel(self)
        raise AttributeError(
            f"'{object.__getattribute__(self, '_ad')}' köprüsünde "
            f"'{ad}' bulunamadı (denenen: {', '.join(adaylar)})"
        )

    def __getattr__(self, ad: str) -> Any:
        ozel = _OZEL.get(ad)
        if ozel is not None:
            return ozel(self)
        return _sar(self._coz(ad), f'{object.__getattribute__(self, "_ad")}.{ad}')

    def __setattr__(self, ad: str, deger: Any) -> None:
        hedef = object.__getattribute__(self, '_hedef')
        aday = ad if hasattr(hedef, ad) else ingilizce_ad(ad)
        setattr(hedef, aday, _coz_ham(deger))

    def __delattr__(self, ad: str) -> None:
        hedef = object.__getattribute__(self, '_hedef')
        aday = ad if hasattr(hedef, ad) else ingilizce_ad(ad)
        delattr(hedef, aday)

    def __dir__(self):
        hedef = object.__getattribute__(self, '_hedef')
        adlar = set(dir(hedef))
        adlar.update(turkce_ad(a) for a in dir(hedef))
        return sorted(adlar)

    def __repr__(self) -> str:
        return f'<Kopru {object.__getattribute__(self, "_ad")}>'

    # --- çağrı ---
    def __call__(self, *args, **kwargs):
        hedef = object.__getattribute__(self, '_hedef')
        ad = object.__getattribute__(self, '_ad')
        cevrilmis = _kw_cevir(kwargs)
        try:
            return _sar(hedef(*args, **cevrilmis), ad + '()')
        except TypeError:
            if cevrilmis != kwargs:
                return _sar(hedef(*args, **kwargs), ad + '()')
            raise

    # --- kapsayıcı / bağlam protokolleri ---
    def __len__(self):
        return len(object.__getattribute__(self, '_hedef'))

    def __iter__(self):
        return iter(object.__getattribute__(self, '_hedef'))

    def __next__(self):
        return next(object.__getattribute__(self, '_hedef'))

    def __getitem__(self, anahtar):
        return _sar(object.__getattribute__(self, '_hedef')[anahtar],
                    object.__getattribute__(self, '_ad') + '[]')

    def __setitem__(self, anahtar, deger):
        object.__getattribute__(self, '_hedef')[anahtar] = _coz_ham(deger)

    def __delitem__(self, anahtar):
        del object.__getattribute__(self, '_hedef')[anahtar]

    def __contains__(self, oge):
        return oge in object.__getattribute__(self, '_hedef')

    def __bool__(self):
        return bool(object.__getattribute__(self, '_hedef'))

    def __enter__(self):
        return _sar(object.__getattribute__(self, '_hedef').__enter__(),
                    object.__getattribute__(self, '_ad'))

    def __exit__(self, *arg):
        return object.__getattribute__(self, '_hedef').__exit__(*arg)

    def __str__(self):
        return str(object.__getattribute__(self, '_hedef'))

    def __int__(self):
        return int(object.__getattribute__(self, '_hedef'))

    def __float__(self):
        return float(object.__getattribute__(self, '_hedef'))

    def __index__(self):
        return object.__getattribute__(self, '_hedef').__index__()

    def __hash__(self):
        return hash(object.__getattribute__(self, '_hedef'))

    def __eq__(self, diger):
        return object.__getattribute__(self, '_hedef') == _coz_ham(diger)

    def __ne__(self, diger):
        return object.__getattribute__(self, '_hedef') != _coz_ham(diger)

    def __lt__(self, diger):
        return object.__getattribute__(self, '_hedef') < _coz_ham(diger)

    def __le__(self, diger):
        return object.__getattribute__(self, '_hedef') <= _coz_ham(diger)

    def __gt__(self, diger):
        return object.__getattribute__(self, '_hedef') > _coz_ham(diger)

    def __ge__(self, diger):
        return object.__getattribute__(self, '_hedef') >= _coz_ham(diger)

    def __add__(self, diger):
        return object.__getattribute__(self, '_hedef') + _coz_ham(diger)

    def __radd__(self, diger):
        return _coz_ham(diger) + object.__getattribute__(self, '_hedef')

    def __sub__(self, diger):
        return object.__getattribute__(self, '_hedef') - _coz_ham(diger)

    def __mul__(self, diger):
        return object.__getattribute__(self, '_hedef') * _coz_ham(diger)

    def __truediv__(self, diger):
        return object.__getattribute__(self, '_hedef') / _coz_ham(diger)

    def __mod__(self, diger):
        return object.__getattribute__(self, '_hedef') % _coz_ham(diger)

    def __neg__(self):
        return -object.__getattribute__(self, '_hedef')

    def __getstate__(self):
        return object.__getattribute__(self, '_hedef')

    def __setstate__(self, durum):
        object.__setattr__(self, '_hedef', durum)

    @property
    def __class__(self):
        return object.__getattribute__(self, '_hedef').__class__

    @property
    def __dict__(self):
        return object.__getattribute__(self, '_hedef').__dict__

    @property
    def __wrapped__(self):
        """Sarmalanmış özgün nesne."""
        return object.__getattribute__(self, '_hedef')


def _coz_ham(deger: Any) -> Any:
    if isinstance(deger, Kopru):
        return object.__getattribute__(deger, '_hedef')
    return deger


def _sar(deger: Any, ad: Optional[str] = None) -> Any:
    """Nesneyi uygun bir sarmalayıcıya çevir.

    Yalnızca modüller, sınıflar ve başka kütüphanelerden gelen keyfi
    nesneler sarmalanır; yerleşik skaler/dizi türleri olduğu gibi kalır.
    """
    if isinstance(deger, Kopru):
        return deger
    if isinstance(deger, (str, bytes, bytearray, int, float, complex,
                          bool, type(None), list, tuple, dict, set,
                          frozenset, range, memoryview)):
        return deger
    if isinstance(deger, types.ModuleType):
        return Kopru(deger, getattr(deger, '__name__', ad))
    if isinstance(deger, type):
        return Kopru(deger, getattr(deger, '__name__', ad))
    if callable(deger) or hasattr(deger, '__dict__'):
        return Kopru(deger, ad)
    return deger


# Kopru üzerinden doğrudan erişilebilen yardımcılar
_OZEL = {
    'ozgun': lambda k: object.__getattribute__(k, '_hedef'),
    'sarmalanmis': lambda k: object.__getattribute__(k, '_hedef'),
    'turkce_adlar': lambda k: {a: turkce_ad(a)
                               for a in dir(object.__getattribute__(k, '_hedef'))},
    'ozellikler': lambda k: sorted(
        dir(object.__getattribute__(k, '_hedef'))),
}


def bagla(modul: Any, takma_ad: Optional[str] = None) -> Kopru:
    """Bir Python modülünü (adı veya nesnesi) PARS köprüsüne bağla.

    Örnek::

        içe_aktar kopru
        istek = kopru.bagla("requests")
        yanit = istek.al("https://ornek.com")
        yaz(yanit.durum_kodu)
    """
    if isinstance(modul, str):
        modul = importlib.import_module(modul)
    return Kopru(modul, takma_ad or getattr(modul, '__name__', None))


def kutuphane_yukle(modul: Any, takma_ad: Optional[str] = None) -> Kopru:
    """``bagla`` için Türkçe eşanlamlı."""
    return bagla(modul, takma_ad)


def ozellik_listesi(modul: Any) -> Dict[str, str]:
    """Modülün genel öznitelikleri ve Türkçe karşılıklarını döndür."""
    if isinstance(modul, str):
        modul = importlib.import_module(modul)
    if isinstance(modul, Kopru):
        modul = object.__getattribute__(modul, '_hedef')
    sonuc = {}
    for ad in dir(modul):
        if ad.startswith('_'):
            continue
        sonuc[ad] = turkce_ad(ad)
    return sonuc


def disa_aktar(modul_adi: str, hedef_yol: Optional[str] = None,
               takma_ad: Optional[str] = None) -> str:
    """Bir Python kütüphanesi için PARS sarmalayıcı dosyası üret.

    Üretilen ``.pars`` dosyası, kütüphaneyi köprü üzerinden bağlar ve
    Türkçe adlarla kullanılabilir hâle getirir. Döndürülen değer yazılan
    dosyanın yoludur.
    """
    ad = takma_ad or modul_adi.replace('.', '_')
    if hedef_yol is None:
        hedef_yol = f'{ad}_kopru.pars'
    icerik = (
        f'# Otomatik üretildi: {modul_adi} → PARS köprüsü\n'
        f'# Kullanım: içe_aktar {ad}_kopru\n'
        f'\n'
        f'içe_aktar kopru\n'
        f'\n'
        f'{ad} = kopru.bagla("{modul_adi}")\n'
    )
    with open(hedef_yol, 'w', encoding='utf-8') as dosya:
        dosya.write(icerik)
    return hedef_yol


def _dogrula(ad: str) -> Dict[str, Any]:
    try:
        modul = importlib.import_module(ad)
    except Exception as hata:  # pragma: no cover - tanılama amaçlı
        return {'basarili': False, 'hata': str(hata)}
    return {
        'basarili': True,
        'ad': getattr(modul, '__name__', ad),
        'surum': getattr(modul, '__version__', None),
        'ozellik_sayisi': len([a for a in dir(modul) if not a.startswith('_')]),
    }


# Modül üzerinden erişilebilen tanılama yardımcıları
sys.modules.setdefault(__name__, sys.modules[__name__])
