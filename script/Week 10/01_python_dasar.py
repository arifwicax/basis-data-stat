# ============================================================
# 01_python_dasar.py
# Week 10 - Basis Data
# Topik: Sintaks Dasar Python untuk Pengolahan Data
# ============================================================

# -------------------------------------------------------
# 1. VARIABEL DAN TIPE DATA
# -------------------------------------------------------
print("=" * 50)
print("1. VARIABEL DAN TIPE DATA")
print("=" * 50)

nim      = "2021001001"   # str
nama     = "Andi Wijaya"  # str
sks      = 18             # int
ipk      = 3.75           # float
aktif    = True           # bool

print(f"NIM    : {nim}  -> tipe: {type(nim).__name__}")
print(f"Nama   : {nama} -> tipe: {type(nama).__name__}")
print(f"SKS    : {sks}  -> tipe: {type(sks).__name__}")
print(f"IPK    : {ipk}  -> tipe: {type(ipk).__name__}")
print(f"Aktif  : {aktif} -> tipe: {type(aktif).__name__}")

# -------------------------------------------------------
# 2. LIST
# -------------------------------------------------------
print("\n" + "=" * 50)
print("2. LIST")
print("=" * 50)

matakuliah = ["Basis Data", "Pemrograman Web", "Struktur Data", "Algoritma"]

print(f"Semua  : {matakuliah}")
print(f"Pertama: {matakuliah[0]}")      # indeks dimulai dari 0
print(f"Terakhir: {matakuliah[-1]}")    # indeks -1 = elemen terakhir
print(f"Jumlah : {len(matakuliah)}")

# Tambah elemen
matakuliah.append("Sistem Operasi")
print(f"Setelah append: {matakuliah}")

# Slice
print(f"Indeks 1-2: {matakuliah[1:3]}")  # [start:end] → end tidak termasuk

# -------------------------------------------------------
# 3. DICTIONARY
# -------------------------------------------------------
print("\n" + "=" * 50)
print("3. DICTIONARY")
print("=" * 50)

mahasiswa = {
    "nim"          : "2021001001",
    "nama"         : "Andi Wijaya",
    "jurusan"      : "Teknik Informatika",
    "total_sks"    : 18,
    "ipk"          : 3.75
}

print(f"NIM     : {mahasiswa['nim']}")
print(f"Nama    : {mahasiswa['nama']}")
print(f"IPK     : {mahasiswa['ipk']}")

# Tambah / ubah nilai
mahasiswa["email"] = "andi@student.univ.ac.id"
print(f"Email   : {mahasiswa['email']}")

# Iterasi key-value
print("\nSemua data mahasiswa:")
for key, value in mahasiswa.items():
    print(f"  {key:12s}: {value}")

# -------------------------------------------------------
# 4. PERULANGAN (LOOP)
# -------------------------------------------------------
print("\n" + "=" * 50)
print("4. PERULANGAN")
print("=" * 50)

# for loop atas list
print("Daftar matakuliah:")
for i, mk in enumerate(matakuliah, start=1):
    print(f"  {i}. {mk}")

# for loop dengan range
print("\nSemester 1 sampai 8:")
for semester in range(1, 9):
    print(f"  Semester {semester}", end="")
    if semester % 2 == 0:
        print(" (Genap)", end="")
    else:
        print(" (Ganjil)", end="")
    print()

# while loop
print("\nHitung mundur dari 5:")
n = 5
while n > 0:
    print(f"  {n}...")
    n -= 1
print("  Selesai!")

# -------------------------------------------------------
# 5. KONDISIONAL
# -------------------------------------------------------
print("\n" + "=" * 50)
print("5. KONDISIONAL")
print("=" * 50)

def predikat_ipk(ipk):
    if ipk >= 3.5:
        return "Cumlaude"
    elif ipk >= 3.0:
        return "Sangat Memuaskan"
    elif ipk >= 2.5:
        return "Memuaskan"
    else:
        return "Cukup"

daftar_ipk = [3.75, 3.20, 2.80, 2.40]
for nilai in daftar_ipk:
    print(f"  IPK {nilai} → {predikat_ipk(nilai)}")

# -------------------------------------------------------
# 6. FUNGSI
# -------------------------------------------------------
print("\n" + "=" * 50)
print("6. FUNGSI")
print("=" * 50)

def hitung_total_sks(daftar_sks: list) -> int:
    """Menjumlahkan semua SKS dari daftar yang diberikan."""
    return sum(daftar_sks)

def format_nama_nim(nama: str, nim: str) -> str:
    """Menggabungkan nama dan NIM menjadi label."""
    return f"{nama} ({nim})"

sks_list = [3, 3, 3, 2, 3, 2]
print(f"Total SKS: {hitung_total_sks(sks_list)}")
print(format_nama_nim("Andi Wijaya", "2021001001"))

# -------------------------------------------------------
# 7. LIST COMPREHENSION
# -------------------------------------------------------
print("\n" + "=" * 50)
print("7. LIST COMPREHENSION")
print("=" * 50)

# Cara panjang
sks_values = [3, 2, 3, 3, 2]
sks_berlaku = []
for s in sks_values:
    if s >= 3:
        sks_berlaku.append(s)

# Cara singkat dengan list comprehension
sks_berlaku = [s for s in sks_values if s >= 3]
print(f"SKS >= 3: {sks_berlaku}")

# Buat list nama mahasiswa dalam huruf besar
nama_mahasiswa = ["Andi", "Bela", "Candra", "Diana"]
nama_upper = [n.upper() for n in nama_mahasiswa]
print(f"Nama kapital: {nama_upper}")

# -------------------------------------------------------
# 8. F-STRING DAN FORMAT ANGKA
# -------------------------------------------------------
print("\n" + "=" * 50)
print("8. F-STRING DAN FORMAT ANGKA")
print("=" * 50)

total = 18
maks  = 24
persen = total / maks * 100

print(f"SKS diambil : {total} dari {maks}")
print(f"Persentase  : {persen:.1f}%")          # 1 desimal
print(f"IPK         : {3.75:.2f}")              # 2 desimal
print(f"NIM rata kanan: {nim:>15}")             # rata kanan lebar 15
print(f"Nama rata kiri: {nama:<20}|")           # rata kiri lebar 20
