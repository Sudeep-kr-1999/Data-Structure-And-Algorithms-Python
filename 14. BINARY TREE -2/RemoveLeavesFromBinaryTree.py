# <<<<<<<<<<<<<<<[ Removing Leaves From Binary Tree]>>>>>>>>>>>>>>>>>>>>

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

def remmoveLeaves(root):
    if root==None:
        return None
    if root.left==None and root.Right==None:
        return None

    # if write it simply it will not update the binary tree as expected....!
    # remmoveLeaves(root.left)
    # remmoveLeaves(root.Right)


    # so we are required to write like this.....!!
    # leaf remmove krne ke baad jo tree left and right side mein bcch jaayega usse root ko link kr dege aur recursion baaki kaam kr dega...!
    # very very important step!!!!!!!!
    root.left=remmoveLeaves(root.left)
    root.Right=remmoveLeaves(root.Right)
    return root


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
print("the tree given by the user : ")
printTreeDetailed(root)
remmoveLeaves(root)
print("the tree after removing its leaves is below :")
printTreeDetailed(root)
