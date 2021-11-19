# <<<<<<<<<<<<<<<[ PRINTING GENERIC TREES]>>>>>>>>>>>>>>

class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

# def printTree(root):
#     # TOOOOO  what if root is none:
#     #printing in pre order.
#     # we are doing it for iterative way!!!!

#     if root==None:
#         return None
#     # the above if condition is not a base case it is the edge case( important)
#     # our base case is when root is leaf because when root is leaf for loop will not execute.!

#     print(root.data)
#     for child in root.children:
#         printTree(child)

def PrintTreeDetailed(root):
    if root is None:
        return None
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        PrintTreeDetailed(child)

n1=GenericTreeNode(5)
n2=GenericTreeNode(2)
n3=GenericTreeNode(9)
n4=GenericTreeNode(8)
n5=GenericTreeNode(7)
n6=GenericTreeNode(15)
n7=GenericTreeNode(1)


#connecting node for n1
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

#connecting node for n3
n3.children.append(n6)
n3.children.append(n7)
# printTree(n1)
PrintTreeDetailed(n1)




