# 70-Climbing_Stairs_EASY.py

# https://leetcode.com/problems/climbing-stairs/

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Assumptions:
# n fits on a single computer
# recursive solution ok - will not cause stack overflow

# Approach:
# Each time you add the number of steps before: e.g. for n = 3 it is the
# number of ways to climb n = 1 and n = 2
# for n = 1 there is 1 way to climb (1 step)
# for n = 2 there are two ways to climb (1 step + 1 step or 2 steps)
# for n = 4 it is the number of ways to climb n = 1, 2, 3
# for n = 3 there are 3 ways to climb:
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# so for n = 4 there are 6 ways to climb (1 for 1, 2 for 2, 3 for 3 = 6 for 4)
# THIS IS NOT TRUE. For n = 4 there are only 5 ways
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 2 + 1
# 4. 2 + 1 + 1
# 5. 2 + 2
# for n = 5 there are 8 ways
# 1. 1 + 1 + 1 + 1 + 1
# 2. 1 + 1 + 1 + 2
# 3. 1 + 1 + 2 + 1
# 4. 1 + 2 + 1 + 1
# 5. 2 + 1 + 1 + 1
# 6. 1 + 2 + 2
# 7. 2 + 1 + 2
# 8. 2 + 2 + 1

# Hint # 1: To reach nth step, what could have been your previous steps?
# (Think about the step sizes)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89

# OK well duh - it is not all the previous step configurations, just the
# last two.

# Time and space complexity:
# Time complexity is O(N) since we memoize the inputs, we only call them once
# thus for each N we only do lookups (constant O(1)) after the initial call
# Space complexity O(N) since we store each call on the stack

class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def climbStairsRecursive(n: int, cache: dict) -> int:

            if cache.get(n):
                return cache[n]

            elif n < 4:
                return n

            else:

                cache[n] = climbStairsRecursive(n - 1, cache) + climbStairsRecursive(n - 2, cache)
                return cache[n]

        return climbStairsRecursive(n, cache)


import unittest

class TestClimbStairs(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.climbStairs(2), 2)


    def test_example_2(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_1_to_10(self):

        input_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        output = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

        for i in range(len(input_n)):
            self.assertEqual(self.solution.climbStairs(input_n[i]), output[i])


if __name__ == '__main__':
    unittest.main()

