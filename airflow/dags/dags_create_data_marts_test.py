"""DAG тестирования Data Marts"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(
    dag_id="dags_test_data_marts",
    start_date=days_ago(5),
    schedule_interval=None,
)

create_data_marts = BashOperator(
    task_id="test_data_marts", bash_command="cd /mnt/dbt/spacex/ && dbt test", dag=dag
)


create_data_marts
