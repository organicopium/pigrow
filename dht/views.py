from django.shortcuts import render
from django.http import HttpResponse
from dht.models import DhtData


def index(request):
    d = DhtData.objects.latest('id')
    TS_FORMAT = '%Y-%m-%d %H:%M:%S'
    ts_formatted = datetime.utcfromtimestamp(d.ts).strftime(TIME_FORMAT)
    return HttpResponse("temperature {:.2f}°c, humidity {:.2f}%, at {}".format(d.temperature, d.humidity, ts_formatted))
