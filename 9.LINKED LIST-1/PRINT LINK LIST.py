# <<<<<<<<<<<<<<<<<<<<[ how to print linked list ]>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creating link list..................!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def take_Input():
    print("enter the element for the  nodes of link list: ",end=" ")
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

# printing link list..............!!!!!
def printLink_List(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")

printLink_List(head)



