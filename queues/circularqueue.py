# Circular queue is best implemented using a linked list


# Enqueue
"""
    if not front:
        front = newNode
    else:
        tail.next = newNode
    tail = newNode
    tail.next = front

"""

# Dequeue
"""
    if not front:
        return Error
    elif front == tail:         # one node
        value = front.data
        front = tail = None
    else:                       # multiple nodes
        value = front.data
        front = front.next
        tail.next = front
    return value

"""
