import csv
import datetime
import random

# day of records
records = 86_400
fieldnames = ["time", "temp", "hum", "co2", "pm1", "pm25", "pm10"]
init_time = datetime.datetime(2020, 6, 1, 0, 0, 0, 0)


def generate_data():
    csv_writer = csv.DictWriter(open("test_data.csv", "w"), fieldnames=fieldnames)
    csv_writer.writerow(dict(zip(fieldnames, fieldnames)))
    current_time = init_time
    for i in range(0, records):
        current_time = current_time + datetime.timedelta(seconds=1)
        row = dict(
            [
                ("time", current_time.isoformat()),
                ("temp", "%.1f" % random.uniform(32.5, 90.2)),
                ("hum", "%.1f" % random.uniform(0.0, 100.0)),
                ("co2", "%.1f" % random.uniform(0.0, 54.2)),
                ("pm1", "%.1f" % random.uniform(0.0, 500.0)),
                ("pm25", "%.1f" % random.uniform(0.0, 500.0)),
                ("pm10", "%.1f" % random.uniform(0.0, 500.0)),
            ]
        )
        csv_writer.writerow(row)


if __name__ == "__main__":
    generate_data()
