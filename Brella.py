import discord
from discord.ext import commands
import os ,dotenv, requests
import datetime as date

dotenv.load_dotenv()
#Intents are like permissions
intents = discord.Intents.all()

#bot here is an instance of the discord bot
bot = commands.Bot(command_prefix = "!", intents=intents)

BASEURL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY  = os.getenv("WEATHER_API")

def create_url(CITY, BASEURL = BASEURL, API_KEY = API_KEY):
        url = BASEURL + "appid=" + API_KEY + "&q=" + CITY
        return url

def create_response(CITY):
        response = requests.get(create_url(CITY)).json()
        return response

def kelvin_to_fahrenheit(temp_kelvin):
        faren = (((temp_kelvin - 273.15)*9)/5) +32
        return round(faren, 2)

def kelvin_to_celcius(temp_kelvin):
        return round(temp_kelvin - 273.15, 2)


#This considers booting the bot as an event and displays the info if the bot booted successfully
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

"""The functinality of the bot are implemented with the following syntax:
@bot.command()
async funct
"""


#ctx is like context for the message. It stores the info regarding the passed message in the channel in which the bot is used

@bot.command()
async def skills(ctx):
    message = """
    My functionalities:
    1. hello
    2. about_u
    3. temp_at
    4. weather_at
    5. type_of_day"""
    await ctx.send(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name} :)")

@bot.command()
async def about_u(ctx):
    await ctx.send("I'm just a bot who will act as your umbrella ;)")

@bot.command()
async def temp_at(ctx, city):
    BASEURL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY  = os.getenv("WEATHER_API")
    CITY = city

    '''def kelvin_to_fahrenheit(temp_kelvin):
        faren = (((temp_kelvin - 273.15)*9)/5) +32
        return round(faren, 2)


    def kelvin_to_celcius(temp_kelvin):
        return round(temp_kelvin - 273.15, 2)'''

#url = BASEURL + "appid=" + API_KEY + "&q=" + CITY
    response = create_response(CITY)

    temp_kelvin = response['main']['temp']
    await ctx.send(f"The temperature at {city.capitalize()} is {kelvin_to_celcius(temp_kelvin)}C or {kelvin_to_fahrenheit(temp_kelvin)}F")

@bot.command()
async def weather_at(ctx, place):
    response = create_response(place)
    clouds = response['weather'][0]['description']
    humidity = response['main']['humidity']
    windspeed = response['wind']['speed']

    await ctx.send(f"Currently in {place.capitalize()} \nCloud status: {clouds}\nHumidity: {humidity}\nWindspeed: {windspeed} km/h")

@bot.command()
async def type_of_day(ctx, place):
     def kelvin_to_celcius(temp_kelvin):
        return round(temp_kelvin - 273.15, 2)
     response = create_response(place)
     temp = kelvin_to_celcius(response['main']['temp'])
     clouds = response['weather'][0]['description']
     humidity = response['main']['humidity']

     



     



bot.run(os.getenv("TOKEN"))

