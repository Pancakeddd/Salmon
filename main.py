import parser
import variablepar
import functionpar


with open("test.salmon") as f:
    for line in f:
        parser.parsetxt(line)
