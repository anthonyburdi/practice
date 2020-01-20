# 9-Palindrome_Number_EASY.py

# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Assumptions:
        # Given an integer
        # Negative numbers are not palindromes
        # 0 is a palindrome as is any single digit
        # given integer doesn't overflow

        # Approach:
        # First check all easy cases (negative, single digits)
        # for others
        # Start with first digit and last digit, check for equivalency
        # to get the digits by themselves do a mod 10 and then
        # integer divide by 10 to get rid of it and append the digit
        # to an array. Doesn't matter that the digits are backwards as
        # we will then check whether it is a palindrome by moving a pointer
        # from the front to the back and back to the front checking each
        # digit for equivalency.

        # Complexity:
        # Time: O(N) since we hit each digit in the number
        # Space: O(N) since we create a new array

        # Potential improvements
        # we could do this in O(1) space if we get the digits from the
        # number front and back at the same time. I'm not sure how to know
        # what power of 10 to start with though. We could go to the max
        # allowable for python and then work backwards but that seems
        # like not a great solution. Python3 int is unbounded...
        # https://stackoverflow.com/a/7604981
        # I can't think of a way to do this but this would be an improvement
        # if possible.

        # Edge cases
        # negative integers
        # single digits
        # non-integer


        # 1. Handle edge cases
        if (type(x) is not int) or x < 0:
            return False
        if x < 10:
            return True

        # 2. Convert integer to array of digits (non string)
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10

        # 3. Check whether the array is a palindrome & return

        left = 0
        right = len(digits) - 1

        while left < right:
            if digits[left] is not digits[right]:
                return False
            left += 1
            right -= 1

        return True




import unittest

class TestIsPalindrome(unittest.TestCase):


    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):
        self.assertTrue(self.solution.isPalindrome(121))


    def test_example_2(self):
        self.assertFalse(self.solution.isPalindrome(-121))


    def test_example_3(self):
        self.assertFalse(self.solution.isPalindrome(10))


    def test_single_digits(self):
        for i in range(10):
            self.assertTrue(self.solution.isPalindrome(i))


    def test_non_integer(self):
        self.assertFalse(self.solution.isPalindrome("121"))
        self.assertFalse(self.solution.isPalindrome("hello"))
        self.assertFalse(self.solution.isPalindrome(121.0))


if __name__ == '__main__':
    unittest.main()





