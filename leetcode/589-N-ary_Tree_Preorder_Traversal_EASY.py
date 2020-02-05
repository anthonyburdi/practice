# 589-N-ary_Tree_Preorder_Traversal_EASY.py

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Given an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



# Follow up:

# Recursive solution is trivial, could you do it iteratively?



# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:

    def __init__(self):
        self.answer = []

    def preorder(self, root: 'Node') -> List[int]:

        # Assumptions
        # Children are stored in a list
        # entire tree fits on a single machine

        # Approach, complexity, Tradeoffs, Improvements
        # Iterative
        # Add each node's children to a stack and visit the top item
        # adding it's children to the top of the stack
        # continue until the stack is depleted
        # O(N) time and space since the stack could be the size of the tree

        # Recursive
        # call preorder on each child node in a loop
        # O(N) time and space complexity

        # Edge Cases
        # null root node

        if root is None:
            return root

        stack = [root]

        while stack != []:
            curr = stack.pop()
            self.answer.append(curr.val)
            stack.extend(curr.children[::-1])

        return self.answer





