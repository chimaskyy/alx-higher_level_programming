-- display avaerage temperature(Fah)
-- display top 3 of cities temperature
-- during july and August
-- by city ordered by temperature(desc)

SELECT city,
AVG(value) AS avg_temp FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
