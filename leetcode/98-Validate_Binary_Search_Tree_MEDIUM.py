# 98-Validate_Binary_Search_Tree_MEDIUM.py

# https://leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Assumptions
# We can do this recursively without hitting stack depth issues
# Assume numeric values for data
# Assume integers
# No duplicate nodes

# Approach
# Recursive algorithm that runs itself on each child and returns "and" of all
# the subcalls
# Base case is when there are no left and right children then return True
# If the left subtree is greater than the root then return false
# also if the right subtree is greater than the root return false

# NOTE: Also need to keep upper and lower limits to make sure ALL of the
# subtree nodes are correct. (eg all of right subtree must be larger than
# ALL of left subtree, not just root)

# Time and space complexity
# Time complexity is O(N) since we have to hit each node
# Space complexity is also O(N) since we have a recursive call for each N
# on the stack


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:


        implementation = "Iterative"


        if implementation == "Recursive":
            # Recursive

            def helper(root: TreeNode, lower: int, upper: int) -> bool:

                if root == None:
                    return True

                # check if root is within the limits
                if root.val <= lower or root.val >= upper:
                    return False

                # call helper on left and right children
                return (
                    helper(root.left, lower, root.val) and
                    helper(root.right, root.val, upper)
                )

            return helper(root, float('-inf'), float('inf'))

        # Iterative
        if implementation == "Iterative":

            # Add child nodes to a stack and return false if any of the
            # constraints are missed as we remove the items and process them

            if root == None:
                return True

            stack = [(root, float('-inf'), float('inf'))]
            while stack != []:

                curr_node_with_limits =  stack.pop()

                # Shorten variable names
                curr_node = curr_node_with_limits[0]
                val = curr_node_with_limits[0].val
                lower = curr_node_with_limits[1]
                upper = curr_node_with_limits[2]

                # Check constraints
                if val <= lower or val >= upper:
                    return False

                # Add children to the stack
                if curr_node.left != None:
                    stack.append((curr_node.left, lower, val))
                if curr_node.right != None:
                    stack.append((curr_node.right, val, upper))

            # If no issues are found
            return True



import unittest

class TestIsValidBST(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

        # Example 1:

        #     2
        #    / \
        #   1   3

        # Input: [2,1,3]
        # Output: true

        self.ex1_n1 = TreeNode(1)
        self.ex1_n2 = TreeNode(2)
        self.ex1_n3 = TreeNode(3)
        self.ex1_n2.left = self.ex1_n1
        self.ex1_n2.right = self.ex1_n3

        # Example 2:

        #     5
        #    / \
        #   1   4
        #      / \
        #     3   6

        # Input: [5,1,4,null,null,3,6]
        # Output: false
        # Explanation: The root node's value is 5 but its right child's value is 4.

        self.ex2_n1 = TreeNode(1)
        self.ex2_n2 = TreeNode(2)
        self.ex2_n3 = TreeNode(3)
        self.ex2_n4 = TreeNode(4)
        self.ex2_n5 = TreeNode(5)
        self.ex2_n6 = TreeNode(6)

        self.ex2_n5.left = self.ex2_n1
        self.ex2_n5.right = self.ex2_n4
        self.ex2_n4.left = self.ex2_n3
        self.ex2_n4.right = self.ex2_n6


        # ex [1,null,1] = False

        # 1
        #  \
        #   1

        self.ex3_n1 = TreeNode(1)
        self.ex3_n2 = TreeNode(1)

        self.ex3_n1.right = self.ex3_n2


        # ex [10,5,15,null,null,6,20] = False

        #   10
        #  / \
        # 5   15
        #    / \
        #   6   20

        self.ex4_n10 = TreeNode(10)
        self.ex4_n5 = TreeNode(5)
        self.ex4_n15 = TreeNode(15)
        self.ex4_n6 = TreeNode(6)
        self.ex4_n20 = TreeNode(20)


        self.ex4_n10.left = self.ex4_n5
        self.ex4_n10.right = self.ex4_n15
        self.ex4_n15.left = self.ex4_n6
        self.ex4_n15.right = self.ex4_n20


    def test_example_1(self):
        self.assertTrue(self.solution.isValidBST(self.ex1_n2))

    def test_example_2(self):
        self.assertFalse(self.solution.isValidBST(self.ex2_n5))

    def test_example_3(self):
        self.assertFalse(self.solution.isValidBST(self.ex3_n1))

    def test_example_4(self):
        self.assertFalse(self.solution.isValidBST(self.ex4_n10))

    def test_no_root(self):
        self.assertTrue(self.solution.isValidBST(None))



if __name__ == '__main__':

    unittest.main()

    # # Example 1:

    # #     2
    # #    / \
    # #   1   3

    # # Input: [2,1,3]
    # # Output: true

    # ex1_n1 = TreeNode(1)
    # ex1_n2 = TreeNode(2)
    # ex1_n3 = TreeNode(3)
    # ex1_n2.left = ex1_n1
    # ex1_n2.right = ex1_n3

    # solution = Solution()

    # print("True:", solution.isValidBST(ex1_n2))

    # # Example 2:

    # #     5
    # #    / \
    # #   1   4
    # #      / \
    # #     3   6

    # # Input: [5,1,4,null,null,3,6]
    # # Output: false
    # # Explanation: The root node's value is 5 but its right child's value is 4.

    # ex2_n1 = TreeNode(1)
    # ex2_n2 = TreeNode(2)
    # ex2_n3 = TreeNode(3)
    # ex2_n4 = TreeNode(4)
    # ex2_n5 = TreeNode(5)
    # ex2_n6 = TreeNode(6)

    # ex2_n5.left = ex2_n1
    # ex2_n5.right = ex2_n4
    # ex2_n4.left = ex2_n3
    # ex2_n4.right = ex2_n6

    # print("False:", solution.isValidBST(ex2_n5))


    # # ex [1,null,1] = False

    # # 1
    # #  \
    # #   1

    # ex3_n1 = TreeNode(1)
    # ex3_n2 = TreeNode(1)

    # ex3_n1.right = ex3_n2

    # print("False:", solution.isValidBST(ex3_n1))

    # # ex [10,5,15,null,null,6,20] = False

    # #   10
    # #  / \
    # # 5   15
    # #    / \
    # #   6   20

    # ex4_n10 = TreeNode(10)
    # ex4_n5 = TreeNode(5)
    # ex4_n15 = TreeNode(15)
    # ex4_n6 = TreeNode(6)
    # ex4_n20 = TreeNode(20)


    # ex4_n10.left = ex4_n5
    # ex4_n10.right = ex4_n15
    # ex4_n15.left = ex4_n6
    # ex4_n15.right = ex4_n20

    # print("False:", solution.isValidBST(ex4_n10))


