{{ config(materialized='view') }}

SELECT {{ source('my_database', 'rockets') }}.name, count(*) as count_launches
FROM {{ ref('view_starlink_satellites') }}  JOIN {{ source('my_database', 'launches') }} 
												ON {{ ref('view_starlink_satellites') }}.launch = {{ source('my_database', 'launches') }}.id 
	 									   JOIN {{ source('my_database', 'rockets') }} 
										   		ON {{ source('my_database', 'launches') }}.rocket = {{ source('my_database', 'rockets') }}.id
GROUP BY {{ source('my_database', 'rockets') }}.name 
ORDER BY count_launches DESC
