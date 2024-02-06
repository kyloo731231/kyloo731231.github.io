from aiogram import Bot, Dispatcher
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telebot
import asyncio
bot = Bot(token='6921668923:AAEE0B2Ee--aWFyE9bJPfPbmPV6QRCLAZAM')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.char.id, 'Приветствую вас в увлекательном мире стиля для ваших любимых мопсов! 🐶💖 Добро пожаловать в "MopsStyle" – ваш идеальный выбор для стильной одежды и аксессуаров для мопсов. 🕺🌈')
bot.polling(none_stope=True)
