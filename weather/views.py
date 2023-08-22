from django.shortcuts import render
import requests 
from django.http import JsonResponse
import datetime
import json

# Create your views here.
def getWeather(request):
    city = "Athens"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + "cbec624ef2c60055a21f567c45b3fd47"
    response = requests.get(url).json()
    icon = "https://openweathermap.org/img/w/" + response['weather'][0]['icon'] + ".png"
    return render(request, 'index2.html',{'city': response['name'], 'weather': response['weather'][0]['main'], 'icon': icon, 'temp': response['main']['temp']})

def search(request, city):
    city = city
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + "cbec624ef2c60055a21f567c45b3fd47"
    response = requests.get(url).json()
    icon = "https://openweathermap.org/img/w/" + response['weather'][0]['icon'] + ".png"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(response['coord']['lat']) + "&lon=" + str(response['coord']['lon']) + "&appid=" + "cbec624ef2c60055a21f567c45b3fd47"
    forecast_response = requests.get(forecast_url).json()['list']
    weather_forecast = []
    icon_forecast = []
    temp_forecast = []
    dates = []
    tmp_date = ""
    for i in forecast_response:
        if (tmp_date != datetime.datetime.fromtimestamp(i['dt']).strftime('%A')):
            tmp_date = datetime.datetime.fromtimestamp(i['dt']).strftime('%A')
            dates.append(tmp_date)
            weather_forecast.append(i['weather'][0]['main'])
            icon_forecast.append("https://openweathermap.org/img/w/" + i['weather'][0]['icon'] + ".png")
            temp_forecast.append(i['main']['temp'])
    return render(request, 'index2.html',{'city': response['name'], 'weather': response['weather'][0]['main'], 'icon': icon, 'temp': response['main']['temp'], 'day1' : dates[0], 'w1': weather_forecast[0], 'i1' : icon_forecast[0], 't1' : temp_forecast[0]})
