from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"temlplate_app/first.html")

def weather_view(request):
    weather_dictionarry = {
        "istanbul":"30",
        "amsterdam":"50",
        "paris":[10,20,40,50],
        "rome":{"a":30,"b":20,"c":55}
    }
    return render(request,"temlplate_app/weather.html",context=weather_dictionarry)
