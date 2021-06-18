# Up to the programmer to decide which node to search

# Insert into unrolled linked list
"""
1. Find node e
2. If the number of elements in e is less than the capacity
    2a. Insert element into e
    2b. Increase the size of e by 1
3. If the number of elements in e is greater than or equal to the capacity,
    3a. Create a new node e1 and place it after e
    3b. Move the final half of e into e1
    3c. Insert element into e1
    3d. Divide the number of elements in e by 2
    3e. Declare size of e1

"""


# Delete in unrolled linked list
"""
1. Find element in node e
2. Remove the element from e
3. Decrease the size of e by 1
4. As long as the number of elements in e is less than the capacity (e.size/2),
    4a. Put the element from e.next in e
    4b. Decrease the number of elements in e.next
    4c. Increase the number of elements in e
5. If the number of elements in e.next is less than the capacity,
    5a. Merge nodes e and e.next
    5b. Delete node e.next

"""
