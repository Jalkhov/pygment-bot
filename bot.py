"""
1628395980:AAHZJERtoZW3ieydpRkuffnwPyyM2BgcKjg
https://core.telegram.org/bots/api

https://api.telegram.org/bot1628395980:AAHZJERtoZW3ieydpRkuffnwPyyM2BgcKjg/getMe
https://api.telegram.org/bot1628395980:AAHZJERtoZW3ieydpRkuffnwPyyM2BgcKjg/getUpdates
"""

import os

#import redis
import telebot
from core import *
from strings import *

token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))


TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'tips'])
def send_welcome(message):

    command = message.text
    chatid = message.chat.id

    if '/start' in command:
        msg = bot.reply_to(message, str_start)
        bot.register_next_step_handler(msg, getCode)
    elif '/tips' in command:
        bot.send_message(chatid, str_tips, parse_mode='Markdown',
                         disable_web_page_preview=True)


def getCode(message):
    msg = message.text
    chatid = message.chat.id

    result = DoWork(msg)
    if result:
        bot.send_photo(chatid, photo=open(f'{result}.png', 'rb'))
        os.remove(f"{result}.png")
        #message.deleteMessage(message.chat.id, message.id)

        #bot.reply_to(message, message.text)
'''
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    chatid = message.chat.id

    result = DoWork(msg)
    if result:
        bot.send_photo(chatid, photo=open(f'{result}.png', 'rb'))
        #bot.deleteMessage(message.chat.id, message.id)
        #bot.reply_to(message, message.text)
'''

bot.polling()
