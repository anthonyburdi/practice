"""Test cases for add_two_numbers.py."""

import unittest

from add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(unittest.TestCase):
    """Test function of solution."""

    def setUp(self):
        """Set up the lists."""
        # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

        self.solution = Solution()
        self.num_list_1 = ListNode(2)
        self.num_list_1.next = ListNode(4)
        self.num_list_1.next.next = ListNode(3)
        self.num_list_2 = ListNode(5)
        self.num_list_2.next = ListNode(6)
        self.num_list_2.next.next = ListNode(4)

    def test_question_test_case(self):
        """Test the case from the question."""
        node = ListNode(7)
        node.next = ListNode(0)
        node.next.next = ListNode(8)
        self.assertEqual(
            node,
            self.solution.addTwoNumbers(self.num_list_1, self.num_list_2)
        )

if __name__ == '__main__':
    unittest.main()
