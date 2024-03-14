from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn1 = KeyboardButton("Search by city names 🔎")
    btn2 = KeyboardButton("Choose by city names 🏙")
    btn3 = KeyboardButton("Search by location 📍", request_location=True)

    markup.add(btn1, btn2, btn3)

    return markup
def cities():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    NewYork = KeyboardButton('New York')
    Moscow = KeyboardButton('Moscow')
    London = KeyboardButton('London')
    Paris = KeyboardButton('Paris')
    Dubai = KeyboardButton('Dubai')
    Berlin = KeyboardButton('Berlin')
    Warsaw = KeyboardButton('Warsaw')
    Seoul = KeyboardButton('Seoul')
    Mekkah = KeyboardButton('Mekkah')

    markup.add(NewYork, Moscow, London, Paris, Dubai, Berlin, Warsaw, Seoul, Mekkah)
    return markup