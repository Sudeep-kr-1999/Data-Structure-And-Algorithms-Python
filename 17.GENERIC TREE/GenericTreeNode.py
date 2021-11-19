# <<<<<<<<<<<<<<<<<<<<<<<<[ Generic Tree Node Class]>>>>>>>>>>>>>>>>>>>>>>>.

class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

n1=GenericTreeNode(5)
n2=GenericTreeNode(2)
n3=GenericTreeNode(9)
n4=GenericTreeNode(8)
n5=GenericTreeNode(7)
n6=GenericTreeNode(15)
n7=GenericTreeNode(1) 


#connecting node for n1
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

#connecting node for n3
n3.children.append(n6)
n3.children.append(n7)



