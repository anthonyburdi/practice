# 232-Implement_Queue_using_Stacks_EASY.py

# https://leetcode.com/problems/implement-queue-using-stacks/

# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:

# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


# See also: https://docs.google.com/document/d/1v-dR-KJmNdhCycCb2kPaZl4rWewsQkFlh5pv6Ri0CNM/edit

# Assumptions
# All data can fit on a single machine or API is the same

# Approach, Complexity, Potential Improvements, Tradeoffs
# Use two stacks. The queue is the first stack when peeking, popping or checking if empty
# when pushing, use the second stack. First empty in order (from top to bottom) the first stack
# into the second. Then push the new item onto the first stack and then the rest of the items
# from the second stack back on to preserve order. Now the added item is at the back of the queue
# Time Complexity: O(1) for pop, peek, empty. O(n) for push where n is the number of items currently in the queue
# Space complexity: O(1) since we are simply moving items back and forth from the two queues
# We could use a single list and add items to the front for a queue, or dequeue which is pythons
# built in queue (faster since enqueue and dequeue are both O(1).

# Edge Cases
# When the queue is empty, adding one item
# removing the last item
# removing when empty


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use a list as a stack and only call pop() not pop(0) etc.
        # This first stack is the queue except during the push operation so we call it queue
        self.queue = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # check if queue is empty, if so then just add the element
        if self.empty():
            self.queue.append(x)
            return

        # first create the second stack and add elements to it
        temp_stack = []
        for _ in range(len(self.queue)):
            temp_stack.append(self.queue.pop())

        # then add x to the first stack
        self.queue.append(x)

        # then add the second stack elements back to the first
        for _ in range(len(temp_stack)):
            self.queue.append(temp_stack.pop())


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
    # return the last element of the first stack, which is top element of queue
        return self.queue[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()