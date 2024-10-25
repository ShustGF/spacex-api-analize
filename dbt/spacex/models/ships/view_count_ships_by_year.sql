SELECT YEAR(date_utc) as year_start, count(s.id) as count_ships_by_years 
FROM {{ source("db_spacex", "ships") }} s
	JOIN {{ source("db_spacex", "launches") }} l
		ON arrayJoin(s.launches) = l.id  
where l.success 
GROUP BY year_start
ORDER BY year_start