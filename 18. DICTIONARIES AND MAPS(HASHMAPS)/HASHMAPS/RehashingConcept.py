# <<<<<<<<<<<<<<<<<<[ CONCEPT OF REHASHING]>>>>>>>>>>>>>>>>>>>>>

class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketSize=5
        self.buckets=[None]*self.bucketSize
        self.count=0

    def size(self):
        return self.count
    def getBucketIndex(self,hashcode):
        return (abs(hashcode)%(self.bucketSize))


    def remove(self,key):
        hashcode=hash(key)
        index=self.getBucketIndex(hashcode)
        head=self.buckets[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev==None:
                    self.buckets[index]=head.next
                else:
                    prev.next=head.next
                self.count-=1
                return head.value
            prev=head
            head=head.next
        return None

    def getValue(self,key):
        hashcode=hash(key)
        index=self.getBucketIndex(hashcode)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None

    def rehash(self):
        temp=self.buckets
        self.buckets=[None for i in range(self.bucketSize*2)]
        self.bucketSize=2*self.bucketSize
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next

    def loadFactor(self):
        return self.count/self.bucketSize

    def insert(self,key,value):
        hashcode=hash(key)
        index=self.getBucketIndex(hashcode)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        head=self.buckets[index]
        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[index]=newNode
        self.count+=1
        # insert krne ke baad load factor ka dhyan rkhna h!!!
        loadFactor=self.count/self.bucketSize
        if loadFactor>=0.7:
            self.rehash()

m=Map()
# m.insert("Parikh",2)
# print(m.getValue("Parikh"))
# print(m.size())
# m.insert("Rohan",7)
# print(m.size())
# m.insert("Parikh",9)
# print(m.size())
# print(m.getValue("Rohan"))
# print(m.getValue("Parikh"))
# m.remove("Rohan")
# print(m.getValue("Rohan"))
# print(m.getValue("Parikh"))

for i in range(10):
    m.insert("abc"+str(i),i+1)
    print(m.loadFactor())

for i in range(10):
    print("abc"+str(i)+":",m.getValue("abc"+str(i)))






