import requests
import json
from sqlalchemy import create_engine

URL = "https://api.spacexdata.com/v4/starlink"

def return_request(URL):
  r = requests.get(URL)
  if r.status_code == 404:
    raise AttributeError("Неверное значение URL-адреса")
  return r.text



class Starlink_sat:
  def __init__(self, spaceTrack, version=None, launch=None, longitude=None, latitude=None, height_km=None, velocity_kms=None, id=None):
    self.spaceTrack = spaceTrack
    self.version = version
    self.launch = launch
    self.longitude = longitude
    self.latitude = latitude
    self.height_km = height_km
    self.velocity_kms = velocity_kms
    self.id = id

    @property
    def spaceTrack(self):
      return self._spaceTrack
    
    @spaceTrack.setter
    def spaceTrack(self, spaceTrack):
      self._spaceTrack = json.loads(spaceTrack)




sat_json =  json.loads(return_request(URL))[0]

starlink_sat = Starlink_sat(
  spaceTrack=sat_json['spaceTrack'], 
  version=sat_json['version'],
  launch=sat_json['launch'],
  longitude=sat_json['longitude'],
  latitude=sat_json['latitude'],
  height_km=sat_json['height_km'],
  velocity_kms=sat_json['velocity_kms'],
  id=sat_json['id']
)

print(starlink_sat.spaceTrack)


engine = create_engine('postgresql+psycopg2://postgres:gfh0km@localhost:5433/postgres')