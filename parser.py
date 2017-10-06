import lexer as lexr
from rply.token import BaseBox
from rply import ParserGenerator
linenum = 1


pg = ParserGenerator(
    ['number',
     'equals', 'variablenam','string','plus','minus','mult','divide','codeblock','specialcodeblock',
     'ifequals','ifgreater','iflesser','if','while','infinite','timedloop','lpar','rpar','lcod','rcod','functiondef','functionbind',
     'ifequalsnot','true','false'
    ]
)


@pg.error
def error_handler(token):
    raise ValueError("Unexpected {0}, {1} at line {2}.".format(token.gettokentype(),token,linenum))
    raise KeyError("Unexpected {0}, {1}.".format(token.gettokentype(),token))
    raise LexingError("Error in lexing. {0}".format(token.gettokentype()))



def parsetxt(text,line = False):
    global linenum
    parser.parse(lexr.l.lex(text))
    if (line != False):
        linenum = linenum + 1

def parsetxtreturn(text):
    return parser.parse(lexr.l.lex(text))
