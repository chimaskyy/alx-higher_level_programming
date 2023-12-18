-- list all records of the table second_table
-- list records >= 10
-- records are ordered by score

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
