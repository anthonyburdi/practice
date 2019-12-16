# 36-isValidSudoku.py

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# A partially filled sudoku which is valid.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Example 1:

# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:

# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we create a sub function to check if a list of values
        # has any duplicates by counting each value using a hashmap
        # if any value is greater than 1 we return false
        # if we wanted to return where or which value we could as well
        # as check for more values but for this exercise we won't.
        # there also may be a smarter way to check rather than going through
        # all the different sections of the board, but I can't think of it
        # right now so let's just do that
        # maybe it's something like memoize if you've visited a cell already
        # but i'm not sure if that is super helpful. Maybe to disregard
        # unfilled cells?

        def check_for_duplicate_ints(section: List[str]) -> bool:
            """Check for duplicates in a list of integers."""
            counts = {}
            for item in section:
                # only count integers
                if not item == ".":
                    counts[item] = counts.get(item, 0) + 1

            for n in counts.values():
                if n > 1:
                    return True
            return False

        # check rows
        for row in board:
            # if there is a duplicate, then it's not valid sudoku so return False
            if check_for_duplicate_ints(row): return False

        # check columns
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])

            if check_for_duplicate_ints(col): return False

        # check squares
        boundaries = [(0,3), (3,6), (6,9)]
        for row_boundary in boundaries:
            for col_boundary in boundaries:

                square = []
                # column
                for i in range(col_boundary[0],col_boundary[1]):
                    # row
                    for row in board[row_boundary[0]:row_boundary[1]]:
                        square.append(row[i])

                if check_for_duplicate_ints(square): return False

        return True

if __name__ == '__main__':
    solution = Solution()

    ex_1 = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]

    print("Example 1 Should be True: ", solution.isValidSudoku(ex_1))

    ex_2 = [
                ["8","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]

    print("Example 2 Should be False: ", solution.isValidSudoku(ex_2))


    def check_for_duplicate_ints(section: List[str]) -> bool:
        """Check for duplicates in a list of integers."""
        counts = {}
        for item in section:
            # only count integers
            if type(item) == int:
                counts[item] = counts.get(item, 0) + 1

        for n in counts.values():
            if n > 1:
                return True
        return False

    print("should be false", check_for_duplicate_ints([1, 2, 3, 4, 5]))
    print("should be true", check_for_duplicate_ints([1, 2, 3, 4, 5, 5]))
