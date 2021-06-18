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


# Performs BFS traversal algorithm using recursion
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


# Find maximum element in the binary tree
""" Note: Same method can be used to search for an element, find the size of the tree, and find
          the deepest node. To find the deepest node, simply return cur.data at the end of the
          while loop as cur will hold the last value in the tree.

             FIND ELEMENT                  SIZE
          cur = q.pop(0)                cur = q.pop(0)
          if cur.data == val:           count += 1
              return True
"""
def findMax(node):
    q = [node]
    max = float('-inf')
    while q:
        cur = q.pop(0)
        if cur.data > max:      # If current value is greater than max,
            max = cur.data      # set current to max

        # Add left and right child to the queue if they exist
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return max

# Finds maximum element in a tree recursively
def findMaxRecur(node):
    if not node:
        return float('-inf')

    # Returns max between current node, its left tree maximum and right tree maximum
    return max(node.data, findMaxRecur(node.left), findMaxRecur(node.right))


# Search for an element recursively
def searchRecur(node,val):
    if not node:
        return False
    if node.data == val:
        return True

    return searchRecur(node.left,val) or searchRecur(node.right,val)


# Find the size of the tree recursively
def findSizeRecur(node):
    if not node:                # if not node.left and not node.right:
        return 0                #     return 1
    return findSizeRecur(node.left) + findSizeRecur(node.right) + 1


# Find the maximum depth/height of a tree
def maxDepth(node):
    if not node:
        return 0

    if not node.left and not node.right:    # Necessary if depth = # of levels-1
        return 0

    # Gets the maximum depth between the left and right subtrees
    return max(maxDepth(node.right), maxDepth(node.left)) + 1


# Finds the maximum depth/height of a tree iteratively, where
# maximum depth/height = # of levels in the tree
""" Can do the same to find level with maximum sum. If cur does not exist (end of
    the level), check if current sum is greater than maximum sum. Then increment
    level and reset current sum. If cur does exist, add cur's data to current sum
    and add left and right child. """
def findMaxDepthIteratively(node):
    q = [node, None]
    depth = 0

    while q:
        cur = q.pop(0)

        # If cur == None, the entire level has been processed. If there are elements
        # in the queue, add None to signify a new level. Only do this if the queue 
        # has elements or else an infinite loop will occur.
        if not cur:
            if q:
                q.append(None)
            depth += 1
        # If cur exists, add its left and right child to the queue
        else:
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return depth


# Find the minimum depth of a tree, where depth = # of levels in a tree
def minDepth(node):
    if not node:
        return 0
    elif not node.right:
        return minDepth(node.left) + 1
    elif not node.left:
        return minDepth(node.right) + 1
    else:
        return min(minDepth(node.right), minDepth(node.left)) + 1

# Find the minimum depth of a tree where depth = # of levels-1
def minDepth2(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 0
    return min(minDepth2(node.right), minDepth2(node.left)) + 1


# Find the sum of all elements in the tree
def getSum(node):
    if not node:
        return 0
    return node.data + getSum(node.left) + getSum(node.right)


# Print nodes at odd levels of a tree
def printOddLevels(node,odd=True):
    if not node:
        return
    if odd:
        print(node.data, end=' ')
    printOddLevels(node.left,not odd)
    printOddLevels(node.right,not odd)


# Print full nodes of a BT
def printFull(node):
    # Perform in order traversal and check if children exist
    if node:
        printFull(node.left)
        if node.left and node.right:
            print(node.data, end=' ')
        printFull(node.right)


# Print nodes k distance away from root
def printDistanceFromRoot(node,k):
    if not node:
        return
    if k == 0:
        print(node.data, end=' ')
        return
    printDistanceFromRoot(node.left,k-1)
    printDistanceFromRoot(node.right,k-1)


root = Node(1)
insert(root,2)
insert(root,3)

root2 = Node(10)
insert(root2,8)
insert(root2,2)
insert(root2,3)
insert(root2,5)
insert(root2,2)
