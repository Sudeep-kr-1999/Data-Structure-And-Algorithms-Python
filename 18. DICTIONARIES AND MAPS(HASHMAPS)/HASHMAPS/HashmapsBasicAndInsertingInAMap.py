# <<<<<<<<<<<<<<<[ HASHMAPS BASIC AND INSERTING IN THE HASHMAPS]>>>>>>>>>>>>>>>>>>>>>>

class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketSize=10
        self.buckets=[None]*self.bucketSize
        self.count=0

    def size(self):
        return self.count
    def getBucketIndex(self,hashcode):
        return (abs(hashcode)%(self.bucketSize))

    def insert(self,key,value):
        hashcode=hash(key)
        index=self.getBucketIndex(hashcode)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        newNode=MapNode(key,value)
        newNode.next=head
        head=self.buckets[index]
        self.buckets[index]=newNode
        self.count+=1

m=Map()
m.insert("Parikh",2)
print(m.size())
m.insert("Rohan",7)
print(m.size())
m.insert("Parikh",9)
print(m.size())

