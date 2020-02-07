# 4-4_Check_Balanced.py

# Implement a function to check if a binary tree is balanced (heights of the
# two subtrees of any node never differ by more than one).

# Assumptions
# Tree is binary tree, not necessarily BST
# Tree fits on single machine or API is equivalent

# Approach, complexity, tradeoffs, potential improvements
# Recursive check for height given root node
# compare height of two children of given node, if off by more than 1
# then return false
# At most we visit each node, so this algorithm is O(N) time and O(N) space
# since we will have recursive calls on the stack.

# Edge cases
# Empty tree
# Single node
# Very unbalanced

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def get_height(root: TreeNode, height=0: int) -> int:
#     """Return the max height of a node of a binary tree."""

#     if root == None:
#         return height
#     else:
#         height += 1
#         return max(get_height(root.left, height), get_height(root.right, height))

# check get_height()
#  10
#  /\
# 5  20
#    /\
#   3  7
#  /\
# 9  18

# root = 10 height = 1 -> max(?, ?) -> max(2, 4) -> return 4
# root = 5 height = 2 -> return 2
# root = 20 height = 2
# root = 7 height = 3 -> max(3, ?) -> max(3, 4) -> 4
# root = 3 height = 3
# root = 9 height = 4 -> return 4
# root = 18 height = 4 -> return 4

from typing import List

def check_balanced_recursive(root: TreeNode):
    """Is a binary tree balanced (no two subtrees differ by more than 1)?"""

    # use a list so it can be modified outside of the function
    return_bool = [True]

    def helper(root: TreeNode, return_bool: List, height: int = 0) -> int:
        """Recursive helper."""

        if root == None:
            return height

        else:
            height += 1

            # check heights
            left_height = helper(root.left, return_bool, height)
            right_height = helper(root.right, return_bool, height)

            if abs(left_height - right_height) > 1:
                return_bool[0] = return_bool[0] and False
            else:
                return_bool[0] = return_bool[0] and True

            return max(left_height, right_height)


    helper(root, return_bool, 0)

    return return_bool[0]



# check get_height()
#  10
#  /\
# 5  20
#    /\
#   3  7
#  /\
# 9  18

# return_bool = []
# root = 10 height = 0+1 = 1
# left_height:
# root = 5 height = 1+1 = 2
# left_height = right_height = 2 return_bool = [True]
# right_height:
# root = 20 height = 1+1 = 2
# left_height:
# root = 3 height = 2+1 = 3
# left_height:
# root = 9 height = 3+1 = 4
# left_height = 4
# right_height:
# root = 18 height = 3+1 = 4
# left_height - right_height = 0 return_bool = [True, True]

# root = 7 height = 2+1 = 3
# left_height = 4 - right_height = 3 => 1 return_bool = [True, True, True]

# root = 10
# left_height = 2
# right_height = 4
# abs(left_height - right_height) = 2 > 1
# return_bool = [True, True, True, False]

# return False which is correct


# Test Cases

import unittest

class TestCheckBalanced(unittest.TestCase):

    def setUp(self):
        #  10
        #  /\
        # 5  20
        #    /\
        #   3  7
        #  /\
        # 9  18

        self.n10 = TreeNode(10)
        self.n5 = TreeNode(5)
        self.n20 = TreeNode(20)
        self.n3 = TreeNode(3)
        self.n7 = TreeNode(7)
        self.n9 = TreeNode(9)
        self.n18 = TreeNode(18)


        self.n10.left = self.n5
        self.n10.right = self.n20

        self.n20.left = self.n3
        self.n20.right = self.n7

        self.n3.left = self.n9
        self.n3.right = self.n18

        # # testing
        self.n12 = TreeNode(12)
        self.n7.right = self.n12


    def test_example_1(self):

        self.assertFalse(check_balanced_recursive(self.n10))


    def test_edge_cases(self):

        self.assertTrue(check_balanced_recursive(self.n18))
        self.assertTrue(check_balanced_recursive(None))


if __name__ == '__main__':
    unittest.main()












