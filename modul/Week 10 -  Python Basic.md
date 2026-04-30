# Modul Week 10 — Python Basic untuk Visualisasi Basis Data

**Mata Kuliah:** Basis Data
**Topik:** Pengenalan Python & Integrasi dengan MySQL untuk Visualisasi Data

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. Memahami sintaks dasar Python yang relevan untuk pengolahan data.
2. Menghubungkan Python ke database MySQL.
3. Mengambil data dari MySQL menggunakan library `mysql-connector-python`.
4. Mengolah data tabel menggunakan `pandas` DataFrame.
5. Membuat visualisasi data dari database menggunakan `matplotlib` dan `seaborn`.

---

## Persiapan

### Instalasi Library

Buka terminal dan jalankan perintah berikut:

```bash
pip install mysql-connector-python pandas matplotlib seaborn
```

Atau gunakan file `requirements.txt` yang tersedia di folder `script/Week 10/`:

```bash
pip install -r requirements.txt
```

### Struktur File Praktikum

```
script/Week 10/
├── requirements.txt          # daftar library yang dibutuhkan
├── 01_python_dasar.py        # sintaks dasar Python
├── 02_koneksi_mysql.py       # koneksi Python ke MySQL
├── 03_pandas_dataframe.py    # pengolahan data dengan pandas
└── 04_visualisasi.py         # visualisasi data dari MySQL
```

---

## 1. Python Dasar

Bagian ini membahas konsep Python yang paling sering digunakan dalam pengolahan data.

### 1.1 Variabel dan Tipe Data

Python tidak memerlukan deklarasi tipe. Tipe ditentukan otomatis saat nilai diberikan.

```python
# Tipe dasar
nim       = "2021001001"   # str  (teks)
sks       = 3              # int  (bilangan bulat)
ipk       = 3.75           # float (bilangan desimal)
aktif     = True           # bool (benar/salah)

# Cek tipe data
print(type(nim))    # <class 'str'>
print(type(sks))    # <class 'int'>
```

### 1.2 List dan Dictionary

```python
# List — urutan data (seperti array)
matakuliah = ["Basis Data", "Pemrograman Web", "Struktur Data"]
print(matakuliah[0])       # Basis Data
print(len(matakuliah))     # 3

# Dictionary — pasangan kunci:nilai (seperti record)
mahasiswa = {
    "nim"  : "2021001001",
    "nama" : "Andi Wijaya",
    "sks"  : 18
}
print(mahasiswa["nama"])   # Andi Wijaya
```

### 1.3 Perulangan (Loop)

```python
# for loop — iterasi elemen
for mk in matakuliah:
    print(mk)

# for loop dengan range
for i in range(1, 6):
    print(f"Semester {i}")

# while loop
nilai = 0
while nilai < 3:
    nilai += 1
    print(f"Iterasi ke-{nilai}")
```

### 1.4 Kondisional (if / elif / else)

```python
ipk = 3.5

if ipk >= 3.5:
    predikat = "Cumlaude"
elif ipk >= 3.0:
    predikat = "Sangat Memuaskan"
elif ipk >= 2.5:
    predikat = "Memuaskan"
else:
    predikat = "Cukup"

print(f"Predikat: {predikat}")
```

### 1.5 Fungsi

```python
# Mendefinisikan fungsi
def hitung_total_sks(daftar_sks):
    total = 0
    for sks in daftar_sks:
        total += sks
    return total

# Memanggil fungsi
sks_per_mk = [3, 3, 3, 2, 2]
print(hitung_total_sks(sks_per_mk))   # 13
```

### 1.6 f-String (Format Teks)

```python
nama = "Andi Wijaya"
ipk  = 3.75

# f-string memudahkan menyisipkan variabel ke dalam teks
pesan = f"Mahasiswa {nama} memiliki IPK {ipk:.2f}"
print(pesan)   # Mahasiswa Andi Wijaya memiliki IPK 3.75
```

---

## 2. Koneksi Python ke MySQL

### 2.1 Library `mysql-connector-python`

```python
import mysql.connector

# Membuat koneksi
conn = mysql.connector.connect(
    host     = "localhost",
    port     = 3306,        # port default MySQL
    user     = "root",
    password = "root",      # sesuaikan dengan password MySQL Anda
    database = "sistem_akademik"
)

# Membuat cursor (objek untuk menjalankan query)
cursor = conn.cursor()

print("Koneksi berhasil!")
```

> **Catatan port:** Jika menggunakan MAMP, port MySQL biasanya `8889`. Jika menggunakan XAMPP atau instalasi default, port biasanya `3306`.

### 2.2 Menjalankan Query SELECT

```python
# Eksekusi query
cursor.execute("SELECT nim, nama, email FROM Mahasiswa")

# Ambil semua baris hasil
rows = cursor.fetchall()

# Tampilkan tiap baris
for row in rows:
    nim, nama, email = row
    print(f"{nim} | {nama} | {email}")
```

### 2.3 Query dengan Parameter (Aman dari SQL Injection)

```python
# JANGAN lakukan ini (rentan SQL Injection):
# cursor.execute("SELECT * FROM Mahasiswa WHERE nim = '" + nim + "'")

# LAKUKAN ini (gunakan placeholder %s):
nim_cari = "2021001001"
cursor.execute("SELECT * FROM Mahasiswa WHERE nim = %s", (nim_cari,))
hasil = cursor.fetchone()
print(hasil)
```

### 2.4 Menutup Koneksi

```python
# Selalu tutup cursor dan koneksi setelah selesai
cursor.close()
conn.close()
```

---

## 3. Pengolahan Data dengan Pandas

`pandas` adalah library Python untuk analisis dan manipulasi data. Data disimpan dalam struktur **DataFrame** (mirip tabel spreadsheet).

### 3.1 Membuat DataFrame dari Hasil Query MySQL

```python
import mysql.connector
import pandas as pd

conn   = mysql.connector.connect(host="localhost", port=3306,
                                  user="root", password="root",
                                  database="sistem_akademik")
cursor = conn.cursor()

cursor.execute("""
    SELECT m.nim, m.nama, j.nama AS jurusan, j.jenjang
    FROM   Mahasiswa m
    JOIN   Jurusan   j ON m.kode_jurusan = j.kode
""")

# Buat DataFrame dari hasil query
df = pd.DataFrame(cursor.fetchall(), columns=["nim", "nama", "jurusan", "jenjang"])

cursor.close()
conn.close()

print(df)
print(f"\nTotal mahasiswa: {len(df)}")
```

### 3.2 Eksplorasi DataFrame

```python
print(df.head())          # 5 baris pertama
print(df.shape)           # (jumlah baris, jumlah kolom)
print(df.dtypes)          # tipe data tiap kolom
print(df.describe())      # statistik deskriptif
print(df.isnull().sum())  # cek nilai NULL
```

### 3.3 Filter dan Agregasi

```python
# Filter: tampilkan hanya mahasiswa jurusan Informatika
df_if = df[df["jurusan"] == "Teknik Informatika"]
print(df_if)

# Hitung jumlah mahasiswa per jurusan
per_jurusan = df.groupby("jurusan")["nim"].count().reset_index()
per_jurusan.columns = ["jurusan", "jumlah_mahasiswa"]
print(per_jurusan)

# Urutkan dari terbanyak
per_jurusan = per_jurusan.sort_values("jumlah_mahasiswa", ascending=False)
```

### 3.4 Menghitung Total SKS per Mahasiswa

```python
cursor.execute("""
    SELECT mhs.nim, mhs.nama, SUM(mk.sks) AS total_sks
    FROM   Mengikuti  mgt
    JOIN   Mahasiswa  mhs ON mgt.nim         = mhs.nim
    JOIN   Mengajar   mg  ON mgt.id_mengajar = mg.id_mengajar
    JOIN   Matakuliah mk  ON mg.kode_mk      = mk.kode_mk
    WHERE  mg.tahun = 2024
    GROUP  BY mhs.nim, mhs.nama
    ORDER  BY total_sks DESC
""")

df_sks = pd.DataFrame(cursor.fetchall(), columns=["nim", "nama", "total_sks"])
print(df_sks)
```

---

## 4. Visualisasi Data dengan Matplotlib & Seaborn

### 4.1 Konsep Dasar Matplotlib

```python
import matplotlib.pyplot as plt

# Struktur dasar:
# 1. Siapkan data
# 2. Buat figure dan axes
# 3. Plot data
# 4. Tambahkan label & judul
# 5. Tampilkan / simpan

fig, ax = plt.subplots(figsize=(8, 5))   # ukuran kanvas (lebar, tinggi inci)
ax.bar(["A", "B", "C"], [10, 7, 13])     # grafik batang
ax.set_title("Contoh Grafik Batang")
ax.set_xlabel("Kategori")
ax.set_ylabel("Nilai")
plt.tight_layout()
plt.show()
```

### 4.2 Bar Chart — Jumlah Mahasiswa per Jurusan

```python
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

conn   = mysql.connector.connect(host="localhost", port=3306,
                                  user="root", password="root",
                                  database="sistem_akademik")
cursor = conn.cursor()
cursor.execute("""
    SELECT j.nama, COUNT(m.nim) AS jumlah
    FROM   Jurusan   j
    LEFT JOIN Mahasiswa m ON m.kode_jurusan = j.kode
    GROUP  BY j.kode, j.nama
    ORDER  BY jumlah DESC
""")
df = pd.DataFrame(cursor.fetchall(), columns=["jurusan", "jumlah"])
cursor.close(); conn.close()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(df["jurusan"], df["jumlah"], color="steelblue", edgecolor="white")

# Tampilkan angka di atas setiap batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(int(bar.get_height())),
            ha="center", va="bottom", fontweight="bold")

ax.set_title("Jumlah Mahasiswa per Jurusan", fontsize=14, fontweight="bold")
ax.set_xlabel("Jurusan")
ax.set_ylabel("Jumlah Mahasiswa")
ax.tick_params(axis="x", rotation=15)
plt.tight_layout()
plt.savefig("mahasiswa_per_jurusan.png", dpi=150)  # simpan gambar
plt.show()
```

### 4.3 Horizontal Bar Chart — Total SKS per Mahasiswa

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(df_sks["nama"], df_sks["total_sks"], color="coral")
ax.set_title("Total SKS Diambil per Mahasiswa (2024)", fontsize=13)
ax.set_xlabel("Total SKS")
ax.invert_yaxis()   # nama terbanyak di atas
plt.tight_layout()
plt.show()
```

### 4.4 Pie Chart — Proporsi Mahasiswa per Jenjang

```python
cursor.execute("""
    SELECT j.jenjang, COUNT(m.nim) AS jumlah
    FROM   Jurusan j
    LEFT JOIN Mahasiswa m ON m.kode_jurusan = j.kode
    GROUP  BY j.jenjang
""")
df_jenjang = pd.DataFrame(cursor.fetchall(), columns=["jenjang", "jumlah"])

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(df_jenjang["jumlah"],
       labels=df_jenjang["jenjang"],
       autopct="%1.1f%%",
       startangle=90,
       colors=["#4C72B0", "#DD8452", "#55A868"])
ax.set_title("Proporsi Mahasiswa per Jenjang")
plt.tight_layout()
plt.show()
```

### 4.5 Stacked Bar Chart — SKS per Matakuliah per Jurusan (Seaborn)

`seaborn` dibangun di atas `matplotlib` dan menghasilkan grafik yang lebih estetis dengan kode lebih singkat.

```python
import seaborn as sns

cursor.execute("""
    SELECT j.nama AS jurusan, mk.nama AS matakuliah, COUNT(*) AS peserta
    FROM   Mengikuti  mgt
    JOIN   Mahasiswa  mhs ON mgt.nim         = mhs.nim
    JOIN   Jurusan    j   ON mhs.kode_jurusan = j.kode
    JOIN   Mengajar   mg  ON mgt.id_mengajar  = mg.id_mengajar
    JOIN   Matakuliah mk  ON mg.kode_mk       = mk.kode_mk
    GROUP  BY j.nama, mk.nama
    ORDER  BY jurusan, peserta DESC
""")
df_pivot = pd.DataFrame(cursor.fetchall(), columns=["jurusan", "matakuliah", "peserta"])

# Pivot untuk stacked bar
pivot = df_pivot.pivot_table(index="jurusan", columns="matakuliah",
                              values="peserta", fill_value=0)

pivot.plot(kind="bar", stacked=True, figsize=(10, 6),
           colormap="tab10", edgecolor="white")
plt.title("Peserta Matakuliah per Jurusan", fontsize=13, fontweight="bold")
plt.xlabel("Jurusan")
plt.ylabel("Jumlah Peserta")
plt.xticks(rotation=15)
plt.legend(title="Matakuliah", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
```

---

## 5. Pola Koneksi yang Dianjurkan

Gunakan pola berikut agar koneksi selalu ditutup meskipun terjadi error:

```python
import mysql.connector
import pandas as pd

def ambil_data(query, columns, params=None):
    """Helper: jalankan query dan kembalikan DataFrame."""
    conn = mysql.connector.connect(
        host="localhost", port=3306,
        user="root", password="root",
        database="sistem_akademik"
    )
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
    finally:
        cursor.close()
        conn.close()
    return df

# Contoh pemakaian
df_mhs = ambil_data(
    "SELECT nim, nama FROM Mahasiswa WHERE kode_jurusan = %s",
    ["nim", "nama"],
    params=("IF",)
)
print(df_mhs)
```

---

## 6. Rangkuman

| Konsep | Library / Sintaks |
|---|---|
| Koneksi ke MySQL | `mysql.connector.connect(...)` |
| Jalankan query | `cursor.execute(sql, params)` |
| Ambil hasil query | `cursor.fetchall()` / `fetchone()` |
| Buat DataFrame | `pd.DataFrame(rows, columns=[...])` |
| Filter baris | `df[df["kolom"] == nilai]` |
| Agregasi | `df.groupby("kolom").agg(...)` |
| Bar chart | `ax.bar()` / `ax.barh()` |
| Pie chart | `ax.pie()` |
| Stacked bar | `df.plot(kind="bar", stacked=True)` |
| Simpan gambar | `plt.savefig("file.png", dpi=150)` |

---

## 7. Latihan

1. **Koneksi** — Buat script yang menampilkan semua dosen beserta jumlah kelas yang mereka ajarkan di tahun 2024 menggunakan `GROUP BY`.
2. **Pandas** — Dari hasil query KRS, hitung rata-rata SKS yang diambil per mahasiswa. Gunakan `df.groupby().mean()`.
3. **Bar Chart** — Buat bar chart horizontal yang menampilkan jumlah kelas per dosen, urutkan dari terbanyak.
4. **Pie Chart** — Buat pie chart proporsi matakuliah yang paling banyak diikuti mahasiswa.
5. **Tantangan** — Buat dashboard sederhana dalam satu script yang menampilkan **4 grafik sekaligus** dalam satu figure menggunakan `plt.subplots(2, 2)`.

---

## Referensi

- Dokumentasi `pandas` — [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- Dokumentasi `matplotlib` — [https://matplotlib.org/stable/](https://matplotlib.org/stable/)
- Dokumentasi `seaborn` — [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- MySQL Connector/Python — [https://dev.mysql.com/doc/connector-python/en/](https://dev.mysql.com/doc/connector-python/en/)
