def minStepsTo1DP(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    i = 4
    while i<=n:
        ans2 = 10000000
        ans3 = 10000000
        ans1 = dp[i-1]
        if i%2==0:
            ans2 = dp[i//2]
        if i%3==0:
            ans3 = dp[i//3]
        dp[i] = 1+min(ans1,ans2,ans3)
        i = i+1
    return dp[n]


# Main
n=int(input())
print(minStepsTo1DP(n))