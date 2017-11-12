"""Binary search tree implementation."""
import random
import sys


class Node():
    """Node in a tree."""

    def __init__(self, data):
        """Initialize the node."""
        self.data = data
        self.left = None
        self.right = None


class Tree():
    """Binary search tree."""

    def __init__(self):
        """Initialize tree."""
        self.root = None

    def insert(self, node, value):
        """Insert new value into tree."""
        if not self.root:
            self.root = Node(value)
            return

        if value < node.data:
            if not node.left:
                node.left = Node(value)
            else:
                self.insert(node.left, value)

        if value > node.data:
            if not node.right:
                node.right = Node(value)
            else:
                self.insert(node.right, value)

    def pre_order(self, node=None):
        """Traverse in pre order (node, left, right)."""
        if node:
            sys.stdout.write(str(node.data) + ' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        """Traverse in order (left, node, right)."""
        if node:
            self.in_order(node.left)
            sys.stdout.write(str(node.data) + ' ')
            self.in_order(node.right)

    def post_order(self, node):
        """Traverse in reverse order (right, left, node)."""
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            sys.stdout.write(str(node.data) + ' ')

    def breadth_first(self):
        """Breadth first traversal."""
        print "not yet implemented"

    def search(self, value):
        """Search for the node that contains value."""
        if self.root.data == value:
            return self.root
        else:
            node = self.root
            while node.data != value:
                if value > node.data:
                    node = node.right
                else:
                    node = node.left

                if not node:
                    return None

                if node.data == value:
                    return node

test_tree = Tree()
# test_tree.insert(None, 1)

values_to_insert = range(1, 10)
random.shuffle(values_to_insert)

values_to_insert = [27, 14, 35, 10, 19, 31, 42]

for i in values_to_insert:
    test_tree.insert(test_tree.root, i)
print 'Root node: ', test_tree.root.data

print '=====> Printing pre_order()'
test_tree.pre_order(test_tree.root)

print '\n=====> Printing in_order()'
test_tree.in_order(test_tree.root)

print '\n=====> Printing post_order()'
test_tree.post_order(test_tree.root)

print "\nSearch for Node w 3: ", test_tree.search(3)
print "Search for Node w 100: ", test_tree.search(100)
print "Search for Node w 31: ", test_tree.search(31)
