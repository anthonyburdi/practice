# 200-Number_of_Islands_MEDIUM.py

# https://leetcode.com/problems/number-of-islands/

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Num islands in rectangular grid where 0 = water and 1 = land."""

        if grid is None or grid == [[]]: return 0

        visited = set()
        tot_num_islands = 0

        def helper(grid: List[List[str]], row: int, col: int, visited: set) -> set:

            visited.add((row, col))
            if grid[row][col] == "0":
                return visited
            else:
                # visit neighbors if we haven't already
                # left
                if col - 1 >= 0 and (row, col - 1) not in visited:
                    visited = helper(grid, row, col - 1, visited)

                # right
                if col + 1 < len(grid[0]) and (row, col + 1) not in visited:
                    visited = helper(grid, row, col + 1, visited)

                # up
                if row - 1 >= 0 and (row - 1, col) not in visited:
                    visited = helper(grid, row - 1, col, visited)

                # down
                if row + 1 < len(grid) and (row + 1, col) not in visited:
                    visited = helper(grid, row + 1, col, visited)

            return visited


        # loop through all points
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    # if water skip
                    if grid[row][col] == "0":
                        visited.add((row, col))

                    # if land visit all neighboring land
                    elif grid[row][col] == "1":
                        visited = helper(grid, row, col, visited)
                        tot_num_islands += 1

                    else:
                        return -1 # if input is erroneous

        return tot_num_islands





