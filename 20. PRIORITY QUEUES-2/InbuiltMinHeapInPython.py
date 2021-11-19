# <<<<<<<<<<<<<[ Inbuilt  MinHeap In Python]>>>>>>>>>>>>

import heapq

li=[1,5,4,8,7,9,11]
heapq.heapify(li)  # by default it arrages array in the heap order!
                   # BY DEFAULT IT FOLLOWS MIN HEAP PROPERTY....!
print(li)
heapq.heappush(li,2)   # heap li mein 2 insert kr dega.!
print(li)


minimum=heapq.heappop(li)    # remove minimum element   !
print(minimum)
print(li)  # print heap after removal!

heapq.heapreplace(li,6)
# ye minimum element ko remove krega and uske jagah pr heap mein "value" insert krke heapify kr dega..!
print(li)

print(heapq.heapreplace(li,10))   # return minimum element!
print(li)






