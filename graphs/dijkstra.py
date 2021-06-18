""" Using matrices.
The following class can have arbitrary node labels. """

class Graph:

    def __init__(self,v):
        self.graph = [[0 for x in range(v)] for y in range(v)]
        self.map = {}           # To map the index of each node
        self.vertices = []
        self.index = 0


    # To add a node, add the node to the vertices list, set
    # its index, and increase the attr index by 1
    def addNodes(self,nodes):
        for i in nodes:
            self.vertices.append(i)
            self.map[i] = self.index
            self.index += 1


    def addEdges(self,edges):
        for u, v, weight in edges:
            self.graph[self.map[u]][self.map[v]] = weight
            self.graph[self.map[v]][self.map[u]] = weight


    def printGraph(self):
        print(self.graph)


    def bfs(self,src):
        visited = set()
        visited.add(src)
        q = [src]
        res = []

        while q:
            v = q.pop(0)
            res.append(v)

            # Get the index of the popped node to
            # check its adjacent vertices
            index = self.map[v]

            # Find adjacent vertices that have not been processed
            # and add them to the queue
            for k in range(len(self.vertices)):
                if self.graph[index][k] != 0 and self.vertices[k] not in visited:
                    q.append(self.vertices[k])
                    visited.add(self.vertices[k])
        return res


    # Returns node with the minimum distances of all
    # nodes not yet processed
    def minDistance(self,visited,dist):
        u, minVal = -1, float('inf')

        for i in range(len(self.vertices)):
            if dist[self.vertices[i]] < minVal and self.vertices[i] not in visited:
                minVal = dist[self.vertices[i]]
                u = self.vertices[i]

        return u


    # Finds the minimum distance from the source node to all other nodes
    def dijkstra(self,src):
        visited = set()
        dist = {i: float('inf') for i in self.vertices}
        dist[src] = 0

        for j in range(len(self.vertices)):

            # Finds node with minimum distance of vertices
            # that have not been processed
            u = self.minDistance(visited,dist)

            # Add node to the set and find its index
            visited.add(u)
            index = self.map[u]

            # For each adjacent node that has not been processed, if
            # the node's distance is greater than the current node's
            # distance plus the weight between them, change it.
            for v in range(len(self.vertices)):
                if self.graph[index][v] > 0 and self.vertices[v] not in visited \
                    and dist[self.vertices[v]] > dist[u] + self.graph[index][v]:
                    dist[self.vertices[v]] = dist[u] + self.graph[index][v]

        return dist


    # Returns the shortest path from the source node to the destination node
    """ Beginning of the algorithm is the same as dijkstra """
    def dijkstraPath(self,src,dest):
        visited = set()
        dist = {i: float('inf') for i in self.vertices}
        parent = {i: -1 for i in self.vertices}
        dist[src] = 0

        for j in range(len(self.graph)):
            u = self.minDistance(visited,dist)

            visited.add(u)
            index = self.map[u]

            for v in range(len(self.vertices)):
                if self.graph[index][v] > 0 and self.vertices[v] not in visited \
                    and dist[self.vertices[v]] > dist[u] + self.graph[index][v]:
                    dist[self.vertices[v]] = dist[u] + self.graph[index][v]
                    parent[self.vertices[v]] = u

        # Returns the path from the source to destination by
        # following parent nodes
        path = []
        cur = dest

        while cur != src:
            path.append(cur)
            cur = parent[cur]
        path.append(src)

        return list(reversed(path))


    # Returns the shortest path from the source node to all other nodes
    def allDijkstraPath(self,src):
        visited = set()
        dist = {i: float('inf') for i in self.vertices}
        parent = {i: -1 for i in self.vertices}
        dist[src] = 0

        for j in range(len(self.graph)):
            u = self.minDistance(visited,dist)

            visited.add(u)
            index = self.map[u]

            for v in range(len(self.vertices)):
                if self.graph[index][v] > 0 and self.vertices[v] not in visited \
                    and dist[self.vertices[v]] > dist[u] + self.graph[index][v]:
                    dist[self.vertices[v]] = dist[u] + self.graph[index][v]
                    parent[self.vertices[v]] = u

        # Creates an empty list for each vertice
        paths = {i: [] for i in self.vertices}

        # Iterates through each vertice and creates the path
        # by following the parent node
        for k in paths:
            paths[k] = self.createPath(k,parent)

        return paths


    # Creates a path list given a node and the parent list
    def createPath(self,i,parent):
        path = []

        # If no parent exists, append the node
        # to the list and return the list
        if parent[i] == -1:
            path.append(i)
            return path

        path = self.createPath(parent[i],parent)

        # After the function recurs to the base
        # case, the rest of the nodes are appended
        path.append(i)
        return path


g = Graph(9)
g.addNodes([1,2,3,4,5,6,7,8,9])

g.addEdges([(1,2,4),(1,8,8),(2,3,8),(2,8,11),(3,9,2),(3,4,7),(3,6,4),\
    (4,6,14),(4,5,9),(5,6,10),(6,7,2),(7,9,6),(7,8,1),(8,9,7)])

#g.printGraph()
print(g.dijkstraPath(3,5))
print(g.allDijkstraPath(1))
print(g.allDijkstraPath(3))


# ------------------------------------------------------------------------------------ #


""" When nodes are labeled 0 to n. Unlike the algorithm above, the
functions below add each node and edge separately.  """

class Graph1:

    def __init__(self,v):
        self.graph = [[0 for x in range(v)] for y in range(v)]
        self.vertices = []
        self.v = v


    def addNode(self,node):
        self.vertices.append(node)


    def addEdge(self,u,v,weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight


    def printGraph(self):
        print(self.graph)


    def bfs(self,src):
        visited = set()
        visited.add(src)
        q = [src]
        res = []

        while q:
            v = q.pop(0)
            res.append(v)

            for i in range(self.v):
                if self.graph[v][i] != 0 and i not in visited:
                    q.append(i)
                    visited.add(i)

        return res


    def minDistance(self,visited,dist):
        minVal, minIndex = float('inf'), -1

        for i in range(len(self.vertices)):
            if dist[self.vertices[i]] < minVal and self.vertices[i] not in visited:
                minVal = dist[self.vertices[i]]
                minIndex = i

        return minIndex


    def dijkstra(self,src):
        visited = set()
        dist = {i: float('inf') for i in range(len(self.vertices))}
        dist[src] = 0

        for j in range(len(self.vertices)):
            u = self.minDistance(visited,dist)

            visited.add(u)

            # Since each node is labeled 0-n, no mapping is needed
            for v in range(len(self.vertices)):
                if self.graph[u][v] > 0 and v not in visited \
                    and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist


g = Graph1(10)
g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)
g.addNode(5)
g.addNode(6)
g.addNode(7)
g.addNode(8)
g.addNode(9)

g.graph = [[0, 17, 16, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 14, 0, 0, 0],
        [0, 18, 0, 4, 12, 0, 0, 0, 0, 0],
        [11, 0, 0, 0, 0, 21, 0, 0, 0, 10],
        [0, 1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 13, 0, 3, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 6, 0, 15, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 10, 19],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 9, 0, 0, 0, 0],
        ]

print(g.dijkstra(0))
