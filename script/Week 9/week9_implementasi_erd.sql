-- ============================================================
-- Implementasi ERD Sistem Akademik
-- Week 9 - Basis Data
-- ============================================================

DROP DATABASE IF EXISTS sistem_akademik;
CREATE DATABASE sistem_akademik CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sistem_akademik;

-- ============================================================
-- DDL: Buat Tabel
-- ============================================================

-- 1. Tabel Jurusan
CREATE TABLE Jurusan (
    kode        VARCHAR(10)  NOT NULL,
    nama        VARCHAR(100) NOT NULL,
    jenjang     VARCHAR(5)   NOT NULL,  -- S1, S2, D3, dst.
    CONSTRAINT pk_jurusan PRIMARY KEY (kode)
);

-- 2. Tabel Dosen
CREATE TABLE Dosen (
    nip         VARCHAR(20)  NOT NULL,
    nama        VARCHAR(100) NOT NULL,
    email       VARCHAR(100),
    CONSTRAINT pk_dosen PRIMARY KEY (nip)
);

-- 3. Tabel Mahasiswa
--    - kode_jurusan : relasi "memiliki" (N Mahasiswa → 1 Jurusan)
--    - nip_wali     : relasi "Wali"     (N Mahasiswa → 1 Dosen)
--    - nip_pembimbing : relasi "Pembimbing Skripsi" (N Mahasiswa → 1 Dosen)
CREATE TABLE Mahasiswa (
    nim             VARCHAR(15)  NOT NULL,
    nama            VARCHAR(100) NOT NULL,
    email           VARCHAR(100),
    kode_jurusan    VARCHAR(10)  NOT NULL,
    nip_wali        VARCHAR(20),
    nip_pembimbing  VARCHAR(20),
    CONSTRAINT pk_mahasiswa         PRIMARY KEY (nim),
    CONSTRAINT fk_mhs_jurusan       FOREIGN KEY (kode_jurusan)   REFERENCES Jurusan(kode),
    CONSTRAINT fk_mhs_wali          FOREIGN KEY (nip_wali)       REFERENCES Dosen(nip),
    CONSTRAINT fk_mhs_pembimbing    FOREIGN KEY (nip_pembimbing) REFERENCES Dosen(nip)
);

-- 4. Tabel Matakuliah
CREATE TABLE Matakuliah (
    kode_mk     VARCHAR(10)  NOT NULL,
    nama        VARCHAR(100) NOT NULL,
    sks         TINYINT      NOT NULL,
    CONSTRAINT pk_matakuliah PRIMARY KEY (kode_mk)
);

-- 5. Tabel Prasyarat (relasi rekursif pada Matakuliah)
--    Satu Matakuliah dapat memiliki banyak prasyarat
CREATE TABLE Prasyarat (
    kode_mk          VARCHAR(10) NOT NULL,
    kode_mk_prasyarat VARCHAR(10) NOT NULL,
    CONSTRAINT pk_prasyarat PRIMARY KEY (kode_mk, kode_mk_prasyarat),
    CONSTRAINT fk_prs_mk        FOREIGN KEY (kode_mk)           REFERENCES Matakuliah(kode_mk),
    CONSTRAINT fk_prs_mk_prs    FOREIGN KEY (kode_mk_prasyarat) REFERENCES Matakuliah(kode_mk)
);

-- 6. Tabel Mengajar (entitas asosiatif Dosen ↔ Matakuliah)
CREATE TABLE Mengajar (
    id_mengajar INT          NOT NULL AUTO_INCREMENT,
    nip_dosen   VARCHAR(20)  NOT NULL,
    kode_mk     VARCHAR(10)  NOT NULL,
    semester    VARCHAR(15)  NOT NULL,  -- Ganjil / Genap
    tahun       YEAR         NOT NULL,
    CONSTRAINT pk_mengajar  PRIMARY KEY (id_mengajar),
    CONSTRAINT fk_mgj_dosen FOREIGN KEY (nip_dosen) REFERENCES Dosen(nip),
    CONSTRAINT fk_mgj_mk    FOREIGN KEY (kode_mk)   REFERENCES Matakuliah(kode_mk)
);

-- 7. Tabel Mengikuti (relasi Mahasiswa mengikuti kelas Mengajar)
CREATE TABLE Mengikuti (
    nim         VARCHAR(15) NOT NULL,
    id_mengajar INT         NOT NULL,
    CONSTRAINT pk_mengikuti  PRIMARY KEY (nim, id_mengajar),
    CONSTRAINT fk_mgt_mhs    FOREIGN KEY (nim)         REFERENCES Mahasiswa(nim),
    CONSTRAINT fk_mgt_mgj    FOREIGN KEY (id_mengajar) REFERENCES Mengajar(id_mengajar)
);


-- ============================================================
-- DML: Dummy Data
-- ============================================================

-- Jurusan
INSERT INTO Jurusan (kode, nama, jenjang) VALUES
    ('IF',  'Teknik Informatika',          'S1'),
    ('SI',  'Sistem Informasi',            'S1'),
    ('TK',  'Teknik Komputer',             'S1'),
    ('MTI', 'Magister Teknik Informatika', 'S2'),
    ('MI',  'Manajemen Informatika',       'D3');

-- Dosen
INSERT INTO Dosen (nip, nama, email) VALUES
    ('198501012010011001', 'Dr. Ahmad Fauzi, M.Kom',     'ahmad.fauzi@univ.ac.id'),
    ('197803152005012002', 'Dr. Siti Rahayu, M.T',       'siti.rahayu@univ.ac.id'),
    ('198209202008011003', 'Budi Santoso, S.Kom, M.Cs',  'budi.santoso@univ.ac.id'),
    ('197512102003012004', 'Dewi Anggraini, M.Kom',      'dewi.anggraini@univ.ac.id'),
    ('198811252015011005', 'Rizky Pratama, M.T',         'rizky.pratama@univ.ac.id');

-- Matakuliah
INSERT INTO Matakuliah (kode_mk, nama, sks) VALUES
    ('MK001', 'Basis Data',                   3),
    ('MK002', 'Pemrograman Web',              3),
    ('MK003', 'Struktur Data',                3),
    ('MK004', 'Algoritma dan Pemrograman',    3),
    ('MK005', 'Sistem Operasi',               3),
    ('MK006', 'Jaringan Komputer',            3),
    ('MK007', 'Rekayasa Perangkat Lunak',     3),
    ('MK008', 'Kecerdasan Buatan',            3);

-- Prasyarat
INSERT INTO Prasyarat (kode_mk, kode_mk_prasyarat) VALUES
    ('MK001', 'MK004'),   -- Basis Data   prasyarat: Algoritma dan Pemrograman
    ('MK002', 'MK004'),   -- Pemrograman Web prasyarat: Algoritma dan Pemrograman
    ('MK003', 'MK004'),   -- Struktur Data prasyarat: Algoritma dan Pemrograman
    ('MK007', 'MK003'),   -- RPL prasyarat: Struktur Data
    ('MK008', 'MK003'),   -- Kecerdasan Buatan prasyarat: Struktur Data
    ('MK006', 'MK005');   -- Jaringan Komputer prasyarat: Sistem Operasi

-- Mahasiswa
INSERT INTO Mahasiswa (nim, nama, email, kode_jurusan, nip_wali, nip_pembimbing) VALUES
    ('2021001001', 'Andi Wijaya',       'andi.wijaya@student.univ.ac.id',       'IF',  '198501012010011001', '197803152005012002'),
    ('2021001002', 'Bela Safitri',      'bela.safitri@student.univ.ac.id',      'IF',  '198501012010011001', '198209202008011003'),
    ('2021001003', 'Candra Kusuma',     'candra.kusuma@student.univ.ac.id',     'SI',  '197803152005012002', '198501012010011001'),
    ('2021001004', 'Diana Pertiwi',     'diana.pertiwi@student.univ.ac.id',     'SI',  '197803152005012002', '197512102003012004'),
    ('2021001005', 'Eko Prasetyo',      'eko.prasetyo@student.univ.ac.id',      'TK',  '198209202008011003', '198811252015011005'),
    ('2021001006', 'Fitri Handayani',   'fitri.handayani@student.univ.ac.id',   'TK',  '198209202008011003', '198501012010011001'),
    ('2021001007', 'Galang Ramadhan',   'galang.ramadhan@student.univ.ac.id',   'IF',  '197512102003012004', '197803152005012002'),
    ('2021001008', 'Hani Lestari',      'hani.lestari@student.univ.ac.id',      'SI',  '198811252015011005', '198209202008011003'),
    ('2021001009', 'Ivan Setiawan',     'ivan.setiawan@student.univ.ac.id',     'IF',  '198501012010011001', NULL),
    ('2021001010', 'Julia Anggraeni',   'julia.anggraeni@student.univ.ac.id',   'MI',  '197512102003012004', NULL);

-- Mengajar (kelas yang diajarkan per semester/tahun)
INSERT INTO Mengajar (nip_dosen, kode_mk, semester, tahun) VALUES
    ('198501012010011001', 'MK001', 'Ganjil',  2024),   -- id=1
    ('198501012010011001', 'MK003', 'Genap',   2024),   -- id=2
    ('197803152005012002', 'MK002', 'Ganjil',  2024),   -- id=3
    ('197803152005012002', 'MK007', 'Genap',   2024),   -- id=4
    ('198209202008011003', 'MK004', 'Ganjil',  2024),   -- id=5
    ('198209202008011003', 'MK005', 'Genap',   2024),   -- id=6
    ('197512102003012004', 'MK006', 'Genap',   2024),   -- id=7
    ('198811252015011005', 'MK008', 'Ganjil',  2024),   -- id=8
    ('198501012010011001', 'MK001', 'Ganjil',  2025),   -- id=9
    ('197803152005012002', 'MK002', 'Ganjil',  2025);   -- id=10

-- Mengikuti (pendaftaran mahasiswa ke kelas)
INSERT INTO Mengikuti (nim, id_mengajar) VALUES
    -- Andi Wijaya mengambil beberapa kelas
    ('2021001001', 1),
    ('2021001001', 3),
    ('2021001001', 5),
    -- Bela Safitri
    ('2021001002', 1),
    ('2021001002', 6),
    ('2021001002', 8),
    -- Candra Kusuma
    ('2021001003', 3),
    ('2021001003', 4),
    ('2021001003', 5),
    -- Diana Pertiwi
    ('2021001004', 1),
    ('2021001004', 3),
    ('2021001004', 7),
    -- Eko Prasetyo
    ('2021001005', 5),
    ('2021001005', 6),
    ('2021001005', 8),
    -- Fitri Handayani
    ('2021001006', 2),
    ('2021001006', 5),
    ('2021001006', 7),
    -- Galang Ramadhan
    ('2021001007', 1),
    ('2021001007', 8),
    -- Hani Lestari
    ('2021001008', 3),
    ('2021001008', 4),
    ('2021001008', 6),
    -- Ivan Setiawan
    ('2021001009', 9),
    ('2021001009', 5),
    -- Julia Anggraeni
    ('2021001010', 5),
    ('2021001010', 6);


-- ============================================================
-- Verifikasi Data
-- ============================================================

-- Daftar mahasiswa beserta jurusan dan dosen wali
SELECT
    m.nim,
    m.nama                  AS mahasiswa,
    j.nama                  AS jurusan,
    j.jenjang,
    dw.nama                 AS dosen_wali,
    dp.nama                 AS pembimbing_skripsi
FROM Mahasiswa m
JOIN Jurusan  j  ON m.kode_jurusan   = j.kode
LEFT JOIN Dosen dw ON m.nip_wali       = dw.nip
LEFT JOIN Dosen dp ON m.nip_pembimbing = dp.nip
ORDER BY m.nim;

-- Jadwal mengajar dosen
SELECT
    mg.id_mengajar,
    d.nama      AS dosen,
    mk.nama     AS matakuliah,
    mk.sks,
    mg.semester,
    mg.tahun
FROM Mengajar mg
JOIN Dosen      d  ON mg.nip_dosen = d.nip
JOIN Matakuliah mk ON mg.kode_mk   = mk.kode_mk
ORDER BY mg.tahun, mg.semester, d.nama;

-- KRS mahasiswa (mata kuliah yang diikuti)
SELECT
    mhs.nim,
    mhs.nama    AS mahasiswa,
    mk.kode_mk,
    mk.nama     AS matakuliah,
    mk.sks,
    mg.semester,
    mg.tahun,
    d.nama      AS dosen_pengampu
FROM Mengikuti  mgt
JOIN Mahasiswa  mhs ON mgt.nim         = mhs.nim
JOIN Mengajar   mg  ON mgt.id_mengajar = mg.id_mengajar
JOIN Matakuliah mk  ON mg.kode_mk      = mk.kode_mk
JOIN Dosen      d   ON mg.nip_dosen    = d.nip
ORDER BY mhs.nim, mg.tahun, mg.semester;

-- Prasyarat matakuliah
SELECT
    mk.nama              AS matakuliah,
    mp.nama              AS prasyarat
FROM Prasyarat  p
JOIN Matakuliah mk ON p.kode_mk           = mk.kode_mk
JOIN Matakuliah mp ON p.kode_mk_prasyarat = mp.kode_mk
ORDER BY mk.nama;
