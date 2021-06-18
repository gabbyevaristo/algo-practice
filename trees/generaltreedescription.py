# Edge of T: a pair of nodes (u,v) such that u is the parent of v, or vice-versa


# Height of T = max(depth of T's leaves) = Depth of T
    # Note: Height and depth of individual nodes could be different, however

# Depth of p
"""
p = position of a node of tree T
depth of p = number of ancestors of p, excluding p itself

Recursively:
    If p == root, depth of p = 0
    Else, depth of p = 1 + depth of the p's parent

Time complexity:
    O(dp + 1): algorithms runs one more than the depth of p ~ O(n)
"""
def depth(self, p):
    if self.isRoot(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))


# Height of p
"""
Recursively:
    If p == a leaf, height of p = 0
    Else, height of p = 1 + max(height of p's childrens)
"""
def height(self, p):
    if self.isLeaf(p):
        return 0
    else:
        return 1 + max(self.height(c) for c in self.children(p))


# Size of p
"""
    size of p = number of descendants of p, including itself
              = height of p + 1
"""
