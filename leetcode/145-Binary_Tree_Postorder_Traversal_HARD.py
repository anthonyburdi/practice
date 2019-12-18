# 145-Binary_Tree_Postorder_Traversal_HARD.py

# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def postorderTraversalRecursive(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        left_list = self.postorderTraversalRecursive(root.left)
        right_list = self.postorderTraversalRecursive(root.right)

        return left_list + right_list + [root.val]


    def postorderTraversalIterative(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        return_vals = []

        stack1 = [root]
        stack2 = []

        while stack1:
            popped_node = stack1.pop()
            stack2.append(popped_node)

            if popped_node.left:
                stack1.append(popped_node.left)
            if popped_node.right:
                stack1.append(popped_node.right)

        # we can also just reverse the list like so:
        # s = [node.val for node in stack2]
        # s.reverse()
        # return s

        while stack2:
            node = stack2.pop()
            return_vals.append(node.val)

        return return_vals





if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.right = n2
    n2.left = n3

    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5

    print("Recursive Example 1 should be [3,2,1]:", s.postorderTraversalRecursive(n1))
    print("Recursive Example 2 should be [4,5,2,3,1]:", s.postorderTraversalRecursive(a1))
    print("Iterative Example 1 should be [3,2,1]:", s.postorderTraversalIterative(n1))
    print("Iterative Example 2 should be [4,5,2,3,1]:", s.postorderTraversalIterative(a1))

