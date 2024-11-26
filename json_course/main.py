import json
from datetime import datetime, timedelta

#LIRE DES DONNÉES
with open('weather.json', 'r') as file:
    data = json.load(file)
    # 1. Afficher dans la console le taux d’humidité.
humidity_ = data['main']['humidity']
print(f"Humidity: {humidity_}")
# 2. Afficher dans la console les coordonnées, latitude et longitude.
longitude_ = data['coord']['lon']
latitude_ = data['coord']['lat']
print(f"Latitude: {latitude_}, Longitude: {longitude_}")
# 3. Afficher dans la console la vitesse du vent.
wind_speed = data['wind']['speed']
print(f"Wind Speed: {wind_speed} m/s")
# 4. Afficher dans la console le nombre de propriété du dictionnaire “main”.
main_dict = data['main']
count_properties = len(main_dict)
print(f"Number of properties in 'main': {count_properties}")
    
# 5. Afficher dans la console la date du sunset sous le format jj/mm/yyyy.
timestamp_date = data['sys']['sunset']
dt_obj = datetime.fromtimestamp(timestamp_date)
formatted_date = dt_obj.strftime('%d/%m/%Y')
print(f"Sunset date: {formatted_date}")

# ÉCRIRE DES DONNÉES

with open('weather.json', 'r') as original_file:
    modified_data = json.load(original_file)

# 1. Modifier la valeur de “sea_level” en 1156.
modified_data['main']['sea_level'] = 1156

# 2. Supprimer la propriété “description” de “weather”.
if 'weather' in modified_data and isinstance(modified_data['weather'], list):
    for weather_item in modified_data['weather']:
        weather_item.pop('description', None)

# 3. Afficher à quelle date correspond sunrise puis enlever 15 minutes.
sunrise_timestamp = modified_data['sys']['sunrise']
sunrise_datetime = datetime.fromtimestamp(sunrise_timestamp)
sunrise_minus_15 = sunrise_datetime - timedelta(minutes=15)
print(f"Sunrise original: {sunrise_datetime.strftime('%H:%M:%S')}, Sunrise - 15 min: {sunrise_minus_15.strftime('%H:%M:%S')}")

# 4. Ajouter dans “main” la température en Celsius.
if 'temp' in modified_data['main']:
    kelvin_temp = modified_data['main']['temp']
    celsius_temp = kelvin_temp - 273.15
    modified_data['main']['temp_celsius'] = round(celsius_temp, 2)

# 5. Calculer dans le format hh:mm:ss la durée de la journée, puis ajouter cette valeur dans la clef “day_duration” dans “sys”.
sunset_timestamp = modified_data['sys']['sunset']
day_duration:int = datetime.fromtimestamp(sunset_timestamp) - datetime.fromtimestamp(sunrise_timestamp)
modified_data['sys']['day_duration'] = str(day_duration)

# Sauvegarder dans un nouveau fichier
with open('modified_weather.json', 'w') as modified_file:
    json.dump(modified_data, modified_file, indent=4)

print("Modifications in 'modified_weather.json'.")