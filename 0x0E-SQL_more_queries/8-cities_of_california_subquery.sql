-- List cities in database: hbtn_0d_usa
-- display cities in ascending order
SELECT `id`, `name` FROM `cities` WHERE `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "California")
ORDER BY `id`;
