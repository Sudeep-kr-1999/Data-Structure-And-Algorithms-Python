# <<<<<<<<<<<<<<<<<<<<[ Largest Data In A Binary Tree]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

def largestData(root):
    if root is None:
        return -1  # idealy return "-inf"
    leftLargest=largestData(root.left)
    rightLargest=largestData(root.Right)
    #here we use inbuilt max function ........(very very important)!!!
    largest=max(leftLargest,rightLargest,root.data)
    return largest

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
printTreeDetailed(root)
print("the largest data in the tree is : ",largestData(root))
