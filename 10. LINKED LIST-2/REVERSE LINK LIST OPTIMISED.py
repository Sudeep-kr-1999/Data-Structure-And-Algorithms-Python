def reversel(head):
    if head is None or head.next is None:
        return head,head

    smallhead,smalltail=reversel(head.next)
    smalltail.next=head
    head.next=None

    return smallhead,head


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
head,tail=reversel(head)
printLink_List(head)

