from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
import requests
from datetime import datetime

from buttons import main_menu, cities

api_key = '3b502459ad3dac3cb3eeb8d9637e5e07'
parameters = {
    'appid': api_key,
    'units': 'metric'
}

bot = TeleBot('7157820108:AAEE0z9gNw9hJYp4dnvGi-4X4wuLAEB93yg', parse_mode='html')
@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id,f'Hi, {full_name} \n'
                             f'Welcome to <b>Weather bot</b> ', reply_markup=main_menu())

def get_data(message: Message):
    chat_id = message.chat.id
    parameters['q'] = message.text
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?', params=parameters).json()
    get_info(weather, chat_id)

def get_info(weather: Message, chat_id):
    print(weather)
    city = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    hum = weather['main']['humidity']
    wind = weather['wind']['speed']
    sunrise = datetime.utcfromtimestamp(weather['sys']['sunrise']+weather['timezone']).strftime('%H:%M')
    sunset = datetime.utcfromtimestamp(weather['sys']['sunset']+weather['timezone']).strftime('%H:%M')
    text = (f"Weather condition in {city} is {desc} \n"
            f"Temperature: {temp} C\n"
            f"Wind speed: {wind}\n"
            f"Humidity: {hum} %\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}")
    bot.send_message(chat_id, text, reply_markup=main_menu())

@bot.message_handler(regexp="Search by city names 🔎")
def text(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Input city name", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_data)

@bot.message_handler(regexp="Choose by city names 🏙")
def get_city(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Cities', reply_markup=cities())

@bot.message_handler(func=lambda message: message.text in ['New York', 'Moscow', 'London', 'Paris', 'Dubai', 'Berlin', 'Warsaw', 'Seoul', 'Mekkah'])
def cityby(message:Message):
    get_data(message)

@bot.message_handler(content_types=['location'])
def location(message: Message):
    chat_id = message.chat.id
    lat = message.location.latitude
    lon = message.location.longitude
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric').json()
    get_info(weather, chat_id)









if __name__ == '__main__':
    bot.infinity_polling()



