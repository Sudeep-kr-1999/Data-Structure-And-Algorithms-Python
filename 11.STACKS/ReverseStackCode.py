# <<<<<<<<<<<<<<<<<<[ REVERSING A STACK  USING A EMPTY STACK AND A INBUILT STACK RECURSIVELY]>>>>>>>>>>>>>>>>>>>>>>>>>

def reverseStack(s1,s2):
    if len(s1)<=1:
        return

    while len(s1)!=1:
        ele=s1.pop()
        s2.append(ele)

    lastElement=s1.pop()

    while len(s2)!=0:
        ele=s2.pop()
        s1.append(ele)
    reverseStack(s1,s2)
    s1.append(lastElement)

from sys import setrecursionlimit
setrecursionlimit(11000)

n=int(input())
s1=[ int(ele) for ele in input().split()]
s2=[]

reverseStack(s1,s2)
print("the elements of stack after reversing pops out from the stack like this :")
while len(s1)!=0:
    print(s1.pop(),end=" ")
