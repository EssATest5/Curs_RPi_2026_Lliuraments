import time
import random
import threading
import telebot

TOKEN = "8593097818:AAGjuSLMThrjafNj3bM5l7Vby5cku7EpJvU"

# Dades compartides entre els threads
temperatura = 0
humitat = 0


# Protegeix l'accés concurrent a les dades
lock = threading.Lock()

# 1. Creació del bot: fil principal
bot = telebot.TeleBot(TOKEN)



# 2. Registre dels gestors: fil principal
@bot.message_handler(commands=["temp"])
def enviar_temperatura(message):
    
    bot.send_message(message.chat.id,f"Temp ={temperatura} ºC"
    )


@bot.message_handler(commands=["hum"])
def enviar_humitat(message):

    bot.send_message(message.chat.id, f"Hum ={humitat} %"
    )


# 3. Funció d'adquisició: s'executarà en un altre thread
def adquirir_dades():
    global humitat
    global temperatura
    while True:
        # Simulació de lectura dels sensors
        with lock:
            temperatura = random.randrange(20, 30)
            humitat = random.randrange(50, 70)



        time.sleep(5)


# 4. Creació i inici del thread d'adquisició
thread_sensors = threading.Thread(
    target=adquirir_dades,
    daemon=True
)
thread_sensors.start()

# 5. El fil principal queda atenent Telegram
bot.infinity_polling()
