# 50-Pow_x_n_MEDIUM.py

# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

# Assumption:
# n small enough that we can calculate this on a single machine in under 1min
# output fits in a standard integer (this may not be true)
# we can't use built in functions
# we want to use recursion since this was mentioned in the recursion chapter
# round to the nearest 5th decimal digit

# Approach:
# first let's use the naive approach of just calling the operator
# x ** n
# For a recursive approach we can create a helper function and then just
# multiply x by itself until the helper function has been called n times
# if n is negative, then divide by itself until the function has been called
# n times
# for a binary search approach - I have no idea

# Complexity:
# Recursive Time complexity O(N) since we have to do an operation
# (multiplication or division) for each n
# Recursive space complexity O(N) since we have to make a recursive call
# for each n

# Possible improvements
# iterative? Just multiply (or divide) for each n. Then no stack overhead
# also O(N)


class Solution:
    def myPow(self, x: float, n: int) -> float:

        method = 'recursive'

        if n == 0 or round(x, 5) == 1.00000:
            return 1.0

        if method == 'naive':
            return round(x ** n, 5)

        if method == 'recursive':
            # Exceeds maximum recursion depth:
            # def pow_recursive(x, n):

            #     if n == 0:
            #         return 1.0
            #     if n > 0:
            #         return x * pow_recursive(x, n - 1)
            #     if n < 0:
            #         return x / pow_recursive(x, n + 1)

            # if n > 0:
            #     return round(pow_recursive(x, n), 5)
            # else:
            #     return round(1 / pow_recursive(x, -n), 5)

            def power(x, n):
                if n == 0:
                    return 1.0
                half = power(x, n//2)
                if n % 2 == 0:
                    return half * half
                else:
                    return half * half * x

            if n < 0:
                return round(1 / power(x, -n), 5)
            else:
                return round(power(x, n), 5)

        if method == 'iterative':
            # Max time limit exceeded
            return_value = x
            if n > 0:
                for i in range(1, n):
                    return_value *= x
                    if round(return_value, 5) == 0.00000:
                        return 0.00000

            if n < 0:
                for i in range(1, -n + 2):
                    return_value /= x
                    if round(return_value, 5) == 0.00000:
                        return 0.00000

            return round(return_value, 5)


import unittest

class TestMyPow(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        x = 2.00000
        n = 10
        output = 1024.00000

        self.assertEqual(self.solution.myPow(x, n), output)

    def test_example_2(self):
        x = 2.10000
        n = 3
        output = 9.26100

        self.assertEqual(self.solution.myPow(x, n), output)

    def test_example_3(self):
        x = 2.00000
        n = -2
        output = 0.25000

        self.assertEqual(self.solution.myPow(x, n), output)

    def test_small_x_large_n(self):
        x = 0.00001
        n = 2147483647
        output = 0.00000

        self.assertEqual(self.solution.myPow(x, n), output)

    def test_x_1(self):
        x = 1.00000
        n = 2147483647
        output = 1.00000

        self.assertEqual(self.solution.myPow(x, n), output)


if __name__ == '__main__':
    unittest.main()

