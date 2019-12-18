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
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        left_ans = self.maxDepth(root.left)
        right_ans = self.maxDepth(root.right)

        return max(left_ans, right_ans) + 1


if __name__ == '__main__':
    s = Solution()

    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    print("Example 1: should be 3", s.maxDepth(n3))