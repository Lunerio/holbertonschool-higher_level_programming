-- Show a table with a list of genres in data base and how many shows each genre has

SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
