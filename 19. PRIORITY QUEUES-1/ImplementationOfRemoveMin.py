class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority


class PriorityQueue:
    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize()==0

    def getMin(self):
        if self.isEmpty() is True:
            return None

        return self.pq[0].value
        # value return kr rhe h but jiska value return krege wo priority ke base pr arrange hoga.!

    def __percolateUp(self):
        childIndex=self.getSize()-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex].priority<self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break


    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()


    def __percolateDown(self):
        parentIndex=0
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2
        while leftChildIndex<self.getSize():
            MinIndex=parentIndex
            # to get the index of minimum element among leftchild,rightchild and parent element!

            if self.pq[MinIndex].priority>self.pq[leftChildIndex].priority:
                MinIndex=leftChildIndex


            # right child se compare krne se pehle ye dhyan rkhege ki right child exist kr bhi rha h ya nhi (very very important)!!!!
            if rightChildIndex<self.getSize() and self.pq[MinIndex].priority>self.pq[rightChildIndex].priority:
                MinIndex=rightChildIndex


            if MinIndex==parentIndex:
                break

            self.pq[parentIndex],self.pq[MinIndex]=self.pq[MinIndex],self.pq[parentIndex]
            parentIndex=MinIndex
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2





    def removeMin(self):
        if self.isEmpty():
            return None
        ele=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele


pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)

for i in range(4):
    print(pq.removeMin())

# output...!

# D
# C
# A
# B
# the output is on the basic of  min priority so it is correct....!

