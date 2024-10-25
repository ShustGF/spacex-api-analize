{% test values_more_zero(model, column_name, value_more=0) %}

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