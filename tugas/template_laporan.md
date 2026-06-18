# LAPORAN PROYEK BASIS DATA
## Perancangan dan Implementasi Database MySQL

---

<div align="center">

**[JUDUL PROYEK]**
*(contoh: Sistem Informasi Perpustakaan / Sistem Manajemen Klinik / dst.)*

---

Disusun Oleh:

| Nama | NIM |
|------|-----|
| [Nama Mahasiswa] | [NIM] |

---

**PROGRAM STUDI STATISTIKA**
**FAKULTAS [NAMA FAKULTAS]**
**[NAMA UNIVERSITAS]**
**[KOTA], [TAHUN]**

</div>

---

## KATA PENGANTAR

Puji syukur penulis panjatkan kepada Tuhan Yang Maha Esa atas selesainya laporan proyek mata kuliah Basis Data dengan judul **"[Judul Proyek]"**.

Laporan ini disusun sebagai pemenuhan tugas proyek akhir mata kuliah Basis Data, yang mencakup tahapan perancangan basis data mulai dari identifikasi kebutuhan, perancangan Entity-Relationship Diagram (ERD), hingga implementasi ke dalam sistem manajemen basis data MySQL.

Penulis menyadari laporan ini masih jauh dari sempurna. Oleh karena itu, kritik dan saran yang membangun sangat diharapkan.

[Kota], [Tanggal Bulan Tahun]

**Penulis**

---

## DAFTAR ISI

1. [Pendahuluan](#1-pendahuluan)
2. [Identifikasi Kebutuhan Sistem](#2-identifikasi-kebutuhan-sistem)
3. [Perancangan Konseptual — ERD](#3-perancangan-konseptual--erd)
4. [Perancangan Logis — Skema Relasional](#4-perancangan-logis--skema-relasional)
5. [Implementasi DDL — Pembuatan Database dan Tabel](#5-implementasi-ddl--pembuatan-database-dan-tabel)
6. [Pengisian Data — DML INSERT](#6-pengisian-data--dml-insert)
7. [Pengujian Query](#7-pengujian-query)
8. [Kesimpulan](#8-kesimpulan)
9. [Referensi](#9-referensi)
10. [Lampiran](#10-lampiran)

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang

> *Jelaskan konteks dan permasalahan yang melatarbelakangi pembuatan proyek basis data ini. Mengapa sistem ini dibutuhkan? Apa masalah yang ingin diselesaikan?*

[Tuliskan latar belakang proyek di sini. Contoh:]

Pengelolaan data [domain proyek] selama ini masih dilakukan secara manual sehingga menimbulkan berbagai permasalahan seperti redundansi data, inkonsistensi informasi, dan sulitnya pengaksesan data yang cepat dan akurat. Oleh karena itu, diperlukan sebuah sistem basis data yang terstruktur dan terkelola dengan baik untuk mengatasi permasalahan tersebut.

### 1.2 Tujuan

1. Merancang Entity-Relationship Diagram (ERD) untuk sistem [nama sistem].
2. Mengkonversi ERD menjadi skema tabel relasional yang normal.
3. Mengimplementasikan skema tersebut ke dalam database MySQL.
4. Mengisi database dengan data sampel yang representatif.
5. Memverifikasi integritas data melalui pengujian query SQL.

### 1.3 Ruang Lingkup

> *Jelaskan batasan-batasan dari sistem yang dirancang.*

Sistem basis data yang dirancang mencakup:
- [Fitur/entitas 1]
- [Fitur/entitas 2]
- [Fitur/entitas 3]

Sistem ini **tidak** mencakup:
- [Hal di luar scope 1]
- [Hal di luar scope 2]

### 1.4 Metodologi

Pengerjaan proyek ini mengikuti tahapan perancangan basis data secara sistematis:

```
Identifikasi Kebutuhan
        ↓
Perancangan Konseptual (ERD)
        ↓
Perancangan Logis (Skema Relasional)
        ↓
Implementasi DDL (CREATE TABLE)
        ↓
Pengisian Data (INSERT)
        ↓
Pengujian Query (SELECT / JOIN / dll.)
```

---

## 2. IDENTIFIKASI KEBUTUHAN SISTEM

### 2.1 Deskripsi Sistem

> *Deskripsikan sistem yang akan dibangun secara singkat dan jelas.*

[Nama Sistem] adalah sebuah sistem basis data yang digunakan untuk mengelola data [domain]. Sistem ini melibatkan beberapa pihak/pengguna sebagai berikut:

| Pengguna/Aktor | Peran |
|----------------|-------|
| [Aktor 1] | [Deskripsi peran] |
| [Aktor 2] | [Deskripsi peran] |
| [Aktor 3] | [Deskripsi peran] |

### 2.2 Identifikasi Entitas

Berdasarkan analisis kebutuhan, ditemukan entitas-entitas berikut:

| No | Entitas | Deskripsi |
|----|---------|-----------|
| 1 | [Entitas 1] | [Deskripsi singkat] |
| 2 | [Entitas 2] | [Deskripsi singkat] |
| 3 | [Entitas 3] | [Deskripsi singkat] |
| 4 | [Entitas 4] | [Deskripsi singkat] |

### 2.3 Identifikasi Atribut

| Entitas | Atribut | Tipe Data | Keterangan |
|---------|---------|-----------|------------|
| [Entitas 1] | [pk_atribut] | INT / VARCHAR | Primary Key |
| [Entitas 1] | [atribut_2] | VARCHAR(100) | |
| [Entitas 1] | [atribut_3] | DATE | |
| [Entitas 2] | [pk_atribut] | INT | Primary Key |
| [Entitas 2] | [atribut_2] | VARCHAR(100) | |

### 2.4 Identifikasi Relasi

| No | Relasi | Entitas A | Entitas B | Kardinalitas | Keterangan |
|----|--------|-----------|-----------|--------------|------------|
| 1 | [nama relasi] | [Entitas 1] | [Entitas 2] | 1 : N | [Deskripsi] |
| 2 | [nama relasi] | [Entitas 2] | [Entitas 3] | N : M | [Deskripsi] |
| 3 | [nama relasi] | [Entitas 1] | [Entitas 3] | 1 : 1 | [Deskripsi] |

---

## 3. PERANCANGAN KONSEPTUAL — ERD

### 3.1 Diagram ERD

> *Tempelkan gambar ERD di sini. Gunakan tools seperti draw.io, Lucidchart, MySQL Workbench, atau dbdiagram.io.*

![ERD [Nama Sistem]](./assets/erd_[nama_sistem].png)

*Gambar 3.1 Entity-Relationship Diagram [Nama Sistem]*

### 3.2 Penjelasan ERD

#### Entitas dan Primary Key

| Entitas | Primary Key | Atribut Lainnya |
|---------|-------------|-----------------|
| [Entitas 1] | [id_1] | [attr_a], [attr_b], [attr_c] |
| [Entitas 2] | [id_2] | [attr_a], [attr_b] |
| [Entitas 3] | [id_3] | [attr_a], [attr_b], [attr_c] |

#### Penjelasan Relasi

**Relasi 1: [Nama Relasi]**
- **Entitas yang terlibat:** [Entitas A] dan [Entitas B]
- **Kardinalitas:** [1:N / N:M / 1:1]
- **Penjelasan:** [Satu Entitas A dapat memiliki banyak Entitas B, sedangkan setiap Entitas B hanya dimiliki oleh satu Entitas A.]

**Relasi 2: [Nama Relasi]**
- **Entitas yang terlibat:** [Entitas B] dan [Entitas C]
- **Kardinalitas:** [N:M]
- **Penjelasan:** [Deskripsi relasi.]
- **Atribut relasi:** [atribut_relasi_1], [atribut_relasi_2] *(jika ada)*

---

## 4. PERANCANGAN LOGIS — SKEMA RELASIONAL

### 4.1 Aturan Konversi yang Digunakan

| Aturan | Penerapan dalam Proyek Ini |
|--------|---------------------------|
| Entitas kuat → Tabel mandiri | [Entitas 1], [Entitas 2], [Entitas 3] masing-masing menjadi tabel tersendiri |
| Relasi 1:N → Foreign key di sisi N | [FK dari Entitas B merujuk ke Entitas A] |
| Relasi N:M → Tabel asosiatif baru | [Tabel baru: nama_tabel_asosiatif] |
| Atribut multivalued → Tabel terpisah | *(jika ada)* |

### 4.2 Skema Tabel Relasional

Notasi: **PK** = Primary Key, **FK** = Foreign Key, *kolom miring* = NOT NULL

---

**Tabel: `[nama_tabel_1]`**

| Kolom | Tipe Data | Constraint | Keterangan |
|-------|-----------|------------|------------|
| `[id_1]` | INT | PK, AUTO_INCREMENT | Identitas unik |
| `[kolom_2]` | VARCHAR(100) | NOT NULL | [deskripsi] |
| `[kolom_3]` | DATE | | [deskripsi] |
| `[kolom_4]` | DECIMAL(10,2) | | [deskripsi] |

---

**Tabel: `[nama_tabel_2]`**

| Kolom | Tipe Data | Constraint | Keterangan |
|-------|-----------|------------|------------|
| `[id_2]` | INT | PK, AUTO_INCREMENT | Identitas unik |
| `[kolom_2]` | VARCHAR(100) | NOT NULL | [deskripsi] |
| `[id_1]` | INT | FK → [nama_tabel_1]([id_1]) | [deskripsi relasi] |

---

**Tabel: `[nama_tabel_asosiatif]`** *(dari relasi N:M)*

| Kolom | Tipe Data | Constraint | Keterangan |
|-------|-----------|------------|------------|
| `[id_a]` | INT | PK, FK → [tabel_a]([id_a]) | Bagian dari composite PK |
| `[id_b]` | INT | PK, FK → [tabel_b]([id_b]) | Bagian dari composite PK |
| `[atribut_relasi]` | VARCHAR(50) | | Atribut dari relasi |

---

### 4.3 Diagram Skema Relasional

> *Opsional: tambahkan diagram schema/relational model di sini.*

```
[nama_tabel_1] ([id_1], kolom_2, kolom_3)
[nama_tabel_2] ([id_2], kolom_2, *id_1*)
[nama_tabel_asosiatif] ([id_a], [id_b], atribut_relasi)
```

---

## 5. IMPLEMENTASI DDL — PEMBUATAN DATABASE DAN TABEL

### 5.1 Pembuatan Database

```sql
-- Membuat database
CREATE DATABASE IF NOT EXISTS [nama_database]
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE [nama_database];
```

### 5.2 Pembuatan Tabel

> *Tuliskan seluruh perintah CREATE TABLE sesuai skema yang telah dirancang. Pastikan urutan pembuatan tabel memperhatikan dependensi foreign key (tabel yang dirujuk dibuat lebih dahulu).*

```sql
-- ============================================
-- Tabel: [nama_tabel_1]
-- Deskripsi: [deskripsi singkat tabel ini]
-- ============================================
CREATE TABLE [nama_tabel_1] (
    [id_1]    INT           NOT NULL AUTO_INCREMENT,
    [kolom_2] VARCHAR(100)  NOT NULL,
    [kolom_3] DATE,
    [kolom_4] DECIMAL(10,2) DEFAULT 0.00,
    PRIMARY KEY ([id_1])
);

-- ============================================
-- Tabel: [nama_tabel_2]
-- Deskripsi: [deskripsi singkat tabel ini]
-- ============================================
CREATE TABLE [nama_tabel_2] (
    [id_2]    INT           NOT NULL AUTO_INCREMENT,
    [kolom_2] VARCHAR(100)  NOT NULL,
    [id_1]    INT           NOT NULL,
    PRIMARY KEY ([id_2]),
    CONSTRAINT fk_[tabel2]_[tabel1]
        FOREIGN KEY ([id_1])
        REFERENCES [nama_tabel_1]([id_1])
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ============================================
-- Tabel: [nama_tabel_asosiatif]
-- Deskripsi: Relasi N:M antara [Entitas A] dan [Entitas B]
-- ============================================
CREATE TABLE [nama_tabel_asosiatif] (
    [id_a]          INT          NOT NULL,
    [id_b]          INT          NOT NULL,
    [atribut_relasi] VARCHAR(50),
    PRIMARY KEY ([id_a], [id_b]),
    CONSTRAINT fk_asosiatif_a
        FOREIGN KEY ([id_a]) REFERENCES [tabel_a]([id_a])
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_asosiatif_b
        FOREIGN KEY ([id_b]) REFERENCES [tabel_b]([id_b])
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

### 5.3 Verifikasi Struktur Tabel

```sql
-- Melihat daftar tabel yang telah dibuat
SHOW TABLES;

-- Melihat struktur masing-masing tabel
DESCRIBE [nama_tabel_1];
DESCRIBE [nama_tabel_2];
DESCRIBE [nama_tabel_asosiatif];
```

**Hasil output `SHOW TABLES`:**

```
+----------------------------------+
| Tables_in_[nama_database]        |
+----------------------------------+
| [nama_tabel_1]                   |
| [nama_tabel_2]                   |
| [nama_tabel_asosiatif]           |
+----------------------------------+
```

> *Sertakan screenshot hasil eksekusi di sini.*

---

## 6. PENGISIAN DATA — DML INSERT

> *Isi setiap tabel dengan minimal 5–10 baris data sampel yang realistis dan mencerminkan relasi antar tabel.*

### 6.1 Data Tabel `[nama_tabel_1]`

```sql
INSERT INTO [nama_tabel_1] ([kolom_2], [kolom_3], [kolom_4])
VALUES
    ('[nilai_1]', '[nilai_2]', [nilai_3]),
    ('[nilai_1]', '[nilai_2]', [nilai_3]),
    ('[nilai_1]', '[nilai_2]', [nilai_3]),
    ('[nilai_1]', '[nilai_2]', [nilai_3]),
    ('[nilai_1]', '[nilai_2]', [nilai_3]);
```

### 6.2 Data Tabel `[nama_tabel_2]`

```sql
INSERT INTO [nama_tabel_2] ([kolom_2], [id_1])
VALUES
    ('[nilai_1]', 1),
    ('[nilai_1]', 1),
    ('[nilai_1]', 2),
    ('[nilai_1]', 3),
    ('[nilai_1]', 2);
```

### 6.3 Data Tabel `[nama_tabel_asosiatif]`

```sql
INSERT INTO [nama_tabel_asosiatif] ([id_a], [id_b], [atribut_relasi])
VALUES
    (1, 1, '[nilai]'),
    (1, 2, '[nilai]'),
    (2, 1, '[nilai]'),
    (2, 3, '[nilai]'),
    (3, 2, '[nilai]');
```

---

## 7. PENGUJIAN QUERY

> *Lakukan minimal 5 pengujian query yang menguji berbagai aspek basis data: SELECT sederhana, filtering, JOIN, agregasi, dan subquery.*

### 7.1 Query Dasar — Menampilkan Seluruh Data

**Tujuan:** Memverifikasi data berhasil dimasukkan ke dalam tabel.

```sql
SELECT * FROM [nama_tabel_1];
SELECT * FROM [nama_tabel_2];
```

**Hasil:**

> *Sertakan screenshot atau tabel hasil output di sini.*

---

### 7.2 Query Filtering — Pencarian Data Spesifik

**Tujuan:** [Deskripsi tujuan query ini, contoh: Mencari semua [entitas] dengan kondisi tertentu.]

```sql
SELECT [kolom_1], [kolom_2]
FROM   [nama_tabel]
WHERE  [kondisi];
```

**Hasil:**

> *Sertakan screenshot atau tabel hasil output di sini.*

---

### 7.3 Query JOIN — Menggabungkan Data Antar Tabel

**Tujuan:** [Deskripsi tujuan query ini, contoh: Menampilkan [data A] beserta [data B] yang berelasi.]

```sql
SELECT
    a.[kolom_1],
    a.[kolom_2],
    b.[kolom_1] AS [alias]
FROM  [nama_tabel_1] a
JOIN  [nama_tabel_2] b ON a.[id_1] = b.[id_1]
WHERE [kondisi opsional]
ORDER BY a.[kolom_1];
```

**Hasil:**

> *Sertakan screenshot atau tabel hasil output di sini.*

---

### 7.4 Query Agregasi — Statistik / Ringkasan Data

**Tujuan:** [Deskripsi tujuan query ini, contoh: Menghitung total/rata-rata [nilai] per [kategori].]

```sql
SELECT
    a.[kolom_kategori],
    COUNT(b.[id_2])        AS jumlah_[entitas],
    SUM(b.[kolom_nilai])   AS total_[nilai],
    AVG(b.[kolom_nilai])   AS rata_rata_[nilai]
FROM  [nama_tabel_1] a
JOIN  [nama_tabel_2] b ON a.[id_1] = b.[id_1]
GROUP BY a.[kolom_kategori]
ORDER BY total_[nilai] DESC;
```

**Hasil:**

> *Sertakan screenshot atau tabel hasil output di sini.*

---

### 7.5 Query Lanjutan — Subquery / HAVING / Query Kompleks

**Tujuan:** [Deskripsi tujuan query, contoh: Mencari [entitas] yang memenuhi kriteria tertentu berdasarkan agregasi.]

```sql
SELECT [kolom_1], [kolom_2]
FROM   [nama_tabel]
WHERE  [id] IN (
    SELECT [id]
    FROM   [nama_tabel_lain]
    GROUP BY [id]
    HAVING COUNT(*) > [nilai]
);
```

**Hasil:**

> *Sertakan screenshot atau tabel hasil output di sini.*

---

### 7.6 Ringkasan Pengujian

| No | Query | Tujuan | Status |
|----|-------|--------|--------|
| 1 | SELECT * | Verifikasi data | ✅ Berhasil |
| 2 | WHERE | Filtering data | ✅ Berhasil |
| 3 | JOIN | Penggabungan tabel | ✅ Berhasil |
| 4 | GROUP BY + Agregasi | Ringkasan statistik | ✅ Berhasil |
| 5 | Subquery | Query kompleks | ✅ Berhasil |

---

## 8. KESIMPULAN

### 8.1 Kesimpulan

Berdasarkan hasil perancangan dan implementasi yang telah dilakukan, dapat disimpulkan:

1. **Perancangan ERD** berhasil mengidentifikasi [jumlah] entitas, yaitu [daftar entitas], beserta relasi-relasinya.
2. **Konversi ERD ke skema relasional** menghasilkan [jumlah] tabel, termasuk [jumlah] tabel asosiatif untuk relasi N:M.
3. **Implementasi DDL** berhasil membuat database `[nama_database]` dengan seluruh tabel, constraint PRIMARY KEY, dan FOREIGN KEY sesuai rancangan.
4. **Integritas referensial** terjaga melalui penerapan FOREIGN KEY dengan aturan `ON DELETE RESTRICT` dan `ON UPDATE CASCADE`.
5. **Pengujian query** membuktikan bahwa basis data dapat merespons berbagai kebutuhan data dengan benar, mulai dari query sederhana hingga JOIN dan agregasi.

### 8.2 Saran Pengembangan

- [Saran 1: misalnya, menambahkan indeks pada kolom yang sering diquery untuk meningkatkan performa]
- [Saran 2: misalnya, mengimplementasikan stored procedure untuk operasi yang sering diulang]
- [Saran 3: misalnya, menambahkan mekanisme backup otomatis]

---

## 9. REFERENSI

1. [Nama Pengarang]. ([Tahun]). *[Judul Buku]*. [Penerbit].
2. [Nama Pengarang]. ([Tahun]). *[Judul Artikel/Jurnal]*. [Nama Jurnal], [Volume]([Nomor]), [Halaman].
3. MySQL Documentation. (2024). *MySQL 8.0 Reference Manual*. Oracle Corporation. https://dev.mysql.com/doc/refman/8.0/en/
4. [Sumber lain yang digunakan]

---

## 10. LAMPIRAN

### Lampiran A — Full Script SQL (DDL + DML)

> *Sertakan keseluruhan script SQL yang dapat dijalankan secara berurutan untuk membuat ulang database dari awal.*

```sql
-- ================================================
-- DATABASE: [nama_database]
-- Proyek  : [Judul Proyek]
-- Dibuat  : [Tanggal]
-- Penulis : [Nama Mahasiswa] ([NIM])
-- ================================================

DROP DATABASE IF EXISTS [nama_database];
CREATE DATABASE [nama_database]
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE [nama_database];

-- [ Paste seluruh CREATE TABLE di sini ]

-- [ Paste seluruh INSERT INTO di sini ]
```

### Lampiran B — Screenshot Hasil Eksekusi

> *Sertakan screenshot tampilan MySQL Workbench / DBeaver / terminal mysql saat menjalankan perintah DDL, INSERT, dan query pengujian.*

**B.1 Screenshot Pembuatan Tabel**

![Screenshot DDL](./assets/screenshot_ddl.png)

**B.2 Screenshot Pengisian Data**

![Screenshot INSERT](./assets/screenshot_insert.png)

**B.3 Screenshot Hasil Query**

![Screenshot Query](./assets/screenshot_query.png)

### Lampiran C — Kamus Data *(Data Dictionary)*

| Tabel | Kolom | Tipe Data | Null | Default | Keterangan |
|-------|-------|-----------|------|---------|------------|
| [tabel_1] | [id_1] | INT | NO | AUTO_INCREMENT | PK |
| [tabel_1] | [kolom_2] | VARCHAR(100) | NO | - | [deskripsi] |
| [tabel_2] | [id_2] | INT | NO | AUTO_INCREMENT | PK |
| [tabel_2] | [id_1] | INT | NO | - | FK → [tabel_1] |

---

*— Akhir Laporan —*
