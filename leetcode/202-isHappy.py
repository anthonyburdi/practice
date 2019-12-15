# 202-isHappy.py

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int, new_n_visited: set=None) -> bool:
        # First get the digits by using modulo
        # Then perform the squaring operation and return again
        # I'm not sure yet how to end if it is going on a long time
        # For now I'll add a counter I guess? I think it is kind of arbitrary.
        # Maybe something happens like the number keeps getting bigger rather than smaller
        # Let's test it out with a few numbers and see if there is a pattern

        new_n_visited = set() if not new_n_visited else new_n_visited

        verbose = False

        if verbose:
            print("n:", n)

        digits = []

        return_value = False

        # Base case
        if n == 1:
            # new_n_visited=set()
            return True

        n_digits = 1
        while n:
            # Get the digit starting from ones place (then tens, hundreds etc)
            digit = int((n % 10**n_digits) / 10**(n_digits - 1))

            # subtract from n
            n -= (n % 10**n_digits)

            digits.append(digit)
            n_digits += 1

        new_n = sum([d**2 for d in digits])

        if verbose:
            print("digits: ", digits)
            print("new_n:", new_n)
            print("new_n_visited:", new_n_visited)
            print("return_value:", return_value)

        if new_n in new_n_visited:
            if verbose:
                print("-------------------------new_n in new_n_visited------------------------------")
                print("new_n:", new_n)
                print("new_n_visited:", new_n_visited)
            return False
        else:
            new_n_visited.add(new_n)

            return_value = self.isHappy(new_n, new_n_visited)
            if return_value:
                # new_n_visited=set()
                return True
            else:
                # new_n_visited=set()
                return False


if __name__ == '__main__':
    solution = Solution()

    print("=========================>  25 (False): ", solution.isHappy(25))
    print("--------------------------------------------------------------------------------------------")
    print("=========================>  19 (True): ", solution.isHappy(19))
    print("--------------------------------------------------------------------------------------------")
    print("=========================>  7 (True): ", solution.isHappy(7))

