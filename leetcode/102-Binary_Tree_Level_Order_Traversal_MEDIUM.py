# 102-Binary_Tree_Level_Order_Traversal_MEDIUM.py

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Let's do this iteratively
        # for each node add it's children to the overall queue
        # but also to a second queue for the level
        # for each level append to the main list

        if not root:
            return []

        return_queue = []
        level_queue = [root]
        next_level_queue = [1] # do while hack

        while next_level_queue:
            next_level_queue = [] # do while hack

            level_queue_vals = [node.val for node in level_queue]

            return_queue.append(level_queue_vals)

            while level_queue:
                first_item = level_queue.pop(0)

                if first_item.left:
                    next_level_queue.append(first_item.left)
                if first_item.right:
                    next_level_queue.append(first_item.right)

            level_queue = next_level_queue

        return return_queue

if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print("Example 1:", s.levelOrder(n1))


    a3 = TreeNode(3)
    a9 = TreeNode(9)
    a20 = TreeNode(20)
    a2 = TreeNode(2)
    a1 = TreeNode(1)
    a15 = TreeNode(15)
    a7 = TreeNode(7)
    a17 = TreeNode(17)
    a19 = TreeNode(19)
    a37 = TreeNode(37)
    a21 = TreeNode(21)

    a3.left = a9
    a3.right = a20
    a9.left = a2
    a9.right = a1
    a20.left = a15
    a20.right = a7
    a2.left = a17
    a2.right = a19
    a7.left = a37
    a7.right = a21

    print("Example 2:", s.levelOrder(a3))



