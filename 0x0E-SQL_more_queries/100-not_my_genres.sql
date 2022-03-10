-- list all genres not linked to the show Dexter
-- USING ONLY ONE JOIN :p 

SELECT name 
FROM tv_genres
WHERE tv_genres.id not in(
SELECT tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;


-- SQL                                        
-- SQL                                        
                                              
                                              
--SELECT name                                   
--FROM tv_genres where id not in(               
--select tv_show_genres.genre_id                
--from tv_shows join tv_show_genres             
--on tv_show_genres.show_id = tv_shows.id       
--where (title = 'Dexter'))                     
--ORDER BY name;                                
                 
