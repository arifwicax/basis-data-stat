# ============================================================
# 02_koneksi_mysql.py
# Week 10 - Basis Data
# Topik: Koneksi Python ke MySQL (database sistem_akademik)
# ============================================================
#
# Pastikan database sistem_akademik sudah dibuat dari Week 9:
#   mysql -u root -p < ../Week\ 9/week9_implementasi_erd.sql
#
# Sesuaikan HOST, PORT, USER, PASSWORD di bagian CONFIG.
# ============================================================

import mysql.connector
from mysql.connector import Error

# -------------------------------------------------------
# CONFIG — sesuaikan dengan pengaturan MySQL lokal Anda
# -------------------------------------------------------
DB_CONFIG = {
    "host"     : "localhost",
    "port"     : 3306,       # XAMPP/default: 3306 | MAMP: 8889
    "user"     : "root",
    "password" : "root",     # ganti sesuai password Anda
    "database" : "sistem_akademik"
}

# -------------------------------------------------------
# 1. MEMBUAT KONEKSI
# -------------------------------------------------------
print("=" * 55)
print("1. MEMBUAT KONEKSI KE MYSQL")
print("=" * 55)

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    if conn.is_connected():
        info = conn.get_server_info()
        print(f"✓ Koneksi berhasil! Versi MySQL Server: {info}")
        print(f"  Database aktif: {DB_CONFIG['database']}")
except Error as e:
    print(f"✗ Koneksi gagal: {e}")
    print("  Periksa HOST, PORT, USER, PASSWORD di DB_CONFIG.")
    exit(1)

cursor = conn.cursor()

# -------------------------------------------------------
# 2. QUERY SELECT SEDERHANA
# -------------------------------------------------------
print("\n" + "=" * 55)
print("2. QUERY SELECT SEDERHANA")
print("=" * 55)

cursor.execute("SELECT nim, nama, email FROM Mahasiswa LIMIT 5")
rows = cursor.fetchall()

print(f"{'NIM':<14} {'NAMA':<20} {'EMAIL'}")
print("-" * 55)
for nim, nama, email in rows:
    email_str = email if email else "(kosong)"
    print(f"{nim:<14} {nama:<20} {email_str}")

# -------------------------------------------------------
# 3. QUERY DENGAN JOIN
# -------------------------------------------------------
print("\n" + "=" * 55)
print("3. QUERY DENGAN JOIN — Mahasiswa + Jurusan")
print("=" * 55)

query_join = """
    SELECT m.nim, m.nama, j.nama AS jurusan, j.jenjang
    FROM   Mahasiswa m
    JOIN   Jurusan   j ON m.kode_jurusan = j.kode
    ORDER  BY j.nama, m.nama
"""
cursor.execute(query_join)
rows = cursor.fetchall()

print(f"{'NIM':<14} {'NAMA':<18} {'JURUSAN':<28} {'JENJANG'}")
print("-" * 70)
for nim, nama, jurusan, jenjang in rows:
    print(f"{nim:<14} {nama:<18} {jurusan:<28} {jenjang}")

# -------------------------------------------------------
# 4. QUERY DENGAN PARAMETER (%s) — Aman dari SQL Injection
# -------------------------------------------------------
print("\n" + "=" * 55)
print("4. QUERY DENGAN PARAMETER")
print("=" * 55)

jurusan_cari = "IF"
cursor.execute(
    "SELECT nim, nama FROM Mahasiswa WHERE kode_jurusan = %s ORDER BY nama",
    (jurusan_cari,)   # parameter selalu berupa tuple
)
rows = cursor.fetchall()
print(f"Mahasiswa jurusan '{jurusan_cari}':")
for nim, nama in rows:
    print(f"  {nim} — {nama}")

# -------------------------------------------------------
# 5. QUERY AGREGASI
# -------------------------------------------------------
print("\n" + "=" * 55)
print("5. QUERY AGREGASI — Jumlah Mahasiswa per Jurusan")
print("=" * 55)

cursor.execute("""
    SELECT j.nama, j.jenjang, COUNT(m.nim) AS jumlah
    FROM   Jurusan   j
    LEFT JOIN Mahasiswa m ON m.kode_jurusan = j.kode
    GROUP  BY j.kode, j.nama, j.jenjang
    ORDER  BY jumlah DESC
""")
rows = cursor.fetchall()

print(f"{'JURUSAN':<30} {'JENJANG':<8} {'JUMLAH':>7}")
print("-" * 48)
for jurusan, jenjang, jumlah in rows:
    bar = "█" * jumlah                 # bar sederhana di terminal
    print(f"{jurusan:<30} {jenjang:<8} {jumlah:>7}  {bar}")

# -------------------------------------------------------
# 6. FETCHONE vs FETCHALL vs FETCHMANY
# -------------------------------------------------------
print("\n" + "=" * 55)
print("6. FETCHONE / FETCHALL / FETCHMANY")
print("=" * 55)

cursor.execute("SELECT nip, nama FROM Dosen ORDER BY nama")

# fetchone() — ambil satu baris
satu = cursor.fetchone()
print(f"fetchone() : {satu}")

# fetchmany(n) — ambil n baris berikutnya
beberapa = cursor.fetchmany(2)
print(f"fetchmany(2): {beberapa}")

# fetchall() — ambil sisa baris
sisa = cursor.fetchall()
print(f"fetchall() sisanya: {len(sisa)} baris")

# -------------------------------------------------------
# 7. MENUTUP KONEKSI
# -------------------------------------------------------
print("\n" + "=" * 55)
print("7. MENUTUP KONEKSI")
print("=" * 55)

cursor.close()
conn.close()
print("✓ Cursor dan koneksi berhasil ditutup.")
