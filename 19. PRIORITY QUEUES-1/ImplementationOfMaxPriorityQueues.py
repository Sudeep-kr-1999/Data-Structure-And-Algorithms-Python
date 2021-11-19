# <<<<<<<<<<<<<<<<<<[ Implementation of Max Priority Queues]>>>>>>>>>>>>>>>>>>>>

class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class PriorityQueue:
    def __init__(self):
        self.pq=[]

    def isEmpty(self):
        return self.getSize()==0

    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.getSize()==0:
            return
        ele=self.pq[0].value
        return ele

    def __percolateUp(self):
            child_index=self.getSize()-1
            while child_index>0:
                parent_index=((child_index)-1)//2
                if self.pq[child_index].priority>self.pq[parent_index].priority:
                    self.pq[child_index],self.pq[parent_index]=self.pq[parent_index],self.pq[child_index]
                    child_index=parent_index
                else:
                    break

    def insert(self,ele,priority):
        pqNode=PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parent_index=0
        left_child_index=2*parent_index+1
        right_child_index=2*parent_index+2


        while left_child_index<self.getSize():
            max_index=parent_index

            if self.pq[left_child_index].priority>self.pq[max_index].priority:
                max_index=left_child_index
            if right_child_index<self.getSize() and self.pq[right_child_index].priority>self.pq[max_index].priority:
                max_index=right_child_index
            if max_index==parent_index:
                break

            self.pq[max_index],self.pq[parent_index]=self.pq[parent_index],self.pq[max_index]
            parent_index=max_index
            left_child_index=2*parent_index+1
            right_child_index=2*parent_index+2

    def removeMax(self):
        if self.isEmpty():
            return None
        ele=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

pq = PriorityQueue()

pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)

for i in range(4):
    print(pq.removeMax())

# OUTPUTS:------///
# B
# A
# C
# D

# Output is on the basic of max priority so correct....!!!