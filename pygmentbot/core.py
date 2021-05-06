import random
import string

import pygments
from draculatheme import dracula
from pygments import highlight, lexers
from pygments.formatters import BmpImageFormatter


def checkLexer(key):
    '''Verifica si el código (lexer) recibido existe en Pygments'''
    try:
        lex = lexers.get_lexer_by_name(key)
        return lex.name
    except pygments.util.ClassNotFound:
        return False


def Randname():
    '''Genera un nombre al azar destinado a las imágenes generadas'''
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


def codetoimage(code, lexer):
    '''Genera la imagen y la guarda localmente'''
    imgname = Randname()
    style1 = dracula.DraculaStyle
    formatter = BmpImageFormatter(
        style=style1, image_format='PNG', line_numbers=False, font_size=16)
    lex = lexers.get_lexer_by_name(lexer)
    highlight(code, lex, formatter, f'{imgname}.png')
    return imgname


def DoWork(code, lexer):
    '''Empieza todo el trabajo'''
    return(codetoimage(code, lexer))
