-- List cities in database: hbtn_0d_usa
-- display cities in ascending order
SELECT `id`, `name` FROM `cities` where `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "Carlifornia")
ORDER BY `id`;
