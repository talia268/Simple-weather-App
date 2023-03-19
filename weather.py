import requests

# OpenWeatherMap API key
API_KEY = "YOUR_API_KEY_HERE"

# Base URL for API requests
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data for a location
def get_weather_data(city):
    # Complete URL for API request
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    
    # Send API request and store response
    response = requests.get(URL)
    
    # Extract data from response
    data = response.json()
    
    # Check if request was successful
    if data["cod"] != "404":
        # Extract weather information
        weather = data["main"]
        temperature = weather["temp"]
        pressure = weather["pressure"]
        humidity = weather["humidity"]
        
        # Display weather information
        print(f"Temperature: {temperature} K")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        
    else:
        print("Invalid city name.")

# Ask user for city name
city = input("Enter city name: ")

# Get weather data for city
get_weather_data(city)
