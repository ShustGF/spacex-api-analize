{% test values_more_zero(model, column_name, value_more) %}

    SELECT
        *
    FROM (
        SELECT
            {{ column_name }}
        FROM
            {{ model }} 
        WHERE {{ column_name }} < {{ value_more}}
    ) validation_errors

{% endtest %}