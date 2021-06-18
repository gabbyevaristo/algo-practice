class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


""" Inserts element to list """
def insert(head,element):
    newNode = Node(element)

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = newNode


""" Print linked list """
def printList(head):
    if not head:
        return
    cur = head
    while cur:
        print(cur.data, end=' ')
        cur = cur.next


""" Get middle of linked list """
def getMiddle(head):
    if not head:
        return

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeBack(left,right):
    result = None

    if not left:
        return right
    if not right:
        return left

    # Add the smaller value and call merge back function with the
    # appropriate values
    if left.data <= right.data:
        result = left
        result.next = mergeBack(left.next,right)
    else:
        result = right
        result.next = mergeBack(left,right.next)
    return result


def mergeSort(head):
    if not head or not head.next:
        return head

    # Get middle of list, store middle.next, then set middle.next to None
    mid = getMiddle(head)
    nextToMid = mid.next
    mid.next = None

    # Apply merge sort to left and right list (break them down)
    left = mergeSort(head)
    right = mergeSort(nextToMid)

    # Merge the left and right lists back together
    return mergeBack(left,right)


head = Node(4)
insert(head,15)
insert(head,10)
insert(head,5)
insert(head,20)
insert(head,3)
insert(head,2)

merged = None
merged = mergeSort(head)
print('\n')
printList(merged)
