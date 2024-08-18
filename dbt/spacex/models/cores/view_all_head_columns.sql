SELECT static_fire_date_utc, 
	   success, 
	   failures, 
	   details,
	   l.name,
	   spacetrack,
	   version,
	   ss.longitude,
	   ss.latitude,
	   height_km,
	   velocity_kms,
	   legacy_id,
	   model,
	   s.type,
	   roles,
	   s.mass_kg,
	   home_port,
	   year_built,
	   s.name,
	   s.active,
	   height,
	   diameter,
	   mass,
	   r.name,
	   country,
	   company,
	   p.name,
	   p.type,
	   p.mass_kg,
	   orbit,
	   reference_system,
	   regime,
	   l2.name,
	   full_name,
	   locality,
	   region,
	   c.last_update,
	   c.serial,
	   c.status,
	   c2.name,
	   c2.status,
	   c3.reuse_count,
	   c3.status,
	   c3.type
FROM {{ source("db_spacex", "launches") }} l 
	LEFT JOIN {{ source("db_spacex", "starlink_satellites") }} ss 
		ON l.id = ss.launch 
	LEFT JOIN {{ source("db_spacex", "ships") }} s 
		ON l.id = arrayJoin(s.launches)
	LEFT JOIN {{ source("db_spacex", "rockets") }} r 
		ON l.rocket = r.id
	LEFT JOIN {{ source("db_spacex", "payload") }} p 
		ON l.id = p.launch 
	LEFT JOIN {{ source("db_spacex", "launchpads") }} l2 
		ON l.id = arrayJoin(l2.launches) 
	LEFT JOIN {{ source("db_spacex", "cores") }} c 
		ON l.id = arrayJoin(c.launches)   
	LEFT JOIN {{ source("db_spacex", "crew") }} c2 
		ON l.id = arrayJoin(c2.launches)
	LEFT JOIN {{ source("db_spacex", "capsules") }} c3 
		ON l.id = arrayJoin(c3.launches) 