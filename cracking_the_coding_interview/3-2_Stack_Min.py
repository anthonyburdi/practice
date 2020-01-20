# 3-2_Stack_Min.py

# Design a stack with push, pop and min (which returns min element) all in O(1) time.

# Assumptions:
# all elements are numerical
# num of elements fits in memory on a single machine

# Approach:
# store the min element as a class attribute and check on each insert
# also check on each removal
# if we remove the min element we will have to find the min element again
# which is O(N) time...
# So maybe we need another stack for the min elements? This would still
# take more than O(1) time to update as new items are inserted
# I can't think of a way to fix this without storing a sorted stack
# or finding the min each time we remove it... Even if it is stored in
# a min heap there is still more than O(1) time to re-heapify after we
# remove the min.

# Complexity
# O(1) for all operations, except if we remove the min element and have
# to find the next min element

# Potential improvements
# we could use a min heap to keep track of the minimum element instead
# insertion and removal are logarithmic, so when we remove the min element
# we don't have to iterate through to find the next min


class myStack:

    def __init__(self):

        self.stack = []
        self.min_element = None


    def push(self, new_element):
        self.stack.append(new_element)

        if not self.min_element:
            self.min_element = new_element
        elif new_element < self.min_element:
            self.min_element = new_element


    def pop(self):
        popped_element = self.stack.pop()
        if popped_element == self.min_element:
            self.min_element = min(self.stack)
        return popped_element


    def min(self):
        return self.min_element



import unittest

class TestMyStack(unittest.TestCase):

    def setUp(self):

        self.stack = myStack()

        self.elements = [1,6,3,9,4,6,12,54,773,32,-1,7,3,43,67,4,-5]

        for elem in self.elements:
            self.stack.push(elem)


    def test_mystack_min(self):
        self.assertEqual(self.stack.min(), -5)


    def test_mystack_new_min(self):
        popped = self.stack.pop()
        self.assertEqual(popped, -5)
        self.assertEqual(self.stack.min(), -1)
        popped2 = self.stack.pop()
        self.assertEqual(popped2, 4)
        self.assertEqual(self.stack.min(), -1)
        for num in reversed([773,32,-1,7,3,43,67]):
            popped = self.stack.pop()
            self.assertEqual(popped, num)

        self.assertEqual(self.stack.min(), 1)


if __name__ == '__main__':
    unittest.main()



