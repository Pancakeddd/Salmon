class Variabledata():
    def __init__(self, callname,holdingvar):
        self.callname = callname
        self.holdingvar = holdingvar
class Variable():
    def __init__(self, name,variabledata,data):
        self.name = name
        self.variabledata = variabledata
        self.data = data


variabletypelist = [Variabledata("int",int),Variabledata("string",str),Variabledata("long",long)]

variables = {}

def addvariable(var):
    variables[var.name] = var
def getvariable(name):
    return variables[name]
def remvariable(name):
    del variables[name]
