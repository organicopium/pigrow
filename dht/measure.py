import sqlite3
from sqlite3 import Error
import time
import datetime

db = "dht_data"

def create_table(conn):
    create_table_query = """ CREATE TABLE IF NOT EXISTS dht_data (
                            id integer PRIMARY KEY,
                            humidity real ,
                            temperature real,
                            ts text
                        );"""
    try:
        c = conn.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)

def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def insertMeasure(conn, measure):
    insert_query = ''' INSERT INTO dht_data(humidity, temperature, ts)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(insert_query, measure)
    conn.commit()

def work():
    conn = create_connection(db)
    while conn is not None:
        create_table(conn)
        import Adafruit_DHT
        sensor = Adafruit_DHT.DHT22
        sensor_pin = 18

        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
        humidity = "{:.2f}".format(humidity)
        temperature = "{:.2f}".format(temperature)
        ts = datetime.datetime.now().timestamp()
        measure = (humidity, temperature, ts)
        insertMeasure(conn, measure)
        print("inserted {}".format(measure))
        time.sleep(1)
    print("Database connection does not exist")


if __name__ == '__main__':
    work()