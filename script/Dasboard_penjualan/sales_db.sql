-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 02, 2025 at 02:40 AM
-- Server version: 8.0.35
-- PHP Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sales_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `address` text,
  `birthdate` date DEFAULT NULL COMMENT 'Tanggal lahir pelanggan'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `email`, `phone`, `address`, `birthdate`) VALUES
(1, 'Andi Wijaya', 'andi.wijaya@example.com', '08123456781', 'Jl. Sudirman No. 1, Jakarta', '1990-05-15'),
(2, 'Budi Santoso', 'budi.santoso@example.com', '08123456782', 'Jl. Gatot Subroto No. 5, Bandung', '1985-08-20'),
(3, 'Citra Kusuma', 'citra.kusuma@example.com', '08123456783', 'Jl. Diponegoro No. 10, Surabaya', '1992-03-10'),
(4, 'Dewi Lestari', 'dewi.lestari@example.com', '08123456784', 'Jl. Imam Bonjol No. 15, Medan', '1988-11-25'),
(5, 'Eko Prasetyo', 'eko.prasetyo@example.com', '08123456785', 'Jl. Ahmad Yani No. 20, Semarang', '1995-07-05'),
(6, 'Fajar Nugraha', 'fajar.nugraha@example.com', '08123456786', 'Jl. Pahlawan No. 25, Makassar', '1980-12-10'),
(7, 'Gita Permata', 'gita.permata@example.com', '08123456787', 'Jl. Veteran No. 30, Palembang', '1993-04-22'),
(8, 'Hendra Setiawan', 'hendra.setiawan@example.com', '08123456788', 'Jl. Merdeka No. 35, Denpasar', '1987-09-15'),
(9, 'Indah Kartika', 'indah.kartika@example.com', '08123456789', 'Jl. Hayam Wuruk No. 40, Yogyakarta', '1994-06-30'),
(10, 'Joko Susanto', 'joko.susanto@example.com', '08123456790', 'Jl. Raya Bogor No. 45, Bogor', '1982-02-05'),
(11, 'Kiki Amelia', 'kiki.amelia@example.com', '08123456791', 'Jl. Cik Ditiro No. 50, Malang', '1991-11-12'),
(12, 'Lina Sari', 'lina.sari@example.com', '08123456792', 'Jl. Asia Afrika No. 55, Bandung', '1986-07-20'),
(13, 'Mira Anggraeni', 'mira.anggraeni@example.com', '08123456793', 'Jl. Pasar Baru No. 60, Jakarta', '1996-01-18'),
(14, 'Nanda Pratama', 'nanda.pratama@example.com', '08123456794', 'Jl. Cempaka Putih No. 65, Tangerang', '1989-03-25'),
(15, 'Oscar Hidayat', 'oscar.hidayat@example.com', '08123456795', 'Jl. Teuku Umar No. 70, Balikpapan', '1984-10-10'),
(16, 'Putri Anindya', 'putri.anindya@example.com', '08123456796', 'Jl. Gajah Mada No. 75, Pontianak', '1997-05-05'),
(17, 'Rafi Ramadhan', 'rafi.ramadhan@example.com', '08123456797', 'Jl. Cut Nyak Dien No. 80, Banda Aceh', '1983-08-20'),
(18, 'Sari Wulandari', 'sari.wulandari@example.com', '08123456798', 'Jl. Jenderal Sudirman No. 85, Padang', '1990-09-15'),
(19, 'Taufik Hidayat', 'taufik.hidayat@example.com', '08123456799', 'Jl. Pemuda No. 90, Solo', '1981-12-01'),
(20, 'Umi Kulsum', 'umi.kulsum@example.com', '08123456800', 'Jl. Thamrin No. 95, Batam', '1995-04-10'),
(21, 'Vina Safitri', 'vina.safitri@example.com', '08123456801', 'Jl. Pattimura No. 100, Manado', '1988-02-20'),
(22, 'Wawan Setiawan', 'wawan.setiawan@example.com', '08123456802', 'Jl. Sisingamangaraja No. 105, Pekanbaru', '1992-07-25'),
(23, 'Xavier Prasetya', 'xavier.prasetya@example.com', '08123456803', 'Jl. Raya Cibubur No. 110, Depok', '1986-03-15'),
(24, 'Yanti Wulansari', 'yanti.wulansari@example.com', '08123456804', 'Jl. Cempaka Wangi No. 115, Bekasi', '1994-11-30'),
(25, 'Zaki Rahman', 'zaki.rahman@example.com', '08123456805', 'Jl. Raya Bogor No. 120, Cibinong', '1987-06-20'),
(26, 'Adi Nugroho', 'adi.nugroho@example.com', '08123456806', 'Jl. Raya Serpong No. 125, Tangerang Selatan', '1993-08-05'),
(27, 'Bella Ayu', 'bella.ayu@example.com', '08123456807', 'Jl. Raya Kebayoran Lama No. 130, Jakarta Selatan', '1989-04-10'),
(28, 'Ciko Pratama', 'ciko.pratama@example.com', '08123456808', 'Jl. Raya Pondok Indah No. 135, Jakarta Selatan', '1991-02-25'),
(29, 'Dina Rahmawati', 'dina.rahmawati@example.com', '08123456809', 'Jl. Raya Fatmawati No. 140, Jakarta Selatan', '1985-09-15'),
(30, 'Evan Setiawan', 'evan.setiawan@example.com', '08123456810', 'Jl. Raya Lenteng Agung No. 145, Jakarta Selatan', '1990-05-20'),
(31, 'Fitri Wulandari', 'fitri.wulandari@example.com', '08123456811', 'Jl. Raya Jagakarsa No. 150, Jakarta Selatan', '1982-11-10'),
(32, 'Galih Pratama', 'galih.pratama@example.com', '08123456812', 'Jl. Raya Cilandak No. 155, Jakarta Selatan', '1996-03-25'),
(33, 'Hana Safitri', 'hana.safitri@example.com', '08123456813', 'Jl. Raya Lebak Bulus No. 160, Jakarta Selatan', '1984-07-05'),
(34, 'Irfan Hidayat', 'irfan.hidayat@example.com', '08123456814', 'Jl. Raya Pondok Labu No. 165, Jakarta Selatan', '1992-06-15'),
(35, 'Jihan Wulansari', 'jihan.wulansari@example.com', '08123456815', 'Jl. Raya Kemang No. 170, Jakarta Selatan', '1988-02-20'),
(36, 'Kevin Pratama', 'kevin.pratama@example.com', '08123456816', 'Jl. Raya Bangka No. 175, Jakarta Selatan', '1994-10-10'),
(37, 'Laras Ayu', 'laras.ayu@example.com', '08123456817', 'Jl. Raya Melawai No. 180, Jakarta Selatan', '1987-04-25'),
(38, 'Mia Rahmawati', 'mia.rahmawati@example.com', '08123456818', 'Jl. Raya Blok M No. 185, Jakarta Selatan', '1990-01-15'),
(39, 'Nisa Setiawan', 'nisa.setiawan@example.com', '08123456819', 'Jl. Raya Senayan No. 190, Jakarta Selatan', '1983-09-10'),
(40, 'Ovi Wulandari', 'ovi.wulandari@example.com', '08123456820', 'Jl. Raya Palmerah No. 195, Jakarta Selatan', '1995-06-20'),
(41, 'Pasha Safitri', 'pasha.safitri@example.com', '08123456821', 'Jl. Raya Slipi No. 200, Jakarta Selatan', '1989-03-05'),
(42, 'Qori Hidayat', 'qori.hidayat@example.com', '08123456822', 'Jl. Raya Tomang No. 205, Jakarta Selatan', '1991-11-25'),
(43, 'Rara Wulansari', 'rara.wulansari@example.com', '08123456823', 'Jl. Raya Grogol No. 210, Jakarta Selatan', '1986-05-10'),
(44, 'Saka Pratama', 'saka.pratama@example.com', '08123456824', 'Jl. Raya Roxy No. 215, Jakarta Selatan', '1993-02-20'),
(45, 'Tasya Ayu', 'tasya.ayu@example.com', '08123456825', 'Jl. Raya Mangga Besar No. 220, Jakarta Selatan', '1988-08-15'),
(46, 'Ulya Rahmawati', 'ulya.rahmawati@example.com', '08123456826', 'Jl. Raya Glodok No. 225, Jakarta Selatan', '1994-04-05'),
(47, 'Vera Setiawan', 'vera.setiawan@example.com', '08123456827', 'Jl. Raya Tambora No. 230, Jakarta Selatan', '1985-12-20'),
(48, 'Widi Wulandari', 'widi.wulandari@example.com', '08123456828', 'Jl. Raya Kebon Jeruk No. 235, Jakarta Selatan', '1992-07-10'),
(49, 'Xena Safitri', 'xena.safitri@example.com', '08123456829', 'Jl. Raya Tanjung Duren No. 240, Jakarta Selatan', '1987-01-25'),
(50, 'Yoga Hidayat', 'yoga.hidayat@example.com', '08123456830', 'Jl. Raya Kedoya No. 245, Jakarta Selatan', '1990-03-15'),
(51, 'Zara Wulansari', 'zara.wulansari@example.com', '08123456831', 'Jl. Raya Kapuk No. 250, Jakarta Selatan', '1984-10-30');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `order_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `total_amount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `customer_id`, `order_date`, `total_amount`) VALUES
(1, 1, '2023-07-01 10:00:00', 250000.00),
(2, 2, '2023-07-02 14:30:00', 450000.00),
(3, 3, '2023-07-03 09:45:00', 150000.00),
(4, 4, '2023-07-04 16:00:00', 75000.00),
(5, 5, '2023-07-05 12:15:00', 300000.00),
(6, 6, '2023-07-06 18:30:00', 500000.00),
(7, 7, '2023-07-07 11:45:00', 120000.00),
(8, 8, '2023-07-08 19:00:00', 60000.00),
(9, 9, '2023-07-09 20:15:00', 400000.00),
(10, 10, '2023-07-10 08:30:00', 80000.00),
(11, 11, '2023-07-11 10:00:00', 250000.00),
(12, 12, '2023-07-12 15:30:00', 450000.00),
(13, 13, '2023-07-13 17:45:00', 150000.00),
(14, 14, '2023-07-14 12:00:00', 75000.00),
(15, 15, '2023-07-15 13:15:00', 300000.00),
(16, 16, '2023-07-16 14:30:00', 500000.00),
(17, 17, '2023-07-17 09:45:00', 120000.00),
(18, 18, '2023-07-18 17:00:00', 60000.00),
(19, 19, '2023-07-19 18:15:00', 400000.00),
(20, 20, '2023-07-20 21:30:00', 80000.00),
(21, 21, '2023-07-21 08:00:00', 250000.00),
(22, 22, '2023-07-22 09:30:00', 450000.00),
(23, 23, '2023-07-23 10:45:00', 150000.00),
(24, 24, '2023-07-24 12:00:00', 75000.00),
(25, 25, '2023-07-25 13:15:00', 300000.00),
(26, 26, '2023-07-26 14:30:00', 500000.00),
(27, 27, '2023-07-27 15:45:00', 120000.00),
(28, 28, '2023-07-28 17:00:00', 60000.00),
(29, 29, '2023-07-29 18:15:00', 400000.00),
(30, 30, '2023-07-30 19:30:00', 80000.00);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `order_detail_id` int NOT NULL,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) GENERATED ALWAYS AS ((`quantity` * `price`)) STORED
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`order_detail_id`, `order_id`, `product_id`, `quantity`, `price`) VALUES
(1, 1, 1, 1, 250000.00),
(2, 2, 3, 2, 75000.00),
(3, 2, 5, 1, 400000.00),
(4, 3, 7, 1, 1000000.00),
(5, 4, 9, 1, 60000.00),
(6, 5, 11, 2, 80000.00),
(7, 6, 13, 1, 500000.00),
(8, 7, 15, 3, 35000.00),
(9, 8, 17, 1, 350000.00),
(10, 9, 19, 2, 40000.00),
(11, 10, 2, 1, 1500000.00),
(12, 11, 4, 1, 300000.00),
(13, 12, 6, 2, 50000.00),
(14, 13, 8, 4, 25000.00),
(15, 14, 10, 1, 150000.00),
(16, 15, 12, 1, 600000.00),
(17, 16, 14, 5, 15000.00),
(18, 17, 16, 1, 200000.00),
(19, 18, 18, 2, 45000.00),
(20, 19, 1, 2, 250000.00),
(21, 20, 3, 1, 75000.00),
(22, 21, 5, 1, 400000.00),
(23, 22, 7, 1, 1000000.00),
(24, 23, 9, 2, 60000.00),
(25, 24, 11, 1, 80000.00),
(26, 25, 13, 1, 500000.00),
(27, 26, 15, 2, 35000.00),
(28, 27, 17, 1, 350000.00),
(29, 28, 19, 1, 40000.00),
(30, 29, 2, 1, 1500000.00),
(31, 30, 4, 1, 300000.00);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text,
  `price` decimal(10,2) NOT NULL,
  `stock` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `description`, `price`, `stock`) VALUES
(1, 'Batik Tulis Solo', 'Kain batik tulis asli dari Solo dengan motif khas Jawa Tengah.', 250000.00, 50),
(2, 'Keris Pusaka', 'Keris tradisional dengan ukiran khas Jawa, cocok untuk koleksi.', 1500000.00, 10),
(3, 'Rendang Padang', 'Makanan khas Minangkabau berbahan dasar daging sapi.', 75000.00, 100),
(4, 'Wayang Kulit', 'Wayang kulit khas Jawa dengan detail ukiran halus.', 300000.00, 20),
(5, 'Songket Palembang', 'Kain songket mewah dari Palembang dengan benang emas.', 400000.00, 30),
(6, 'Pempek Palembang', 'Makanan khas Palembang terbuat dari ikan tenggiri.', 50000.00, 200),
(7, 'Kopi Luwak', 'Kopi premium dari biji kopi yang difermentasi oleh luwak.', 1000000.00, 5),
(8, 'Sambal Terasi', 'Sambal khas Indonesia dengan cita rasa pedas dan gurih.', 25000.00, 500),
(9, 'Gudeg Jogja', 'Makanan khas Yogyakarta terbuat dari nangka muda.', 60000.00, 150),
(10, 'Kerajinan Gerabah', 'Gerabah khas Kasongan Yogyakarta dengan desain unik.', 150000.00, 40),
(11, 'Kue Lapis Legit', 'Kue lapis legit khas Indonesia dengan tekstur lembut.', 80000.00, 80),
(12, 'Baju Adat Batak', 'Pakaian adat tradisional dari suku Batak Sumatera Utara.', 600000.00, 15),
(13, 'Ulos Batak', 'Kain ulos khas Batak dengan makna budaya mendalam.', 500000.00, 25),
(14, 'Kerupuk Udang', 'Kerupuk udang renyah khas Indonesia.', 15000.00, 300),
(15, 'Teh Poci', 'Teh khas Indonesia disajikan dengan gayung poci.', 35000.00, 250),
(16, 'Kerajinan Rotan', 'Kerajinan rotan handmade dari Kalimantan.', 200000.00, 60),
(17, 'Ikat Sumba', 'Kain tenun ikat tradisional dari Pulau Sumba.', 350000.00, 35),
(18, 'Siomay Bandung', 'Makanan khas Bandung dengan bahan dasar ikan tenggiri.', 45000.00, 120),
(19, 'Kerajinan Ukir Kayu', 'Ukir kayu khas Jepara dengan detail rumit.', 500000.00, 10),
(20, 'Nasi Liwet Solo', 'Nasi liwet khas Solo dengan cita rasa gurih.', 40000.00, 180);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`order_detail_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `order_detail_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE;

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
