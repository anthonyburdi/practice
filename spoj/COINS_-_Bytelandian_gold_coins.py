# COINS_-_Bytelandian_gold_coins.py

# https://www.spoj.com/problems/COINS/

# In Byteland they have a very strange monetary system.

# Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all rounded down (the banks have to make a profit).

# You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.

# You have one gold coin. What is the maximum amount of American dollars you can get for it?

# Input
# The input will contain several test cases (not more than 10). Each testcase is a single line with a number n, 0 <= n <= 1 000 000 000. It is the number written on your coin.

# Output
# For each test case output a single line, containing the maximum amount of American dollars you can make.

# Example
# Input:
# 12
# 2

# Output:
# 13
# 2
# You can change 12 into 6, 4 and 3, and then change these into $6+$4+$3 = $13. If you try changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get no more than $1 out of them. It is better just to change the 2 coin directly into $2.


# Assumptions
# n is positive int
# bank rounds down n/2, n/3 and n/4

# Approach, Complexity, Tradeoffs
# 1. brute force try all combinations. O(3^n) exponential since for each coin
# we can separate into 3 other coins and then do the same
# 2. the same but we memoize the calculations so if we have calculated the
# max for a specific number we just return that. O(N) time and O(N) space for
# memo table

# Base cases
# n(0) = 0, n(1) = 1, n(2) = 2, n(3) = 3, n(4) = 2 + 1 + 1 = 4
# n(5) = 2 + 1 + 1 XXX = 5, n(6) = 3 + 2 + 1 = 6...
# n(12) = 6, 4, 3 = 13 # n(20) = 10 + 6 + 5 = 21 or n(10) + n(6) + n(5)
# where n(10) = 5 + 3 + 2 = 10 so n(20) = 21
# n(50) = 25 + 16 + 12 = 53 or n(25) + n(16) + n(12)
# n(25) = 12 + 8 + 6 or n(12) + n(8) + n(6)
# n(8) = 4 + 2 + 2 = 8
# so n(25) max = n(12) + n(8) + n(6) = 13 + 8 + 6 = 27 > 25
# n(16) = n(8) + n(5) + n(4) = 8 + 5 + 4 = 17 > 16
# so n(50) max = n(25) + n(16) + n(12) = 27 + 17 + 13 = 57

# so our return is something like:
# return max(lookup[n], f(n//2) + f(n//3) + f(n//4))

# Edge cases n < 0, n >> 1

def max_usd(n: int) -> int:
    """For one gold coin of denomination n, how many usd can you get."""
    # convert coins each for n/2, n/3 and n/4 coins (each rounded down).

    # some base cases and initialization
    memo = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    def helper(n: int, memo: dict) -> int:
        """Recursive helper function which takes a memoization table."""

        if memo.get(n) is not None:
            return memo[n]

        else:
            memo[n] = max(
                n,
                helper(n//2,  memo) + helper(n//3, memo) + helper(n//4, memo)
            )

        return memo[n]

    return helper(n, memo)


import unittest

class TestMaxUSD(unittest.TestCase):

    def test_given_examples(self):
        self.assertEqual(max_usd(2), 2)
        self.assertEqual(max_usd(12), 13)


    def test_other_examples(self):
        self.assertEqual(max_usd(6), 6)
        self.assertEqual(max_usd(20), 21)
        self.assertEqual(max_usd(50), 57)

        self.assertEqual(max_usd(1000), 1370)


if __name__ == "__main__":
    unittest.main()






