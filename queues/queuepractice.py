# Reverse a queue
def reverseQueue(queue):
    stack = []

    while queue:            # Deque all elements and add them to a stack
        stack.append(queue.pop(0))

    while stack:            # Pop all elements and add them back to the queue
        queue.append(stack.pop())
    return queue


# Reverse a queue, recursively
""" In main, create a queue, call reverseQueueRecur(queue), and then print the queue. """
def reverseQueueRecur(queue):
    # Pops all values off the queue. Once it hits the last value, it adds all values
    # back into the empty queue.
    if not queue:
        return

    x = queue.pop(0)
    reverseQueue(queue)
    queue.append(x)


# Reverse the order of the first k elements of a queue
def reverseKElements(queue,k):
    if not queue or k > len(queue):
        return -1

    stack = []
    for i in range(k):                  # Dequeues k elements and adds them to a stack
        stack.append(queue.pop(0))
    while stack:                        # Adds the k elements to the back of the queue
        queue.append(stack.pop())
    for i in range(len(queue)-k):       # Wraps the rest of the values to the back of the queue
        queue.append(queue.pop(0))
    return queue


# Alternate values in a stack
def alternateQueue(queue):
    if len(queue) % 2 != 0:
        return -1

    stack, mid = [], len(queue) / 2

    for i in range(mid):                # Put first half into a stack
        stack.append(queue.pop(0))
    while stack:                        # Add reversed first half to the back of queue
        queue.append(stack.pop())
    for i in range(mid):                # Add second half of list to the back of queue
        queue.append(queue.pop(0))
    for i in range(mid):                # Put first half into the stack again
        stack.append(queue.pop(0))
    while stack:                        # Interweave the elements by popping off the stack
        queue.append(stack.pop())       # and dequeuing from the queue
        queue.append(queue.pop(0))
    return queue


# Find the maximum of all subarrays of size k
def maximum(arr,k):
    q, result = [], []

    # Process the first window
    for i in range(k):
        # Remove the previous smaller elements from the back, so that
        # the front of the queue holds the largest value
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    # Start at index k. Each window looks at index of current element minus
    # k to current element.
    for i in range(k,len(arr)):
        # Element at the front of the queue is the largest element in
        # the previous window
        result.append(arr[q[0]])

        # Remove elements that are out of the window. These elements
        # will be at the front of the queue
        while q and q[0] <= i-k:
            q.pop(0)

        # Remove all elements smaller than the currently added element
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

    result.append(arr[q[0]])
    return result

def findMax(arr):
    arr.sort()
    return arr[-1]


arr = [8,53,43,23,23,34,5465,34,54]
print(findMax(arr))

#print(maximum([12,1,1,90,57,89,56],2))
