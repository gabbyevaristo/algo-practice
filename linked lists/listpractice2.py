class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Add an element to the back of the list
    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:         # Stops at the last element in the list
                cur = cur.next
            cur.next = newNode
        self.size += 1

    # Print the list
    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


    # Move the last element to the front
    def moveLastToFront(self):
        if not self.head or not self.head.next:     # Exits if list is empty or size of list = 1
            return
        cur = self.head
        while cur.next.next:        # At the end of the loop, cur = second to last element
            cur = cur.next
        cur.next.next = self.head
        self.head = cur.next
        cur.next = None


    # Makes the middle node the head node
    def makeMiddleHead(self,element):
        if not self.head or not self.head.next:
            return

        slow = fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow                 # At the end, prev = node before the middle node
            slow = slow.next            # At the end, slow = middle node
            fast = fast.next.next

        prev.next = slow.next
        slow.next = self.head
        self.head = slow
        """prev.next = slow.next         # Just this line will delete the middle node"""


    # Swap elements pair wise (changing data values)
    def swapByData(self):
        if not self.head or not self.head.next: return
        cur = self.head
        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next


    # Swap elements pair wise (changing pointers)
    def swapByPointers(self):
        if not self.head or not self.head.next: return
        cur, prev = self.head, None
        count = 0           # Created to declare head in the first iteration

        while cur and cur.next:
            if prev:
                prev.next.next = cur.next
            prev = cur.next
            cur.next = cur.next.next
            prev.next = cur
            if count == 0:
                self.head = prev
            cur = cur.next
            count += 1


    # Swap two given nodes without changing their data
    def swapNodes(self,x,y):
        prevX = curX = None
        prevY = curY = None
        cur, prev = self.head, None

        while cur:
            if cur.data == x:       # If x is found, set prevX to prev value and curX to cur value
                prevX = prev
                curX = cur
            if cur.data == y:       # If y is found, set prevY to prev value and curY to cur value
                prevY = prev
                curY = cur
            prev = cur
            cur = cur.next

        if not curX or not curY: return         # If x or y is not found in the list
        if prevX:                   # If x isn't the head, set x's previous value to y
            prevX.next = curY
        else:
            self.head = curY        # If x is the head, set y to be the head
        if prevY:                   # If y isn't the head, set y's previous value to x
            prevY.next = curX
        else:
            self.head = curX        # If y is the head, set x to be the head

        curX.next, curY.next = curY.next, curX.next     # Swap the next values of x and y


    # Detect loop in linked list
    """
    1. Hashing (similar to removing duplicates in an unsorted list)
        Iterate through the list as long as cur is not None. If the node (not the value)
        is not in the set, add it to the set. If the node is in the set, there is a loop.

    2. Fast and slow pointers
        Start both pointers at the head. Iterate through the list as long as fast and fast.next
        is not None. Set slow to slow.next and fast to fast.next.next. If slow is equal to fast,
        there is a loop.
    """

    # Find starting point of the loop in a linked list
    """
        Following method 2 from above. Once you find the collision point, set slow to the list's
        head. Move both fast and slow 1 unit forward. Where they meet is the starting point.
    """

    # Find the length of a loop in a linked list
    """
        Use second approach above. Once the loop is detected, start a count.
        Once slow is equal to fast, set count to 1 and slow to slow.next. As long as slow.next
        does not equal to fast (the end of the loop), increment count and move slow to slow.next.
    """


    # Rotate the list counter-clockwise by k nodes
    def rotateList(self,k):
        if not self.head or k == 0: return

        cur, count = self.head, 0
        kthNode = None

        while cur.next:
            count += 1
            if count == k:
                kthNode = cur
            cur = cur.next

        if not kthNode: return      # Returns if k is greater than the number of nodes in the list
        cur.next = self.head        # Sets the last value's next ptr to the head
        self.head = kthNode.next
        kthNode.next = None


    # Retain M nodes and then delete N nodes
    def retainAndDelete(self,M,N):
        cur = self.head
        while cur:
            for _ in range(M-1):        # Skip M nodes. Stop at M-1 to be at the last M value kept
                cur = cur.next
                if not cur: return      # Exits if M is greater than the list size
            for _ in range(N):      # Bypass N values
                if not cur.next: return
                cur.next = cur.next.next
            cur = cur.next



l1 = LinkedList()
l1.append(9)
l1.append(9)
l1.append(7)
l1.append(10)
l1.append(6)
l1.append(5)
l1.append(2)
l1.append(3)
l1.append(5)

l1.retainAndDelete(3,3)
l1.printList()
