from django.urls import path
from . import views
urlpatterns = [
    path('country/',views.getWeather,name="getWeather"),  
    path('search/<str:city>/',views.search,name="search")
]