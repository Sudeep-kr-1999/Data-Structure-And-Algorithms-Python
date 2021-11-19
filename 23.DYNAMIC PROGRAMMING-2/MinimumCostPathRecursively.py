# <<<<<<<<<<<<<<<[ Minimum cost path recursively]>>>>>>>>>>>>>>>>>>
import sys
def minCost(cost,i,j,n,m):

    # special case....!
    if i==n-1 and j==m-1:
        return cost[i][j]

    # base case...!!!!
    if i>=n or j>=m:
        return sys.maxsize

    ans1=minCost(cost,i,j+1,n,m)
    ans2=minCost(cost,i+1,j,n,m)
    ans3=minCost(cost,i+1,j+1,n,m)
    ans=cost[i][j]+min(ans1,ans2,ans3)
    return ans


cost=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
# minCost(cost,starting_row_index,starting_column_index,no_of_rows,no_of_columns)
ans=minCost(cost,0,0,4,3)
print(ans)

