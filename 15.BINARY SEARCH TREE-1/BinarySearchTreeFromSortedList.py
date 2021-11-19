# <<<<<<<<<<<<<<<<[ MAKE BINARY SEARCH TREE FROM THE SORTED LIST]>>>>>>>>>>>>>>>>>>>>>>>

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

def BSTFromTheSortedList(li):
    if len(li)==0:
        return None

    length=len(li)
    root_index=((length-1)//2)  #root index find kr ke left or right ko recursion mein bhej dege...!!
    root=BinaryTreeNode(li[root_index])

    left_sub_tree=BSTFromTheSortedList(li[0:root_index])
    right_sub_tree=BSTFromTheSortedList(li[root_index+1:])
    root.left=left_sub_tree
    root.right=right_sub_tree
    return root


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# root=takeLevelWiseTreeInput()
print("give sorted list for the formation of binary search tree :",end="")
li=[int(x) for x in input().split()]
root=BSTFromTheSortedList(li)
print("required the best possible binary search tree is :")
printTreeDetailed(root)

