# <<<<<<<<<<<<<<<<<<[ Matrix chain multiplication]>>>>>>>>>>>>>>>>>>>>>>>>

# without memoization.............!
import sys
def mcm(p,i,j):

    if i==j:
        return 0

    min_value=sys.maxsize
    for k in range(i,j):
        ans1=mcm(p,i,k)
        ans2=mcm(p,k+1,j)
        mCost=p[i-1]*p[k]*p[j]
        current_value=ans1+ans2+mCost
        min_value=min(min_value,current_value)
    return min_value

p=[2,3,4,5,6]
n=len(p)-1
ans=mcm(p,1,n)
print(ans)









