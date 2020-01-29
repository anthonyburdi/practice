# ACODE_Alphacode.py

# https://www.spoj.com/problems/ACODE/

# Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:

# Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

# Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”
# Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”
# Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”
# Alice: “How many different decodings?”
# Bob: “Jillions!”

# For some reason, Alice is still unconvinced by Bob’s argument, so she requires a program that will determine how many decodings there can be for a given string using her code.

# Input
# Input will consist of multiple input sets. Each set will consist of a single line of at most 5000 digits representing a valid encryption (for example, no line will begin with a 0). There will be no spaces between the digits. An input line of ‘0’ will terminate the input and should not be processed.

# Output
# For each input set, output the number of possible decodings for the input string. All answers will be within the range of a 64 bit signed integer.

# Example
# Input:

# 25114
# 1111111111
# 3333333333
# 0

# Output:

# 6
# 89
# 1

# Assumptions
# Digits are all integers between 1-26 inclusive
# len(digits) <= 5000
# we can convert the string of digits to a char array

# Approach, Complexity, Tradeoffs, Potential Improvements
# for each digit if it is <= 2 then it could be part of a double digit num
# so then check the next digit - if it is also <= 6 then create two
# candidates. One is prefix + letter[curr_digit] and the other is prefix +
# letter[curr_digit * 10 + next_digit].
# make these the new prefixes and then proceed to the rest of the input

# Cache the result of the next call. E.g. call on the array without the one or
# two digits being considered. If we have already called on that array then
# just return the value.

# Time complexity O(n) linear since we eliminate duplicate recursive calls
# Space complexity O(n) since we store both the char array of the string and
# the memoization table.

# ****************************
# I'm not sure how to use a memoization table here.
# There seems to be a lot of duplicated work.
# maybe if we start at the back of the array and work left?
# ****************************

# If we get to the end of the char array then add one to the list of decodings.

# Edge Cases
# No digits, single digit, two digits

from typing import List

def count_decodings(s: str) -> int:
    """Count the number of decodings of alpha code given string of digits.

    >>> count_decodings("25114")
    6
    >>> count_decodings("1111111111")
    89
    >>> count_decodings("3333333333")
    1
    >>> count_decodings("33")
    1
    """
    # Stack depth exceeded
    # >>> count_decodings("25114"*1000)
    # 100

    # RECURSIVE FROM FRONT
    total_decodings = 0
    chars = [int(char) for char in s]

    def helper(chars: List[int]) -> None:
        """Recursive helper function."""

        # Base Case
        if len(chars) == 0:
            nonlocal total_decodings
            total_decodings += 1
            return

        # Work
        if len(chars) >= 2 and chars[0] <= 2 and chars[1] <= 6:
            # create two options single and two char
            # single
            helper(chars[1:])
            # two char
            helper(chars[2:])

        else:
            # single char
            helper(chars[1:])

    helper(chars)

    return total_decodings



    # RECURSIVE MEMOIZED
    # memo = {}
    # chars = [int(char) for char in s]

    # def helper(chars: List[int]) -> int:
    #     """Recursive helper function."""

    #     nonlocal memo

    #     if tuple(chars) in memo:
    #         return memo[tuple(chars)]

    #     # Base Case
    #     if len(chars) == 0:
    #         # nonlocal total_decodings
    #         # total_decodings += 1
    #         return

    #     # Work
    #     if len(chars) >= 2 and chars[0] <= 2 and chars[1] <= 6:
    #         # create two options single and two char
    #         # single
    #         memo[tuple(chars)] = 2
    #         helper(chars[1:])
    #         # two char
    #         helper(chars[2:])

    #     else:
    #         # single char
    #         memo[tuple(chars)] = 1
    #         helper(chars[1:])

    # helper(chars)

    # total_decodings = sum(memo.values())

    # return total_decodings



if __name__ == '__main__':
    import doctest
    doctest.testmod()










