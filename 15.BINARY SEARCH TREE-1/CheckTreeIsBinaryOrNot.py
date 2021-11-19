# <<<<<<<<<<<<<<<<<<<<<<<<<[ CHECK WETHER THE TREE IS BINARY SEARCH TREE OR NOT]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

def minTree(root):
    if root ==None:
        return 1000000000
    left_min=minTree(root.left)
    right_min=minTree(root.right)
    return min(left_min,right_min,root.data)

def maxTree(root):
    if root==None:
        return -100000000
    left_max=maxTree(root.left)
    right_max=maxTree(root.right)
    return max(left_max,right_max,root.data)

def isBST(root):
    if root==None:
        return True
    leftmax=maxTree(root.left)
    rightmin=minTree(root.right)
    if root.data>rightmin or root.data<=leftmax:
        return False
    isleftBST=isBST(root.left)
    isrightBST=isBST(root.right)
    return isleftBST and isrightBST



class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=takeLevelWiseTreeInput()
printTreeDetailed(root)
ans=(isBST(root))
if ans==True:
    print("YES THE GIVEN TREE IS BINARY SEARCH TREE")

else:
    print("NO THE GIVEN TREE IS NOT THE BINARY SEARCH TREE")

# for balanced tree time complexity=O(nlogn)
# for worst case tree time complexity is=O(n**2)

