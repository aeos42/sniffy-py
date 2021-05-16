from sqlalchemy import Column, Float, DateTime, String, Integer
from db import Base



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

    def __init__(self, time=None, temp=None, hum=None, co2=None, pm1=None, pm25=None, pm10=None):
        self.time = time
        self.temp = temp
        self.hum = hum
        self.co2 = co2
        self.pm1 = pm1
        self.pm25 = pm25
        self.pm10 = pm10


