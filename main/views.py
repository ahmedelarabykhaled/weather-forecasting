from django.shortcuts import render

from django.http import HttpResponse

from .includes.getWeather import ModelsPredict
import pandas as pd

# Create your views here.

def prepare_dataset() :
    dataset = pd.read_csv('includes/models/weatherHistory.csv')
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


last_dataset = prepare_dataset()


def index(response) :
    # predict = ModelsPredict(,[])
    return HttpResponse(
        '<div style="display:flex;justify-content:center;align-items:center;height:500px;flex-direction:column;"><h1 style="font-size:6em;font-family: \'Roboto\', sans-serif;">Home Page</h1><p style="font-family: \'Open Sans\', sans-serif;">Ahmed Khaled</p></div>')

def home(response) :
    return HttpResponse("welcome here form the home page")