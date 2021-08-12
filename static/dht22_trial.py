import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
sensor_pin = 18

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    print("humidity: {}, temperature {}".format(humidity, temperature))