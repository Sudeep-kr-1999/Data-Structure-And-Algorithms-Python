from StackUsingLL import Stack

s=Stack()
s.push(12)
s.push(13)
s.push(15)

while s.isEmpty() is False:
    print("Poped element is : ",s.pop())
s.top()