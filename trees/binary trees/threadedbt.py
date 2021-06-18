# Also called stack/queue-less traversals

# Issues with regular BT traversals
"""
    - Storage space required for stack/queue is large
    - Majority of pointers are NULL
        * A tree with n nodes has n+1 NULL wasted pointers
"""

# Uses
"""
    - Makes inorder traversal faster (does so without using recursion or a stack)
    - Fast access of ancestors nodes
"""

# Single vs. double threaded
"""
Single threaded: NULL right pointer is made to point to inorder successor
Double threaded: both left and right NULL pointers are made to point to inorder
                 predecessor and inorder successor, respectively

Note: Can also work for pre/post order traversals
"""

# How it works (for double threaded)
"""
Declare bool attributes (lthread and rthread) that indicate whether the right/
left pointer points to a child or an inorder predecessor/successor
    If true: pointer points to a thread
    If false: pointer points to a child
"""
