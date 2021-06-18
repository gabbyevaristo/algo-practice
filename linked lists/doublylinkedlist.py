class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList(Node):

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    # Add element to the tail
    def addElement(self,element):      # element = data
        newNode = Node(element)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            # newNode.prev = self.tail
            # self.tail.next = newNode
            # self.tail = newNode
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
        self.size += 1

    # Add element to the head
    def addElementToTop(self,element):
        newNode = Node(element)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    # Add element to certain index
    def addElementAtIndex(self, i, element):
        newNode = Node(element)
        if i > self.size:
            print("Cannot add element")
        elif self.size == 0 or i == self.size:    # Add when empty
            self.addElement(element)
        elif i == 0:                # Add to top
            self.addElementToTop(element)
        else:
            cur = self.head
            for j in range(i-1):
                cur = cur.next        # Element will be added after this one
            cur.next.prev = newNode
            newNode.next = cur.next
            cur.next = newNode
            newNode.prev = cur
        self.size += 1

    def removeHead(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def removeTail(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1


    def removeAtIndex(self,index):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        cur.next = cur.next.next
        cur.next.prev = cur


    def getHead(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            return self.head.data

    def getTail(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            return self.tail.data

    def getSize(self):
        return self.size

    def printList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


l = LinkedList()

l.addElement(2)
l.addElement(3)

l.printList()
