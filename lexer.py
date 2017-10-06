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
lg.add('while', r'while')
lg.add('infinite', r'inf')
lg.add('functiondef', r'fun')
lg.add('functionbind', r'@')
lg.add('timedloop', r'tloop')
lg.add('codeblock', r'({.*?}\|)')
lg.add('specialcodeblock', r'({.*?}\/)')
lg.add('divide', r'/')
lg.add('lpar',r'\(')
lg.add('rpar',r'\)')
lg.add('lcod',r'\[')
lg.add('rcod',r'\]')
lg.add('char', r'char')
lg.add('equals', r'\=')
lg.add('variablenam', r'[A-Za-z]+')
lg.add('string', r'"([^"]*)"')
lg.ignore(r'\s+')
lg.ignore(r';+')
lg.ignore(r',+')

l = lg.build()




def parsetext(text):
    tokenreturn = []
    for token in l.lex(text):
        tokenreturn.append(token)
    return tokenreturn
