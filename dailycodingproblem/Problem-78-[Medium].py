# Problem-78-[Medium].py

# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

from typing import List

class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


def merge_sorted_linked_lists(heads: List[Node]) -> Node:
    """Merge k sorted singly linked lists into one sorted singly linked list."""

    # Assumptions
    # given lists are not empty
    # all data fits on a single machine
    # all value data is numerical
    # can remove items from their original lists

    # Approach
    # Create new list
    # loop through all other lists adding the next smallest item
    # O(k * n) where k is num lists and n is num items (average)

    # Edge cases
    # none given assumptions

    # create new list
    new_list_head = None
    new_list_tail = None

    while len(heads) > 0:
    # loop through each list's head to find next smallest item
        smallest_item = None
        list_with_smallest_item = None
        for idx, current_head in enumerate(heads):
            if smallest_item == None or current_head.val < smallest_item.val:
                smallest_item = current_head
                list_with_smallest_item = idx

        # remove found smallest item from original list and add to new
        if heads[list_with_smallest_item].next != None:
            heads[list_with_smallest_item] = heads[list_with_smallest_item].next
        else:
        # if removing last item then remove list from heads list
            heads.pop(list_with_smallest_item)

        smallest_item.next = None

    # add to new
        if new_list_tail != None:
            new_list_tail.next = smallest_item
            # move tail pointer
            new_list_tail = smallest_item
        else:
            new_list_tail = smallest_item

        if new_list_head == None:
            new_list_head = smallest_item

    return new_list_head



def convert_array_to_linked_list(given_list: List[int]) -> Node:
    """Return head node of a linked list from the given int array."""

    head = Node(given_list[0])

    curr = head
    i = 1
    while i < len(given_list):
        curr.next = Node(given_list[i])
        curr = curr.next
        i += 1

    return head


def linked_list_to_array(given_head: Node) -> List[int]:
    """Create array of values of a linked list."""

    curr = given_head
    values = []

    while curr != None:
        values.append(curr.val)
        curr = curr.next

    return values


import unittest

class TestMergeSortedLinkedLists(unittest.TestCase):

    def setUp(self):
        self.lists = [
            sorted([-550, -639, -243, 81, -200]),
            sorted([-570, -433, -540, -871, -25]),
            sorted([-924, -721, 516, -261, 308]),
            sorted([-340, 899, 567, 836, -161]),
            sorted([-519, -335, -982, -356, -466]),
            sorted([577, -347, -933, 148, 429])
        ]

        self.answer = []
        for l in self.lists:
            for i in l:
                self.answer.append(i)

        self.answer.sort()

        self.heads = []
        for l in self.lists:
            self.heads.append(convert_array_to_linked_list(l))



    def test_example_1(self):

        self.assertEqual(
            linked_list_to_array(merge_sorted_linked_lists(self.heads)),
            self.answer

        )


    def test_random_example(self):
        import random

        # create random lists
        lists = []
        for i in range(100):
            new_list = sorted(
                [random.randint(-1000,1000) for _ in range(random.randint(1,1000))]
            )
            lists.append(new_list)

        # create answer
        answer = []
        for l in lists:
            for i in l:
                answer.append(i)

        answer.sort()

        # create heads array of Node instances from arrays
        heads = []
        for l in lists:
            heads.append(convert_array_to_linked_list(l))

        self.assertEqual(
            linked_list_to_array(merge_sorted_linked_lists(heads)),
            answer

        )


if __name__ == '__main__':
    unittest.main()


