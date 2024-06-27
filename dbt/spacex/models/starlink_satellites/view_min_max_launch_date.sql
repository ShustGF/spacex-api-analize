SELECT 
	min(toDate(JSONExtractString(spacetrack, 'LAUNCH_DATE'))) AS min_launch_date,
	max(toDate(JSONExtractString(spacetrack, 'LAUNCH_DATE'))) AS max_launch_date
FROM {{ source("db_spacex", "starlink_satellites") }}