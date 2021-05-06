import os

import telebot
from core import *
from strings import *
from telebot import types

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)
hideBoard = types.ReplyKeyboardRemove()


class Collect:
    '''Clase para recolectar algunos datos durante la ejecución de la tarea'''

    def __init__(self):
        self.lexer = None
        self.chatid = None


Coll = Collect()


@bot.message_handler(commands=['start', 'tips', 'info'])
def send_welcome(message):
    '''Función que procesa los comandos recibidos'''
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

    elif '/info' in command:
        bot.send_message(Coll.chatid,
                         str_info,
                         parse_mode='Markdown')


def ProcessLexer(message):
    '''Procesar el código (lexer) recibido'''
    lang = message.text
    # Si el lenguaje seleccionado está entre los predeterminados
    if lang in availangs:
        Coll.lexer = lang
        msg = bot.reply_to(message, f'Ok, ahora envíame el código {lang}', reply_markup=hideBoard)
        bot.register_next_step_handler(msg, getCode)
    else:
        CheckLexer = checkLexer(lang)
        if CheckLexer:
            langname = CheckLexer
            msg = bot.reply_to(
                message, f'Ok, ahora envíame el código {langname}', reply_markup=hideBoard)
            Coll.lexer = lang
            bot.register_next_step_handler(msg, getCode)
        else:
            bot.send_message(
                Coll.chatid, 'El código ingresado es erróneo, por favor verifíquelo.', reply_markup=hideBoard)


def getCode(message):
    '''Función que recibe el código (Python, HTML...)'''
    code = message.text
    msgid = message.message_id
    lexer = Coll.lexer

    result = codetoimage(code, lexer)

    bot.send_photo(Coll.chatid,
                   photo=open(f'{result}.png', 'rb'),
                   reply_to_message_id=msgid)

    os.remove(f"{result}.png")


bot.polling()
