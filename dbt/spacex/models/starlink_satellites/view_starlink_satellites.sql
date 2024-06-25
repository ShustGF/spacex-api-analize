{ { config(materialized = 'view') } }

SELECT JSONExtractString(spacetrack, 'OBJECT_NAME') AS object_name,
	toDate(
		JSONExtractString(spacetrack, 'LAUNCH_DATE')
	) AS launch_date,
	toDate(
		JSONExtractString(spacetrack, 'DECAY_DATE')
	) AS decay_date,
	JSONExtractString(spacetrack, 'ORIGINATOR') AS originator,
	spacetrack,
	version,
	launch,
	longitude,
	latitude,
	height_km,
	velocity_kms,
	id,
	datetime_in
FROM { { source('my_database', 'starlink_satellites') } }