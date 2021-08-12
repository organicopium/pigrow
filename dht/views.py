from django.shortcuts import render
from django.http import HttpResponse
from dht.models import DhtData
from datetime import datetime

def index(request):
    d = DhtData.objects.latest('id')
    TS_FORMAT = '%Y-%m-%d %H:%M:%S'
    ts_formatted = datetime.utcfromtimestamp(float(d.ts)).strftime(TS_FORMAT)
    return HttpResponse("{}: temperature {:.2f}°c, humidity {:.2f}%".format(ts_formatted, d.temperature, d.humidity))
