# 113-Path_Sum_II_MEDIUM.py

# https://leetcode.com/problems/path-sum-ii/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.solutions = []


    def pathSum(self, root: TreeNode, desired_sum: int) -> List[List[int]]:
        # Assumptions
        # Nodes have integer values
        # Nodes can be negative or zero
        # Paths with negative or zero nodes are also acceptable
        # Tree can be empty

        # Approach, Complexity, Tradeoffs, Potential Improvements
        # Store solutions in Solution class attribute for access
        # during calls of path sum
        # 1. Recursive traversal
        # recurse each node of the tree passing the sum up to that point to the
        # recursive call. If the sum plus the current node is less than the
        # desired sum keep traversing, if more than the sum then stop.
        # Actually if more than the sum is not a stopping point if we allow
        # negative numbers. Bc we could get back to the desired sum by adding
        # a negative (and vice versa if desired sum is negative by adding pos)
        # if we are at a leaf node then compare the sum to desired and add
        # to solutions if equal otherwise stop.
        # during each recursive call pass the current path values in as well
        # and append to this the current
        # Depth first so call on both children
        # 2. Iterative traversal
        # Depth first iterative traversal
        # Add child nodes to stack at each node
        # Add nodes to hashmap of node: path to get to that node
        # Once we hit a leaf node check the path to get to that node's sum
        # and if equal to the desired sum add to solutions  list
        # we can also check at each node whether the sum is greater than
        # the desired. If so we can stop iterating down that path to save
        # traversal time.
        # Also we can use this hash map as a memoization. If the node is
        # in the memo table already we already calculated it's history.
        # Time complexity O(n) since we hit every node
        # Space complexity at least O(n) since we keep a memo table
        # but each entry has a list as well... so this could be O(n^2) space
        # in both cases.
        # I'm not sure yet how to improve that space issue...

        # Edge Cases
        # Empty tree
        # Single node, one and two node
        # zero and negative values

        implementation = "Iterative"

        if implementation == "Recursive":

            # Recursive
            curr_sum = 0
            # curr_path = []
            curr_path = ()


            def helper(
                curr_node: TreeNode,
                curr_sum: int,
                desired_sum: int,
                curr_path: List[int]
            ):

                # Handle empty tree
                if root == None:
                    return

                # Recompute curr_sum
                curr_sum += curr_node.val

                # add curr_node to curr_path
                # curr_path.append(curr_node.val)
                temp_path_list = list(curr_path)
                temp_path_list.append(curr_node.val)
                curr_path = tuple(temp_path_list)

                # Check if we are at leaf node & whether to add solution
                if curr_node.left == None and curr_node.right == None:
                    if curr_sum == desired_sum:
                        self.solutions.append(list(curr_path))
                    else:
                        return

                # call on children if they exist
                if curr_node.left != None:
                    helper(curr_node.left, curr_sum, desired_sum, curr_path)
                if curr_node.right != None:
                    helper(curr_node.right, curr_sum, desired_sum, curr_path)

            helper(root, curr_sum, desired_sum, curr_path)
            return self.solutions


        if implementation == "Iterative":

            if root == None:
                return self.solutions

            stack = [root]
            paths = {}
            visited = set()

            while stack:
                curr_node = stack.pop()
                if curr_node in visited:
                    continue
                visited.add(curr_node)

                if curr_node not in paths:
                    paths[curr_node] = [curr_node.val]

                if curr_node.left != None:
                    stack.append(curr_node.left)
                    # add path
                    paths[curr_node.left] = paths[curr_node] + [curr_node.left.val]

                if curr_node.right != None:
                    stack.append(curr_node.right)
                    # add path
                    paths[curr_node.right] = paths[curr_node] + [curr_node.right.val]

                # if leaf node check for solution
                if curr_node.left == None and curr_node.right == None:
                    if sum(paths[curr_node]) == desired_sum:
                        self.solutions.append(paths[curr_node])

            return self.solutions


import unittest

class TestPathSum(unittest.TestCase):

    def setUp(self):

        self.solution = Solution()

        self.n5 = TreeNode(5)
        self.n4 = TreeNode(4)
        self.n8 = TreeNode(8)
        self.n11 = TreeNode(11)
        self.n13 = TreeNode(13)
        self.n4a = TreeNode(4)
        self.n7 = TreeNode(7)
        self.n2 = TreeNode(2)
        self.n5a = TreeNode(5)
        self.n1 = TreeNode(1)

        self.n5.left = self.n4
        self.n5.right = self.n8
        self.n4.left  = self.n11
        self.n8.left = self.n13
        self.n8.right = self.n4a
        self.n11.left = self.n7
        self.n11.right = self.n2
        self.n4a.left = self.n5a
        self.n4a.right = self.n1
        self.sum1 = 22

        self.a1 = TreeNode(-2)
        self.a2 = TreeNode(-3)
        self.sum2 = -5

        self.a1.right = self.a2

    def test_example_1(self):

        desired_sum = self.sum1
        answer = self.solution.pathSum(root=self.n5, desired_sum=desired_sum)
        self.assertEqual(
            answer.sort(),
            [
               [5,4,11,2],
               [5,8,4,5]
            ].sort()
        )

    def test_empty_list(self):

        desired_sum = self.sum1
        answer = self.solution.pathSum(root=None, desired_sum=desired_sum)
        self.assertEqual(
            answer.sort(),
            [].sort()
        )


    def test_negatives(self):

        desired_sum = self.sum2
        answer = self.solution.pathSum(root=self.a1, desired_sum=desired_sum)
        self.assertEqual(
            answer.sort(),
            [[-2,-3]].sort()
        )





if __name__ == '__main__':
    unittest.main()






