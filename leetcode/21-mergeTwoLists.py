# 21-mergeTwoLists.py

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # First define a function to help add nodes
        def append_node(head_node, node_to_add):
            """Append a node to the end of a singly linked list given head_node"""
            if not head_node.next:
                head_node.next = node_to_add
                return
            last = head_node
            while last.next:
                last = last.next
            last.next = node_to_add
            return

        # Loop thorugh all nodes of l1 and l2
        # at each step compare which node is smaller, then add that
        # smaller node to the output list

        # first initialize the first node
        if l1 and l2:
            if l1.val <= l2.val:
                output_list = ListNode(l1.val)
                l1 = l1.next
            else:
                output_list = ListNode(l2.val)
                l2 = l2.next

        # If given only one list or none, return appropriately:
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None

        while l1 and l2:
            if l1.val <= l2.val:
                append_node(
                    head_node=output_list,
                    node_to_add=ListNode(l1.val)
                )
                l1 = l1.next
            else:
                append_node(
                    head_node=output_list,
                    node_to_add=ListNode(l2.val)
                )
                l2 = l2.next

        # If one list has run out of items, add rest of other list to output
        if l1:
            append_node(
                head_node=output_list,
                node_to_add=l1
            )
        elif l2:
            append_node(
                head_node=output_list,
                node_to_add=l2
            )

        return output_list


if __name__ == '__main__':

    solution = Solution()

    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    l1 = ListNode(1)
    l1_a = ListNode(2)
    l1_b = ListNode(4)
    l1.next = l1_a
    l1_a.next = l1_b

    l2 = ListNode(1)
    l2_a = ListNode(3)
    l2_b = ListNode(4)
    l2.next = l2_a
    l2_a.next = l2_b

    print("l1: ")
    printval = l1
    while printval:
        print(printval.val)
        printval = printval.next

    print("l2: ")
    printval = l2
    while printval:
        print(printval.val)
        printval = printval.next

    output_list = solution.mergeTwoLists(l1, l2)

    print("SOLUTION: -----------------------------")
    while output_list:
        print(output_list.val)
        output_list = output_list.next


    print("Solution with None inputs")
    output_list = solution.mergeTwoLists(None, None)
    while output_list:
        print(output_list.val)
        output_list = output_list.next

    # Input: 2, 1
    # Output: 1->2
    l1 = ListNode(2)

    l2 = ListNode(1)

    print("l1: ")
    printval = l1
    while printval:
        print(printval.val)
        printval = printval.next

    print("l2: ")
    printval = l2
    while printval:
        print(printval.val)
        printval = printval.next

    output_list = solution.mergeTwoLists(l1, l2)

    print("SOLUTION: -----------------------------")
    while output_list:
        print(output_list.val)
        output_list = output_list.next