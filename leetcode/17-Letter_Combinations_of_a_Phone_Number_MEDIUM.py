# 17-Letter_Combinations_of_a_Phone_Number_MEDIUM.py

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.

# Assumptions:

# output = [] if input is ""
# Only digits 2-9
# Small enough to fit in memory - e.g. phone numbers ~10 digits
# duplicates can be included
# Output is the set of combinations, e.g. no duplicate combinations in output
# I don't think there can be anyway.

# Approach:
# Iterative
# Brute force each first digit with each second digit and so on.
# E.g. two for loops - one going through each digit, then one through each
# possible letter for that digit

# There is a recursive solution to this which I don't think will be fine given
# the length of the input (phone number, of order 10 digits).
# Hmm - maybe this can't fit on a recursion stack... it's going to be
# O(3^N) for the output which is 59,049 for N=10
# Python's recursion depth is 1000 by default
# import sys; sys.getrecursionlimit()
# although 59049 is not the recursion depth... the recursion depth might be N


# Time and Space Complexity:
# The recursive solution is O(3^N) since we have to calculate each combination
# given 3 choices

# Potential Improvements:
# memoization? Potentially we can compute some combinations once and then
# not have to re-compute them. I'm not sure this will help since we have
# to go through all combinations.


class Solution:

    def __init__(self):
        self.answer = []

    def letterCombinations(self, digits: str) -> List[str]:

        # Recursive
        output = []
        if digits == "":
            return output

        conversion = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # recursive helper function
        subset = [None] * len(digits)

        def helper(digits, subset, i):
            if i == len(subset):
                self.answer.append("".join(subset))
            else:
                for letter in conversion[digits[i]]:
                    subset[i] = letter
                    helper(digits, subset, i + 1)
                    # subset[i] = None

        helper(digits, subset, 0)

        return self.answer





