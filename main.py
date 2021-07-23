import os
import telebot


   bot = telebot.TeleBot("1902353429:AAEQluxyYFlU-jDmx11DT0-prZ2RgoYhQW4")

@bot.message_handler(commands=["start"])
def send_welcome(message):
bot.reply_to(massage,"hellow")

@bot.message_handler(commands=["start"])
def send_message(message):
bot.send_message(massage,"hellow"

bot.polling()