#<<<<<<<<<<<<<<<<<<<<<<<<<[ INTRODUCTION TO BASIC LINK LIST CONCEPT IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(13)
b=Node(15)
a.next=b
print(a.data)
print(b.data)
print(a.next.data)
print(a.next.next)
print(a)
print(a.next)
print(b)
# print(b.next.data)  # it give you the error because "b" donot have a next node so there is no data....!






