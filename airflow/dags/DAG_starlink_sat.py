import json

import airflow
import airflow.utils
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from structure_json import StarlinkSat


def get_data_from_url(url):
  req_answer = requests.get(url)
  if req_answer.status_code == 404:
    raise AttributeError('Неверное значение URL-адреса')
  return req_answer.text


def get_object_starlink(sat_json):
  starlink_sat = StarlinkSat(
    spacetrack=sat_json['spaceTrack'], 
    version=sat_json['version'],
    launch=sat_json['launch'],
    longitude=sat_json['longitude'],
    latitude=sat_json['latitude'],
    height_km=sat_json['height_km'],
    velocity_kms=sat_json['velocity_kms'],
    id=sat_json['id']
  )
  return starlink_sat


def _add_values_starlink_in_table():
  pg_hook = PostgresHook(postgres_conn_id='logical_rep')
  engine = pg_hook.get_sqlalchemy_engine()
  session = Session(bind=engine)
  session.add_all([get_object_starlink(json_sat) for json_sat in json.loads(get_data_from_url(url_starlink))])
  session.commit()
  print('Выполнено')


url_starlink = 'https://api.spacexdata.com/v4/starlink'

dag = DAG(
    dag_id='get_objects_starlink',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
  )

add_values_starlink_in_table = PythonOperator(
    task_id = 'add_values_starlink_in_table',
    python_callable=_add_values_starlink_in_table,
    dag=dag,
  )