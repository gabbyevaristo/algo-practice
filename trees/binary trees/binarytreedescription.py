# Degenerate/pathological tree
""" When every node has only one child

    Performance is the same as a linked list
"""


# Proper/full BT
""" When each node has either 0 or 2 children

    # of external nodes = # of internal nodes + 1
"""


# Complete BT
""" When all levels are completely filled except for the last level and the last
level is filled from left to right (possible for a node to only have one child)

    # of nodes = between 2^h and 2^(h+1)-1     (h of root = 0)
    # of nodes = between 2^(h-1) and 2^h + 1   (h of root = 1)
"""


# Perfect BT
""" When all levels are completely filled - all nodes have two children and all
leaves are at the same level

    # of nodes = 2^(h+1)-1     (h starting at 0)
    # of leaf nodes = 2^h

    Level h has 2^h nodes
        Level 0 = 1 node    (2^0)
        Level 1 = 2 nodes   (2^1)
        Level 2 = 4 nodes   (2^2)
        Level 3 = 8 nodes   (2^3)
"""


# Array vs. linked list representation
"""
Drawbacks of arrays:
    - Some update operations (e.g. deleting a node) cannot be efficiently supported
        * Must update the positions of its children
    - Space usuage depends on tree's shape (may have a number of empty cells)
"""


# Trees vs. arrays and linked lists
"""
- Searching: faster than LLs, but slower than arrays
- Insertion/deletion: faster than arrays, but slower than unordered LLs
"""


# Traversal space complexities
"""
Level order traversal is O(w), where w is the maximum width of the BT
    (queue stores)

Depth first traversal is O(h), where h is the maximum height of the BT
    (stack stores all ancestors of a node on the call stack)

For level order, more space when the tree is balanced, and for depth first,
more space when the tree is less balaned (skewed)
"""
