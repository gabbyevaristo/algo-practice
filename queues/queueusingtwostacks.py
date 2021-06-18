# Using two stacks
class QueuesTwoStacks:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.size = 0


    """ Enqueue to the queue """
    # Add the element to s1. Move all elements one-by-one from s1 to s2
    # by popping. Then move elements back to s1.
    def enqueue(self,val):
        self.size += 1

        while self.s1:                  # Move elements from s1 to s2
            x = self.s1.pop()
            self.s2.append(x)

        self.s1.append(val)             # Add to s2

        while self.s2:                  # Move elements back to s1
            x = self.s2.pop()
            self.s1.append(x)

    """ Deque from the queue"""
    # If s1 is empty, the queue is empty. Else, decrease the size
    # and return the value at the 0th index of s1.
    def dequeue(self):
        if not self.s1:
            return -1
        self.size -= 1
        return self.s1.pop()


    def getSize(self):
        return self.size


q = QueuesTwoStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
