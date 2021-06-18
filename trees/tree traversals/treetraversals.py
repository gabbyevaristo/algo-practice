# Inorder (left, root, right)
"""
Gives nodes in ascending order

Algorithm:
    1. Traverse left subtree, i.e. call Inorder(left-subtree)
    2. Visit root
    3. Traverse right subtree, i.e. call Inorder(right-subtree)
"""

# Preorder (root, left, right)
"""
Used to create a copy of the tree

Algorithm:
    1. Visit root
    2. Traverse left subtree, i.e. call Preorder(left-subtree)
    3. Traverse right subtree, i.e. call Preorder(right-subtree)
"""

# Postorder (left, right, root)
"""
Used to delete the tree

Algorithm:
    1. Traverse left subtree, i.e. call Postorder(left-subtree)
    2. Traverse right subtree, i.e. call Postorder(right-subtree)
    3. Visit root
"""

# Breadth first
"""
- Visit all positions at depth d before visiting positions at depth d+1

Algorithm:
    Initialize queue Q to contain T.root
    while Q not empty:
        p = Q.dequeue       # front of queue
        add p to result
        add p's left child to Q
        add p's right child to Q

"""
