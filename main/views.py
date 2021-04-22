from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np
from .getWeather import ModelsPredict
# import os
from .includes import Includes
import json

# path = r"D:\Ahmed Khaled\graduation project\django project\WeatherForecasting\main"
# path = os.path.abspath(os.path.dirname(__file__))

days = Includes().getDays()

def index(response) :
    # predict = ModelsPredict(,[])
    return HttpResponse(
        '<div style="display:flex;justify-content:center;align-items:center;height:500px;flex-direction:column;"><h1 style="font-size:6em;font-family: \'Roboto\', sans-serif;">Home Page</h1><p style="font-family: \'Open Sans\', sans-serif;">Ahmed Khaled</p></div>')

def predictTempreture(response) :
    ModelWeather = ModelsPredict(days , [])
    tempreature = ModelWeather.PredictTempreture()
    return HttpResponse(tempreature)

def predictHumidity(response) : 
    ModelWeather = ModelsPredict(days, [])
    Humadity = ModelWeather.predictHumidity()
    return HttpResponse( Humadity )

def predictLoadCover(response) :
    ModelWeather = ModelsPredict(days, [])
    loadCover = ModelWeather.predictLoadCover()
    return HttpResponse( loadCover )

def predictWind(response) :
    ModellWeather = ModelsPredict(days, [])
    wind = ModellWeather.predictWind()
    return HttpResponse( wind )

def predictSummery(response) :
    ModelWeather = ModelsPredict(days, [])
    summery = ModelWeather.Summary()
    return HttpResponse( summery )
