import requests
def main():
    weather_api()
def weather_api():    
    api_key = 'YOUR KEY',#replace with your key
    city = 'Puducherry' # default city
    message = ''
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url).json()
    if response['cod'] == 200:
        weather = response['weather'][0]['description']
        temp = response['main']['temp']
        feels_like = response['main']['feels_like']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        message = f'The weather in {city}: {weather}, Temperature: {temp}°C, Feels like: {feels_like}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s'
        return message  
    else:
        message = 'Sorry, could not fetch weather information for ' + city + ' at the moment.'
        return message
if __name__=="__main__":
    main()