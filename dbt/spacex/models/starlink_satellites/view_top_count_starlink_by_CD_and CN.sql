SELECT 
	if(empty(JSONExtractString(spacetrack, 'COUNTRY_CODE')), 
	   'US',
	   JSONExtractString(spacetrack, 'COUNTRY_CODE')) AS COUNTRY_CODE, 
	JSONExtractString(spacetrack, 'CENTER_NAME') AS CENTER_NAME,
	COUNT(id) AS count_satellite
FROM {{ source("db_spacex", "starlink_satellites") }}
GROUP BY 
	COUNTRY_CODE, 
	CENTER_NAME