import airflow
import airflow.utils

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator


from starlink_sat import get_starlink_object,  get_starlink_object, loads_data_in_db



def _add_values_starlink_in_table():
  pg_hook = PostgresHook(postgres_conn_id='logical_rep')
  engine = pg_hook.get_sqlalchemy_engine()
  loads_data_in_db(get_starlink_object, url_starlink, engine)


url_starlink = 'https://api.spacexdata.com/v4/starlink'

dag = DAG(
    dag_id='get_objects_starlink',
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval=None,
  )

add_values_starlink_in_table = PythonOperator(
    task_id = 'add_values_starlink_in_table',
    python_callable=_add_values_starlink_in_table,
    dag=dag,
  )

сhecking_the_connection_PSQL = PostgresOperator(
  task_id = 'сhecking_the_connection_PSQL',
  postgres_conn_id='logical_rep',
  sql="""
  SELECT 1
  FROM starlink_satellites
  WHERE 1=0
  """,
  dag=dag,
) 

сhecking_the_connection_PSQL >> add_values_starlink_in_table
