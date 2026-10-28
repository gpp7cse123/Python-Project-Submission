import requests
city = input("Enter city name: ")

# Get city coordinates
url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name": city, "count": 1}

data = requests.get(url, params=params).json()

if "results" in data:
    place = data["results"][0]
    lat = place["latitude"]
    lon = place["longitude"]

    # Get weather data
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    weather = requests.get(url, params=params).json()
    current = weather["current"]

    print("\n--- Weather Report ---")
    print("City:", place["name"])
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")

else:
    print("City not found!")