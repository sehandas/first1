import os
import telebot


bot = telebot.TeleBot("1902353429:AAEQluxyYFlU-jDmx11DT0-prZ2RgoYhQW4")

@bot.massage_handler(commands=["start"])
def send_welcome(message):
bot.reply_to(massage,"hellow")

bot.polling()