{% macro values_from_json(column_json, value_key) %}

    JSONExtractString({{ column_json }}, '{{ value_key }}')

{% endmacro %}