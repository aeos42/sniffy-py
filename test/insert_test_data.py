import csv
from datetime import datetime
import dateutil.parser
import db
from db import db_session
from models import AirData


def write_test_data():

    with open("test_data.csv") as csv_file:
        db.init_db()
        reader = csv.DictReader(csv_file)
        for row in reader:
            time = dateutil.parser.isoparse(row["time"])
            temp = float(row["temp"])
            hum = float(row["hum"])
            co2 = float(row["co2"])
            pm1 = float(row["pm1"])
            pm25 = float(row["pm25"])
            pm10 = float(row["pm10"])
            data_point = AirData(
                time=time,
                temp=temp,
                hum=hum,
                co2=co2,
                pm1=pm1,
                pm25=pm25,
                pm10=pm10,
            )
            db_session.add(data_point)
            db_session.commit()


if __name__ == "__main__":
    write_test_data()
