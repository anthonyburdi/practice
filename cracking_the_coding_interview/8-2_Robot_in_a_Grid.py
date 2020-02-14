# 8-2_Robot_in_a_Grid.py


# This doesn't quite answer the question - they are asking for any path
# not all the paths & shortest.


from typing import List

def robot_paths(grid:List[List[int]]):
    """All possible paths for a robot that can go down and right."""

    def helper(
        grid:List[List[int]],
        all_paths:List[List[str]],
        row: int,
        col: int,
        curr_path: List[str],
        step: int
    ):

        # if we are at the end, return a good path
        if grid[row][col] == -1:
            curr_path = [i for i in curr_path if i is not None]
            all_paths.append(curr_path.copy())

        # otherwise go right and down

        else:
            # go down
            if row < (len(grid) - 1) and grid[row + 1][col] < 1:
                curr_path[step] = "D"
                helper(grid, all_paths, row + 1, col, curr_path, step + 1)
            # go right
            if col < (len(grid[0]) - 1) and grid[row][col + 1] < 1:
                curr_path[step] = "R"
                helper(grid, all_paths, row, col + 1, curr_path, step + 1)


    row = col = 0
    all_paths = []

    step = 0
    curr_path = [None] * ((len(grid) - 1) * (len(grid[0]) - 1))

    helper(grid, all_paths, row, col, curr_path, step)
    shortest_path = min([len(a) for a in all_paths])
    num_paths = len(all_paths)

    return {
        "all_paths": all_paths,
        "shortest_path": shortest_path,
        "num_paths": num_paths
    }




if __name__ == '__main__':

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, -1]
    ]

    print(robot_paths(grid))

    grid = [
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, -1],
    ]

    print(robot_paths(grid))



