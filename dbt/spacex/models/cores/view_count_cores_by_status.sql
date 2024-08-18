SELECT 
	status,
	COUNT(id) AS count_cores_by_status
FROM {{ source("db_spacex","cores") }}
GROUP BY status
ORDER BY count_cores_by_status DESC