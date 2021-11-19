# <<<<<<<<<<<<<<<<<<[ RANGE BASED SOLUTION FOR THE ISBST PROBLEM(ANOTHER SOLUTION)]>>>>>>>>>>>>>>>>>>>>>>>>>>

def printTreeDetailed(root):
    if root ==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()

    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

import queue
def takeLevelWiseTreeInput():
    q=queue.Queue()
    print("Enter Root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of ",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of ",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root

# def minTree(root):
#     if root ==None:
#         return 1000000000
#     left_min=minTree(root.left)
#     right_min=minTree(root.right)
#     return min(left_min,right_min,root.data)

# def maxTree(root):
#     if root==None:
#         return -100000000
#     left_max=maxTree(root.left)
#     right_max=maxTree(root.right)
#     return max(left_max,right_max,root.data)

# def isBST2(root):
#     if root==None:
#         return 10000000,-1000000000,True
#     leftmin,leftmax,isleftBST=isBST2(root.left)
#     rightmin,rightmax,isrightBST=isBST2(root.right)
#     minimum=min(leftmin,rightmin,root.data)
#     maximum=max(leftmax,rightmax,root.data)

#     isTreeBST=True
#     if root.data<=leftmax or root.data>rightmin:
#         isTreeBST=False
#     if not(isleftBST) or not(isrightBST):
#         isTreeBST=False
#     return minimum,maximum,isTreeBST


def isBST3(root,min_range,max_range):
    if root==None:
        return True
    if root.data<min_range or root.data>max_range:
        return False
    isLeftWithinConstraint=isBST3(root.left,min_range,root.data-1)
    isRightWithinConstraint=isBST3(root.right,root.data,max_range)

    return isLeftWithinConstraint and isRightWithinConstraint

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=takeLevelWiseTreeInput()
printTreeDetailed(root)
print((isBST3(root,-1000000,100000000)))
# for balanced tree time complexity=O(n)
# for worst case tree time complexity is=O(n)

