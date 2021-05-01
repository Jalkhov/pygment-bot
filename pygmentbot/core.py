import ast
import os
import random
import string

import pygments
from draculatheme import dracula
from pygments import highlight, lexers
from pygments.formatters import BmpImageFormatter


"""
def IsPythonCode(message):
    '''Detect if recived message is a valid Python Code'''
    try:
        ast.parse(message)
    except SyntaxError:
        return False
    return True
"""


def checkLexer(key):
    try:
        lexers.get_lexer_by_name(key)
        return True
    except pygments.util.ClassNotFound:
        return False


def Randname():
    '''Get random name with numbers and chars'''
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


def codetoimage(code, lexer):
    '''Genera la imagen y la guarda localmente'''
    imgname = Randname()
    style1 = dracula.DraculaStyle
    style2 = 'monokai'
    formatter = BmpImageFormatter(
        style=style1, image_format='PNG', line_numbers=False, font_size=16)
    lex = lexers.get_lexer_by_name(lexer)
    highlight(code, lex, formatter, f'{imgname}.png')
    return imgname


"""
def autopep8(code):
    return code
"""


def DoWork(code, lexer):
    #formatted = autopep8(code)
    return(codetoimage(code, lexer))
