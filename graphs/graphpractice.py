# UNWEIGHTED UNDIRECTED GRAPHS

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
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

            (self.graph[u]).sort()
            (self.graph[v]).sort()


    def printGraph(self):
        return self.graph


    # Performs bfs on the graph
    """ Time complexity: O(V + E) for adjacency lists
                         O(V^2) for graphs

    If there are more than one components, a main bfs function is needed
    that loops over all unvisited vertices and calls this helper function. """
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


    # Performs dfs on the graph
    """ Time complexity: O(V + E) for adjacency lists
                         O(V^2) for graphs """
    def dfs(self,src):
        visited = set()
        res = []

        # Loop needed here if the graph has more than one component
        return self.dfsHelper(src,visited,res)

    def dfsHelper(self,v,visited,res):
        visited.add(v)
        res.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.dfsHelper(i,visited,res)
        return res


    # Finds the minimum number of edges from u to v
    """ Time algorithm: O(|E|+|V|)

    For a weighted graph, if fastest way from u to v is asked for, use this
    minimum edges algorithm. If cheapest way is asked for, use Dijkstra's """
    def minEdges(self,u,v):
        visited = set()
        visited.add(u)
        dist = {i: 0 for i in self.graph}
        count = 0
        q = [u]

        while q:
            val = q.pop(0)

            # For each unvisted adjacent vertice,
            # increase its distance by 1
            for i in self.graph[val]:
                if i not in visited:
                    dist[i] = dist[val] + 1
                    q.append(i)
                    visited.add(i)

        # Return the distance at destination node v
        return dist[v]



g = Graph()
g.addNodes([1,2,3,4,5,6])

g.addEdges([(1,2),(1,3),(2,3),(3,4),(4,5),(2,4),(6,5),(6,3)])


print(g.dfs(4))
