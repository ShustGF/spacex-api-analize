SELECT 
	if(empty({{ values_from_json('spacetrack', "COUNTRY_CODE") }}), 
	   'US',
	   {{ values_from_json('spacetrack', "COUNTRY_CODE") }}) AS COUNTRY_CODE, 
	{{ values_from_json('spacetrack', "CENTER_NAME") }} AS CENTER_NAME,
	COUNT(id) AS count_satellite
FROM {{ source("db_spacex", "starlink_satellites") }}
GROUP BY 
	COUNTRY_CODE, 
	CENTER_NAME