# 605-Can_Place_Flowers_EASY.py

# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots -
# they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

from typing import List
import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Approach:
        # given the assumptions that the input array doesn't violate the rule
        # I think we can just sum up the input array
        # and make sure that there is enough space for n flowers
        # The max amount of flowers
        # Time Complexity:
        # O(N) to create the sum, all other operations are constant O(1)
        # incl len() for python because python stores len in the object header
        # https://effbot.org/zone/python-list.htm#performance
        # Space Complexity:
        # O(1) for extra space bc we just add a few integers, not dependent on N
        # Possible Improvements:
        # I don't see any way to improve this, I think you always have to
        # look at the flowerbed so at min it is O(N)

        # Facepalm! Of course this won't work if the flowers are arranged
        # poorly, e.g. [0,1,0] has no room even though there are two spots
        # so current_flowers = 1 and max_flowers = 2

        # import math # imported here for leetcode

        # current_flowers = sum(flowerbed)

        # max_flowers = math.ceil(len(flowerbed) / 2)

        # return max_flowers >= (current_flowers + n)

        # NEW Approach, Time & Space Complexity & Possible Improvements:
        # Approach:
        # Loop through and count occurrences of 3 0's in a row
        # Complexity:
        # O(N) time to loop through and O(1) constant extra space
        # Possible Improvements:
        # I can't think of any

        # return if too small:
        # This can definitely be simplified!!
        if not flowerbed:
            return False
        if n == 0:
            return True


        elif flowerbed == [0]:
            if n == 1:
                return True
            else:
                return False
        elif flowerbed == [1]:
            return False
        elif len(flowerbed) == 2:
            if sum(flowerbed) > 0:
                return False
            elif sum(flowerbed) == 0 and n == 1:
                return True
            else:
                return False

        num_spaces = 0

        # if first two items are 0 add one in first slot
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            num_spaces += 1

            # return early if we have enough room for n flowers
            if num_spaces >= n:
                return True

            # add a flower in first slot so we don't double count
            flowerbed[0] = 1

        # iterate through all but last item in flowerbed
        for idx, num in enumerate(flowerbed[:-1]):
            # skip the first item
            if idx > 0:
                # if both neighbors and current are 0 then add one
                if sum([flowerbed[idx - 1], num, flowerbed[idx + 1]]) == 0:

                    # Insert a flower here so we don't double count
                    flowerbed[idx] = 1

                    num_spaces += 1

                    # return early if we have enough room for n flowers
                    if num_spaces >= n:
                        return True

        # Is this necessary?
        # add one if the last two items are 0
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            num_spaces += 1

        return num_spaces >= n




import unittest

class TestCanPlaceFlowers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        flowerbed = [1,0,0,0,1]
        n = 1
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_2(self):
        flowerbed = [1,0,0,0,1]
        n = 2
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_3(self):
        flowerbed = [1,0,0,1]
        n = 1
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_4(self):
        flowerbed = [1,0,0,0,0,0,1]
        n = 2
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_5(self):
        flowerbed = [1,0,0,0,0,1]
        n = 2
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_6(self):
        flowerbed = [1]
        n = 1
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_7(self):
        flowerbed = []
        n = 1
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_8(self):
        flowerbed = [1,0,0,0,1]
        n = 89
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_example_9(self):
        flowerbed = [0,1,0]
        n = 1
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_small_flowerbed_1(self):
        flowerbed = [0,1]
        n = 1
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_small_flowerbed_2(self):
        flowerbed = [0,0]
        n = 1
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_small_flowerbed_3(self):
        flowerbed = [0,1]
        n = 0
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_zeroes_at_end_1(self):
        flowerbed = [0,1,0,0]
        n = 1
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_zeroes_at_end_2(self):
        flowerbed = [0,1,0,0,0]
        n = 1
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_zeroes_at_end_2(self):
        flowerbed = [0,1,0,0,0]
        n = 2
        output = False
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_zeroes_at_end_3(self):
        flowerbed = [0,0,0]
        n = 1
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

    def test_ones_at_end_1(self):
        flowerbed = [0,0,0]
        n = 2
        output = True
        self.assertEqual(
            self.solution.canPlaceFlowers(flowerbed, n),
            output
        )

if __name__ == '__main__':
    unittest.main()