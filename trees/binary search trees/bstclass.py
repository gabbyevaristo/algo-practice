class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.size = 0


    """ Inserts an element in the correct position in a BST """
    def insert(self,element):
        if not self.root:
            newNode = Node(element)
            self.root = newNode
        else:
            self.insertHelper(self.root,element)    # Calls the helper function
        self.size += 1                              # Increase the size of tree by 1

    def insertHelper(self,node,element):
        """ The below approach compares both the data and checks if the left or
        right child are None. """
        # if element < node.data and not node.left:
        #     newNode = Node(element)
        #     node.left = newNode
        # elif element > node.data and not node.right:
        #     newNode = Node(element)
        #     node.right = newNode
        # elif element < node.data:
        #     self.insertHelper(node.left,element)
        # else:
        #     self.insertHelper(node.right,element)

        if not node:
            return Node(element)        # Returns the new element
        elif element < node.data:
            node.left = self.insertHelper(node.left,element)
        else:
            node.right = self.insertHelper(node.right,element)
        return node

    # Inserts an element iteratively
    def insertNonRecur(self,element):
        newNode = Node(element)
        if not self.root:
            self.root = newNode
        else:
            node, parent = self.root, None

            # At the end of the loop, node = position to be inserted at
            # and parent = parent of node
            while node:
                parent = node
                if element < node.data:
                    node = node.left
                else:
                    node = node.right

            if element < parent.data:
                parent.left = newNode
            else:
                parent.right = newNode
        self.size += 1


    # ---------------------------------------------------------------------- #

    """ Deletes an element in a BST """
    def delete(self,element):
        val = self.deleteHelper(self.root,element)
        self.size = self.size - 1 if val else self.size

    def deleteHelper(self,node,element):
        if not node:
            return
        if element < node.data:
            node.left = self.deleteHelper(node.left,element)
        elif element > node.data:
            node.right = self.deleteHelper(node.right,element)
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
            val = self.findMinimumHelper(node.right)
            node.data = val
            node.right = self.deleteHelper(node.right,val)

        return node


    # ---------------------------------------------------------------------- #

    """ Finds an element in the BST """
    def find(self,element):
        return self.findHelper(self.root,element)

    def findHelper(self,node,element):
        if not node:
            return False
        elif node.data == element:
            return True
        elif element < node.data:
            return self.findHelper(node.left,element)
        else:
            return self.findHelper(node.right,element)

    # Finds an element iteratively
    def findNonRecur(self,element):
        if not self.root:
            return False
        else:
            cur = self.root
            while cur:
                if element == cur.data:
                    return True
                elif element < cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
        return False


   # ---------------------------------------------------------------------- #

    """ Performs LNR traversal algorithm using recursion """
    def inOrderTraversal(self):
        def inOrderTraversalHelper(node,tree):
            if node:
                tree = inOrderTraversalHelper(node.left,tree)
                tree.append(node.data)
                tree = inOrderTraversalHelper(node.right,tree)
            return tree
        tree = []
        return inOrderTraversalHelper(self.root,tree)


    """ Finds the minimum element in a BST """
    # Traverses to the furthest left node and returns that node's data
    def findMinimum(self):
        if not self.root:
            return -1
        else:
            return self.findMinimumHelper(self.root)

    def findMinimumHelper(self,node):
        if not node.left:
            return node.data
        else:
            return self.findMinimumHelper(node.left)

    # Finds the minimum element in a BST iteratively
    def findMinimumNonRecur(self):
        if not self.root:
            return -1
        else:
            cur = self.root
            while cur.left:
                cur = cur.left
            return cur.data


    """ Finds the kth smallest element in a BST iteratively """
    def findKthSmallest(self,k):
        return self.kthSmallest(self.root,k)

    def kthSmallest(self,node,k):
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


    """ Given a range, prints all values in that range """
    def printRange(self,low,high):
        self.printRangeHelper(self.root,low,high)

    # Can also mimic countNodesInRangeHelper
    def printRangeHelper(self,node,low,high):
        if not node:
            return

        if low <= node.data and high >= node.data:
            print(node.data)

        if node.data > low:
            self.printRangeHelper(node.left,low,high)

        if node.data < high:
            self.printRangeHelper(node.right,low,high)


    """ Given a range, count the number of nodes that fall in that range """
    def countNodesInRange(self,low,high):
        return self.countNodesInRangeHelper(self.root,low,high)

    def countNodesInRangeHelper(self,node,low,high):
        if not node:
            return 0

        if low <= node.data and high >= node.data:
            return (1 + self.countNodesInRangeHelper(node.left,low,high) \
                + self.countNodesInRangeHelper(node.right,low,high))

        if node.data < low:
            return self.countNodesInRangeHelper(node.right,low,high)

        if node.data > high:
            return self.countNodesInRangeHelper(node.left,low,high)


    """ Converts a BST to a DLL """
    def convertToDLL(self):
        self.head = None            # Creates a head attribute
        self.convertToDLLHelper(self.root)

    def convertToDLLHelper(self,node):
        stack = []
        cur, prev = node, None

        while stack or cur:
            # Traverses to the furthest left node
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                if not self.head:           # If node is smallest node, set it to head
                    self.head = cur
                else:                       # If node is not the first node, set the next
                    prev.right = cur        # of the previous node to the current node
                cur.left = prev             # Set current's prev to the previous node

                prev = cur
                cur = cur.right

        prev.right = None                   # Prev is the last node


    def printList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.right


b = BST()
b.insertNonRecur(25)
b.insertNonRecur(10)
b.insertNonRecur(30)
b.insertNonRecur(7)
b.insertNonRecur(12)
b.insertNonRecur(31)
b.insertNonRecur(2)
b.insertNonRecur(39)
b.insertNonRecur(3)

b.printRange(9,32)
print(b.countNodesInRange(9,32))
