SELECT {{ values_from_json('spacetrack', "OBJECT_NAME") }} AS object_name,
	toDate(
		{{ values_from_json('spacetrack', "LAUNCH_DATE") }} 
	) AS launch_date,
	toDate(
		{{ values_from_json('spacetrack', "DECAY_DATE") }}
	) AS decay_date,
	{{ values_from_json('spacetrack', "ORIGINATOR") }} AS originator,
	spacetrack,
	version,
	launch,
	longitude,
	latitude,
	height_km,
	velocity_kms,
	id,
	datetime_in
FROM {{ source("db_spacex", "starlink_satellites") }}