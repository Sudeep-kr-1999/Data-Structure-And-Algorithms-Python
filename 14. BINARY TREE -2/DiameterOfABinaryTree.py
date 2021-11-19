# <<<<<<<<<<<<<<<<<<<<<<<<<[ finding diameter of a binary tree]>>>>>>>>>>>>>>>>>>>>>>>>

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# very very important logic:
def heightwithdiameter(root):
    if root is None:
        return 0,0
    lh,leftDiameter=heightwithdiameter(root.left)
    rh,rightDiameter=heightwithdiameter(root.right)
    h=1+max(lh,rh)

    return h, max((lh+rh+1),leftDiameter,rightDiameter)  # very very important step.....!!!
    # NOTE:---- here lh is for left height and rh is for right height and "+1" is for root itself because it is also included in the
               # diameter

def diameter(root):
    h,diameter=heightwithdiameter(root)
    return diameter


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(diameter(root))