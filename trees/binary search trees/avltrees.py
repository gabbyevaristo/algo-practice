# AVL (Adelson-Velskii and Landis) trees
""" Difference between height of left and right subtrees is at most 1 - HB(1) """


# Description
"""
    - Rotations are used to restore AVL property
    - Height attribute declared
    - Guarantees upper bound of O(logn) for all operations (insertion, deletion, search)
      since the height remains O(logn) after insertion and deletion
        * Most operations take O(h) time, where h is the height,
          and O(n) if the tree is skewed
"""


# AVL vs. red black
"""
Similarity:
    - Guarantee O(logn) for insertion, deletion, and search

Differences:
    - AVL is more strict in balancing (slightly bigger constant factor)
    - AVL has fast searches due to point above
    - RB is faster for insertion while AVL is faster for searcing

Few insertions/erasions and a lot of searches --> AVL
A lot of insertions/erasions and few searches --> Red black
"""


# Four violations
"""
Single rotation:    1. Insertion into left subtree of left child   (rotate right)
                    2. Insertion into right subtree of right child (rotate left)

Double rotation:    3. Insertion into left subtree of right child  (rotate left, then right)
                    4. Insertion into right subtree of left child  (rotate right, then left)
"""


# Insertion into AVL tree
"""
Similar to insertion into a BST. After insertion, we just need to check whether
there is a height imbalance. If so, call the appropriate rotation functions.
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):

    # Step 1 - Perform normal BST insertion
    if not root:
        return Node(key)
    elif key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Step 2 - Update height of ancestor node
    """ Height = max height of left subtree and right subtree """
    root.height = 1 + max(root.left.height, root.right.height)

    # Step 3 - Get the balance factor
    balance = root.left.height - root.right.height

    # Step 4 - If node is unbalanced, perform one of four cases
    # case 1 - left left
    if balance > 1 and key < root.left.data:
        return rightRotate(root)

    # case 2 - right right
    if balance < -1 and key > root.right.data:
        return leftRotate(root)

    # Case 3 - left right
    if balance > 1 and key > root.left.data:
        root.left = leftRotate(root.left)       # Note: rotate left on root.left
        return rightRotate(root)

    # Case 4 - right left
    if balance < -1 and key < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def leftRotate(node):
    y = node.right
    T2 = y.left
    y.left = node        # Perform rotation
    node.right = T2

    # Update heights
    node.height = 1 + max(node.left.height, node.right.height)
    y.height = 1 + max(y.left.height, y.right.height)

    return y


def rightRotate(node):
    y = node.left
    T3 = y.right
    y.right = node      # Perform rotation
    node.left = T3

    # Update heights
    node.height = 1 + max(node.left.height, node.right.height)
    y.height = 1 + max(y.left.height, y.right.height)

    return y
