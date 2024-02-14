-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT se.title, ge.genre_id
  FROM tv_shows AS se
        INNER JOIN tv_show_genres AS ge
	ON se.id = ge.show_id
 ORDER BY se.title, ge.genre_id;
