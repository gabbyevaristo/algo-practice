# Merge lists using Node class

class Node:

    # Initialize data attributes
    def __init__(self, data):
        self.data = data
        self.next = None

    # Merge lists l1 and l2
    def mergeLists(self,l1,l2):

        head = Node(None)
        newList = Node(None)
        head.next = newList     # head -> newList

        # Runs until one of the lists is empty
        # l1 and l2, so when one is false, the loop will break
        while l1 and l2:
            if l1.data < l2.data:
                newList.next = l1
                l1 = l1.next
                newList = newList.next
            else:
                newList.next = l2
                l2 = l2.next
                newList = newList.next

        # Add the rest of the values of the non-empty list
        newList.next = l1 or l2

        cur = head.next.next
        while cur != None:
            print(cur.data)
            cur = cur.next


l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next = Node(17)

l2 = Node(1)
l2.next = Node(10)
l2.next.next = Node(12)
l2.next.next.next = Node(15)

print("\n")
l1.mergeLists(l1,l2)
