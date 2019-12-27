# 2-1_Remove_Dups.py

# Chapter 2 | Linked Lists

# 2.1 Remove Dups:
# Write code to remove duplicates from an unsorted linked list.

# FOLLOW UP

# How would you solve this problem if a temporary buffer is not allowed?

# Assumptions, Approach, Time & Space Complexity & Possible Improvements:

# Assumptions:
# Singly linked list
# Assume we keep the first instance of the data and remove following duplicates
# First assume positive integers as data
# Assume we delete the first occurrences of the data, leaving the last
# (rather than keeping the first and deleting the rest)

# Approach:
# Approach 1: store data that has been visited in a hashset. When traversing
# the list, if the data already exists in the hashset then delete that node
# and continue traversing.
# Approach 2: Without temporary buffer. Use two pointers. First pointer
# starts at the first node, second pointer starts at the second node
# traverse the second pointer, removing nodes equal to the first
# then move the first pointer to the second node and the second pointer to the
# third node and repeat.

# Time & Space Complexity:
# Approach 1: O(N) time since we have to walk the list. Checking for an item
# in a hashset is O(1) so overall we are O(N). Deleting items is done during
# the walk so that adds only constant extra time.
# O(N) additional space for the hashset, however this will be smaller than
# the original dataset if there are duplicates.
# Approach 2: O(N^2) time since we have to check each pair of data.
# O(1) space since we don't have an additional dataset, just walking the
# original

# Possible improvements:
# I can't think of any, just the time/space tradeoff of approach 1 & 2.
# maybe leaving the first occurrence of a node and deleting the following
# rather than deleting the earliest occurrence would be best.
# see LinkedList.remove_node() vs LinkedList.remove_node_data()


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None


    def remove_node_data(self, data_to_remove):
        """Remove the first occurrence of data_to_remove."""
        # remove head if it is node
        if self.head.data == data_to_remove:
            self.head = self.head.next
            # return since we only want to remove first occurrence
            return

        # walk the list, if we find node then replace prev.next with
        # curr.next so the node is cut out of the list
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data_to_remove:
                # skip over the current
                prev.next = curr.next

                # return since we only want to remove first occurrence
                return

            else:
                # Move prev to the current node
                prev = curr
            # Move curr to the next node
            curr = curr.next


    def remove_node(self, node_to_remove):
        """Remove the node at node_to_remove."""
        # remove head if it is node
        if self.head == node_to_remove:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr == node_to_remove:
                prev.next = curr.next
                return
            else:
                prev = curr
            curr = curr.next


    def print_linked_list(self):

        if not self.head:
            print("Empty Linked List")

        curr = self.head

        while curr:
            print(curr.data)
            if curr.next:
                curr = curr.next
            else:
                curr = None


    def linked_list_as_list(self):

        linked_list_as_list = []

        if not self.head:
            return linked_list_as_list

        curr = self.head
        while curr:
            linked_list_as_list.append(curr.data)
            if curr.next:
                curr = curr.next
            else:
                curr = None

        return linked_list_as_list


def remove_dups(linked_list, approach):
    """Remove duplicates from an unsorted linked list."""

    # Approach 1: store data that has been visited in a hashset.
    # When traversing
    # the list, if the data already exists in the hashset then delete
    # that node
    # and continue traversing.
    if approach == 1:

        if not linked_list.head:
            return

        visited = set()

        curr = linked_list.head

        while curr:
            if curr.data in visited:
                # remove the first occurrence of the data
                # linked_list.remove_node_data(curr.data)

                # remove the second and future occurrences of the data
                linked_list.remove_node(curr)
            else:
                visited.add(curr.data)
            curr = curr.next

    # Approach 2: Without temporary buffer. Use two pointers. First pointer
    # starts at the first node, second pointer starts at the second node
    # traverse the second pointer, removing nodes equal to the first
    # then move the first pointer to the second node and the second pointer
    # to the
    # third node and repeat.
    if approach == 2:

        # there can't be duplicates if it's empty or only has a single element
        if not linked_list.head or not linked_list.head.next:
            return

        curr_node_1 = linked_list.head
        curr_node_2 = curr_node_1.next

        while curr_node_1:

            while curr_node_2:

                if curr_node_1.data == curr_node_2.data:

                    linked_list.remove_node(curr_node_2)

                curr_node_2 = curr_node_2.next

            curr_node_1 = curr_node_1.next
            if curr_node_1:
                curr_node_2 = curr_node_1.next
            else:
                return



import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

        self.head = Node(5)

        self.linked_list.head = self.head

        self.n1 = Node(63)
        self.n2 = Node(32)
        self.n3 = Node(5)
        self.n4 = Node(98)
        self.n5 = Node(63)

        self.linked_list.head.next = self.n1
        self.linked_list.head.next.next = self.n2
        self.linked_list.head.next.next.next = self.n3
        self.linked_list.head.next.next.next.next = self.n4
        self.linked_list.head.next.next.next.next.next = self.n5

        # Test case 2

        self.linked_list_2 = LinkedList()

        self.head_2 = Node(124)

        self.linked_list_2.head = self.head_2

        self.a1 = Node(45)
        self.a2 = Node(324)
        self.a3 = Node(75)
        self.a4 = Node(19)
        self.a5 = Node(324)
        self.a6 = Node(324)
        self.a7 = Node(324)
        self.a8 = Node(324)

        self.linked_list_2.head.next = self.a1
        self.linked_list_2.head.next.next = self.a2
        self.linked_list_2.head.next.next.next = self.a3
        self.linked_list_2.head.next.next.next.next = self.a4
        self.linked_list_2.head.next.next.next.next.next = self.a5
        self.linked_list_2.head.next.next.next.next.next.next = self.a6
        self.linked_list_2.head.next.next.next.next.next.next.next = self.a7
        self.linked_list_2.head.next.next.next.next.next.next.next.next = self.a8


    def test_printing(self):

        self.linked_list.print_linked_list()

        # Should print:
        # 5
        # 63
        # 32
        # 5
        # 98
        # 63


    def test_linked_list_as_list(self):

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [5, 63, 32, 5, 98, 63]
        )


    def test_remove_node_data_32(self):
        self.linked_list.remove_node_data(32)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [5, 63, 5, 98, 63]
        )


    def test_remove_node_data_5_head(self):
        self.linked_list.remove_node_data(5)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [63, 32, 5, 98, 63]
        )


    def test_remove_node_data_63(self):
        self.linked_list.remove_node_data(63)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [5, 32, 5, 98, 63]
        )


    def test_remove_node_n2_32(self):
        self.linked_list.remove_node(self.n2)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [5, 63, 5, 98, 63]
        )


    def test_remove_node_head_5(self):
        self.linked_list.remove_node(self.head)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [63, 32, 5, 98, 63]
        )


    def test_remove_node_n5_63(self):
        self.linked_list.remove_node(self.n5)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            [5, 63, 32, 5, 98]
        )


    def test_remove_dups_approach_1(self):

        remove_dups(self.linked_list, approach=1)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            # Remove first occurrences of dupes
            # [32, 5, 98, 63]
            # Remove second and future occurrences of dupes
            [5, 63, 32, 98]
        )

        remove_dups(self.linked_list_2, approach=1)

        self.assertEqual(
            self.linked_list_2.linked_list_as_list(),
            [124, 45, 324, 75, 19]
        )


    def test_remove_dups_approach_2(self):
        remove_dups(self.linked_list, approach=2)

        self.assertEqual(
            self.linked_list.linked_list_as_list(),
            # Remove first occurrences of dupes
            # [32, 5, 98, 63]
            # Remove second and future occurrences of dupes
            [5, 63, 32, 98]
        )

        remove_dups(self.linked_list_2, approach=2)

        self.assertEqual(
            self.linked_list_2.linked_list_as_list(),
            [124, 45, 324, 75, 19]
        )


if __name__ == '__main__':
    unittest.main()
