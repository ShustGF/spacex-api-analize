SELECT JSONExtractString(spacetrack, 'OBJECT_NAME') AS OBJECT_NAME
FROM {{ source("db_spacex", "starlink_satellites") }}
WHERE longitude IS NULL OR 
	  latitude IS NULL OR
	  height_km IS NULL OR
	  velocity_kms IS NULL