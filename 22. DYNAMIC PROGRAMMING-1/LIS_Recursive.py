# <<<<<<<<<<<<<<<<<<<[ LONGEST INCREASING SUBSEQUENCE (LIS)]>>>>>>>>>>>>>>>>>>>>>>>

# Length Of "LIS" Starting from ith position...!!!!
def LIS(arr,i,n):

    if i==n:
        return 0,0
    # including_the number the LIS length is initially by default is 1 for the number itself..!

    including_max=1
    for j in range(i+1,n):
        if arr[j]>=arr[i]:
            further_including_max=LIS(arr,j,n)[0]
            # returing statement mein "0"th position pr including max hai to iske liye upar [0] likha h.....( vvi )

            including_max=max(including_max,1+further_including_max)

    excluding_max=LIS(arr,i+1,n)[1]
    # returning mein 1st position pr overall max hai to uske liye we have to write [1] there taaki wo hamesha overall  max ke logic se operate kr sake..!


    overallMax=max(including_max,excluding_max)
    return including_max,overallMax

n=int(input())
li=[int(x) for x in input().split()]
# LIS(li,0,n) it means find LIS starting form "0"th position.......!!!!

# here we are finding the overallMaxLIS So we write [1].....!
ans=LIS(li,0,n)[1]
print(ans)

