# <<<<<<<<<<<<<<<<<<<<<[ PRINTING BINARY TREES]>>>>>>>>>>>>>>>>>>
def printTree(root):
    if root ==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.Right)
   # it will just print data but do not give the exact picture of it...!


# def printTreeDetailed(root):
#     if root ==None:
#         return
#     print(root.data,end=":")
#     print("L",root.left.data,end=",")
#     print("R",root.Right.data)
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.Right)
#     # here we get an error:----> " 'NoneType' object has no attribute 'data'"!
#    # it will just print data but do not give the exact picture of it...!


# corrected print function for trees...!!!!!!!!
def printTreeDetailed(root):
    if root ==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.Right!=None:
        print("R",root.Right.data,end="")
    print()

    printTreeDetailed(root.left)
    printTreeDetailed(root.Right)


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)
btn5=BinaryTreeNode(5)




btn1.left=btn2  #btn2 is the left child of btn1!
btn1.Right=btn3  # btn3 is the right child of btn1!!
btn2.left=btn4
btn2.Right=btn5
printTree(btn1)
printTreeDetailed(btn1)

