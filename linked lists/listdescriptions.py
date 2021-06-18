# Time complexity for arrays and singly/doubly linked lists
"""
                                    Arrays        Singly LL      Doubly LL

Access an element                    O(1)           O(n)           O(n)
Add/remove first element             O(n)           O(1)           O(1)
Add last element                     O(1)           O(n) w/o tail  O(1)
                                                    O(1) w/ tail
Delete last element                  O(1)           O(n)           O(1)
Add in middle                        O(n)           O(n)           O(n)
Delete in middle                     O(n)           O(n)           O(n)
Wasted space                          0             O(n)           O(n^2)
Search                           O(n) for linear    O(n)           O(n)
                               O(logn) for binary

"""


# Arrays
"""
Advantages:
    - Elements can be accessed in constant time by index
        ~ Direct random access method
        ~ Address of element = address of base array + offset
    - Good spacial locality as elements are stored contiguously

Disadvantages:
    - Fixed size capacity (static)
    - Preallocates all needed memory up front (wastes memory space for empty slots)
    - Insertion and deletion at interior positions is expensive as elements need to be shifted

"""


# Linked lists (singly and doubly)
"""
Advantages:
    - Size is not fixed (max size depeonds on the heap)
    - Able to add new elements without needing to copy or reallocate
    - Does not waste memory space (but does take some extra memory for pointers)
    - Insertions and deletions at interior positions are not as expensive as in arrays

Disadvantages:
    - Elements cannot be efficiently accessed by an index (elements stored randomly)
        ~ Sequential access method
    - Reference pointers take up space
    - Not cache friendly (no locality of reference)


For doubly linked lists,
    - More advantages:
        ~ Deletion of the last element can be done in constant time

    - More disadvantages
        ~ Each node requires an extra pointer
        ~ Insertion/deletion takes a bit longer (more pointer operations)

"""


# Circular linked lists
"""
Advantages:
    - Any node can be a starting point (list can be traversed from any point)
    - Useful for queue implementation
        ~ Can maintain a pointer to the last node and front can be called by next of last
    - Useful in round-robin applications

Disadvantages:
    - Inefficient for long lists
    - Difficult to manipulate (e.g. reversing the list)

"""


# Unrolled linked lists
"""
* Combine array advantages (small memory overhead) with benefits of linked lists (fast insertion/deletion)
* Array capacity is usually at 75% to make insertion quicker
* Can reduce search time if elements are in ascending order

Advantages:
    - Lower overhead for entire list
    - Linear search is faster due to cache behavior
        ~ Entire array is cached so elements in the same array do not need to be imported again
    - Requires less storage space for references
    - Insertion/deletion/traversal is quicker

Disadvantages:
    - Overhead per node for references and elements is high compared to a node in a singly linked list
        ~ Has to also store number of elements
    - Not a good data structure if you need a large number of insertions

"""


# Skip lists
"""
* Can be used as an alternative to balanced binary trees (almost half of nodes is skipped after comparison w/ root)
* Nodes have many next (forward) references
* Size of the node = number of levels in a node

Advantages:
    - Search is quicker (number of comparisons is reduced) = O(logn)

Disadvantages:

"""