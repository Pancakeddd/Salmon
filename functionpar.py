import variable
import function
import typed
import parser
pg = parser.pg
@pg.production('expression : variablenam expression')
@pg.production('expression : variablenam expression expression')
def expression_runf(p):
    try:
        if(isinstance(function.getfunction(p[0].getstr()),function.PycFunction)):
            INPFUNC_SPECIAL_1 = p
            OUTFUNC_SPECIAL_1 = None
            ldict = locals()
            exec(function.getfunction(p[0].getstr()).pyc,None,ldict)
            OUTFUNC_SPECIAL_1 = ldict['OUTFUNC_SPECIAL_1']
            return typed.returntype(OUTFUNC_SPECIAL_1)
        else:
            iterv = 1
            itervas = 1
            for i in function.getfunction(p[0].getstr()).args:
                variable.addvariable(variable.Variable(i,variable.variabletypelist[0],p[itervas].evalv() ) )
                itervas+=1
            for i in function.getfunction(p[0].getstr()).code:
                if(len(function.getfunction(p[0].getstr()).code) != iterv):
                    parser.parsetxt(i)
                else:
                    return parser.parsetxtreturn(i)
                iterv+=1
            intervas = 1
            for i in function.getfunction(p[0].getstr()).args:
                variable.remvariable(i)
                itervas+=1
    except AttributeError:
        raise AttributeError('Unknown Function "{0}"'.format(p[0].getstr()))

@pg.production('expression : if expression expression')
def expression_ifr(p):
    if(p[1].evalv() == True):
        if(isinstance(p[2],typed.ListCodeBlock)):
            for i in p[2].evalv():
                parser.parsetxt(i)
        else:
            parser.parsetxt(p[2].evalv())
@pg.production('expression : while expression expression')
def expression_whiler(p):
    running = True
    while(running):
        if(p[1].evalv() == False):
            running = False
        if(isinstance(p[2],typed.ListCodeBlock)):
            for i in p[2].evalv():
                parser.parsetxt(i)
        else:
            parser.parsetxt(p[2].evalv())
@pg.production('expression : infinite expression')
def expression_whiler(p):
    while(True):
        if(isinstance(p[1],typed.ListCodeBlock)):
            for i in p[1].evalv():
                parser.parsetxt(i)
        else:
            parser.parsetxt(p[1].evalv())
@pg.production('expression : timedloop expression expression')
def expression_timedr(p):
    i = 0
    while(i < p[1].evalv()):
        if(isinstance(p[2],typed.ListCodeBlock)):
            for d in p[2].evalv():
                parser.parsetxt(d)
        else:
            parser.parsetxt(p[2].evalv())
        i = i + 1
@pg.production('expression : functiondef variablenam expression expression')
def expression_functiondef(p):
    if(isinstance(function.getfunction(p[1].getstr()),function.PycFunction) != True):
        if (isinstance(p[3],typed.ListCodeBlock)):
            if (isinstance(p[2],typed.ListCodeBlock)):
                function.createfunction(function.Function(p[1].getstr(),p[2].evalv(),p[3].evalv()))
            else:
                function.createfunction(function.Function(p[1].getstr(),[p[2].evalv()],p[3].evalv()))
        else:
            if (isinstance(p[2],typed.ListCodeBlock)):
                function.createfunction(function.Function(p[1].getstr(),p[2].evalv(),[p[3].evalv()]))
            else:
                function.createfunction(function.Function(p[1].getstr(),[p[2].evalv()],[p[3].evalv()]))
    else:
        raise ValueError ("Can't overwrite default function")
@pg.production('expression : functionbind variablenam expression')
def expression_functiondef(p):
    function.createfunction(function.PycFunction(p[1].getstr(),p[2].evalv()))
