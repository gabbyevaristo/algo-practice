class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inserts an element iteratively
def insert(node,element):
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


# Find the lowest common ancestor (LCA) of two given nodes, p and q, in a BST
""" The first node encountered with value between p and q is the LCA. Traverse
the BST in a pre-order fashion.

    # Note: Since p may be greater than or smaller than q, move this to
            the else case and don't check directly (if p < node < q). """
def lowestCommonAncestor(root,p,q):
    if root.data < p and root.data < q:
        return lowestCommonAncestor(root.right,p,q)
    elif root.data > p and root.data > q:
        return lowestCommonAncestor(root.left,p,q)
    else:
        return root.data


# Get the shortest path between two nodes in a BST
""" Same process as finding the LCA between two nodes. Once the LCA is found,
sum the distance from the LCA to both nodes. """
def getShortestPath(root,p,q):
    if root.data < p and root.data < q:
        return getShortestPath(root.right,p,q)
    elif root.data > p and root.data > q:
        return getShortestPath(root.left,p,q)
    elif root.data >= p and root.data <= q:
        return distance(root,p) + distance(root,q)

# Finds the distance between two nodes
def distance(node,val):
    cur = node
    distance = 0

    while cur.data != val:
        if cur.data > val:
            cur = cur.left
        else:
            cur = cur.right
        distance += 1
    return distance


# Determine whether a given binary tree is a BST or not
"""
The following method traverses down the tree, keeping track of the narrowing
min and max allowed values as it goes. Another method involves performing in
order traversal. At each node, check if the node's data is greater than the
value of the previously visited node.

Another method: Do inorder traversal and store the result in a temporary array,
and check if it is sorted in ascending order. It can be optimized by storing
the previously visited node. If the current node is less than the previous node,
the tree is not a BST.
"""
def isBST(node):
    return isBSTHelper(node, float('-inf'),float('inf'))

def isBSTHelper(node, mini, maxi):
    if node is None:        # Empty tree is a BST
        return True

    # Returns false if the node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Checks the subtrees and tightens the min/max constraint. While traversing
    # left, max is tightened. While traversing right, min is tightened.
    return (isBSTHelper(node.left, mini, node.data-1) and
          isBSTHelper(node.right, node.data+1, maxi))


def isBSTInOrder(root):
    s = []
    cur = root

    while s or cur:
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            node = s.pop()
            if (node.left and node.left.data > node.data) or (node.right and node.right.data < node.data):
                return False
            cur = node.right
    return True


# Determine if BST has a dead end
""" Perform the same process as determining if a tree is a BST or not. When node is
None, return False (no dead end). The second if statement needs to be changed to
check if mini == maxi. If so, a dead end exists, so return true. """


# Determine if two BSTs are identical
def isIdentical(root1,root2):
    # If both roots are empty, return True
    if not root1 and not root2:
        return True

    # If one root is empty and the other is not, return False
    if not root1 or not root2:
        return False

    # Return true if the current roots are equal and their L/R roots are equal
    return root1.data == root2.data and isIdentical(root1.left,root2.left) and \
            isIdentical(root.right,root2.right)


# Find the element closest to a given key
""" Can use level-order traversal, and for every element, compute the difference between
the given key and the node's data. If the difference is less than the previous difference,
update the new difference and the new element to return. """


# Find the largest number less than or equal to n
def findLargestGivenN(root,n):
    if not root:
        return -1
    if root.data == n:
        return n

    # If current node's value is less than n, recur to right subtree to determine if
    # there is a closer value.
    if root.data < n:
        k = findLargestGivenN(root.right,n)
        if k == -1:
            return root.data
        else:
            return k
    # If current node's value is greater than n, recur to left subtree
    else:
        return findLargestGivenN(root.left,n)


# Find a pair with given sum in BST
"""
Method 1: Perform inorder traversal of the tree and store it in an array.
Check for pairs using two pointers approach, with one starting at the front
and another starting at the end. If the sum of the two elements is less than
the target, move front pointer up by 1, else move end pointer down by 1.

Method 2: Perform in order traversal. Add every node to the set. If target -
node.data is in the set, then add the pair to the result.
"""
def findPair(node,target):
    if not node:
        return -1
    else:
        s, res, pairs = [], [], set()
        cur = node
        while cur or s:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()

                if target - cur.data in pairs:
                    res.append((cur.data, target-cur.data))
                pairs.add(cur.data)

                cur = cur.right
        return res


# Determine if an array represents inorder of BST
""" Perform inorder traversal of the tree and store it in an array.
Iterate through array, and return false is arr[i-1] > arr[i]. """


""" Performs LNR traversal algorithm using recursion """
def inOrderTraversalRecur(node):
    tree = []
    if node:
        tree = tree + inOrderTraversalRecur(node.left)
        tree.append(node.data)
        tree = tree + inOrderTraversalRecur(node.right)
    return tree


def inOrderTraversal(node):
    s, res = [], []
    cur = node

    while s or cur:
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            node = s.pop()
            res.append(node.data)
            cur = node.right
    return res


def maxK(node,k):
    stack, maxK = [], []
    cur = node

    while (stack or cur) and (len(maxK) < k):
        if cur:
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            maxK.append(cur.data)
            cur = cur.left

    return maxK


def kLargest(root,k):
    kLargest = []
    kthLargestHelper(root,k,kLargest)
    return kLargest

def kthLargestHelper(root,k,kLargest):
    if root.right:
        kthLargestHelper(root.right,k,kLargest)
    if len(kLargest) < k:
        kLargest.append(root.data)
        if root.left:
            kthLargestHelper(root.left,k,kLargest)
    return kLargest



# Inserts an element in level order iteratively
def insertNonBST(node,element):
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



# root = Node(15)
# insert(root,7)
# insert(root,17)
# insert(root,18)
# insert(root,3)
# insert(root,2)
# insert(root,9)
# insert(root,11)
# insert(root,10)

root = Node(15)
insertNonBST(root,7)
insertNonBST(root,17)
insertNonBST(root,5)
insertNonBST(root,23)

# print(maxK(root, 4))
# print(inOrderTraversal(root))
print(isBSTInOrder(root))
