from keyboards import standart_keyboard
from config import *
import telebot
import logging

bot = telebot.TeleBot(main_token)

def send(user_id, msg, keyboard):

    logging.info(f'Ответил: "{msg}" пользователю с id: {user_id}')
    return bot.send_message(user_id, msg, reply_markup = keyboard, parse_mode='html')

def send_attachment(user_id, image, keyboard):

    logging.info(f'Отправил фото пользователю с id: {user_id}')
    return bot.send_photo(user_id, image, reply_markup = keyboard)

def send_documents(user_id, document, keyboard):

    logging.info(f'Отправил документ пользователю с id: {user_id}')
    return bot.send_document(user_id, document, reply_markup=keyboard)