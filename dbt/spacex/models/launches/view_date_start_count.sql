{{ config(materialized='view') }}

with table_launches_in_launchpads as(
SELECT t_launchpads.name as name, 
	   t_launchpads.launches as launches_id 
FROM {{ source('my_database', 'launchpads') }} AS t_launchpads ARRAY JOIN 
		t_launchpads.launches),
table_date_start_count as (
SELECT name, 
	   launches_id, 
	   toStartOfMonth(t_launches.static_fire_date_utc) as data_start
FROM table_launches_in_launchpads 
		JOIN {{ source('my_database', 'launches') }} AS t_launches
			ON table_launches_in_launchpads.launches_id = 
				t_launches.id
WHERE t_launches.static_fire_date_utc IS NOT NULL)
SELECT data_start, 
	   count(launches_id) as count_launch_in_launchpads
FROM table_date_start_count
GROUP BY data_start
