import sqlite3
from sqlite3 import Error
import time
import datetime

db = "/home/pi/projects/pigrow/db.sqlite3"

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
    import Adafruit_DHT
    sensor = Adafruit_DHT.DHT22
    sensor_pin = 18
    while True:
        conn = create_connection(db)
        create_table(conn)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
        ts = datetime.datetime.now().timestamp()
        measure = (humidity, temperature, ts)
        insertMeasure(conn, measure)
        print("inserted {}".format(measure))
        conn.close()
        time.sleep(20)
    print("Database connection does not exist")

if __name__ == '__main__':
    work()
