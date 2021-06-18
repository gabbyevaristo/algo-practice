# UNWEIGHTED DIRECTED GRAPHS

""" Using lists """
class Graph:

    def __init__(self):
        self.graph = {}
        self.edges = None
        self.time = 0


    # To add a node, add a key with the node label
    # and set its value to an empty list
    def addNodes(self,nodes):
        for i in nodes:
            self.graph[i] = []


    def addEdges(self,edges):
        self.edges = edges
        for u, v in edges:
            self.graph[u].append(v)
            #self.graph[v].append(u)
            (self.graph[v]).sort()
            #(self.graph[u]).sort()


    def printGraph(self):
        print(self.edges)


    def bfs(self,src):
        visited = set()
        visited.add(src)
        q = [src]
        res = []

        while q:
            v = q.pop(0)
            res.append(v)

            # For each unvisited adjacent vertice
            for i in self.graph[v]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
        return res


    def bfs(self,src):
        visited = set()
        visited.add(src)
        q = [src]
        res = [src]

        while q:
            cur = q.pop(0)
            for i in self.graph[cur]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
                    res.append(i)

        return res


    def bfs1(self,src):
        visited = set()
        visited.add(src)

        layers = [[src]]
        count = 0

        while layers[count]:

            temp = []
            for v in layers[count]:
                for i in self.graph[v]:
                    if i not in visited:
                        visited.add(i)
                        temp.append(i)

            layers.append(temp)
            count += 1

        for k in range(1,len(layers)-1):
            if len(layers[k]) == 1:
                return layers[k][0]


    def getIndegree(self):
        indegree = {i: 0 for i in self.graph}

        for i in self.graph:
            for v in self.graph[i]:
                indegree[v] += 1
        return indegree


    def isBipartite(self,src):
        visited = set()
        visited.add(src)

        q = [src]
        layer = {i: -1 for i in self.graph}
        layer[src] = 0

        while q:
            u = q.pop(0)

            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
                    layer[v] = layer[u] + 1

                elif layer[v] == layer[u]:
                    return False

        # If true, construct the partition
        x, y = [], []
        for i in layer:
            if layer[i] % 2 == 0:
                x.append(i)
            else:
                y.append(i)
        return (x,y)


    def isBipartite2(self,src):
        visited = set()
        visited.add(src)

        q = [src]
        layer = {i: -1 for i in self.graph}
        layer[src] = 0
        edges = set()

        while q:
            u = q.pop(0)

            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
                    layer[v] = layer[u] + 1

                if (u,v) not in edges and (v,u) not in edges:
                    edges.add((u,v))

        for j, k in edges:
            if layer[j] == layer[k]:
                return False
        return True


    def hasCycle(self):
        visited = set()
        start = {i: -1 for i in self.graph}
        finish = {i: -1 for i in self.graph}

        for u in self.graph:
            if u not in visited:
                self.hasCycleHelper(u,visited,start,finish)

        return (start,finish)


    def hasCycleHelper(self,u,visited,start,finish):
        visited.add(u)
        self.time += 1
        start[u] = self.time

        for v in self.graph[u]:
            if v not in visited:
                self.hasCycleHelper(v,visited,start,finish)

            elif finish[v] == -1:
                print("Cycle exists")

        self.time += 1
        finish[u] = self.time


g = Graph()
g.addNodes([1,2,3,4,5,6,7])

g.addEdges([(1,2),(2,3),(1,3),(6,3),(2,6),(2,4),(4,5),(5,6),(5,7)])

print(g.bfs(1))

# g.addNodes([1,2,3,4])
# g.addEdges([(1,3),(3,4),(1,4),(4,2),(1,2)])

# print(g.hasCycle())
