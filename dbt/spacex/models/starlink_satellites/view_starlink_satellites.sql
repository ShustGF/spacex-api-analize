{{ config(materialized='view') }}

SELECT JSONExtractString({{ source('my_database', 'starlink_satellites') }}.spacetrack, 'OBJECT_NAME') as object_name,
	   toDate(JSONExtractString({{ source('my_database', 'starlink_satellites') }}.spacetrack, 'LAUNCH_DATE')) as launch_date,
	   toDate(JSONExtractString({{ source('my_database', 'starlink_satellites') }}.spacetrack, 'DECAY_DATE')) as decay_date,
	   JSONExtractString({{ source('my_database', 'starlink_satellites') }}.spacetrack, 'ORIGINATOR') as originator,
	   {{ source('my_database', 'starlink_satellites') }}.spacetrack, 
	   {{ source('my_database', 'starlink_satellites') }}.version, 
	   {{ source('my_database', 'starlink_satellites') }}.launch, 
	   {{ source('my_database', 'starlink_satellites') }}.longitude, 
	   {{ source('my_database', 'starlink_satellites') }}.latitude, 
	   {{ source('my_database', 'starlink_satellites') }}.height_km, 
	   {{ source('my_database', 'starlink_satellites') }}.velocity_kms, 
	   {{ source('my_database', 'starlink_satellites') }}.id, 
	   {{ source('my_database', 'starlink_satellites') }}.datetime_in
FROM my_database.starlink_satellites
