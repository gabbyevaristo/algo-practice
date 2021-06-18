def main():
    root = Node(20)
    root.insert(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(30)
    root.insert(23)
    root.insert(21)
    print(root.preorderTraversal(root))


class Node:

    def __init__(self, data):
        """Initialize Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def insert(self, val):
        """Insert values to tree accordingly."""

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


    def preorderTraversal(self, val):
        """Performs NLR traversal algorithm using recursion."""

        # Create an empty list
        tree = []

        # Add root to the list. Move to the left, adding each node to
        # the list until the left most node is hit. Once hit, go backwards
        # to the right of each node and add to the list.
        if val:
            tree.append(val.data)
            tree = tree + self.preorderTraversal(val.left)
            tree = tree + self.preorderTraversal(val.right)
        return tree


if __name__ == '__main__':
	main()
