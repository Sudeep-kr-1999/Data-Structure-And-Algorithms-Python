#                     <<<<<<<<<<<<<<<<<<<<[ RERCUSION IN PYTHON ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

                    # <<<<<<<<<<<<[ FACTORIAL USING RECURSION]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def fact(n):
#     if n==0:
#         return 1
#     return  n*fact(n-1)

# n=int(input())
# ans=fact(n)
# print(ans)
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#                    <<<<<<<<<<<<<<<<<<<<<[ SUM OF FIRST N NATURAL NUMBERS]>>>>>>>>>>>>>>>>>>>>>

# def sum_n(n):
#     if n==0:
#         return 0
#     small_output=sum_n(n-1)
#     return n+small_output

# n=int(input())
# sum=sum_n(n)
# print(sum)
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -


#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ x to the power n function by recursion]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def power_number(a,b):
#     if b==0:
#         return 1
#     small_output=pow(a,b-1)
#     return small_output*a

# str=input().split()
# x,n=int(str[0]),int(str[1])
# ans=power_number(x,n)
# print(ans)
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -


#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#                      <<<<<<<<<<<[ PRINT FIRST N NATURAL NUMBERS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
# from 1  to n:
# def print_1to_n(n):
#     if n==0:
#         return
#     print_1to_n(n-1)
#     print(n)

# n=int(input())
# print_1to_n(n)
# #- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
#from n to 1:
# def print_nto_1(n):
#     if n==0:
#         return
#     print(n)
#     print_nto_1(n-1)


# n=int(input())
# print_nto_1(n)
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
                    #   <<<<<<<<<<<<<<<< [ n-th Fibonacci number ]>>>>>>>>>>>>>>>>>>>>>>

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     fib_n_1=fib(n-1)
#     fib_n_2=fib(n-2)
#     output=fib_n_1+fib_n_2
#     return output

# n=int(input())
# ans=fib(n)
# print(ans)

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#                <<<<<<<<<<<<<<<<<[ RECURSION LIMITS IN THE PYTHON]>>>>>>>>>>>>>>>>>>>>

# NOTE:-- IF YOU WANT TO INCREASE THE LIMIT OF RECURSION
#         WE USE (sys) LIBRARY AND SET RECURSION LIMIT AS sys.setrecursionlimit(value)

# # for factorial function.............!

# import sys
# sys.setrecursionlimit(5000)

# def fact(n):
#     if n==0:
#         return 1
#     return  n*fact(n-1)

# n=int(input())
# ans=fact(n)
# print(ans)

#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -
#- - --  - - -  - - -  - -   - - -  - -  - - -  - - -  - - - -  - - - - -  - - - - - - - --- - - - - - -  - - - - - - - - -- - - ---- -

#<<<<<<<<<<<<<<<<<<[CHECK WHETHER THE LIST IS SORTED OR NOT VIA RECURSION]>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def isSorted(a):
#     l=len(a)
#     if l==0 or l==1:
#         return True
#     if a[0]>a[1]:
#         return False
#     smallerList=a[1:]
#     isSmallerListSorted=isSorted(smallerList)
#     # return isSmallerListSorted

#     if isSmallerListSorted:
#         return True
#     else:
#         return False

# li=[int(x) for x in input().split()]    # space seprated input.........!!!!!!!!!!!
# ans=isSorted(li)
# print(ans)




#<<<<<<<<<<<<<<<<<<<<<<<<<<<[ SUM OF ELEMENTS OF ARRAY RECURSIVELY]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def sumArray(arr):
#     length=len(arr)
#     if length==0:
#         return
#     elif length==1:
#         return arr[0]
#     sum=arr[0]
#     arr1=arr[1:]
#     smaller_array_sum=sumArray(arr1)
#     output=arr[0]+smaller_array_sum
#     return output

#     pass

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# print(sumArray(arr))



# <<<<<<<<<<<<<<<<<<<<<<<[ CHECK WETHER A GIVEN NUMBER IS AVAILABLE IN THE LIST OR NOT]>>>>>>>>>>>>>>>>>>>
def checkNumber(arr, x):
    length=len(arr)
    if length==0:
        return
    if length==1:
        if arr[0]==x:
            return True
        else:
            return False

    if x==arr[0]:
        return True
    smaller_array=arr[1:]
    is_element_in_smaller_array=checkNumber(smaller_array,x)

    if is_element_in_smaller_array:
        return True
    else:
        return False

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
ans=checkNumber(arr,x)
if ans:
    print("true")
else:
    print("false")



    