
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT,
    birthdate DATE COMMENT 'Tanggal lahir pelanggan'
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) AS (quantity * price) STORED,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON DELETE CASCADE
);

INSERT INTO customers (name, email, phone, address, birthdate) VALUES
('Andi Wijaya', 'andi.wijaya@example.com', '08123456781', 'Jl. Sudirman No. 1, Jakarta', '1990-05-15'),
('Budi Santoso', 'budi.santoso@example.com', '08123456782', 'Jl. Gatot Subroto No. 5, Bandung', '1985-08-20'),
('Citra Kusuma', 'citra.kusuma@example.com', '08123456783', 'Jl. Diponegoro No. 10, Surabaya', '1992-03-10'),
('Dewi Lestari', 'dewi.lestari@example.com', '08123456784', 'Jl. Imam Bonjol No. 15, Medan', '1988-11-25'),
('Eko Prasetyo', 'eko.prasetyo@example.com', '08123456785', 'Jl. Ahmad Yani No. 20, Semarang', '1995-07-05'),
('Fajar Nugraha', 'fajar.nugraha@example.com', '08123456786', 'Jl. Pahlawan No. 25, Makassar', '1980-12-10'),
('Gita Permata', 'gita.permata@example.com', '08123456787', 'Jl. Veteran No. 30, Palembang', '1993-04-22'),
('Hendra Setiawan', 'hendra.setiawan@example.com', '08123456788', 'Jl. Merdeka No. 35, Denpasar', '1987-09-15'),
('Indah Kartika', 'indah.kartika@example.com', '08123456789', 'Jl. Hayam Wuruk No. 40, Yogyakarta', '1994-06-30'),
('Joko Susanto', 'joko.susanto@example.com', '08123456790', 'Jl. Raya Bogor No. 45, Bogor', '1982-02-05'),
('Kiki Amelia', 'kiki.amelia@example.com', '08123456791', 'Jl. Cik Ditiro No. 50, Malang', '1991-11-12'),
('Lina Sari', 'lina.sari@example.com', '08123456792', 'Jl. Asia Afrika No. 55, Bandung', '1986-07-20'),
('Mira Anggraeni', 'mira.anggraeni@example.com', '08123456793', 'Jl. Pasar Baru No. 60, Jakarta', '1996-01-18'),
('Nanda Pratama', 'nanda.pratama@example.com', '08123456794', 'Jl. Cempaka Putih No. 65, Tangerang', '1989-03-25'),
('Oscar Hidayat', 'oscar.hidayat@example.com', '08123456795', 'Jl. Teuku Umar No. 70, Balikpapan', '1984-10-10'),
('Putri Anindya', 'putri.anindya@example.com', '08123456796', 'Jl. Gajah Mada No. 75, Pontianak', '1997-05-05'),
('Rafi Ramadhan', 'rafi.ramadhan@example.com', '08123456797', 'Jl. Cut Nyak Dien No. 80, Banda Aceh', '1983-08-20'),
('Sari Wulandari', 'sari.wulandari@example.com', '08123456798', 'Jl. Jenderal Sudirman No. 85, Padang', '1990-09-15'),
('Taufik Hidayat', 'taufik.hidayat@example.com', '08123456799', 'Jl. Pemuda No. 90, Solo', '1981-12-01'),
('Umi Kulsum', 'umi.kulsum@example.com', '08123456800', 'Jl. Thamrin No. 95, Batam', '1995-04-10'),
('Vina Safitri', 'vina.safitri@example.com', '08123456801', 'Jl. Pattimura No. 100, Manado', '1988-02-20'),
('Wawan Setiawan', 'wawan.setiawan@example.com', '08123456802', 'Jl. Sisingamangaraja No. 105, Pekanbaru', '1992-07-25'),
('Xavier Prasetya', 'xavier.prasetya@example.com', '08123456803', 'Jl. Raya Cibubur No. 110, Depok', '1986-03-15'),
('Yanti Wulansari', 'yanti.wulansari@example.com', '08123456804', 'Jl. Cempaka Wangi No. 115, Bekasi', '1994-11-30'),
('Zaki Rahman', 'zaki.rahman@example.com', '08123456805', 'Jl. Raya Bogor No. 120, Cibinong', '1987-06-20'),
('Adi Nugroho', 'adi.nugroho@example.com', '08123456806', 'Jl. Raya Serpong No. 125, Tangerang Selatan', '1993-08-05'),
('Bella Ayu', 'bella.ayu@example.com', '08123456807', 'Jl. Raya Kebayoran Lama No. 130, Jakarta Selatan', '1989-04-10'),
('Ciko Pratama', 'ciko.pratama@example.com', '08123456808', 'Jl. Raya Pondok Indah No. 135, Jakarta Selatan', '1991-02-25'),
('Dina Rahmawati', 'dina.rahmawati@example.com', '08123456809', 'Jl. Raya Fatmawati No. 140, Jakarta Selatan', '1985-09-15'),
('Evan Setiawan', 'evan.setiawan@example.com', '08123456810', 'Jl. Raya Lenteng Agung No. 145, Jakarta Selatan', '1990-05-20'),
('Fitri Wulandari', 'fitri.wulandari@example.com', '08123456811', 'Jl. Raya Jagakarsa No. 150, Jakarta Selatan', '1982-11-10'),
('Galih Pratama', 'galih.pratama@example.com', '08123456812', 'Jl. Raya Cilandak No. 155, Jakarta Selatan', '1996-03-25'),
('Hana Safitri', 'hana.safitri@example.com', '08123456813', 'Jl. Raya Lebak Bulus No. 160, Jakarta Selatan', '1984-07-05'),
('Irfan Hidayat', 'irfan.hidayat@example.com', '08123456814', 'Jl. Raya Pondok Labu No. 165, Jakarta Selatan', '1992-06-15'),
('Jihan Wulansari', 'jihan.wulansari@example.com', '08123456815', 'Jl. Raya Kemang No. 170, Jakarta Selatan', '1988-02-20'),
('Kevin Pratama', 'kevin.pratama@example.com', '08123456816', 'Jl. Raya Bangka No. 175, Jakarta Selatan', '1994-10-10'),
('Laras Ayu', 'laras.ayu@example.com', '08123456817', 'Jl. Raya Melawai No. 180, Jakarta Selatan', '1987-04-25'),
('Mia Rahmawati', 'mia.rahmawati@example.com', '08123456818', 'Jl. Raya Blok M No. 185, Jakarta Selatan', '1990-01-15'),
('Nisa Setiawan', 'nisa.setiawan@example.com', '08123456819', 'Jl. Raya Senayan No. 190, Jakarta Selatan', '1983-09-10'),
('Ovi Wulandari', 'ovi.wulandari@example.com', '08123456820', 'Jl. Raya Palmerah No. 195, Jakarta Selatan', '1995-06-20'),
('Pasha Safitri', 'pasha.safitri@example.com', '08123456821', 'Jl. Raya Slipi No. 200, Jakarta Selatan', '1989-03-05'),
('Qori Hidayat', 'qori.hidayat@example.com', '08123456822', 'Jl. Raya Tomang No. 205, Jakarta Selatan', '1991-11-25'),
('Rara Wulansari', 'rara.wulansari@example.com', '08123456823', 'Jl. Raya Grogol No. 210, Jakarta Selatan', '1986-05-10'),
('Saka Pratama', 'saka.pratama@example.com', '08123456824', 'Jl. Raya Roxy No. 215, Jakarta Selatan', '1993-02-20'),
('Tasya Ayu', 'tasya.ayu@example.com', '08123456825', 'Jl. Raya Mangga Besar No. 220, Jakarta Selatan', '1988-08-15'),
('Ulya Rahmawati', 'ulya.rahmawati@example.com', '08123456826', 'Jl. Raya Glodok No. 225, Jakarta Selatan', '1994-04-05'),
('Vera Setiawan', 'vera.setiawan@example.com', '08123456827', 'Jl. Raya Tambora No. 230, Jakarta Selatan', '1985-12-20'),
('Widi Wulandari', 'widi.wulandari@example.com', '08123456828', 'Jl. Raya Kebon Jeruk No. 235, Jakarta Selatan', '1992-07-10'),
('Xena Safitri', 'xena.safitri@example.com', '08123456829', 'Jl. Raya Tanjung Duren No. 240, Jakarta Selatan', '1987-01-25'),
('Yoga Hidayat', 'yoga.hidayat@example.com', '08123456830', 'Jl. Raya Kedoya No. 245, Jakarta Selatan', '1990-03-15'),
('Zara Wulansari', 'zara.wulansari@example.com', '08123456831', 'Jl. Raya Kapuk No. 250, Jakarta Selatan', '1984-10-30');

INSERT INTO products (name, description, price, stock) VALUES
('Batik Tulis Solo', 'Kain batik tulis asli dari Solo dengan motif khas Jawa Tengah.', 250000, 50),
('Keris Pusaka', 'Keris tradisional dengan ukiran khas Jawa, cocok untuk koleksi.', 1500000, 10),
('Rendang Padang', 'Makanan khas Minangkabau berbahan dasar daging sapi.', 75000, 100),
('Wayang Kulit', 'Wayang kulit khas Jawa dengan detail ukiran halus.', 300000, 20),
('Songket Palembang', 'Kain songket mewah dari Palembang dengan benang emas.', 400000, 30),
('Pempek Palembang', 'Makanan khas Palembang terbuat dari ikan tenggiri.', 50000, 200),
('Kopi Luwak', 'Kopi premium dari biji kopi yang difermentasi oleh luwak.', 1000000, 5),
('Sambal Terasi', 'Sambal khas Indonesia dengan cita rasa pedas dan gurih.', 25000, 500),
('Gudeg Jogja', 'Makanan khas Yogyakarta terbuat dari nangka muda.', 60000, 150),
('Kerajinan Gerabah', 'Gerabah khas Kasongan Yogyakarta dengan desain unik.', 150000, 40),
('Kue Lapis Legit', 'Kue lapis legit khas Indonesia dengan tekstur lembut.', 80000, 80),
('Baju Adat Batak', 'Pakaian adat tradisional dari suku Batak Sumatera Utara.', 600000, 15),
('Ulos Batak', 'Kain ulos khas Batak dengan makna budaya mendalam.', 500000, 25),
('Kerupuk Udang', 'Kerupuk udang renyah khas Indonesia.', 15000, 300),
('Teh Poci', 'Teh khas Indonesia disajikan dengan gayung poci.', 35000, 250),
('Kerajinan Rotan', 'Kerajinan rotan handmade dari Kalimantan.', 200000, 60),
('Ikat Sumba', 'Kain tenun ikat tradisional dari Pulau Sumba.', 350000, 35),
('Siomay Bandung', 'Makanan khas Bandung dengan bahan dasar ikan tenggiri.', 45000, 120),
('Kerajinan Ukir Kayu', 'Ukir kayu khas Jepara dengan detail rumit.', 500000, 10),
('Nasi Liwet Solo', 'Nasi liwet khas Solo dengan cita rasa gurih.', 40000, 180);

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-07-01 10:00:00', 250000),
(2, '2023-07-02 14:30:00', 450000),
(3, '2023-07-03 09:45:00', 150000),
(4, '2023-07-04 16:00:00', 75000),
(5, '2023-07-05 12:15:00', 300000),
(6, '2023-07-06 18:30:00', 500000),
(7, '2023-07-07 11:45:00', 120000),
(8, '2023-07-08 19:00:00', 60000),
(9, '2023-07-09 20:15:00', 400000),
(10, '2023-07-10 08:30:00', 80000),
(11, '2023-07-11 10:00:00', 250000),
(12, '2023-07-12 15:30:00', 450000),
(13, '2023-07-13 17:45:00', 150000),
(14, '2023-07-14 12:00:00', 75000),
(15, '2023-07-15 13:15:00', 300000),
(16, '2023-07-16 14:30:00', 500000),
(17, '2023-07-17 09:45:00', 120000),
(18, '2023-07-18 17:00:00', 60000),
(19, '2023-07-19 18:15:00', 400000),
(20, '2023-07-20 21:30:00', 80000),
(21, '2023-07-21 08:00:00', 250000),
(22, '2023-07-22 09:30:00', 450000),
(23, '2023-07-23 10:45:00', 150000),
(24, '2023-07-24 12:00:00', 75000),
(25, '2023-07-25 13:15:00', 300000),
(26, '2023-07-26 14:30:00', 500000),
(27, '2023-07-27 15:45:00', 120000),
(28, '2023-07-28 17:00:00', 60000),
(29, '2023-07-29 18:15:00', 400000),
(30, '2023-07-30 19:30:00', 80000);


INSERT INTO order_details (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 250000), -- Batik Tulis Solo @250000 x 1 = 250000
(2, 3, 2, 75000),  -- Rendang Padang @75000 x 2 = 150000
(2, 5, 1, 400000), -- Songket Palembang @400000 x 1 = 400000
(3, 7, 1, 1000000), -- Kopi Luwak @1000000 x 1 = 1000000
(4, 9, 1, 60000),  -- Gudeg Jogja @60000 x 1 = 60000
(5, 11, 2, 80000), -- Kue Lapis Legit @80000 x 2 = 160000
(6, 13, 1, 500000), -- Ulos Batak @500000 x 1 = 500000
(7, 15, 3, 35000), -- Teh Poci @35000 x 3 = 105000
(8, 17, 1, 350000), -- Ikat Sumba @350000 x 1 = 350000
(9, 19, 2, 40000), -- Nasi Liwet Solo @40000 x 2 = 80000
(10, 2, 1, 1500000), -- Keris Pusaka @1500000 x 1 = 1500000
(11, 4, 1, 300000), -- Wayang Kulit @300000 x 1 = 300000
(12, 6, 2, 50000),  -- Pempek Palembang @50000 x 2 = 100000
(13, 8, 4, 25000),  -- Sambal Terasi @25000 x 4 = 100000
(14, 10, 1, 150000), -- Kerajinan Gerabah @150000 x 1 = 150000
(15, 12, 1, 600000), -- Baju Adat Batak @600000 x 1 = 600000
(16, 14, 5, 15000), -- Kerupuk Udang @15000 x 5 = 75000
(17, 16, 1, 200000), -- Kerajinan Rotan @200000 x 1 = 200000
(18, 18, 2, 45000), -- Siomay Bandung @45000 x 2 = 90000
(19, 1, 2, 250000), -- Batik Tulis Solo @250000 x 2 = 500000
(20, 3, 1, 75000),  -- Rendang Padang @75000 x 1 = 75000
(21, 5, 1, 400000), -- Songket Palembang @400000 x 1 = 400000
(22, 7, 1, 1000000), -- Kopi Luwak @1000000 x 1 = 1000000
(23, 9, 2, 60000),  -- Gudeg Jogja @60000 x 2 = 120000
(24, 11, 1, 80000), -- Kue Lapis Legit @80000 x 1 = 80000
(25, 13, 1, 500000), -- Ulos Batak @500000 x 1 = 500000
(26, 15, 2, 35000), -- Teh Poci @35000 x 2 = 70000
(27, 17, 1, 350000), -- Ikat Sumba @350000 x 1 = 350000
(28, 19, 1, 40000), -- Nasi Liwet Solo @40000 x 1 = 40000
(29, 2, 1, 1500000), -- Keris Pusaka @1500000 x 1 = 1500000
(30, 4, 1, 300000); -- Wayang Kulit @300000 x 1 = 300000

SELECT * FROM customers ORDER BY name ASC

SELECT 
            o.order_id, 
            o.order_date, 
            o.total_amount, 
            c.name AS customer_name, 
            c.phone 
        FROM 
            orders o 
        JOIN 
            customers c ON o.customer_id = c.customer_id 
        ORDER BY 
            o.order_date DESC

SELECT 
            od.order_detail_id,
            o.order_id,
            o.order_date,
            c.customer_id,
            c.name AS customer_name,
            p.product_id,-
            p.name AS product_name,
            p.price AS unit_price,
            od.quantity,
            od.subtotal,
            o.total_amount AS order_total,
            c.phone
        FROM 
            order_details od
        JOIN 
            orders o ON od.order_id = o.order_id
        JOIN 
            customers c ON o.customer_id = c.customer_id
        JOIN 
            products p ON od.product_id = p.product_id
        ORDER BY 
            o.order_date DESC


SELECT * FROM `customers`





