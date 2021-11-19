# <<<<<<<<<<<<<<<<<[ TAKE TREE INPUT FOR GENERIC TREE LEVEL WISE]>>>>>>>>>>>>>>>>>>>
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

import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root data:")
    rootData=int(input())
    if rootData==-1:
        return None
    root=GenericTreeNode(rootData)
    q.put(root)
    while(not q.empty()):
        current_node=q.get()
        print("Enter number of children for ",current_node.data)
        number_of_children=int(input())
        for i in range(number_of_children):
            print("Enter next child for :",current_node.data)
            childData=input()
            child_node=GenericTreeNode(childData)
            current_node.children.append(child_node)
            q.put(child_node)
    return root

root=takeTreeInputLevelWise()
PrintTreeDetailed(root)




