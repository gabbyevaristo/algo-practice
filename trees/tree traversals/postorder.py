def main():
    root = Node(20)
    root.insert(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(30)
    root.insert(23)
    root.insert(21)
    print(root.postorderTraversal(root))


class Node:

    def __init__(self, data):
        """Initializes Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def insert(self, val):
        """Inserts values to tree accordingly."""

        # Add value to left of root if value is less than root
        if val < self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                # Calls insert using left of current value
                self.left.insert(val)

        # Add value to right of root if value is greater than root
        if val > self.data:
            if self.right is None:
                self.right = Node(val)
            else:
                # Calls insert using right of current value
                self.right.insert(val)


    def postorderTraversal(self, val):
        """Performs LRN traversal algorithm using recursion."""

        # Create an empty list
        tree = []
        if val:
            tree = tree + self.postorderTraversal(val.left)
            tree = tree + self.postorderTraversal(val.right)
            tree.append(val.data)
        return tree


if __name__ == "__main__":
    main()
