SELECT 
	{{ values_from_json('height', "meters") }} as height_metr, -- вариант напсиания макроса на DBT
	{{ values_from_json('diameter', "meters") }} as diameter_metr, 
	{{ values_from_json('mass', "kg") }} as mass_kg, 
	{{ values_from_json('first_stage', "engines") }} as count_engines_all,  
	{{ values_from_json('arrayJoin(payload_weights)', "name") }}  AS end_point,
	{{ values_from_json('arrayJoin(payload_weights)', "kg") }} as max_weight, 
	name,  
	active, 
	stages, 
	cost_per_launch
FROM {{ source("db_spacex", "rockets") }}