# <<<<<<<<<<<<<<<[ check whether the tree is balance or not]>>>>>>>>>>>>>>>>>>>>>>>>
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


def height(root):
    if root==None:
        return 0
    return 1 +max(height(root.left),height(root.Right))

# VERY VERY IMPORTANT LOGIC.....!!!!!!!!!
def isTreeBalanced(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.Right)
    if lh-rh>1 or rh-lh>1:
        return False
    isLeftBalanced=isTreeBalanced(root.left)
    isRightBalanced=isTreeBalanced(root.Right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

# better function for isbalanced check....!!!
def getHeightAndCheckBalanced(root):
    if root==None:
        return 0,True
    lh,isLeftBalanced=getHeightAndCheckBalanced(root.left)
    rh,isRightBalanced=getHeightAndCheckBalanced(root.Right)
    h=1+max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return h,False
    if isLeftBalanced and isRightBalanced:
        return h,True
    else:
        return h,False
    #height and isbalanced function dono ek saath kaam  kr rha h.....!!!!

# if you want recursive call to return 2 things you also need to return 2 things as well....!!!!

# for return only result for isbalanced nothing else not any height...!!!!
def isBalanced2(root):
    h,isRootBalanced=getHeightAndCheckBalanced(root)
    return isRootBalanced


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

root=treeInput()
print("the tree given by the user : ")
printTreeDetailed(root)
# print(isTreeBalanced(root))
# print(isBalanced2(root))
print(getHeightAndCheckBalanced(root))
