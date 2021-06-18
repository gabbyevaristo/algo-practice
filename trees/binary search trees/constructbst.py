class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ListNode:

    def __init__(self,data):
        self.data = data
        self.next = None


""" Insert an element in the correct position in a BST """
def insertToTree(node,element):
    if not node:
        return TreeNode(element)
    if element <= node.data:
        node.left = insertToTree(node.left,element)
    else:
        node.right = insertToTree(node.right,element)
    return node

""" Inserts an element to a singly linked list """
def insertToList(head,element):
    newNode = ListNode(element)

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = newNode


""" Converts a BST to a DLL """
# Traverses in-order and assigns left as previous and right as next
def convertToDLL(node,head):
    stack = []
    cur, prev = node, None

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()

            if not head:
                head = cur
            else:
                prev.right = cur
            cur.left = prev

            prev = cur
            cur = cur.right

    prev.right = None                   # Prev is the last node
    return head


""" Convert a sorted array to a balanced BST """
def arrayToBST(arr,left,right):     # left = 0, right = len(arr)-1
    # If left is greater than right, the node has only 1 child
    if left > right:
        return None

    mid = (left + right) / 2
    newNode = TreeNode(arr[mid])
    newNode.left = arrayToBST(arr,left,mid-1)
    newNode.right = arrayToBST(arr,mid+1,right)
    return newNode


""" Convert a normal BST to a balanced BST """
# Traverse the tree in inorder and store the result in a temp array -
# this takes O(n) time. Then, use the function arrayToBST to convert it.


""" Convert a SLL to a balanced BST """
def sllToBST(head):
    if not head:        # When a node only has one child
        return None

    # Get the middle element - prev is used to disconnect the left half
    # from the middle node
    prev, mid, temp = None, head, head
    while temp and temp.next:
        prev, mid, temp = mid, mid.next, temp.next.next
    if prev:
        prev.next = None

    newNode = TreeNode(mid.data)
    if head == mid:
        return newNode

    newNode.left = sllToBST(head)
    newNode.right = sllToBST(mid.next)
    return newNode


""" Construct BST given preorder traversal """
def constructGivenPreorder(pre):
    index = [0]
    # Sends in first element and min/max constraints
    return constructHelper(pre, pre[0], index, float('-inf'), float('inf'))

def constructHelper(pre,key,index,mini,maxi):
    if index[0] >= len(pre):
        return None

    # If the next if statement is not reached, None is sent in as a
    # node's left or right child
    root = None

    # Creates a new node and increments count if key falls within min/max constraints
    if key > mini and key < maxi:
        root = TreeNode(key)
        index[0] += 1

        # Only construct children if there are nodes left in preorder array
        if index[0] < len(pre):
            root.left = constructHelper(pre,pre[index[0]],index,mini,key)
            root.right = constructHelper(pre,pre[index[0]],index,key,maxi)
    return root


""" Construct BST from given level order traversal """
def constructGivenLevel(arr):
    if not arr:
        return None

    root = None

    # For each value in the array, insert it appropriately
    for i in range(len(arr)):
        root = insertToTree(root,arr[i])
    return root


"""Convert BST to greater tree, where every key is changed to the original key plus the
sum of all keys greater than it """
# Can manipulate function to convert to smaller tree by traversing the left subtree and
# then the right subtree
"""
    def greaterTree(node):
        greaterTreeHelper(node,0)
        return node

    def greaterTreeHelper(node,sum):
        if not node:
            return sum

        # Stores value of right child and adds it to node. When calling left child, the node's new
        # data (sum) is passed in as the sum parameter.
        ans = greaterTreeHelper(node.right,sum)
        node.data += ans
        return greaterTreeHelper(node.left,node.data)
"""
def greaterTree(node):
    s = [0]
    greaterTreeHelper(node,s)

def greaterTreeHelper(node,s):
    if not node:
        return

    # Stores value of right child and adds it to node. When calling left child, the node's new
    # data (sum) is passed in as the sum parameter.
    greaterTreeHelper(node.right,s)
    s[0] = s[0] + node.data
    node.data = s[0]
    greaterTreeHelper(node.left,s)


""" Convert a binary tree to a threaded binary tree """
# Create a queue and populate it with the inorder traversal of the binary tree. In a separate
# function, create the threads. Traverse to leftmost node and pop. If right node exists,
# traverse to the right, else check the length of the queue. If it is empty, node.right is None,
# else, node.right = q[0].
def createThreads(root):
    q = []
    populateQueue(root,q)       # Perform inorder traversal
    createThreadsHelper(root,q)

def populateQueue(node,q):
    pass

def createThreadsHelper(node,q):
    if not node:
        return
    createThreadsHelper(node.left,q)
    q.pop(0)

    # If right child exists, traverse to right child, else create thread
    if node.right:
        createThreadsHelper(node.right,q)
    else:
        if not q:
            node.right = None
        else:
            node.right = q[0]


# Convert a BT to a BST, keeping the same structure
"""
Perform a traversal on the BT and store it in an array. Sort the array.
Then in a separate function, recur to the left tree and change the data
to arr[i], then pop from the array. Now recur to the right tree. By 
traversing the BT, we are ensuring that we keep the same structure.

    def arrayToBST(node,arr):
        if not node: return
        arrayToBST(node.left,arr)
        node.data = arr.pop()
        arrayToBST(node.right,arr)
"""


""" Check if given sorted sub-sequence exists in BST """
def seqExist(node,seq):
    index = [0]

    # Append random value to get by index error in helper function
    seq.append(float('-inf'))
    seqExistHelper(node,seq,index)

    return True if index[0] == len(seq)-1 else False

def seqExistHelper(node,seq,index):
    if not node:
        return

    # Traverse to the left and check if node's data is equal
    # to current index in sequence
    seqExistHelper(node.left,seq,index)
    if node.data == seq[index[0]]:
        index[0] += 1
    seqExistHelper(node.right,seq,index)


def printList(head):
    node = head
    while node:
        print(node.data)
        node = node.next

def printTree(node):
    if node:
        printTree(node.left)
        print(node.data)
        printTree(node.right)


# root = TreeNode(15)
# insertToTree(root,7)
# insertToTree(root,17)
# insertToTree(root,18)
# insertToTree(root,3)
# insertToTree(root,2)
# insertToTree(root,9)
# insertToTree(root,11)
# insertToTree(root,10)
# seq = [2,7,10,17]
# print(seqExist(root,seq))

# head = ListNode(1)
# insertToList(head,2)
# insertToList(head,3)
# insertToList(head,4)
# insertToList(head,5)
# insertToList(head,6)
# val = None
# val = sllToBST(head)
# printTree(val)

arr = [10,5,1,7,40,50]
root = constructGivenPreorder(arr)
print(printTree(root))
