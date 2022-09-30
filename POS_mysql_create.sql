#DROP DATABASE POS;
#CREATE DATABASE POS;
USE POS;
#SELECT * FROM company;
CREATE TABLE `products` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`description` varchar(255),
	`price_per_unit` bigint NOT NULL,
	`company_id` bigint,
	`barcode` varchar(255),
	`category_id` bigint NOT NULL,
	`quantity` bigint NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `customer` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`first_name` varchar(255),
	`last_name` varchar(255) NOT NULL,
	`mobile` varchar(255),
	`address` int(255),
	`city` varchar(255),
	`province` varchar(255),
	`block` varchar(255),
	`street` varchar(255),
	`phone` varchar(255),
	`birthdate` DATE,
	`gender` varchar(255) NOT NULL,
	`occupation` varchar(255),
	`contract_type` varchar(255),
	`customer_type` varchar(255),
	PRIMARY KEY (`id`)
);

CREATE TABLE `sell` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`product_id` bigint NOT NULL,
	`quantity` bigint NOT NULL,
	`discount` bigint,
	PRIMARY KEY (`id`)
);

CREATE TABLE `sell_invoice` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`customer_id` bigint NOT NULL,
	`sell_id` bigint NOT NULL,
	`order_type_id` int NOT NULL,
	`time` DATETIME NOT NULL,
	`shipping_type_id` int NOT NULL,
	`shipping_cost` bigint,
	`discount` bigint,
	PRIMARY KEY (`id`)
);

CREATE TABLE `buy_invoice` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`company_id` bigint NOT NULL,
	`buy_id` bigint NOT NULL,
	`time` DATETIME NOT NULL,
	`order_type_id` int NOT NULL,
	`discount` bigint,
	`official_invoice_id` varchar(255),
	PRIMARY KEY (`id`)
);

CREATE TABLE `buy` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`product_id` bigint NOT NULL,
	`quantity` bigint NOT NULL,
	`price_per_unit` bigint,
	`discount` bigint,
	PRIMARY KEY (`id`)
);

CREATE TABLE `company` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL UNIQUE,
	`phone` varchar(255) NOT NULL,
	`mobile` varchar(255),
	`address` varchar(255),
	`city` varchar(255),
	`province` varchar(255),
	PRIMARY KEY (`id`)
);

CREATE TABLE `order_type` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`description` varchar(255),
	PRIMARY KEY (`id`)
);

CREATE TABLE `shipping_type` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `product_category` (
	`id` bigint NOT NULL AUTO_INCREMENT,
	`name` bigint NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

ALTER TABLE `products` ADD CONSTRAINT `products_fk0` FOREIGN KEY (`company_id`) REFERENCES `company`(`id`);

ALTER TABLE `products` ADD CONSTRAINT `products_fk1` FOREIGN KEY (`category_id`) REFERENCES `product_category`(`id`);

ALTER TABLE `sell` ADD CONSTRAINT `sell_fk0` FOREIGN KEY (`product_id`) REFERENCES `products`(`id`);

ALTER TABLE `sell_invoice` ADD CONSTRAINT `sell_invoice_fk0` FOREIGN KEY (`customer_id`) REFERENCES `customer`(`id`);

ALTER TABLE `sell_invoice` ADD CONSTRAINT `sell_invoice_fk1` FOREIGN KEY (`sell_id`) REFERENCES `sell`(`id`);

ALTER TABLE `sell_invoice` ADD CONSTRAINT `sell_invoice_fk2` FOREIGN KEY (`order_type_id`) REFERENCES `order_type`(`id`);

ALTER TABLE `sell_invoice` ADD CONSTRAINT `sell_invoice_fk3` FOREIGN KEY (`shipping_type_id`) REFERENCES `shipping_type`(`id`);

ALTER TABLE `buy_invoice` ADD CONSTRAINT `buy_invoice_fk0` FOREIGN KEY (`company_id`) REFERENCES `company`(`id`);

ALTER TABLE `buy_invoice` ADD CONSTRAINT `buy_invoice_fk1` FOREIGN KEY (`buy_id`) REFERENCES `buy`(`id`);

ALTER TABLE `buy_invoice` ADD CONSTRAINT `buy_invoice_fk2` FOREIGN KEY (`order_type_id`) REFERENCES `order_type`(`id`);

ALTER TABLE `buy` ADD CONSTRAINT `buy_fk0` FOREIGN KEY (`product_id`) REFERENCES `products`(`id`);


