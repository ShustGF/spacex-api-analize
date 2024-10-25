SELECT YEAR(l.date_utc) as YEAR_launc, 
	   COUNT(DISTINCT l.id) as count_launces_starlink_and_ships_by_year
FROM {{ source("db_spacex", "ships") }} s
	JOIN {{ source("db_spacex", "launches") }} l
		ON arrayJoin(s.launches) = l.id  
	JOIN {{ source("db_spacex", "starlink_satellites") }} ss 
		ON l.id = ss.launch 
WHERE l.success
GROUP BY YEAR_launc