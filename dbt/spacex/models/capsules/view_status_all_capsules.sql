SELECT status, count(c.id)
FROM {{ source("db_spacex", "launches") }} l 
	JOIN {{ source("db_spacex", "capsules") }} c 
		ON l.id = arrayJoin(c.launches) 
where l.success 
group by status 