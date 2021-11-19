# <<<<<<<<<<<<<<<<<<<[ LONGEST INCREASING SUBSEQUENCE (LIS) MEMOIZATION]>>>>>>>>>>>>>>>>>>>>>>>

# Length Of "LIS" Starting from ith position...!!!!
def LIS(arr,i,n,dp):

    if i==n:
        return 0,0
    # including_the number the LIS length is initially by default is 1 for the number itself..!

    including_max=1
    for j in range(i+1,n):
        if arr[j]>=arr[i]:
            if dp[j]==-1:
                ans=LIS(arr,j,n,dp)
                dp[j]=ans
                further_including_max=ans[0]
            # returing statement mein "0"th position pr including max hai to iske liye upar [0] likha h.....( vvi )
            else:
                further_including_max=dp[j][1]
            including_max=max(including_max,1+further_including_max)
    if dp[i+1]==-1:
        ans=LIS(arr,i+1,n,dp)
        dp[i+1]=ans
        excluding_max=ans[1]
    # returning mein 1st position pr overall max hai to uske liye we have to write [1] there taaki wo hamesha overall  max ke logic se operate kr sake..!
    else:
        excluding_max=dp[i+1][1]
    overallMax=max(including_max,excluding_max)
    return including_max,overallMax

n=int(input())
li=[int(x) for x in input().split()]
dp=[-1 for i in range(n+1)]

# LIS(li,0,n) it means find LIS starting form "0"th position.......!!!!

# here we are finding the overallMaxLIS So we write [1].....!
ans=LIS(li,0,n,dp)[1]
print(ans)

