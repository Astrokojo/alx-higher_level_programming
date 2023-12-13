-- Create database: hbtn_0d_usa
-- with table: states
-- id INT 1 unique aitu generated not null primary key
-- name VARHVAR(256)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	PRIMARY KEY(`id`),
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
);
