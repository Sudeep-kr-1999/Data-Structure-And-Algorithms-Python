# <<<<<<<<<<<<<<<<[ BEST SOLUTION FOR REVERSING A LINK LIST]>>>>>>>>>>>>>>>>>>>


# very very impotant approach......................!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def reversel(head):
    if head is None or head.next is None:
        return head
    smallhead=reversel(head.next)
    tail=head.next # if we logically see the tail of the smaller link list is just the head.next of the previous link list so we donot
                  # need to iterate from smallhead to the last to find the tail of the link list and we just use the logic and reverse the
                  # link list................!!!!!!!!!!!!!!!!
    tail.next=head
    head.next=None

    return smallhead

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

