from django.shortcuts import render
from django.http import HttpResponse
from dht.models import DhtData
from datetime import datetime

def index(request):
    d = DhtData.objects.latest('id')
    TS_FORMAT = '%Y-%m-%d %H:%M:%S'
    ts_formatted = datetime.utcfromtimestamp(float(d.ts)).strftime(TS_FORMAT)
    temperature_f = d.temperature * 1.8 + 32.0
    return HttpResponse("temperature {:.2f}°c, {:-2f}°F; humidity {:.2f}%, at {}".format(d.temperature, temperature_f, d.humidity, ts_formatted))
