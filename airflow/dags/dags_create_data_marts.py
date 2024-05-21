"""DAG создания Data Marts"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


dag = DAG(
    dag_id="dags_change_data_marts",
    start_date=days_ago(5),
    schedule_interval=None,
)

create_data_marts = BashOperator(
    task_id="create_test_view", bash_command="cd /mnt/dbt/spacex/ && dbt run", dag=dag
)

create_data_marts