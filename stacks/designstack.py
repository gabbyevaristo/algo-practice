# Implement a stack with push, pop, find middle and delete middle operations in
# O(1) time complexity
"""
What data structure to use?
    - O(n) for deleting the middle element of an array
    - Not possible to move the middle pointer up and down in a singly linked list
    - Solution: doubly linked list

Push operation:
    Create a new node, set its previous pointer to None and its next pointer to the
    current head, and increase the size by 1. If the size is 1 (only one node), then
    set that node to mid. Else, set the current head's previous pointer to the new
    node, and if the size is even, set mid.prev to mid. Otherwise, the mid is left
    as is. Set the new node to the head.

        if size is 1:
            mid = newNode
        else:
            head.prev = newNode
            if count is even:
                mid = mid.prev

Pop operation:
    If there are no elements, raise an error. Else, store the value of the current
    head (to return it at the end) and then set the head to head.next. If the list
    does not become empty, set head.prev to None, then decrease the size. If the
    size is odd, set mid.next to mid. Return the stored value of the old head.

Find middle operation:
    If there are no elements, raise an error. Else, return mid.data.

"""


# Implement two stacks in an array
class twoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size


    """ Push an element to stack 1 """
    # Let's say you default top1 to 0. If there is room, you would first set arr[0]
    # to the element and then increase top1 by 1. If you call pop, it will attempt
    # to pop arr[1] instead of arr[0]. Top should equal index you are adding at.
    def push1(self, x):
        if self.top1 < self.top2 - 1:       # If there is space for an element
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("Stack overflow")


    """ Push an element to stack 2 """
    def push2(self, x):
        if self.top1 < self.top2 - 1:       # If there is space for an element
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
        else :
           print("Stack overflow")


    """ Pop from stack 1 """
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 -1
            return x
        else:
            print("Stack underflow")


    """ Pop from stack 2 """
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack underflow ")



# Create a mergable stack that has the following operations in O(1)
#       a. push(Stack s, x)             Adds an item x to stack s
#       b. pop(Stack s)                 Removes the top item from stack s
#       c. merge(Stack s1, Stack s2)    Merges contents of s2 into s1
"""
* Cannot use an array since merging two arrays takes O(n) time

Linked list with two pointers at the head and tail:
    a. Push: add at the head
    b. Pop: delete from the head
    c. Merge: s1.tail.next = s2.head

If an extra pointer is not allowed, use a circular linked list, where you
keep track of the last node (since node.next = head/top):
    a. Push: add new item as tail.next
    b. Pop: delete tail.next (tail.next = tail.next.next)
    c. Merge: s1.tail.next = s2.tail.next and s2.tail = last
"""



# Design a stack such that getMinimum() is O(1)
# O(n) space complexity
"""
Method 1:
    Take an auxiliary stack, say min stack, that maintains the minimum value in the stack.
    We only push to the min stack when the value being pushed onto the main stack is less
    than or equal to the current min value. We only pop from the min stack when the value
    we pop from the main stack is equal to it. At any point, if we want to get the minimum,
    we just return the top element from the min stack.

        push(element):
            append element to mainStack
            if minStack is empty or top of minStack >= element:
                append element to minStack

        pop():
            if mainStack is empty:
                return -1
            temp = pop from mainStack
            if temp == top of minStack:
                pop from minStack
            return temp
"""

def push(mainStack, minStack, element):
    mainStack.append(element)
    # If minStack is empty or element is less than the current minimum value,
    # push the value onto the minStack
    if not minStack or element <= minStack[-1]:
        minStack.append(element)

def pop(mainStack, minStack):
    if not mainStack:
        return -1
    temp = mainStack.pop()
    # If the value being popped is equal to the top of the minStack, pop it as well
    if temp == minStack[-1]:
        minStack.pop()
    return temp

def getMinimum(minStack):
    return minStack[-1]
