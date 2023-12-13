-- Lists number of records with same score table: second_table
-- displays score and number of records,
-- sorted by number of records in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC
