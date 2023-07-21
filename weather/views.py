from django.shortcuts import render
import requests 

# Create your views here.
def getWeather(request):
    city = "Athens"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + "cbec624ef2c60055a21f567c45b3fd47"
    response = requests.get(url).json()
    icon = "https://openweathermap.org/img/w/" + response['weather'][0]['icon'] + ".png"
    print(response)
    return render(request, 'index2.html',{'city': response['name'], 'weather': response['weather'][0]['main'], 'icon': icon, 'temp': response['main']['temp']})