from django.shortcuts import render
from django.http import HttpResponse

import Adafruit_DHT




def index(request):
    humidity, temperature = getCurrentMeasures()
    return HttpResponse("temperature {:.2f}°c, humidity {:.2f}%".format(humidity, temperature))

def getCurrentMeasures():
    sensor = Adafruit_DHT.DHT22
    ensor_pin = 18
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    return humidity, temperature
