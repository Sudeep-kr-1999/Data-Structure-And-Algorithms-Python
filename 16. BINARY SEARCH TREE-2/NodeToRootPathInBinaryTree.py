
# <<<<<<<<<<<<<<<<<<[ GIVEN A NODE FIND NODE TO ROOT PATH IN BINARY TREE IF NODE IS PRESENT IN THE BINARY TREE]>>>>>>>>>>>>>>>>>>>>>>>>>>

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

def nodeToRootPath(root,s):
    if root==None:
        return None
    if root.data==s:
        l=list()
        l.append(root.data)
        return l
    left_output=nodeToRootPath(root.left,s)
    if left_output!=None:
        left_output.append(root.data)
        return left_output
    right_output=nodeToRootPath(root.right,s)
    if right_output!=None:
        right_output.append(root.data)
        return right_output
    else:
        return None
# in this fuction output is the list....!!!!!!!!

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=takeLevelWiseTreeInput()
printTreeDetailed(root)
print(nodeToRootPath(root,5))

