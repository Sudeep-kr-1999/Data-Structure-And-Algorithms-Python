# <<<<<<<<<<<<<<<[ BFS (Breadth first search traversal in graphs)]>>>>>>>>>>>>>>>>>>>>>

from os import rename, truncate
import queue
from queue import Empty
import sys


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]
                          for j in range(nVertices)]

    def addEdge(self, v1, v2,wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

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

    def __bfshelper(self, starting_vertex, visited):
        q = queue.Queue()
        q.put(starting_vertex)
        visited[starting_vertex] = True
        while q.empty() is False:
            u = q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):

        # taking care of disconnected graph very important here also....................!!!!!!!!!!!!!!!
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] == False:
                self.__bfshelper(i, visited)

    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)


    def __get_minVertex(self,visited,weight):
        min_vertex=-1
        for i in range(self.nVertices):
            if (visited[i] is False and (min_vertex==-1 or weight[min_vertex]>weight[i])):
                min_vertex=i
        return min_vertex
    def prims(self):
        visited= [False for i in range(self.nVertices)]
        parent=[-1 for i in range(self.nVertices)]
        weight=[sys.maxsize for i in range(self.nVertices)]

        for i in range(self.nVertices-1):
            min_vertex=self.__get_minVertex(visited,weight)
            visited[min_vertex]=True

            # explore the neighbour of the min vertex which is not visited and update the weight corresponding to them if required!
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j]>0 and visited[j] is False:
                    if (weight[j]>self.adjMatrix[min_vertex][j]):
                        weight[j]=self.adjMatrix[min_vertex][j]
                        parent[j]=min_vertex

        for i in range(1,self.nVertices):
            if i<parent[i]:
                print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
            else:
                print(str(parent[i])+" "+str(i)+" "+str(weight[i]))

li=[int(ele) for ele in input().split()]
n=li[0]
E=li[1]

g=Graph(n)
for i in range(E):
    current_input=[int(ele) for ele in input().split()]
    g.addEdge(current_input[0],current_input[1],current_input[2])
g.prims()
