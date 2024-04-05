from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

from utils import get_starlink_object,  get_starlink_object, loads_data_in_db, get_launches


def _add_starlink_values_to_table():
  # pg_hook = PostgresHook(postgres_conn_id='logical_rep')
  # engine = pg_hook.get_sqlalchemy_engine()
  loads_data_in_db(get_starlink_object, url_starlink, postgres_conn_id='logical_rep')

def _add_launches_values_to_table():
  # pg_hook = PostgresHook(postgres_conn_id='logical_rep')
  # engine = pg_hook.get_sqlalchemy_engine()
  loads_data_in_db(get_launches, url_launches, postgres_conn_id='logical_rep')


url_starlink = 'https://api.spacexdata.com/v4/starlink'
url_launches = 'https://api.spacexdata.com/v4/launches'

dag = DAG(
  dag_id='DAG_DB_SpaceX_API',
  start_date=days_ago(5),
  schedule_interval=None,
)

add_starlink_values_to_table  = PythonOperator(
  task_id = 'add_starlink_values_to_table',
  python_callable=_add_starlink_values_to_table,
  dag=dag,
)

add_launches_values_to_table  = PythonOperator(
  task_id = 'add_launches_values_to_table',
  python_callable=_add_launches_values_to_table,
  dag=dag,
)

check_db_connection = PostgresOperator(
  task_id = 'check_db_connection',
  postgres_conn_id='logical_rep',
  sql='''
  SELECT 1
  ''',
  dag=dag,
) 

check_db_connection >> add_starlink_values_to_table
check_db_connection >> add_launches_values_to_table
