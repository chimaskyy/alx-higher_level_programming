-- list genres of show dexter
 
SELECT name
FROM tv_genres
WHERE id IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id IN (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY name ASC;
