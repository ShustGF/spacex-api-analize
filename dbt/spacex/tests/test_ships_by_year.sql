SELECT 
	*
FROM {{ ref("view_count_ships_by_year") }} 
WHERE year_start BETWEEN 2000 and 2100