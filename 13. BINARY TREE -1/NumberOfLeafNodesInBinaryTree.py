# <<<<<<<<<<<<<<<<<<<[ Number of Leaf Nodes In a Binary Tree]>>>>>>>>>>>>>>>>>>

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

def numLeafNodes(root):
    if root is None:
        return 0
    if root.left==None and root.Right==None:
        return 1
    numLeafLeft=numLeafNodes(root.left)
    numLeafRight=numLeafNodes(root.Right)
    return numLeafLeft+numLeafRight

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
printTreeDetailed(root)
print("number of leaf nodes in binary tree : ",numLeafNodes(root))
