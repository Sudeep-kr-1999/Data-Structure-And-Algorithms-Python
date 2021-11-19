# <<<<<<<<<<<<<<<<<<[ IN-BUILT STACK AND QUEUE CONCEPT]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# NOTE :----> for inbuilt stack we should use list in python.........!!!!


# inbuilt stack as list....!!!
# s=[1,2,3]
# s.append(4)
# s.append(5)
# print(s.pop())
# print(s.pop())


# FOR QUEUE WE SHOULD NOT USE LIST RATHER WE HAVE A INBUILT LIBRARY "queue" from python 3 onwards.........!!!

# Queue follow first in first out property(FIFO).....!!!


# for inbuilt queue....!!
import queue
# q=queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)

# while not q.empty():
#     print(q.get())   #q.get() deque the element and return the element dequeued...!!


q=queue.LifoQueue()  # lifoQueue is just like the stacks as it is last in first out case....!!!!!!!
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())





