# <<<<<<<<<<[ printing elements in binary tree which are in range form "k1" to "k2"]>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<[ searching data in binary search tree]>>>>>>>>>>>>>>>>>>>>>>>>>
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

def printBetweenK1andK2(root,k1,k2):
    if root==None:
        return None
    if root.data>k2:
        printBetweenK1andK2(root.left,k1,k2)
    elif root.data<k1:
         printBetweenK1andK2(root.right,k1,k2)
    else:
        print(root.data)
        printBetweenK1andK2(root.left,k1,k2)
        printBetweenK1andK2(root.right,k1,k2)




class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=takeLevelWiseTreeInput()
printTreeDetailed(root)
printBetweenK1andK2(root,5,10)
