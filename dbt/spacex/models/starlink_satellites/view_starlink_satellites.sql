{{ config(materialized='view') }}

SELECT JSONExtractString(t_starlink_satellites.spacetrack, 'OBJECT_NAME') as object_name,
	   toDate(JSONExtractString(t_starlink_satellites.spacetrack, 'LAUNCH_DATE')) as launch_date,
	   toDate(JSONExtractString(t_starlink_satellites.spacetrack, 'DECAY_DATE')) as decay_date,
	   JSONExtractString(t_starlink_satellites.spacetrack, 'ORIGINATOR') as originator,
	   t_starlink_satellites.spacetrack, 
	   t_starlink_satellites.version, 
	   t_starlink_satellites.launch, 
	   t_starlink_satellites.longitude, 
	   t_starlink_satellites.latitude, 
	   t_starlink_satellites.height_km, 
	   t_starlink_satellites.velocity_kms, 
	   t_starlink_satellites.id, 
	   t_starlink_satellites.datetime_in
FROM {{ source('my_database', 'starlink_satellites') }} AS t_starlink_satellites
