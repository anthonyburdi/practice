# 226-Invert_Binary_Tree_EASY.py

# https://leetcode.com/problems/invert-binary-tree/

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Assumptions
        # Tree fits on a single computer

        # Approach, complexity, tradeoffs, potential improvements
        # Recursively swap left and right for each root node
        # O(N) time since we hit each node once
        # O(N) space as well for the recursion stack

        # We can do this iteratively with a queue, adding each child node
        # that would still be O(N) time and O(N) space for the  queue which
        # at max size would be all the leaf nodes 2^depth which is
        # 2^depth / (2^(depth - 1) + 2^(depth - 2) + ...) of the tree which
        # converges to 1/2 the nodes but 1/2 is a constant so still O(N) space

        # Edge cases
        # single node
        # no node
        # two nodes (maybe but prob not)

        # Recursive

        # def helper(root: TreeNode):
        #     # Base Case
        #     if root is None:
        #         return
        #     else:
        #         temp = root.left
        #         root.left = root.right
        #         root.right = temp

        #         self.invertTree(root.left)
        #         self.invertTree(root.right)

        # helper(root)

        # return root

        # Iterative

        if root is None:
            return
        else:
            from collections import deque
            queue = deque([root])

            while queue:
                current = queue.popleft()
                temp = current.left
                current.left = current.right
                current.right = temp
                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

        return root














