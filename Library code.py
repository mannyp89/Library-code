import requests  # Import the requests library

api_key = "8b1440df0dcf03b0d8a1cefd1c4c7186"
city = "Malvern"

# Create the URL to fetch weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Make a GET request to the OpenWeather API
response = requests.get(url)

 
# Check if successful
if response.status_code == 200:
    data = response.json()  # Convert the response to JSON format
    # Extract temperature and weather condition
    temp_kelvin = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_kelvin - 273.15) * (9/5) + 32
    
    print(f"Weather in {city}: {weather_desc}, Temp: {temp_fahrenheit:.2f}°F")
else:
    print("Error fetching data.")  # Print error message if request failed
