import datetime
import dateutil.parser
from flask import Flask
from flask import request

import db
from db import db_session
from models import AirData

db.init_db()

app = Flask(__name__)
DATA_POINTS = ("temp", "hum", "co2", "pm1", "pm25", "pm10")


def get_data_point(point, start_time, end_time):
    if point not in DATA_POINTS:
        raise ValueError

    air_data = []
    for time, pt in (
        db_session.query(AirData.time, getattr(AirData, point))
        .filter(AirData.time >= start_time)
        .filter(AirData.time <= end_time)
    ):
        air_data.append({"time": time, point: pt})

    air_data = {"points": air_data}
    return air_data


@app.route("/temperature")
def get_temperature():
    start_time = dateutil.parser.isoparse(request.args.get("start"))
    end_time = dateutil.parser.isoparse(request.args.get("end"))
    data = get_data_point("temp", start_time, end_time)
    return data


@app.route("/humidity")
def get_humidity():
    string_datetime = str(datetime.datetime.now().isoformat())
    humidity = {string_datetime: 48.2}
    return humidity


@app.route("/PM25")
def get_pm25():
    # micrometers per cubic meter?
    string_datetime = str(datetime.datetime.now().isoformat())
    pm25 = {string_datetime: 73.2}
    return pm25

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()