# all_subsets_of_a_set.py

# Facebook Coding Interview Question and Answer #1: All Subsets of a Set

# https://www.youtube.com/watch?v=bGC2fNALbNU

from typing import List

subsets = []

def all_subsets(given_array: List, subsets: List) -> None:

    subset = [None] * len(given_array)

    helper(given_array, subset, 0, subsets)

    return subsets


def helper(given_array: List, subset: List, i: int, subsets: List) -> None:

    if i == len(given_array):
        print(subset)
        # remove None
        temp_subset = [n for n in subset if n is not None]
        subsets.append(temp_subset)
    else:
        # don't include item
        subset[i] = None
        helper(given_array, subset, i + 1, subsets)
        # include item
        subset[i] = given_array[i]
        helper(given_array, subset, i + 1, subsets)


import unittest

class TestAllSubsets(unittest.TestCase):

    def setUp(self):
        subsets = []

    def test_given_example(self):

        given_array = [1, 2]

        self.assertEqual(
            sorted(all_subsets(given_array, subsets)),
            # [[None, None],[1, None],[None, 2],[1, 2]]
            sorted([[], [1], [2], [1, 2]])
        )


if __name__ == '__main__':
    unittest.main()