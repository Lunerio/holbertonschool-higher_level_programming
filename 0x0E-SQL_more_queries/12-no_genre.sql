-- list shows without a genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_shows.id
WHERE show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
