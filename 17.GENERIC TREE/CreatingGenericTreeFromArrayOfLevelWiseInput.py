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


def PrintTreeDetailed(root):
    if root is None:
        return None
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        PrintTreeDetailed(child)

class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

arr=[int(x) for x in input().split()]
root=levelwiseinput(arr)
print("THE REQUIRED TREE IS: ")
PrintTreeDetailed(root)

