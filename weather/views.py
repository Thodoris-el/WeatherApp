from django.shortcuts import render
import requests 

# Create your views here.
def getWeather(request):
    city = "Athens"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + "cbec624ef2c60055a21f567c45b3fd47"
    response = requests.get(url).json()
    print(response)
    return  