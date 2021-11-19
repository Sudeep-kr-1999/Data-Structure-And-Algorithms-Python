# <<<<<<<<<<<<<<<<<<[ QUEUES USING 2 STACKS]>>>>>>>>>>>>>>>>>>>>

class QueueUsingTwoStacks:
    def __init__(self):
        # two stacks s1 and s2 as a list.......!
        self.__s1=[]
        self.__s2=[]


# ek element s1 mein enter krege phir agle ke liye saare ko s2 pr bhejege aur nya element enter krege phir s2 wla wapas s1 mein le aayege 
# is process ko repeat krte rehne k h 
    def enqueue(self,data):
        #(O(n))
        while(len(self.__s1)!=0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)

        while(len(self.__s2)!=0):
            self.__s1.append(self.__s2.pop())

        return

    def dequeue(self):
        #(O(1))
        if(len(self.__s1)==0):
            return -1
        return self.__s1.pop()


    def front(self):
        if(len(self.__s1)==0):
            return -1
        return self.__s1[-1]



    def size(self):
        return(len(self.__s1))


    def isEmpty(self):
        return self.size()==0


q=QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()
print(q.front())