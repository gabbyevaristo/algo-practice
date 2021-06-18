class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inserts an element in level order iteratively
def insert(node,element):
    if not node: return

    newNode = Node(element)
    q = [node]
    while q:
        cur = q.pop(0)

        # If left child is empty, new node is added and the function returns. If
        # right child is empty, new node is added and the function returns.
        if not cur.left:
            cur.left = newNode
            break
        if not cur.right:
            cur.right = newNode
            break

        # Add existing left and right child to the queue.
        q.append(cur.left)
        q.append(cur.right)


def printLeaves(node):
    if not node:
        return

    # Can change if statement to print full/half nodes
    if not node.left and not node.right:
        print(node.data)

    printLeaves(node.left)
    printLeaves(node.right)


# Find the number of leaves
def countLeavesRecur(node):
    if not node:
        return 0
    if not node.right and not node.left:
        return 1
    # Number of leaves = # of leaves in left subtree + # of leaves in right subtree
    return countLeavesRecur(node.left) + countLeavesRecur(node.right)

# Find the number of leaves iteratively
def countLeaves(node):
    if not node: return

    q = [node]
    leaves = 0

    while q:
        cur = q.pop(0)

        # Can change if statement to count number of full/half nodes
        if not cur.left and not cur.right:
            leaves += 1

        # Add left and right child to the queue iff first if case fails
        else:
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return leaves


# Count the number of full nodes in the tree
def countFullNodes(node):
    if not node:
        return 0

    fullNodes = 0
    """ Just change if statement to count half nodes """
    if node.left and node.right:    # If node is full, increment by 1
        fullNodes += 1

    fullNodes += (countFullNodes(node.left) + countFullNodes(node.right))
    return fullNodes


# Print out all of the root-to-leaf paths in a tree
def printRootToLeaf(node):
    if not node:
        return []
    res, stack = [], [(node,[])]

    while stack:
        cur, path = stack.pop()     # Path holds the current path
        # When leaf node is reached, add the temp list to the result list
        if not cur.left and not cur.right:
            res.append(path + [cur.data])
        if cur.left:
            stack.append((cur.left, path + [cur.data]))
        if cur.right:
            stack.append((cur.right, path + [cur.data]))
    return res


# Determine if there is a path from root to leaf with the given sum
def isPathWithSum(node,target):
    if not node:
        return False
    stack = [(node, target)]

    while stack:
        cur, sum = stack.pop()
        # Remove last two conditions if asked if there simply exists a path with
        # given sum
        if cur.data == sum and not cur.right and not cur.left:
            return True
        if cur.left:
            stack.append((cur.left, sum - cur.data))
        if cur.right:
            stack.append((cur.right, sum - cur.data))
    return False


# Print out all of the root-to-leaf paths in a tree that sum to a given target
def printRootToLeafForGivenSum(node,target):
    if not node:
        return []
    res, stack = [], [(node, target, [])]
    while stack:
        cur, sum, path = stack.pop()
        if cur.data == sum and not cur.left and not cur.right:
            res.append(path + [cur.data])
        if cur.left:
            stack.append((cur.left, sum - cur.data, path + [cur.data]))
        if cur.right:
            stack.append((cur.right, sum - cur.data, path + [cur.data]))
    return res


# Remove leaves of a given tree
def removeLeaves(node):
    if not node:
        return
    if not node.left and not node.right:
        return None
    node.left = removeLeaves(node.left)
    node.right = removeLeaves(node.right)
    return node


# Given a binary tree with an extra pointer (next), fill each next pointer
def nextSibling(node):
    if not node:
        return None

    q = [node,None]

    while q:
        cur = q.pop(0)
        if not cur:
            if q:               # Add new level indicator as long as q is not empty
                q.append(None)
        else:
            cur.next = q[0]     # Current value's next sibling is at front of the queue
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return None

def nextSibling2(node):
    if not node:
        return None

    cur, next = root, root.left
    while cur.left:
        # Sets node's left next pointer to node's right pointer
        """ node.left --> node.right """
        cur.left.next = cur.right

        # If node has a sibling, then set node's right pointer to node's next
        # left pointer
        """ node.right --> node.next.left """
        if cur.next:
            cur.right.next = cur.next.left
            cur = cur.next
        else:       # Make next the furthest left nodes
            cur = next
            next = cur.left
    return node


# Print the ancestors of a given node
def printAncestorsOfANode(node,val):
    if not node:
        return False
    if node.data == val:
        print(node.data)        # Only print if target is included in ancestor list
        return True

    # Node is an ancestor if one of their children is the target value
    if printAncestorsOfANode(node.left,val) or printAncestorsOfANode(node.right,val):
        print(node.data)
        return True
    return False


# Find the LCA of two nodes, assuming both x and y are present in the tree
def findLCA(node,x,y):
    if not node:
        return None

    # Report presence of x or y by returning the node
    if node.data == x or node.data == y:
        return node.data

    left = findLCA(node.left,x,y)
    right = findLCA(node.right,x,y)

    # If above calls are not None, then current node is the LCA
    if left and right:
        return node.data

    return left if left else right


# Performs BFS traversal algorithm
def traversal(node):
    res, q = [], [node]
    while q:
        cur = q.pop(0)
        res.append(cur.data)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return res


# Find density of tree, where density = size / height of tree
def density(node):
    size = [0]
    height = densityHelper(node,size)
    return float(size[0]) / height

def densityHelper(node,size):
    if not node:
        return 0

    size[0] += 1    # Increase size by 1

    # Gets the maximum depth between the left and right subtrees
    return max(densityHelper(node.right,size), densityHelper(node.left,size)) + 1


# Check if a BT contains duplicates
def containsDuplicates(node):
    s = set()
    return containsDuplicatesHelper(node,s)

def containsDuplicatesHelper(node,s):
    if not node:
        return False
    if node.data in s:      # Returns true if data is already in set
        return True
    s.add(node.data)        # Adds data to set if it is not in set
    return containsDuplicatesHelper(node.left,s) or containsDuplicatesHelper(node.right,s)


# Performs BFS traversal algorithm
def printBFS(node):
    q, res = [node], []
    while q:
        temp = []
        for _ in range(len(q)):
            cur = q.pop(0)
            temp.append(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        res.append(temp)
    return res


root = Node(1)
insert(root,2)
insert(root,3)
insert(root,4)
insert(root,5)
insert(root,6)

print(printBFS(root))
