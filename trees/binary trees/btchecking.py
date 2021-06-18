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


# Determine if two trees contain the same elements
def containSameElements(node1,node2):
    if not node1 and not node2:
        return True

    if (node1 and not node2) or (not node1 and node2):
        return False

    # Creates a set of elements for node1 and node2 and compares their data
    s1, s2 = set(), set()
    s1 = traversal(node1)
    s2 = traversal(node2)

    return s1 == s2


# Determines if two binary trees are structurally identical
def areIdentical(node1,node2):
    if not node1 and not node2:
        return True

    # Same as "if node1 and not node2 or not node1 and node2" since the first case
    # returns True if both node1 and node2 are None
    if not node1 or not node2:
        return False

    # Identical if the node's data are identical and their left and right children
    # are identical
    return node1.data == node2.data and areIdentical(node1.left,node2.left) \
        and areIdentical(node1.right,node2.right)


# Determines if two binary trees are mirrors of each other
def areMirrors(node1,node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False

    # Mirror if the node's data are the same and their left and right child are interchanged
    return node1.data == node2.data and areMirrors(node1.left,node2.right) \
        and areMirrors(node1.right,node2.left)


# Determine if the tree satisfies the children sum property (for every node, the
# data value must be equal to the sum of data values in its children)
def childrenSumProperty(node):
    if not node or (not node.left and not node.right):
        return True

    # If node does only has one child, check if that child has the same value as 
    # the node and traverse to that child
    if not node.right:
        return node.data == node.left.data and childrenSumProperty(node.left)

    if not node.left:
        return node.data == node.right.data and childrenSumProperty(node.right)

    childSum = node.left.data + node.right.data
    return node.data == childSum and childrenSumProperty(node.left) \
        and childrenSumProperty(node.right)

def childrenSumProperty2(node):
    lChild = rChild = 0

    if not node or (not node.left and not node.right):
        return True
    else:
        # If children are not present, 0 is used as the data
        if node.right:
            rChild = node.right.data
        if node.left:
            lChild = node.left.data
        return node.data == rChild + lChild and childrenSumProperty2(node.left) \
            and childrenSumProperty2(node.right)


# Determine if a tree is a full BT
def isFull(node):
    if not node or (not node.left and not node.right):  # If leaf
        return True

    if not node.left or not node.right:                 # If node only has one child
        return False

    return isFull(node.left) and isFull(node.right)


# Determine if a tree is a complete BT
def isComplete(node):
    if not node:
        return True

    q, flag = [node], False
    while q:
        cur = q.pop(0)

        # If flag is set to True, it means we have seen a non-full node. If we
        # iterate again, and we see a left or right child, the tree is not complete.
        if cur.left:
            if flag:
                return False
            q.append(cur.left)
        else:
            # Set flag to true if node is not full
            flag = True

        if cur.right:
            if flag:
                return False
            q.append(cur.right)
        else:
            flag = True
    return True


root = Node(1)
insert(root,2)
insert(root,3)

root2 = Node(10)
insert(root2,8)
insert(root2,2)
insert(root2,3)
insert(root2,5)
insert(root2,4)
insert(root2,9)
