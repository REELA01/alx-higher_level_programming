-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT se.`title`, ge.`genre_id`
  FROM `tv_shows` AS se
       LEFT JOIN `tv_show_genres` AS ge
       ON se.`id` = ge.`show_id`
 ORDER BY se.`title`, ge.`genre_id`;
