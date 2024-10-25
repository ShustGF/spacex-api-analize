SELECT 
	min(toDate({{ values_from_json('spacetrack', "LAUNCH_DATE") }})) AS min_launch_date,
	max(toDate({{ values_from_json('spacetrack', "LAUNCH_DATE") }})) AS max_launch_date
FROM {{ source("db_spacex", "starlink_satellites") }}