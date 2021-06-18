# Inserting an element at the head:
"""
    Create a new node, set its element to the new element, set its next link to
    refer to the current head, and then set the list's head to point to the new node

    newNode = Node(e)
    newNode.next = L.head
    L.head = newNode
    L.size = L.size + 1
"""

# Inserting an element at the tail:
"""
    Create a new node, assign its next reference to None, set the next reference to
    point to this new node, and then update the tail reference to point to the new node

    newNode = Node(e)
    newNode.next = None
    L.tail.next = newNode
    L.tail = newNode
    L.size = L.size + 1
"""

# Removing an element at the head:
"""
if L.head is None:
    return "Error, list is empty"
L.head = L.head.next
L.size = L.size - 1
"""

# Removing an element at the tail:
"""
More difficult as you must traverse the entire list - though we keep a tail reference,
we cannot reach the node before it by following next links from the tail

Solution: a doubly linked list
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None


    def addElement(self,element):      # element = data
        newNode = Node(element)
        if self.size == 0:
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def addElementToTop(self,element):
        newNode = Node(element)
        if self.size == 0:
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1


    def removeHead(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            self.head = self.head.next
            self.size -= 1


    def removeTail(self):
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        self.tail = cur


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


linkedList = LinkedList()

n = int(input("How many values do you want to add? "))

for el in range(n):
    num = int(input())
    linkedList.addElement(num)

# linkedList.addElementToTop(100)
# linkedList.addElementToTop(4)

linkedList.removeTail()
# linkedList.reverseList()
print("\n")

linkedList.printList()
print("\nSize of list: " + str(linkedList.getSize()))
