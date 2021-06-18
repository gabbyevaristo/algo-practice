"""
Note: max depth of a tree = max height of a tree
"""

# If the node is a leaf, then lDepth and rDepth return 0. The
# program will then return 1 for the parent of that leaf.

def maxDepth(node):
    if node is None:
        return 0

    # Compute the depth of each subtree
    lDepth = maxDepth(node.left)
    rDepth = maxDepth(node.right)

    # Use the larger depth
    if (lDepth > rDepth):
        return lDepth + 1
    else:
        return rDepth + 1

def maxDepth1(root):
    # Base case
    if root is None: return 0

    # If node is a leaf, then depth = 1
    elif root.left is None and root.right is None:
        return 1

    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
