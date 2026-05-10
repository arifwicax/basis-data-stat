# Praktikum Week 10 - Join Query MySQL

## Mata Kuliah
Basis Data Statistik

## Tujuan Praktikum
1. Menjalankan query join pada MySQL dengan benar.
2. Membedakan hasil `INNER JOIN`, `LEFT JOIN`, dan `RIGHT JOIN`.
3. Mensimulasikan `FULL OUTER JOIN` di MySQL menggunakan `UNION`.
4. Menerapkan join untuk kasus filter, agregasi, dan pencarian data tanpa pasangan.

---

## A. Persiapan Lingkungan

1. Pastikan MySQL Server aktif.
2. Buat database praktikum:

```sql
DROP DATABASE IF EXISTS db_join_week10;
CREATE DATABASE db_join_week10;
USE db_join_week10;
```

3. Jalankan semua perintah DDL dan DML pada bagian B.
4. Gunakan MySQL client (CLI, MySQL Workbench, atau phpMyAdmin).

---

## B. Dataset Latihan JOIN

Jalankan SQL berikut di MySQL:

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

Validasi awal data:

```sql
SELECT COUNT(*) AS total_mahasiswa FROM mahasiswa;
SELECT COUNT(*) AS total_jurusan_universitas FROM universitas;
```

---

## C. Praktik SQL JOIN

1. INNER JOIN - menampilkan baris yang match di kedua tabel:

```sql
SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan;
```

2. LEFT JOIN - semua data mahasiswa tetap tampil:

```sql
SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
FROM mahasiswa m
LEFT JOIN universitas u ON m.jurusan = u.jurusan;
```

3. RIGHT JOIN - semua data universitas tetap tampil:

```sql
SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
FROM mahasiswa m
RIGHT JOIN universitas u ON m.jurusan = u.jurusan;
```

4. Simulasi FULL OUTER JOIN di MySQL (`LEFT JOIN` + `RIGHT JOIN` + `UNION`):

```sql
SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
FROM mahasiswa m
LEFT JOIN universitas u ON m.jurusan = u.jurusan

UNION

SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
FROM mahasiswa m
RIGHT JOIN universitas u ON m.jurusan = u.jurusan;
```

5. JOIN + filter (nilai UAN di atas 320 dan akreditasi B):

```sql
SELECT m.nama, m.nilai_uan, m.jurusan, u.akr
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan
WHERE m.nilai_uan > 320
  AND u.akr = 'B'
ORDER BY m.nilai_uan DESC;
```

6. JOIN + agregasi (jumlah dan rata-rata nilai per jurusan):

```sql
SELECT m.jurusan,
       COUNT(*) AS jumlah_mahasiswa,
       ROUND(AVG(m.nilai_uan), 2) AS rata_nilai
FROM mahasiswa m
JOIN universitas u ON m.jurusan = u.jurusan
GROUP BY m.jurusan
ORDER BY rata_nilai DESC;
```

7. Menemukan data tanpa pasangan (jurusan yang belum dipilih mahasiswa):

```sql
SELECT u.jurusan, u.nama_dekan, u.akr
FROM universitas u
LEFT JOIN mahasiswa m ON m.jurusan = u.jurusan
WHERE m.id_mahasiswa IS NULL
ORDER BY u.jurusan;
```

8. Analisis perbedaan `ON` vs `WHERE` pada `LEFT JOIN`:

```sql
-- Versi A: filter di ON
SELECT m.nama, m.jurusan, u.akr
FROM mahasiswa m
LEFT JOIN universitas u
  ON m.jurusan = u.jurusan
   AND u.akr = 'A';

-- Versi B: filter di WHERE
SELECT m.nama, m.jurusan, u.akr
FROM mahasiswa m
LEFT JOIN universitas u
  ON m.jurusan = u.jurusan
WHERE u.akr = 'A';
```

Catat perbedaan jumlah baris hasil versi A dan versi B.

---

## D. Tugas Praktikum

1. Tambahkan 2 mahasiswa baru dari jurusan Kimia.
2. Jalankan ulang query INNER JOIN dan cek apakah data baru muncul.
3. Buat query untuk menampilkan jurusan yang belum punya mahasiswa.
4. Buat query untuk menampilkan 5 mahasiswa dengan nilai UAN tertinggi.
5. Buat simulasi `FULL OUTER JOIN` dan tampilkan total jumlah baris hasilnya.
6. Buat query self join untuk menampilkan pasangan mahasiswa dalam jurusan yang sama.
7. Tulis analisis singkat (3-5 kalimat) tentang kapan sebaiknya memakai `LEFT JOIN` dibanding `INNER JOIN`.

Template jawaban hitung jumlah baris:

```sql
SELECT COUNT(*) AS total_baris
FROM (
  SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
  FROM mahasiswa m
  LEFT JOIN universitas u ON m.jurusan = u.jurusan

  UNION

  SELECT m.nama, m.jurusan, u.nama_dekan, u.akr
  FROM mahasiswa m
  RIGHT JOIN universitas u ON m.jurusan = u.jurusan
) AS hasil_full_join;
```

---

## E. Kriteria Penilaian

1. Ketepatan hasil query JOIN.
2. Kerapian dan keterbacaan SQL.
3. Ketepatan penggunaan `ON` dan `WHERE`.
4. Ketepatan penggunaan agregasi (`COUNT`, `AVG`, `GROUP BY`).
5. Kemampuan menjelaskan hasil dan insight query.
