# Panduan Lengkap Streamlit: Dasar Hingga Advanced

## Pendahuluan

### Apa itu Streamlit?

Streamlit adalah framework Python untuk membuat aplikasi web interaktif dengan cepat tanpa harus menggunakan HTML, CSS, dan JavaScript.

Streamlit sangat populer untuk:

* Data Science
* Machine Learning
* Dashboard
* Visualisasi Data
* Sistem Monitoring
* Prototype Aplikasi
* Portofolio Python

---

# 1. Instalasi Streamlit

## Install Streamlit

```bash
pip install streamlit
```

## Cek Versi

```bash
streamlit version
```

## Menjalankan Aplikasi

```bash
streamlit run app.py
```

---

# 2. Struktur Dasar Streamlit

## Contoh Pertama

```python
import streamlit as st

st.title("Hello Streamlit")
st.write("Aplikasi pertama saya")
```

## Penjelasan

| Kode                   | Fungsi                      |
| ---------------------- | --------------------------- |
| import streamlit as st | Mengimpor library Streamlit |
| st.title()             | Membuat judul besar         |
| st.write()             | Menampilkan teks/data       |

---

# 3. Komponen Text

## Title

```python
st.title("Judul Utama")
```

## Header

```python
st.header("Header")
```

## Subheader

```python
st.subheader("Subheader")
```

## Text

```python
st.text("Teks biasa")
```

## Markdown

```python
st.markdown("**Bold**")
st.markdown("*Italic*")
```

## Write

```python
st.write("Halo Dunia")
```

`st.write()` adalah fungsi paling fleksibel.

Bisa menampilkan:

* Text
* Angka
* Tabel
* Grafik
* DataFrame
* Variabel

---

# 4. Input Pengguna

## Text Input

```python
nama = st.text_input("Masukkan Nama")

st.write(nama)
```

## Number Input

```python
umur = st.number_input(
    "Masukkan Umur",
    min_value=1,
    max_value=100
)
```

## Text Area

```python
alamat = st.text_area("Masukkan Alamat")
```

## Date Input

```python
tanggal = st.date_input("Pilih Tanggal")
```

## Time Input

```python
jam = st.time_input("Pilih Jam")
```

---

# 5. Button dan Interaksi

## Button

```python
if st.button("Klik Saya"):
    st.write("Tombol ditekan")
```

## Checkbox

```python
if st.checkbox("Tampilkan Data"):
    st.write("Data ditampilkan")
```

## Radio Button

```python
gender = st.radio(
    "Pilih Gender",
    ["Laki-laki", "Perempuan"]
)
```

## Selectbox

```python
prodi = st.selectbox(
    "Pilih Program Studi",
    ["SI", "TI", "MI"]
)
```

## Multiselect

```python
hobi = st.multiselect(
    "Pilih Hobi",
    ["Coding", "Gaming", "Membaca"]
)
```

## Slider

```python
nilai = st.slider(
    "Pilih Nilai",
    0,
    100,
    75
)
```

---

# 6. Menampilkan Data

## Tabel Sederhana

```python
import pandas as pd


data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [90, 85, 95]
}


df = pd.DataFrame(data)

st.table(df)
```

## Dataframe Interaktif

```python
st.dataframe(df)
```

Perbedaan:

| Fungsi         | Karakteristik    |
| -------------- | ---------------- |
| st.table()     | Tabel statis     |
| st.dataframe() | Tabel interaktif |

---

# 7. Menampilkan Media

## Menampilkan Gambar

```python
st.image("gambar.jpg")
```

## Menampilkan Video

```python
st.video("video.mp4")
```

## Menampilkan Audio

```python
st.audio("musik.mp3")
```

---

# 8. Layout Streamlit

## Sidebar

```python
st.sidebar.title("Menu")
```

## Columns

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Kolom 1")

with col2:
    st.write("Kolom 2")
```

## Tabs

```python

tab1, tab2 = st.tabs([
    "Data",
    "Grafik"
])

with tab1:
    st.write("Isi Tab 1")

with tab2:
    st.write("Isi Tab 2")
```

## Expander

```python
with st.expander("Lihat Detail"):
    st.write("Isi detail")
```

---

# 9. Visualisasi Data

## Line Chart

```python
chart_data = {
    "Nilai": [10, 20, 30, 40, 50]
}

st.line_chart(chart_data)
```

## Bar Chart

```python
st.bar_chart(chart_data)
```

## Area Chart

```python
st.area_chart(chart_data)
```

---

# 10. Menggunakan Matplotlib

## Install Matplotlib

```bash
pip install matplotlib
```

## Contoh Grafik

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_title("Line Plot")

st.pyplot(fig)
```

## Penjelasan

| Kode           | Fungsi                          |
| -------------- | ------------------------------- |
| plt.subplots() | Membuat figure                  |
| ax.plot()      | Membuat grafik                  |
| st.pyplot()    | Menampilkan grafik ke Streamlit |

---

# 11. Upload File

## Upload CSV

```python
uploaded_file = st.file_uploader(
    "Upload File CSV",
    type=["csv"]
)
```

## Membaca CSV

```python
import pandas as pd

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

---

# 12. Session State

Session State digunakan untuk menyimpan data sementara.

## Contoh Counter

```python
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Tambah"):
    st.session_state.counter += 1

st.write(st.session_state.counter)
```

---

# 13. Form Streamlit

## Contoh Form

```python
with st.form("form_mahasiswa"):

    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    submit = st.form_submit_button("Simpan")

if submit:
    st.success("Data berhasil disimpan")
```

---

# 14. Caching

Caching mempercepat aplikasi.

## Contoh

```python
@st.cache_data

def load_data():
    return "Data Loaded"
```

---

# 15. Multipage App

## Struktur Folder

```text
project/
│
├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_Data.py
│   └── 3_Grafik.py
```

Streamlit otomatis membaca folder `pages`.

---

# 16. Integrasi Machine Learning

## Contoh Prediksi Sederhana

```python
import pickle

model = pickle.load(open("model.pkl", "rb"))

input_data = st.number_input("Masukkan Nilai")

if st.button("Prediksi"):

    hasil = model.predict([[input_data]])

    st.write("Hasil Prediksi:", hasil)
```

---

# 17. Integrasi Database

## SQLite

```python
import sqlite3

conn = sqlite3.connect("database.db")
```

## MySQL

```python
import pymysql
```

## PostgreSQL

```python
import psycopg2
```

---

# 18. Login Sederhana

## Contoh Login

```python
username = st.text_input("Username")
password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "admin" and password == "123":
        st.success("Login Berhasil")
    else:
        st.error("Login Gagal")
```

---

# 19. Deploy Streamlit

## Streamlit Community Cloud

Website:

```text
https://streamlit.io/cloud
```

## Langkah Deploy

1. Upload project ke GitHub
2. Login Streamlit Cloud
3. Hubungkan repository
4. Deploy aplikasi

---

# 20. Struktur Project Professional

```text
project_streamlit/
│
├── app.py
├── requirements.txt
├── pages/
├── assets/
├── data/
├── models/
├── utils/
└── README.md
```

## Penjelasan Folder

| Folder | Fungsi                 |
| ------ | ---------------------- |
| pages  | Halaman aplikasi       |
| assets | Gambar/video           |
| data   | Dataset                |
| models | Model machine learning |
| utils  | Fungsi bantuan         |

---

# 21. Tips Best Practice

## Gunakan Fungsi

```python

def tampilkan_data():
    st.write("Data")
```

## Pisahkan File

Jangan menulis semua kode dalam satu file.

## Gunakan Requirements

```bash
pip freeze > requirements.txt
```

## Gunakan Virtual Environment

```bash
python -m venv env
```

---

# 22. Contoh Project Portofolio

## Level Dasar

* Kalkulator
* Biodata Mahasiswa
* Konversi Suhu
* To Do List

## Level Menengah

* Dashboard Penjualan
* Sistem CRUD
* Visualisasi Data CSV
* Sistem Monitoring

## Level Advanced

* Dashboard Machine Learning
* Sistem Deteksi Objek
* Sistem Prediksi
* Web GIS
* Monitoring IoT
* Analisis Sentimen

---

# 23. Contoh Mini Project Lengkap

## Dashboard Nilai Mahasiswa

```python
import streamlit as st
import pandas as pd

st.title("Dashboard Nilai Mahasiswa")

# Data

data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [90, 85, 95]
}

# DataFrame

df = pd.DataFrame(data)

# Tampilkan tabel

st.dataframe(df)

# Statistik

st.write("Rata-rata Nilai:", df["Nilai"].mean())

# Grafik

st.bar_chart(df.set_index("Nama"))
```

---

# 24. Kesalahan Umum Pemula

## Lupa Menjalankan Streamlit

Salah:

```bash
python app.py
```

Benar:

```bash
streamlit run app.py
```

---

## Salah Indentasi

Python sangat sensitif terhadap indentasi.

---

## Tidak Install Library

Pastikan semua library sudah diinstall.

---

# 25. Roadmap Belajar Streamlit

## Tahap 1

Pelajari:

* Text
* Button
* Input
* Layout

## Tahap 2

Pelajari:

* Pandas
* Visualisasi
* Upload File
* Sidebar

## Tahap 3

Pelajari:

* Database
* Machine Learning
* Authentication
* Deployment

## Tahap 4

Pelajari:

* API
* Web GIS
* Docker
* Cloud Deployment

---

# 26. Kesimpulan

Streamlit adalah framework Python yang sangat cepat untuk membangun aplikasi web interaktif.

Kelebihan:

* Mudah dipelajari
* Cepat dikembangkan
* Cocok untuk data science
* Tidak perlu frontend kompleks

Kekurangan:

* Kurang fleksibel dibanding framework frontend murni
* Tidak cocok untuk aplikasi enterprise yang sangat kompleks

Namun untuk:

* Prototype
* Dashboard
* Monitoring
* Machine Learning
* Visualisasi Data

