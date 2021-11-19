# <<<<<<<<<<<<<<<<<<<<<<<<<<[ Minimum Squares to represent N iteratively]>>>>>>>>>>>>>>>>>

import math,sys
def minSquaresIteratively(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0

    for i in range(1,n+1):
        ans=sys.maxsize
        sq_root=int(math.sqrt(i))
        for j in range(1,sq_root+1):
            current_ans=1+dp[i-(j**2)]
            ans=min(current_ans,ans)
        dp[i]=ans
    return dp[n]

n=int(input())
ans=minSquaresIteratively(n)
print(ans)

