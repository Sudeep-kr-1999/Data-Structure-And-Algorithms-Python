# <<<<<<<<<<<<<[ FINDING K SMALLEST NUMBER IN THE ARRAY USING MAXHEAP]>>>>>>>>>>>>>>>>>>>>>>>>>

import heapq

def kSmallest(arr,k):
    heap=arr[:k]
    heapq._heapify_max(heap)
    n=len(arr)
    for i in range(k,n):
        if heap[0]>arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap

arr=[int(x) for x in input().split()]
elements=kSmallest(arr,4)
for ele in elements:
    print(ele,end=" ")
