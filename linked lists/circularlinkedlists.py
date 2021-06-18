class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,element):
        newNode = Node(element)

        if not self.head:
            self.head = newNode
            newNode.next = newNode
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
        self.size += 1


    """ Only call if there are elements in the list """
    def addToFront(self,element):
        newNode = Node(element)

        cur = self.head
        while cur.next != self.head:    # Iterates to the last element in the list
            cur = cur.next
        cur.next = newNode

        newNode.next = self.head
        self.head = newNode
        self.size += 1


    def addAtIndex(self,element,index):
        if index > self.size or index < 0:
            return "ERROR"

        newNode = Node(element)
        cur = self.head
        for i in range(index-1):    # Stops before the position you want to add at
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1


    def deleteBack(self):
        cur = self.head
        while cur.next.next != self.head:
            cur = cur.next
        cur.next = self.head


    def deleteFront(self):
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = self.head.next
        self.head = cur.next


    def getSize(self):
        return self.size


    def printList(self):
        if not self.head:
            return

        cur = self.head
        while True:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


c = CircularLinkedList()
c.append(0)
c.append(1)
c.append(2)
c.append(3)
c.append(4)
c.append(5)
c.append(6)
c.append(7)
c.append(8)

c.addAtIndex(44,-1)
c.printList()
