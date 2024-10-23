from django.shortcuts import render

import urllib.request
import json
import datetime

# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=YOUR_API').read()

        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['name']) + ', '+ str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            'temp': int(list_of_data['main']['temp']),
            'pressure':int(list_of_data['main']['pressure']),
            'humidity':int(list_of_data['main']['humidity']),
            'description': str.title(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
            'feels_like': int(list_of_data['main']['feels_like']),
            'wind_speed': float(list_of_data['wind']['speed']),
            'day': datetime.date.today
        }
        print(data)
    else:
        data = {}
    return render(request, 'index.html', data)
