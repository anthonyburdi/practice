# 3-4_Queue_via_Stacks.py

# implement a MyQueue class which implements a queue using two stacks

# Assumptions
# numeric data types
# all can fit in memory on a single machine


# Approach
# create a stack which new items get added to
# then pop off the items one by one to put into a separate stack
# these items then will be in reverse order, so popping them off will
# function like a queue
# For an insert, we move the queue back to the stack, add an item
# then pop the items back to the "queue stack"
# We only shuffle back on an insert, so if we have multiple pops from the
# queue they'll all be O(1)


# Complexity
# Time:
# O(N) for insertion since we need to move to the temporary stack
# O(1) for access
# Memory:
# O(N) since we have two stacks but they are only ever filled with N elements


# Potential improvements
# I can't think of any at this time


class myStack:
    """Stack implementation."""

    def __init__(self):
        self.stack = []

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack


class myQueue:
    """Queue using two stacks."""

    def __init__(self):

        self.stack = myStack()
        self.queue = myStack()


    def add(self, new_item):
        """Add an new_item to the end of the queue."""

        # move items from queue to stack
        while not self.queue.is_empty():
            self.stack.push(self.queue.pop())

        # add new_item to stack
        self.stack.push(new_item)

        # move items back to queue
        while not self.stack.is_empty():
            self.queue.push(self.stack.pop())


    def remove(self):
        """Remove the first item in the queue."""
        return self.queue.pop()


    def peek(self):
        """Return the top of the queue."""
        return self.queue.peek()


    def is_empty(self):
        """Return true if and only if the queue is empty."""
        return not self.queue



import unittest
import random

class TestMyQueue(unittest.TestCase):

    def setUp(self):

        self.queue = myQueue()
        self.input = [random.randint(-1000,1000) for _ in range(100)]
        self.input2 = [random.randint(-1000,1000) for _ in range(5)]


    def test_add_and_remove(self):

        for item in self.input:
            self.queue.add(item)

        self.assertEqual(self.input[0], self.queue.peek())

        popped = self.queue.remove()
        self.assertEqual(popped, self.input[0])
        self.assertEqual(self.input[1], self.queue.peek())


if __name__ == '__main__':
    unittest.main()



