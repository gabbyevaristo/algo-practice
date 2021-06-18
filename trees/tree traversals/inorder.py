def main():
    root = Node(20)
    root.insert(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(30)
    root.insert(23)
    root.insert(21)
    print(root.inorderTraversal(root))


class Node:

    def __init__(self, data):
        """Initializes Node data attributes."""

        self.data = data
        self.left = None
        self.right = None


    def insert(self, val):
        """Insert values to tree accordingly."""

        # Add value to left of root if value is less than root
        if val < self.data:
            if not self.left:
                self.left = Node(val)
            else:
                # Calls insert using left of current value
                self.left.insert(val)

        # Add value to right of root if value is greater than root
        if val > self.data:
            if not self.right:
                self.right = Node(val)
            else:
                # Calls insert using right of current value
                self.right.insert(val)


    def inorderTraversal(self, val):
        """Performs LNR traversal algorithm using recursion."""

        # Create an empty list
        tree = []

        # Move to the furthest left node. Add value to the list and traverse
        # right tree. Move backwards to previous "left" node, add the value
        # to the list, and then traverse right tree. Repeat.
        if val:
            tree = tree + self.inorderTraversal(val.left)
            tree.append(val.data)
            tree = tree + self.inorderTraversal(val.right)
        return tree


if __name__ == '__main__':
	main()
