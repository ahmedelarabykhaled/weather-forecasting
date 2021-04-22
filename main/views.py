from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np
from .getWeather import ModelsPredict
from .includes import Includes
import json
import pickle

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
    tempreture = ModelWeather.PredictTempreture()
    humadity = ModelWeather.predictHumidity()
    loadCover = ModelWeather.predictLoadCover()
    wind = ModelWeather.predictWind()

    summaryarray =  [[0] * 4 for i in range(5)]
    for i in range (5):
        summaryarray[i][0] = tempreture [0][i]
        summaryarray[i][1] = humadity [0][i]
        summaryarray[i][2] = wind  [0][i]
        summaryarray[i][3] = loadCover [0][i]
    summaryWeather = ModelsPredict([] , summaryarray )
    summary = summaryWeather.Summary() 
    return HttpResponse( summary )

def predictWeather(response) :
    ModelWeather = ModelsPredict(days, [])
    tempreture = ModelWeather.PredictTempreture()
    humadity = ModelWeather.predictHumidity()
    loadCover = ModelWeather.predictLoadCover()
    wind = ModelWeather.predictWind()

    summaryarray =  [[0] * 4 for i in range(5)]
    for i in range (5):
        summaryarray[i][0] = tempreture [0][i]
        summaryarray[i][1] = humadity [0][i]
        summaryarray[i][2] = wind  [0][i]
        summaryarray[i][3] = loadCover [0][i]
    summaryWeather = ModelsPredict([] , summaryarray )
    Summary = summaryWeather.Summary()
    weatherResults = [[0] * 5 for i in range(5)]
    for i in range (5):
        weatherResults[i][0] = tempreture [0][i]
        weatherResults[i][1] = humadity [0][i]
        weatherResults[i][2] = wind  [0][i]
        weatherResults[i][3] = loadCover [0][i]
        weatherResults[i][4] = Summary[i]
    return HttpResponse( weatherResults )
