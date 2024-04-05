from sqlalchemy import Column, Numeric, String, JSON, Boolean, ARRAY, TIMESTAMP
from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()


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
    

class LaunchesSpaceX(Base):
  __tablename__ = 'launches'
  fairings = Column(JSON)
  links = Column(JSON)
  static_fire_date_utc = Column(TIMESTAMP)
  static_fire_date_unix = Column(Numeric)
  tbd = Column(Boolean)
  net = Column(Boolean)
  window = Column(Numeric)
  rocket = Column(String)
  success = Column(Boolean)
  failures = Column(ARRAY(JSON))
  details = Column(String)
  crew = Column(ARRAY(String))
  ships = Column(ARRAY(String))
  capsules = Column(ARRAY(String))
  payloads = Column(ARRAY(String))
  launchpad = Column(String)
  auto_update = Column(Boolean)
  flight_number = Column(Numeric)
  name = Column(String)
  date_utc = Column(TIMESTAMP)
  date_unix = Column(Numeric)
  date_local = Column(String)
  date_precision = Column(String)
  upcoming = Column(Boolean)
  cores = Column(ARRAY(JSON))
  id = Column(String, primary_key=True)

  def __init__(self, fairings=None, links=None, static_fire_date_utc=None, static_fire_date_unix=None,
                tbd=None, net=None, window=None, rocket=None, success=None, failures=[], details=None,
                crew=None, ships=None, capsules=None, payloads=None, launchpad=None, auto_update=None, 
                flight_number=None, name=None, date_utc=None, date_unix=None, date_local=None,
                date_precision=None, upcoming=None, cores=None, id=None):
    self.fairings = fairings
    self.links = links
    self.static_fire_date_utc = static_fire_date_utc
    self.static_fire_date_unix = static_fire_date_unix
    self.tbd = tbd
    self.net = net
    self.window = window
    self.rocket = rocket
    self.success = success
    self.failures = failures
    self.details = details
    self.crew = crew
    self.ships = ships
    self.capsules = capsules
    self.payloads = payloads
    self.launchpad = launchpad
    self.auto_update = auto_update
    self.flight_number = flight_number
    self.name = name
    self.date_utc = date_utc
    self.date_unix = date_unix
    self.date_local = date_local
    self.date_precision = date_precision
    self.upcoming = upcoming
    self.cores = cores
    self.id = id

    def __current_datetime_utc(self, value):
      if value == None:
        return None
      else:
        format_time_utc = '%Y-%m-%dT%H:%M:%S.%fZ'
        return datetime.strptime(value,format_time_utc)

    @property
    def static_fire_date_utc(self):
      return self._static_fire_date_utc
    
    @static_fire_date_utc.setter
    def static_fire_date_utc(name, value):
      self._static_fire_date_utc=__current_datetime_utc(value=value)


    @property
    def date_utc(self):
      return self._static_fire_date_utc
    
    @date_utc.setter
    def date_utc(name, value):
      if value == None:
        self._date_utc=__current_datetime_utc(value=value)

class Capsules(Base):
  __tablename__='capsules'
  reuse_count=Column(Numeric)
  water_landings=Column(Numeric)
  land_landings=Column(Numeric)
  last_update=Column(String)
  launches=Column(ARRAY(String))
  serial=Column(String)
  status=Column(String)
  type=Column(String)
  id = Column(String, primary_key=True)

  def __init__(self, reuse_count=None, water_landings=None, land_landings=None, last_update=None, 
               launches=None, serial=None, status=None, type=None, id=None):
    self.reuse_count = reuse_count
    self.water_landings = water_landings
    self.land_landings = land_landings
    self.last_update = last_update
    self.launches = launches
    self.serial = serial
    self.status = status
    self.type = type
    self.id = id
