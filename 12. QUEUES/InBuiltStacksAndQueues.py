# <<<<<<<<<<<[ IN BUILT STAKS AND QUEUES IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>


# for inbuilt stacks we can use simple lists in python......!!!!!
# s=[1,2,3]
# s.append(4)
# s.append(5)

# print(s.pop())
# print(s.pop())




# inbuilt queues:-----> for inbuilt queues we cannot use list of python.....in a good way because it is not efficient..!
# we have a proper library queue in python 3 onwards
# in the library "queue" we have a Queue class ....!!
import queue

# # inbuilt queue
# q=queue.Queue()  # means 'q' is the object of the "Queue" class which is present in the inbuilt library of "queue" provided by the python 3 onwards..!!
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# while not q.empty():
#     print(q.get())      ## q.get() dequeue the element...!!

#NOTE:------->> this "queue" library also contain inbuilt "stack" as the class name "LifoQueue" which in really a stack because it follow LIFO Property....!

q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
while not q.empty():
    print(q.get())


