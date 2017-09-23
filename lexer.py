import re
from rply import LexerGenerator


lg = LexerGenerator()


lg.add('number', r'\-?[0-9]+')
lg.add('floatnumber', r'\-?[0-9]+\.[0-9]+')
lg.add('plus', r'\+')
lg.add('minus', r'\-')
lg.add('mult', r'\*')
lg.add('true',r'True')
lg.add('false',r'False')
lg.add('ifequals', r'\=\=')
lg.add('ifgreater', r'\>')
lg.add('iflesser', r'\<')
lg.add('ifequalsnot', r'\!\=')
lg.add('if', r'if')
lg.add('codel', r'\{')
lg.add('coder', r'\}')
lg.add('divide', r'/')
lg.add('lpar',r'\(')
lg.add('rpar',r'\)')
lg.add('char', r'char')
lg.add('equals', r'\=')
lg.add('variablenam', r'[A-Za-z]+')
lg.add('string', r'"([^"]*)"')
lg.ignore(r'\s+')

l = lg.build()




def parsetext(text):
    tokenreturn = []
    for token in l.lex(text):
        tokenreturn.append(token)
    return tokenreturn
