# <<<<<<<<<<<<<<<<<<<<[ BALANCED PARENTHESIS CODE]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def isBalanced(string):
    s=[]
    for char in string:
        if char in '({[':
            s.append(char)
        elif char == ')':
            if (not s or s[-1]!='('):    # not s is used to check wether stack is empty !!!!!!!!!!!!!!!
                                         # s[-1] here we use negative indexing means it is the last element of the list...........!!
                return False
            s.pop()
        elif char == '}':
            if (not s or s[-1]!='{'):
                return False
            s.pop()
        elif char == ']':
            if (not s or s[-1]!='['):
                return False
            s.pop()
    if (not s):
        return True
    return False

string=input()
ans=isBalanced(string)
print(ans)