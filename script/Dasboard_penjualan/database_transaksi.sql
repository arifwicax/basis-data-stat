-- Membuat tabel untuk produk
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Membuat tabel untuk transaksi
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_date DATE NOT NULL,
    customer_name VARCHAR(255) NOT NULL
);

-- Membuat tabel untuk detail transaksi
CREATE TABLE transaction_details (
    transaction_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id INT,
    product_id INT,
    quantity INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Menambahkan data dummy ke tabel products
INSERT INTO products (product_name, price) VALUES
('Laptop Pro', 1500.00),
('Mouse Gaming', 75.50),
('Keyboard Mechanical', 120.00),
('Monitor 4K', 450.75);

-- Menambahkan data dummy ke tabel transactions
INSERT INTO transactions (transaction_date, customer_name) VALUES
('2024-08-01', 'Andi'),
('2024-08-01', 'Budi'),
('2024-08-02', 'Cici');

-- Menambahkan data dummy ke tabel transaction_details
-- Transaksi 1 (Andi)
INSERT INTO transaction_details (transaction_id, product_id, quantity, subtotal) VALUES
(1, 1, 1, 1500.00),
(1, 2, 1, 75.50);

-- Transaksi 2 (Budi)
INSERT INTO transaction_details (transaction_id, product_id, quantity, subtotal) VALUES
(2, 3, 2, 240.00);

-- Transaksi 3 (Cici)
INSERT INTO transaction_details (transaction_id, product_id, quantity, subtotal) VALUES
(3, 4, 1, 450.75),
(3, 2, 1, 75.50);
