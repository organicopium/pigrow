from django.shortcuts import render
from django.http import HttpResponse
import measure



def index(request):
    humidity, temperature = measure.getCurrentMeasures()
    return HttpResponse("temperature {:.2f}°c, humidity {:.2f}%".format(humidity, temperature))
