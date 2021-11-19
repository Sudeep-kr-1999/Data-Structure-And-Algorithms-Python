# <<<<<<<<<<<<<<<[ binary tree from "preorder" and "inorder" of the binary tree]>>>>>>>>>>>>>>>>>>>>

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

def buildTreeFromPreorderAndInorder(pre,inorder):
    if len(pre)==0:
        return None
    rootData=pre[0]
    root=BinaryTreeNode(rootData)
    rootIndexInInorder=-1
    for i in range(0,len(inorder)):
        if inorder[i]==rootData:
            rootIndexInInorder=i
            break
    if rootIndexInInorder==-1:
        return None
    leftInOrder=inorder[0:rootIndexInInorder]  #slicing concept
    RightInOrder=inorder[rootIndexInInorder+1:]

    lengthOfLeftSubTree=len(leftInOrder)
    leftPreOrder=pre[1:lengthOfLeftSubTree+1]
    RightPreOrder=pre[lengthOfLeftSubTree+1:]

    leftChild=buildTreeFromPreorderAndInorder(leftPreOrder,leftInOrder)
    rightChild=buildTreeFromPreorderAndInorder(RightPreOrder,RightInOrder)
    root.left=leftChild
    root.Right=rightChild
    return root

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.Right=None

import sys
sys.setrecursionlimit(11000)
pre=[1,2,4,3,5,7,8,6]
inorder=[4,2,1,7,5,8,3,6]
root=buildTreeFromPreorderAndInorder(pre,inorder)
print("the tree given by the user : ")
printTreeDetailed(root)