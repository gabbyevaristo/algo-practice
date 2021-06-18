class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Append to the front
    def append(self,data):
        newNode = Node(data)
        if self.head:               # If list is not empty
            newNode.next = self.head
        self.head = newNode
        self.size += 1


    # Pop from the front
    def pop(self):
        if not self.head:
            print("Stack is empty")
            return
        val = self.head.data        # Save data of popped value
        self.head = self.head.next
        self.size -= 1
        return val                  # Returns popped value


    def getSize(self):
        return self.size

    def printList(self):
        cur = self.head
        while cur:
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
