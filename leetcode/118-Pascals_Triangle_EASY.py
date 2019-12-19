# 118-Pascals_Triangle_EASY.py

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        return_list = []

        for current_row_idx in range(numRows):
            # row = [None for _ in range(current_row_idx + 1)] # generate an empty array
            row = [None] * (current_row_idx + 1) # generate an empty array
            row[0] = 1
            row[-1] = 1

            # for each of the columns (not including the first element or last)
            # calculate and add the corresponding element
            for j in range(1, len(row) - 1):
                row[j] = return_list[current_row_idx - 1][j - 1] + return_list[current_row_idx - 1][j]

            return_list.append(row)

        return return_list


if __name__ == '__main__':
    s = Solution()

    print(s.generate(5))

    # Output should be:
    # [
    #      [1],
    #     [1,1],
    #    [1,2,1],
    #   [1,3,3,1],
    #  [1,4,6,4,1]
    # ]
