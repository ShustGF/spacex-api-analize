SELECT 
    full_name, 
    LENGTH(launches) AS count_launches
FROM {{ source("db_spacex", "landpads") }}