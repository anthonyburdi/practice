# 117-Populating_Next_Right_Pointers_in_Each_Node_II_MEDIUM.py

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.



# Follow up:

# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


# Example 1:



# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


# Constraints:

# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """Connect nodes on the same level left to right via .next attr."""

        # Assumptions
        # < 6000 nodes
        # node val can be negative
        # next is not populated in given tree
        # OK to use collections.deque instead of making a queue

        # Approach, complexity, tradeoffs, potential improvements
        # 1. Iterative breadth first to get each level
        # While popping off the level point the popped node next to the
        # item at the front of the queue
        # Continue until queue runs out
        # O(N) time since we visit all nodes
        # O(N) space since we store nodes in a queue while processing
        # 2. Perhaps instead of a queue of all nodes in a level
        # we process whenever there are 2 nodes in the queue
        # that way there is a constant (and small) amount of space used
        # Time O(N) space O(1)
        # we need to keep track of when we hit the end of a level so we don't
        # mess up the pointers.
        # We can have a prev_row and next_row queues and then while looping
        # and populating each we process the next pointer if either has two
        # nodes
        # if the prev_row is none then swap next and prev rows and continue

        # Actually this won't work bc processing the next_row will require a new
        # next row to store the new elements

        # Hmm there has to be a better solution

        # I can't think of one so let's go with this for now
        # I don't think recursion will make it better, except that the problem
        # statement says the extra space from the recursion stack doesn't count
        # towards the space (would that also include the iterative queue? since
        # it's essentially the same thing?)

        # Edge cases
        # root = None - Handled
        # single node - Handled
        # two nodes - Handled

        # Handle edge case root = None
        if root == None:
            return root


        prev_row = deque([root])
        next_row = deque()

        while len(prev_row) > 0 or len(next_row) > 0:

            # Check if prev row is empty, swap prev and next if so
            if len(prev_row) == 0:
                prev_row = next_row.copy() # TODO: Does deque support copy? Is this necessary?
                next_row = deque()

            # Check if prev_row has 2 or more items, process them if so
            # Nevermind, We will process prev_row if it is not empty
            # if len(prev_row) >= 2:

            else:
                # Pop first item and add it's children to next_row
                curr_item = prev_row.popleft()
                if curr_item.left != None:
                    next_row.append(curr_item.left)
                if curr_item.right != None:
                    next_row.append(curr_item.right)

                # set curr_item.next to first item in prev_row if exists else None
                if len(prev_row) >= 1:
                    curr_item.next = prev_row[0]
                else:
                    curr_item.next = None

            # Check if next_row has 2 or more items, process them if so
            # Nevermind, just process as we see them

        return root




















