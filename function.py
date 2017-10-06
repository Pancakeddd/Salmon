import parser
class Function():
    def __init__(self, name,arguments,code):
        self.name = name
        self.args = arguments
        self.code = code
class PycFunction():
    def __init__(self, name,pythoncode):
        self.name = name
        self.pyc = compile(pythoncode[0], "duddg", 'exec')

functions = {}

def createfunction(func):
    functions[func.name] = func
def getfunction(name):
    return functions.get(name)

def runfilesal(text):
    strfinish = ""
    with open(text) as f:
        for line in f:
            strfinish = strfinish + line
    strfinish = strfinish.replace('\n','')
    strfinish = strfinish.replace(';','\n')
    for line in strfinish.splitlines():
        parser.parsetxt(line)
createfunction(PycFunction("import",['function.runfilesal(INPFUNC_SPECIAL_1[1].evalv())']))
