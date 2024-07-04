SELECT DISTINCT full_name
FROM {{ source("db_spacex", "landpads") }}