# ============================================================
# 03_pandas_dataframe.py
# Week 11 - Basis Data Statistik
# Topik: Pengolahan Data PostgreSQL dengan pandas DataFrame
# ============================================================

import pandas as pd
import psycopg2

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "postgres",
    "dbname": "sistem_akademik",
}

def get_df(query, columns, params=None):
    """Jalankan query dan kembalikan sebagai pandas DataFrame."""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params or ())
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
    finally:
        cursor.close()
        conn.close()
    return df


# -------------------------------------------------------
# 1. MEMBUAT DATAFRAME DARI POSTGRESQL
# -------------------------------------------------------
print("=" * 60)
print("1. DATAFRAME MAHASISWA")
print("=" * 60)

df_mhs = get_df("""
    SELECT m.nim, m.nama, j.nama AS jurusan, j.jenjang,
           dw.nama AS dosen_wali
    FROM   Mahasiswa m
    JOIN   Jurusan   j  ON m.kode_jurusan = j.kode
    LEFT JOIN Dosen  dw ON m.nip_wali     = dw.nip
    ORDER  BY m.nim
""", ["nim", "nama", "jurusan", "jenjang", "dosen_wali"])

print(df_mhs.to_string(index=False))

# -------------------------------------------------------
# 2. EKSPLORASI DATAFRAME
# -------------------------------------------------------
print("\n" + "=" * 60)
print("2. EKSPLORASI DATAFRAME")
print("=" * 60)

print(f"\n• Bentuk (baris x kolom) : {df_mhs.shape}")
print(f"• Tipe data tiap kolom:\n{df_mhs.dtypes}")
print(f"\n• 3 baris pertama (head):\n{df_mhs.head(3)}")
print(f"\n• Cek nilai NULL per kolom:\n{df_mhs.isnull().sum()}")

# -------------------------------------------------------
# 3. FILTER BARIS
# -------------------------------------------------------
print("\n" + "=" * 60)
print("3. FILTER BARIS")
print("=" * 60)

# Filter satu kondisi
df_s1 = df_mhs[df_mhs["jenjang"] == "S1"]
print(f"\nMahasiswa jenjang S1: {len(df_s1)} orang")

# Filter gabungan (& = AND, | = OR)
df_if_s1 = df_mhs[(df_mhs["jurusan"] == "Teknik Informatika") & (df_mhs["jenjang"] == "S1")]
print(f"Mahasiswa Teknik Informatika (S1): {len(df_if_s1)} orang")
print(df_if_s1[["nim", "nama", "dosen_wali"]].to_string(index=False))

# -------------------------------------------------------
# 4. AGREGASI — groupby
# -------------------------------------------------------
print("\n" + "=" * 60)
print("4. AGREGASI — JUMLAH MAHASISWA PER JURUSAN")
print("=" * 60)

per_jurusan = (
    df_mhs
    .groupby(["jurusan", "jenjang"])["nim"]
    .count()
    .reset_index()
    .rename(columns={"nim": "jumlah_mahasiswa"})
    .sort_values("jumlah_mahasiswa", ascending=False)
)
print(per_jurusan.to_string(index=False))

# -------------------------------------------------------
# 5. DATAFRAME KRS + TOTAL SKS
# -------------------------------------------------------
print("\n" + "=" * 60)
print("5. KRS MAHASISWA — TOTAL SKS PER MAHASISWA (2024)")
print("=" * 60)

df_krs = get_df("""
    SELECT mhs.nim, mhs.nama,
           mk.kode_mk, mk.nama AS matakuliah, mk.sks,
           mg.semester, mg.tahun
    FROM   Mengikuti  mgt
    JOIN   Mahasiswa  mhs ON mgt.nim         = mhs.nim
    JOIN   Mengajar   mg  ON mgt.id_mengajar = mg.id_mengajar
    JOIN   Matakuliah mk  ON mg.kode_mk      = mk.kode_mk
    WHERE  mg.tahun = 2024
    ORDER  BY mhs.nim, mg.semester
""", ["nim", "nama", "kode_mk", "matakuliah", "sks", "semester", "tahun"])

# Total SKS per mahasiswa
df_total_sks = (
    df_krs
    .groupby(["nim", "nama"])["sks"]
    .sum()
    .reset_index()
    .rename(columns={"sks": "total_sks"})
    .sort_values("total_sks", ascending=False)
)
print(df_total_sks.to_string(index=False))

print(f"\nRata-rata SKS : {df_total_sks['total_sks'].mean():.2f}")
print(f"Maksimum SKS  : {df_total_sks['total_sks'].max()}")
print(f"Minimum SKS   : {df_total_sks['total_sks'].min()}")

# -------------------------------------------------------
# 6. PIVOT TABLE — Peserta per Matakuliah per Semester
# -------------------------------------------------------
print("\n" + "=" * 60)
print("6. PIVOT TABLE — PESERTA PER MATAKULIAH PER SEMESTER (2024)")
print("=" * 60)

pivot = df_krs.pivot_table(
    index   = "matakuliah",
    columns = "semester",
    values  = "nim",
    aggfunc = "count",
    fill_value = 0
)
print(pivot)

# -------------------------------------------------------
# 7. MERGE DUA DATAFRAME
# -------------------------------------------------------
print("\n" + "=" * 60)
print("7. MERGE — Gabungkan DataFrame KRS dengan Total SKS")
print("=" * 60)

df_gabung = df_mhs[["nim", "nama", "jurusan"]].merge(
    df_total_sks[["nim", "total_sks"]],
    on  = "nim",
    how = "left"    # left join: semua mahasiswa tetap muncul, meski tidak ada di KRS
)
df_gabung["total_sks"] = df_gabung["total_sks"].fillna(0).astype(int)
print(df_gabung.to_string(index=False))

# -------------------------------------------------------
# 8. STATISTIK DESKRIPTIF
# -------------------------------------------------------
print("\n" + "=" * 60)
print("8. STATISTIK DESKRIPTIF")
print("=" * 60)

df_mk = get_df(
    "SELECT kode_mk, nama, sks FROM Matakuliah",
    ["kode_mk", "nama", "sks"]
)

print(f"\nTotal SKS seluruh matakuliah : {df_mk['sks'].sum()}")
print(f"Rata-rata SKS per matakuliah : {df_mk['sks'].mean():.2f}")
print(f"\nDistribusi nilai SKS:")
print(df_mk["sks"].value_counts().sort_index())
