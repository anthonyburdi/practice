# 24-Swap_Nodes_in_Pairs.py

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.



# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:


        if not head or not head.next:
            return head

        # Swap
        n1 = head
        n2 = head.next

        # call on rest of list to link to original head
        n1.next = self.swapPairs(n2.next)

        # move n2 to head
        n2.next = n1

        return n2



    def printLinkedList(self, prefix, head: ListNode) -> None:
        """Given head node, print the linked list."""

        print(prefix)

        if not head:
            print('No head node given.')

        current_node = head
        print_values = []

        while current_node:
            print_values.append(current_node.val)
            current_node = current_node.next

        print(" -> ".join(str(x) for x in print_values))



if __name__ == '__main__':
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    # print("Example 1 original linked list:")
    s.printLinkedList("Example 1 original linked list:", n1)

    new_head = s.swapPairs(n1)

    # print("Example 1, should be 2->1->4->3:")
    s.printLinkedList("Example 1, should be 2->1->4->3:", new_head)

