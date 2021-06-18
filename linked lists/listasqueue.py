class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Add element to the back
    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        self.size += 1


    # Pop element from the front
    def pop(self):
        if not self.head:
            print("Queue is empty")
            return
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val


    def getSize(self):
        return self.size

    def printList(self):
        cur = self.head
        while cur.next:
            print(cur.data)
            cur = cur.next


l1 = LinkedList()
l1.append(4)
l1.append(3)
l1.append(100)
l1.append(22)
l1.append(44)
l1.printList()
print("Size: " + str(l1.getSize()))

print("\nPopped value: " + str(l1.pop()))
print("\nNew list:")
l1.printList()
print("Size: " + str(l1.getSize()))
