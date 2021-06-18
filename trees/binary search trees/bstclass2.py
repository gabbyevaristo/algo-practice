class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" Insert an element in the correct position in a BST """
def insert(node,element):
    if not node:
        return Node(element)

    if element < node.data:
        node.left = insert(node.left,element)
    else:
        node.right = insert(node.right,element)

    return node


# Inserts an element iteratively
def insertNonRecur(node,element):
    newNode = Node(element)
    cur, parent = node, None

    while cur:
        parent = cur
        if element < cur.data:
            cur = cur.left
        else:
            cur = cur.right

    if not parent:
        parent = newNode
    elif element < parent.data:
        parent.left = newNode
    else:
        parent.right = newNode


""" Delete an element in a BST """
    # def delete(self,element):
    #     val = self.deleteHelper(self.root,element)
    #     self.size = self.size - 1 if val else self.size

def delete(node,element):
    if not node:
        return
    if element < node.data:
        node.left = delete(node.left,element)
    elif element > node.data:
        node.right = delete(node.right,element)
    else:
        """ If node to be deleted has zero or one child - If the node to be deleted has
        only one child, the child's data is copied to the node. If the node has no children,
        the node's right child (None) will be set as the new node. """
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        """ If node to be deleted has two children, the node's data is replaced by its
        inorder sucessor (maximum value in its right subtree). This is found by calling the
        minimum helper function with the node's right child. The successor value is then set
        to the node, and the successor is deleted. """
        val = findMinimumHelper(node.right)
        node.data = val
        node.right = delete(node.right,val)

    return node


# Given a node, find the minimum value in its subtree
def findMinimumHelper(node):
    if not node.left:
        return node.data
    else:
        return findMinimumHelper(node.left)


""" Performs LNR traversal algorithm using recursion """
def inOrderTraversal(node):
    tree = []
    if node:
        tree = tree + inOrderTraversal(node.left)
        tree.append(node.data)
        tree = tree + inOrderTraversal(node.right)
    return tree


""" Given a range, prints all values in that range """
def printRange(node,low,high):
    if not node:
        return

    if low < node.data:
        printRange(node.left,low,high)

    if low <= node.data and high >= node.data:
        print(node.data)

    if high > node.data:
        printRange(node.right,low,high)


""" Returns the sum of k smallest elements in a BST """
def sumOfKSmallest(node,k):
    stack, sum = [], 0
    cur = node
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            k -= 1
            sum += cur.data
            if k == 0:
                return sum
            cur = cur.right


""" Returns the kth smallest element in a BST iteratively """
# Can perform the same method to find the kth largest element by traversing to
# right child if cur exists and traversing to right child when cur does not exist.
def kthSmallest(node,k):
    stack = []
    cur = node
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.data
            cur = cur.right
    return "Error"


""" Returns the kth largest element in a BST """
# Can perform the same method to find the kth smallest element by first calling
# the helper function on the left child and then the right child.
def kthLargest(root,k):
    count = [0]
    kthLargestHelper(root,k,count)

def kthLargestHelper(root,k,count):
    if not root or count[0] >= k:
        return

    kthLargestHelper(root.right,k,count)

    # Increment count of visited nodes. If c equals k, return node's data
    count[0] += 1
    if count[0] == k:
        print(root.data)

    kthLargestHelper(root.left,k,count)


""" Performs bfs on a tree and adds it to a set """
def levelOrderTraversal(node):
    res, q = set(), [node]
    while q:
        cur = q.pop(0)
        res.add(cur.data)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return res


""" Determine if two BSTs contain the same elements """
def containSameElements(node1,node2):
    if not node1 and not node2:
        return True

    if (node1 and not node2) or (not node1 and node2):
        return False

    # Creates a set of elements for node1 and node2 and compares their data
    s1, s2 = set(), set()
    s1 = levelOrderTraversal(node1)
    s2 = levelOrderTraversal(node2)

    return s1 == s2


""" Find the intersection of two BSTs """
def intersection(root1,root2):
    if (not root1 and not root2) or (not root1 and root2) or (root1 and not root2):
        return

    set1, set2 = set(), set()
    res = []

    # Adds all nodes to two separate sets
    set1 = levelOrderTraversal(root1)
    set2 = levelOrderTraversal(root2)

    # For each element in set1, if it is also in set2, add it to the result
    for i in set1:
        if i in set2:
            res.append(i)
    return res


""" Implement a change key function that takes in root of tree, old key value,
and new key value """
def changeKey(root,oldKey,newKey):
    # Delete old key value and add new key value
    root = delete(root,oldKey)
    root = insert(root,newKey)
    return root



root = Node(15)
insertNonRecur(root,5)
insertNonRecur(root,1)
insertNonRecur(root,10)
insertNonRecur(root,0)
insertNonRecur(root,20)
insertNonRecur(root,7)
insertNonRecur(root,9)

root1 = Node(10)
insertNonRecur(root1,7)
insertNonRecur(root1,20)
insertNonRecur(root1,4)
insertNonRecur(root1,9)

print(sumOfKSmallest(root,6))
