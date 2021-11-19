# <<<<<<<<<<<<<<<<<<<<<<<<<<<<[ knapsack TOP DOWN APPROACH]>>>>>>>>>>>>>>>>>>>>>>>>>

def knapsack(W,val,wt):
    n=len(val)
    dp=[[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j<wt[i-1]:
                ans=dp[i-1][j]
            else:
                ans1=val[i-1]+dp[i-1][j-wt[i-1]]
                ans2=dp[i-1][j]
                ans=max(ans1,ans2)
            dp[i][j]=ans

    return dp[n][W]



val=[200,300,100]
wt=[20,25,30]
W=50

ans=knapsack(W,val,wt)
print(ans)
