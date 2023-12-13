-- List records of table: second_table
-- exclude rows without a name value.
-- display the score and the name in that order,
-- display records in descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
