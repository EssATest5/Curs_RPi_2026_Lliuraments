import telebot
from telebot import custom_filters
import random

bot = telebot.TeleBot('8911193196:AAE-YhDr7t1WMcbEXuXr8tDIYXIHVVzmbXg')

@bot.message_handler(commands=['temp'])
def enviar_dades(message):
    temperatura = random.randrange(20,30)
    bot.send_message(message.chat.id, f'T={temperatura}')
    
    
@bot.message_handler(commands=['hum'])
def enviar_dades(message):
    humitat = random.randrange(50,70)
    bot.send_message(message.chat.id, f'H={humitat}')


bot.add_custom_filter(custom_filters.ChatFilter())
bot.polling(none_stop=True)
