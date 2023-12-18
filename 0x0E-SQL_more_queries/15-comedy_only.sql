-- list comedy shows

SELECT title
FROM tv_shows
WHERE id IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id IN (
        SELECT id 
        FROM tv_genres
        WHERE name = 'comedy'
    )
)
ORDER BY title ASC;