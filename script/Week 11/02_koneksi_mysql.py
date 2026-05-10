# ============================================================
# 02_koneksi_mysql.py
# Week 11 - Basis Data Statistik
# Topik: Koneksi Python ke PostgreSQL + contoh query JOIN
# ============================================================

import sys

import psycopg2
from psycopg2 import Error

# -------------------------------------------------------
# CONFIG — sesuaikan dengan PostgreSQL lokal Anda
# -------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "postgres",
    "dbname": "sistem_akademik",
}


def print_section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


print("=" * 60)
print("1. MEMBUAT KONEKSI KE POSTGRESQL")
print("=" * 60)

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Koneksi berhasil!")
    print(f"Database aktif: {DB_CONFIG['dbname']}")
except Error as err:
    print(f"Koneksi gagal: {err}")
    print("Periksa HOST, PORT, USER, PASSWORD, dan nama database di DB_CONFIG.")
    sys.exit(1)

cursor = conn.cursor()

print_section("2. QUERY SELECT SEDERHANA")
cursor.execute("SELECT nim, nama, email FROM mahasiswa LIMIT 5")
rows = cursor.fetchall()

print(f"{'NIM':<14} {'NAMA':<22} {'EMAIL'}")
print("-" * 70)
for nim, nama, email in rows:
    print(f"{nim:<14} {nama:<22} {email or '(kosong)'}")

print_section("3. QUERY JOIN: MAHASISWA + JURUSAN")
query_join = """
    SELECT m.nim, m.nama, j.nama AS jurusan, j.jenjang
    FROM mahasiswa m
    JOIN jurusan j ON m.kode_jurusan = j.kode
    ORDER BY j.nama, m.nama
"""
cursor.execute(query_join)
rows = cursor.fetchall()

print(f"{'NIM':<14} {'NAMA':<22} {'JURUSAN':<28} {'JENJANG'}")
print("-" * 90)
for nim, nama, jurusan, jenjang in rows:
    print(f"{nim:<14} {nama:<22} {jurusan:<28} {jenjang}")

print_section("4. QUERY PARAMETERIZED (AMAN SQL INJECTION)")
jurusan_cari = "IF"
cursor.execute(
    "SELECT nim, nama FROM mahasiswa WHERE kode_jurusan = %s ORDER BY nama",
    (jurusan_cari,),
)
rows = cursor.fetchall()

print(f"Mahasiswa jurusan '{jurusan_cari}':")
for nim, nama in rows:
    print(f"- {nim} | {nama}")

print_section("5. AGREGASI DENGAN JOIN")
cursor.execute(
    """
    SELECT j.nama, j.jenjang, COUNT(m.nim) AS jumlah
    FROM jurusan j
    LEFT JOIN mahasiswa m ON m.kode_jurusan = j.kode
    GROUP BY j.kode, j.nama, j.jenjang
    ORDER BY jumlah DESC, j.nama
    """
)
rows = cursor.fetchall()

print(f"{'JURUSAN':<30} {'JENJANG':<8} {'JUMLAH':>7}")
print("-" * 52)
for jurusan, jenjang, jumlah in rows:
    print(f"{jurusan:<30} {jenjang:<8} {jumlah:>7}")

print_section("6. MENUTUP KONEKSI")
cursor.close()
conn.close()
print("Cursor dan koneksi berhasil ditutup.")
