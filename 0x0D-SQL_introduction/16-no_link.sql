-- list all record of the table second_table
-- rows without a name value to be skipped
-- display score and name
-- listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
