SELECT region, 
       SUM(LENGTH(launches)) as count_launches
FROM {{ source("db_spacex", "landpads") }}
GROUP BY region
ORDER BY  count_launches DESC