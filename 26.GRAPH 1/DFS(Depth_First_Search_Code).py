# <<<<<<<<<<<<<<<[ DFS( Depth first search in graph code)]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]
                          for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfs_helper(self, starting_vertex, visited):
        print(starting_vertex)
        visited[starting_vertex] = True
        for i in range(self.nVertices):
            if self.adjMatrix[starting_vertex][i] > 0 and visited[i] == False:
                self.__dfs_helper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]

        # taking care of disconnected graph also vey important...................!!!!!!!!!!!!!!!!
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfs_helper(i, visited)

    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)


g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(4, 6)
g.dfs()
