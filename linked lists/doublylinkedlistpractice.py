class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Add element to the tail
    def addElement(self,element):
        newNode = Node(element)
        if self.size == 0:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
        self.size += 1

    def printList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


    # Delete the element at the given index
    def deleteAtIndex(self,index):
        if not self.head or index < 0: return

        cur = self.head
        # Traverse until the node to be deleted is reached
        for _ in range(index):
            if not cur: return
            cur = cur.next              # Cur will point to node to be deleted after loop

        if cur == self.head:            # If node to be deleted is the head
            self.head = cur.next
        elif not cur.next:              # If node to be deleted is the tail
            cur.prev.next = None
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev


    # Remove duplicates in an unsorted and sorted list
    """
        Both methods are similar to their singly linked list counterparts. An extra step is
        added to correct the prev pointer. If the deleted node is not the tail (cur.next is
        not None), then set cur.next.prev to cur. If the deleted node is the tail, then
        cur.next is None and attempting to set None.prev will fail.
    """


   # Remove the given value in the list, given that it only appears once
    def deleteOneVal(self,val):
        if self.head.data == val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur:
                if cur.data == val:
                    cur.prev.next = cur.next
                    return
                cur = cur.next


    # Remove the given value in the list, given that it can appear multiple times
    def deleteMultVal(self,val):
        while self.head and self.head.data == val:
            self.head = self.head.next

        if not self.head: return        # Can occur if list only contained the passed in value

        cur = self.head
        while cur:
            if cur.data == val:
                cur.prev.next = cur.next
                if cur.next:            # If the key is the tail, cur.next = None
                    cur.next.prev = cur.prev
            cur = cur.next


    # Find pairs with a given sum in a sorted linked list
    def findPairsWithGivenSum(self,sum):
        if not self.head or not self.head.next: return

        tail = cur = self.head
        result = []
        while tail.next:            # Move tail to tail
            tail = tail.next

        while cur != tail:
            if cur.data + tail.data == sum:
                result.append((cur.data, tail.data))
                cur = cur.next
                tail = tail.prev
            elif cur.data + tail.data < sum:
                cur = cur.next
            else:
                tail = tail.prev

        return result


    def reverse(self):
        cur, prev = self.head, None

        # For each iteration, you only change the node's next and prev ptr
        while cur:
            prev = cur.prev
            cur.prev = cur.next
            cur.next = prev         # Next ptr of a node is changed after the node's iteration
            cur = cur.prev

        # Check for cases where list is empty or only has one node
        if prev is not None:
            self.head = prev.prev



l = LinkedList()

l.addElement(1)
l.addElement(2)
l.addElement(3)
l.addElement(5)
l.addElement(6)
l.addElement(7)
l.addElement(10)

l.reverseList()
l.printList()
