# <<<<<<<<<<<<<<<<<<<<<[ Heap Sort Code]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def down_heapify(arr,i,n):
    parentIndex=i
    leftChildIndex=2*parentIndex+1
    rightChildIndex=2*parentIndex+2

    # till left child index within the length of array.!
    while leftChildIndex<n:
        minIndex=parentIndex
        if arr[minIndex]>arr[leftChildIndex]:
            minIndex=leftChildIndex
        if rightChildIndex<n and arr[minIndex]>arr[rightChildIndex]:
            minIndex=rightChildIndex
        if minIndex==parentIndex:
            return
        arr[minIndex],arr[parentIndex]=arr[parentIndex],arr[minIndex]
        parentIndex=minIndex
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2
    return

def heapSort(arr):
    # first Build The Heap..!
    n=len(arr)
    # pehle n//2-1 se 0 tak jaayege non leaf nodes ke liye...!
    for i in range(n//2-1,-1,-1):
        down_heapify(arr,i,n)
        #passing real arr, initial,index,and size of the array to be working....!!(very very imoortant)!!

    # n-1 se 1 index tk jaayege............!!!!!
    for i in range(n-1,0,-1):
        # pehle minimum ele means arr[0] aur last element swap hote h!!!!!!
        arr[0],arr[i]=arr[i],arr[0]
        # rest part of heap ke liye down down_heapify krege
        down_heapify(arr,0,i)
    return



    #Removing n elements from the heap and put them into correct position..!


arr= [int(x) for x in input().split()]
heapSort(arr)
print("in descending order:", end="")
for ele in arr:
    print(ele,end=" ")
print()
print("in ascending order:",end="")
for ele in arr[::-1]:
    print(ele,end=" ")
