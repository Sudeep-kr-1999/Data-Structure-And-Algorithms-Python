# <<<<<<<<<<<<<<<<<<<<<<[ Implementation of Priority Queues]>>>>>>>>>>>>>>>>>>>>>>>>>>>
# by using Min Heap....!!!!!
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
    def insert(self,value,priority):
        pass

    def removeMin(self):
        pass

