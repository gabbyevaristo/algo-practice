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


# Return the zigzag traversal of a given tree
def zigzagTraversal(root):
    # Push root and level to a queue
    res, queue = [], [(root, 0)]

    while queue:
        cur, level = queue.pop(0)
        if cur:
            # Adds a new list if a new level is encountered
            if len(res) < level+1:
                res.append([])

            # If level is even, elements are added from left to right. If
            # level is odd, elements are added from right to left.
            if level % 2 == 0:
                res[level].append(cur.data)
            else:
                res[level].insert(0, cur.data)

            queue.append((cur.left, level+1))
            queue.append((cur.right, level+1))
    return res

# Return the zigzag traversal of a given tree
def zigzagTraversal2(root):
    curLevel, nextLevel = [root], []
    flag = True

    while curLevel:
        cur = curLevel.pop()
        print(cur.data, end=' ')

        if flag:
            if cur.left:
                nextLevel.append(cur.left)
            if cur.right:
                nextLevel.append(cur.right)
        else:
            if cur.right:
                nextLevel.append(cur.right)
            if cur.left:
                nextLevel.append(cur.left)

        if not curLevel:
            flag = not flag
            curLevel, nextLevel = nextLevel, curLevel


# Print level order line by line
def levelOrderTraversal(node):
    cur = node
    q = [cur]
    while q:
        # Declares a count to keep track of the elements on a level. When
        # the next level occurs, a new line is printed.
        count = len(q)
        while count > 0:
            cur = q.pop(0)
            print(cur.data, end=' ')
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            count -= 1
        print(' ')

def levelOrderTraversalIteratively(node):
    q = [node, None]

    while len(q) > 1:
        cur = q.pop(0)

        if not cur:
            if q:
                q.append(None)
            print(' ')
        else:
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            print(cur.data, end=' ')


# Print reverse level order traversal (from bottom to top)
def reverseLevelOrder(node):
    s, q = [], [node]

    while q:
        node = q.pop(0)
        s.append(node)

        # Adds right child first since nodes are popped off the
        # stack backwards
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    while s:
        node = s.pop()
        print(node.data, end=' ')


# Print entire level order data in reverse order
"""
            1               = [3 2 1]
        2       3

Perform level order traversal with a queue. When each node is popped, add its data
to a stack. At the end of the loop, the stack will contain the data in order. By 
popping and then printing each value, the data will be shown in reverse order.

"""


# Print perfect binary tree specific level order traversal
""" Traversal begins at the root and prints data inwards """
def specificLevelOrderFromRoot(node):
    # Checks if the first two levels exist
    if not node:
        return
    print(node.data, end=' ')

    if not node.left:
        return
    print(node.left.data, end=' ')
    print(node.right.data, end=' ')

    if not node.left.left:
        return

    # Create a queue and enqueue left and right children of root
    q = [root.left, root.right]

    while q:
        first = q.pop(0)
        second = q.pop(0)

        # Print children of first and second in specific level order
        print(first.left.data, end=' ')
        print(second.right.data, end=' ')
        print(first.right.data, end=' ')
        print(second.left.data, end=' ')

        # If first and second have grandchildren, enqueue them in reverse order
        if first.left.left:
            q.append(first.left)
            q.append(second.right)
            q.append(first.right)
            q.append(second.left)


# Print perfect binary tree specific level order traversal
""" Traversal begins at the last level and prints data inwards """
def specificLevelOrderFromLeaf(root):
    cur = root
    q, s = [], [cur.data]

    if cur.right:
        q.append(cur.right)
    if cur.left:
        q.append(cur.left)

    while len(q) > 0:
        # Processes two nodes at a time
        first = q.pop(0)
        s.append(first.data)
        second = q.pop(0)
        s.append(second.data)

        # Can check just one since input is a complete binary tree
        if first.left and second.right and first.right and second.left:
            q.append(first.left)
            q.append(second.right)
            q.append(first.right)
            q.append(second.left)

    # At the end of the while loop, the stack will contain the values in reverse order
    for i in range(len(s)-1,-1,-1):
        print(s[i], end=' ')
    # for elements in reversed(s):
    #     print elements,


# Print elements diagonally
def diagonal(node):
    if not node:
        return

    q = [node,None]
    while q:
        cur = q.pop(0)

        if not cur:
            if not q:
                return
            print(' ')
            q.append(None)
        else:
            # Prints data as long as there exists a right child
            while cur:
                print(cur.data, end=' ')
                # Adds left child to a queue
                if cur.left:
                    q.append(cur.left)
                cur = cur.right


root = Node(1)
insert(root,2)
insert(root,9)
insert(root,7)
insert(root,4)
insert(root,3)
insert(root,99)

diagonal(root)
