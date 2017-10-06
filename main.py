def main(argv):
    linenumber = 1
    import parser
    import variablepar
    import functionpar
    parser.parser = parser.pg.build()
    strfinish = ""
    with open("test.salmon") as f:
        for line in f:
            strfinish = strfinish + line
    strfinish = strfinish.replace('\n','')
    strfinish = strfinish.replace(';','\n')
    for line in strfinish.splitlines():
        parser.parsetxt(line,True)
if __name__ == "__main__":
    import sys
    main(sys.argv)

def target(*args):
    return main, None
