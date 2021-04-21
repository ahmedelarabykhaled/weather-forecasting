from django.shortcuts import render

from django.http import HttpResponse


import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional
from keras.models import load_model
import numpy as np
from .getWeather import ModelsPredict
import os

# path = r"D:\Ahmed Khaled\graduation project\django project\WeatherForecasting\main"
path = os.path.abspath(os.path.dirname(__file__))

def index(response) :
    # predict = ModelsPredict(,[])
    return HttpResponse(path +
        '<div style="display:flex;justify-content:center;align-items:center;height:500px;flex-direction:column;"><h1 style="font-size:6em;font-family: \'Roboto\', sans-serif;">Home Page</h1><p style="font-family: \'Open Sans\', sans-serif;">Ahmed Khaled</p></div>')

def home(response) :
    return HttpResponse("welcome here form the home page")


def test(response) :
    dataset = pd.read_csv(path+'\weatherHistory.csv')
    final_summary = pd.DataFrame(dataset)
    unique_values = final_summary.Summary.unique()
    final_summary.Summary = pd.Categorical(final_summary.Summary)
    final_summary['summary_code'] = final_summary.Summary
    final_summary['Summary'] = final_summary.Summary.cat.codes
    final_precip_type = pd.DataFrame(dataset)
    unique_values_precip_types = final_precip_type['Precip Type'].unique()
    final_precip_type['Precip Type'] = pd.Categorical(final_precip_type['Precip Type'])
    final_precip_type['precip_type'] = final_precip_type['Precip Type']
    final_precip_type['Precip Type'] = final_precip_type['Precip Type'].cat.codes
    tempreature_training_set = final_precip_type.iloc[:,1:11]

    tempreature_training_set = np.array(tempreature_training_set)
    days = tempreature_training_set[:, 0:11]
    ModelWeather = ModelsPredict(days , [])
    tempreature = ModelWeather.PredictTempreture()
    return HttpResponse(tempreature)
