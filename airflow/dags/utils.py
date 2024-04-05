import json
import requests
import logging

from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy.orm import Session
from entities import StarlinkSat, LaunchesSpaceX


def get_data_from_url(url):
  req_answer = requests.get(url)
  if req_answer.status_code == 404:
    raise AttributeError('Неверное значение URL-адреса')
  return req_answer.text


def get_starlink_object(sat_json):
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


def get_launches(sat_json):
  starlink_sat = LaunchesSpaceX(
    fairings=sat_json['fairings'],
    links=sat_json['links'],
    static_fire_date_utc=sat_json['static_fire_date_utc'],
    static_fire_date_unix=sat_json['static_fire_date_unix'],
    tbd=sat_json['tbd'],
    net=sat_json['net'],
    window=sat_json['window'],
    rocket=sat_json['rocket'],
    success=sat_json['success'],
    failures=sat_json['failures'],
    details=sat_json['details'],
    crew=sat_json['crew'],
    ships=sat_json['ships'],
    capsules=sat_json['capsules'],
    payloads=sat_json['payloads'],
    launchpad=sat_json['launchpad'],
    auto_update=sat_json['auto_update'],
    flight_number=sat_json['flight_number'],
    name=sat_json['name'],
    date_utc=sat_json['date_utc'],
    date_unix=sat_json['date_unix'],
    date_local=sat_json['date_local'],
    date_precision=sat_json['date_precision'],
    upcoming=sat_json['upcoming'],
    cores=sat_json['cores'],
    id=sat_json['id']
  )
  return starlink_sat


def loads_data_in_db(function_class, url, postgres_conn_id):
  logger = logging.getLogger(__name__)
  pg_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
  engine = pg_hook.get_sqlalchemy_engine()
  session = Session(bind=engine)
  json_values = json.loads(get_data_from_url(url))
  session.add_all([function_class(json_value) for json_value in json_values])
  session.commit()
  logger.info(f'Данные от URL({url}) обработаны успешно')


if __name__ == '__main__':
  pass
