import telebot
from telebot import custom_filters
import random
import time
import threading

TOKEN = "8593097818:AAGjuSLMThrjafNj3bM5l7Vby5cku7EpJvU"

bot = telebot.TeleBot(TOKEN)

aturar = threading.Event()

@bot.message_handler(commands=['medeix'])
def enviar_dades(message):
    while not aturar.is_set():
        temperatura = random.randrange(20, 30)
        humitat = random.randrange(50, 70)

        if temperatura > 25 and humitat > 60:
            bot.send_message(message.chat.id, f'T={temperatura} H={humitat}')

        time.sleep(2)

try:
    bot.add_custom_filter(custom_filters.ChatFilter())
    bot.polling(none_stop=True)

except KeyboardInterrupt:
    print("Aturant el bot...")
    aturar.set()
    bot.stop_polling()
    print("Programa finalitzat")
