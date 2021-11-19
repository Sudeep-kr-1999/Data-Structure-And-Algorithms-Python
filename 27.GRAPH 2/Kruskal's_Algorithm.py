# <<<<<<<<<<<<<<<<<<<<<<<[ Kruskal's Algorithm in graphs ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)


def Kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key=lambda edge: edge.weight)
    count = 0
    output = []
    i = 0

    # do loop operation as long as count is less than (no. of vertices-1) when count reach the value (no of vertices-1) then loop will not work since
    # we need only (no.of vertices-1) edges................!!!!!!!!!!!
    while(count < nVertices-1):
        currentEdge = edges[i]
        source_parent = getParent(currentEdge.source, parent)
        destination_parent = getParent(currentEdge.destination, parent)

        if source_parent != destination_parent:
            output.append(currentEdge)
            count = count+1
            parent[source_parent] = destination_parent
        i = i+1
    return output


li = [int(ele) for ele in input().split()]
no_of_vertices = li[0]
no_of_edges = li[1]
edges = []

for i in range(no_of_edges):
    current_input = [int(ele) for ele in input().split()]
    src = current_input[0]
    dest = current_input[1]
    weight = current_input[2]
    edge = Edge(src, dest, weight)
    edges.append(edge)


print()
print("----------------------------Output-------------------------------")
print()

output = Kruskal(edges, no_of_vertices)
for edge in output:
    if edge.source < edge.destination:
        print(str(edge.source)+" "+str(edge.destination)+" "+str(edge.weight))
    else:
        print(str(edge.destination)+" "+str(edge.source)+" "+str(edge.weight))

# 4 4
# 0 1 2
# 1 3 3
# 0 2 5
# 2 3 8