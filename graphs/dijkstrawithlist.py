""" Using lists """

class Graph:

    def __init__(self):
        self.graph = {}


    # To add a node, add a key with the node label
    # and set its value to an empty list
    def addNodes(self,nodes):
        for i in nodes:
            self.graph[i] = []


    def addEdges(self,edges):
        for u, v, weight in edges:
            self.graph[u].append((v,weight))
            self.graph[v].append((u,weight))

            (self.graph[u]).sort()
            (self.graph[v]).sort()


    def printGraph(self):
        return self.graph


    # Returns node with the minimum distances of all
    # nodes not yet processed
    def minDistance(self,visited,dist):
        minVal, minDist = -1, float('inf')

        for i in dist:
            if dist[i] < minDist and i not in visited:
                minDist = dist[i]
                minVal = i

        return minVal


    # Finds the minimum distance from the source node to all other nodes
    def dijkstra(self,src):
        visited = set()
        dist = {i: float('inf') for i in self.graph}
        dist[src] = 0

        for j in range(len(self.graph)):

            # Finds node with minimum distance of vertices
            # that have not been processed
            u = self.minDistance(visited,dist)

            visited.add(u)

            # For each adjacent node that has not been processed, if
            # the node's distance is greater than the current node's
            # distance plus the weight between them, change it.
            for v, weight in self.graph[u]:
                if v not in visited and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight

        return dist


    # Returns the shortest path from the source node to the destination node
    """ Beginning of the algorithm is the same as dijkstra """
    def dijkstraPath(self,src,dest):
        visited = set()
        dist = {i: float('inf') for i in self.graph}
        parent = {i: -1 for i in self.graph}
        dist[src] = 0

        for j in range(len(self.graph)):
            u = self.minDistance(visited,dist)

            visited.add(u)

            for v, weight in self.graph[u]:
                if v not in visited and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    parent[v] = u

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
        dist = {i: float('inf') for i in self.graph}
        parent = {i: -1 for i in self.graph}
        dist[src] = 0

        for j in range(len(self.graph)):
            u = self.minDistance(visited,dist)

            visited.add(u)

            for v in self.graph[u]:
                if v[0] not in visited and dist[v[0]] > dist[u] + v[1]:
                    dist[v[0]] = dist[u] + v[1]
                    parent[v[0]] = u

        # Creates an empty list for each vertice
        paths = {i: [] for i in self.graph}

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



g = Graph()
g.addNodes([1,2,3,4,5,6,7,8,9])

g.addEdges([(1,2,4),(1,8,8),(2,3,8),(2,8,11),(3,9,2),(3,4,7),(3,6,4),\
    (4,6,14),(4,5,9),(5,6,10),(6,7,2),(7,9,6),(7,8,1),(8,9,7)])


#print(g.printGraph())
#g.dijkstraPath(3,5)
print(g.allDijkstraPath(1))
print(g.allDijkstraPath(3))
