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


    # Determine if two lists are identical
    def areIdentical(self,l2):
        l1, l2 = self.head, l2.head

        while l1 and l2:
            if l1.data != l2.data:
                return False
            l1, l2 = l1.next, l2.next
        return not l1 and not l2        # If identical, both l1 and l2 will be None


    # Merge two sorted lists
    def mergeSorted(self,l1,l2):
        """ Making the newList of type LinkedList and using the append method
            to add values. """

        l1, l2 = l1.head, l2.head
        prev = cur = None

        # Runs only when both lists are not None
        while l1 and l2:
            # If l1 is less than or equal to l2, create a new node with l1's data
            if l1.data == l2.data or l1.data < l2.data:
                newNode = Node(l1.data)
                l1 = l1.next
            # If l2 is smaller than l2, create a new node with l2's data
            else:
                newNode = Node(l2.data)
                l2 = l2.next

            if not self.head:
                self.head = newNode
            else:
                prev.next = newNode

            prev = newNode

        # Only one of the two lists will be None at this point. Add the rest of the other
        # list to the resulting list
        if not l1: prev.next = l2
        if not l2: prev.next = l1


   # Find the intersection of two sorted lists
    def intersectionSorted(self,l2):
        l1, l2 = self.head, l2.head
        result = []

        while l1 and l2:
            if l1.data == l2.data:
                result.append(l1.data)
                l1 = l1.next
                l2 = l2.next
            elif l1.data < l2.data:
                l1 = l1.next
            else:
                l2 = l2.next

        return result


    # Find the intersection of two unsorted lists
    def intersectionUnsorted(self,l2):
        l1, l2 = self.head, l2.head
        result = []
        s = set()

        while l1:
            if l1.data not in s:
                s.add(l1.data)
            l1 = l1.next

        while l2:
            if l2.data in s:
                result.append(l2.data)
            l2 = l2.next

        return result


    # Determine if there is an intersection between two lists
    """
        1. Use a hash table and determine if a node in list 1 is the same as a node in list 2
        2. Traverse to the end of both lists and compare the nodes. If the nodes are not the
           same, there isn't an intersection. If it is, there is an intersection (how would you
           find it though?)
    """

    # Find the intersection point of two linked lists
    """
    Hashing:
    * Time = O(m) + O(n) = Time for creating hash + time for scanning list
    * Space = O(n) or O(m), depending on which list is used for the hash

        1. Add all the nodes from one list to a set
        2. Traverse the second list and check whether the node is already in the set
        3. If the traversal ends and the check fails, there is no merging point

    --------------------------------------------------------------------------------------------

    Repeating number approach:
    * Time = O(m+n) = Time for creating a list + Time for find repeating element
    * Space = O(m+n) = Space to create a list + Space to create a hash

        1. Create a list and add all nodes to the list
        2. Find the first repeating element (merging point)
              - Traverse the list from right to left, adding each node into a hash. If the node
                is in the hash, set it to a temporary variable. At the end of the loop, the
                temporary variable will store the first repeating element.

    --------------------------------------------------------------------------------------------

    Stacks:
    * Time = O(m+n) for scanning both lists + comparing the top of the lists
    * Space = O(m+n) for creating two stacks

        1. Create two stacks, one for the first list and another for the second
        2. Traverse the first list and push all nodes onto the first stack
        3. Traverse the second list and push all nodes onto the second stack
        4. Compare the top nodes of both stacks. If they are the same, take the top element
           from one and keep it in a temporary variable.
        5. Continue step 4 until the top nodes are not the same (merging point)
        6. Return the value of the temporary variable

    --------------------------------------------------------------------------------------------

    Best method:
    * Time = O(m+n) = Time for getting the lengths + time for traversing the lists
    * Space = O(1)

        1. Run through both lists to get the lengths and the tails
        2. Compare the tails (if they are different, immediately return False)
        3. Set two pointers to the start of each list
        4. Traverse the longer list by the difference in lengths (both lists will start with an equal number)
        5. Traverse the lists in parallel until a common node is found
    """

    # Adds two numbers and returns the sum
    def addTwoNumbers(self,l1,l2):
        l1, l2 = l1.head, l2.head
        prev, temp = None, None
        carry, sum = 0, 0

        # Run while either of the lists is not None
        while l1 or l2:

            l1Data = 0 if not l1 else l1.data
            l2Data = 0 if not l2 else l2.data
            sum = l1Data + l2Data + carry

            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10
            temp = Node(sum)

            # Creates the new list
            if not self.head:
                self.head = temp
            else :
                prev.next = temp

            prev = temp

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            temp.next = Node(carry)


l1 = LinkedList()
l1.append(1)
l1.append(3)
l1.append(5)
l1.append(8)

l2 = LinkedList()
l2.append(2)
l2.append(5)
l2.append(8)
l2.append(9)
l2.append(13)
l2.append(60)

print(l1.intersectionSorted(l2))
