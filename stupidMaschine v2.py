import telebot
import logging
from telebot import types

bot = telebot.TeleBot("1087470565:AAHKtxzBruFyG2uQDb5cv97uS-5lHvJohSs")

#user = bot.get_me() #it is a dict

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, message.from_user.first_name)

bot.polling(none_stop=True)