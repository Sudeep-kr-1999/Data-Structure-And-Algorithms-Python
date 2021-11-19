# <<<<<<<<<<<<<<<[ INPLACE HEAP SORT WAY-1]>>>>>>>>>>>>>>>>>>>>>>>>
# heap sort only works properly when there is possibility of making heaps..........(very very important )!!!!!!!

def percolateDown(arr,i,n):
    parent_index=i
    left_child_index=2*parent_index+1
    right_child_index=2*parent_index+2
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

def inplaceHeapSort1(arr):
    if len(arr)==0 or len(arr)==1:
        return
    n=len(arr)
    for i in range(1,n):
        child_index=i

        while child_index>0:
            parent_index=(child_index-1)//2
            if arr[parent_index]>arr[child_index]:
                arr[parent_index],arr[child_index]=arr[child_index],arr[parent_index]
                child_index=parent_index
            else:
                break

    # n-1 se 1 index tk jaayege............!!!!!
    for i in range(n-1,0,-1):
        # pehle minimum ele means arr[0] aur last element swap hote h!!!!!!
        arr[0],arr[i]=arr[i],arr[0]
        # rest part of heap ke liye down down_heapify krege
        percolateDown(arr,0,i)

    return arr

print("Give the input array for sorting : ",end="")
arr=[int(x) for x in input().split()]
ans_arr=inplaceHeapSort1(arr)

print("in descending order:", end="")
for ele in ans_arr:
    print(ele,end=" ")
print()
print("in ascending order:",end="")
for ele in ans_arr[::-1]:
    print(ele,end=" ")