import parser
import variable
import function
from rply.token import BaseBox
pg = parser.pg


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return self.value
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
class Bool(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return self.value
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return self.value
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
class CodeBlock(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return self.value
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
class ListCodeBlock(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return self.value
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
class VariableName(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    def evalv(self):
        return variable.getvariable(self.value).data
    def __eq__(self, other) :
        return self.__dict__ == other.__dict__

def returntype(val):
    if(type(val) == int):
        return Number(val)
    elif(type(val) == str):
        return String(val)
    else:
        return None

@pg.production('expression : number')
def expression_number(p):
    return Number(int(p[0].getstr()))
@pg.production('expression : codeblock')
def expression_codeblock(p):
    st = p[0].getstr()[1:][:-2]
    st = st.replace("}","}|")
    print(st)
    return ListCodeBlock(st.split(","))
@pg.production('expression : specialcodeblock')
def expression_specialcodeblock(p):
    st = p[0].getstr()[1:][:-2]
    st = st.replace("}","}/")
    return ListCodeBlock(st.split(":"))
@pg.production('expression : string')
def expression_str(p):
    st = p[0].getstr()[:-1][1:]
    return String(st)
@pg.production('expression : lpar expression rpar')
def expression_parenthc(p):
    return p[1]
@pg.production('expression : lcod expression rcod')
def expression_codc(p):
    return p[1].eval()
@pg.production('expression : true')
@pg.production('expression : false')
def expression_bool(p):
    return Bool(bool(p[0].getstr()))
@pg.production('expression : variablenam')
def expression_varname(p):
    if(function.getfunction(p[0].getstr()) != None):
        if(isinstance(function.getfunction(p[0].getstr()),function.PycFunction)):
            INPFUNC_SPECIAL_1 = p
            OUTFUNC_SPECIAL_1 = None
            ldict = locals()
            exec(function.getfunction(p[0].getstr()).pyc,None,ldict)
            OUTFUNC_SPECIAL_1 = ldict['OUTFUNC_SPECIAL_1']
            return typed.returntype(OUTFUNC_SPECIAL_1)
        else:
            iterv = 1
            for i in function.getfunction(p[0].getstr()).code:
                if(len(function.getfunction(p[0].getstr()).code) != iterv):
                    parser.parsetxt(i)
                else:
                    return parser.parsetxtreturn(i)
                iterv+=1
    else:
        return VariableName(p[0].getstr())
