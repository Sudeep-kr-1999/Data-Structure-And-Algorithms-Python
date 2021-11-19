# <<<<<<<<<<<<<<<<[ link list input-2]>>>>>>>>>>>>>>
# it has the time complexity of order n..!

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
        else:                # optimized code.......!!!( very very important)!!!!
            tail.next=newNode # purane tail ke reference mein next node ka address store krege !
            tail=newNode     #purane node mein next node ka reference store krne ke baad tail ko aage bhadyaege means newnode ko tail bna dege!
    return head


head=take_Input()

# printing link list..............!!!!!
def printLink_List(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")

printLink_List(head)


