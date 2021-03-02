-- list all shows and related genres linked to the show
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id;
LEFT JOIN tv_genres ON tv_show_genres.genre.id = tv_genres.id;
