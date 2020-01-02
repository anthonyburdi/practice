# 11 Container_With_Most_Water_MEDIUM.py

# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
# with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can
# contain is 49.


# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


# Assumptions:
# n is at least 2 per the problem statement
# height of the container is the height of the smaller line
# lines are non-negative

# Approach:
# Create subfunction to compute the area given two items from list, using
# the minimum item as the height and the distance between the items as the
# width.
# Brute force is to try each combination. I'm struggling to see any improvement
# to this because we cannot just look for the longest lines since shorter but
# further apart lines could hold more water.
# I'm thinking maybe we can discount some cases based on what we've already
# calculated. But we still need to hit each item combination.


# Complexity (Time & Space):
# Brute force is O(n^2) since we have to visit each combination.
# Space complexity is O(1) since we don't store any additional data besides
# a few variables.

# Potential improvements:
# I'm sure there is a better algorithm for this. Maybe we can discount
# any line that doesn't meet the height requirement for it's width.
# In other words, once we have a current maximum area, we calculate the
# minimum width at each location to beat it and then don't calculate the area
# at each location if it doesn't meet the standard. I don't think this
# saves much time though. Maybe only a constant amount since we still have
# to hit each item.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Compute the max rectangular area between two lines on the x axis."""

        max_area = 0

        for i in range(len(height)):
            for j in range(i, len(height)):

                area = self.calcArea(i, height[i], j, height[j])
                if area > max_area:
                    max_area = area


        return max_area



    def calcArea(self, id1: int, height1: int, id2: int, height2: int) -> int:
        """Calculate the area between a pair of lines & x axis."""

        return min(height1, height2) * abs(id2 - id1)



import unittest

class TestCalcArea(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):

        id1 = 1
        id2 = 8
        height1 = 8
        height2 = 7
        self.assertEqual(
            self.solution.calcArea(id1, height1, id2, height2),
            49
        )


class TestMaxArea(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):

        input_arr = [1,8,6,2,5,4,8,3,7]
        output = 49

        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )


    def test_large_array_1(self):
        input_arr = [
            7, 77, 68, 38, 100, 9, 64, 75, 38, 28, 62, 56, 57, 27,
            17, 23, 46, 55, 41, 35, 95, 22, 46, 56, 4, 21, 9, 45, 80, 42
        ]
        output = 2079
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )

    def test_large_array_2(self):
        input_arr = [
            10, 67, 42, 7, 5, 99, 29, 6, 8, 84, 27, 27, 50, 65, 72, 86, 45, 28,
            35, 99, 13, 36, 75, 40, 89, 85, 89, 87, 97, 11, 1, 30, 73, 8, 28,
            93, 61, 4, 87, 85, 45, 12, 78, 28, 10, 100, 26, 89, 72, 35, 55, 65,
            37, 78, 67, 68, 25, 8, 98, 24, 67, 30, 97, 76, 34, 83, 75, 15, 76,
            39, 68, 33, 3, 57, 87, 26, 21, 15, 70, 76, 5, 41, 69, 5, 38, 72, 75,
            66, 97, 67, 67, 96, 52, 49, 43, 53, 28, 48, 11, 97
        ]
        output = 9118
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )


    def test_large_array_3(self):
        import random
        random.seed(64)
        input_arr = [random.randint(1,1000) for i in range(5000)]
        output = 4932116
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )


    def test_edge_cases(self):

        input_arr = [1,1,1,1,1]
        output = 4
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )

        input_arr = [1,1]
        output = 1
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )

        input_arr = [0,1]
        output = 0
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )
        input_arr = [0,0]
        output = 0
        self.assertEqual(
            self.solution.maxArea(input_arr),
            output
        )



if __name__ == '__main__':
    unittest.main()
