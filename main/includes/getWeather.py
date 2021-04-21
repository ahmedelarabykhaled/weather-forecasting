import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional
from keras.models import load_model
import pickle



class ModelsPredict :
    def __init__(self , days , summaryArray):
      self.days = days
      self.summaryArray = summaryArray


    def PredictTempreture (self):
      np_days = self.days
      temp_days = np.array(np_days)
      temp_days = np.reshape(temp_days, (1, temp_days.shape[0], 10))
      tempreature = load_model('models/modeltemptraing.h5')
      predicted_Tempreature = tempreature.predict(temp_days)
      return predicted_Tempreature

    def predictHumidity (self):
      np_days = self.days
      humd_days = np.array(np_days)
      humd_days = np.reshape(humd_days, (1, humd_days.shape[0], 10))
      humidity = load_model('models/modeltrainghumidity.h5')
      predicted_Humidity = humidity.predict(humd_days)
      return predicted_Humidity

    
    def predictLoadCover (self) : 
      np_days = self.days
      load_days = np.array(np_days)
      load_days = np.reshape(load_days, (1, load_days.shape[0], 10))
      load_cover = load_model('models/modeltraingLoadCover.h5')
      predicted_LoadCover = load_cover.predict(load_days)
      return predicted_LoadCover

    def predictWind (self) :
      np_days = self.days 
      wind_days = np_days [: , 5:7]
      wind_days = np.array(wind_days)
      wind_days = np.reshape(wind_days, (1, wind_days.shape[0], 2))
      wind = load_model('models/modelwindtraing.h5')
      predicted_Wind = wind.predict(wind_days)
      return predicted_Wind

    def Summary (self):
      summary_Array = np.array(self.summaryArray)
      summary_model = pickle.load(open('models/summary.h5', 'rb'))
      summaryResult = summary_model.predict(summary_Array)
      return summaryResult


















