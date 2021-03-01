-- count the rows with the same score values
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
