# 69-Sqrt(x)_EASY.py

# https://leetcode.com/problems/sqrtx/

# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

# Assumptions:
# non negative integer input
# return truncated integer
# can be very large integer but fits in memory on single computer
# sqrt of 0 is 0

# Approach:
# we can always just use math.sqrt() and truncate the result... but not here
# hmm - brute force is to start with 1 and iterate until the square of the
# number is more than x and take the previous.

# I'm not sure how this relates to binary search.
# Ah - I can do a binary search for the number from all integers from
# 0 to the number. Just using a different comparison for the binary search.


# Complexity (time and space):
# Brute force
# O(N) time complexity but much less than N... we are just checking up to the
# sqrt of N.
# O(1) space complexity since we only store a few variables.
# binary search:
# O(log N), much faster
# O(1) since we are not storing anything other than pointers

# Possible improvements:
# No ideas at this time.
# maybe start with a guess closer to the order of the number?
# or jump more if further away?
# jump back if we went past it and double check?
# Ok - do a binary search and keep checking if the square is bigger or
# smaller than the value before moving the search space.



class Solution:
    def mySqrt(self, x: int) -> int:

        # Brute force for less than 17
        if x < 17:
            current_guess = 0

            while current_guess ** 2 <= x:
                current_guess += 1

            return current_guess - 1

        # Binary search if greater than 17:
        if x >= 17:
            # since we are skipping up to sqrt 3 we can divide the search
            # space into the first third already, might help a bit
            right = x // 2
            left = 4

            # then we check if the square of mid is less than x, then
            # move the left and right if so. If the square of mid == x
            # then return mid

            while right > (left + 1):

                mid = left + (right - left) // 2
                mid_square = mid ** 2

                if mid_square == x:
                    return mid
                elif mid_square > x:
                    right = mid
                elif mid_square < x:
                    left = mid

            # if we don't hit the number exactly, then return mid after we
            # exit the loop (after right == left == mid)

            # also if we are still on the high side, return mid - 1
            if mid_square > x:
                return mid - 1
            else:
                return mid


    def mySqrtBruteForce(self, x: int) -> int:

        current_guess = 0

        while current_guess ** 2 <= x:
            current_guess += 1

        return current_guess - 1



# Example 1:

# Input: 4
# Output: 2
# current_guess = 0
# current_guess ** 2 = 0 <= 4
# current_guess += 1 = 1
# current_guess ** 2 = 1 <= 4
# current_guess += 1 = 2
# current_guess ** 2 = 4 <= 4
# current_guess += 1 = 3
# current_guess ** 2 = 9 !<= 4
# return current_guess(3) - 1 = 2
# Correct

# Example 2:

# Input: 8
# Output: 2
# current_guess = 0
# current_guess ** 2 = 0 <= 8
# current_guess += 1 = 1
# current_guess ** 2 = 1 <= 8
# current_guess += 1 = 2
# current_guess ** 2 = 4 <= 8
# current_guess += 1 = 3
# current_guess ** 2 = 9 !<= 8
# return current_guess(3) - 1 = 2
# Correct


import unittest

class TestMySqrt(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        i = 4
        o = 2
        self.assertEqual(self.solution.mySqrt(i), o)

    def test_example_2(self):
        i = 8
        o = 2
        self.assertEqual(self.solution.mySqrt(i), o)

    def test_17(self):
        i = 17
        o = 4
        self.assertEqual(self.solution.mySqrt(i), o)

    def test_integers_to_100000(self):

        for i in range(100001):
            import math
            o = int(math.sqrt(i))
            self.assertEqual(self.solution.mySqrt(i), o)

    def test_large_input_leetcode(self):
        i = 1960677540
        o = 44279

        def wrapper(func, *args, **kwargs):
            def wrapped():
                return func(*args, **kwargs)
            return wrapped

        wrapped_brute_force = wrapper(self.solution.mySqrtBruteForce, i)
        import timeit
        print(
            "===== mySqrtBruteForce time for {}:".format(i),
            timeit.timeit(wrapped_brute_force, number=100)
        )

        wrapped_binary_search = wrapper(self.solution.mySqrt, i)
        import timeit
        print(
            "===== mySqrt time for {}:".format(i),
            timeit.timeit(wrapped_binary_search, number=100)
        )

        self.assertEqual(self.solution.mySqrt(i), o)




if __name__ == '__main__':
    unittest.main()












