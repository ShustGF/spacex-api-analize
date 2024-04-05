import json

import requests
import logging

from sqlalchemy.orm import Session
from structure_json import StarlinkSat


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

def loads_data_in_db(function_class, url, engine):
  logger = logging.getLogger(__name__)
  session = Session(bind=engine)
  json_values = json.loads(get_data_from_url(url))
  session.add_all([function_class(json_value) for json_value in json_values])
  session.commit()
  logger.info(f'Данные от URL({url}) обрыботаны успешно')


if __name__ == '__main__':
  pass
