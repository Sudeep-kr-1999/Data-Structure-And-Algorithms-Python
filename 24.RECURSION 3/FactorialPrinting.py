# <<<<<<<<<<<<[ print factorial instead of returning]>>>>>>>>>>>>>>>>

# def factorial_helper(n):
#     if n==0:
#         return 1
#     small_output=factorial_helper(n-1)
#     output=n*small_output
#     return output
# def fact(n):
#     output=factorial_helper(n)
#     print(output)

# fact(5)

# - - - - - - - -  - -  - - -  - -  - - -  - - - - -  - - - -  - - -  - -  - - - - - - - -  - - - -  - - - - -  -  - - - - - - - - - - - -
# - - - - - - - -  - -  - - -  - -  - - -  - - - - -  - - - -  - - -  - -  - - - - - - - -  - - - -  - - - - -  -  - - - - - - - - - - - -

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ Final programme for only printing not returning]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def factorial(n,ans=1):
    if n==0:
        print(ans)
        return
    ans=ans*n
    factorial(n-1,ans)

factorial(5)


