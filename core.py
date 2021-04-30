import ast
import os
import random
import string

from draculatheme import dracula
from pygments import highlight, lexers
from pygments.formatters import BmpImageFormatter


def IsPythonCode(message):
    '''Detect if recived message is a valid Python Code'''
    try:
        ast.parse(message)
    except SyntaxError:
        return False
    return True


def Randname():
    '''Get random name with numbers and chars'''
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


def codetoimage(code):
    '''Genera la imagen y la guarda localmente'''
    imgname = Randname()
    style1 = dracula.DraculaStyle
    style2 = 'monokai'
    formatter = BmpImageFormatter(
        style=style2, image_format='PNG', line_numbers=False, font_size=16)
    lex = lexers.get_lexer_by_name("python")
    highlight(code, lex, formatter, f'{imgname}.png')
    return imgname


def autopep8(code):
    return code


def DoWork(message):
    if IsPythonCode(message):
        code = message
        formatted = autopep8(code)
        return(codetoimage(formatted))
    else:
        return False
