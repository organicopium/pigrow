import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
sensor_pin = 18

def getCurrentMeasures():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    return humidity, temperature