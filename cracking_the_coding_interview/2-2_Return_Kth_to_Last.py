# 2-2_Return_Kth_to_Last.py

# Find the kth to last element of a singly linked list.

# See notebook for Assumptions, approach, complexity and improvements

class ListItem:

    def __init__(self, data):
        self.data = data
        self.next = None



def kth_to_last(head: ListItem, k: int) -> ListItem:
    """Return kth to last item of singly linked list given head node."""

    curr = head
    index = 0
    desired_node = None

    while curr:
        if index == k - 1:
            desired_node = head
        if index > k - 1:
            desired_node = desired_node.next

        curr = curr.next
        index += 1

    return desired_node


import unittest

class TestKthToLast(unittest.TestCase):

    def setUp(self):

        self.n0 = ListItem(0)
        self.n1 = ListItem(1)
        self.n2 = ListItem(2)
        self.n3 = ListItem(3)
        self.n4 = ListItem(4)
        self.n5 = ListItem(5)

        self.n0.next = self.n1
        self.n1.next = self.n2
        self.n2.next = self.n3
        self.n3.next = self.n4
        self.n4.next = self.n5


        self.a0 = ListItem(-5)
        self.a1 = ListItem(42)
        self.a2 = ListItem(3323453)
        self.a3 = ListItem("hello")
        self.a4 = ListItem("puppies")
        self.a5 = ListItem(16.39295)

        self.a0.next = self.a1
        self.a1.next = self.a2
        self.a2.next = self.a3
        self.a3.next = self.a4
        self.a4.next = self.a5

    def test_example_1(self):

        head = self.n0
        k = 2
        result = kth_to_last(head, k).data

        self.assertEqual(result, 4)


    def test_example_2(self):

        head = self.a0
        k = 2
        result = kth_to_last(head, k).data

        self.assertEqual(result, "puppies")


    def test_k_too_large(self):

        head = self.n0
        k = 55
        # Just returning node since there is no data attribute for null node
        result = kth_to_last(head, k)

        self.assertEqual(result, None)

        head = self.a0
        k = 2039
        # Just returning node since there is no data attribute for null node
        result = kth_to_last(head, k)

        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()





