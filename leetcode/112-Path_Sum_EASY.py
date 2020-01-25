# 112-Path_Sum_EASY.py

# https://leetcode.com/problems/path-sum/

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, given_sum: int) -> bool:
        # Assumptions
    # sum given as an integer (see function signature)

        # Approach
    # depth first search computing sum for each traversal
    # if the sum is found then return True otherwise after searching all paths return false
    # let’s do this recursively
    # Let’s also memoize so we don’t do repeated work

        # Complexity
    # Time: O(N) since we go to each node
    # Space: O(1) since we keep track of only running sums

        # Potential improvements
    # Unknown at this time

        # Edge cases
    # Empty tree
    # Sum = 0
    # Negative numbers in tree
    # Negative sum


        # Approach
        # traverse the tree (depth first may be fastest, in case we find the
        # sum before hitting all the nodes)
        # for each node add to a "visited" set
        # add sum up to and including that node to a sums dict
        # if we are at a leaf node, then check the calculated sum against the
        # given sum and if true return true else continue searching
        # return false if we don't find it

        # see here for much simpler and faster solution:
        # https://leetcode.com/problems/path-sum/discuss/489184/Python3-Simple-98.3greater-Recursive

        # Complexity

        # Potential improvements

        # Edge cases

        visited = set()
        sums = {}

        def helper(root: TreeNode, given_sum: int, visited: set, sums: dict) -> bool:

            if root is None:
                return False

            # set node visited
            visited.add(root)
            # set node sums if not already there
            if root not in sums:
                sums[root] = root.val
            # set children sums
            if root.left is not None:
                sums[root.left] = sums[root] + root.left.val
            if root.right is not None:
                sums[root.right] = sums[root] + root.right.val

            # if no child nodes check sum against desired sum
            if root.left is None and root.right is None:
                if sums[root] == given_sum:
                    return True
                else:
                    return False

            return (
                helper(root.left, given_sum, visited, sums) or
                helper(root.right, given_sum, visited, sums)
            )

        return helper(root, given_sum, visited, sums)

import unittest

class TestHasPathSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):

        # Example:

        # Given the below binary tree and sum = 22,

        #       5
        #      / \
        #     4   8
        #    /   / \
        #   11  13  4
        #  /  \      \
        # 7    2      1
        # return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

        # node_datas = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        # sum = 22

        # in_process = []

        # while node_datas:
        #     node_data = node_datas.pop(0)

        given_sum = 22
        n5 = TreeNode(5)
        n4 = TreeNode(4)
        n8 = TreeNode(8)
        n11 = TreeNode(11)
        n13 = TreeNode(13)
        n4 = TreeNode(4)
        n7 = TreeNode(7)
        n2 = TreeNode(2)
        n1 = TreeNode(1)

        n5.left = n4
        n5.right = n8
        n4.left = n11
        n11.left = n7
        n11.right = n2
        n8.left = n13
        n8.right = n4
        n4.right = n1

        self.assertTrue(self.solution.hasPathSum(n5, given_sum))


if __name__ == '__main__':
    unittest.main()


