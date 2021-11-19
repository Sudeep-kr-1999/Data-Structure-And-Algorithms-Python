# <<<<<<<<<<<<<<<[ Print Tree Level Wise]>>>>>>>>>>>>>>>>>>>>>>

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

import queue
def printLevelWiseTree(root):
    if root is None:
        return None
    q=queue.Queue()
    q.put(root)
    while(not q.empty()):
        current_node=q.get()
        print(current_node.data,end="")
        print(":",end="")
        length=len(current_node.children)
        for child in current_node.children:
            print(child.data,end="")
            length=length-1
            if length!=0:
                print(",",end="")
            q.put(child)
        print()


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print("THE REQUIRED TREE IS AS FOLLOWS")
printLevelWiseTree(tree)
