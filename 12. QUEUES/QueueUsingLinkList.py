# <<<<<<<<<<<<<<<<<<<[ implementation of queue using link list]>>>>>>>>>>>>>>>>>>>>>>>>

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class QueueUsingLL:

    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0

    def enqueue(self,data):
        # same algo as used in making link list......!!!!!!!!!!!!
        newNode=Node(data)
        if self.__head is None:
            self.__head=newNode
            self.__tail=newNode
            self.__count+=1
        else:
            self.__tail.next=newNode
            self.__tail=newNode
            self.__count+=1

    def dequeue(self):
        if self.__count==0:
            print("queue is empty")
            return
        data=self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data

    def isEmpty(self):
        return self.size()==0

    def size(self):
        return self.__count

    def front(self):
        if self.__head is None:
            print("queue is empty")
            return
        data=self.__head.data
        return data


