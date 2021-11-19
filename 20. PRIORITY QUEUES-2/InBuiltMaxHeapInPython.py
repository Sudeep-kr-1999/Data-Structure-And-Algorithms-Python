# <<<<<<<<<<<<<<<<<<<[ In Built Max Heap In Python]>>>>>>>>>>>>>>>>>>>>

import heapq
li=[1,5,4,7,8,9,2,3]
heapq._heapify_max(li)
print(li)

print(heapq._heappop_max(li)) #max ko pop kr dega
print(li)

heapq._heapreplace_max(li,0)
print(li)

# for pushing the element
li.append(6)
heapq._siftdown_max(li,0,len(li)-1)

# first argument=== heap list jisme krna h
# second argument== kha tak humko arrange krne ke liye jaana hoga
# third argument= kis position pr insert krege

print(li)


