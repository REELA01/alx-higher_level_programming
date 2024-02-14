-- Lists all shows in the database hbtn_0d_tvshows without a genre linked
SELECT se.title, ge.genre_id
  FROM tv_shows AS se
       LEFT JOIN tv_show_genres AS ge
       ON se.id = ge.show_id
       WHERE ge.genre_id IS NULL
 ORDER BY se.title, ge.genre_id;
