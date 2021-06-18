def main():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(25)
    #root.left.right = Node(15)
    # root.left.left = Node(8)
    # root.left.left.left = Node(6)
    # root.right = Node(30)
    # root.right.left = Node(23)
    # root.right.left.left = Node(21)
    print(root.postorderIteration(root))


class Node:

    def __init__(self, data):
        """Initializes Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def peek(self, stack):
        """Returns top of the stack."""

        if stack:
            return stack[-1]
        return None


    def postorderIteration(self, root):
        """Performs LRN traversal algorithm iteratively."""

        """1) Create an empty stack
           2) Push root node to stack.
           3) Do the following while stack is not empty:
              a) Pop last item from the stack and add it to the beginning of the result.
              b) Push the left child of the popped item to the stack.
              c) Push the right child of the popped item to the stack."""

        # Check for empty tree
        if not root:
            return

        # Create a temporary stack and push root to it
        stack, tree = [root], []    # tree is also a stack

        # Run as long as the stack is not empty
        while stack:
            # Pop top item from stack and add it to the beginning of the list
            node = stack.pop()
            tree.append(node.data)      # tree.insert(0,node.data)

            # Left child is pushed last so that it is processed last. Those processed
            # last are added to the beginning of the result
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Since values are in backwards, pop them from the tree and add them back
        # to the stack
        while tree:
            stack.append(tree.pop())

        return stack


if __name__ == "__main__":
    main()
