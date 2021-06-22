#first pip3 install pyTelegramBotApi

import telebot

token="1788777170:AAHTLuWoAULj6Brp_DRl***************"    #your token 
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,'Welcome')
  
@bot.message_handler(commands=['help'])
def send_help(message):
  bot.reply_to(message,"Hello, How may help you?")
  
  
@bot.message_handler(func=lambda message:True)
def send_help(message):
  bot.reply_to(message,message.text)
   
print("Telegram Bot Started ")
print("Press (ctrl+c) To Stop ")

bot.polling()

