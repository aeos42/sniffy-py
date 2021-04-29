from sqlalchemy import Column, Float, DateTime, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AirData(Base):
    __tablename__ = 'air_data'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    temp = Column(Float)
    hum = Column(Float)
    co2 = Column(Float)
    pm1 = Column(Float)
    pm25 = Column(Float)
    pm10 = Column(Float)


