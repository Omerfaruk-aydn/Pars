# Python Kütüphaneleri ile Kullanım

PARS, tüm Python kütüphanelerini doğrudan destekler.

## NumPy

```pars
içe_aktar numpy olarak np

a = np.array([1, 2, 3, 4, 5])
yaz(f"Ortalama: {np.mean(a)}")
yaz(f"Standart Sapma: {np.std(a)}")

matris = np.random.randint(1, 10, size=(3, 3))
yaz(f"Matris:\n{matris}")
```

Kurulum: `pars paket yükle numpy`

## Pandas

```pars
içe_aktar pandas olarak pd

veriler = {
    "isim": ["Ahmet", "Ayşe", "Mehmet"],
    "yaş": [25, 30, 22]
}
df = pd.DataFrame(veriler)
yaz(df)
yaz(f"Ortalama yaş: {df['yaş'].mean()}")
```

Kurulum: `pars paket yükle pandas`

## Flask

```pars
den_aktar flask içe_aktar Flask

uygulama = Flask(__name__)

@uygulama.route('/')
fonksiyon ana_sayfa():
    döndür "Merhaba PARS!"

uygulama.run()
```

Kurulum: `pars paket yükle flask`

## Requests

```pars
içe_aktar requests

yanit = requests.get("https://api.ornek.com")
yaz(yanit.json())
```

Kurulum: `pars paket yükle requests`

## Matplotlib

```pars
içe_aktar matplotlib.pyplot olarak plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("PARS Grafiği")
plt.show()
```

Kurulum: `pars paket yükle matplotlib`

## SQLite3 (Standart)

```pars
içe_aktar sqlite3

baglanti = sqlite3.connect(":memory:")
cursor = baglanti.cursor()
cursor.execute("CREATE TABLE test (id INTEGER, isim TEXT)")
cursor.execute("INSERT INTO test VALUES (1, 'PARS')")
baglanti.commit()
```

## JSON (Standart)

```pars
içe_aktar json

veri = {"ad": "Ahmet", "yaş": 25}
json_metin = json.dumps(veri, ensure_ascii=False)
yaz(json_metin)
```

## DateTime (Standart)

```pars
içe_aktar datetime

şimdi = datetime.datetime.now()
yaz(şimdi.strftime("%d.%m.%Y %H:%M:%S"))
```

## Random (Standart)

```pars
içe_aktar random

yaz(random.randint(1, 100))
yaz(random.choice(["elma", "armut", "muz"]))
```
