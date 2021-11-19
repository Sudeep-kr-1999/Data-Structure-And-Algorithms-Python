# <<<<<<<<<<<<<[ PRINT NODES AT DEPTH "K" IN THE BINARY TREE]>>>>>>>>>>>>>>


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

def printDepthK(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    printDepthK(root.left,k-1)
    printDepthK(root.Right,k-1)


# another way of printing nodes at depth k....!!!!!
def printDepthKV2(root,k,d=0):
    if root==None:
        return
    if k==d:
        print(root.data)
        return
    printDepthKV2(root.left,k,d+1)
    printDepthKV2(root.Right,k,d+1)

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
printTreeDetailed(root)
printDepthK(root,2)
printDepthKV2(root,2)

