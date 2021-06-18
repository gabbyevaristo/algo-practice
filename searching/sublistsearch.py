# Check whether the first list is present in the second list
""" Time complexity: O(m*n) """

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


""" Performs sublist search """
def sublistSearch(head1,head2):
    # Return true if both lists are empty
    if not head1 and not head2:
        return True

    # Return false if first list is empty or if first list
    # exists and second list is empty
    if not head1 or head1 and not head2:
        return False

    ptr1, ptr2 = head1, head2
    while ptr2:
        list2 = ptr2

        # Begin matching first list with second list
        while ptr1:
            # If second list becomes empty while first
            # one exists, then return False
            if not list2:
                return False

            # If data is equal, go to next on both lists
            elif ptr1.data == list2.data:
                ptr1 = ptr1.next
                list2 = list2.next

            # If data is unequal, break
            else:
                break

        # If first list gets traversed completely (without
        # hitting the break statement above), it means list1
        # is a sublist of list2
        if not ptr1:
            return True

        # Else, reset list1 and move ptr2 to ptr2.next
        ptr1 = head1
        ptr2 = ptr2.next

    return False


head1 = Node(4)
insert(head1,15)
# insert(head1,1)

head2 = Node(15)
insert(head2,5)
insert(head2,4)
insert(head2,19)
insert(head2,15)
insert(head2,22)

print(sublistSearch(head1,head2))
