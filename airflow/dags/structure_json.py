from sqlalchemy import Column, Numeric, String, JSON
from sqlalchemy.orm import declarative_base

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