# 104-Maximum_Depth_of_Binary_Tree_EASY.py

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.answer = 0

    def maxDepthBottomUp(self, root: TreeNode) -> int:

        # Bottom up
        if not root:
            return 0

        left_ans = self.maxDepthBottomUp(root.left)
        right_ans = self.maxDepthBottomUp(root.right)

        return max(left_ans, right_ans) + 1

    def maxDepthTopDown(self, root: TreeNode, depth: int) -> int:
        # Top down
        if root == None:
            return 0

        left_ans = self.maxDepthTopDown(root.left, depth + 1)
        right_ans = self.maxDepthTopDown(root.right, depth + 1)
        return max(left_ans, right_ans) + 1


import unittest

class TestMaxDepth(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.n3 = TreeNode(3)
        self.n9 = TreeNode(9)
        self.n20 = TreeNode(20)
        self.n15 = TreeNode(15)
        self.n7 = TreeNode(7)

        self.n3.left = self.n9
        self.n3.right = self.n20
        self.n20.left = self.n15
        self.n20.right = self.n7

    def test_example_1(self):
        answer = 3
        self.assertEqual(self.solution.maxDepthBottomUp(self.n3), answer)
        self.assertEqual(
            self.solution.maxDepthTopDown(self.n3, self.solution.answer),
            answer
        )


if __name__ == '__main__':
    unittest.main()
