# 7-Reverse_Integer_EASY.py

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        # we could do this by turning the integer into a list of digits in array then reversing
        # let's do this with only integers instead of turning into a list
        # comments in parens are for example -123

        given_int = x
        n = abs(x) # peel off the negative sign then add back later
        new_int = 0
        f = 1

        # create a loop that keeps removing a digit from the int and then adding to new int
        # do this by doing modulo 10 to get digit, then subtracting and dividing by 10
        # then multiplying by 10 of new int and adding new digit


        while n:
            digit = n % 10 # get the next ones digit (example digit = 3, digit = 2, digit = 1)
            n -= digit # remove digit from n (example n = 120, n = 10, n = 0)
            n = n // 10 # remove digit from n (example n = 12, n = 1, n = 0)
            # new_int *= f # shift new_int over so we can add new digit (example new_int = 0, new_int = 30, new_int = 320)
            new_int *= 10
            new_int += digit # add digit to new int (example new_int = 3, new_int = 32, new_int = 321)
            f = 10 # change f back to 10 after first round through loop at 1

        # add the negative sign back if the original number was negative
        if given_int < 0:
            new_int = -new_int

        # first check if overflows before returning
        if new_int < -2**31:
            return 0
        if new_int > (2**31 - 1):
            return 0

        # otherwise return new_int
        return new_int

        # Q: can f just be replaced with 10? I think so. Seems to work.
        # what is the complexity here? I guess O(N) where N is the number of digits of the integer to swap

if __name__ == '__main__':
    solution = Solution()

    examples = {
        "Example 1": [123, 321],
        "Example 2": [-123, -321],
        "Example 3": [120, 21],
        "Example 4": [0, 0],
        "Example 5": [-0, 0],
        "Example 6": [-1234541651321, 0],
        "Example 7": [1234541651321, 0],
        "Example 8": [1534236469, 0],
        "Example 9": [15342, 24351]
    }

    for name, data in examples.items():
        print(
            "{name} (given {given} result should be {desired_result}): {result}".format(
                name=name,
                given=data[0],
                desired_result=data[1],
                result=solution.reverse(data[0])
            )
        )

