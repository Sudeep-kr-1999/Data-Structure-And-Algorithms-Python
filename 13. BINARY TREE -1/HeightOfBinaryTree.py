# <<<<<<<<<<<<<<[ FINDING HEIGHT OF A BINARY TREE]>>>>>>>>>>>

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

def treeInput():
    rootData=int(input())
    #if user input is "-1" then it means it is None! means no new node will be created..!!
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.Right=rightTree
    return root

#FINDING HEIGHT OF THE BINARY TREE..............!!!!!!!!
def heightOfBinaryTree(root):
    if root==None:
        return 0
    left_height=heightOfBinaryTree(root.left)
    right_height=heightOfBinaryTree(root.Right)
    max_height=0
    if left_height>=right_height:
        max_height=left_height
    else:
        max_height=right_height

    return 1+max_height

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
print("tree given by the user is follows :")
printTreeDetailed(root)
print("height of the binary tree is :",end=" ")
print(heightOfBinaryTree(root))


