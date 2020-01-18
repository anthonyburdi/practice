# 374-Guess_Number_Higher_or_Lower_EASY.py

# https://leetcode.com/problems/guess-number-higher-or-lower/

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example :

# Input: n = 10, pick = 6
# Output: 6

# Assumptions:
# n is only non-negative integers
# n is small

# Approach:
# start the search space of integers from 0 to n
# call guess result on the midpoint, and move the search space based on whether
# the midpoint is greater or less than the picked number

# Complexity:
# Time: O(log n) because each guess removes half the search space
# Space: O(1) since we only store a few pointers

# Potential improvements:
# I can't think of any

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 0
        right = n

        while True:
            mid = left + (right - left) // 2
            guess_result = guess(mid)

            if guess_result == 0:
                return mid
            elif guess_result < 0:
                right = mid - 1
            elif guess_result > 0:
                left = mid + 1

