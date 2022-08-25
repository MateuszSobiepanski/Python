CREATE TABLE `clients` (
	`id_client` int NOT NULL AUTO_INCREMENT,
	`id_address` int NOT NULL,
	`name` varchar(50) NOT NULL,
	`s_name` varchar(50) NOT NULL,
	`phone` varchar(50) NOT NULL,
	PRIMARY KEY (`id_client`)
);

CREATE TABLE `address` (
	`id_address` int NOT NULL AUTO_INCREMENT,
	`city` varchar(50) NOT NULL,
	`street` varchar(50) NOT NULL,
	`number` varchar(15) NOT NULL,
	PRIMARY KEY (`id_address`)
);

CREATE TABLE `accounts` (
	`account_id` int NOT NULL AUTO_INCREMENT,
	`id_client` int NOT NULL,
	`username` varchar(50) NOT NULL,
	`password` varchar(50) NOT NULL,
	`balance` bigint NOT NULL DEFAULT '0',
	`created_at` DATETIME NOT NULL,
	`delted_at` DATETIME NOT NULL,
	PRIMARY KEY (`account_id`)
);

CREATE TABLE `transactions` (
	`id_transaction` int NOT NULL AUTO_INCREMENT,
	`from_account_id` int NOT NULL,
	`to_account_id` int NOT NULL,
	`date` DATETIME NOT NULL,
	`amount` bigint NOT NULL,
	`transaction_status` varchar(50) NOT NULL,
	`transaction_type` varchar(50) NOT NULL,
	PRIMARY KEY (`id_transaction`)
);

CREATE TABLE `login_try` (
	`id_login` int NOT NULL AUTO_INCREMENT,
	`account_id` int NOT NULL,
	`date` DATETIME NOT NULL,
	`status` varchar(50) NOT NULL,
	PRIMARY KEY (`id_login`)
);

ALTER TABLE `clients` ADD CONSTRAINT `clients_fk0` FOREIGN KEY (`id_address`) REFERENCES `address`(`id_address`);

ALTER TABLE `accounts` ADD CONSTRAINT `accounts_fk0` FOREIGN KEY (`id_client`) REFERENCES `clients`(`id_client`);

ALTER TABLE `transactions` ADD CONSTRAINT `transactions_fk0` FOREIGN KEY (`from_account_id`) REFERENCES `accounts`(`account_id`);

ALTER TABLE `transactions` ADD CONSTRAINT `transactions_fk1` FOREIGN KEY (`to_account_id`) REFERENCES `accounts`(`account_id`);

ALTER TABLE `login_try` ADD CONSTRAINT `login_try_fk0` FOREIGN KEY (`account_id`) REFERENCES `accounts`(`account_id`);






