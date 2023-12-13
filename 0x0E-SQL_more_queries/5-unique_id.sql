-- Create table: unique_id
-- id INT 1
-- name VARHVAR(256)
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
