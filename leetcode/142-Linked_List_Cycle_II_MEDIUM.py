# 142-Linked_List_Cycle_II_MEDIUM.py

# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.



# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.




# Follow-up:
# Can you solve it without using extra space?

# Assumptions
# singly linked list
# list fits on a single computer

# Approach, Complexity, Tradeoffs, Potential Improvements
# 1. first use slow/fast pointer to find out if it has a cycle
# also put each node:pos in a hashmap and if we
# hit a duplicate with the slow pointer then
# that is where the tail connects
# Maybe we only need a slow pointer and hashmap and not a fast pointer
# This is O(N) time and O(N) space since we keep a hashmap of visited nodes
# 2. To eliminate the space I think we need to increase the time.
# So for each node we traverse we have two slow pointers & fast. The first
# stays at the node, the second traverses until it either hits the first node
# or the fast pointer. If it hits the fast pointer then we increment the
# furthest back slow pointer and start all 3 pointers again.
# this is O(N^2) time complexity but O(1) space since we only have 3 pointers.

# Maybe there is an O(N) time and O(1) space solution?

# Edge Cases
# Single node with and without link
# No root node



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head == None:
            return head

        visited = {}
        curr = head
        i = 0

        while curr:
            if curr in visited:
                return curr
            else:
                visited[curr] = i
                curr = curr.next
                i += 1

        return None






