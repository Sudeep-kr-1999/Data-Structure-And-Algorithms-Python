# <<<<<<<<<<<<<<[ FINDING NUMBER OF NODES IN A BINARY TREE]>>>>>>>>>>>>>>
def numNodes(root):
    if root is None:
        return 0
    left_count=numNodes(root.left)
    right_count=numNodes(root.Right)
    return 1+left_count+right_count
    # here in return statement if we donot add "1" corresponding to each nodes we will get zero as ans..!!!

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

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
printTreeDetailed(root)
print("total number of nodes in the binary tree is : ",numNodes(root))
