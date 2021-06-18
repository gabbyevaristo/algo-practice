# Used to implement priority queues

# Priority queue implementations
"""
                        Insertion      Deletion     Find min/max

Unordered array           O(1)           O(n)           O(n)
Unordered LL              O(1)           O(n)           O(n)
Ordered array             O(n)           O(1)           O(1)
Ordered LL                O(n)           O(1)           O(1)
BST                      O(logn)        O(logn)       O(logn)    (all on average)
Balanced BST             O(logn)        O(logn)       O(logn)    (all in worst case)
Binary heap              O(logn)        O(logn)         O(1)


Finding min/max in a balanced BST is O(logn), but can be implemented to be O(1) by
keeping an extra pointer to the min/max. Since heaps are implemented using arrays,
however, there is a better locality of reference. They are also easier to implement,
do not require extra space for pointers, and can be built in O(n) time, instead of
balanced BST's O(nlogn) time.

"""


# Heap implementation (best way to implement a PQ)
"""
Implemented using ARRAYS as they form complete BTs (no location wastage)

One way of declaration:
    def __init__(capacity, heapType):
        self.arr = []                   # empty heap
        self.count = 0                  # current number of elements in heap
        self.capacity = capacity        # max values allowed
        self.heapType = heapType        # max or min heap
"""


# Properties
"""
1   All leaves should be at level h
2   Max/min (depending on heap) is stored at arr[0]

3   Parent of node at ith location:       (i-1)/2
4   Children of node at ith location:     (2*i)+1 and (2*i)+2

5   Min and max number of elements in a heap of height h:
        Min:     2^h
        Max:     2^(h+1)-1    (complete tree)

6   Height of a heap with n elements = logn
        2^h <=  n   <= 2^(h+1)-1
          h <= logn <= h+1
"""
