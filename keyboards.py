from telebot import types
from emoji import emojize

standart_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
standart_keyboard.add(emojize("🤖 Статус 🤖"), emojize("⏳ Время работы ⏳")).add(emojize("📊 Загруженность 📊")).add(emojize("👤 Пользователи 👤"))

# import psutil
# def check_rdp_sessions():
#     # Получаем список всех пользователей
#     users = psutil.users()

#     # Проверяем, есть ли активные RDP-сессии
#     rdp_sessions = [user for user in users if user.name != 'SYSTEM' and user.terminal == 'rdp-tcp']

#     if rdp_sessions:
#         print("Активные RDP-сессии:")
#         for session in rdp_sessions:
#             print(f"Пользователь: {session.name}, Терминал: {session.terminal}, Время входа: {session.started}")
#     else:
#         print("Нет активных RDP-сессий.")

# check_rdp_sessions()
