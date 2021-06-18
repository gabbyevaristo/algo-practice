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

# Returns inorder traversal
def traversal(node):
    tree = []
    if node:
        tree = tree + traversal(node.left)
        tree.append(node.data)
        tree = tree + traversal(node.right)
    return tree



# Construct tree given inorder and preorder traversals
"""
    In preorder, first element denotes the root of the tree. In inorder, all
    elements to the left side of the root are in the left subtree and all
    elements to the right side of the root are in the right subtree. Construct
    left subtree first as value is being popped from the front of preorder.
"""
def constructGivenPreAndIn(preorder,inorder):   # Constructs tree using slicing
    if not preorder or not inorder:
        return

    rootVal = preorder.pop(0)           # First node in preorder is root
    root = Node(rootVal)                # Create a node with that value
    rootIndex = inorder.index(rootVal)

    root.left = constructGivenPreAndIn(preorder, inorder[:rootIndex])
    root.right = constructGivenPreAndIn(preorder, inorder[rootIndex+1:])
    return root


# Construct tree given inorder and preorder traversals without slicing
def constructGivenPreAndIn2(preorder,inorder):
    # Creates a dictionary for O(1) look up time
    d = {}
    for i in range(len(inorder)):
        d[inorder[i]] = i

    n = len(inorder)
    return constructHelper(preorder,inorder,0,n-1,d)

def constructHelper(preorder,inorder,start,end, d):
    if start > end:
        return None

    rootVal = preorder.pop(0)           # First node in preorder is root
    root = Node(rootVal)                # Create a node with that value
    rootIndex = d[rootVal]              # Looks up index in dictionary

    # Creates the right and left subtrees by passing start and end indexes
    root.left = constructHelper(preorder, inorder, start, rootIndex-1, d)
    root.right = constructHelper(preorder, inorder, rootIndex+1, end, d)
    return root



# Construct tree given inorder and postorder traversals
"""
    In postorder, last element denotes the root of the tree. In inorder, all
    elements to the left side of the root are in the left subtree and all
    elements to the right side of the root are in the right subtree. Construct
    right subtree first as value is being popped from the back of preorder.
"""
def constructGivenPostAndIn(postorder,inorder):     # Constructs tree using slicing
    if not postorder or not inorder:
        return

    root = Node(postorder.pop())             # Create a node with last value in postorder
    rootIndex = inorder.index(root.data)    # Get the root's index in inorder

    root.right = constructGivenPostAndIn(postorder, inorder[rootIndex+1:])
    root.left = constructGivenPostAndIn(postorder, inorder[:rootIndex])
    return root


# Construct tree given inorder and postorder traversals without slicing
def constructGivenPostAndIn2(postorder,inorder):
    # Creates a dictionary for O(1) look up time
    d = {}
    for i in range(len(inorder)):
        d[inorder[i]] = i

    n = len(inorder)
    return constructHelper2(postorder,inorder,0,n-1,d)

def constructHelper2(postorder,inorder,start,end, d):
    if start > end:
        return None

    root = Node(postorder.pop())             # Create a node with last value in postorder
    rootIndex = d[root.data]                # Get the root's index in inorder

    # Creates the right and left subtrees by passing start and end indexes
    root.right = constructHelper2(postorder, inorder, rootIndex+1, end, d)
    root.left = constructHelper2(postorder, inorder, start, rootIndex-1, d)
    return root



# If given two traversal sequences, can a binary tree be constructed uniquely?
"""
    If one of the traversals is inorder, then the tree can be constructed uniquely,
    otherwise it cannot.

    Postorder and preorder, preorder and level order, & postorder and level order
    cannot uniquely indentify a tree. For the following two trees, postorder,
    preorder, and level order produce the same results [A,B].

            A           A
        B                   B

"""


# How many different trees are possible with n nodes?
""" In general, if there are n nodes, there exist 2^n - n different trees.

        For example, n = 3. Maximum combination = 2^3 - 3 = 5 combinations


        A                   A       A                   A       A
    B       C           B               B           B               B
                    C                       C           C       C

"""



root = Node(1)
insert(root,2)
insert(root,9)
insert(root,7)
insert(root,4)
insert(root,3)

inorder = [4,2,5,1,6,3]
preorder = [1,2,4,5,3,6]
postorder = [4,5,2,6,3,1]

v = constructGivenPostAndIn2(postorder,inorder)
print(traversal(v))
