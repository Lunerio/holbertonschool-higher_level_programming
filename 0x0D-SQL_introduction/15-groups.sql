-- count the rows with the same score values
SELECT score, COUNT(*) as number FROM second_table GROUP BY score;
