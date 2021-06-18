# Description
"""
Spanning tree (ST)
- Subgraph of a connected, undirected graph that is a tree and connects all the
  vertices together
- A single graph can have many different spanning trees
- Weight of a ST = sum of the weight given to each edge in the ST

Minimum spanning tree (MST): spanning tree with weight less than or equal to the
weight of every other spanning tree

Edges of a ST/MST = V-1 edges

NOTE: A spanning tree only exists if the graph is connected

"""


# Kruskal
"""
Process:
    1. Sort all the edges in non-decreasing order of their weight
    2. Pick the smallest edge and check if it forms a cycle with the spanning tree
       formed so far. If no cycle is formed, include the edge. Else, discard it.
    3. Repeat step 2 until there are V-1 edges in the spanning tree

NOTE: For this algorithm, a detect cycle function on an unweighted graph is needed.

"""


# Prim
"""
Similar to Dijkstra's (only difference is the definition of key/distance)

- Greedy algorithm
- Always chooses node with smallest key
- Key of a node = shortest path from an adjacent node to that node
  (In Dijkstra's, key of a node = shortest path from source to that node)

"""


class Prim:

    def __init__(self,v):
        self.graph = [[0 for x in range(v)] for y in range(v)]
        self.map = {}
        self.vertices = []
        self.index = 0


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


    # Returns node with minimum key
    def getKey(self,visited,key):
        u, minVal = -1, float('inf')

        for i in range(len(self.vertices)):
            if key[self.vertices[i]] < minVal and self.vertices[i] not in visited:
                minVal = key[self.vertices[i]]
                u = self.vertices[i]

        return u


    # Finds a minimum spanning tree
    def prim(self):
        visited = set()
        key = {i: float('inf') for i in self.vertices}
        # Set the key for the node at index 0 to 0
        key[self.vertices[0]] = 0

        parent = {i: -1 for i in self.vertices}

        mst = 0         # To get mst number

        # Iterate through all the vertices
        for j in range(len(self.vertices)):

            # Finds node with minimum key of vertices
            # that have not been processed
            u = self.getKey(visited,key)

            # Add node to the set and find its index
            visited.add(u)
            index = self.map[u]

            # For each adjacent node that has not been processed, if
            # the node's key is greater than the weight between the
            # node and current node, change it.
            for v in range(len(self.vertices)):
                if self.graph[index][v] > 0 and self.vertices[v] not in visited \
                    and key[self.vertices[v]] > self.graph[index][v]:
                    key[self.vertices[v]] = self.graph[index][v]
                    parent[self.vertices[v]] = u

        # If MST value is needed, return mst
        for value in key.values():
            mst += value

        # Prints the MST with each edge
        # and its corresponding weight
        self.printMST(parent)


    def printMST(self,parent):
        print("Edge\tWeight")
        for i in range(1,len(self.vertices)):
            v = self.vertices[i]
            print(str(parent[v]) + " - " + str(v) + "\t" + \
                str(self.graph[self.map[v]][self.map[parent[v]]]))


g = Prim(9)
# g.addNodes([0,1,2,3,4,5,6,7,8])

# g.addEdges([(0,1,4),(0,7,8),(1,2,8),(1,7,11),(2,8,2),(2,3,7),(2,5,4),\
#     (3,5,14),(3,4,9),(4,5,10),(5,6,2),(6,8,6),(6,7,1),(7,8,7)])

g.addNodes([1,2,3,4,5,6,7,8,9])

g.addEdges([(1,2,4),(1,8,8),(2,3,8),(2,8,11),(3,9,2),(3,4,7),(3,6,4),\
    (4,6,14),(4,5,9),(5,6,10),(6,7,2),(7,9,6),(7,8,1),(8,9,7)])

print(g.prim())
