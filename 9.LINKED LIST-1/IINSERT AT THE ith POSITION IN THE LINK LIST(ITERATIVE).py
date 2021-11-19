class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    print(count)
    return count


def insertAtI(head,i,data):
    if (i<0 or i>length(head)):   # condition is important....................!!!!!!!!!!!
        return head
    count=0
    current=head
    previous=None
    while(count<i):
        #order is important here..............!
        previous=current
        current=current.next
        count=count+1
    newNode=Node(data)
    if previous is not None:         #note:--------> condition for khi bhi middle mein or tail mein insert krne ke liye.....!!!!!!!!!
        previous.next=newNode
    else:                # note:----> kyuki agar previous none hua to uska koi mtlb nhi hoga kuyki uske paas koi data or refrerence store krne ka block nhi hoga...!!
        head=newNode
    newNode.next=current

    return head


def take_Input():
    inputList=[int(x) for x in input().split()]
    head=None
    tail=None
    for currentdata in inputList:
        if currentdata==-1:
            break
        newNode=Node(currentdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head


head=take_Input()

# printing link list..............!!!!!
def printLink_List(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")

printLink_List(head)
head=insertAtI(head,6,6)
printLink_List(head)
head=insertAtI(head,0,9)
printLink_List(head)
head=insertAtI(head,7,10)
printLink_List(head)
