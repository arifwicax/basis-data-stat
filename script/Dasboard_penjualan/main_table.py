
# Import library
import streamlit as st
import pandas as pd
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Import fungsi dari config.py
from config import *

# Set konfigurasi halaman dashboard
st.set_page_config("Dashboard", page_icon="📊", layout="wide")  # Judul, ikon, tata letak lebar

# Ambil data pelanggan
result_customers = view_customers()

# Buat DataFrame pelanggan
df_customers = pd.DataFrame(result_customers, columns=[
    "customer_id", "name", "email", "phone", "address", "birthdate"
])

# Hitung usia dari birthdate
df_customers['birthdate'] = pd.to_datetime(df_customers['birthdate'])
df_customers['Age'] = (datetime.now() - df_customers['birthdate']).dt.days // 365

# Ambil data produk
result_products = view_products()

# Buat DataFrame produk
df_products = pd.DataFrame(result_products, columns=[
    "product_id", "name", "description", "price", "stock"
])

# Ambil data orders
result_orders = view_orders_with_customers()

# Buat DataFrame orders
df_orders = pd.DataFrame(result_orders, columns=[
    "order_id", "order_date", "total_amount", "customer_name", "phone"
])

# Ambil data order details
result_order_details = view_order_details_with_info()

# Buat DataFrame
df_order_details = pd.DataFrame(result_order_details, columns=[
    "order_detail_id", 
    "order_id", 
    "order_date", 
    "customer_id",
    "customer_name", 
    "product_id", 
    "product_name", 
    "price",
    "quantity", 
    "subtotal", 
    "total_amount", 
    "phone"
])


# Fungsi tampilkan tabel + export CSV
def tabelCustomers_dan_export():
    # Hitung jumlah pelanggan
    total_customers = df_customers.shape[0]

    # Tampilkan metrik
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="📦 Total Pelanggan", value=total_customers, delta="Semua Data")

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
    st.markdown("### 📋 Tabel Data Pelanggan")
    
    showdata = st.multiselect(
        "Pilih Kolom Pelanggan yang Ditampilkan",
        options=filtered_df.columns,
        default=["customer_id", "name", "email", "phone", "address", "birthdate"]
    )
    
    st.dataframe(filtered_df[showdata], use_container_width=True)

    @st.cache_data
    def convert_df_to_csv(_df):
        return _df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df_to_csv(filtered_df[showdata])
    st.download_button(
        label="⬇️ Download Data Pelanggan sebagai CSV",
        data=csv,
        file_name='data_pelanggan.csv',
        mime='text/csv'
    )

def tabelProducts_dan_export():
    # Tampilkan judul tabel produk
    st.markdown("### 🛒 Tabel Data Produk")
    
    # Sidebar: Filter berdasarkan rentang harga
    st.sidebar.header("FilterWhere Harga")
    min_price = int(df_products['price'].min())
    max_price = int(df_products['price'].max())
    price_range = st.sidebar.slider(
        "Pilih Rentang Harga",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )

    # Sidebar: Filter berdasarkan rentang stock
    st.sidebar.header("FilterWhere Stock")
    min_stock = int(df_products['stock'].min())
    max_stock = int(df_products['stock'].max())
    stock_range = st.sidebar.slider(
        "Pilih Rentang Stock",
        min_value=min_stock,
        max_value=max_stock,
        value=(min_stock, max_stock)
    )

    # Terapkan filter ke DataFrame
    filtered_df = df_products[
        df_products['price'].between(*price_range) &
        df_products['stock'].between(*stock_range)
    ]

# Hitung jumlah total stock (semua produk)
    total_stock = df_products['stock'].sum()

    # Hitung jumlah stock setelah filter
    filtered_stock = filtered_df['stock'].sum()

    # Hitung jumlah produk
    total_products = df_products.shape[0]
    filtered_product_count = filtered_df.shape[0]

    # Tampilkan metrik
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Produk", value=total_products, delta="Semua Kategori")

    with col2:
        st.metric(label="📦 Total Stock Semua Produk", value=filtered_stock, delta=f"Filter: {min_stock}-{max_stock}")

    # Widget multiselect untuk pilih kolom yang ditampilkan
    showdata = st.multiselect(
        "Pilih Kolom Produk yang Ditampilkan",
        options=filtered_df.columns,
        default=["product_id", "name", "description", "price", "stock"]
    )
    
    # Tampilkan tabel interaktif
    st.dataframe(filtered_df[showdata], use_container_width=True)

    # Tombol download CSV
    @st.cache_data
    def convert_df_to_csv(_df):
        return _df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df[showdata])
    st.download_button(
        label="⬇️ Download Data Produk sebagai CSV",
        data=csv,
        file_name='data_produk.csv',
        mime='text/csv'
    )

def tabelOrders_dan_export():
    st.markdown("### 🛒 Tabel Pesanan dengan Informasi Pelanggan")

    # Pastikan order_date bertipe datetime agar bisa difilter
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

    # Ambil tanggal minimal dan maksimal dari order_date
    min_date = df_orders['order_date'].min().date()
    max_date = df_orders['order_date'].max().date()

    # Sidebar: Filter berdasarkan rentang tanggal
    st.sidebar.header("FilterWhere Tanggal Pesanan")
    selected_dates = st.sidebar.date_input(
        "Pilih Rentang Tanggal",
        value=(min_date, max_date),  # Harus tuple agar selalu ada 2 tanggal
        min_value=min_date,
        max_value=max_date
    )

    # Pastikan selalu ada 2 nilai (start_date dan end_date)
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date = end_date = selected_dates[0]

    # Konversi ke Timestamp untuk filter
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date) + pd.Timedelta(days=1)  # Include end_date penuh

    # Terapkan filter tanggal
    filtered_df = df_orders[
        (df_orders['order_date'] >= start_date) &
        (df_orders['order_date'] <= end_date)
    ]

    # Hitung jumlah pesanan
    total_orders = df_orders.shape[0]
    filtered_order_count = filtered_df.shape[0]

    # Tampilkan metrik
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Semua Pesanan", value=total_orders)
    with col2:
        st.metric(label="⏱️ Jumlah Dalam Periode", value=filtered_order_count)

    showdata = st.multiselect(
        "Pilih Kolom yang Ditampilkan",
        options=filtered_df.columns,
        default=["order_id", "order_date", "total_amount", "customer_name", "phone"]
    )

    # Tampilkan DataFrame hasil filter
    st.dataframe(filtered_df[showdata], use_container_width=True)

    @st.cache_data
    def convert_df_to_csv(_df):
        return _df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df[showdata])
    st.download_button(
        label="⬇️ Download Data Pesanan sebagai CSV",
        data=csv,
        file_name='data_pesanan.csv',
        mime='text/csv'
    )

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def tabelOrderDetails_dan_export():
    st.markdown("### 📄 Tabel Detail Pesanan dengan Informasi Lengkap")

    # Ambil data dari database dan buat DataFrame
    result = view_order_details_with_info()
    df_order_details = pd.DataFrame(result, columns=[
        "order_detail_id", 
        "order_id", 
        "order_date", 
        "customer_id",
        "customer_name", 
        "product_id", 
        "product_nama", 
        "price",
        "quantity", 
        "subtotal", 
        "total_amount", 
        "phone"
    ])

    # Konversi kolom order_date ke datetime
    df_order_details['order_date'] = pd.to_datetime(df_order_details['order_date'])

    # Fungsi untuk menampilkan metrik statistik
    def metrics():
        col1, col2, col3 = st.columns(3)  # Membagi layar jadi 3 kolom

        # Hitung total jumlah transaksi (order_id unik)
        total_transaksi = df_order_details['order_id'].nunique()

        # Hitung total amount dari semua pesanan
        total_amount = df_order_details['total_amount'].sum()

        # Hitung total quantity produk yang terjual
        total_quantity = df_order_details['quantity'].sum()

        # Tampilkan metrik
        col1.metric("Total Transaksi", value=total_transaksi, delta="Semua Pesanan")
        col2.metric("Total Penjualan (IDR)", value=f"{total_amount:,.0f}", delta="Total Amount")
        col3.metric("Total Produk Terjual", value=total_quantity, delta="Quantity")

    # Jalankan fungsi metrics (dipindahkan ke atas tabel)
    metrics()

    # Visualisasi 1: Penjualan Berdasarkan Waktu
    st.markdown("### 📈 Visualisasi Penjualan Berdasarkan Waktu")
    df_time_series = df_order_details.groupby(df_order_details['order_date'].dt.date).agg(
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

    # Visualisasi 2: Produk Terlaris
    st.markdown("### 🏆 Produk Terlaris")
    df_product_sales = df_order_details.groupby('product_nama').agg(
        total_quantity=('quantity', 'sum')
    ).reset_index().sort_values(by='total_quantity', ascending=False)

    # Bar Chart
    fig_product_bar = px.bar(
        df_product_sales.head(10),  # Top 10 produk
        x='product_nama',
        y='total_quantity',
        title="Top 10 Produk Terlaris (Berdasarkan Kuantitas)",
        labels={'total_quantity': 'Total Kuantitas Terjual', 'product_nama': 'Nama Produk'}
    )
    st.plotly_chart(fig_product_bar, use_container_width=True)

    # Pie Chart
    fig_product_pie = px.pie(
        df_product_sales.head(10),  # Top 10 produk
        names='product_nama',
        values='total_quantity',
        title="Kontribusi Produk Terhadap Total Penjualan (Top 10)"
    )
    st.plotly_chart(fig_product_pie, use_container_width=True)

    # Visualisasi 3: Kontribusi Produk terhadap Total Penjualan
    st.markdown("### 💰 Kontribusi Produk terhadap Total Penjualan")
    df_product_revenue = df_order_details.groupby('product_nama').agg(
        total_revenue=('subtotal', 'sum')
    ).reset_index().sort_values(by='total_revenue', ascending=False)

    # Bar Chart
    fig_revenue_bar = px.bar(
        df_product_revenue.head(10),  # Top 10 produk
        x='product_nama',
        y='total_revenue',
        title="Top 10 Produk dengan Pendapatan Tertinggi",
        labels={'total_revenue': 'Total Pendapatan (IDR)', 'product_nama': 'Nama Produk'}
    )
    st.plotly_chart(fig_revenue_bar, use_container_width=True)

    # Treemap
    fig_treemap = px.treemap(
        df_product_revenue,
        path=['product_nama'],
        values='total_revenue',
        title="Proporsi Kontribusi Produk terhadap Total Pendapatan"
    )
    st.plotly_chart(fig_treemap, use_container_width=True)

    # Pilihan kolom untuk ditampilkan
    showdata = st.multiselect(
        "Pilih Kolom yang Ditampilkan",
        options=df_order_details.columns,
        default=["order_detail_id", "order_id", "order_date", "customer_id", "customer_name", "product_id", "product_nama", "price", "quantity", "subtotal", "total_amount", "phone"]
    )

    # Tampilkan tabel interaktif
    st.dataframe(df_order_details[showdata], use_container_width=True)

    # Fungsi bantu export ke CSV
    @st.cache_data
    def convert_df_to_csv(_df):
        return _df.to_csv(index=False).encode('utf-8')

    # Tombol download CSV
    csv = convert_df_to_csv(df_order_details[showdata])
    st.download_button(
        label="⬇️ Download Data Detail Pesanan sebagai CSV",
        data=csv,
        file_name='detail_pesanan.csv',
        mime='text/csv'
    )

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