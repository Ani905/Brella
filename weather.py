import datetime as date
import requests, os, dotenv

dotenv.load_dotenv()

BASEURL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY  = os.getenv("WEATHER_API")
CITY = input("Enter city: ")

def kelvin_to_fahrenheit(temp_kelvin):
    faren = (((temp_kelvin - 273.15)*9)/5) +32
    return faren


def kelvin_to_celcius(temp_kelvin):
    return temp_kelvin - 273.15

def create_url(CITY, BASEURL = BASEURL, API_KEY = API_KEY):
    url = BASEURL + "appid=" + API_KEY + "&q=" + CITY
    return url

def create_response(CITY):
    response = requests.get(create_url(CITY)).json()
    return response


#url = BASEURL + "appid=" + API_KEY + "&q=" + CITY

response = create_response(CITY)
print(response)

temp_kelvin = response['main']['temp']

clouds = response['weather'][0]['description']
humidity = response['main']['humidity']

print(temp_kelvin, 'K')
print(round( kelvin_to_celcius(temp_kelvin), 2), "C")
print(round( kelvin_to_fahrenheit(temp_kelvin), 2), "F")
print(clouds, humidity)

"""'coord': {'lon': 76.7, 'lat': 11.4}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 286.6, 'feels_like': 285.36, 'temp_min': 286.6, 'temp_max': 286.6, 'pressure': 1014, 'humidity': 52, 'sea_level': 1014, 'grnd_level': 782}, 'visibility': 10000, 'wind': {'speed': 0.8, 'deg': 156, 'gust': 2.19}, 'clouds': {'all': 15}, 'dt': 1678628186, 'sys': {'country': 'IN', 'sunrise': 1678582960, 'sunset': 1678626226}, 'timezone': 19800, 'id': 1253993, 'name': 'Ooty', 'cod': 200}"""