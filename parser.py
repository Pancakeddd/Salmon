import lexer as lexr
from rply.token import BaseBox
from rply import ParserGenerator



pg = ParserGenerator(
    ['number',
     'equals', 'variablenam','string','plus','minus','mult','divide','codeblock',"colon",
     'ifequals','ifgreater','iflesser','if','codel','coder',
     'ifequalsnot','true','false'
    ]
)


@pg.error
def error_handler(token):
    raise ValueError("Unexpected {0}, {1}.".format(token.gettokentype(),token))
    raise KeyError("Unexpected {0}, {1}.".format(token.gettokentype(),token))
    raise LexingError("Error in lexing. {0}".format(token.gettokentype()))





def parsetxt(text):
    parser = pg.build()
    parser.parse(lexr.l.lex(text))
