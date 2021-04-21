from django.shortcuts import render

from django.http import HttpResponse

from .includes.getWeather import ModelsPredict


# Create your views here.


def index(response) :
    predict = ModelsPredict()
    return HttpResponse(
        '<div style="display:flex;justify-content:center;align-items:center;height:500px;flex-direction:column;"><h1 style="font-size:6em;font-family: \'Roboto\', sans-serif;">Home Page</h1><p style="font-family: \'Open Sans\', sans-serif;">Ahmed Khaled</p></div>')

def home(response) :
    return HttpResponse("welcome here form the home page")