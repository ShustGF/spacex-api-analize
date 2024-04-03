import json

import requests
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from structure_json import StarlinkSat


def return_request(url):
  req_answer = requests.get(url)
  if req_answer.status_code == 404:
    raise AttributeError("Неверное значение URL-адреса")
  return req_answer.text


def object_starlink(sat_json):
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

if __name__ == '__main__':
  
  db_name = config('POSTGRES_SENDER_DB')
  db_user = config('POSTGRES_SENDER_USER')
  db_pass = config('POSTGRES_SENDER_PASSWORD')
  db_host = config('POSTGRES_SENDER_HOST')
  db_port = config('POSTGRES_SENDER_PORT')
  db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

  url_starlink = "https://api.spacexdata.com/v4/starlink"
  
  engine = create_engine(db_string)
  session = Session(bind=engine)
  session.add_all([object_starlink(json_sat) for json_sat in json.loads(return_request(url_starlink))])
  # print(session.new)
  session.commit()
  print("Выполнено")