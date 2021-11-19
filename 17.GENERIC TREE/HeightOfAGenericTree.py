# <<<<<<<<<<<<<[ FINDING HEIGHT OF GENERIC TREE]>>>>>>>>>>>>>>>>>>>>>>>

## Read input as specified in the question.
## Print output as specified in the question.
class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

import queue 
def levelwiseinput(arr):
    if len(arr)==None:
        return None
    root_data=arr[0]
    root=GenericTreeNode(root_data)
    q = [root]
    i=1
    while(i<len(arr)):
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = GenericTreeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def heightofgenerictree(root):
    if root==None:
        return 0
    if len(root.children)==0:
        return 1
    largest_child_height=heightofgenerictree(root.children[0])
    for i in range(1,len(root.children)):
        child_height=heightofgenerictree(root.children[i])
        if child_height>=largest_child_height:
            largest_child_height=child_height
    return largest_child_height+1

# PRINT ARRAY FOR LEVEL WISE INPUT!!!!!!!!!!!
arr=[int(x) for x in input().split()]
root=levelwiseinput(arr)
print(heightofgenerictree(root))
