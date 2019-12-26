# binary_tree.py
# https://www.youtube.com/watch?v=oSWTXtMglKE&list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt


# Node class with pointer to left and right, data + constructor
class Node:
    def __init__(self, data: int) -> None:
        self.left = None
        self.right = None
        self.data = data


    def insert(self, value: int) -> None:
        """Insert new value recursively."""
        # If value is less, go left
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        # Otherwise go right
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value: int) -> bool:
        """Check if tree contains value recursively."""
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print_data(self):
        print("---------------------------------------")
        print("Printing node data:")
        if self.data:
            print("Data:", self.data)
        if self.left:
            print("Left Data:", self.left.data)
        if self.right:
            print("Right Data:", self.right.data)
        print("---------------------------------------")

    def print_in_order(self):
        """Print node data in order (left -> root -> right)."""
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()


    def print_pre_order(self):
        """Print node data in pre-order (root -> left -> right)."""
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()


    def print_post_order(self):
        """Print node data in post-order (left -> right -> root)."""
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)


if __name__ == '__main__':

    # Example 1
    # insert 8 into:
    #   10
    #  /  \
    # 5   15

    # Output
    #   10
    #  /  \
    # 5   15
    #  \
    #   8

    # initialize nodes
    n10 = Node(10)
    n5 = Node(5)
    n15 = Node(15)

    # build tree
    n10.left = n5
    n10.right = n15

    # insert new node
    n10.insert(8)

    # print nodes
    n10.print_data()
    n5.print_data()
    n15.print_data()
    n5.right.print_data()

    # Example 1a - does tree now contain 8?

    root = n10
    print("Does tree contain 8?:", root.contains(8))
    print("Does tree contain 85?:", root.contains(85))

    # Example 1b - print in order
    print("Printing tree in order:")
    n10.print_in_order()

    print("Printing tree in pre order:")
    n10.print_pre_order()

    print("Printing tree in post order:")
    n10.print_post_order()

