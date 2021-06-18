class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    """---------------ADDING ALGORITHMS---------------"""

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


    # Add an element at the given index in the list
    def addAtIndex(self,element,index):
        if not self.head or index < 0: return

        newNode = Node(element)
        cur = self.head

        for i in range(index-1):
            cur = cur.next
            if not cur:             # If cur doesn't exist, then index is greater than the size
                return "Error"
        temp = cur.next
        cur.next = newNode
        newNode.next = temp


    # Insert the given element into a sorted list
    def insertIntoSortedList(self,element):
        cur, prev = self.head, None
        newNode = Node(element)

        if not self.head:                   # Case for empty linked list
            self.head = newNode
        elif element < cur.data:              # Case, where the element is less than the head
            newNode.next = self.head
            self.head = newNode
        else:
            while cur and cur.data < element:   # Moves to the next vaue as long as current value is
                prev = cur                      # less than the inserted element
                cur = cur.next

            prev.next = newNode
            newNode.next = cur


    # Insert the given element into the middle
    def insertIntoMiddle(self,element):
        if not self.head or not self.head.next:
            return
        # By starting fast at self.head.next, it allows you to stop at the first middle
        # value if the input is even
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next            # At the end, slow = middle node
            fast = fast.next.next

        newNode = Node(element)
        newNode.next = slow.next
        slow.next = newNode



    """---------------DELETING ALGORITHMS---------------"""

    # Delete the node at the given index
    def deleteAtIndex(self,index):
        if not self.head or index < 0: return
        cur = self.head
        for _ in range(index-1):
            cur = cur.next
            if not cur:
                return
        del cur.next.data
        cur.next = cur.next.next


    # Remove the given value in the list, given that it can appear multiple times
    def deleteMultVal(self,val):
        while self.head and self.head.data == val:
            self.head = self.head.next

        if not self.head: return        # Can occur if list only contained the passed in value

        cur = self.head
        while cur.next:
            if cur.next.data == val:
                cur.next = cur.next.next
            else:       # Cur won't change until cur.next.data != val
                cur = cur.next


    # Remove the given value in the list, given that it only appears once
    """ Can also not have a special case for the head and instead have a prev pointer.
        If current data == val, use prev pointer to correct pointers. """
    def deleteOneVal(self,val):
        if self.head.data == val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next:
                if cur.next.data == val:
                    cur.next = cur.next.next
                    return
                cur = cur.next

    # Remove all duplicates in a sorted list, keeping one duplicate
    def removeDupsSorted(self):
        if not self.head: return
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next  # Only changed once the next val doesn't equal to val


    # Remove all duplicates in an unsorted list, keeping one duplicate
    """ 1. Brute force method: use two loops and compare every element = O(n^2)
        2. Merge sort and then use method above = O(nlogn)
            - For this method, element order is not preserved """
    def removeDupsUnsorted(self):
        s = set()
        prev, cur = None, self.head
        while cur:
            if cur.data in s:
                prev.next = cur.next
            else:
                s.add(cur.data)
                prev = cur
            cur = cur.next


    # Delete all occurrences of duplicates in a sorted list
    def deleteAllDuplicates(self):
        if not self.head: return
        cur, prev = self.head, None

        while cur:
            if cur.next and cur.data == cur.next.data:
                # Need to check cur and cur.next for the last iteration when cur.next is None.
                # The comparison cur.data == cur.next.data will fail if the check isn't added.
                while cur and cur.next and cur.data == cur.next.data:
                    cur = cur.next          # Cur will be at the last duplicate
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next


    # Remove every kth node in the list
    def removeEveryKthNode(self, k):
        if not self.head: return
        cur, count = self.head, 1

        if k == 1:                          # Special case
            self.head = None                # Delete head
            return

        while cur and cur.next:
            if (count + 1) % k == 0:        # Count + 1 is checked to have a reference to the previous node
                cur.next = cur.next.next
                count = 1                   # Reset count to 1 once node is deleted
            else:
                count += 1
            cur = cur.next



    """---------------SEARCHING ALGORITHMS---------------"""

    # Find second to last node in the list
    def findSecondToLastNode(self):
        cur = self.head
        while cur:
            if cur.next.next == None:
                return cur.data
            cur = cur.next


    # Get the middle of the list -- if size is even, return the second middle number
    def getMiddle(self):
        if not self.head: return
        # Using size of the list
        """n = self.size // 2
        cur = self.head
        for _ in range(n):
            cur = cur.next
        return cur.data"""

        # Using a new list
        """A = [self.head]
        while A[-1].next:
            A.append(A[-1].next)        # Adds all elements to a list
        return A[len(A) // 2].data"""

        # Using fast and slow pointers
        """fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next       # When fast reaches the end, slow will be in the middle
            slow = slow.next
        return slow.data"""

        # Increments mid only when count is odd -- only half the list will be traversed
        mid, cur = self.head, self.head
        count = 0
        while cur.next:
            if count % 2 == 0:
                mid = mid.next
            count += 1
            cur = cur.next
        return mid.data


    # Find kth element in the list
    def findKthElement(self,k):
        if not self.head or k < 0: return
        cur = self.head
        for i in range(k):
            cur = cur.next
            if not cur:
                return None
        return cur.data


    # Find the kth to last element in the list
    def findKthLastElement(self,k):
        fast = slow = self.head

        # Moves fast pointer k-1 units from slow pointer
        for i in range(k-1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.data

        """for i in range(self.size-k):
            fast = fast.next
        return fast.data"""


    # Return true if the element exists and false otherwise
    def findVal(self,element):
        if not self.head: return
        cur = self.head
        while cur:
            if cur.data == element:
                return True
            cur = cur.next
        return False

    # Return true if the element exists and false otherwise, recursively
    def findValRecur(self, element):
        def find(node, element):        # Another function is created to pass self.head into it
            # Two base cases: if element is found or if end of the list is reached
            if not node:
                return False
            if node.data == element:
                return True
            return find(node.next, element)
        return find(self.head, element)


    # Get the data at the given index
    def getDataAtIndex(self,index):
        if not self.head or index < 0: return
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if not cur:
                return None
        return cur.data

    # Get the data at the given index, recursively
    def getDataAtIndexRecur(self,index):
        def getData(node,index,count):
            if not node:
                return False
            if count == index:
                return node.data
            return getData(node.next,index,count+1)     # Increment count with each recursive call
        return getData(self.head,index,0)



    """---------------PRINTING ALGORITHMS---------------"""

    # Reverse the list
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next      # In the last iteration, next = None
        self.head = prev

    # Reverse the list recursively
    def reverseRecur(self):
        self.head = self.reverseRecurHelper(self.head)

    def reverseRecurHelper(self,node):
        if not node or not node.next:
            return node

        rest = self.reverseRecurHelper(node.next)
        node.next.next = node
        node.next = None
        return rest


    # Reverse the first k nodes of the list
    def reverseKNodes(self,k):
        cur, prev = self.head, None
        count = 0
        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count += 1

        self.head.next = cur    # At the end of the loop, head's next will be pointing to the
                                # next value in the original list
        self.head = prev        # Prev will be the last reversed value


    # Print the list
    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # Print the list in reverse
    def printListInReverse(self):
        reverse, node = [], self.head
        while node:
            reverse.append(node.data)
            node = node.next
        for _ in range(len(reverse)):
            print(reverse.pop())



    """---------------COUNTING ALGORITHMS---------------"""

    # Get the size of the list
    def getSize(self):
        count, cur = 0, self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    # Get the size of the list, recursively
    def getSizeRecur(self):
        def count(node):
            if not node:
                return 0
            else:
                return 1 + count(node.next)
        return count(self.head)


    # Determine if the length of the list is odd or even
    """Easier algorithm is to keep a count of the elements in the list"""
    def oddOrEven(self):
        cur = self.head
        while cur.next:
            cur = cur.next.next
        return "Odd" if cur else "Even"     # If cur has a value, the length is even


    # Count the occurrences of the given key in the list
    def countOccurrences(self,key):
        count, cur = 0, self.head
        while cur:
            if cur.data == key:
                count += 1
            cur = cur.next
        return count

    # Count the occurrences of the given key in the list, recursively
    def countOccurrencesRecur(self,key):
        def count(node,key):
            if not node:
                return 0
            if node.data == key:
                return 1 + count(node.next,key)     # Return "1 +" if a new occurrence is found
            return count(node.next,key)             # If no new occurrence is found, do not add one to the count
        return count(self.head,key)


    # Find the sum of the last k elements
    """ Another option is to reverse the list and add the first k elements """
    def findSum(self,k):
        # Using two pointers
        fast = slow = self.head
        sum = 0

        for i in range(k-1):       # Moves fast pointer k-1 units from slow pointer
            fast = fast.next
            if not fast: return
        while fast.next:           # Gets slow pointer to the kth to last element
            fast = fast.next
            slow = slow.next
        while slow:                # Traverses from k to the end of the list
            sum += slow.data
            slow = slow.next
        return sum

        # Using the size of the list
        """cur, sum = self.head, 0
        for i in range(self.size-k):
            cur = cur.next
        while cur:
            sum += cur.data
            cur = cur.next
        return sum"""

        # Using a stack and popping the last n elements
        """cur, stack, sum = self.head, [], 0
        while cur:
            stack.append(cur.data)
            cur = cur.next
        for i in range(k):
            sum += stack.pop()
        return sum"""


    # Remove all nodes which have a greater value on the right side
    """ Idea is to reverse the list, keeping track of the maximum value. If
        the current value is less than the max value, delete it. If it is not,
        make the current node max. """
    def deleteNodeGreaterThan(self):
        if not self.head: return
        self.reverse()
        prev = max = self.head
        cur = self.head.next

        while cur:
            if cur.data < max.data:
                prev.next = prev.next.next
                cur = prev.next
            else:
                max = prev = cur
                cur = cur.next

        self.reverse()
        self.printList()


    # Determine if a linked list is a palindrome
    def palindrome(self):
        s = []
        traverse, cur = self.head, self.head

        # Add all values to a stack
        while traverse:
            s.append(traverse)
            traverse = traverse.next

        # Start from the head and run half the length of the stack. If the data
        # at the top of the stack does not equal the current value, return False.
        for i in range(len(s)/2):
            if s.pop().data != cur.data:
                return False
            cur = cur.next

        return True



l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

l1.reverseRecur()
l1.printList()
