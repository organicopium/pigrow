from django.shortcuts import render
from django.http import HttpResponse
from dht import measure



def index(request):
    #TODO read from db and respond
    return HttpResponse("temperature {:.2f}°c, humidity {:.2f}%".format(-1, -1))
