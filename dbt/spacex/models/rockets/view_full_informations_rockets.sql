SELECT 
	{{ values_from_json('height', "meters") }} as height_metr, -- вариант напсиания макроса на DBT
	JSONExtractString(diameter, 'meters') as diameter_metr, 
	JSONExtractString(mass, 'kg') as mass_kg, 
	JSONExtractInt(first_stage, 'engines') + JSONExtractInt(second_stage, 'engines') as count_engines_all,  
	JSONExtractString(arrayJoin(payload_weights), 'name') AS end_point,
	JSONExtractString(arrayJoin(payload_weights), 'kg') as max_weight, 
	name,  
	active, 
	stages, 
	cost_per_launch
FROM {{ source("db_spacex", "rockets") }}