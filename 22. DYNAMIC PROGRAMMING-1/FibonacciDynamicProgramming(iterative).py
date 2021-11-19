# <<<<<<<<<<<<[ ITERATIVE SOLUTION OF FIBONACCI NUMBER BY DYNAMIC PROGRAMMING ]>>>>>>>>>>>>>>>>>>>>>

def fibbI(n):
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1

    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i=i+1

    return dp[n]


n=int(input())
ans=fibbI(n)
print(ans)
