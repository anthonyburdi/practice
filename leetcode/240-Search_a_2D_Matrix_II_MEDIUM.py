# 240-Search_a_2D_Matrix_II_MEDIUM.py

# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.

from typing import List

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Assumptions
        # Integers could be negative as well
        # matrix fits on a single machine
        # matrix is small enough we don't hit stack depth

        # Approach, Complexity, Tradeoffs, Potential Improvements
        # for input matrix, find the midpoint of row and column
        # check the midpoint and return True if that is the target
        # Otherwise check the other 4 quadrants
        # However we can eliminate one quadrant by comparing the midpoint to
        # the target since the rows and columns are sorted
        # If the target is less than the midpoint then we eliminate from the
        # midpoint to the right and down
        # If the target is greater than the midpoint then we eliminate from
        # the midpoint to the left and up
        # This solution is something like O(log(m * n)) since we are reducing the
        # solution space by 75% each time. Need to calculate this better
        # Space is O(1) since we are doing this in place.
        # Ok first we are doing it by slicing so that creates copies
        # so we are doing it in O(m * n) space

        # There is another solution where we iterate along the midcolumn
        # until we hit the value that exceeds the target. Then we take the
        # bottom left and top right zones and search there. This solution
        # is more like O(log(m * n)) since we are halving the search space each
        # time.

        # Edge Cases
        # Target doesn't exist
        # matrix is single item
        # matrix is empty
        # m or n = 1

        def getSubmatrix(matrix: List[List[int]], row: int, col: int) -> dict:
            """Clockwise submatrices given row and col of split point."""

            top_left = []
            top_right = []
            bot_right = []
            bot_left = []
            for r in range(len(matrix)):
                if r < row:
                    top_left.append(matrix[r][:col])
                    top_right.append(matrix[r][col:])
                else:
                    bot_left.append(matrix[r][:col])
                    bot_right.append(matrix[r][col:])

            return {
                "top_left": top_left,
                "top_right": top_right,
                "bot_right": bot_right,
                "bot_left": bot_left
            }


        def helper(matrix, target):

            # Base case
            if len(matrix) == 0:
                return False
            elif len(matrix[0]) == 0:
                return False

            mid_row = len(matrix) // 2
            mid_col = len(matrix[0]) // 2

            mid_val = matrix[mid_row][mid_col]

            # Base case
            if mid_val == target:
                return True
            if mid_row == mid_col == 0:
                return False

            # figure out which quadrant to ignore
            # call helper on the other 3 quadrants
            quadrants = getSubmatrix(matrix, mid_row, mid_col)

            top_left = quadrants["top_left"]
            top_right = quadrants["top_right"]
            bot_right = quadrants["bot_right"]
            bot_left = quadrants["bot_left"]

            if mid_val < target:
                # ignore top left quadrant
                return (
                    helper(top_right, target) or
                    helper(bot_left, target) or
                    helper(bot_right, target)
                )

            else:
                # ignore bottom right quadrant
                return (
                    helper(top_left, target) or
                    helper(top_right, target) or
                    helper(bot_left, target)
                )

        return helper(matrix, target)



import unittest

class TestSearchMatrix(unittest.TestCase):


    def setUp(self):

        self.solution = Solution()


    def test_given_examples(self):

        matrix = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]

        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 20))

        # Others
        self.assertTrue(self.solution.searchMatrix(matrix, 9))
        self.assertTrue(self.solution.searchMatrix(matrix, 24))
        self.assertTrue(self.solution.searchMatrix(matrix, 21))
        self.assertFalse(self.solution.searchMatrix(matrix, 97))
        self.assertFalse(self.solution.searchMatrix(matrix, 120))
        self.assertFalse(self.solution.searchMatrix(matrix, 25))


    def test_negatives(self):

        matrix = [
            [-15,   -11,  -7, -4, -1],
            [-19,   -12,  -8, -5, -2],
            [-22,   -16,  -9, -6, -3]
        ]

        self.assertTrue(self.solution.searchMatrix(matrix, -5))
        self.assertFalse(self.solution.searchMatrix(matrix, -20))
        self.assertFalse(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 20))

        matrix = [
            [-15,   -11,  -7],
            [-19,   -12,  -8],
            [-22,   -16,  -9]
        ]

        self.assertTrue(self.solution.searchMatrix(matrix, -19))
        self.assertTrue(self.solution.searchMatrix(matrix, -11))
        self.assertTrue(self.solution.searchMatrix(matrix, -15))
        self.assertTrue(self.solution.searchMatrix(matrix, -9))
        self.assertFalse(self.solution.searchMatrix(matrix, -20))
        self.assertFalse(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 20))


    def test_small_and_empty(self):
        matrices = [[[]], [[1]], [[0]], [[-1]]]
        targets = [1, 0, -1]

        for matrix in matrices:
            for target in targets:
                if matrix == [[]] or target != matrix[0][0]:
                    self.assertFalse(self.solution.searchMatrix(matrix, target))
                else:
                    self.assertTrue(self.solution.searchMatrix(matrix, target))

        matrix = [[-1]]
        target = -1
        self.assertTrue(self.solution.searchMatrix(matrix, target))



if __name__ == '__main__':
    unittest.main()
