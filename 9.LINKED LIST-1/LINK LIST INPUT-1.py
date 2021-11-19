# <<<<<<<<<<<<<[ LINKED LIST INPUTS-1]>>>>>>>>>>>>>>>>>>>>>>

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def take_Input():
    inputList=[int(x) for x in input().split()]
    head=None
    for currentdata in inputList:
        if currentdata==-1:
            break
        newNode=Node(currentdata)
        if head is None:
            head=newNode
        else:
            current=head
            while current.next is not None:
                current=current.next
            current.next=newNode

    return head


head=take_Input() 
print(head)
