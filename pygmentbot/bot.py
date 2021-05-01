import os

import telebot
from core import *
from strings import *
from telebot import types

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)


class Collect:
    def __init__(self):
        self.lexer = None
        self.chatid = None


Coll = Collect()


@bot.message_handler(commands=['start', 'tips'])
def send_welcome(message):
    command = message.text
    Coll.chatid = message.chat.id

    if '/start' in command:
        markup = types.ReplyKeyboardMarkup(row_width=4,
                                           resize_keyboard=True,
                                           one_time_keyboard=True)

        markup.add(types.KeyboardButton('HTML'),
                   types.KeyboardButton('Python'),
                   types.KeyboardButton('Java'),
                   types.KeyboardButton('PHP'),
                   types.KeyboardButton('C++'),
                   types.KeyboardButton('Go'))

        msg = bot.send_message(Coll.chatid,
                               str_selexer,
                               reply_markup=markup,
                               disable_web_page_preview=True,
                               parse_mode='Markdown')

        bot.register_next_step_handler(msg, ProcessLexer)

    elif '/tips' in command:
        bot.send_message(Coll.chatid,
                         str_tips,
                         parse_mode='Markdown',
                         disable_web_page_preview=True)


def ProcessLexer(message):
    lang = message.text
    # Si el lenguaje seleccionado está entre los predeterminados
    if lang in availangs:
        Coll.lexer = lang
        msg = bot.reply_to(message, f'Ok, ahora envíame el código {lang}')
        bot.register_next_step_handler(msg, getCode)
    else:
        CheckLexer = checkLexer(lang)
        print(checkLexer)
        if CheckLexer:
            msg = bot.reply_to(message, 'Ok, ahora envíame el código')
            Coll.lexer = lang
            bot.register_next_step_handler(msg, getCode)
        else:
            bot.send_message(
                Coll.chatid, 'El lexer ingresado es erroneo, por favor verifíquelo.')


def getCode(message):
    code = message.text
    msgid = message.message_id
    lexer = Coll.lexer

    result = codetoimage(code, lexer)

    bot.send_photo(Coll.chatid,
                   photo=open(f'{result}.png', 'rb'),
                   reply_to_message_id=msgid)

    os.remove(f"{result}.png")


bot.polling()