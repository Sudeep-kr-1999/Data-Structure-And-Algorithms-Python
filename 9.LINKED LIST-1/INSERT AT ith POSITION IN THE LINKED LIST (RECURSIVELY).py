class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# def length(head):
#     count=0
#     while head is not None:
#         count=count+1
#         head=head.next
#     return count

def insertAtIR(head,i,data):

    if i<0:
        return head
    if i==0:
        # head mein insert krna sbse aasan hota h.........! to sbse phele hum insertion wale index ko chota krte krte index 0 bnayege tb usme first pr insert krke 
        #smalloutput mein head ko us returned list se jor dege to get the final complete link list...............!!!!!!!!!!!!!!!
        newNode=Node(data)
        newNode.next=head
        return newNode
    # order is important........!!!!!!!!!!!!!!
    if head is None:
        return None

    smallhead=insertAtIR(head.next,i-1,data)
    head.next=smallhead
    return head

# def insertAtI(head,i,data):
#     if (i<0 or i>length(head)):
#         return head
#     count=0
#     current=head
#     previous=None
#     while(count<i):
#         #order is important here..............!
#         previous=current
#         current=current.next
#         count=count+1
#     newNode=Node(data)
#     if previous is not None:
#         previous.next=newNode
#     else:
#         head=newNode
#     newNode.next=current

#     return head


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
head=insertAtIR(head,2,6)
printLink_List(head)
head=insertAtIR(head,0,9)
printLink_List(head)
head=insertAtIR(head,7,10)
printLink_List(head)
