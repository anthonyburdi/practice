# 4-2_Minimal_Tree.py

# Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

# See notebook for Assumptions, Approach, Complexity, Potential Improvements, Diagrams, Tests, etc.

from typing import List

class TreeNode:
    """Simple tree node class."""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def binary_search_tree(nums: List) -> TreeNode:
    """Given a sorted (increasing order) array with unique integer elements return binary search tree with minimal height."""

    return helper(nums, 0, len(nums) - 1)


def helper(nums: List, left: int, right: int) -> TreeNode:
    if right < left:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = helper(nums, left, mid - 1)
    root.right = helper(nums, mid + 1, right)
    return root


def print_in_order(root: TreeNode) -> None:
    """Given a binary search tree root node print elements in order."""

    if root is not None:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


def list_in_order(root: TreeNode) -> List:
    """Given a binary search tree root node create a list of elements in order."""
    nums = []
    list_in_order_helper(root, nums)
    return nums


def list_in_order_helper(root: TreeNode, nums: List) -> None:

    if root is not None:
        list_in_order_helper(root.left, nums)
        nums.append(root.val)
        list_in_order_helper(root.right, nums)


import unittest

class TestBinarySearchTree(unittest.TestCase):

    def test_small_example(self):
        nums = [i for i in range(11)]
        self.assertEqual(
            nums,
            list_in_order(binary_search_tree(nums))
        )

    def test_small_example_2(self):
        nums = [i for i in range(1)]
        self.assertEqual(
            nums,
            list_in_order(binary_search_tree(nums))
        )

    def test_large_example(self):
        nums = [i for i in range(1001)]
        self.assertEqual(
            nums,
            list_in_order(binary_search_tree(nums))
        )


if __name__ == '__main__':

    # nums = [1,2,3,4,5,6,7,8]
    # root = binary_search_tree(nums)
    # print_in_order(root)
    # print(list_in_order(root))

    unittest.main()