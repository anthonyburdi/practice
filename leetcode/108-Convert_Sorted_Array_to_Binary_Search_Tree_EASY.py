# 108-Convert_Sorted_Array_to_Binary_Search_Tree_EASY.py

# 108. Convert Sorted Array to Binary Search Tree

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Assumptions
        # given sorted integers
        # can fit given array in memory on a single machine
        # Return None if given an empty array

        # Approach
        # I'm not sure if this is silly or not - but since it is sorted
        # maybe we can insert in a specific order to ensure that the height
        # is balanced? I can't think of how to prove this but:
        # Root node is the middle item (for odd lists or one of the two for
        # even lists). Then we begin inserting from the middle to the left
        # until we hit the beginning of the list.
        # Then we start at the end of the list and work in towards the middle
        # inserting as we go.
        # I think if we don't insert intelligently then we will have to re-
        # balance at some point which I think is out of the scope of this
        # question.

        # Complexity
        # Time: O(NlogN) since we visit each item in the list and then the
        # insertion takes logN time.
        # Space: O(N) since we have a tree in addition to our array with N items

        # Potential improvements
        # I think we could use a self balancing tree here

        # Edge cases
        # given empty nums list


        # IMPLEMENTATION

        # handle edge cases
        if nums == []:
            return None

        # create the root node
        mid_index = (len(nums)) // 2
        root = TreeNode(nums[mid_index])

        # # Insert from mid_index - 1 to the beginning of the list
        # for i in range(mid_index - 1, -1, -1):
        #     root = self._insert(root, nums[i])

        # # Insert from the end of the list to mid_index
        # for j in range(len(nums) - 1, mid_index, -1):
        #     root = self._insert(root, nums[j])

        root.left =  self.sortedArrayToBST(nums[:mid_index])
        root.right = self.sortedArrayToBST(nums[(mid_index + 1):])


        return root


    def _insert(self, node: TreeNode, val: int) -> None:
        """Recursive insert of value into binary search tree."""


        if val < node.val:
            if node.left == None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)

        if val >= node.val:
            if node.right == None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)


        return node


    def pre_order_array_repr(self, node: TreeNode) -> List:
        """Return the array representation using pre-order traversal."""

        return_array = []

        self._pre_order_array_repr(node, return_array)

        return return_array


    def _pre_order_array_repr(self, node: TreeNode, return_array: List) -> None:
        """Recursive pre-order traversal to generate list of values."""

        if node is not None:
            return_array.append(node.val)
            self._pre_order_array_repr(node.left, return_array)
            self._pre_order_array_repr(node.right, return_array)




import unittest

class TestSortedArrayToBST(unittest.TestCase):

    def setUp(self):

        self.solution = Solution()

    def test_example_1(self):

        nums = [-10,-3,0,5,9]

        node = self.solution.sortedArrayToBST(nums)

        print(self.solution.pre_order_array_repr(node))


    def test_leetcode_testcase_1(self):

        nums = [0,1,2,3,4,5]
        output = [3,1,5,0,2,4]

        node = self.solution.sortedArrayToBST(nums)
        array_repr = self.solution.pre_order_array_repr(node)

        self.assertEqual(
            output,
            array_repr
        )



if __name__ == '__main__':
    unittest.main()















