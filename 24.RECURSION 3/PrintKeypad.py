# <<<<<<<<<<<<<<<<[ PRINT KEYPAD NOT RETURNING]>>>>>>>>>>>>>>>>>>>>>>

def getstirng(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return " "

def printKeypad(n,outputSoFar=""):
    if n==0:
        print(outputSoFar)
        return
    smallNumber=n//10
    lastDigit=n%10
    optionsForLastDigit=getstirng(lastDigit)
    for c in optionsForLastDigit:
        newoutput=c+outputSoFar
        printKeypad(smallNumber,newoutput)

printKeypad(23)
