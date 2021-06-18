# Using one queue
"""
Assumes we can find the size (s) of the queue at any point.

Push: Enqueue x to the queue, then one-by-one deque s items from the
queue and enqueue them.
    Ex:  queue = [3,2,1,0]
         push(4)
         queue = [3,2,1,0,4]
"""
class StackOneQueue:

    def __init__(self):
        self.q = []
        self.size = 0


    """ Push to the stack """
    def push(self,val):
        self.q.append(val)
        self.size += 1

        for i in range(self.size-1):
            x = self.q.pop(0)
            self.q.append(x)


    """ Pop from the stack"""
    def pop(self):
        if not self.q:
            return -1
        self.size -= 1
        return self.q.pop(0)


    """ Return the top element in the stack """
    def top(self):
        if not self.q1:
            return -1
        return self.q[0]


    def getSize(self):
        return self.size


# ----------------------------------------------------------------------- #


# Using two queues
class StackTwoQueues:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.size = 0


    """ Push to the stack """
    # Add the element to q2. Move all elements one-by-one from
    # q1 to q2 by dequeing. Then, swap the names of q1 and q2.
    def push(self,val):
        self.q2.append(val)                     # Add to q2
        self.size += 1

        while self.q1:
            x = self.q1.pop(0)
            self.q2.append(x)

        self.q1, self.q2 = self.q2, self.q1     # Swap the names


    """ Pop from the stack"""
    # If q1 is empty, the stack is empty. Else, decrease the size
    # and return the value at the 0th index of q1.
    def pop(self):
        if not self.q1:
            return -1
        self.size -= 1
        return self.q1.pop(0)

    """ Return the top element in the stack """
    def top(self):
        if not self.q1:
            return -1
        return self.q1[0]


    def getSize(self):
        return self.size


s = StackOneQueue()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.getSize())
print(s.pop())
print(s.pop())
