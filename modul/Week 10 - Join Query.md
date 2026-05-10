# Modul Week 10 - Join Query (MySQL)

**Mata Kuliah:** Basis Data Statistik  
**Topik:** Teori dan praktik Join Query menggunakan MySQL

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. Menjelaskan konsep join pada model data relasional.
2. Membedakan `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, dan simulasi `FULL OUTER JOIN` di MySQL.
3. Menulis query join dengan filter, agregasi, dan sorting.
4. Memahami perbedaan peletakan kondisi di `ON` dan `WHERE`.
5. Menerapkan praktik dasar optimasi query join di MySQL.

---

## 1. Teori Dasar Join

### 1.1 Mengapa JOIN dibutuhkan

Dalam basis data relasional, data biasanya dipisah ke banyak tabel agar tidak redundan. JOIN dipakai untuk menggabungkan data tersebut saat dibaca.

Contoh pada modul ini:

1. Tabel `mahasiswa` menyimpan data mahasiswa.
2. Tabel `universitas` menyimpan data jurusan.

Relasi logis: `mahasiswa.jurusan = universitas.jurusan`

### 1.2 Konsep himpunan pada JOIN

1. `INNER JOIN`: irisan data yang cocok di kedua tabel.
2. `LEFT JOIN`: semua data tabel kiri + data cocok dari tabel kanan.
3. `RIGHT JOIN`: semua data tabel kanan + data cocok dari tabel kiri.
4. `FULL OUTER JOIN`: semua data dari kedua tabel (MySQL tidak menyediakan langsung).

### 1.3 Urutan logis eksekusi query

Secara konsep, MySQL memproses query dengan urutan logis:

1. `FROM` dan `JOIN`
2. `ON`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `SELECT`
7. `ORDER BY`
8. `LIMIT`

Ini penting saat membedakan kondisi di `ON` dan `WHERE` pada outer join.

### 1.4 `ON` vs `WHERE` pada outer join

1. Kondisi di `ON` menentukan pasangan baris saat join.
2. Kondisi di `WHERE` menyaring hasil akhir.

Jika `LEFT JOIN` lalu syarat tabel kanan diletakkan di `WHERE`, hasil bisa berubah seperti `INNER JOIN` karena baris `NULL` ikut terfilter.

---

## 2. Persiapan Data (MySQL)

### 2.1 Membuat tabel

```sql
DROP TABLE IF EXISTS mahasiswa;
DROP TABLE IF EXISTS universitas;

CREATE TABLE mahasiswa (
    id_mahasiswa INT AUTO_INCREMENT PRIMARY KEY,
    nama         VARCHAR(50) NOT NULL,
    asal         VARCHAR(50) NOT NULL,
    kel          ENUM('L', 'P') NOT NULL,
    tinggi       TINYINT UNSIGNED NOT NULL,
    jurusan      VARCHAR(30) NOT NULL,
    nilai_uan    DECIMAL(5,2) NOT NULL
);

CREATE TABLE universitas (
    id_jurusan   INT AUTO_INCREMENT PRIMARY KEY,
    jurusan      VARCHAR(30) NOT NULL UNIQUE,
    tgl_berdiri  DATE NOT NULL,
    nama_dekan   VARCHAR(60) NOT NULL,
    jum_mhs      SMALLINT UNSIGNED NOT NULL,
    akr          ENUM('A', 'B', 'C', 'N/A') NOT NULL
);
```

### 2.2 Mengisi data contoh

```sql
INSERT INTO mahasiswa (nama, asal, kel, tinggi, jurusan, nilai_uan) VALUES
('Riana Putria', 'Padang', 'P', 155, 'Kimia', 339.20),
('Rudi Permana', 'Bandung', 'L', 163, 'Ilmu Komputer', 290.44),
('Sari Citra Lestari', 'Jakarta', 'P', 161, 'Manajemen', 310.60),
('Rina Kumala Sari', 'Jakarta', 'P', 158, 'Akuntansi', 337.99),
('James Situmorang', 'Medan', 'L', 168, 'Kedokteran Gigi', 341.10),
('Sandri Fatmala', 'Bandung', 'P', 165, 'Ilmu Komputer', 322.91),
('Husli Khairan', 'Jakarta', 'L', 170, 'Akuntansi', 288.55),
('Christine Wijaya', 'Medan', 'P', 157, 'Manajemen', 321.74),
('Ikhsan Prayoga', 'Jakarta', 'L', 172, 'Ilmu Komputer', 300.16),
('Bobby Permana', 'Medan', 'L', 161, 'Ilmu Komputer', 280.82);

INSERT INTO universitas (jurusan, tgl_berdiri, nama_dekan, jum_mhs, akr) VALUES
('Kimia', '1987-07-12', 'Prof. Mulyono, M.Sc.', 662, 'B'),
('Ilmu Komputer', '2003-02-23', 'Dr. Syahrial, M.Kom.', 412, 'A'),
('Akuntansi', '1985-03-19', 'Maya Fitrianti, M.M.', 895, 'B'),
('Farmasi', '1997-05-30', 'Prof. Silvia Nst, M.Farm.', 312, 'C'),
('Fisika', '1989-12-10', 'Dr. Umar Agustinus, M.Sc.', 275, 'A'),
('Hukum', '1983-08-08', 'Prof. Gunarto, M.H.', 754, 'B');
```

---

## 3. Jenis Join di MySQL

### 3.1 INNER JOIN

Hanya menampilkan data yang match di kedua tabel.

```sql
SELECT
    m.nama,
    m.jurusan,
    u.nama_dekan,
    u.akr
FROM mahasiswa AS m
INNER JOIN universitas AS u
    ON m.jurusan = u.jurusan;
```

### 3.2 LEFT JOIN

Semua data dari tabel kiri (`mahasiswa`) akan tetap tampil.

```sql
SELECT
    m.nama,
    m.jurusan,
    u.nama_dekan,
    u.akr
FROM mahasiswa AS m
LEFT JOIN universitas AS u
    ON m.jurusan = u.jurusan
ORDER BY m.nama;
```

### 3.3 RIGHT JOIN

Semua data dari tabel kanan (`universitas`) akan tetap tampil.

```sql
SELECT
    m.nama,
    m.jurusan,
    u.nama_dekan,
    u.akr
FROM mahasiswa AS m
RIGHT JOIN universitas AS u
    ON m.jurusan = u.jurusan
ORDER BY u.jurusan;
```

### 3.4 FULL OUTER JOIN di MySQL

MySQL tidak punya sintaks `FULL OUTER JOIN` langsung. Solusinya adalah gabung `LEFT JOIN` + `RIGHT JOIN` dengan `UNION`.

```sql
SELECT
    m.nama,
    m.jurusan,
    u.nama_dekan,
    u.akr
FROM mahasiswa m
LEFT JOIN universitas u ON m.jurusan = u.jurusan

UNION

SELECT
    m.nama,
    m.jurusan,
    u.nama_dekan,
    u.akr
FROM mahasiswa m
RIGHT JOIN universitas u ON m.jurusan = u.jurusan;
```

### 3.5 Implicit join vs explicit join

```sql
-- Implicit join (gaya lama)
SELECT m.nama, m.jurusan, u.nama_dekan
FROM mahasiswa m, universitas u
WHERE m.jurusan = u.jurusan;

-- Explicit join (direkomendasikan)
SELECT m.nama, m.jurusan, u.nama_dekan
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan;
```

---

## 4. Contoh Query Lanjutan

### 4.1 Join dengan filter

```sql
SELECT
    m.nama,
    m.nilai_uan,
    m.jurusan,
    u.akr
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan
WHERE m.nilai_uan > 320
  AND u.akr = 'B'
ORDER BY m.nilai_uan DESC;
```

### 4.2 Join dengan agregasi

```sql
SELECT
    m.jurusan,
    COUNT(*) AS jumlah_mahasiswa,
    ROUND(AVG(m.nilai_uan), 2) AS rata_nilai_uan,
    MAX(m.nilai_uan) AS nilai_tertinggi
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan
GROUP BY m.jurusan
ORDER BY rata_nilai_uan DESC;
```

### 4.3 Mencari data tanpa pasangan

Jurusan di tabel `universitas` yang belum dipilih mahasiswa.

```sql
SELECT
    u.jurusan,
    u.nama_dekan,
    u.akr
FROM universitas u
LEFT JOIN mahasiswa m ON m.jurusan = u.jurusan
WHERE m.id_mahasiswa IS NULL
ORDER BY u.jurusan;
```

### 4.4 Self join

Menampilkan pasangan mahasiswa dalam jurusan yang sama.

```sql
SELECT
    m1.jurusan,
    m1.nama AS mahasiswa_1,
    m2.nama AS mahasiswa_2
FROM mahasiswa m1
JOIN mahasiswa m2
    ON m1.jurusan = m2.jurusan
   AND m1.id_mahasiswa < m2.id_mahasiswa
ORDER BY m1.jurusan, m1.nama, m2.nama;
```

### 4.5 Join tiga tabel (materi tambahan teori)

Contoh pola umum saat sistem sudah besar: satu query bisa menggabungkan lebih dari 2 tabel.

```sql
SELECT a.col1, b.col2, c.col3
FROM tabel_a a
JOIN tabel_b b ON a.id_b = b.id_b
JOIN tabel_c c ON b.id_c = c.id_c;
```

---

## 5. Catatan Teori Penting di MySQL

1. Gunakan index pada kolom join, misalnya `mahasiswa.jurusan` dan `universitas.jurusan`.
2. Gunakan `EXPLAIN` untuk membaca rencana eksekusi query.
3. Hindari `SELECT *` untuk query analitik besar; pilih kolom yang diperlukan.
4. Pahami bahwa `UNION` menghapus duplikasi, sedangkan `UNION ALL` mempertahankan semua baris.
5. Untuk outer join, hati-hati menaruh filter kolom tabel kanan di `WHERE`.

Contoh cek rencana query:

```sql
EXPLAIN
SELECT m.nama, u.nama_dekan
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan;
```

---

## 6. Ringkasan

1. `INNER JOIN` untuk data yang berpasangan.
2. `LEFT JOIN` dan `RIGHT JOIN` untuk mempertahankan seluruh baris salah satu sisi.
3. `FULL OUTER JOIN` di MySQL disimulasikan dengan `LEFT JOIN` + `RIGHT JOIN` + `UNION`.
4. `ON` menentukan pasangan data, `WHERE` menyaring hasil akhir.
5. Gunakan index dan `EXPLAIN` agar query join lebih efisien.

---

## 7. Latihan

1. Tampilkan daftar mahasiswa dari kota Jakarta beserta akreditasi jurusannya.
2. Tampilkan jurusan dengan jumlah mahasiswa paling banyak (urut menurun).
3. Tampilkan jurusan yang ada di `universitas` tetapi belum dipilih mahasiswa.
4. Tampilkan 3 mahasiswa dengan nilai UAN tertinggi pada jurusan berakreditasi A.
5. Simulasikan `FULL OUTER JOIN` dan hitung jumlah baris hasil akhirnya.
6. Bandingkan hasil query saat kondisi `u.akr = 'A'` diletakkan di `ON` dan di `WHERE` pada `LEFT JOIN`.

---

## Referensi

- MySQL 8.0 Reference Manual: https://dev.mysql.com/doc/refman/8.0/en/
- MySQL JOIN Clause: https://dev.mysql.com/doc/refman/8.0/en/join.html
- SQL Style Guide (opsional): https://www.sqlstyle.guide/
