# 101-Symmetric_Tree_EASY.py

# https://leetcode.com/problems/symmetric-tree/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# Note:
# Bonus points if you could solve it both recursively and iteratively.

# See notebook for Assumptions, Approach, Complexity & Edge Cases

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if (
            (type(root) is not TreeNode) or
            (root is None) or
            (root.left is None and root.right is None)
        ):
            return True

        solution_type = "recursive"

        # Iterative
        if solution_type == "iterative":
            prev_queue = [root]
            next_queue = []

            while prev_queue:
                while prev_queue:
                    # load up next_queue
                    item = prev_queue.pop(0) # should use dequeue
                    if item is not None:
                        next_queue.append(item.left)
                        next_queue.append(item.right)

                # check for symmetry of next_queue
                if next_queue == []:
                    continue
                left = 0
                right = len(next_queue) - 1
                while left < right:
                    if next_queue[left] is None and next_queue[right] is None:
                        left += 1
                        right -= 1
                        continue
                    elif next_queue[left] is None or next_queue[right] is None:
                        return False
                    elif next_queue[left].val is not next_queue[right].val:
                        return False
                    left += 1
                    right -= 1

                prev_queue = next_queue
                next_queue = []

            return True

        if solution_type == "recursive":

            def helper(n1: TreeNode, n2: TreeNode) -> bool:
                if n1 is None and n2 is None:
                    return True
                elif n1 is None or n2 is None:
                    return False

                return (
                    (n1.val == n2.val) and
                    helper(n1.left, n2.right) and
                    helper(n1.right, n2.left)
                )

            return helper(root, root)


# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

import unittest

class TestIsSymmetric(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.n1 = TreeNode(1)
        self.n2 = TreeNode(2)
        self.n3 = TreeNode(2)
        self.n4 = TreeNode(3)
        self.n5 = TreeNode(4)
        self.n6 = TreeNode(4)
        self.n7 = TreeNode(3)

        self.n1.left = self.n2
        self.n1.right = self.n3
        self.n2.left = self.n4
        self.n2.right = self.n5
        self.n3.left = self.n6
        self.n3.right = self.n7

        self.a1 = TreeNode(1)
        self.a2 = TreeNode(2)
        self.a3 = TreeNode(2)
        self.a4 = TreeNode(3)
        self.a5 = TreeNode(3)

        self.a1.left = self.a2
        self.a1.right = self.a3
        self.a2.right = self.a4
        self.a3.right = self.a5


    def test_example_1(self):
        self.assertTrue(self.solution.isSymmetric(self.n1))


    def test_example_2(self):
        self.assertFalse(self.solution.isSymmetric(self.a1))



if __name__ == '__main__':
    unittest.main()




