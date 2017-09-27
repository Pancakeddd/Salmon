class Function():
    def __init__(self, name,arguments,pythoncode):
        self.name = name
        self.args = arguments
        self.pyc = pythoncode
class PycFunction():
    def __init__(self, name,pythoncode):
        self.name = name
        self.pyc = compile(pythoncode, "duddg", 'exec')

functions = {}

def createfunction(func):
    functions[func.name] = func
def getfunction(name):
    return functions.get(name)

createfunction(PycFunction("println",'print(INPFUNC_SPECIAL_1[1].evalv())'))
createfunction(PycFunction("print","import sys; sys.stdout.write(INPFUNC_SPECIAL_1[1].evalv())"))
createfunction(PycFunction("random",'import random;OUTFUNC_SPECIAL_1 = random.randint(INPFUNC_SPECIAL_1[1].evalv(),INPFUNC_SPECIAL_1[2].evalv())'))
createfunction(PycFunction("input",'OUTFUNC_SPECIAL_1 = raw_input(INPFUNC_SPECIAL_1[1].evalv())'))
createfunction(PycFunction("cint",'OUTFUNC_SPECIAL_1 = ord(INPFUNC_SPECIAL_1[1].evalv())'))
createfunction(PycFunction("toint",'OUTFUNC_SPECIAL_1 = int(INPFUNC_SPECIAL_1[1].evalv())'))
createfunction(PycFunction("istring",'OUTFUNC_SPECIAL_1 = chr(INPFUNC_SPECIAL_1[1].evalv())'))
createfunction(PycFunction("deletev",'variable.remvariable(INPFUNC_SPECIAL_2.eval())'))
