import requests

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "40e85b41c5e09f1fd685ee0f9ba0d2a7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# User se city name input lena
city = input("Enter city name: ")

# API request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# API se data fetch karna
response = requests.get(url)
data = response.json()

# Debugging output
print(f"Response Code: {response.status_code}")
print(f"Response Data: {data}")

# Data check karna
if data.get("cod") == 200:
    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Output print karna
    print(f"\n🌍 Location: {city_name}, {country}")
    print(f"🌡 Temperature: {temperature}°C")
    print(f"☁️ Weather: {weather_description}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")

else:
    print("❌ Error: City not found! Please enter a valid city name.")
