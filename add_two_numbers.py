"""Add Two Numbers."""
# https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        digits_1 = []
        digits_2 = []

        while l1:
            digits_1.append(l1.val)
            l1 = l1.next

        while l2:
            digits_2.append(l2.val)
            l2 = l2.next

        print digits_1
        print digits_2
        sum_digits = []

        for i, digit in enumerate(digits_1):
            sum_digits.append(digit + digits_2[i])

        # deal with carry
        for idx, digit in enumerate(sum_digits):
            if digit >= 10:
                sum_digits[idx] = digit % 10
                if idx <= len(sum_digits) - 1:
                    sum_digits[idx + 1] += digit / 10

        nodes = []
        # output = ListNode(sum_digits[0])

        for digit in sum_digits:
            nodes.append(ListNode(digit))

        for idx, node in enumerate(nodes):
            if idx < len(nodes) - 1:
                node.next = nodes[idx + 1]

        return nodes[0]
