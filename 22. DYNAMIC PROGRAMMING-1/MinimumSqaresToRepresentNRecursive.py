# <<<<<<<<<<<<<<<[ MINIMUM SQUARES TO REPRESENT "N"]>>>>>>>>>>>>>>>>>>>>>

import math,sys

# without memoization....!!!!!!!!
# def minSquares(n):

#     if n==0:
#         return 0

#     ans=sys.maxsize
#     sq_root=int(math.sqrt(n))
#     for i in range(1,sq_root+1):
#         current_ans=1+minSquares(n-(i**2))
#         ans=min(ans,current_ans)
#     return ans

# n=int(input())
# ans=minSquares(n)
# print(ans)


# with memoization...........!!!!!!
def minSquares(n,dp):

    if n==0:
        return 0

    ans=sys.maxsize
    sq_root=int(math.sqrt(n))
    for i in range(1,sq_root+1):
        newCheckValue=(n-(i**2))
        if dp[newCheckValue]==-1:
            small_ans=minSquares(newCheckValue,dp)
            dp[newCheckValue]=small_ans
            current_ans=1+small_ans
        else:
            current_ans=1+dp[newCheckValue]

        ans=min(ans,current_ans)
    return ans

n=int(input())
dp=[-1 for i in range(n+1)]
ans=minSquares(n,dp)
print(ans)
