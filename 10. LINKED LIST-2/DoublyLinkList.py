# <<<<<<<<<<<<<<<<<<<<<<<[ Doubly link list]>>>>>>>>>>>>>>>>>>>>>>>>
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None


def doubly_link_list_inserting_forward(input_arr):
    head=None
    tail=None
    for currentdata in input_arr:
        if currentdata==-1:
            break

        newnode=Node(currentdata)
        if head is None:
            head=newnode
            tail=newnode
        else:
            duplicate=tail
            tail.next=newnode
            tail=newnode
            tail.previous=duplicate

    return head,tail

def print_doubly_link_list_forward(head):
    if head is None:
        print("None")
        return
    temp=head
    while temp is not None:
        print(str(temp.value)+" <==> ",end="")
        temp=temp.next
    print("None")
    return


def print_doubly_link_list_backward(tail):
    if tail is None:
        print("None")
        return

    temp_1=tail
    while temp_1 is not None:
        print(str(temp_1.value)+" <==> ",end="")
        temp_1=temp_1.previous
    print("None")



print("Enter the space sepreated input to enter in the doubly link list : ",end="")
input_arr=[int(x) for x in input().split()]

head,tail=doubly_link_list_inserting_forward(input_arr)
print()
print("the forward doubly link list is: ",end="")
print_doubly_link_list_forward(head)
print()
print("the backward doubly link list is: ",end="")
print_doubly_link_list_backward(tail)
print()





