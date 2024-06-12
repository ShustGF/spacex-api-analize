{{ config(materialized='view') }}

with table_launches_in_launchpads as(
SELECT {{ source('my_database', 'launchpads') }}.name as name, 
	   {{ source('my_database', 'launchpads') }}.launches as launches_id 
FROM {{ source('my_database', 'launchpads') }} ARRAY JOIN 
		{{ source('my_database', 'launchpads') }}.launches),
table_date_start_count as (
SELECT name, 
	   launches_id, 
	   toStartOfMonth({{ source('my_database', 'launches') }}.static_fire_date_utc) as data_start
FROM table_launches_in_launchpads 
		JOIN {{ source('my_database', 'launches') }} 
			ON table_launches_in_launchpads.launches_id = 
				{{ source('my_database', 'launches') }}.id)
SELECT data_start, 
	   count(launches_id) as count_launch_in_launchpads
FROM table_date_start_count
GROUP BY data_start
HAVING data_start IS NOT NULL
