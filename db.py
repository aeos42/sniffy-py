from datetime import datetime
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///air.db')
models.Base.metadata.create_all(engine)

testRecord = models.AirData(time=datetime.now(
), temp=40.2, hum=3.2, co2=30.2, pm1=23.1, pm25=30.2, pm10=87.21)
print(testRecord.time)

Session = sessionmaker(bind=engine)
session = Session()

session.add(testRecord)
session.commit()

