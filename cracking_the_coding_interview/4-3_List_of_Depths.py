# 4-3_List_of_Depths.py

# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth (e.g., if you have a tree with depth D, you'll have
# D linked lists).

# See notebook for Assumptions, Approach, Complexity, Potential Improvements

# Edge Cases
# empty tree
# single node
# two nodes?

from typing import List

class Node:
    """Node class that can be used in a binary tree or singly linked list."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return "Node: {} Left Child: {} Right Child: {} Next: {}".format(
            self.val, self.left, self.right, self.next
        )

    def __repr__(self):
        return "N" + str(self.val)


# Note - using this node class is probably unwise, but it does allow us
# to use the same instances for both the tree and linked list without copying
# the data... in some cases that may be desired. We probably would want to
# instead use a TreeNode and ListNode with specific functionality.


def list_of_depths(root: Node) -> List[Node]:
    """List of linked lists of rows of binary tree with root node."""

    # Handle edge cases
    if root == None: return []

    # Initialize
    row_nodes = [root]
    depth = 0
    prev_row = row_nodes[depth]
    next_row = []


    while prev_row:

        # Create next_row as a list
        while prev_row:
            if prev_row.left:
                next_row.append(prev_row.left)
            if prev_row.right:
                next_row.append(prev_row.right)
            prev_row = prev_row.next

        # Create linked list from next_row
        for i in range(1, len(next_row)):
            next_row[i - 1].next = next_row[i]

        # Add to output
        if next_row:
            row_nodes.append(next_row[0])
        else:
            break

        # Prep for next iteration
        depth += 1
        prev_row = row_nodes[depth]
        next_row = []

    return row_nodes

# Straight to linked list without list in between:

def append_to_linked_list(head: Node, node_to_add: Node) -> Node:
    """Add a node to the end of a linked list then return the head."""

    if head == None:
        return node_to_add

    curr = head
    # prev = None

    # while curr:
    #     prev = curr
    #     curr = curr.next

    # prev.next = node_to_add

    while True:
        if curr.next == None:
            curr.next = node_to_add
            break
        else:
            curr = curr.next

    return head


# def list_of_depths(root: Node) -> List[Node]:
#     """List of linked lists of rows of binary tree with root node."""

#     # Handle edge cases
#     if root == None: return []

#     # Initialize
#     row_nodes = [root]
#     depth = 0
#     prev_row = row_nodes[depth]
#     next_row = None


#     while prev_row:

#         # Create next_row as a list
#         while prev_row:
#             import pdb; pdb.set_trace()
#             if prev_row.left:
#                 next_row = append_to_linked_list(
#                     head=next_row,
#                     node_to_add=prev_row.left
#                 )
#             if prev_row.right:
#                 next_row = append_to_linked_list(
#                     head=next_row,
#                     node_to_add=prev_row.right
#                 )


#             prev_row = prev_row.next


#         # Add to output
#         if next_row is not None:
#             row_nodes.append(next_row)
#         else:
#             break

#         # Prep for next iteration
#         depth += 1
#         prev_row = row_nodes[depth]
#         next_row = None

#     return row_nodes


def linked_list_as_list(root: Node) -> List[Node]:
    """Return linked list as a list of nodes."""

    node_list = []
    curr = root

    while curr:
        node_list.append(curr)
        curr = curr.next

    return node_list



import unittest

class TestAppendToLinkedList(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)

        self.n1.next = self.n2
        self.n2.next = self.n3


    def test_simple_linked_list(self):

        output = append_to_linked_list(self.n1, self.n4)
        output_list = linked_list_as_list(output)
        desired_output = [self.n1, self.n2, self.n3, self.n4]
        self.assertEqual(output_list, desired_output)


    def test_append_multiple(self):

        output = append_to_linked_list(self.n1, self.n4)
        output = append_to_linked_list(output, self.n5)
        output = append_to_linked_list(output, self.n6)
        output_list = linked_list_as_list(output)
        desired_output = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6]
        self.assertEqual(output_list, desired_output)



class TestListOfDepths(unittest.TestCase):

    def setUp(self):

        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n7 = Node(7)
        self.n1.left = self.n2
        self.n1.right = self.n3
        self.n2.left = self.n4
        self.n2.right = self.n5
        self.n3.left = self.n6
        self.n3.right = self.n7

        self.n2.next = self.n3
        self.n4.next = self.n5
        self.n5.next = self.n6
        self.n6.next = self.n7

        self.output = [self.n1, self.n2, self.n4]


    def test_simple_example(self):

        self.assertEqual(
            list_of_depths(self.n1),
            self.output
        )


    def test_single_node(self):

        root = Node(1)
        self.assertEqual(list_of_depths(root), [root])


    def test_empty_node(self):

        self.assertEqual(list_of_depths(None), [])


    def test_two_nodes(self):

        root = Node(1)
        child = Node(2)
        root.left = child

        self.assertEqual(list_of_depths(root), [root, child])


    def test_two_nodes_2(self):

        root = Node(1)
        child = Node(2)
        root.right = child

        self.assertEqual(list_of_depths(root), [root, child])


if __name__ == '__main__':
    unittest.main()














