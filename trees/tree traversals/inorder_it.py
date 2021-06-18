def main():
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.right = Node(6)
    print(root.inorderIteration(root))


class Node:

    def __init__(self, data):
        """Initializes Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def inorderIteration(self, root):
        """Performs LNR traversal algorithm iteratively."""

        # Check for empty tree
        if not root:
            return

        # Create a temporary stack
        stack, tree = [], []
        cur = root

        while stack or cur:

            # Add current node to stack, and make
            # current to current's left child
            if cur:
                stack.append(cur)
                cur = cur.left

            # Pop top of stack, add it to the tree,
            # and make current to current's right child
            else:
                node = stack.pop()
                tree.append(node.data)
                cur = node.right

        return tree


if __name__ == "__main__":
    main()
