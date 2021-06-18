# Queue applications: CPU scheduling, asynchronous data transfer



# Using lists
"""
Easy to implement, but there are speed issues that come with pop operations.
To remove a value, the value at index 0 is removed, and all subsequent values
are shifted downwards, making removal O(n).

"""

# Using deque
"""
from collections import deque
queue = deque()                 # Creates an empty queue

    - Uses append and popleft
    - Preferred for quicker append and pop operations
        * O(1) compared to list's O(n) time complexity
"""

# Using Queue
"""
from queue import Queue
queue = Queue(maxsize=3)     # if maxsize is not declared, the queue size is infinite

Functions:
    - maxsize       Number of items allowed in the queue
    - empty()       Returns true if the queue is empty, false otherwise
    - full()        Returns true if there are maxsize items in the queue
    - get()         Removes and returns an item from the queue
    - put(item)     Puts an item into the queue
    - qsize()       Returns the number of items in the queue
"""
