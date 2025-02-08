import requests

def get_weather(city):
    api_key= "9ba3e662d7909fe574f468c26f3c2c48"
    base_url= "http://api.openweathermap.org/data/2.5/weather?"
    complete_url=f"{base_url}q={city}&appid={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
        
        return {
            'temperature' : round(temperature_celsius,2),
            'pressure' : main['pressure'],
            'humidity' : main['humidity'],
            'wind_speed' : wind['speed'],
            'description' : weather_description
        }
    else:
        return None

if __name__ == "__main__":
    city = input("Enter City name")
    # city = 'Kolkata'
    weather = get_weather(city)
    
    if weather:
        print(f"The Weather data of {city}")
        print(f"Temperature : {weather['temperature']} °C")
        print(f"Pressure : {weather['pressure']} hPa")
        print(f"Humidity : {weather['humidity']} %")
        print(f"Wind Speed : {weather['wind_speed']} ms")
        print(f"Description : {weather['description']}")
    else:
        print("City not Found")
        