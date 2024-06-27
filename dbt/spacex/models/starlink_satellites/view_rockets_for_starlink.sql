SELECT 
	t_rockets.name,
	count(*) as count_launches
FROM {{ ref("view_starlink_satellites") }} AS t_starlink_satellites
	JOIN {{ source("db_spacex", "launches") }} as t_launches 
		ON t_starlink_satellites.launch = t_launches.id
	JOIN {{ source("db_spacex", "rockets") }} AS t_rockets 
		ON t_launches.rocket = t_rockets.id
GROUP BY t_rockets.name
ORDER BY count_launches DESC