# <<<<<<<<<<<<<<<<[ STRUCTURE OF BST CLASS]>>>>>>>>>>>>>>>>>>

# basic structure of the BST CLASS!
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:

    def __init__(self):
        self.root=None
        self.numnodes=0

    def printTreeHelper(self,root):
        if root ==None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print("L",root.left.data,end=",")
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)


    def printTree(self):
        self.printTreeHelper(self.root)

    def isPresentHelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            #call on left
            return self.isPresentHelper(root.left,data)
        else:
            #call on right
            return self.isPresentHelper(root.right,data)
    def isPresent(self,data):
        # if self.root is None:
        #     return False
        # if self.root.data==data:
        #     return True
        # if self.root.data>data:
        #     # isPresent(root.left,data)    #not possible
        #     # isPresent(data)  #leads to infinite recursion
        #     #call on left
        #     pass
        # else:
        #     #call on right (not possible)!!!
        #     pass
        # for solving above issue we made isPresentHelper() function which take root as argument and can help us reaching recursion..!


        return self.isPresentHelper(self.root,data)
    def insertHelper(self,root,data):
        if root==None:
            Node=BinaryTreeNode(data)
            return Node
        if root.data>data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root

    def insert(self,data):
        self.numnodes+=1
        self.root=self.insertHelper(self.root,data)
        # self.root is used if root will change it will reflect in it!!!
    def min(self,root):
        if root is None:
            return 10000000
        if root.left==None:
            return root.data
        else:
            return self.min(root.left)
            # note:==== minumum hamesha left side ya root wala hi hoga kyuki root ke right sb root se large hota h!

    def deleteDataHelper(self,root,data):
        if root==None:
            return False,None
        if root.data<data:
            deleted,new_right_node=self.deleteDataHelper(root.right,data)
            root.right=new_right_node
            return deleted,root
        if root.data>data:
            deleted,new_left_child=self.deleteDataHelper(root.left,data)
            root.left=new_left_child
            return deleted,root
        else:#------------>(root.data==data)

            #root as leaf.
            if root.left==None and root.right==None:
                return True,None

            #root has one child
            if root.left==None:
                return True,root.right
            if root.right==None:
                return True,root.left

            #root has 2 children
            replacement=self.min(root.right)
            root.data=replacement

            # it will delete replacement from the right side!!!
            deleted,newRightNode=self.deleteDataHelper(root.right,replacement)
            root.right=newRightNode
            return True,root

    def deletedata(self,data):
        # return False #WETHER DATA IS PRESENT IN THE BST!
        deleted,newroot=self.deleteDataHelper(self.root,data)
        if deleted:
            self.numnodes-=1
        self.root=newroot
        return deleted
    def count(self):
        return self.numnodes


b=BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()
# print(b.count())
# b.deletedata(8)
# b.printTree()
# b.deletedata(5)
# b.printTree()
b.deletedata(10)
b.printTree()
