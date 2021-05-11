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
    tempreture_list = tempreature.tolist()
    return HttpResponse(json.dumps(tempreture_list[0]), content_type ="application/json")

def predictHumidity(response) : 
    ModelWeather = ModelsPredict(days, [])
    Humadity = ModelWeather.predictHumidity()
    humadity_list = Humadity.tolist()
    return HttpResponse( json.dumps(humadity_list), content_type ="application/json")

def predictLoadCover(response) :
    ModelWeather = ModelsPredict(days, [])
    loadCover = ModelWeather.predictLoadCover()
    loadCover_list = loadCover.tolist()
    return HttpResponse( json.dumps(loadCover_list) , content_type = "application/json" )

def predictWind(response) :
    ModellWeather = ModelsPredict(days, [])
    wind = ModellWeather.predictWind()
    wind_list = wind.tolist()
    return HttpResponse( json.dumps(wind_list[0]) , content_type = "application/json" )

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
    summary_list = summary.tolist()
    return HttpResponse( json.dumps(summary_list) , content_type="application/json" )

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

    tempreture = tempreture.tolist()
    humadity = humadity.tolist()
    loadCover = loadCover.tolist()
    wind = wind.tolist()
    Summary = Summary.tolist()

    weatherResults = [[0] * 5 for i in range(5)]
    for i in range (5):
        weatherResults[i][0] = tempreture [0][i]
        weatherResults[i][1] = humadity [0][i]
        weatherResults[i][2] = wind  [0][i]
        weatherResults[i][3] = loadCover [0][i]
        weatherResults[i][4] = Summary[i]
    weatherResults = np.array(weatherResults).tolist()
    return HttpResponse( json.dumps(weatherResults) , content_type = "application/json" )

def testPrediction(response) :
    model = ModelsPredict(days, [])
    testPredict = model.WeatherResults()
    testPredictList = testPredict.tolist()
    return HttpResponse( json.dumps( str(testPredictList) ) , content_type = "application/json" )
