from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

from starlink_sat import get_starlink_object,  get_starlink_object, loads_data_in_db


def _add_starlink_values_to_table():
  pg_hook = PostgresHook(postgres_conn_id='logical_rep')
  engine = pg_hook.get_sqlalchemy_engine()
  loads_data_in_db(get_starlink_object, url_starlink, engine)


url_starlink = 'https://api.spacexdata.com/v4/starlink'

dag = DAG(
  dag_id='get_objects_starlink',
  start_date=days_ago(5),
  schedule_interval=None,
)

add_starlink_values_to_table  = PythonOperator(
  task_id = 'add_starlink_values_to_table ',
  python_callable=_add_starlink_values_to_table,
  dag=dag,
)

check_db_connection = PostgresOperator(
  task_id = 'check_db_connection',
  postgres_conn_id='logical_rep',
  sql="""
  SELECT 1
  FROM starlink_satellites
  WHERE 1=0
  """,
  dag=dag,
) 

check_db_connection >> add_starlink_values_to_table
