# 121-Best_Time_to_Buy_and_Sell_Stock_EASY.py

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Assumptions
        # prices only contains numeric data
        # prices is small enough to fit on one machine

        # Approach
        # iterate through prices from front and back
        # keep track of minimum value and maximum value seen
        # maximum from back and minimum from front
        # if our indices meet, break and report maximum (or 0 if negative)

        # Actually this won't work... if the price rise was on the second day
        # for example we would never see it....

        # Maybe we can just have two pointers? one after the other?
        # We update min_price on the following pointer
        # and max_price on the leading pointer

        # Won't work either

        # HMMMM......

        # Keep track of both indices?

        # OK I peeked
        # we keep track of the min price and the max profit
        # and update at each step





        # Complexity
        # Time: O(N) since we go through each element
        # Space: O(1) since we only add extra variables

        # Potential improvements
        # I can't think of any

        # WRONG
        # left = 0
        # right = len(prices) - 1

        # min_price = None
        # max_price = None

        # while left < right:
        #     if min_price is None or min_price > prices[left]:
        #         min_price = prices[left]
        #     if max_price is None or max_price < prices[right]:
        #         max_price = prices[right]

        #     left += 1
        #     right -= 1

        # if min_price > max_price:
        #     return 0
        # else:
        #     return max_price - min_price



        # WRONG
        # if len(prices) < 2:
        #     return 0

        # leader = 1
        # follower = 0

        # min_price = None
        # max_price = None

        # while leader < len(prices):
        #     if min_price is None or min_price > prices[follower]:
        #         min_price = prices[follower]

        #     if max_price is None or max_price < prices[leader]:
        #         max_price = prices[leader]

        #     leader += 1
        #     follower += 1

        # if min_price > max_price:
        #     return 0
        # else:
        #     return max_price - min_price

        min_price = None
        max_profit = 0

        for price in prices:
            if min_price is None or price < min_price:
                min_price = price

            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit





import unittest

class TestMaxProfit(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):

        prices = [7,1,5,3,6,4]
        output = 5
        self.assertEqual(self.solution.maxProfit(prices), output)


    def test_example_2(self):

        prices = [7,6,4,3,1]
        output = 0
        self.assertEqual(self.solution.maxProfit(prices), output)


    def test_example_3(self):
        prices = [1,7,5,3,6,4]
        output = 6
        self.assertEqual(self.solution.maxProfit(prices), output)


if __name__ == '__main__':
    unittest.main()




