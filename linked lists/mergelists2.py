# Merge lists using LinkedList class

class Node:

    # Initialize data attributes
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(Node):

    # Initialize data attributes
    def __init__(self):
        self.head = None
        self.size = 0


    # Add element to the end
    def addElement(self,data):
        newNode = Node(data)

        # Add element when linked list is empty
        if not self.head:
            self.head = newNode
            self.size += 1
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.size += 1


    # Merge lists l1 and l2
    def mergeLists(self,l1,l2,newList):
        l1ptr = l1.head
        l2ptr = l2.head

        # Runs until both lists are empty
        while l1ptr or l2ptr:
            if l1ptr is None:
                newList.addElement(l2ptr.data)
                l2ptr = l2ptr.next
            elif l2ptr is None:
                newList.addElement(l1ptr.data)
                l1ptr = l1ptr.next
            elif l1ptr.data <= l2ptr.data:
                newList.addElement(l1ptr.data)
                l1ptr = l1ptr.next
            elif l1ptr.data > l2ptr.data:
                newList.addElement(l2ptr.data)
                l2ptr = l2ptr.next


    def printList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


l1 = LinkedList()
l1.addElement(1)
l1.addElement(3)
l1.addElement(5)
l1.addElement(44)
l1.addElement(52)
l1.addElement(77)
l1.printList()

l2 = LinkedList()
l2.addElement(1)
l2.addElement(3)
l2.addElement(4)
l2.addElement(8)
l2.addElement(15)
l2.addElement(22)

newList = LinkedList()
newList.mergeLists(l1,l2,newList)
newList.printList()
