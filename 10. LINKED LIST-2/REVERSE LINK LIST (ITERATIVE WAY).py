
def reversel(head):
    if head is None:
        return None
    if head.next is None:
        return head

    previous=None
    current=head
    while(current is not None):
        next=current.next
        current.next=previous
        previous=current
        current=next
    head=previous
    return head

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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



# printing link list..............!!!!!
def printLink_List(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")

head=take_Input()
printLink_List(head)
head=reversel(head)
printLink_List(head)


