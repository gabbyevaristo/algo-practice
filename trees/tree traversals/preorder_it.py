def main():
    root = Node(20)
    root.left = Node(10)
    root.left.right = Node(15)
    root.left.left = Node(8)
    root.left.left.left = Node(6)
    root.right = Node(30)
    root.right.left = Node(23)
    root.right.left.left = Node(21)
    print(root.preorderIteration(root))


class Node:

    def __init__(self, data):
        """Initialize Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def preorderIteration(self, root):
        """Performs NLR traversal algorithm iteratively."""

        """1) Create an empty stack
           2) Push root node to stack.
           3) Do the following while stack is not empty:
              a) Pop last item from the stack and add it to the result.
              b) Push the right child of the popped item to the stack.
              c) Push the left child of the popped item to the stack."""

        # Check for empty tree
        if not root:
            return

        # Create a temporary stack and push root to it
        stack, tree = [root], []

        # Run as long as the stack is not empty
        while stack:

            # Pop top item from stack and add it to the list
            node = stack.pop()
            tree.append(node.data)

            # Right child is pushed first so that left child is
            # processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return tree


if __name__ == "__main__":
    main()
