# ============================================================
# 04_visualisasi.py
# Week 10 - Basis Data
# Topik: Visualisasi Data MySQL dengan Matplotlib & Seaborn
#
# Menghasilkan satu figure dengan 4 grafik:
#   [1] Bar Chart   — Jumlah Mahasiswa per Jurusan
#   [2] Horiz. Bar  — Total SKS per Mahasiswa (2024)
#   [3] Pie Chart   — Proporsi Mahasiswa per Jenjang
#   [4] Stacked Bar — Peserta Matakuliah per Jurusan
# ============================================================

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
DB_CONFIG = {
    "host"     : "localhost",
    "port"     : 3306,
    "user"     : "root",
    "password" : "root",
    "database" : "sistem_akademik"
}

WARNA_UTAMA = "#4C72B0"
WARNA_SET   = sns.color_palette("tab10")

def get_df(query, columns, params=None):
    conn   = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params or ())
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
    finally:
        cursor.close()
        conn.close()
    return df

# -------------------------------------------------------
# AMBIL DATA
# -------------------------------------------------------

# [1] Jumlah mahasiswa per jurusan
df_per_jurusan = get_df("""
    SELECT j.nama, COUNT(m.nim) AS jumlah
    FROM   Jurusan j
    LEFT JOIN Mahasiswa m ON m.kode_jurusan = j.kode
    GROUP  BY j.kode, j.nama
    ORDER  BY jumlah DESC
""", ["jurusan", "jumlah"])

# [2] Total SKS per mahasiswa tahun 2024
df_sks = get_df("""
    SELECT mhs.nama, SUM(mk.sks) AS total_sks
    FROM   Mengikuti  mgt
    JOIN   Mahasiswa  mhs ON mgt.nim         = mhs.nim
    JOIN   Mengajar   mg  ON mgt.id_mengajar = mg.id_mengajar
    JOIN   Matakuliah mk  ON mg.kode_mk      = mk.kode_mk
    WHERE  mg.tahun = 2024
    GROUP  BY mhs.nim, mhs.nama
    ORDER  BY total_sks DESC
""", ["nama", "total_sks"])

# [3] Proporsi mahasiswa per jenjang
df_jenjang = get_df("""
    SELECT j.jenjang, COUNT(m.nim) AS jumlah
    FROM   Jurusan j
    LEFT JOIN Mahasiswa m ON m.kode_jurusan = j.kode
    GROUP  BY j.jenjang
    ORDER  BY jumlah DESC
""", ["jenjang", "jumlah"])

# [4] Peserta matakuliah per jurusan (untuk stacked bar)
df_stacked = get_df("""
    SELECT j.nama AS jurusan, mk.nama AS matakuliah, COUNT(*) AS peserta
    FROM   Mengikuti  mgt
    JOIN   Mahasiswa  mhs ON mgt.nim          = mhs.nim
    JOIN   Jurusan    j   ON mhs.kode_jurusan = j.kode
    JOIN   Mengajar   mg  ON mgt.id_mengajar  = mg.id_mengajar
    JOIN   Matakuliah mk  ON mg.kode_mk       = mk.kode_mk
    GROUP  BY j.nama, mk.nama
    ORDER  BY jurusan
""", ["jurusan", "matakuliah", "peserta"])

pivot_stacked = df_stacked.pivot_table(
    index="jurusan", columns="matakuliah",
    values="peserta", fill_value=0
)

# -------------------------------------------------------
# BUAT FIGURE — 2 x 2 SUBPLOT
# -------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("Dashboard Sistem Akademik — Visualisasi Data MySQL",
             fontsize=16, fontweight="bold", y=1.01)

sns.set_style("whitegrid")

# ───────────────────────────────────────────
# [1] BAR CHART — Mahasiswa per Jurusan
# ───────────────────────────────────────────
ax1 = axes[0, 0]
bars = ax1.bar(df_per_jurusan["jurusan"], df_per_jurusan["jumlah"],
               color=WARNA_SET[:len(df_per_jurusan)], edgecolor="white", width=0.6)

for bar in bars:
    h = bar.get_height()
    if h > 0:
        ax1.text(bar.get_x() + bar.get_width() / 2, h + 0.05,
                 str(int(h)), ha="center", va="bottom",
                 fontsize=11, fontweight="bold")

ax1.set_title("Jumlah Mahasiswa per Jurusan", fontsize=12, fontweight="bold")
ax1.set_xlabel("Jurusan", fontsize=10)
ax1.set_ylabel("Jumlah Mahasiswa", fontsize=10)
ax1.set_ylim(0, df_per_jurusan["jumlah"].max() + 1.5)
ax1.tick_params(axis="x", rotation=15, labelsize=9)
ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# ───────────────────────────────────────────
# [2] HORIZONTAL BAR — Total SKS per Mahasiswa
# ───────────────────────────────────────────
ax2 = axes[0, 1]
colors_sks = [WARNA_SET[i % len(WARNA_SET)] for i in range(len(df_sks))]
hbars = ax2.barh(df_sks["nama"], df_sks["total_sks"],
                 color=colors_sks, edgecolor="white", height=0.6)

for hbar in hbars:
    w = hbar.get_width()
    ax2.text(w + 0.05, hbar.get_y() + hbar.get_height() / 2,
             str(int(w)), va="center", fontsize=10, fontweight="bold")

ax2.set_title("Total SKS per Mahasiswa (2024)", fontsize=12, fontweight="bold")
ax2.set_xlabel("Total SKS", fontsize=10)
ax2.set_ylabel("Mahasiswa", fontsize=10)
ax2.set_xlim(0, df_sks["total_sks"].max() + 2)
ax2.invert_yaxis()   # mahasiswa dengan SKS terbanyak di atas

# ───────────────────────────────────────────
# [3] PIE CHART — Proporsi Mahasiswa per Jenjang
# ───────────────────────────────────────────
ax3 = axes[1, 0]

# Filter hanya jenjang yang punya mahasiswa
df_jenjang_ada = df_jenjang[df_jenjang["jumlah"] > 0]

wedges, texts, autotexts = ax3.pie(
    df_jenjang_ada["jumlah"],
    labels    = df_jenjang_ada["jenjang"],
    autopct   = "%1.1f%%",
    startangle= 90,
    colors    = WARNA_SET[:len(df_jenjang_ada)],
    wedgeprops= {"edgecolor": "white", "linewidth": 1.5}
)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_fontweight("bold")

ax3.set_title("Proporsi Mahasiswa per Jenjang", fontsize=12, fontweight="bold")

# ───────────────────────────────────────────
# [4] STACKED BAR — Peserta Matakuliah per Jurusan
# ───────────────────────────────────────────
ax4 = axes[1, 1]
pivot_stacked.plot(
    kind      = "bar",
    stacked   = True,
    ax        = ax4,
    colormap  = "tab10",
    edgecolor = "white",
    width     = 0.6
)

ax4.set_title("Peserta Matakuliah per Jurusan", fontsize=12, fontweight="bold")
ax4.set_xlabel("Jurusan", fontsize=10)
ax4.set_ylabel("Jumlah Peserta", fontsize=10)
ax4.tick_params(axis="x", rotation=15, labelsize=9)
ax4.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax4.legend(title="Matakuliah", fontsize=7, title_fontsize=8,
           bbox_to_anchor=(1.01, 1), loc="upper left")

# -------------------------------------------------------
# FINALISASI
# -------------------------------------------------------
plt.tight_layout()

# Simpan ke file PNG
output_file = demik.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
print(f"✓ Dashboard berhasil disimpan ke: {output_file}")

plt.show()
