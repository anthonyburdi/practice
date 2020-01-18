# 206-Reverse_Linked_List_EASY.py

# https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Assumptions
# singly linked list, given head node

# Approach
# iterative:
# start with first node and add successive to the front of it while
# node.next is not None. Change head node so we do this in place.
# e.g. just move nodes from input to output so we don't create a separate
# array

# Time and space complexity
# O(N) time complexity since we hit each of N nodes
# O(1) space complexity since we can do this using the existing nodes

# Potential improvements
# None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        # steps
        # Input: 1->2->3->4->5->NULL
        # Output: 5->4->3->2->1->NULL
        # 1. create copy of head, head.next
        # 2. set reversed_head to head, then clear it's next (since it will
        # be the end of the list)
        # 3. start from new head of input, save it's next as old_next
        # 4. set new head of input's next to reversed_head
        # 5. set new head of input to old_next

        node_to_move = head.next
        # move head to end head of new reversed list
        reversed_head = head
        reversed_head.next = None

        # add each node of input to beginning of reversed list
        while node_to_move:
            next_to_move = node_to_move.next

            # add node to beginning of reversed list
            old_reversed_head = reversed_head
            reversed_head = node_to_move
            reversed_head.next = old_reversed_head

            node_to_move = next_to_move

        return reversed_head

    def printLinkedList(self, head: ListNode):
        """Print a list data given head node."""

        output = []
        curr_node = head
        while curr_node:
            output.append(str(curr_node.val) + "->")
            curr_node = curr_node.next
        output.append("NULL")
        print("".join(output))


if __name__ == '__main__':
    solution = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    solution.printLinkedList(n1)

    reversed_list = solution.reverseList(n1)

    solution.printLinkedList(reversed_list)

