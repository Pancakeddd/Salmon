import variable
import typed
import parser
pg = parser.pg

@pg.production('expression : expression equals expression')
def expression_setv(p):
    variable.addvariable(variable.Variable(p[0].eval(),variable.variabletypelist[0],p[2].evalv() ) )

@pg.production('expression : expression plus expression')
def expression_addv(p):
    return typed.returntype((p[0].evalv() + p[2].evalv()))
@pg.production('expression : expression plus plus')
def expression_addsmv(p):
    return typed.returntype((p[0].evalv()+1))

@pg.production('expression : expression minus expression')
def expression_subv(p):
    return typed.returntype((p[0].evalv() - p[2].evalv()))

@pg.production('expression : expression minus minus')
def expression_addsmv(p):
    return typed.returntype((p[0].evalv()-1))

@pg.production('expression : expression mult expression')
def expression_multv(p):
    return typed.returntype((p[0].evalv() * p[2].evalv()))

@pg.production('expression : expression mult mult')
def expression_addsmv(p):
    return typed.returntype((p[0].evalv() * 2)) 

@pg.production('expression : expression divide expression')
def expression_multv(p):
    return typed.returntype((p[0].evalv() / p[2].evalv()))

@pg.production('expression : expression divide divide')
def expression_addsmv(p):
    return typed.returntype((p[0].evalv() / 2))

@pg.production('expression : expression ifequals expression')
def expression_bequal(p):
    return typed.Bool(p[0].evalv() == p[2].evalv())

@pg.production('expression : expression ifgreater expression')
def expression_bgreat(p):
    return typed.Bool(p[0].evalv() > p[2].evalv())

@pg.production('expression : expression iflesser expression')
def expression_bless(p):
    return typed.Bool(p[0].evalv() < p[2].evalv())

@pg.production('expression : expression ifequalsnot expression')
def expression_bnequal(p):
    return typed.Bool(p[0].evalv() != p[2].evalv())
