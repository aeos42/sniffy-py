import datetime
from flask import Flask
from flask import request

app = Flask(__name__)

# PM1, 2.5, 10
# temp, humidity, c02


@app.route('/temperature')
def get_temperature():
    string_datetime = str(datetime.datetime.now().isoformat())
    temp = {string_datetime: 68.2}
    return temp


@app.route('/humidity')
def get_humidity():
    string_datetime = str(datetime.datetime.now().isoformat())
    humidity = {string_datetime: 48.2}
    return humidity


@app.route('/PM25')
def get_pm25():
    # micrometers per cubic meter?
    string_datetime = str(datetime.datetime.now().isoformat())
    pm25 = {string_datetime: 73.2}
    return pm25
