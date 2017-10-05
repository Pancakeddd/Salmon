import lexer as lexr
from rply.token import BaseBox
from rply import ParserGenerator



pg = ParserGenerator(
    ['number',
     'equals', 'variablenam','string','plus','minus','mult','divide','codeblock',"colon",
     'ifequals','ifgreater','iflesser','if','while','infinite','timedloop','lpar','rpar','lcod','rcod','functiondef','functionbind',
     'ifequalsnot','true','false'
    ]
)


@pg.error
def error_handler(token):
    raise ValueError("Unexpected {0}, {1}.".format(token.gettokentype(),token))
    raise KeyError("Unexpected {0}, {1}.".format(token.gettokentype(),token))
    raise LexingError("Error in lexing. {0}".format(token.gettokentype()))



parser = None
def startparser():
    global parser
    parser = pg.build()
def parsetxt(text):
    parser.parse(lexr.l.lex(text))

def parsetxtreturn(text):
    return parser.parse(lexr.l.lex(text))
