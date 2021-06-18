# UNWEIGHTED DIRECTED GRAPHS

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
            (self.graph[u]).sort()


    def printGraph(self):
        print(self.graph)


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


    # Determine if there is a path from u to v
    """ In an undirected graph, a path from u to v does not exist if and
    only if the graph is not connected. """
    def detectPath(self,u,v):
        visited = set()
        visited.add(u)
        q = [u]

        while q:
            m = q.pop(0)

            # If the destination node is reached,
            # a path from u to v exists
            if m == v:
                return True

            for i in self.graph[m]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
        return False


    # Print all the paths from u to v
    def printPaths(self,u,v):
        visited = set()
        path = []
        self.printPathsHelper(u,v,visited,path)

    def printPathsHelper(self,u,v,visited,path):
        # Adds the node to the visited set and the path
        visited.add(u)
        path.append(u)

        # If current node equals destination node,
        # print the path
        if u == v:
            print(path)

        # Else, call function on all unvisted adjacent vertices
        else:
            for i in self.graph[u]:
                if i not in visited:
                    self.printPathsHelper(i,v,visited,path)

        # Once path is printed, remove the last value
        # from both the path and visited set
        path.pop()
        visited.remove(u)


    # Count the paths from u to v
    def countPaths(self,u,v):
        visited = set()
        count = [0]
        self.countPathsHelper(u,v,visited,count)
        return count[0]

    def countPathsHelper(self,u,v,visited,count):
        visited.add(u)

        # Increment count if current node equals destination node
        if u == v:
            count[0] += 1

        # Else, call function on all unvisted adjacent vertices
        else:
            for i in self.graph[u]:
                if i not in visited:
                    self.countPathsHelper(i,v,visited,count)

        # Remove node from visited set
        visited.remove(u)



g = Graph()
g.addNodes([0,1,2,3,4,5])

g.addEdges([(1,2),(1,3),(1,5),(2,4),(2,5),(3,5),(4,3)])

g.printGraph()
print(g.countPaths(1,5))

# print(g.printPaths(1,3))
# print(g.countPaths(1,3))
