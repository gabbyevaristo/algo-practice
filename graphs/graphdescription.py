# Terminology
"""
Graph: a pair (V,E), where V is a set of nodes (vertices) and E is a collection
       of pairs of vertices (edges)

Degree of a vertex: number of edges incident on it

Path: a sequence of vertices v1,v2,...,vk such that for any consecutive pair of
      vertices vi, vi+1 is joined by an edge in the graph

Simple path: a path with no repeated vertices

Cycle: a path where the first and last vertices are the same
       (Simple cycle: a cycle with no repeated vertices or edges, except the
       first and last)

Strongly connected: if there is a path from every vertex to every other vertex
                    (If a graph is not connected, it consists of a set of
                    connected components)

Tree: a strongly connected undirected graph with no cycles
      (acyclic connected graph)

Spanning tree: a subgraph that contains all of that graph's vertices and is a
               single tree

Forest: disjoint set of trees

Spanning forest: the union of spanning trees of its connected components

Bipartite graph: a graph whose vertices can be divided into two sets such that
                 all edges connect a vertex in one set with a vertex in the other

Complete graph: a graph with all edges existing

Network: directed, weighted graphs

Sparse graph: if edges < |V|log|V|

E can range anywhere from 0 to |V|(|V|-1)/2

"""


# Graph representations
"""
Adjacency matrix:
    - Good when graphs are dense (number of edges ~ V^2)

    Pros: removing an edge takes O(1) time; determining whether there is an edge
          is efficient - O(1)
    Cons: consumes more space that lists, even if the graph is sparse; adding a
          vertex takes O(V^2) time

        Space:                  V^2
        Check an edge:          1
        Iterate over v's edges: V


Adjacency list:
    - List of lists where index i represents the ith vertex OR dictionary of lists

    Pros: saves space; adding a vertex is easy
    Cons: determining whether there is an edge is O(V) (not efficient)

        Space:                  E+V
        Check an edge:          1
        Iterate over v's edges: degree(v)

"""


# DFS applications
"""
DFS numbers: order in which the vertices are processed

1. Minimum spanning tree and all-pair shortest path tree for unweighted graphs
2. Cycle detection in undirected graph (either or can be used)
3. Path finding (either or can be used)
4. Topological sorting
5. Test if a graph is bipartite (either or can be used)
6. Finding (strongly) connected components
7. Solving puzzles with only one solution, such as mazes
8. Finding cut vertices (articulation points)

"""


# BFS applications
"""
1. Shortest path and minimum spanning tree for unweighted graphs
2. Peer-to-peer networks
3. Social networking websites (find people with a given distance from a person)
4. GPS navigation systems
5. Cycle detection in undirected graph (either or can be used)
6. Test if a graph is bipartite (either or can be used)
7. Path finding (either or can be used)
8. Finding all nodes within one connected component (either or can be used)

"""
