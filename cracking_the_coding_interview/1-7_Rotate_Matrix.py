# 1-7_Rotate_Matrix.py


from typing import List

def rotate(arr:List[List[int]]) -> List[List[int]]:
    """Rotate an NxN array by 90 deg in place."""

    if arr == None or arr == [[]]:
        return

    # iterate through layers
    # integer divide = skip middle for n odd
    for layer in range(len(arr) // 2):

        # iterate through each space, skipping last one
        for i in range(len(arr) - (2 * layer) - 1):

            # indices that are repeated
            a = i + layer
            b = (len(arr) - 1) - layer
            c = (len(arr) - 1) - layer - i
            d = layer

            # temp_storage
            top_left = arr[d][a]
            top_right = arr[a][b]
            bot_right = arr[b][c]
            bot_left = arr[c][d]

            # Swap
            arr[d][a] = bot_left
            arr[a][b] = top_left
            arr[b][c] = top_right
            arr[c][d] = bot_right

    return arr


# manual 4 x 4
# layer = [0, 1]
# layer = 0
# i = [0, 1, 2, 3]

# i = 0
# a = 0; b = 3; c = 3; d = 0
# tl = 0, 0; tr = 0, 3; br = 3, 3; bl = 3, 0 OK

# i = 1
# a = 1; b = 3; c = 2; d = 0
# tl = 0, 1; tr = 1, 3; br = 3, 2; bl = 2, 0 OK

# i = 2
# a = 2; b = 3; c = 1; d = 0
# tl = 0, 2; tr = 2, 3; br = 3, 1; bl = 1, 0 OK

# i = 3
# a = 3; b = 3; c = 0; d = 0
# tl = 0, 3; tr = 3, 3; br = 3, 0; bl = 0, 0


# a = i + layer
# b = (len(arr) - 1) - layer
# c = (len(arr) - 1) - layer - i
# d = layer

# top_left = arr[d][a]
# top_right = arr[a][b]
# bot_right = arr[b][c]
# bot_left = arr[c][d]



import unittest

class TestRotate(unittest.TestCase):

    def test_2by2(self):
        arr = [
            [1, 2],
            [1, 2]
        ]

        output = [
            [1, 1],
            [2, 2]
        ]

        self.assertEqual(rotate(arr), output)


    def test_4by4(self):
        arr = [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ]

        output = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [4, 4, 4, 4]
        ]

        self.assertEqual(rotate(arr), output)

    def test_5by5(self):
        arr = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]

        output = [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5]
        ]

        self.assertEqual(rotate(arr), output)

    def test_6by6(self):
        arr = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6]
        ]

        output = [
            [1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6]
        ]

        self.assertEqual(rotate(arr), output)


if __name__ == '__main__':
    unittest.main()


