# <<<<<<<<<<<<<<<<<[ FINDING NUMBER OF NODES IN GENERIC TREE]>>>>>>>>>>>>>>>>

class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()


def PrintTreeDetailed(root):
    if root is None:
        return None
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        PrintTreeDetailed(child)

def takeTreeInput():
    print("Enter root data")
    rootData=int(input())
    if rootData==-1:
        return None
    root=GenericTreeNode(rootData)
    print("Enter number of children for :",rootData)
    childrenCount=int(input())
    for i in range(childrenCount):
        child=takeTreeInput()
        root.children.append(child)
    return root


def numnodes(root):
    #edge case : -----------> if root==None then there is no node so count of nodes will be zero(0)!

    if root==None:
        return 0
    # we donot need to write the base case here..!!
    count=1
    for child in root.children:
        count=count+numnodes(child)
    return count


root=takeTreeInput()
PrintTreeDetailed(root)
print("TOTAL NUMBER OF NODES IN TREE : ",numnodes(root))








