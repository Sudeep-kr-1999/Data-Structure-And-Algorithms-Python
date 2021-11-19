# <<<<<<<<<<<<<<<<<[ CREATING NODES IN BINARY TREE]>>>>>>>>>>>>>>>>>>>>>>>>>>>

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(4)
btn3=BinaryTreeNode(5)

btn1.left=btn2  #btn2 is the left child of btn1!
btn1.Right=btn3  # btn3 is the right child of btn1!!


