# <<<<<<<<<<<<<<<<<<<<[ HEAP SORT BY GENERAL METHOD BY MAKING AN HEAP]>>>>>>>>>>>>>>>>>>>>>>>

def percolateUp(arr):
    child_index=len(arr)-1
    while child_index>0:
        parent_index=(child_index-1)//2
        if arr[parent_index]>arr[child_index]:
            arr[parent_index],arr[child_index]=arr[child_index],arr[parent_index]
            child_index=parent_index

        else:
            break


def percolateDown(arr,i,n):
    parent_index=i
    left_child_index=2*parent_index+1
    right_child_index=2*parent_index+2

    #jab tak left child index working array ke length se chota hoga (yha par n as the array size liya gaya h!)
    while left_child_index<n:
        min_index=parent_index
        if arr[min_index]>arr[left_child_index]:
            min_index=left_child_index
        if right_child_index<n and arr[right_child_index]<arr[min_index]:
            min_index=right_child_index
        if min_index==parent_index:
            break
        arr[min_index],arr[parent_index]=arr[parent_index],arr[min_index]
        parent_index=min_index
        left_child_index=2*parent_index+1
        right_child_index=2*parent_index+2

def heap_sort_general(arr):
    if len(arr)==0 or len(arr)==1:
        return
    heap_arr=[]
    for ele in arr:
        heap_arr.append(ele)
        percolateUp(heap_arr)

    n=len(heap_arr)

    # n-1 se 1 index tk jaayege............!!!!!
    for i in range(n-1,0,-1):
         # pehle minimum ele means arr[0] aur last element swap hote h!!!!!!
        heap_arr[0],heap_arr[i]=heap_arr[i],heap_arr[0]
        # rest part of heap ke liye down down_heapify krege
        percolateDown(heap_arr,0,i)

    return heap_arr

arr=[int(x) for x in input().split()]
ans_arr=heap_sort_general(arr)

print("in descending order:", end="")
for ele in ans_arr:
    print(ele,end=" ")
print()
print("in ascending order:",end="")
for ele in ans_arr[::-1]:
    print(ele,end=" ")


# 10 5 11 2 3 7 12 1 6