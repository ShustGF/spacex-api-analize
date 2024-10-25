-- Singular тест
SELECT
	*
FROM 
	{{ ref("view_count_cores_by_status") }}
WHERE
	count_cores_by_status <= 0