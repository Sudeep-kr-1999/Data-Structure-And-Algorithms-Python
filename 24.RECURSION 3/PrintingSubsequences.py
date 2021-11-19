# <<<<<<<<<<<<<<<<<<<<[ PRINTING SUBSEQUENCES]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def printSubs(s,o=""):
    if len(s)==0:
        print(o)
        return

    # don't include 0th char
    printSubs(s[1:],o)

    # include 0th char
    newoutput=o+s[0]
    printSubs(s[1:],newoutput)

printSubs("abc")
