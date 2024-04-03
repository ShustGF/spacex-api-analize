import requests
import json
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column,Numeric , String, JSON

db_name = 'replica_logical'
db_user = 'postgres'
db_pass = 'gfh0km'
db_host = 'localhost'
db_port = '5431'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

url_starlink = "https://api.spacexdata.com/v4/starlink"
Base = sqlalchemy.orm.declarative_base()

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

class StarlinkSat(Base):
  __tablename__ = 'starlink_satellites'
  spacetrack = Column(JSON)
  version = Column(String)
  launch = Column(String)
  longitude = Column(Numeric)
  latitude = Column(Numeric)
  height_km = Column(Numeric)
  velocity_kms = Column(Numeric)
  id = Column(String, primary_key=True)

  def __init__(self, spacetrack, version=None, launch=None, longitude=None, 
               latitude=None, height_km=None, velocity_kms=None, id=None):
    self.spacetrack = spacetrack
    self.version = version
    self.launch = launch
    self.longitude = longitude
    self.latitude = latitude
    self.height_km = height_km
    self.velocity_kms = velocity_kms
    self.id = id

    @property
    def spacetrack(self):
      return self._spacetrack
    
    @spacetrack.setter
    def spacetrack(self, spacetrack):
      self._spacetrack = json.loads(spacetrack)


engine = create_engine(db_string)
session = Session(bind=engine)
session.add_all([object_starlink(json_sat) for json_sat in json.loads(return_request(url_starlink))])
# print(session.new)
session.commit()
print("Выполнено")