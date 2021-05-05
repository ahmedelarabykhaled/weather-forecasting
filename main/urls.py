from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("predictTempreture",views.predictTempreture, name="predictTempreture"),
    path("predictHumidity",views.predictHumidity, name="predictHumidity"),
    path("predictLoadCover",views.predictLoadCover, name="predictLoadCover"),
    path("predictWind",views.predictWind, name="predictWind"),
    path("predictSummery",views.predictSummery, name="predictSummery"),
    path("predictWeather",views.predictWeather, name="predictWeather"),
]