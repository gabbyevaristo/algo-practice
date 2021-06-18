# Time complexity
"""
In normal binary trees, searching has a worst case time complexity of O(n). BSTs reduce
the worst case average search operation to O(logn) ~ height of the tree.

In cases where the tree is skewed, however, the time complexity remains O(n). To reduce
this, height restrictions between the left and right subtree are imposed. This is the
idea behind balanced BSTs.

"""


# Inorder predecessor and successor of a node X
"""
If X has two children, then its predecessor is the maximum value in its left subtree
and its successor is the minimum value in its right subtree.

If X does not have a left child, then its predecessor is its first left ancestor.

"""


# Advantages of BST over hash tables
"""
Hash tables support search, insert, and delete in O(1), while BSTs at best (balanced BSTs)
work in O(logn). Why BSTs then?

Advantages:
    - Able to get keys in sorted order by doing an inorder traversal (not a natural
      operation with hash tables)
    - Easier to implement (usually rely on libraries to implement hashing)
"""
