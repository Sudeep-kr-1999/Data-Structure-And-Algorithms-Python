from QueueUsingLinkList import QueueUsingLL

q=QueueUsingLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)


while q.isEmpty() is False:
    print(q.dequeue())

q.front() 