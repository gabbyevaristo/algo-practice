""" Performed on a directed acyclic graph """


class Graph:

    def __init__(self):
        self.graph = {}
        self.indegree = {}


    def addNodes(self,nodes):
        for i in nodes:
            self.graph[i] = []

            # Set new node's indegree to 0
            self.indegree[i] = 0


    # Since graph is directed, only increase
    # the indegree of the second node paremeter
    def addEdges(self,edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.indegree[v] += 1
            (self.graph[u]).sort()


    def printGraph(self):
        return self.indegree


    # Returns a topological sort on the graph
    def topological(self):
        q, res = [], []

        # Since indegree is altered, make a copy
        # of it to be used in the algorithm
        indegree = self.indegree

        # Append all nodes of indegree 0 to the queue
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.pop(0)
            res.append(u)

            # For each adjacent vertice, decrease its indegree
            # by 1. If the indegree falls to 0, append it to
            # the queue.
            for v in self.graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return res


    def getIndegree(self):
        indegree = {i: 0 for i in self.graph}

        for i in self.graph:
            for v in self.graph[i]:
                indegree[v] += 1
        return indegree




g = Graph()
# g.addNodes([2,3,5,7,8,9,10,11])

# g.addEdges([(7,11),(7,8),(5,11),(3,8),(3,10),(11,2),(11,9),(11,10),(8,9)])

g.addNodes([0,1,2,3,4])

g.addEdges([(0,1),(1,2),(2,3),(2,4),(3,0),(4,3)])
print(g.getIndegree())
print(g.topological())
