CREATE DATABASE olist;
USE olist;

-- ---------------------------------------------------------------------------------------------------------

-- Normalizar Columnas
ALTER TABLE customers MODIFY customer_id VARCHAR(50);
ALTER TABLE customers MODIFY cus_zip_code INT;

ALTER TABLE geolocation MODIFY geo_zip_code INT;

ALTER TABLE order_items MODIFY order_id VARCHAR (50);
ALTER TABLE order_items MODIFY product_id VARCHAR (50);
ALTER TABLE order_items MODIFY seller_id VARCHAR (50);
ALTER TABLE order_items MODIFY order_item_id INT;

ALTER TABLE orders MODIFY order_id VARCHAR(50);
ALTER TABLE orders MODIFY customer_id VARCHAR(50);

ALTER TABLE reviews MODIFY review_id VARCHAR(50);
ALTER TABLE reviews MODIFY order_id VARCHAR(50);

ALTER TABLE sellers MODIFY seller_id VARCHAR(50);
ALTER TABLE sellers MODIFY sel_zip_code INT;

-- ---------------------------------------------------------------------------------------------------------

-- Determinamos claves primarias e indexamos las columnas necesarias
ALTER TABLE customers ADD PRIMARY KEY (customer_id);
ALTER TABLE customers ADD INDEX (cus_zip_code);

ALTER TABLE geolocation ADD PRIMARY KEY (geo_zip_code);
ALTER TABLE geolocation ADD INDEX (geo_zip_code);

ALTER TABLE order_items ADD COLUMN id_item INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE order_items ADD INDEX (order_id);
ALTER TABLE order_items ADD INDEX (seller_id);

ALTER TABLE orders ADD PRIMARY KEY (order_id);
ALTER TABLE orders ADD INDEX (customer_id);

ALTER TABLE reviews ADD PRIMARY KEY (review_id);
ALTER TABLE reviews ADD INDEX (order_id);

ALTER TABLE sellers ADD PRIMARY KEY (seller_id);
ALTER TABLE sellers ADD INDEX (sel_zip_code);

-- ---------------------------------------------------------------------------------------------------------

-- Para habilitar y generar las Foreign_Key
SET foreign_key_checks=0;

ALTER TABLE customers ADD FOREIGN KEY (cus_zip_code) REFERENCES geolocation(geo_zip_code);

ALTER TABLE order_items ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);
ALTER TABLE order_items ADD FOREIGN KEY (seller_id) REFERENCES sellers(seller_id);

ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

ALTER TABLE reviews ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE sellers ADD FOREIGN KEY (sel_zip_code) REFERENCES geolocation(geo_zip_code);