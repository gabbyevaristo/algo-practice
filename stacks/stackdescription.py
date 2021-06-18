# Using lists
"""
Easy to implement, but there are speed issues as the list grows. Since items
are stored next to each other in memory, if the stack grows bigger than the
block of memory that holds it, Python will need to do some memory allocations.
"""

# Using deque
"""
from collections import deque
stack = deque()                 # Creates an empty stack

    - Uses append and pop (similar to lists)
    - Preferred for quicker append and pop operations
        * O(1) compared to list's O(n) time complexity
"""

# Using LIFOQueue
"""
from queue import LifoQueue
stack = LifoQueue(maxsize=3)     # if maxsize is not declared, 0 is used as default

Functions:
    - maxsize       Number of items allowed in the queue
    - empty()       Returns true if the queue is empty, false otherwise
    - full()        Returns true if there are maxsize items in the queue
    - get()         Removes and returns an item from the queue
    - put(item)     Puts an item into the queue
    - qsize()       Returns the number of items in the queue
"""
