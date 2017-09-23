import variable
import function
import typed
import parser
pg = parser.pg
@pg.production('expression : variablenam expression')
@pg.production('expression : variablenam expression expression')
def expression_runf(p):
    try:
        INPFUNC_SPECIAL_1 = p
        OUTFUNC_SPECIAL_1 = None
        ldict = locals()
        exec(function.getfunction(p[0].getstr()).pyc,None,ldict)
        OUTFUNC_SPECIAL_1 = ldict['OUTFUNC_SPECIAL_1']
        return typed.returntype(OUTFUNC_SPECIAL_1)
    except IndexError as e:
        print("Unexpected amount of arguments")

@pg.production('expression : if expression expression')
def expression_ifr(p):
    print(p[2])
    print(p[2].getstr())
    if(p[1].evalv() == True):
        parser.parsetxt(p[2].getstr())
