SELECT 
	   {{ values_from_json('spacetrack', "OBJECT_NAME") }} AS OBJECT_NAME, 
	   {{ values_from_json('spacetrack', "MEAN_MOTION") }} AS MEAN_MOTION
FROM {{ source("db_spacex", "starlink_satellites") }}
ORDER BY MEAN_MOTION DESC
LIMIT 10