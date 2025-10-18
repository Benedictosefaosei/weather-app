from django.shortcuts import render
from .utils import get_weather_data, get_forecast_data

def index(request):
    city = request.GET.get('city', 'Accra')
    weather_data = get_weather_data(city)
    forecast_data = get_forecast_data(city)
    
    context = {
        'city': city,
        'weather': weather_data,
        'forecast': forecast_data['list'][:5],  # next 5 forecasts
    }
    return render(request, 'main/index.html', context)
