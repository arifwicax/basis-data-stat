# Week 12 - Visualisasi Data dengan Python

## Tujuan Pembelajaran
Setelah menyelesaikan modul ini, mahasiswa diharapkan dapat:
1. Memahami konsep dan manfaat penggunaan Miniconda untuk manajemen environment Python
2. Menginstal dan mengkonfigurasi Miniconda di sistem operasi masing-masing
3. Membuat dan mengelola virtual environment untuk proyek Python
4. Memahami library visualisasi data populer di Python (Matplotlib, Seaborn, Plotly)
5. Mengintegrasikan database MySQL dengan Python menggunakan pandas
6. Membuat dashboard interaktif menggunakan Streamlit
7. Mengimplementasikan berbagai jenis visualisasi data (Line Chart, Bar Chart, Pie Chart, Treemap)

---

## Bagian 1: Pengenalan dan Instalasi Miniconda

### 1.1 Apa itu Miniconda?

**Miniconda** adalah versi minimal dari Anaconda yang hanya berisi:
- Python interpreter
- Conda package manager
- Sejumlah kecil package dasar

Miniconda memberikan kontrol penuh kepada pengguna untuk menginstal package yang benar-benar dibutuhkan, berbeda dengan Anaconda yang sudah menyertakan ratusan package secara default.

### 1.2 Manfaat Menggunakan Miniconda

#### Keuntungan Utama:

1. **Ukuran Instalasi Lebih Kecil**
   - Miniconda: ~50-100 MB
   - Anaconda: ~3-5 GB
   - Hemat ruang penyimpanan

2. **Manajemen Environment yang Efisien**
   - Membuat environment terpisah untuk setiap proyek
   - Menghindari konflik dependency antar proyek
   - Mudah berbagi environment dengan tim

3. **Package Management yang Handal**
   - Conda dapat menginstal package Python dan non-Python
   - Resolusi dependency otomatis
   - Cross-platform compatibility

4. **Fleksibilitas**
   - Instal hanya package yang dibutuhkan
   - Kontrol penuh atas environment proyek
   - Lebih cepat dan efisien

5. **Reproduktibilitas**
   - Environment dapat di-export dan di-share
   - Memastikan konsistensi development

### 1.3 Instalasi Miniconda

#### Windows:

1. **Download Installer**
   ```
   Kunjungi: https://docs.conda.io/en/latest/miniconda.html
   Pilih: Miniconda3 Windows 64-bit
   ```

2. **Jalankan Installer**
   - Klik file `.exe` yang sudah didownload
   - Pilih "Just Me" (recommended)
   - Pilih lokasi instalasi default
   - Centang "Add Miniconda3 to my PATH environment variable"
   - Klik Install

3. **Verifikasi Instalasi**
   - Buka Command Prompt atau PowerShell
   ```bash
   conda --version
   python --version
   ```

#### macOS:

1. **Download Installer**
   ```
   Kunjungi: https://docs.conda.io/en/latest/miniconda.html
   Pilih: Miniconda3 macOS 64-bit pkg (atau bash)
   ```

2. **Instalasi via Terminal** (metode bash):
   ```bash
   # Download installer
   curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   
   # Jalankan installer
   bash Miniconda3-latest-MacOSX-x86_64.sh
   
   # Ikuti instruksi on-screen
   # Ketik 'yes' untuk menyetujui license
   # Tekan Enter untuk lokasi default
   # Ketik 'yes' untuk initialize conda
   ```

3. **Restart Terminal dan Verifikasi**
   ```bash
   conda --version
   python --version
   ```

#### Linux (Ubuntu/Debian):

1. **Download dan Install**
   ```bash
   # Download installer
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   
   # Jalankan installer
   bash Miniconda3-latest-Linux-x86_64.sh
   
   # Ikuti instruksi on-screen
   ```

2. **Verifikasi Instalasi**
   ```bash
   conda --version
   python --version
   ```

### 1.4 Konfigurasi Awal Miniconda

Setelah instalasi, lakukan konfigurasi dasar:

```bash
# Update conda ke versi terbaru
conda update conda

# Konfigurasi conda untuk tidak auto-activate base environment
conda config --set auto_activate_base false

# Verifikasi konfigurasi
conda config --show
```

---

## Bagian 2: Manajemen Environment dengan Conda

### 2.1 Membuat Virtual Environment

Virtual environment memungkinkan kita memiliki instalasi Python yang terisolasi untuk setiap proyek.

#### Membuat Environment Baru:

```bash
# Sintaks dasar
conda create --name nama_environment python=3.10

# Contoh untuk proyek ini
conda create --name visualisasi_db python=3.10

# Aktifkan environment
conda activate visualisasi_db
```

### 2.2 Perintah Conda yang Penting

```bash
# Melihat daftar environment
conda env list

# Aktifkan environment
conda activate nama_environment

# Deaktivasi environment
conda deactivate

# Hapus environment
conda env remove --name nama_environment

# Export environment ke file
conda env export > environment.yml

# Buat environment dari file
conda env create -f environment.yml

# Melihat package yang terinstal
conda list

# Install package
conda install nama_package

# Install via pip (dalam conda environment)
pip install nama_package
```

### 2.3 Setup Environment untuk Proyek Visualisasi

```bash
# 1. Buat environment baru
conda create --name visualisasi_db python=3.10

# 2. Aktifkan environment
conda activate visualisasi_db

# 3. Install package yang dibutuhkan
pip install streamlit pandas matplotlib seaborn plotly mysql-connector-python

# 4. Verifikasi instalasi
pip list
```

**Package yang Digunakan:**
- `streamlit`: Framework untuk membuat web dashboard interaktif
- `pandas`: Library untuk manipulasi dan analisis data
- `matplotlib`: Library visualisasi data dasar
- `seaborn`: Library visualisasi statistik
- `plotly`: Library visualisasi interaktif
- `mysql-connector-python`: Connector untuk MySQL database

---

## Bagian 3: Pengenalan Library Visualisasi Python

### 3.1 Matplotlib

**Matplotlib** adalah library visualisasi fundamental di Python.

**Karakteristik:**
- Library visualisasi paling populer dan matang
- Kontrol penuh atas setiap elemen grafik
- Cocok untuk publikasi ilmiah
- Syntax yang cukup verbose

**Contoh Penggunaan:**
```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Buat plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o')
plt.title('Contoh Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
```

### 3.2 Seaborn

**Seaborn** adalah library visualisasi statistik yang dibangun di atas Matplotlib.

**Karakteristik:**
- Interface yang lebih sederhana
- Default styling yang lebih menarik
- Terintegrasi baik dengan pandas DataFrame
- Cocok untuk visualisasi statistik

**Contoh Penggunaan:**
```python
import seaborn as sns
import pandas as pd

# Data
df = pd.DataFrame({
    'kategori': ['A', 'B', 'C', 'D'],
    'nilai': [23, 45, 56, 78]
})

# Buat plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='kategori', y='nilai')
plt.title('Contoh Bar Plot')
plt.show()
```

### 3.3 Plotly

**Plotly** adalah library visualisasi interaktif modern.

**Karakteristik:**
- Visualisasi interaktif (zoom, hover, click)
- Tampilan modern dan menarik
- Cocok untuk dashboard dan web
- Mudah diintegrasikan dengan Streamlit

**Contoh Penggunaan:**
```python
import plotly.express as px

# Data
df = pd.DataFrame({
    'tanggal': ['2024-01', '2024-02', '2024-03'],
    'penjualan': [1000, 1500, 1200]
})

# Buat plot
fig = px.line(df, x='tanggal', y='penjualan', 
              title='Tren Penjualan')
fig.show()
```

### 3.4 Perbandingan Library Visualisasi

| Aspek | Matplotlib | Seaborn | Plotly |
|-------|-----------|---------|--------|
| **Interaktivitas** | Statis | Statis | Interaktif |
| **Kemudahan** | Rendah | Sedang | Tinggi |
| **Tampilan** | Sederhana | Bagus | Sangat Bagus |
| **Performa** | Sangat Baik | Baik | Cukup |
| **Cocok untuk** | Publikasi | Analisis Statistik | Dashboard Web |

---

## Bagian 4: Pengenalan Streamlit

### 4.1 Apa itu Streamlit?

**Streamlit** adalah framework open-source untuk membuat web aplikasi data science dengan cepat.

**Keunggulan:**
- Pure Python (tidak perlu HTML/CSS/JavaScript)
- Real-time update (reactive programming)
- Widget interaktif built-in
- Deployment mudah
- Cocok untuk prototype dan MVP

### 4.2 Komponen Dasar Streamlit

#### 1. **Text Elements**
```python
import streamlit as st

st.title("Judul Utama")
st.header("Header")
st.subheader("Subheader")
st.text("Teks biasa")
st.markdown("**Bold** dan *italic*")
```

#### 2. **Data Display**
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

st.dataframe(df)  # Tabel interaktif
st.table(df)      # Tabel statis
st.metric("Label", value=100, delta=10)
```

#### 3. **Input Widgets**
```python
# Text input
nama = st.text_input("Masukkan nama:")

# Number input
umur = st.number_input("Masukkan umur:", min_value=0, max_value=100)

# Selectbox
pilihan = st.selectbox("Pilih opsi:", ["A", "B", "C"])

# Multiselect
pilihan_multi = st.multiselect("Pilih beberapa:", ["A", "B", "C"])

# Slider
nilai = st.slider("Pilih nilai:", 0, 100, 50)

# Checkbox
setuju = st.checkbox("Saya setuju")

# Button
if st.button("Klik Saya"):
    st.write("Tombol diklik!")
```

#### 4. **Layout**
```python
# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Kolom 1")
with col2:
    st.write("Kolom 2")
with col3:
    st.write("Kolom 3")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Konten sidebar")

# Expander
with st.expander("Klik untuk expand"):
    st.write("Konten tersembunyi")
```

#### 5. **Charts**
```python
# Line chart
st.line_chart(df)

# Bar chart
st.bar_chart(df)

# Plotly chart
import plotly.express as px
fig = px.line(df, x='A', y='B')
st.plotly_chart(fig)
```

### 4.3 Struktur Aplikasi Streamlit

```python
# app.py
import streamlit as st

# 1. Page Configuration (harus di baris pertama)
st.set_page_config(
    page_title="Judul",
    page_icon="chart",
    layout="wide"
)

# 2. Sidebar
st.sidebar.title("Menu")
menu = st.sidebar.selectbox("Pilih:", ["Home", "Data"])

# 3. Main Content
st.title("Dashboard Saya")

if menu == "Home":
    st.write("Halaman Home")
elif menu == "Data":
    st.write("Halaman Data")
```

### 4.4 Menjalankan Aplikasi Streamlit

```bash
# Jalankan aplikasi
streamlit run app.py

# Aplikasi akan terbuka di browser
# Default: http://localhost:8501
```

---

## Bagian 4A: Latihan Streamlit - Portfolio dan Visualisasi

### 4A.1 Setup File Latihan

Buat file baru bernama `latihan_streamlit.py` untuk mengikuti latihan-latihan berikut:

```bash
# Buat file latihan
touch latihan_streamlit.py

# Jalankan aplikasi
streamlit run latihan_streamlit.py
```

### 4A.2 Latihan 1: Portfolio Sederhana

**Tujuan:** Membuat halaman portfolio personal menggunakan Streamlit

**Kode Lengkap:**

```python
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Portfolio Saya",
    page_icon="👨‍💻",
    layout="wide"
)

# Header
st.title("Portfolio Saya")
st.markdown("---")

# Profile Section
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="Foto Profil")

with col2:
    st.header("Nama Anda")
    st.subheader("Data Analyst | Python Developer")
    st.write("📧 Email: nama@email.com")
    st.write("📱 Phone: +62 812-3456-7890")
    st.write("🌐 LinkedIn: linkedin.com/in/nama")

st.markdown("---")

# About Me
st.header("Tentang Saya")
st.write("""
Saya adalah seorang Data Analyst dengan pengalaman dalam analisis data, 
visualisasi, dan pembuatan dashboard interaktif. Passionate dalam 
mengolah data untuk mendukung pengambilan keputusan bisnis.
""")

# Skills
st.header("Keahlian")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("- Python")
    st.write("- SQL")
    st.write("- R")

with col2:
    st.subheader("Data Science")
    st.write("- Data Analysis")
    st.write("- Data Visualization")
    st.write("- Machine Learning")

with col3:
    st.subheader("Tools")
    st.write("- Pandas, NumPy")
    st.write("- Streamlit")
    st.write("- Tableau")

# Experience
st.header("Pengalaman")
with st.expander("Data Analyst - Perusahaan ABC (2022-Sekarang)"):
    st.write("""
    - Melakukan analisis data penjualan untuk meningkatkan revenue 20%
    - Membuat dashboard monitoring KPI menggunakan Streamlit
    - Kolaborasi dengan tim product untuk data-driven decision making
    """)

with st.expander("Intern Data Analyst - Startup XYZ (2021-2022)"):
    st.write("""
    - Analisis customer behavior menggunakan Python dan SQL
    - Membuat visualisasi data untuk presentasi ke stakeholder
    - Membantu automasi reporting harian
    """)

# Education
st.header("Pendidikan")
st.write("**S1 Statistika** - Universitas Indonesia (2018-2022)")
st.write("IPK: 3.75/4.00")

# Contact Form
st.header("Hubungi Saya")
with st.form("contact_form"):
    name = st.text_input("Nama")
    email = st.text_input("Email")
    message = st.text_area("Pesan")
    submit = st.form_submit_button("Kirim")
    
    if submit:
        st.success("Pesan berhasil dikirim! Terima kasih.")
```

**Output yang Diharapkan:**
- Halaman portfolio profesional dengan foto profil
- Informasi kontak yang jelas
- Section skills yang terorganisir
- Timeline experience dengan expander
- Form kontak yang fungsional

**Tips:**
- Ganti placeholder image dengan foto Anda
- Sesuaikan informasi dengan data pribadi
- Tambahkan link media sosial yang aktif

---

### 4A.3 Latihan 2: Input Widgets dan Interaktivitas

**Tujuan:** Memahami berbagai input widgets di Streamlit

**Kode Lengkap:**

```python
import streamlit as st

st.title("Latihan Input Widgets")
st.markdown("---")

# 1. Text Input
st.header("1. Text Input")
nama = st.text_input("Masukkan nama Anda:", placeholder="John Doe")
if nama:
    st.write(f"Halo, {nama}!")

st.markdown("---")

# 2. Number Input
st.header("2. Number Input")
umur = st.number_input("Masukkan umur:", min_value=0, max_value=100, value=25)
st.write(f"Umur Anda: {umur} tahun")

st.markdown("---")

# 3. Slider
st.header("3. Slider")
gaji = st.slider("Pilih gaji (juta):", 0, 50, 10)
st.write(f"Gaji: Rp {gaji} juta")

# Slider range
range_harga = st.slider("Pilih rentang harga:", 0, 1000, (200, 800))
st.write(f"Rentang harga: Rp {range_harga[0]} - Rp {range_harga[1]}")

st.markdown("---")

# 4. Select Box
st.header("4. Select Box")
kota = st.selectbox("Pilih kota:", ["Jakarta", "Bandung", "Surabaya", "Bali"])
st.write(f"Kota yang dipilih: {kota}")

st.markdown("---")

# 5. Multi Select
st.header("5. Multi Select")
skills = st.multiselect(
    "Pilih skills:",
    ["Python", "SQL", "Java", "JavaScript", "R", "Tableau"]
)
if skills:
    st.write("Skills yang dipilih:", ", ".join(skills))

st.markdown("---")

# 6. Checkbox
st.header("6. Checkbox")
agree = st.checkbox("Saya setuju dengan syarat dan ketentuan")
if agree:
    st.success("Terima kasih telah menyetujui!")

st.markdown("---")

# 7. Radio Button
st.header("7. Radio Button")
gender = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
st.write(f"Anda memilih: {gender}")

st.markdown("---")

# 8. Date & Time Input
st.header("8. Date & Time Input")
tanggal = st.date_input("Pilih tanggal:")
waktu = st.time_input("Pilih waktu:")
st.write(f"Tanggal: {tanggal}, Waktu: {waktu}")

st.markdown("---")

# 9. File Uploader
st.header("9. File Uploader")
import pandas as pd

uploaded_file = st.file_uploader("Upload file CSV:", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview Data:")
    st.dataframe(df.head())
    st.write(f"Jumlah baris: {len(df)}, Jumlah kolom: {len(df.columns)}")

st.markdown("---")

# 10. Button & Form
st.header("10. Button & Form")

col1, col2 = st.columns(2)

with col1:
    if st.button("Klik Saya!"):
        st.balloons()
        st.success("Button diklik!")

with col2:
    if st.button("Show Celebration"):
        st.snow()
        st.success("Selamat!")
```

**Penjelasan Widget:**

| Widget | Fungsi | Use Case |
|--------|--------|----------|
| `text_input` | Input teks | Nama, email, search |
| `number_input` | Input angka | Umur, harga, quantity |
| `slider` | Range nilai | Filter harga, rating |
| `selectbox` | Pilih satu opsi | Kategori, kota |
| `multiselect` | Pilih multiple | Skills, tags |
| `checkbox` | Toggle on/off | Agreement, filter |
| `radio` | Pilih satu dari list | Gender, status |
| `date_input` | Pilih tanggal | Date range filter |
| `file_uploader` | Upload file | Import data |
| `button` | Trigger action | Submit, calculate |

---

### 4A.4 Latihan 3: Visualisasi dengan Matplotlib dan Seaborn

**Tujuan:** Membuat berbagai jenis chart menggunakan Matplotlib dan Seaborn

**Kode Lengkap:**

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Latihan Chart - Matplotlib & Seaborn")
st.markdown("---")

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({
    'bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'penjualan': [100, 150, 130, 180, 200, 190],
    'biaya': [80, 90, 85, 95, 110, 100]
})

# 1. Line Chart
st.header("1. Line Chart")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['bulan'], data['penjualan'], marker='o', label='Penjualan', linewidth=2)
ax.plot(data['bulan'], data['biaya'], marker='s', label='Biaya', linewidth=2)
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Nilai (Juta)', fontsize=12)
ax.set_title('Penjualan vs Biaya per Bulan', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)

with st.expander("Lihat Kode"):
    st.code("""
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['bulan'], data['penjualan'], marker='o', label='Penjualan')
ax.plot(data['bulan'], data['biaya'], marker='s', label='Biaya')
ax.set_xlabel('Bulan')
ax.set_ylabel('Nilai (Juta)')
ax.set_title('Penjualan vs Biaya per Bulan')
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)
    """)

st.markdown("---")

# 2. Bar Chart
st.header("2. Bar Chart")

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(data['bulan']))
width = 0.35
ax.bar(x - width/2, data['penjualan'], width, label='Penjualan', color='steelblue')
ax.bar(x + width/2, data['biaya'], width, label='Biaya', color='coral')
ax.set_xlabel('Bulan')
ax.set_ylabel('Nilai (Juta)')
ax.set_title('Perbandingan Penjualan dan Biaya')
ax.set_xticks(x)
ax.set_xticklabels(data['bulan'])
ax.legend()
st.pyplot(fig)

st.markdown("---")

# 3. Pie Chart
st.header("3. Pie Chart")

kategori_data = pd.DataFrame({
    'kategori': ['Elektronik', 'Fashion', 'Makanan', 'Lainnya'],
    'nilai': [30, 25, 20, 25]
})

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0.1, 0, 0, 0)  # Highlight slice pertama
ax.pie(kategori_data['nilai'], labels=kategori_data['kategori'], 
       autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
ax.set_title('Distribusi Penjualan per Kategori', fontsize=14, fontweight='bold')
st.pyplot(fig)

st.markdown("---")

# 4. Histogram
st.header("4. Histogram dengan KDE")

ages = np.random.normal(30, 10, 1000)

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(ages, bins=30, kde=True, ax=ax, color='steelblue')
ax.set_xlabel('Umur')
ax.set_ylabel('Frekuensi')
ax.set_title('Distribusi Umur Pelanggan')
st.pyplot(fig)

st.markdown("---")

# 5. Box Plot
st.header("5. Box Plot")

box_data = pd.DataFrame({
    'Kategori': ['A']*50 + ['B']*50 + ['C']*50,
    'Nilai': list(np.random.normal(100, 15, 50)) + 
             list(np.random.normal(120, 20, 50)) + 
             list(np.random.normal(90, 10, 50))
})

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=box_data, x='Kategori', y='Nilai', ax=ax, palette='Set2')
ax.set_title('Box Plot per Kategori')
st.pyplot(fig)

st.markdown("---")

# 6. Heatmap
st.header("6. Correlation Heatmap")

# Generate correlation data
corr_data = pd.DataFrame(np.random.randn(10, 10), 
                         columns=list('ABCDEFGHIJ'))
correlation = corr_data.corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, ax=ax, square=True)
ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
st.pyplot(fig)
```

**Kapan Menggunakan Chart Apa:**

| Chart Type | Kapan Digunakan | Contoh |
|------------|-----------------|--------|
| Line Chart | Tren waktu | Penjualan bulanan |
| Bar Chart | Perbandingan kategori | Sales per produk |
| Pie Chart | Proporsi/persentase | Market share |
| Histogram | Distribusi data | Distribusi umur |
| Box Plot | Distribusi + outliers | Gaji per divisi |
| Heatmap | Korelasi antar variabel | Correlation matrix |

---

### 4A.5 Latihan 4: Visualisasi Interaktif dengan Plotly

**Tujuan:** Membuat chart interaktif dengan hover, zoom, dan pan

**Kode Lengkap:**

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.title("Latihan Chart Interaktif - Plotly")
st.markdown("---")

# Generate time series data
dates = pd.date_range(start='2024-01-01', end='2024-06-30', freq='D')
df_time = pd.DataFrame({
    'tanggal': dates,
    'penjualan': np.random.randint(1000, 5000, len(dates)),
    'pengunjung': np.random.randint(100, 500, len(dates))
})

# 1. Line Chart Interaktif
st.header("1. Line Chart Interaktif")

fig1 = px.line(df_time, x='tanggal', y='penjualan', 
               title='Tren Penjualan Harian',
               labels={'penjualan': 'Penjualan (Ribu)', 'tanggal': 'Tanggal'})
fig1.update_traces(line_color='#1f77b4', line_width=2)
fig1.update_layout(hovermode='x unified')
st.plotly_chart(fig1, use_container_width=True)

st.info("💡 Tip: Hover untuk melihat detail, drag untuk zoom, double-click untuk reset")

with st.expander("Lihat Kode"):
    st.code("""
fig = px.line(df_time, x='tanggal', y='penjualan', 
              title='Tren Penjualan Harian')
st.plotly_chart(fig, use_container_width=True)
    """)

st.markdown("---")

# 2. Bar Chart Interaktif
st.header("2. Bar Chart Interaktif")

produk = pd.DataFrame({
    'produk': ['Laptop', 'Smartphone', 'Tablet', 'Headphone', 'Smartwatch'],
    'penjualan': [150, 320, 80, 200, 120]
})

fig2 = px.bar(produk, x='produk', y='penjualan',
              title='Penjualan per Produk',
              color='penjualan',
              color_continuous_scale='Blues',
              text='penjualan')
fig2.update_traces(texttemplate='%{text}', textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 3. Scatter Plot
st.header("3. Scatter Plot dengan Size & Color")

scatter_data = pd.DataFrame({
    'harga': np.random.randint(100, 1000, 100),
    'penjualan': np.random.randint(10, 200, 100),
    'kategori': np.random.choice(['A', 'B', 'C'], 100)
})

fig3 = px.scatter(scatter_data, x='harga', y='penjualan', 
                  color='kategori', size='penjualan',
                  title='Hubungan Harga vs Penjualan',
                  hover_data=['harga', 'penjualan'])
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# 4. Pie Chart Interaktif
st.header("4. Pie Chart (Donut)")

pie_data = pd.DataFrame({
    'kategori': ['Elektronik', 'Fashion', 'Makanan', 'Kesehatan', 'Lainnya'],
    'nilai': [35, 25, 20, 12, 8]
})

fig4 = px.pie(pie_data, values='nilai', names='kategori',
              title='Distribusi Penjualan per Kategori',
              hole=0.4)  # Membuat donut chart
fig4.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# 5. Multi-Line Chart
st.header("5. Multiple Lines Chart")

fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    x=df_time['tanggal'], 
    y=df_time['penjualan'],
    name='Penjualan',
    line=dict(color='#1f77b4', width=2)
))
fig5.add_trace(go.Scatter(
    x=df_time['tanggal'], 
    y=df_time['pengunjung']*5,  # Scale untuk visualisasi
    name='Pengunjung (x5)',
    line=dict(color='#ff7f0e', width=2)
))
fig5.update_layout(
    title='Penjualan & Pengunjung',
    hovermode='x unified',
    showlegend=True
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# 6. Treemap
st.header("6. Treemap - Visualisasi Hierarki")

treemap_data = pd.DataFrame({
    'kategori': ['Elektronik']*3 + ['Fashion']*3 + ['Makanan']*2,
    'subkategori': ['Laptop', 'Smartphone', 'Tablet', 
                   'Pakaian', 'Sepatu', 'Tas',
                   'Snack', 'Minuman'],
    'nilai': [150, 320, 80, 200, 150, 100, 90, 110]
})

fig6 = px.treemap(treemap_data, 
                  path=['kategori', 'subkategori'], 
                  values='nilai',
                  title='Treemap Penjualan Hierarki',
                  color='nilai',
                  color_continuous_scale='RdYlGn')
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# 7. Box Plot Interaktif
st.header("7. Box Plot Interaktif")

box_df = pd.DataFrame({
    'kategori': ['A']*100 + ['B']*100 + ['C']*100,
    'nilai': list(np.random.normal(100, 15, 100)) + 
             list(np.random.normal(120, 20, 100)) + 
             list(np.random.normal(90, 10, 100))
})

fig7 = px.box(box_df, x='kategori', y='nilai',
              title='Box Plot per Kategori',
              color='kategori',
              points='outliers')  # Show outliers
st.plotly_chart(fig7, use_container_width=True)
```

**Keunggulan Plotly:**
- Interaktif: hover, zoom, pan
- Export chart ke PNG
- Responsive design
- Animasi smooth
- Legend interaktif (klik untuk hide/show)

---

### 4A.6 Latihan 5: Dashboard Mini dengan Filter

**Tujuan:** Membuat dashboard interaktif dengan filter dan multiple charts

**Kode Lengkap:**

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title("Dashboard Penjualan Mini")
st.markdown("---")

# Generate sample data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', end='2024-06-30', freq='D')
df = pd.DataFrame({
    'tanggal': dates,
    'penjualan': np.random.randint(1000, 5000, len(dates)),
    'biaya': np.random.randint(500, 2000, len(dates)),
    'pengunjung': np.random.randint(100, 500, len(dates)),
    'kategori': np.random.choice(['A', 'B', 'C'], len(dates))
})
df['profit'] = df['penjualan'] - df['biaya']

# Sidebar Filters
st.sidebar.header("Filter Dashboard")

# Date Range Filter
date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(df['tanggal'].min(), df['tanggal'].max())
)

# Category Filter
kategori_filter = st.sidebar.multiselect(
    "Pilih Kategori",
    options=df['kategori'].unique(),
    default=df['kategori'].unique()
)

# Apply Filters
mask = (df['tanggal'] >= pd.to_datetime(date_range[0])) & \
       (df['tanggal'] <= pd.to_datetime(date_range[1])) & \
       (df['kategori'].isin(kategori_filter))
df_filtered = df[mask]

# KPI Metrics
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

total_penjualan = df_filtered['penjualan'].sum()
total_biaya = df_filtered['biaya'].sum()
total_profit = df_filtered['profit'].sum()
avg_pengunjung = df_filtered['pengunjung'].mean()

col1.metric(
    "Total Penjualan",
    f"Rp {total_penjualan/1000:.1f}M",
    delta=f"{(total_penjualan/df['penjualan'].sum()*100):.1f}%"
)
col2.metric(
    "Total Biaya",
    f"Rp {total_biaya/1000:.1f}M",
    delta=f"{(total_biaya/df['biaya'].sum()*100):.1f}%"
)
col3.metric(
    "Total Profit",
    f"Rp {total_profit/1000:.1f}M",
    delta=f"{(total_profit/df['profit'].sum()*100):.1f}%"
)
col4.metric(
    "Avg Pengunjung",
    f"{avg_pengunjung:.0f}",
    delta=f"{((avg_pengunjung/df['pengunjung'].mean()-1)*100):.1f}%"
)

st.markdown("---")

# Charts Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tren Penjualan & Profit")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df_filtered['tanggal'], 
        y=df_filtered['penjualan'],
        name='Penjualan',
        line=dict(color='#1f77b4', width=2)
    ))
    fig1.add_trace(go.Scatter(
        x=df_filtered['tanggal'], 
        y=df_filtered['profit'],
        name='Profit',
        line=dict(color='#2ca02c', width=2)
    ))
    fig1.update_layout(hovermode='x unified', height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Distribusi per Kategori")
    kategori_summary = df_filtered.groupby('kategori').agg({
        'penjualan': 'sum'
    }).reset_index()
    
    fig2 = px.bar(kategori_summary, x='kategori', y='penjualan',
                  title='Total Penjualan per Kategori',
                  color='penjualan',
                  color_continuous_scale='Blues')
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("Korelasi Pengunjung vs Penjualan")
    fig3 = px.scatter(df_filtered, x='pengunjung', y='penjualan',
                     color='kategori', 
                     trendline="ols",
                     title='Pengunjung vs Penjualan')
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Pie Chart Profit per Kategori")
    profit_by_cat = df_filtered.groupby('kategori')['profit'].sum().reset_index()
    fig4 = px.pie(profit_by_cat, values='profit', names='kategori',
                 hole=0.4,
                 title='Kontribusi Profit')
    fig4.update_layout(height=400)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Data Table
st.header("Detail Data")

# Show statistics
st.write("Statistik Deskriptif:")
st.dataframe(df_filtered[['penjualan', 'biaya', 'profit', 'pengunjung']].describe())

# Show raw data
with st.expander("Lihat Data Mentah"):
    st.dataframe(df_filtered, use_container_width=True)

# Download button
csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Data CSV",
    data=csv,
    file_name='dashboard_data.csv',
    mime='text/csv',
)
```

**Fitur Dashboard:**
1. KPI Metrics dengan delta
2. Filter sidebar (tanggal & kategori)
3. Multiple charts dalam grid layout
4. Statistik deskriptif
5. Export data ke CSV
6. Responsive design

---

### 4A.7 Tips & Best Practices

**1. Performance Optimization**

```python
import streamlit as st

# Cache data loading
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    return df

# Cache resource (koneksi database)
@st.cache_resource
def init_connection():
    return mysql.connector.connect(...)
```

**2. Layout Design**

```python
# Gunakan columns untuk layout horizontal
col1, col2, col3 = st.columns([2, 1, 1])

# Gunakan container untuk grouping
with st.container():
    st.write("Konten dalam container")

# Gunakan expander untuk konten tersembunyi
with st.expander("Detail"):
    st.write("Konten detail")
```

**3. Session State untuk Interaktivitas**

```python
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Button dengan state
if st.button('Increment'):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
```

**4. Error Handling**

```python
try:
    df = pd.read_csv(uploaded_file)
    st.success("File berhasil diupload!")
except Exception as e:
    st.error(f"Error: {str(e)}")
```

**5. Custom CSS**

```python
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Custom Text</p>', unsafe_allow_html=True)
```

---

## Bagian 5: Koneksi Database MySQL dengan Python

### 5.1 Struktur Database Proyek

Database yang digunakan: `sales_db`

**Tabel-tabel:**

1. **customers** - Data pelanggan
   - customer_id (PK)
   - name
   - email
   - phone
   - address
   - birthdate

2. **products** - Data produk
   - product_id (PK)
   - name
   - description
   - price
   - stock

3. **orders** - Data pesanan
   - order_id (PK)
   - customer_id (FK)
   - order_date
   - total_amount

4. **order_details** - Detail pesanan
   - order_detail_id (PK)
   - order_id (FK)
   - product_id (FK)
   - quantity
   - subtotal

### 5.2 File Konfigurasi Database (config.py)

File `config.py` berfungsi untuk:
- Membuat koneksi ke database MySQL
- Menyediakan fungsi-fungsi untuk query data
- Memisahkan logic database dari tampilan

**Penjelasan Kode config.py:**

```python
# Import library MySQL connector
import mysql.connector

# Membuat koneksi ke database
conn = mysql.connector.connect(
    host="localhost",        # Server database
    port="8889",            # Port MySQL (default: 3306)
    user="root",            # Username database
    password="root",        # Password database
    database="sales_db"     # Nama database
)

# Membuat cursor untuk eksekusi query
c = conn.cursor()
```

**Fungsi Query Data:**

```python
# 1. Fungsi ambil data customers
def view_customers():
    c.execute('SELECT * FROM customers ORDER BY name ASC')
    return c.fetchall()

# 2. Fungsi ambil data orders dengan JOIN
def view_orders_with_customers():
    c.execute('''
        SELECT 
            o.order_id, 
            o.order_date, 
            o.total_amount, 
            c.name AS customer_name, 
            c.phone 
        FROM orders o 
        JOIN customers c ON o.customer_id = c.customer_id 
        ORDER BY o.order_date DESC
    ''')
    return c.fetchall()

# 3. Fungsi ambil data products
def view_products():
    c.execute('SELECT * FROM products ORDER BY name ASC')
    return c.fetchall()

# 4. Fungsi ambil data order_details dengan JOIN multiple tabel
def view_order_details_with_info():
    c.execute('''
        SELECT 
            od.order_detail_id,
            o.order_id,
            o.order_date,
            c.customer_id,
            c.name AS customer_name,
            p.product_id,
            p.name AS product_name,
            p.price AS unit_price,
            od.quantity,
            od.subtotal,
            o.total_amount AS order_total,
            c.phone
        FROM order_details od
        JOIN orders o ON od.order_id = o.order_id
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN products p ON od.product_id = p.product_id
        ORDER BY o.order_date DESC
    ''')
    return c.fetchall()
```

**Best Practice:**
- Selalu tutup koneksi setelah selesai: `conn.close()`
- Gunakan try-except untuk error handling
- Hindari SQL injection dengan prepared statements
- Pisahkan konfigurasi sensitif (gunakan environment variables)

---

## Bagian 6: Membangun Dashboard Visualisasi

### 6.1 Struktur Proyek

```
Dasboard_penjualan/
│
├── config.py           # Konfigurasi database & fungsi query
├── main_tes.py        # File utama dashboard
├── sales_db.sql       # SQL script database
└── requirements.txt   # Daftar dependencies
```

### 6.2 Import Library dan Setup

```python
# Import library
import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Import fungsi dari config.py
from config import *

# Set konfigurasi halaman dashboard
st.set_page_config(
    "Dashboard",           # Judul tab browser
    page_icon="chart",    # Icon tab
    layout="wide"          # Layout lebar penuh
)
```

**Penjelasan:**
- `layout="wide"`: Menggunakan lebar penuh layar untuk dashboard
- Import fungsi dari `config.py` untuk akses database
- Import library visualisasi yang diperlukan

### 6.3 Memuat Data dari Database

#### 1. Data Customers

```python
# Ambil data pelanggan dari database
result_customers = view_customers()

# Konversi ke DataFrame pandas
df_customers = pd.DataFrame(result_customers, columns=[
    "customer_id", "name", "email", "phone", "address", "birthdate"
])

# Konversi birthdate ke datetime
df_customers['birthdate'] = pd.to_datetime(df_customers['birthdate'])

# Hitung usia dari birthdate
df_customers['Age'] = (datetime.now() - df_customers['birthdate']).dt.days // 365
```

**Penjelasan:**
- `view_customers()`: Panggil fungsi dari config.py
- `pd.DataFrame()`: Konversi hasil query ke DataFrame
- `pd.to_datetime()`: Konversi string ke format datetime
- Menghitung usia dengan selisih tanggal (hari dibagi 365)

#### 2. Data Products

```python
# Ambil data produk
result_products = view_products()

# Buat DataFrame produk
df_products = pd.DataFrame(result_products, columns=[
    "product_id", "name", "description", "price", "stock"
])
```

#### 3. Data Orders

```python
# Ambil data orders
result_orders = view_orders_with_customers()

# Buat DataFrame orders
df_orders = pd.DataFrame(result_orders, columns=[
    "order_id", "order_date", "total_amount", "customer_name", "phone"
])
```

#### 4. Data Order Details

```python
# Ambil data order details
result_order_details = view_order_details_with_info()

# Buat DataFrame
df_order_details = pd.DataFrame(result_order_details, columns=[
    "order_detail_id", "order_id", "order_date", "customer_id",
    "customer_name", "product_id", "product_name", "price",
    "quantity", "subtotal", "total_amount", "phone"
])
```

---

## Bagian 7: Implementasi Fitur Dashboard

### 7.1 Fungsi Tabel Customers dengan Filter

```python
def tabelCustomers_dan_export():
    # Hitung jumlah pelanggan
    total_customers = df_customers.shape[0]
    
    # Tampilkan metrik
    st.metric(label="Total Pelanggan", value=total_customers, delta="Semua Data")
    
    # Sidebar: Filter Rentang Usia
    st.sidebar.header("FilterWhere Rentang Usia")
    min_age = int(df_customers['Age'].min())
    max_age = int(df_customers['Age'].max())
    age_range = st.sidebar.slider(
        "Pilih Rentang Usia",
        min_value=min_age,
        max_value=max_age,
        value=(min_age, max_age)
    )
    
    # Terapkan filter usia
    filtered_df = df_customers[df_customers['Age'].between(*age_range)]
    
    # Tampilkan tabel pelanggan
    st.markdown("### Tabel Data Pelanggan")
    
    showdata = st.multiselect(
        "Pilih Kolom Pelanggan yang Ditampilkan",
        options=filtered_df.columns,
        default=["customer_id", "name", "email", "phone", "address", "birthdate", "Age"]
    )
    
    st.dataframe(filtered_df[showdata], use_container_width=True)
    
    # Fungsi export ke CSV
    @st.cache_data
    def convert_df_to_csv(_df):
        return _df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df_to_csv(filtered_df[showdata])
    st.download_button(
        label="Download Data Pelanggan sebagai CSV",
        data=csv,
        file_name='data_pelanggan.csv',
        mime='text/csv'
    )
```

**Fitur Utama:**
1. **Metrik**: Menampilkan total pelanggan
2. **Filter Usia**: Slider untuk filter rentang usia
3. **Multiselect**: Pilih kolom yang ditampilkan
4. **Export CSV**: Download data ke file CSV
5. **Cache**: `@st.cache_data` untuk performa

### 7.2 Fungsi Tabel Products dengan Filter

```python
def tabelProducts_dan_export():
    st.markdown("### Tabel Data Produk")
    
    # Filter berdasarkan rentang harga
    st.sidebar.header("FilterWhere Harga")
    min_price = int(df_products['price'].min())
    max_price = int(df_products['price'].max())
    price_range = st.sidebar.slider(
        "Pilih Rentang Harga",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )
    
    # Filter berdasarkan rentang stock
    st.sidebar.header("FilterWhere Stock")
    min_stock = int(df_products['stock'].min())
    max_stock = int(df_products['stock'].max())
    stock_range = st.sidebar.slider(
        "Pilih Rentang Stock",
        min_value=min_stock,
        max_value=max_stock,
        value=(min_stock, max_stock)
    )
    
    # Terapkan filter
    filtered_df = df_products[
        df_products['price'].between(*price_range) &
        df_products['stock'].between(*stock_range)
    ]
    
    # Hitung metrik
    total_products = df_products.shape[0]
    filtered_stock = filtered_df['stock'].sum()
    
    # Tampilkan metrik
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Produk", value=total_products, delta="Semua Kategori")
    with col2:
        st.metric(label="Total Stock Semua Produk", value=filtered_stock, 
                 delta=f"Filter: {min_stock}-{max_stock}")
    
    # [Kode multiselect dan export sama seperti customers]
```

**Fitur Tambahan:**
- Multiple filters (harga dan stock)
- Multiple metrics dalam columns
- Conditional filtering dengan operator `&`

### 7.3 Fungsi Tabel Orders dengan Filter Tanggal

```python
def tabelOrders_dan_export():
    st.markdown("### Tabel Pesanan dengan Informasi Pelanggan")
    
    # Konversi order_date ke datetime
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
    
    # Ambil tanggal minimal dan maksimal
    min_date = df_orders['order_date'].min().date()
    max_date = df_orders['order_date'].max().date()
    
    # Filter berdasarkan rentang tanggal
    st.sidebar.header("FilterWhere Tanggal Pesanan")
    selected_dates = st.sidebar.date_input(
        "Pilih Rentang Tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Pastikan selalu ada 2 nilai
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date = end_date = selected_dates[0]
    
    # Konversi ke Timestamp untuk filter
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date) + pd.Timedelta(days=1)
    
    # Terapkan filter tanggal
    filtered_df = df_orders[
        (df_orders['order_date'] >= start_date) &
        (df_orders['order_date'] <= end_date)
    ]
    
    # [Kode tampilan metrik dan tabel]
```

**Konsep Penting:**
- `date_input()`: Widget untuk memilih tanggal
- `pd.Timestamp()`: Konversi date ke timestamp
- `pd.Timedelta()`: Menambah 1 hari untuk include end_date penuh
- Filter dengan kondisi tanggal

---

## Bagian 8: Implementasi Visualisasi Data

### 8.1 Fungsi Dashboard Order Details (Lengkap)

Fungsi ini adalah inti dari dashboard yang menampilkan berbagai visualisasi.

#### 1. Metrik Statistik

```python
def metrics():
    col1, col2, col3 = st.columns(3)
    
    # Total transaksi (order_id unik)
    total_transaksi = df_order_details['order_id'].nunique()
    
    # Total amount
    total_amount = df_order_details['total_amount'].sum()
    
    # Total quantity
    total_quantity = df_order_details['quantity'].sum()
    
    # Tampilkan metrik
    col1.metric("Total Transaksi", value=total_transaksi, delta="Semua Pesanan")
    col2.metric("Total Penjualan (IDR)", value=f"{total_amount:,.0f}", delta="Total Amount")
    col3.metric("Total Produk Terjual", value=total_quantity, delta="Quantity")

metrics()
```

**Penjelasan:**
- `nunique()`: Menghitung nilai unik (untuk total transaksi)
- `sum()`: Menjumlahkan nilai
- `f"{total_amount:,.0f}"`: Format number dengan thousand separator

#### 2. Visualisasi Time Series (Penjualan Berdasarkan Waktu)

```python
st.markdown("### Visualisasi Penjualan Berdasarkan Waktu")

# Group by tanggal dan sum subtotal
df_time_series = df_order_details.groupby(
    df_order_details['order_date'].dt.date
).agg(
    total_sales=('subtotal', 'sum')
).reset_index()

# Line Chart
fig_line = px.line(
    df_time_series,
    x='order_date',
    y='total_sales',
    title="Tren Penjualan Harian",
    labels={'total_sales': 'Total Penjualan (IDR)', 'order_date': 'Tanggal'}
)
st.plotly_chart(fig_line, use_container_width=True)

# Bar Chart
fig_bar = px.bar(
    df_time_series,
    x='order_date',
    y='total_sales',
    title="Total Penjualan Harian",
    labels={'total_sales': 'Total Penjualan (IDR)', 'order_date': 'Tanggal'}
)
st.plotly_chart(fig_bar, use_container_width=True)
```

**Konsep:**
- `groupby()`: Mengelompokkan data berdasarkan tanggal
- `dt.date`: Ekstrak tanggal dari datetime
- `agg()`: Agregasi dengan fungsi sum
- `reset_index()`: Reset index setelah groupby
- `px.line()`: Plotly Express line chart
- `px.bar()`: Plotly Express bar chart

#### 3. Visualisasi Produk Terlaris

```python
st.markdown("### Produk Terlaris")

# Group by produk dan sum quantity
df_product_sales = df_order_details.groupby('product_nama').agg(
    total_quantity=('quantity', 'sum')
).reset_index().sort_values(by='total_quantity', ascending=False)

# Bar Chart - Top 10 produk
fig_product_bar = px.bar(
    df_product_sales.head(10),
    x='product_nama',
    y='total_quantity',
    title="Top 10 Produk Terlaris (Berdasarkan Kuantitas)",
    labels={'total_quantity': 'Total Kuantitas Terjual', 'product_nama': 'Nama Produk'}
)
st.plotly_chart(fig_product_bar, use_container_width=True)

# Pie Chart
fig_product_pie = px.pie(
    df_product_sales.head(10),
    names='product_nama',
    values='total_quantity',
    title="Kontribusi Produk Terhadap Total Penjualan (Top 10)"
)
st.plotly_chart(fig_product_pie, use_container_width=True)
```

**Konsep:**
- `sort_values()`: Mengurutkan data
- `ascending=False`: Urutan descending (terbesar ke terkecil)
- `head(10)`: Ambil 10 data teratas
- `px.pie()`: Pie chart untuk melihat proporsi

#### 4. Visualisasi Pendapatan per Produk

```python
st.markdown("### Kontribusi Produk terhadap Total Penjualan")

# Group by produk dan sum subtotal (pendapatan)
df_product_revenue = df_order_details.groupby('product_nama').agg(
    total_revenue=('subtotal', 'sum')
).reset_index().sort_values(by='total_revenue', ascending=False)

# Bar Chart - Top 10 revenue
fig_revenue_bar = px.bar(
    df_product_revenue.head(10),
    x='product_nama',
    y='total_revenue',
    title="Top 10 Produk dengan Pendapatan Tertinggi",
    labels={'total_revenue': 'Total Pendapatan (IDR)', 'product_nama': 'Nama Produk'}
)
st.plotly_chart(fig_revenue_bar, use_container_width=True)

# Treemap - Proporsi pendapatan
fig_treemap = px.treemap(
    df_product_revenue,
    path=['product_nama'],
    values='total_revenue',
    title="Proporsi Kontribusi Produk terhadap Total Pendapatan"
)
st.plotly_chart(fig_treemap, use_container_width=True)
```

**Konsep Baru:**
- `px.treemap()`: Visualisasi hierarki dalam bentuk kotak bersarang
- Efektif untuk melihat proporsi dan perbandingan

### 8.2 Jenis-jenis Visualisasi dan Kapan Menggunakannya

| Jenis Chart | Kapan Digunakan | Contoh Kasus |
|-------------|-----------------|--------------|
| **Line Chart** | Melihat tren sepanjang waktu | Penjualan harian/bulanan |
| **Bar Chart** | Membandingkan kategori | Penjualan per produk |
| **Pie Chart** | Melihat proporsi/persentase | Market share produk |
| **Scatter Plot** | Melihat korelasi 2 variabel | Harga vs Sales |
| **Histogram** | Distribusi data numerik | Distribusi usia customer |
| **Box Plot** | Melihat distribusi + outliers | Analisis harga produk |
| **Heatmap** | Korelasi antar variabel | Correlation matrix |
| **Treemap** | Hierarki dan proporsi | Kontribusi produk |

---

## Bagian 9: Sidebar dan Navigasi Dashboard

### 9.1 Implementasi Sidebar Menu

```python
# Sidebar untuk memilih tampilan
st.sidebar.success("Pilih Tabel:")

if st.sidebar.checkbox("Tampilkan Pelanggan"):
    tabelCustomers_dan_export()

if st.sidebar.checkbox("Tampilkan Produk"):
    tabelProducts_dan_export()

if st.sidebar.checkbox("Tampilkan Orders"):
    tabelOrders_dan_export()

if st.sidebar.checkbox("Tampilkan Orders Details"):
    tabelOrderDetails_dan_export()
```

**Penjelasan:**
- `st.sidebar.checkbox()`: Checkbox di sidebar
- Multiple checkbox dapat dipilih bersamaan
- Setiap checkbox memanggil fungsi yang sesuai

### 9.2 Tips Desain Dashboard

1. **Layout yang Jelas**
   - Gunakan headers dan subheaders
   - Pisahkan section dengan markdown
   - Gunakan icons untuk visual appeal

2. **Metrik yang Informatif**
   - Tampilkan KPI penting di bagian atas
   - Gunakan delta untuk menunjukkan perubahan
   - Gunakan format number yang tepat

3. **Visualisasi yang Tepat**
   - Pilih chart yang sesuai dengan data
   - Jangan overload dengan terlalu banyak chart
   - Gunakan warna yang konsisten

4. **Interaktivitas**
   - Berikan filter yang berguna
   - Gunakan multiselect untuk fleksibilitas
   - Sediakan opsi export data

5. **Performance**
   - Gunakan `@st.cache_data` untuk cache
   - Minimalisir query database yang berulang
   - Lazy loading untuk data besar

---

## Bagian 10: Menjalankan dan Testing Dashboard

### 10.1 Persiapan Environment

```bash
# 1. Pastikan berada di directory proyek
cd ~/Documents/arifwicax\ github/basis-data-stat/script/Week\ 12/Dasboard_penjualan/

# 2. Aktifkan environment
conda activate visualisasi_db

# 3. Verifikasi package terinstal
pip list | grep -E 'streamlit|pandas|plotly|mysql'
```

### 10.2 Setup Database

```bash
# 1. Pastikan MySQL server berjalan
# macOS dengan MAMP:
# - Buka MAMP
# - Start Servers

# 2. Import database (jika belum)
# Via terminal:
mysql -u root -p -h localhost -P 8889 sales_db < sales_db.sql

# Atau via phpMyAdmin/MySQL Workbench
```

### 10.3 Konfigurasi Database Connection

Edit file `config.py` sesuai setup MySQL Anda:

```python
conn = mysql.connector.connect(
    host="localhost",        # Ubah jika berbeda
    port="8889",            # Default: 3306, MAMP: 8889
    user="root",            # Username Anda
    password="root",        # Password Anda
    database="sales_db"     # Nama database
)
```

### 10.4 Menjalankan Dashboard

```bash
# Jalankan aplikasi
streamlit run main_tes.py

# Output:
#   You can now view your Streamlit app in your browser.
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.x:8501

# Aplikasi akan otomatis terbuka di browser
```

### 10.5 Testing Fitur Dashboard

**Checklist Testing:**

**Data Loading**
- [ ] Data customers berhasil dimuat
- [ ] Data products berhasil dimuat
- [ ] Data orders berhasil dimuat
- [ ] Data order details berhasil dimuat

**Filter & Interaksi**
- [ ] Filter usia customers berfungsi
- [ ] Filter harga & stock products berfungsi
- [ ] Filter tanggal orders berfungsi
- [ ] Multiselect kolom berfungsi

**Visualisasi**
- [ ] Line chart tren penjualan tampil
- [ ] Bar chart penjualan harian tampil
- [ ] Pie chart produk terlaris tampil
- [ ] Treemap kontribusi produk tampil

**Export Data**
- [ ] Download CSV customers berfungsi
- [ ] Download CSV products berfungsi
- [ ] Download CSV orders berfungsi
- [ ] Download CSV order details berfungsi

**Metrik**
- [ ] Total customers benar
- [ ] Total products & stock benar
- [ ] Total transaksi benar
- [ ] Total penjualan benar

---

## Bagian 11: Troubleshooting

### 11.1 Error Umum dan Solusi

#### Error 1: ModuleNotFoundError

```
ModuleNotFoundError: No module named 'streamlit'
```

**Solusi:**
```bash
# Pastikan environment aktif
conda activate visualisasi_db

# Install ulang dependencies
pip install streamlit pandas plotly mysql-connector-python
```

#### Error 2: Database Connection Failed

```
mysql.connector.errors.InterfaceError: 2003: Can't connect to MySQL server
```

**Solusi:**
```bash
# Cek MySQL server running
# macOS MAMP: buka MAMP dan Start Servers

# Cek port yang benar
# Default MySQL: 3306
# MAMP: 8889

# Verifikasi credentials di config.py
```

#### Error 3: Empty DataFrame

```
KeyError: 'column_name'
```

**Solusi:**
```python
# Debug: print raw data
print(result_customers)

# Cek jumlah kolom
print(len(result_customers[0]))

# Pastikan jumlah kolom di DataFrame sesuai dengan query
```

#### Error 4: Date Filter Error

```
TypeError: '<' not supported between instances
```

**Solusi:**
```python
# Pastikan konversi datetime
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# Konversi ke Timestamp untuk filter
start_date = pd.Timestamp(start_date)
```

#### Error 5: Cache Error

```
UnhashableTypeError: Cannot hash object of type
```

**Solusi:**
```python
# Gunakan underscore untuk parameter yang tidak di-hash
@st.cache_data
def convert_df_to_csv(_df):  # _df tidak di-hash
    return _df.to_csv(index=False).encode('utf-8')
```

### 11.2 Debug Tips

```python
# 1. Print untuk debug
st.write("Debug:", df.head())
st.write("Shape:", df.shape)
st.write("Columns:", df.columns.tolist())

# 2. Show raw data
st.dataframe(df)

# 3. Exception handling
try:
    result = view_customers()
    df = pd.DataFrame(result, columns=[...])
except Exception as e:
    st.error(f"Error: {str(e)}")

# 4. Conditional display
if df.empty:
    st.warning("Data kosong!")
else:
    st.dataframe(df)
```

---

## Bagian 12: Pengembangan Lanjutan

### 12.1 Fitur Tambahan yang Bisa Diimplementasikan

#### 1. **Authentication & Authorization**
```python
# Simple password protection
import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "admin123":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Password incorrect")
        return False
    else:
        return True

if check_password():
    # Main dashboard code
    pass
```

#### 2. **Real-time Auto-refresh**
```python
import time

# Auto-refresh setiap 60 detik
placeholder = st.empty()

while True:
    with placeholder.container():
        # Load data terbaru
        df = load_data()
        st.dataframe(df)
        time.sleep(60)
```

#### 3. **Advanced Filters**
```python
# Multiple column filter
st.sidebar.multiselect("Filter by Product", df['product_name'].unique())

# Date range dengan preset
date_option = st.sidebar.selectbox("Period", ["Today", "Last 7 days", "Last 30 days", "Custom"])

if date_option == "Custom":
    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date")
```

#### 4. **Export to Multiple Formats**
```python
from io import BytesIO
import xlsxwriter

# Export to Excel
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

excel_data = to_excel(df)
st.download_button("Download Excel", excel_data, "data.xlsx")
```

#### 5. **Predictive Analytics**
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Simple sales prediction
X = np.array(range(len(df_time_series))).reshape(-1, 1)
y = df_time_series['total_sales'].values

model = LinearRegression()
model.fit(X, y)

# Predict next 7 days
future_X = np.array(range(len(df_time_series), len(df_time_series) + 7)).reshape(-1, 1)
predictions = model.predict(future_X)

st.write("Prediksi 7 hari ke depan:", predictions)
```

### 12.2 Deployment Dashboard

#### Opsi 1: Streamlit Cloud (Gratis)

```bash
# 1. Push ke GitHub
git init
git add .
git commit -m "Initial commit"
git push origin main

# 2. Deploy di Streamlit Cloud
# - Kunjungi: share.streamlit.io
# - Connect GitHub repository
# - Deploy!
```

#### Opsi 2: Heroku

```bash
# 1. Buat file requirements.txt
pip freeze > requirements.txt

# 2. Buat Procfile
echo "web: streamlit run main_tes.py" > Procfile

# 3. Deploy ke Heroku
heroku create app-name
git push heroku main
```

#### Opsi 3: Docker

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main_tes.py"]
```

```bash
# Build dan run
docker build -t dashboard-app .
docker run -p 8501:8501 dashboard-app
```

---

## Bagian 13: Best Practices & Tips

### 13.1 Code Organization

```
project/
│
├── config/
│   ├── __init__.py
│   └── database.py      # Database connection
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py   # Data loading functions
│   └── visualizations.py # Reusable viz functions
│
├── pages/
│   ├── home.py
│   ├── customers.py
│   ├── products.py
│   └── analytics.py
│
├── main.py              # Main dashboard
├── requirements.txt
└── README.md
```

### 13.2 Performance Optimization

```python
# 1. Cache data loading
@st.cache_data(ttl=3600)  # Cache 1 jam
def load_data():
    return view_customers()

# 2. Cache resource (connection)
@st.cache_resource
def init_connection():
    return mysql.connector.connect(...)

# 3. Lazy loading
if st.button("Load Data"):
    df = load_data()
    st.dataframe(df)

# 4. Pagination untuk data besar
page = st.number_input("Page", 1)
rows_per_page = 100
start_idx = (page - 1) * rows_per_page
end_idx = start_idx + rows_per_page
st.dataframe(df.iloc[start_idx:end_idx])
```

### 13.3 Security Best Practices

```python
# 1. Environment variables untuk credentials
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# 2. Prepared statements untuk SQL injection
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# 3. Input validation
if st.text_input("User ID"):
    if user_id.isdigit():
        # Process
        pass
    else:
        st.error("Invalid input")
```

### 13.4 Documentation

```python
def load_sales_data(start_date, end_date):
    """
    Load sales data from database within date range.
    
    Args:
        start_date (datetime): Start date of the range
        end_date (datetime): End date of the range
    
    Returns:
        pd.DataFrame: Sales data with columns [order_id, date, amount]
    
    Example:
        >>> df = load_sales_data('2024-01-01', '2024-01-31')
        >>> print(df.head())
    """
    pass
```

---

## Tugas Praktikum

### Tugas 1: Setup Environment (Bobot: 20%)

1. Install Miniconda di komputer Anda
2. Buat environment baru bernama `visualisasi_db`
3. Install semua package yang diperlukan
4. Screenshot hasil `conda list` dan `streamlit --version`

**Deliverable:**
- Screenshot instalasi
- File `environment.yml` hasil export

### Tugas 2: Modifikasi Dashboard (Bobot: 40%)

Tambahkan fitur baru pada dashboard:

1. **Visualisasi baru**: Buat minimal 2 visualisasi baru yang menampilkan insight berbeda, misalnya:
   - Histogram distribusi usia pelanggan
   - Heatmap korelasi antara harga produk dan quantity terjual
   - Scatter plot: harga vs stock produk

2. **Filter tambahan**: Tambahkan filter baru seperti:
   - Filter berdasarkan nama customer (search box)
   - Filter berdasarkan kategori produk (jika ada)

3. **Metrik tambahan**: Tambahkan KPI baru seperti:
   - Average Order Value (AOV)
   - Customer dengan pembelian terbanyak
   - Produk dengan margin tertinggi

**Deliverable:**
- File `main_tes.py` yang sudah dimodifikasi
- Screenshot dashboard dengan fitur baru
- Penjelasan singkat (max 200 kata) tentang insight yang didapat

### Tugas 3: Analisis Data (Bobot: 40%)

Gunakan dashboard untuk menjawab pertanyaan analisis berikut:

1. **Analisis Penjualan:**
   - Berapa total penjualan dalam 30 hari terakhir?
   - Produk mana yang paling laris?
   - Hari apa yang memiliki penjualan tertinggi?

2. **Analisis Customer:**
   - Berapa rata-rata usia customer?
   - Customer mana yang paling banyak berbelanja?
   - Apakah ada korelasi antara usia dan jumlah pembelian?

3. **Analisis Produk:**
   - Produk mana yang memiliki stock paling sedikit?
   - Produk mana yang memberikan revenue tertinggi?
   - Berapa rata-rata harga produk yang terjual?

4. **Rekomendasi Bisnis:**
   - Berdasarkan data, strategi apa yang Anda rekomendasikan untuk meningkatkan penjualan?
   - Produk mana yang perlu di-restock?
   - Target customer segment mana yang paling potensial?

**Deliverable:**
- Dokumen analisis (PDF/Word)
- Screenshot visualisasi yang mendukung analisis
- Rekomendasi bisnis (minimal 3 poin)

---

## Referensi dan Sumber Belajar

### Dokumentasi Resmi

1. **Streamlit**
   - Docs: https://docs.streamlit.io
   - Gallery: https://streamlit.io/gallery
   - Cheat Sheet: https://docs.streamlit.io/library/cheatsheet

2. **Pandas**
   - Docs: https://pandas.pydata.org/docs/
   - Tutorial: https://pandas.pydata.org/docs/getting_started/tutorials.html

3. **Plotly**
   - Docs: https://plotly.com/python/
   - Gallery: https://plotly.com/python/plotly-express/

4. **Miniconda**
   - Docs: https://docs.conda.io/en/latest/
   - Cheat Sheet: https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html

### Tutorial Video

1. Streamlit Crash Course: https://www.youtube.com/watch?v=JwSS70SZdyM
2. Pandas for Data Analysis: https://www.youtube.com/watch?v=vmEHCJofslg
3. Plotly Express Tutorial: https://www.youtube.com/watch?v=GGL6U0k8WYA

### Buku Rekomendasi

1. "Python for Data Analysis" - Wes McKinney
2. "Interactive Data Visualization with Python" - Abha Belorkar
3. "Streamlit for Data Science" - Tyler Richards

---

## FAQ (Frequently Asked Questions)

**Q: Apakah harus menggunakan Miniconda? Bisa pakai Anaconda atau virtualenv?**
A: Bisa menggunakan Anaconda atau virtualenv, tetapi Miniconda lebih ringan dan direkomendasikan untuk proyek ini.

**Q: Port MySQL saya berbeda (3306), apakah masalah?**
A: Tidak masalah, sesuaikan saja di `config.py`. Default MySQL adalah 3306, MAMP menggunakan 8889.

**Q: Dashboard tidak mau running, error "Address already in use"**
A: Port 8501 sudah digunakan. Gunakan: `streamlit run main_tes.py --server.port 8502`

**Q: Data tidak muncul di dashboard, tapi tidak ada error**
A: Cek koneksi database, pastikan MySQL running dan credentials benar. Gunakan `st.write()` untuk debug.

**Q: Bagaimana cara menambah data dummy ke database?**
A: Gunakan SQL script atau buat fungsi insert di `config.py`:
```python
def insert_customer(name, email, phone):
    c.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", 
              (name, email, phone))
    conn.commit()
```

**Q: Visualisasi terlalu lambat loading**
A: Gunakan `@st.cache_data` dan kurangi jumlah data dengan filter atau limit query.

**Q: Bisa deploy ke hosting gratis?**
A: Ya, bisa deploy ke Streamlit Cloud (gratis), Heroku (gratis tier), atau Railway.

**Q: Apakah bisa connect ke database online (bukan localhost)?**
A: Bisa, ubah `host` di `config.py` ke IP/domain server database Anda.

---

## Kesimpulan

Dalam modul ini, Anda telah mempelajari:

- Instalasi dan konfigurasi Miniconda
- Manajemen environment Python dengan Conda
- Library visualisasi data: Matplotlib, Seaborn, Plotly
- Framework Streamlit untuk dashboard interaktif
- Koneksi database MySQL dengan Python
- Implementasi berbagai jenis visualisasi data
- Best practices dalam membangun dashboard
- Deployment dan troubleshooting

**Next Steps:**
1. Eksplorasi library visualisasi lain (Bokeh, Altair)
2. Belajar advanced analytics (Machine Learning)
3. Pelajari database optimization
4. Explore real-time data streaming

**Selamat belajar dan semoga sukses!**

---

*Modul ini dibuat untuk mata kuliah Basis Data - Week 12*  
*Universitas/Institusi*  
*Tahun 2024*




# programfile
## proyek 1, proyek 2
## 