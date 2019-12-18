# 144-Binary_Tree_Preorder_Traversal_MEDIUM.py

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# ---------------------------- SOLUTION
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversalRecursive(self, root: TreeNode) -> List[int]:

        # Recursive solution
        if not root:
            return []

        # traverse both left and right
        left_list = self.preorderTraversalRecursive(root.left)
        right_list = self.preorderTraversalRecursive(root.right)

        return [root.val] + left_list + right_list

    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:

        # Iterative solution
        if not root:
            return []

        node_stack = [root]

        return_vals = []

        while node_stack:

            # get the current node and add it to our return
            current_node = node_stack.pop()
            return_vals.append(current_node.val)

            # add right nodes first to stack so they are processed after left
            if current_node.right:
                node_stack.append(current_node.right)
            if current_node.left:
                node_stack.append(current_node.left)

        return return_vals


if __name__ == '__main__':
    solution = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3

    print(solution.preorderTraversalRecursive(n1))


    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5

    print(solution.preorderTraversalRecursive(a1))


    print(solution.preorderTraversalIterative(n1))
    print(solution.preorderTraversalIterative(a1))