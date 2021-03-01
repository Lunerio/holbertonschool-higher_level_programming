-- list records from second_table.
-- if there is no name value don't show
-- descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
