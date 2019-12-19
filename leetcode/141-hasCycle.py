# 141-hasCycle.py

# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.




# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Traverse the nodes
        # Create a set of visited nodes
        # if a node already exists in the list of visited
        # then there is a cycle

        # visited = set()

        # current = head
        # while current:
        #     if current in visited:
        #         return True  # we've already been to this node

        #     visited.add(current)

        #     current = current.next
        # return False

        # We can do this with
        # two pointers, one hitting each node and the other
        # hitting every other node. If they are ever equal then
        # there is a cycle
        # that should be constant memory since you don't have any other
        # list etc using up memory

        if not head or not head.next:
            return False

        current_slow = head
        current_fast = head.next

        while current_slow is not current_fast:

            if not current_fast or not current_fast.next:
                return False

            current_slow = current_slow.next
            current_fast = current_fast.next.next

        if current_slow == current_fast:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()

    # Example 1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    print("Example 1 should be True:", s.hasCycle(n1))

    # Example 2
    a1 = ListNode(1)
    a2 = ListNode(2)

    a1.next = a2
    a2.next = a1

    print("Example 2 should be True:", s.hasCycle(a1))

    # Example 3
    b1 = ListNode(1)

    print("Example 3 should be False:", s.hasCycle(b1))

    # Example 4
    c1 = ListNode(3)
    c2 = ListNode(2)
    c3 = ListNode(0)
    c4 = ListNode(-4)

    c1.next = c2
    c2.next = c3
    c3.next = c4

    print("Example 4 should be False:", s.hasCycle(c1))
