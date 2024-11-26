import json
from datetime import datetime


# Lire le fichier weather.json
with open('weather.json', 'r') as file:
    weather_data:dict = json.load(file)

# 1.
print(weather_data['main']['humidity'])

# 2.
print(weather_data['coord'])

# 3.
print(weather_data['wind']['speed'])

# 4.
print(len(weather_data['main']))

# 5.
date_sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
date_sunset_str = date_sunset.strftime("%d/%m/%Y")
print(date_sunset_str)


# II. Écrire des données

# 1.
weather_data['main']['sea_level'] = 1156

# 2.
del weather_data['weather'][0]['description']
# weather_data['weather'][0].pop('description')

# 3.
MINUTES = 15
weather_data['sys']['sunrise'] -= MINUTES * 60
date_sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
date_sunrise_str = date_sunrise.strftime("%d/%m/%Y %H:%M:%S")
print(date_sunrise_str)

# 4.
def kelvin_to_celsius(kelvin_temp:float, precision:int=2) -> float:
    ABSOLUTE_ZERO = 273.15
    return round(kelvin_temp - ABSOLUTE_ZERO, precision)

weather_data['main']['celsius_temp'] = kelvin_to_celsius(weather_data['main']['temp'])
weather_data['main']['celsius_temp_min'] = kelvin_to_celsius(weather_data['main']['temp_min'])
weather_data['main']['celsius_temp_max'] = kelvin_to_celsius(weather_data['main']['temp_max'])


# 5.
day_duration_timestamp:int = weather_data['sys']['sunset'] - weather_data['sys']['sunrise']
day_duration_datetime = datetime.fromtimestamp(day_duration_timestamp)
day_duration_str = day_duration_datetime.strftime("%H:%M:%S")
print(day_duration_str)

with open('weather_updated.json', 'w') as file:
    json_object = json.dumps(weather_data, indent=4)
    file.write(json_object)