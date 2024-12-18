from django.shortcuts import render
from decouple import config

# Create your views here.
from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather

API_KEY = config("API_KEY")

def weather_view(request):
    weather_data = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            weather_data = get_weather(city, API_KEY)
    else:
        form = CityForm()
    return render(request, "weather/weather.html", {"form": form, "weather_data": weather_data})
