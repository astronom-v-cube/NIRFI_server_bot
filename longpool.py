from config import *
from sending_functions import *
import telebot
import psutil
import time
from keyboards import *
import logging
import platform
import subprocess
import os

bot = telebot.TeleBot(main_token)

logging.basicConfig(filename = 'logs.log',  filemode='a', level = logging.INFO, format = ' %(asctime)s - %(levelname)s - %(message)s', encoding = "UTF-8", datefmt='%d-%b-%y %H:%M:%S')
logging.info('Лонгпул запущен...')

if time.time() - psutil.boot_time() < 100:
    for id in users:
        try:
            send(id, f'❗Сервер загружен в ОС {platform.system()}❗', standart_keyboard)
        except:
            logging.info(f'Проблемы с id: {id}')

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() in ['старт', 'начать', 'привет', '/start', 'start']:
        send(message.chat.id, emojize(':robot:'), standart_keyboard)

    elif message.text.lower() in ['статус', emojize("🤖 статус 🤖"), '/status']:
        send(message.chat.id, f'Сервер работает в ОС <b>{platform.system()}</b>', standart_keyboard)

    elif message.text.lower() in ['время', emojize("⏳ время работы ⏳"), '/uptime']:
        uptime_seconds = time.time() - psutil.boot_time()
        send(message.chat.id, f'Сервер работает {int(uptime_seconds // 3600)} ч.', standart_keyboard)

    elif message.text.lower() in [(emojize("📊 мониторинг 📊")), '/monitoring']:
        bot.send_chat_action(message.chat.id, 'typing')
        cpu_percent = psutil.cpu_percent(interval=3)
        memory_percent = psutil.virtual_memory().percent
        send(message.chat.id, f'CPU: {cpu_percent}%, RAM: {memory_percent}%', standart_keyboard)

    elif message.text.lower() in [(emojize("👤 пользователи 👤")), '/users']:
        for user in psutil.users():
            send(message.chat.id, f"👤 {user.name}, авторизован {int((time.time() - user.started)/60)} мин. назад", standart_keyboard)

    elif message.text.lower() in [(emojize("🔗 vpn 🔗")), '/vpn_status']:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', "10.0.0.137"]
        with open(os.devnull, 'w') as devnull:
            if subprocess.call(command, stdout=devnull, stderr=devnull) == 0:
                send(message.chat.id, f"⛔ VPN кем-то занят ⛔", standart_keyboard)
            else:
                send(message.chat.id, f"✅ VPN свободен ✅", standart_keyboard)

    elif message.text.lower() in ['/vpn_key']:
        if message.chat.id in users:
            with open('client.ovpn', 'rb') as document_file:
                send_documents(message.chat.id, document_file, standart_keyboard)
                send(message.chat.id, f'Вот, пожалуйста ☀', standart_keyboard)
        else:
            send(message.chat.id, f'Я вас не знаю... Ваш id не добавлен в систему. Я вам ничего не дам', standart_keyboard)

def job_longpool():
    bot.infinity_polling()